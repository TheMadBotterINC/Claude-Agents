---
name: product-workflow-auditor
description: Audit SaaS and internal-app workflows, including onboarding, core journeys, permissions, empty states, admin flows, and product friction.
---

# Product Workflow Auditor

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

Use this skill to evaluate whether users can complete meaningful work, not just whether screens render correctly. It complements `$ux-tester` by focusing on workflow completeness, decision points, and business friction.

## Workflow

1. Read product docs, README, routes, seed/demo data, roles/permissions, nav structure, and domain models.
2. Map target users, core jobs-to-be-done, and the app's primary workflow loops.
3. Exercise or inspect onboarding, first meaningful action, CRUD flows, search/filtering, exports, notifications, admin/support tasks, and account/billing flows when applicable.
4. Check empty, loading, error, permission-denied, destructive-action, and recovery paths.
5. Save the report to `docs/audits/product_workflow_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Users cannot reach or complete a core workflow.
- Missing first-run/onboarding guidance, seed/demo affordances, or activation path.
- Role/permission behavior is confusing, invisible, or blocks legitimate work.
- Destructive actions lack confirmation, undo, audit trail, or recovery.
- Empty/error states fail to tell users what to do next.
- Admin/support/billing flows are incomplete or hard to operate.
- Workflow requires avoidable repeated entry, context switching, or hidden knowledge.

## Reporting Rules

- Group findings by workflow, ordered by business impact.
- For each finding include user goal, current friction, consequence, and concrete product change.
- Distinguish UX polish from workflow/product gaps; route visual-only issues to `$ux-tester`.
- Include quick wins, launch blockers, and deeper product design questions separately.
- Note assumptions when product intent is not documented.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
