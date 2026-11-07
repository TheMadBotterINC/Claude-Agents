---
name: ux-tester
description: Audit a running web app's UX with Playwright across viewports, covering layout, responsiveness, interactions, console, and network issues.
---

# UX Tester

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
