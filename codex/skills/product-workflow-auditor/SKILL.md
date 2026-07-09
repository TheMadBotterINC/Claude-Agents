---
name: product-workflow-auditor
description: Product workflow auditor for SaaS and internal web apps. Use when asked to review onboarding, activation, core user journeys, billing/admin flows, permissions, empty states, destructive actions, support affordances, workflow friction, product completeness, or whether the app's workflows make business sense.
---

# Product Workflow Auditor

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
