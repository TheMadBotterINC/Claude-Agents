---
name: rails-code-quality
description: Rails code quality and conventions reviewer for maintainability-focused audits. Use when asked to review Rails code quality, conventions, architecture, refactoring opportunities, RuboCop/reek results, fat controllers/models, callback abuse, duplication, dead code, service/query/form object boundaries, helpers, views, or test organization.
---

# Rails Code Quality

## Overview

Use this skill to review Rails code structure and maintainability without changing behavior. Respect the project's existing conventions and focus on findings that make the app easier to understand, test, and evolve.

## Operating Principles

- Be exhaustive by default across `app/` and `lib/` unless the user narrows scope.
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
- Architecture: missing service/query/form/value objects, unclear boundaries, feature envy, primitive obsession, deep nesting, long methods, and duplicated workflows.
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

Prefer small, idiomatic moves: extract query objects for reusable relation logic, service objects for orchestration, form objects for multi-model input, presenters/components for view complexity, scopes for composable filtering, and plain value objects where primitives obscure domain meaning. Recommend tests around behavior before risky refactors.
