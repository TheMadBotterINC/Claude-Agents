---
name: audit-orchestrator
description: Coordinate specialist audit skills and consolidate their reports. Use for full-app or multi-domain audits.
---

# Audit Orchestrator

## Overview

Use this skill to coordinate the local audit suite, launch each selected specialist in an isolated `codex exec` run, and produce a single high-signal summary that links back to the detailed reports. This skill manages scope, sequencing, child-run artifact collection, deduplication, and final prioritization; the specialist skills own the deep audit work.

## Available Audit Skills

- `$ux-tester`: browser UX, responsiveness, visual polish, interactions, console/network issues. Dynamic work requires a verified local/dev URL and available browser tools.
- `$product-workflow-auditor`: onboarding, activation, core workflows, empty states, admin/billing/support flows, destructive actions, and product friction.
- `$web-performance`: lab versus field metrics, network weight, assets, hydration, bundle/build output. Dynamic work requires a verified local/dev URL and measurement capabilities.
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

From the installed `audit-orchestrator` skill directory (resolve its actual
location rather than assuming the target app contains this repository):

```bash
python3 scripts/run_audit_suite.py \
  --target /path/to/app \
  --base-url http://localhost:3000 \
  --skills ux-tester,web-performance,rails-security \
  --scope standard \
  --timeout 900 \
  --sandbox workspace-write
```

The runner owns a unique `docs/audits/.orchestrator-runs/<run-id>/` directory.
It durably records `manifest.json`, per-attempt stdout/stderr/final messages,
and reports at `reports/<skill>.md` (retry reports use `<skill>-N.md`).
Children receive exact absolute report/sidecar paths and completed prior reports.
They must treat those prior reports as read-only context, preserve provenance,
and verify reused claims; do not invent cross-child shared memory.

Each attempt writes `<run_dir>/<skill>/attempt-N/result.json` with
`status` (`completed`, `partial`, or `blocked`), `report_path` (the exact assigned
absolute path), and `blockers` (an array of strings). `completed` requires a
nonempty report, matching path, and no blockers. Process exit zero alone is not
completion. Record incomplete coverage as `partial`, not a clean bill of health.
The suite exits nonzero for blocked/partial outcomes; continue consolidation of
usable reports unless `--strict` requests stopping after the first failure.

`--timeout SECONDS` defaults to 900 per child. `--scope` selects
`quick|standard|comprehensive`; it does not choose the specialist subset.
`--resume PATH` resumes a prior run directory using its frozen target, skills,
base URL, model, scope, timeout, and sandbox (only `--strict` may change).
Preserve old attempts/reports and inspect the durable manifest before retrying.
Do not relaunch completed work merely because an unrelated child was blocked.

Use `--dry-run` before execution to validate the Codex CLI and installed selected
skill locations and inspect its validation report/commands without launching
audits. `--skills-dir PATH` provides an explicit lookup override. Dry-run does
not prove browser connectivity, app readiness, safe DB targets, or model access.
Read-only sandbox is rejected because reports need workspace writes; a writable
sandbox is not authorization to modify application code or external systems.

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

Choose depth separately: quick reviews the named path plus its highest-risk
adjacent boundary; standard inventories applicable layers/categories and reviews
risk-prioritized representative paths; comprehensive expands across inventoried
in-scope paths within an agreed concrete time/item budget. Default to standard.
Keep a coverage ledger per skill (reviewed, sampled, deferred, blocked, not
applicable), including tenant/role/engine boundaries. Stop when planned items are
dispositioned or budget is exhausted and report why. No mode/model guarantees
every defect found; sampled or deferred items prevent a claim of full coverage.

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

For subsets, preserve the relative order above. Missing URL blocks UX/performance
dynamic work, not independent static audits; product-workflow can inspect code
without a URL. Preflight actual browser/recording/screenshot capabilities and
offer approved alternatives or static fallback. Never claim unavailable checks
ran or silently configure/install tooling.

## Running The Audit

When running from a target app repo:

1. Infer or confirm the selected skills.
2. Confirm the target directory. Confirm `--base-url` before selecting browser skills.
3. Run the bundled script from this skill directory with the selected skills.
4. Read `manifest.json`, exact per-attempt result sidecars, child final messages,
   and the run's assigned reports, not stale similarly named reports elsewhere.
5. Continue summarization even if unrelated child runs failed; mark blocked/failed children clearly.

Do not run specialist audits in parallel by default. The runner is intentionally sequential to avoid browser/tool contention and make failures easier to diagnose. If the user explicitly asks for parallel work, explain that a later `--parallel` runner mode or separate worktrees would be safer than ad hoc backgrounding.

## Consolidated Output

Save the consolidated summary inside the unique run directory as
`reports/audit_orchestrator_report.md`, preserving any earlier summary on resume
with a unique suffix. Include:

- Scope: selected skills, depth/budget, ledger, skipped skills, assumptions,
  redacted target URL, and target repo/app.
- Execution log: run order, report paths, tools run, and blockers.
- Top findings: one prioritized list across all audits, ordered by business/user risk.
- Cross-cutting themes: duplicates or related findings across UX, performance, security, database, and code quality.
- Suggested sequence of fixes: immediate blockers, high-risk fixes, quick wins, then larger refactors.
- Verification checklist: how to confirm the top fixes after implementation.

In the final response, include only the consolidated report path, selected skills, critical/high findings, and recommended next actions. Avoid dumping every specialist finding into chat.

## Guardrails

- Verify effective local/dev app, DB, and integrations before any dynamic
  execution; localhost does not imply sandboxed services. Production/external DB
  commands, including SELECT/EXPLAIN, require explicit target/action approval.
- EXPLAIN ANALYZE executes queries and may mutate data/call functions or hold
  locks; prefer vetted plain plans, never label all DB inspection read-only.
- Audit permission does not authorize form submissions, deletes, billing,
  uploads, mail, jobs, webhooks, deploys, account mutations, or tool installs.
- Redact secrets/PII/tenant identifiers in screenshots, traces, logs, SQL, and
  network metadata before capture/save/share; avoid collecting full payloads.
- Never modify application code during an audit unless the user explicitly asks for fixes.
- If one audit discovers a blocker that invalidates later measurements, stop the affected later audits and report the dependency.
- Keep Claude agent files untouched; use the Codex skills for orchestration.

## Offline evaluation fixtures

`evals/evals.json` uses inert `references/audit-fixture.json` run metadata for
selection, false completion, prior-report provenance, and resume/preflight
cases. Paths are relative to this installed skill directory. Simulate decisions
only; do not launch children or real audits. Definitions are not model results.
