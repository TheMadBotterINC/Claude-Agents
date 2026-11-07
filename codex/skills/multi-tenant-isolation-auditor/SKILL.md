---
name: multi-tenant-isolation-auditor
description: Audit Rails multi-tenant isolation for scoping gaps, cross-tenant leaks, unsafe jobs, exports, search, and admin overrides.
---

# Multi-Tenant Isolation Auditor

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

Use this skill to find cross-tenant data exposure and tenant-boundary mistakes. Treat tenant isolation as a security and data-integrity concern, not just an authorization style preference.

## Workflow

1. Identify tenancy model: account/org/customer/site models, subdomains, current tenant setters, default scopes, policy scopes, engines, and admin bypasses.
2. Map tenant-owned models, joins, reports, exports, search, background jobs, uploads, notifications, and API endpoints.
3. Review controllers, policies, queries, services, serializers/views, jobs, and mounted engine code for unscoped loads or missing tenant context.
4. Check dangerous patterns: `Model.find(params[:id])`, global search, report queries, exports, cross-tenant admin paths, signed IDs, public IDs, and cached fragments.
5. Save the report to `docs/audits/multi_tenant_isolation_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- User-controlled IDs loaded without tenant/account scoping.
- Policies that authorize access but do not scope records.
- Reports, dashboards, exports, search, or autocomplete leaking other tenants.
- Jobs/mailers/notifications running without tenant context or using stale/global context.
- Mounted engines or customer gems with independent controllers/policies/views that skip host tenant rules.
- Cache keys, ActiveStorage attachments, signed IDs, or public URLs that cross tenant boundaries.
- Admin override paths without audit logging or constrained scope.

## Reporting Rules

- Order findings by leak impact and exploitability.
- For each finding include tenant model, affected path, unscoped query/code location, impact, and exact scoping fix.
- Mark engine/gem findings with the owning layer so fixes land in the right repo.
- Recommend focused regression tests using two tenants and cross-tenant records.
- Redact any real tenant/customer identifiers found during review.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
