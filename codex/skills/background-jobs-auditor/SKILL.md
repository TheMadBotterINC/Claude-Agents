---
name: background-jobs-auditor
description: Audit Rails background jobs and schedulers for queues, retries, idempotency, locking, payloads, and failure handling.
---

# Background Jobs Auditor

## Safety, scope, and evidence contract

- **Audit only.** Do not edit app code/config, autocorrect, install dependencies,
  generate migrations, or apply fixes without explicit implementation approval.
  Default writes are report/evidence artifacts; propose changes in the report.
- **Verify before execution.** Inspect effective app/test environment, hooks,
  DB target, tenant context, and integrations without exposing credentials.
  Localhost is not proof of isolation. Dynamic checks require verified local/dev/
  test targets, synthetic data, and sandboxed services. Production/external DB
  commands (even SELECT/EXPLAIN) require explicit target/action approval.
  Do not submit forms, delete/upload data, charge, send mail, enqueue jobs,
  trigger webhooks, deploy, mutate accounts, or update tools/advisories without
  specific authorization; otherwise continue statically.
- **DB caution.** EXPLAIN ANALYZE executes queries, including writes/functions;
  SELECT can have effects too. Prefer vetted plain EXPLAIN. ANALYZE requires
  bounded reads on approved disposable local/dev data and a timeout, never
  audit-time migrations/backfills.
- **Minimize/redact before capture or sharing.** Exclude secrets, cookies,
  tokens, headers/bodies, SQL binds, tenant identifiers, and PII from screenshots,
  network evidence, traces, and logs. Prefer metadata/synthetic UI; omit unsafe
  artifacts rather than collecting raw sensitive data.
- **Bound scope:** default `standard` inventories applicable categories/layers
  and reviews risk-prioritized representative paths. `quick` covers the named
  path plus its highest-risk adjacent boundary; `comprehensive` expands across
  inventoried in-scope paths within an agreed concrete time/item budget. No
  mode/model guarantees every defect found.
- **Coverage ledger:** record paths/categories/roles/tenants/engines as reviewed,
  sampled, deferred, blocked, or not applicable, with evidence/reasons. Stop when
  planned items are dispositioned or budget expires; disclose gaps/stopping
  reason. Expand only with a new budget/scope.
- **Honest output:** check surrounding controls/consumers before flagging patterns.
  Separate confirmed findings, static risks, and hypotheses; unavailable tools/
  source are coverage gaps. Honor assigned report paths over unique standalone
  defaults; preserve prior reports as context, not fresh evidence. Include
  ledger, environment, commands/failures, evidence, remedy, and status. Write any
  assigned JSON sidecar with `status` (`completed|partial|blocked`), exact absolute
  `report_path`, and `blockers` array. Completed requires planned coverage,
  nonempty matching report, no blockers; incomplete coverage is partial, and
  missing prerequisites preventing meaningful work are blocked.

## Overview

Use this skill to evaluate whether asynchronous work is reliable, observable, idempotent, and safely deployed.

## Workflow

1. Identify queue backend and scheduler: Sidekiq, GoodJob, Solid Queue, DelayedJob, Active Job, Whenever, cron, Heroku Scheduler, or platform jobs.
2. Read job classes, mailers, callbacks that enqueue jobs, service objects, queue config, retry/dead-letter config, and worker deployment config.
3. Check job arguments, serialization, tenant/user scoping, idempotency, locking, retries, timeouts, error handling, and external API behavior.
4. Inspect scheduled tasks for overlap, missed runs, environment assumptions, and safe reentrancy.
5. Save the report to `docs/audits/background_jobs_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Non-idempotent jobs that can double-charge, double-email, duplicate records, or corrupt state on retry.
- Jobs missing tenant/account scoping or authorization-sensitive context.
- Unbounded jobs, large payloads, N+1-heavy jobs, or jobs that can exhaust memory/timeouts.
- Missing retry strategy, dead-job handling, alerts, or failure visibility.
- Scheduled tasks that overlap, run in the wrong environment, or cannot be replayed safely.
- Worker processes or queues missing from deployment config.
- External API jobs lacking timeout, backoff, circuit-breaker, or compensation behavior.

## Reporting Rules

- Order findings by data/business impact and failure likelihood.
- For each finding include job/scheduler location, failure mode, retry/idempotency risk, and concrete fix.
- Recommend tests for risky jobs, especially retry and duplicate-execution behavior.
- Separate deploy/config gaps from code-level job design issues.
- Do not enqueue or execute real jobs against external services without explicit permission.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
