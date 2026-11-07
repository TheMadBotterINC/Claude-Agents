---
name: data-integrity-auditor
description: Audit Rails data integrity across constraints, validations, migrations, transactions, state transitions, and race conditions.
---

# Data Integrity Auditor

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

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
