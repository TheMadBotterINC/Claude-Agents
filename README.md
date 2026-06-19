# claude_agents

A small suite of authored [Claude Code subagents](https://docs.claude.com/en/docs/claude-code/sub-agents)
for testing and tuning local web apps — primarily Ruby on Rails and Astro/JS
front ends.

Each agent lives in its own folder as `<agent>/<agent>.md` (the subagent prompt,
with YAML frontmatter). `install.sh` links them into `~/.claude/agents/` so they
are available in every project.

## Agents

All agents are **exhaustive by default** — they aim for systematic coverage rather
than spot-checks (ask them to narrow scope when you want a quick triage instead).

| Agent | What it does |
| --- | --- |
| **ux_tester** | Detail-obsessed front-end UX tester. Drives Chrome via the Playwright MCP to find visual, layout, responsive, and interaction defects across desktop + mobile, screenshots every issue, and logs JS console errors. |
| **activerecord_performance** | Rails ActiveRecord performance auditor. Finds N+1 queries, missing/redundant indexes, over-fetching, and unbounded queries — statically (code + schema) then dynamically (query logs, Bullet/Prosopite, `EXPLAIN ANALYZE`). |
| **web_performance** | Front-end performance auditor (the client-side counterpart to activerecord_performance). Measures Core Web Vitals / Lighthouse, bundle & asset weight, render-blocking resources, image/font optimization, and Astro island hydration via Playwright MCP + build tooling. |
| **rails_security** | Defensive Rails security auditor. Brakeman + bundler-audit plus manual review for injection, mass assignment, broken auth/authz & IDOR, CSRF, XSS, SSRF, unsafe deserialization, exposed secrets, and insecure session/header config. |
| **rails_code_quality** | Rails code quality & conventions reviewer. RuboCop (+rails/-performance/-rspec) plus manual review for fat controllers/models, missing service objects, callback abuse, smells, duplication, and dead code — respecting existing style. |

## Install

```bash
./install.sh          # symlink each agent into ~/.claude/agents (edits update live)
./install.sh --copy   # copy instead of symlink
./install.sh --list   # show what's installed from this repo
```

After installing, the agents are available to the `Agent`/Task tool in any
project. Claude will auto-delegate based on each agent's `description`, or you can
ask for one by name.

## Playwright MCP (required by ux_tester)

`ux_tester` controls Chrome through the [Playwright MCP](https://github.com/microsoft/playwright-mcp).
This repo includes a project-scoped `.mcp.json`, so it works out of the box when
you run Claude Code **from this repo**.

Because the agents install **globally** but the MCP config here is **project
scoped**, `ux_tester` will only see the browser tools in a project that also has
the Playwright MCP configured. To use it against an app elsewhere, do one of:

- **Make it global (recommended for everyday use):**
  ```bash
  claude mcp add --scope user playwright -- npx @playwright/mcp@latest
  ```
- **Or add it to the target app** by copying `.mcp.json` into that repo's root.

The first run downloads the Playwright browser if needed. The agent always asks
before installing anything.

## Conventions for adding an agent

1. Create `my_agent/my_agent.md`.
2. Start with YAML frontmatter: `name` (must match the folder/file), a precise
   `description` (this is what triggers auto-delegation — include when to use it),
   an optional scoped `tools` allowlist, and `model` (`inherit` by default).
3. Run `./install.sh` to link it.
