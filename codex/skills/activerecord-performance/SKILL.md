---
name: activerecord-performance
description: Audit Rails ActiveRecord performance, including N+1 queries, indexes, slow SQL, over-fetching, and database hot paths.
---

# ActiveRecord Performance

## Safety, scope, and evidence contract

- **Audit, do not implement.** Do not edit application code/configuration, run
  autocorrect, add dependencies, generate migrations on disk, or apply fixes
  unless the user explicitly requests implementation. Suggested patches belong
  in the report. Report/evidence artifacts are the only default writes.
- **Verify the environment before execution.** Inspect start/test commands and
  hooks, effective app environment, database target, tenant context, and external
  integrations without exposing credentials. A localhost URL alone does not
  prove local data or sandboxed services. Dynamic checks require a verified
  local/dev/test target with synthetic data and isolated integrations. Ask for
  explicit target/action approval before any production or external database
  command, even SELECT or EXPLAIN; otherwise continue statically.
- **No implicit side effects.** Audit permission is not permission to submit
  forms, delete records, send mail, charge payments, upload data, enqueue jobs,
  trigger webhooks, deploy, or mutate accounts. Use approved disposable fixtures
  and stubbed services; ask before any action outside that authorization.
  Do not install tools or update remote vulnerability databases silently.
- **Database execution is not automatically read-only.** EXPLAIN ANALYZE executes
  the query, including writes and called functions, and can create load/locks.
  Even SELECT can invoke side-effecting functions. Prefer plain EXPLAIN after
  inspecting the query; use ANALYZE only for vetted bounded reads on approved
  disposable local/dev data with a timeout. Rollback is not protection from
  external effects. Never run migrations/backfills as part of an audit.
- **Minimize sensitive evidence.** Redact secrets, cookies, Authorization headers,
  query-string tokens, request/response bodies, customer/tenant identifiers, PII,
  SQL bind values, screenshots, traces, and logs before saving or sharing. Prefer
  metadata to full payload capture. Use synthetic accounts and mask UI data
  before capture; if safe redaction is unavailable, omit the artifact and report
  the limitation. Never collect raw sensitive data just to redact it later.
- **Choose a bounded scope.** Use `standard` unless the user/runner selects
  `quick` or `comprehensive`. Quick covers the named path and highest-risk
  adjacent boundary; standard inventories relevant layers and reviews each
  applicable category with risk-prioritized representative paths; comprehensive
  expands to all inventoried in-scope paths and boundaries within an agreed
  time/tool budget. Agree a concrete time or item budget at preflight; runner
  timeout is a ceiling, not a claim of coverage. No mode promises all defects
  found, and none assumes a particular model tier.
- **Keep a coverage ledger.** Record each in-scope path/layer/role/tenant/engine
  and applicable category as reviewed, sampled, deferred, blocked, or not
  applicable, with evidence and reasons. Preserve systematic category coverage
  rather than silently skipping hard areas. Stop when every planned ledger item
  is dispositioned or the agreed budget is reached; report remaining items and
  the stopping reason. Expand only with a new explicit budget/scope.
- **Report honestly.** Separate confirmed findings, static-only risks, and
  hypotheses; include location, evidence, impact, and a proportionate remedy.
  Check surrounding authorization, constraints, framework behavior, and actual
  consumers before flagging a pattern. Missing tools/source are coverage gaps,
  not findings. Finish with `completed` only when planned scope is reviewed;
  use `partial` for incomplete coverage and `blocked` when prerequisites prevent
  meaningful work. A clean sampled review is not proof of absence of defects.
- **Portable output.** Honor a runner-provided report path before any default;
  create only that run's report and evidence, never overwrite prior reports.
  Without a runner, use the skill's default report path with a unique suffix.
  Include scope, ledger, commands/tool failures, environment, stopping reason,
  and status in the report and summarize findings in the final response.
  If the runner assigns a JSON result sidecar, write it at that exact path with
  `status` (`completed|partial|blocked`), `report_path` (the assigned absolute
  report path), and `blockers` (string array). Completed requires a nonempty
  matching report and no blockers; prior reports are read-only context, not
  proof that a check ran in this attempt.

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
