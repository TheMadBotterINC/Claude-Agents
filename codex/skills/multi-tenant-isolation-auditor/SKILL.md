---
name: multi-tenant-isolation-auditor
description: Multi-tenant isolation auditor for Rails and white-label apps. Use when asked to review tenant boundaries, cross-tenant data leaks, account scoping, policy scopes, mounted customer engines, admin overrides, background job tenant context, exports, reports, search, IDs, or authorization in multi-tenant systems.
---

# Multi-Tenant Isolation Auditor

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
