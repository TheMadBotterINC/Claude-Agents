---
name: audit-orchestrator
description: Orchestrates multiple local software-business audit skills into isolated codex exec runs and a consolidated report. Use when asked to run all audits, run a full app audit, coordinate UX/performance/security/code-quality/database audits, choose a subset of audit skills, summarize outputs from several audits, or manage sequential runs of specialist audit skills.
---

# Audit Orchestrator

## Overview

Use this skill to coordinate the local audit suite, launch each selected specialist in an isolated `codex exec` run, and produce a single high-signal summary that links back to the detailed reports. This skill manages scope, sequencing, child-run artifact collection, deduplication, and final prioritization; the specialist skills own the deep audit work.

## Available Audit Skills

- `$ux-tester`: browser UX, responsiveness, visual polish, interactions, console/network issues. Requires a running app URL and Playwright MCP.
- `$product-workflow-auditor`: onboarding, activation, core workflows, empty states, admin/billing/support flows, destructive actions, and product friction.
- `$web-performance`: Core Web Vitals, Lighthouse-style metrics, network weight, assets, hydration, bundle/build output. Requires a running app URL and Playwright MCP.
- `$rails-security`: defensive Rails security, auth/authz, IDOR, injection, XSS, CSRF, SSRF, secrets, dependency CVEs, sessions, headers.
- `$multi-tenant-isolation-auditor`: tenant scoping, policy scopes, mounted engines, cross-tenant leaks, exports, search, jobs, and admin overrides.
- `$data-integrity-auditor`: constraints, validations, foreign keys, uniqueness, nullability, enums, state transitions, migrations, and consistency.
- `$activerecord-performance`: Rails database/query performance, N+1s, indexes, over-fetching, unbounded queries, EXPLAIN/query counts.
- `$background-jobs-auditor`: queues, retries, idempotency, scheduled jobs, locking, payloads, dead jobs, and worker deployment.
- `$test-coverage-auditor`: missing regression tests, critical-flow coverage, flaky tests, factories/fixtures, and suite health.
- `$observability-auditor`: logs, metrics, traces, error reporting, alerts, dashboards, audit logs, and production diagnosability.
- `$deployment-readiness`: env vars, credentials, health checks, releases, rollbacks, workers, storage, email, SSL/CDN/cache, and runbooks.
- `$rails-code-quality`: maintainability, Rails conventions, architecture, RuboCop/Reek, fat models/controllers, callbacks, duplication, dead code.

## Runner Script

Prefer the bundled runner instead of running every specialist inside the parent context:

```bash
python codex/skills/audit-orchestrator/scripts/run_audit_suite.py \
  --target /path/to/app \
  --base-url http://localhost:3000 \
  --skills ux-tester,web-performance,rails-security \
  --sandbox workspace-write
```

The runner creates `docs/audits/.orchestrator-runs/<timestamp>/manifest.json` plus per-skill stdout, stderr, and final-message files. Use `--dry-run` to verify selected skills and generated `codex exec` commands without launching child runs. Use `--strict` only when the user wants the suite to stop after the first failed or blocked child run.

## Scope Selection

Infer the subset from the user's language:

- "all", "full audit", "comprehensive", "everything", "launch readiness", or "app audit" -> all available skills.
- "frontend", "polish", "QA", "responsive", "browser", or "UX" -> `$ux-tester`; add `$product-workflow-auditor` for workflow friction and `$web-performance` when speed, metrics, assets, or Lighthouse are mentioned.
- "performance" alone in a Rails app -> ask whether they mean frontend, database, or both unless the context clearly points one way.
- "security", "hardening", "vulnerability", "auth", "tenant", "secrets", or "CVE" -> `$rails-security`.
- "tenant", "multi-tenant", "white-label", "cross-tenant", "customer engine", or "data leak" -> `$multi-tenant-isolation-auditor`; add `$rails-security` when broader app security is also requested.
- "data integrity", "constraints", "foreign keys", "migrations", "state", "enums", "orphaned", or "race condition" -> `$data-integrity-auditor`.
- "database", "queries", "N+1", "indexes", "ActiveRecord", or "slow SQL" -> `$activerecord-performance`.
- "jobs", "queues", "Sidekiq", "GoodJob", "Solid Queue", "cron", "scheduler", "retry", or "idempotency" -> `$background-jobs-auditor`.
- "tests", "coverage", "flaky", "factories", "fixtures", "RSpec", "Minitest", or "regression tests" -> `$test-coverage-auditor`.
- "observability", "logging", "metrics", "Sentry", "alerts", "dashboards", "tracing", or "diagnostics" -> `$observability-auditor`.
- "deploy", "production", "launch readiness", "rollback", "health check", "env vars", "credentials", or "runbook" -> `$deployment-readiness`.
- "workflow", "onboarding", "activation", "billing", "admin", "support", "empty states", or "product friction" -> `$product-workflow-auditor`.
- "quality", "maintainability", "conventions", "refactor", "smells", or "RuboCop" -> `$rails-code-quality`.

If the requested scope is ambiguous and the choice materially affects runtime or required inputs, ask one concise clarification. Otherwise choose the conservative subset and state the assumption.

## Sequencing

Default full-suite order:

1. `$ux-tester` first when a running app URL is available, because visual/browser defects often reveal broken flows and console/network failures.
2. `$product-workflow-auditor` second, using the same route/workflow map to identify product friction.
3. `$web-performance` third, reusing route knowledge from UX/workflow audits where possible.
4. `$rails-security` fourth, before code-quality refactor advice so security fixes remain clearly prioritized.
5. `$multi-tenant-isolation-auditor` fifth, because tenant boundary issues are security-critical and often cross-cut code layers.
6. `$data-integrity-auditor` sixth, before database performance so correctness constraints are not subordinated to speed.
7. `$activerecord-performance` seventh, after routes, hot paths, and data invariants are known.
8. `$background-jobs-auditor` eighth, after data integrity and DB patterns are mapped.
9. `$test-coverage-auditor` ninth, so it can recommend regression tests for earlier audit findings.
10. `$observability-auditor` tenth, so it can cover failure modes discovered by earlier audits.
11. `$deployment-readiness` eleventh, to evaluate whether the app can ship with the discovered operational constraints.
12. `$rails-code-quality` last, so maintainability recommendations can account for security, data, performance, and operational findings without crowding them.

For subsets, preserve the relative order above. If browser skills are requested but the app is not running or no URL is provided, ask for the URL or start command before beginning those skills.

## Running The Audit

When running from a target app repo:

1. Infer or confirm the selected skills.
2. Confirm the target directory. Confirm `--base-url` before selecting browser skills.
3. Run the bundled script from this skill directory with the selected skills.
4. Read the generated `manifest.json`, child final messages, and any specialist reports under `docs/audits/`.
5. Continue summarization even if unrelated child runs failed; mark blocked/failed children clearly.

Do not run specialist audits in parallel by default. The runner is intentionally sequential to avoid browser/tool contention and make failures easier to diagnose. If the user explicitly asks for parallel work, explain that a later `--parallel` runner mode or separate worktrees would be safer than ad hoc backgrounding.

## Consolidated Output

Save a final summary to `docs/audits/audit_orchestrator_report.md`, using a date or scope suffix if needed. Include:

- Scope: selected skills, skipped skills, assumptions, target URL, and target repo/app.
- Execution log: run order, report paths, tools run, and blockers.
- Top findings: one prioritized list across all audits, ordered by business/user risk.
- Cross-cutting themes: duplicates or related findings across UX, performance, security, database, and code quality.
- Suggested sequence of fixes: immediate blockers, high-risk fixes, quick wins, then larger refactors.
- Verification checklist: how to confirm the top fixes after implementation.

In the final response, include only the consolidated report path, selected skills, critical/high findings, and recommended next actions. Avoid dumping every specialist finding into chat.

## Guardrails

- Respect each specialist skill's safety rules, especially Playwright MCP requirements, secret redaction, DB mutation limits, and install approvals.
- Never modify application code during an audit unless the user explicitly asks for fixes.
- If one audit discovers a blocker that invalidates later measurements, stop the affected later audits and report the dependency.
- Keep Claude agent files untouched; use the Codex skills for orchestration.
