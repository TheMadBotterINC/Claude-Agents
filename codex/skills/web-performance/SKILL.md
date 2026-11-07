---
name: web-performance
description: Measure web performance with Playwright, including Core Web Vitals, network and bundle weight, rendering, hydration, images, and fonts.
---

# Web Performance

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
