---
name: test-coverage-auditor
description: Audit Rails and web-app test coverage, regression gaps, flaky tests, factories, critical flows, and suite health.
---

# Test Coverage Auditor

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

Use this skill to identify where the test suite fails to protect important behavior. Prioritize risk-based coverage over raw coverage percentage.

## Workflow

1. Read test setup: `Gemfile`, `spec/`, `test/`, factories/fixtures, system test config, CI config, SimpleCov or coverage settings, and project test docs.
2. Map critical behavior: authentication, authorization, tenancy, billing, data imports/exports, background jobs, destructive actions, integrations, and core product flows.
3. Run or inspect configured tests when practical. Ask before installing tools or running very slow/destructive suites.
4. Compare production code paths to test coverage: controllers/requests, models, policies, services, jobs, views/components, system flows, and JavaScript behavior.
5. Identify flaky or brittle patterns: sleeps, order dependence, external network calls, over-mocking, fragile selectors, global state, shared mutable fixtures, and non-idempotent factories.
6. Save findings to `docs/audits/test_coverage_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Missing tests for auth/authz, tenant isolation, payments, data integrity, imports/exports, and background jobs.
- Audit findings from security, performance, UX, or data integrity that lack regression tests.
- High-risk files with no direct tests or only trivial happy-path tests.
- Slow/flaky tests that reduce trust in CI.
- Factories/fixtures that hide invalid states, create excessive data, or make tests order-dependent.
- System/request gaps around core workflows and user-visible failure states.

## Reporting Rules

- Order findings by risk, not by coverage percentage.
- For each finding include the untested behavior, existing coverage evidence, risk, and the exact test type to add.
- Recommend concrete examples: request spec, model spec, policy spec, job spec, system test, component/view test, or JavaScript/browser test.
- Separate quick regression tests from larger suite architecture improvements.
- Include commands attempted, test runtime observations, and any suites not run.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
