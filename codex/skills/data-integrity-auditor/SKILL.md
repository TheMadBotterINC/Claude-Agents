---
name: data-integrity-auditor
description: Audit Rails data integrity across constraints, validations, migrations, transactions, state transitions, and race conditions.
---

# Data Integrity Auditor

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

Use this skill to find ways the application can create invalid, inconsistent, orphaned, or unrecoverable data. Focus on invariants that should be enforced in the database, application, or both.

## Workflow

1. Read `db/schema.rb` or `structure.sql`, migrations, models, validations, associations, callbacks, enums, state machines, service objects, imports, seeds, and data tasks.
2. Compare model-level expectations with DB constraints: nullability, foreign keys, uniqueness, checks, enums, defaults, and cascade behavior.
3. Inspect writes that span multiple records for transactions, locking, idempotency, and rollback behavior.
4. Review migrations and backfills for safety: locking, reversibility, batching, defaults, data cleanup, and deployment ordering.
5. Save the report to `docs/audits/data_integrity_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Business-critical uniqueness/foreign-key/nullability enforced only in Rails or not at all.
- Race-prone validations without matching unique indexes or locks.
- Orphaned records, unsafe dependent behavior, or missing cascade/nullify decisions.
- Invalid enum/state transitions, stale status columns, or callbacks that leave partial state.
- Multi-record writes without transactions or with external side effects inside transactions.
- Unsafe migrations that lock large tables, rewrite data eagerly, or cannot be rolled back.
- Imports/backfills that can duplicate, skip, or partially apply data.

## Reporting Rules

- Order findings by corruption risk, blast radius, and recovery difficulty.
- For each finding include invariant, current enforcement gap, failure scenario, and concrete fix.
- Recommend exact Rails migration patterns where appropriate, but do not run migrations without permission.
- Include tests to prove the invariant and race condition when relevant.
- Separate data cleanup tasks from schema/code changes.
