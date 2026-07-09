---
name: ux-tester
description: Exhaustive front-end UX tester for running local web apps, especially Rails, Astro, and JavaScript apps. Use when asked to QA, test, review, audit, or polish a web app's UX, layout, responsiveness, visual design, interactions, console health, or front-end behavior across desktop, tablet, and mobile. Requires globally configured Playwright MCP browser tools.
---

# UX Tester

## Overview

Use this skill to drive a real Chrome browser through Playwright MCP and produce a systematic UX audit. Findings must be concrete, reproducible, screenshot-backed, and phrased as actionable fixes in the app's actual framework and design system.

## Required Setup

- Confirm Playwright MCP browser tools are available before starting browser work. If they are unavailable, stop and tell the user to configure the global Playwright MCP server before continuing.
- Confirm the app is running and get the base URL. If the URL is unclear, inspect the repo for likely dev scripts, but ask for the URL instead of assuming a port.
- Do not install packages, add MCP servers, start long-running servers, or change app code without the user's approval unless the current Codex session already permits that exact action.

## Audit Workflow

1. Read the repo first: README, docs, route files, app views/components, package metadata, CSS framework config, and any design or contribution notes.
2. Identify the stack and conventions: Rails ERB/ViewComponent/Hotwire/Stimulus, Astro islands, React/Vue/Svelte, Tailwind, Bootstrap, Bulma, or custom CSS.
3. Map the relevant pages and flows. Default to exhaustive coverage of every key page and user path unless the user explicitly narrows scope.
4. Test desktop at a standard viewport such as 1440x900, then mobile portrait around 390x844 and 360x800, then tablet around 768x1024.
5. For each page, capture the accessibility snapshot, console messages, network failures, and screenshots for any issue.
6. Exercise interactions: navigation, menus, modals, forms, validation, hover, focus, loading, empty, and error states.
7. Save a Markdown report under `docs/audits/ux_tester_report.md`, using a date or scope suffix if that file already exists. Also summarize the highest-impact findings in the final response.

## What To Look For

- Layout defects: overflow, clipping, overlap, unstable widths, broken grids, bad wrapping, missing responsive constraints, and fixed elements covering content.
- Visual polish defects: inconsistent spacing, alignment drift, type scale mismatches, awkward line length, weak hierarchy, low contrast, noisy palettes, unintentional empty space, and broken images.
- Interaction defects: small tap targets, missing focus rings, broken keyboard flow, dead links, confusing validation, janky transitions, layout shift, inaccessible menus, and missing loading/error/empty states.
- Mobile defects: horizontal scroll, truncated labels, unreadable text, unusable nav, hidden calls to action, cramped controls, and content hidden behind sticky bars.
- Front-end health: JavaScript errors and warnings, failed network requests, slow or missing assets, hydration problems, and unexpected browser dialogs.

## Reporting Rules

- No screenshot, no UX finding. Take the screenshot immediately after observing the issue and record the actual path returned by the tool.
- Group findings by page or flow, ordered by Blocker, Major, Minor, then Nitpick.
- For each finding include: page/flow, element, viewport, screenshot path, what is wrong, why it matters, and a concrete suggested fix.
- Include a dedicated Console & Network section with every observed JS error, warning, failed request, and the page where it occurred.
- Attribute findings to the right layer when a Rails host app uses mounted engines or customer gems. If engine source is outside the repo and cannot be inspected, say so.
- Keep the final response concise: lead with blockers/majors and the report path, not every nitpick.

## Quality Bar

Be exhaustive by default and opinionated only when evidence supports it. Match expectations to the app's domain: operational SaaS should feel dense, clear, and repeatable; marketing pages should carry brand and visual impact; admin tools should prioritize scanability and speed. Every recommendation should be specific enough that another engineer can implement it without re-running the audit.
