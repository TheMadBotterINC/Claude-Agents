---
name: web-performance
description: Front-end web performance auditor for Astro, JavaScript apps, and Rails-served front ends. Use when asked to audit, measure, improve, or explain Core Web Vitals, Lighthouse scores, load speed, bundle size, asset weight, render-blocking resources, image/font performance, Astro island hydration, or frontend network waterfalls. Requires globally configured Playwright MCP browser tools.
---

# Web Performance

## Overview

Use this skill to measure browser-facing performance with real evidence: metrics, byte counts, request waterfalls, build output, and screenshots where useful. Do not report performance guesses as findings.

## Required Setup

- Confirm Playwright MCP browser tools are available before browser measurement. If unavailable, stop and ask the user to configure the global Playwright MCP server.
- Confirm the app is running and get the base URL plus key routes. Inspect scripts and routes to suggest a route list, but do not assume a port.
- Ask before installing Lighthouse, adding analyzer packages, running slow production builds, or modifying application code.

## Measurement Workflow

1. Identify the stack: Astro, Vite, webpack, esbuild, Rollup, importmap, jsbundling/cssbundling, Propshaft, Sprockets, Hotwire, or another pipeline.
2. Read `package.json`, bundler configs, Rails asset config, image/font handling, cache/compression settings, and any performance budgets.
3. Measure every key route on desktop and mobile unless the user narrows scope. Capture cold-cache and warm-cache observations when practical.
4. Use browser performance APIs, network requests, console output, screenshots, and Lighthouse/build tooling when available.
5. Inventory transfer size and request count by JavaScript, CSS, image, font, document, and third-party resources.
6. Inspect production build output when approved. For Astro, count hydrated islands and flag unnecessary `client:load` or hydration on static content.
7. Save the report to `docs/audits/web_performance_report.md`, adding a date or scope suffix if needed, and summarize the highest-impact items in the final response.

## Findings To Prioritize

- Core Web Vitals: LCP, CLS, INP or TBT, FCP, TTFB, and route/device variance.
- Network weight: total transfer size, request count, render-blocking CSS/JS, duplicate assets, missing compression, weak caching, and third-party cost.
- JavaScript: oversized bundles, unneeded hydration, missing code splitting, duplicate dependencies, unminified output, and avoidable client work.
- Images: oversized source assets, missing AVIF/WebP, missing responsive `srcset`, missing lazy loading, poor LCP image priority, and layout shift from missing dimensions.
- Fonts: missing `font-display`, unnecessary families/weights, missing preload for critical fonts, and lack of subsetting.
- Rails/frontend integration: slow server-rendered pages, asset pipeline misconfiguration, importmap bloat, Turbo/Stimulus regressions, and heavy engine-provided assets.

## Reporting Rules

- Lead with a metrics table: route, device, LCP, CLS, INP/TBT, FCP, TTFB, transfer size, and request count. Mark unavailable metrics explicitly.
- Order findings by estimated user impact or bytes saved.
- For each finding include the metric evidence, cause, exact file/config/route where possible, and a concrete fix with expected gain.
- Distinguish measured facts from static-only suspicions.
- Attribute findings to host app versus mounted Rails engine/customer gem when assets or views come from outside the host repo.
- Keep the final response concise and include the report path plus the biggest wins.

## Guardrails

Do not promise production Core Web Vitals from local-only measurements. Do not recommend broad rewrites when a smaller asset, caching, image, or hydration fix addresses the measured problem. Do not mutate the app while auditing unless the user asks for implementation after seeing the findings.
