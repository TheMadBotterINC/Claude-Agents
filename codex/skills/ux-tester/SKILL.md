---
name: ux-tester
description: Audit a running web app's UX with Playwright across viewports, covering layout, responsiveness, interactions, console, and network issues.
---

# UX Tester

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

Use this skill to drive an available authorized browser integration and produce a systematic UX audit. Findings must be concrete, reproducible, evidence-backed, and phrased as actionable fixes in the app's actual framework and design system.

## Required Setup

- Preflight browser navigation, screenshots, viewport controls, accessibility snapshots, console/network metadata, and traces. Prefer configured Playwright MCP; use an approved available alternative if present. If absent, continue static review and mark browser verification blocked/deferred. Do not silently install or configure tools.
- Confirm the app is running and get the base URL. If the URL is unclear, inspect the repo for likely dev scripts, but ask for the URL instead of assuming a port.
- Do not install packages, add MCP servers, start long-running servers, or change app code without the user's approval unless the current Codex session already permits that exact action.

## Audit Workflow

1. Read the repo first: README, docs, route files, app views/components, package metadata, CSS framework config, and any design or contribution notes.
2. Identify the stack and conventions: Rails ERB/ViewComponent/Hotwire/Stimulus, Astro islands, React/Vue/Svelte, Tailwind, Bootstrap, Bulma, or custom CSS.
3. Map the relevant pages and flows. Use the selected scope and coverage ledger; enumerate routes, roles, and engine boundaries before sampling.
4. Test desktop at a standard viewport such as 1440x900, then mobile portrait around 390x844 and 360x800, then tablet around 768x1024.
5. For each selected page, capture redacted accessibility/console/network metadata and suitable defect evidence. Avoid full request headers/bodies and sensitive traces.
6. Exercise non-mutating navigation, menus, keyboard/focus, hover, and UI states. Submit forms or run CRUD/billing/export/upload actions only with explicit action authorization on disposable data with isolated services; otherwise inspect statically and mark execution deferred.
7. Save a Markdown report under `docs/audits/ux_tester_report.md`, using a date or scope suffix if that file already exists. Also summarize the highest-impact findings in the final response.

## What To Look For

- Layout defects: overflow, clipping, overlap, unstable widths, broken grids, bad wrapping, missing responsive constraints, and fixed elements covering content.
- Visual polish defects: inconsistent spacing, alignment drift, type scale mismatches, awkward line length, weak hierarchy, low contrast, noisy palettes, unintentional empty space, and broken images.
- Interaction defects: small tap targets, missing focus rings, broken keyboard flow, dead links, confusing validation, janky transitions, layout shift, inaccessible menus, and missing loading/error/empty states.
- Mobile defects: horizontal scroll, truncated labels, unreadable text, unusable nav, hidden calls to action, cramped controls, and content hidden behind sticky bars.
- Front-end health: JavaScript errors and warnings, failed network requests, slow or missing assets, hydration problems, and unexpected browser dialogs.

## Reporting Rules

- Screenshots are mandatory for visual/layout defects only: mask sensitive UI data before capture, identify the element/viewport, and record the actual tool artifact reference. If unavailable, defer visual conclusions and report the capability gap. Behavioral/accessibility findings may instead use reproduction steps, traces, accessibility snapshots, or redacted logs.
- Group findings by page or flow, ordered by Blocker, Major, Minor, then Nitpick.
- For each finding include: page/flow, element, viewport, evidence reference and reproduction steps, what is wrong, why it matters, and a concrete suggested fix.
- Include a redacted Console & Network section grouped by page, relevance, and reproducibility; deduplicate noise rather than treating every third-party warning as an app defect.
- Attribute findings to the right layer when a Rails host app uses mounted engines or customer gems. If engine source is outside the repo and cannot be inspected, say so.
- Keep the final response concise: lead with blockers/majors and the report path, not every nitpick.

## Quality Bar

Be systematic within the declared scope and opinionated only when evidence supports it. Match expectations to the app's domain: operational SaaS should feel dense, clear, and repeatable; marketing pages should carry brand and visual impact; admin tools should prioritize scanability and speed. Every recommendation should be specific enough that another engineer can implement it without re-running the audit.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
