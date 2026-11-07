---
name: web-performance
description: Measure web performance with Playwright, including Core Web Vitals, network and bundle weight, rendering, hydration, images, and fonts.
---

# Web Performance

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

Use this skill to measure browser-facing performance with real evidence: metrics, byte counts, request waterfalls, build output, and screenshots where useful. Do not report performance guesses as findings.

## Required Setup

- Preflight browser/performance APIs, network metadata, Lighthouse, and build capabilities. Prefer configured Playwright MCP; use an approved available alternative if present. If unavailable, continue static build/config review, mark dynamic/field metrics unavailable, and ask only when the missing capability blocks the requested scope. Do not silently install tooling.
- Confirm the app is running and get the base URL plus key routes. Inspect scripts and routes to suggest a route list, but do not assume a port.
- Ask before installing Lighthouse, adding analyzer packages, running slow production builds, or modifying application code.

## Measurement Workflow

1. Identify the stack: Astro, Vite, webpack, esbuild, Rollup, importmap, jsbundling/cssbundling, Propshaft, Sprockets, Hotwire, or another pipeline.
2. Read `package.json`, bundler configs, Rails asset config, image/font handling, cache/compression settings, and any performance budgets.
3. Measure the ledger-selected routes on desktop and mobile within the selected scope. Capture cold-cache and warm-cache observations when practical.
4. Use browser performance APIs, redacted network timing/size/cache metadata, console output, and approved Lighthouse/build tools. Avoid full request/response headers/bodies. Record tool/version, route, build mode, dataset, viewport/device, CPU/network throttling, cache state, and server conditions. Repeat at least three comparable runs per selected condition; report individual values, median, and range. Separate cold/warm cache; budget-limited single runs are preliminary.
5. Inventory transfer size and request count by JavaScript, CSS, image, font, document, and third-party resources.
6. Inspect production build output when approved. For Astro, count hydrated islands and flag unnecessary `client:load` or hydration on static content.
7. Save the report to `docs/audits/web_performance_report.md`, adding a date or scope suffix if needed, and summarize the highest-impact items in the final response.

## Findings To Prioritize

- Core Web Vitals are LCP, CLS, and INP. Lighthouse is lab data; TBT is a diagnostic, not INP or a replacement for field INP. FCP/TTFB are additional diagnostics. Label scripted interaction INP as lab-observed, not representative field data. Use existing authorized RUM/CrUX with source/time window for field claims; otherwise mark field metrics unavailable.
- Network weight: total transfer size, request count, render-blocking CSS/JS, duplicate assets, missing compression, weak caching, and third-party cost.
- JavaScript: oversized bundles, unneeded hydration, missing code splitting, duplicate dependencies, unminified output, and avoidable client work.
- Images: measured oversized assets, responsive `srcset`, dimensions, decoding, and priority. Lazy-load below-the-fold images, not above-the-fold/LCP hero images: eager loading and fetch priority may be correct. Missing optimization attributes alone are not findings.
- Fonts: missing `font-display`, unnecessary families/weights, missing preload for critical fonts, and lack of subsetting.
- Rails/frontend integration: slow server-rendered pages, asset pipeline misconfiguration, importmap bloat, Turbo/Stimulus regressions, and heavy engine-provided assets.

## Reporting Rules

- Lead with metrics separating lab LCP/CLS/TBT/FCP/TTFB/transfer/request count from available field LCP/CLS/INP with source/period. Include conditions, individual runs, median/range, and explicitly unavailable metrics.
- Order findings by estimated user impact or bytes saved.
- For each finding include metric evidence, cause, exact file/config/route where possible, and a concrete fix. Label expected gains as estimates until verified by repeated comparable before/after runs following explicitly authorized implementation.
- Distinguish measured facts from static-only suspicions.
- Attribute findings to host app versus mounted Rails engine/customer gem when assets or views come from outside the host repo.
- Keep the final response concise and include the report path plus the biggest wins.

## Guardrails

Do not promise production Core Web Vitals from local-only measurements. Do not recommend broad rewrites when a smaller asset, caching, image, or hydration fix addresses the measured problem. Do not mutate the app while auditing unless the user asks for implementation after seeing the findings.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
