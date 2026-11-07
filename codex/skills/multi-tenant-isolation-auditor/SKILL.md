---
name: multi-tenant-isolation-auditor
description: Audit Rails multi-tenant isolation for scoping gaps, cross-tenant leaks, unsafe jobs, exports, search, and admin overrides.
---

# Multi-Tenant Isolation Auditor

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
