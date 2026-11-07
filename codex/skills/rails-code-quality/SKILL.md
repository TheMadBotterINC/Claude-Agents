---
name: rails-code-quality
description: Review Rails maintainability and conventions across architecture, controllers, models, callbacks, duplication, analyzers, and test organization.
---

# Rails Code Quality

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

Use this skill to review Rails code structure and maintainability without changing behavior. Respect the project's existing conventions and focus on findings that make the app easier to understand, test, and evolve.

## Operating Principles

- Read local conventions before judging code: `.rubocop.yml`, `.standard.yml`, `.reek.yml`, `CLAUDE.md`, `AGENTS.md`, README, docs, and surrounding examples.
- Do not impose a foreign architecture when the project has a coherent existing pattern.
- Separate maintainability findings from security and DB performance findings; mention those only enough to route them to the right audit.
- Ask before installing gems, modifying the Gemfile, or running autocorrect.
- Attribute findings to the host app or the correct mounted Rails engine/customer gem.

## Review Workflow

1. Map the app structure: models, controllers, jobs, mailers, services, queries, forms, presenters, concerns, helpers, views, and tests.
2. Identify configured tools: RuboCop, rubocop-rails, rubocop-performance, rubocop-rspec, Standard, Reek, Rails Best Practices, or custom scripts.
3. Run configured analyzers when available and approved by the current environment. Summarize automated output by category and autocorrectability.
4. Manually inspect each layer for structural problems, duplicated concepts, inconsistent boundaries, and patterns that fight the app's conventions.
5. Save the report to `docs/audits/rails_code_quality_report.md`, using a date or scope suffix if needed.

## Findings To Look For

- Controllers: fat actions, business logic, repeated filters, too many instance variables, non-RESTful sprawl, and inconsistent response handling.
- Models: god objects, validation/scope sprawl, callback side effects, external calls in callbacks, concern overuse, and misplaced orchestration.
- Architecture: unclear ownership, coupled effects, feature envy, primitive obsession, deep nesting, and duplicated business rules. Missing service/query/form/value objects is not itself a finding; establish the concrete maintenance problem first.
- Views/helpers: complex template logic, helper bloat, missing partial/component boundaries, repeated markup, and presentation logic in models.
- Jobs/services: unclear command/query split, hidden side effects, poor naming, weak error handling, and hard-to-test collaborators.
- General hygiene: dead code, stale TODOs, commented-out code, magic strings/numbers, broad `rescue`, inconsistent naming, and tests that encode implementation trivia.

## Reporting Rules

- Order findings by maintainability impact, not by linter volume.
- For each finding include location, smell/violation, why it matters in this app, and a concrete refactor sized for action.
- Summarize analyzer tallies separately so cop noise does not crowd out structural review.
- Call out conventions that are healthy and should be preserved when relevant to proposed refactors.
- Clearly mark broad refactor ideas as such; do not present them as required fixes when risk or scope is high.
- Keep the final response focused on the most valuable refactors and include the report path.

## Refactor Guidance

Prefer the smallest idiomatic change that resolves a demonstrated problem. A model method, scope, or direct controller action may be enough; extract query/service/form/presenter/value objects only when reuse, effects, domain clarity, or testability justify that boundary. Recommend behavior tests before risky refactors. Before renaming/removing methods or actions, check routes, partials, engine/host consumers, jobs, external APIs, and rolling deployment compatibility.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
