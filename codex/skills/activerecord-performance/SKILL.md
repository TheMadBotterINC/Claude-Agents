---
name: activerecord-performance
description: Audit Rails ActiveRecord performance, including N+1 queries, indexes, slow SQL, over-fetching, and database hot paths.
---

# ActiveRecord Performance

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

Use this skill to find and prove Rails database performance problems. Every reported issue needs evidence: a file location, schema fact, query count, SQL sample, EXPLAIN output, or measured before/after behavior.

## Guardrails

- Work in two passes: static code/schema analysis first, then dynamic confirmation where practical.
- Prefer static review and redacted existing logs; inspect queries before plain `EXPLAIN`. `EXPLAIN ANALYZE` executes the query and requires the safety contract's local/dev and bounded-read checks.
- Do not run migrations, mutate real data, add gems, or modify the Gemfile without explicit user approval.
- If a production or external database might be involved, stop and ask before running any DB command.
- Attribute findings to the host app or the correct mounted Rails engine/customer gem. If engine source is outside the repo and unavailable, report that gap.

## Static Pass

1. Read `Gemfile`, `Gemfile.lock`, `config/database.yml`, `db/schema.rb` or `structure.sql`, models, controllers, jobs, serializers, views, decorators, and query/service objects.
2. Note Rails version, DB adapter, pagination approach, and whether Bullet, Prosopite, rack-mini-profiler, Marginalia, or strict loading are present.
3. Cross-reference associations, foreign keys, common `where`/`order`/`group` shapes, and schema indexes.
4. Search for N+1 patterns: association access inside loops, collection partials, serializers touching associations, per-row counts, and missing `includes`/`preload`.
5. Search for inefficient usage: `.count` in loops, `.present?` loading records, `.all` then Ruby filtering, missing limits, row-by-row updates, over-fetching full records, callback-heavy persistence, and risky `default_scope`.

## Dynamic Pass

1. Confirm how to boot the app, run console/runner, and exercise key paths. Ask for base URL or credentials when needed.
2. Use existing tooling first: logs, Bullet, Prosopite, rack-mini-profiler, request specs, or local scripts.
3. As a no-gem fallback, use ActiveSupport notifications or SQL logs to count queries for focused actions.
4. Capture actual SQL for the worst offenders and run EXPLAIN on heavyweight queries when safe.
5. Re-measure after a proposed small code change only when the user asked for implementation and the change is in scope.

## Reporting Rules

- Save the report to `docs/audits/activerecord_performance_report.md`, using a date or scope suffix if needed.
- Order findings by estimated impact: queries saved, rows avoided, latency reduced, or risk removed.
- For each finding include location, query shape, problem class, evidence, concrete Rails fix, and expected improvement.
- Mark static-only findings clearly when dynamic confirmation was not possible.
- Suggest exact migrations or code changes, but do not run migrations unless the user explicitly asks.
- Include a short section for tool coverage: what ran, what failed, and what could not be measured.

## Common Fix Patterns

Prefer idiomatic Rails fixes: `includes`/`preload`/`eager_load`, `counter_cache`, scoped association preloading, `exists?`, `pluck`/`pick`/`select`, pagination/limits, and `find_each`/`in_batches`. Bulk writes can bypass validations, callbacks, timestamps, and tenant/authorization rules; verify those semantics before suggesting them. Recommend composite/unique indexes only after checking query shape, selectivity, tenant keys, existing coverage, and write cost. Sequential scans are not inherently defects.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
