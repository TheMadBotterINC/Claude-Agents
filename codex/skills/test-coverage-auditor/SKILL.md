---
name: test-coverage-auditor
description: Test coverage and suite-health auditor for Rails and web apps. Use when asked to review test coverage, missing regression tests, flaky tests, slow tests, brittle mocks, factory/fixture health, system/request/model coverage, critical-flow coverage, or whether audit findings are protected by tests.
---

# Test Coverage Auditor

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
