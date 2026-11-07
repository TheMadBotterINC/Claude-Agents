---
name: rails-code-quality
description: Review Rails maintainability and conventions across architecture, controllers, models, callbacks, duplication, analyzers, and test organization.
---

# Rails Code Quality

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
