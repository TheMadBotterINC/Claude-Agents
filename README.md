# claude_agents

A small suite of authored [Claude Code subagents](https://docs.claude.com/en/docs/claude-code/sub-agents)
for testing and tuning local web apps — primarily Ruby on Rails and Astro/JS
front ends.

**License:** Apache-2.0 (see [LICENSE](LICENSE)).

Each agent lives in its own folder as `<agent>/<agent>.md` (the subagent prompt,
with YAML frontmatter). `install.sh` links them into `~/.claude/agents/` so they
are available in every project.

## Agents

All agents are **exhaustive by default** — they aim for systematic coverage rather
than spot-checks (ask them to narrow scope when you want a quick triage instead).

| Agent | What it does |
| --- | --- |
| **ux_tester** | Detail-obsessed front-end UX tester. Drives Chrome via the Playwright MCP to find visual, layout, responsive, and interaction defects across desktop + mobile, screenshots every issue, and writes a reproducible report. |
| **activerecord_performance** | Rails ActiveRecord performance auditor. Finds N+1 queries, missing/redundant indexes, over-fetching, and unbounded queries — statically (code + schema) then dynamically with logs/EXPLAIN where available. |
| **web_performance** | Front-end performance auditor (the client-side counterpart to activerecord_performance). Measures Core Web Vitals / Lighthouse, bundle & asset weight, render-blocking resources, cache policy, and image/font efficiency. |
| **rails_security** | Defensive Rails security auditor. Brakeman + bundler-audit plus manual review for injection, mass assignment, broken auth/authz & IDOR, CSRF, XSS, SSRF, unsafe deserialization, and secrets handling. |
| **rails_code_quality** | Rails code quality & conventions reviewer. RuboCop (+rails/-performance/-rspec) plus manual review for fat controllers/models, missing service objects, callback abuse, slim test coverage, and maintainability risks. |

## Skills

Alongside the subagents, `skills/` holds [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)
that load into the main coding loop (a subagent can't change how the main agent
writes code — a skill can).

| Skill | What it does |
| --- | --- |
| **thought-thru-architecture** | Design-first coding discipline. Forces a design pass before the first edit (read for shape, pick the altitude, reuse before invention), bans the usual over-engineering moves while coding (defensive wrapping, compat shims, speculative knobs, grab-bag classes), and ends with a shrink pass over the diff. Includes before/after vignettes for larger features. |

Codex-native skills live under `codex/skills/` and include Codex interface metadata.
The collection includes 47 MIT-licensed marketing skills adapted from
[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills);
the pinned source revision and license are recorded in `codex/vendor/marketingskills/`.

## Install

```bash
./install.sh          # symlink Claude agents/skills and Codex skills
./install.sh --copy   # copy instead of symlink
./install.sh --list   # show what's installed from this repo
```

After installing, the Claude agents are available to the `Agent`/Task tool in
any project, and the Codex skills are discovered when the next Codex session or
turn starts. Claude will auto-delegate based on each agent's `description`, or
you can ask for one by name.

## Where reports go

By default each agent writes its findings to **`docs/audits/`** under the project
being audited (e.g. `docs/audits/rails_security_report.md`), creating the directory
if it doesn't exist, and also returns a summary in its final message. These are
local artifacts — add `/docs/audits/` to the target project's `.gitignore`. When
auditing a mounted engine / customer gem (whose source lives outside the host
repo), the report is written into the **host** app's `docs/audits/` with a
`gem_`-prefixed filename.

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
