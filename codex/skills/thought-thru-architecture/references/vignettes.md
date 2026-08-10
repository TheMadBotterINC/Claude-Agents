# Vignettes: the failure modes, concretely

Two before/after pairs. The "before" versions are not strawmen — they are the
default output shape when coding without a design pass. Study the *deltas*,
not the domains.

## Vignette 1 — adding retries to an API call (Ruby)

Task: `SyncCustomerJob` sometimes fails because the billing API times out.
Add retries.

### Before: new machinery for a one-site problem

```ruby
# app/lib/retry_policy.rb
class RetryPolicy
  DEFAULT_MAX_ATTEMPTS = 3
  DEFAULT_BACKOFF = 2

  def initialize(max_attempts: DEFAULT_MAX_ATTEMPTS, backoff: DEFAULT_BACKOFF,
                 retryable_errors: [StandardError], logger: Rails.logger)
    @max_attempts = max_attempts
    @backoff = backoff
    @retryable_errors = retryable_errors
    @logger = logger
  end

  def call
    attempts = 0
    begin
      attempts += 1
      yield
    rescue *@retryable_errors => e
      @logger.warn("Retry #{attempts}/#{@max_attempts}: #{e.message}")
      if attempts < @max_attempts
        sleep(@backoff**attempts)
        retry
      end
      nil # give callers a safe fallback
    end
  end
end

# app/lib/retryable_billing_client.rb
class RetryableBillingClient
  def initialize(client: BillingClient.new, policy: RetryPolicy.new)
    @client = client
    @policy = policy
  end

  def fetch_customer(id)
    @policy.call { @client.fetch_customer(id) }
  end
end

# Kept for backwards compatibility
BillingApiClient = RetryableBillingClient
```

What went wrong, item by item:

- **Wrong altitude.** One call site needed retries; the fix invented a reusable
  policy object, a wrapper class, and five knobs with one caller each.
- **Masked failure.** `nil # give callers a safe fallback` converts a timeout
  into a `NoMethodError` three frames downstream, or worse, a silent no-op.
- **Retries `StandardError`** — including bugs that will never succeed on
  attempt 2.
- **Compat alias nobody asked for.** Nothing referenced `BillingApiClient`.
- **Ignored the platform.** This is a job; the job framework already owns
  retry.

### After: use the seam the codebase already has

```ruby
# app/jobs/sync_customer_job.rb
class SyncCustomerJob < ApplicationJob
  retry_on BillingClient::TimeoutError, wait: :polynomially_longer, attempts: 3
  ...
end
```

One line, at the boundary that already owns failure handling, retrying only
the error that is actually transient, and still loud after the last attempt.
The design pass finds this because step 1 is *read for shape first* — the
codebase already had a place for this problem.

## Vignette 2 — one caller needs a variant (TypeScript)

Task: `formatDuration(ms)` renders `"2h 14m"`. The report page needs seconds
included for durations under a minute.

### Before: flexibility on spec

```typescript
interface FormatDurationOptions {
  includeSeconds?: boolean;
  secondsThresholdMs?: number;
  locale?: string;          // might need i18n later
  compact?: boolean;        // reserved for future use
}

export function formatDuration(
  ms: number,
  options: FormatDurationOptions = {},
): string {
  const {
    includeSeconds = false,
    secondsThresholdMs = 60_000,
    compact = false,
  } = options;
  try {
    // ... branches for every option ...
  } catch {
    return "--"; // never break the UI
  }
}

/** @deprecated use formatDuration with options */
export const formatDurationLegacy = formatDuration;
```

The deltas: two knobs with zero callers (`locale`, `compact`), a threshold
parameter no one asked to tune, a catch-all that turns any future bug into a
silent `"--"`, a deprecation alias for a function whose signature didn't even
break, and a comment (`reserved for future use`) narrating the speculation.

### After: the second-caller rule

```typescript
export function formatDuration(ms: number): string {
  if (ms < 60_000) return `${Math.round(ms / 1000)}s`;
  // ... existing hours/minutes logic unchanged ...
}
```

Reading the call sites first shows every caller *wants* sub-minute durations
to say `"5s"` rather than `"0m"` — the variant was actually a bug fix at the
existing altitude. No options object exists until a second caller genuinely
diverges, and if one ever does, *that* diff is where the parameter earns its
place.
