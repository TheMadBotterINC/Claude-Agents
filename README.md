# claude_agents

A small suite of authored [Claude Code subagents](https://docs.claude.com/en/docs/claude-code/sub-agents)
for testing and tuning local web apps — primarily Ruby on Rails and Astro/JS
front ends.

**License:** Apache-2.0 (see [LICENSE](LICENSE)).

Each agent lives in its own folder as `<agent>/<agent>.md` (the subagent prompt,
with YAML frontmatter). `install.sh` links them into `~/.claude/agents/` so they
are available in every project.

## Agents

Audit agents use bounded, systematic coverage rather than claiming every defect
has been found. Choose **quick** (named path plus its highest-risk boundary),
**standard** (default: relevant categories and risk-prioritized paths), or
**comprehensive** (all inventoried in-scope paths within an agreed budget).
Reports include a coverage ledger, limitations, and a stopping reason.
Audits recommend fixes; implementation requires a separate explicit request.

| Agent | What it does |
| --- | --- |
| **ux_tester** | Front-end UX tester. Uses available browser tools across desktop/mobile, screenshots visual defects, and captures reproducible behavioral/accessibility evidence. |
| **activerecord_performance** | Rails ActiveRecord performance auditor. Finds N+1 queries, missing/redundant indexes, over-fetching, and unbounded queries — statically (code + schema) then dynamically with logs/EXPLAIN where available. |
| **web_performance** | Front-end performance auditor (the client-side counterpart to activerecord_performance). Measures Core Web Vitals / Lighthouse, bundle & asset weight, render-blocking resources, cache policy, and image/font efficiency. |
| **rails_security** | Defensive Rails security auditor. Brakeman + bundler-audit plus manual review for injection, mass assignment, broken auth/authz & IDOR, CSRF, XSS, SSRF, unsafe deserialization, and secrets handling. |
| **rails_code_quality** | Rails conventions reviewer. RuboCop (+rails/-performance/-rspec) plus evidence-driven review of tangled responsibilities, callbacks, duplication, test gaps, and maintainability risks. |
| **demo_recorder** | Records a narrated product demo video from a written scene-by-scene script (numbered UI steps + quoted narration, e.g. a `DEMO_SCRIPT.md`). Drives Chrome via the Playwright MCP, captions each scene as an on-screen chapter card (it can't voice narration), and writes a timing sheet for optional voiceover dubbing. |

## Skills

Alongside the subagents, `skills/` holds [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)
that load into the main coding loop (a subagent can't change how the main agent
writes code — a skill can).

| Skill | What it does |
| --- | --- |
| **thought-thru-architecture** | Risk-scaled design discipline: reuse existing patterns, preserve real compatibility contracts and tenant boundaries, justify abstractions, and shrink the final diff. Includes concrete before/after vignettes. |

Codex-native skills live under `codex/skills/` and include Codex interface metadata.
The collection includes 47 MIT-licensed marketing skills adapted from
[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills);
the pinned source revision and license are recorded in `codex/vendor/marketingskills/`.

## Install

Requires Python 3.10+ and Bash. Installation is local only; it does not configure
MCP servers or install runtime tools.

```bash
./install.sh          # symlink Claude agents/skills and Codex skills
./install.sh --copy   # copy instead of symlink
./install.sh --list   # show what's installed from this repo
```

`--list` never creates files or directories. Install/update preflights every
destination and refuses unrelated files, foreign symlinks, and locally modified
copies before making changes. Existing links to this checkout are recognized.
Copied installs are tracked by hashes in
`~/.claude/.claude-agents-install.json`; do not delete that receipt if you want
future updates to recognize managed copies. Legacy copies without a receipt are
treated as unmanaged: move them aside yourself before reinstalling.
Switching between link/copy modes does not write through old symlinks.
Set an absolute `CODEX_HOME` to select another Codex installation directory.

After installing, the Claude agents are available to the `Agent`/Task tool in
any project, and the Codex skills are discovered when the next Codex session or
turn starts. Claude will auto-delegate based on each agent's `description`, or
you can ask for one by name.

## Where reports go

By default each audit agent writes findings to **`docs/audits/`** under the project
being audited (e.g. `docs/audits/rails_security_report.md`), creating the directory
if it doesn't exist, and also returns a summary in its final message. These are
local artifacts — add `/docs/audits/` to the target project's `.gitignore`. When
auditing a mounted engine / customer gem (whose source lives outside the host
repo), the report is written into the **host** app's `docs/audits/` with a
`gem_`-prefixed filename.

The detailed location/collision/mounted-engine rules live in
[`shared/audit-conventions.md`](shared/audit-conventions.md), which `install.sh`
links to `~/.claude/audit-conventions.md` — each audit agent reads it rather than
needing the long rationale inline. Critical safety, scope, and evidence rules
remain self-contained so missing shared files do not silently remove safeguards.

Dynamic work requires verification of the app environment, database, and external
integrations; a localhost URL is not proof of isolated data/services. Production
or external DB commands need explicit target/action approval, even for SELECT or
EXPLAIN. `EXPLAIN ANALYZE` actually executes the query. Browser audits do not
implicitly authorize submissions, deletion, mail, billing, uploads, or jobs.
Use disposable synthetic fixtures and redact sensitive evidence before capture.

## Codex audit runner

The orchestrator runs specialists sequentially, avoiding browser contention and
passing earlier reports explicitly to later specialists. From this checkout:

```bash
python3 codex/skills/audit-orchestrator/scripts/run_audit_suite.py \
  --target /absolute/path/to/app \
  --skills rails-security,multi-tenant-isolation-auditor,test-coverage-auditor \
  --scope standard --timeout 900 --dry-run
```

Install the skills and ensure `codex` is on PATH first. Preflight searches the
target's `.agents/skills` and `.codex/skills`, then `~/.agents/skills` and
`${CODEX_HOME:-~/.codex}/skills`. `--skills-dir PATH` selects an explicit skill
directory; that exact skill path is passed to each child.
Dry-run writes its manifest and commands but launches no model/audit. It checks
CLI/skill presence, not authentication, browser connectivity, or app readiness.
Remove `--dry-run` to execute. Add `--base-url http://localhost:3000` for browser
UX/performance audits; workflow auditing can inspect source without a URL.
Do not put credentials or tokens in the URL.

Each run has a unique `docs/audits/.orchestrator-runs/<run-id>/` directory inside
the target workspace, containing an atomically updated `manifest.json`,
per-attempt logs/results, and `reports/`. Keep these artifacts private; raw child
output may contain sensitive information despite redaction instructions.
Children use `codex exec --ephemeral` so these isolated runs do not create
persistent Codex sessions; the run artifacts remain available for review/resume.
An existing run directory is never overwritten. Exit zero requires verified,
nonempty reports and valid `completed` sidecars (or successful dry-run preflight).
Partial, blocked, timed-out, or failed audits return nonzero; `--strict` stops
the suite at the first such outcome.

Resume an interrupted/partial run using its directory:

```bash
python3 codex/skills/audit-orchestrator/scripts/run_audit_suite.py \
  --resume /absolute/path/to/app/docs/audits/.orchestrator-runs/RUN_ID
```

Resume preserves attempts and skips verified completed reports whose upstream
handoffs are unchanged. Rerunning an upstream audit invalidates dependent
handoffs. Target, subset, URL, model, scope, timeout, and sandbox are frozen for
that run; start a new run to change them. Read-only sandbox is unsuitable because
reports require workspace writes. Workspace-write is not permission to edit the
application. The runner validates artifacts, not the truth of model findings;
review evidence and the coverage ledger before acting.

`demo_recorder` isn't an audit agent, so it doesn't use those conventions — it
writes its video and timing-sheet report to **`docs/demos/`** instead. Add that
to the target project's `.gitignore` too.

## Playwright MCP and browser capabilities

`ux_tester`, `web_performance`, and `demo_recorder` prefer Chrome through the
[Playwright MCP](https://github.com/microsoft/playwright-mcp).
This repo includes a project-scoped `.mcp.json`, so it works out of the box when
you run Claude Code **from this repo**. It passes `--caps=devtools` so `ux_tester`
can highlight the flagged element before each screenshot, and `demo_recorder` can
record/chapter video — drop that flag and those tools just won't be available.
Preflight actual capabilities rather than assuming tool names are stable.
Audit skills can report static-only coverage when browser tools are missing;
recording requires a working recorder and cannot be replaced by a pretend take.

Because the agents install **globally** but the MCP config here is **project
scoped**, these agents will only see the browser tools in a project that also has
the Playwright MCP configured. To use them against an app elsewhere, do one of:

- **Make it global (recommended for everyday use):**
  ```bash
  claude mcp add --scope user playwright -- npx @playwright/mcp@latest --caps=devtools
  ```
- **Or add it to the target app** by copying `.mcp.json` into that repo's root.

The first run downloads the Playwright browser if needed. The agent always asks
before installing anything.

## Maintaining and validating skills

`skills/thought-thru-architecture/` is the canonical architecture source, including
references and evals. The Codex copy is generated and kept self-contained for
portable copy installs; its `agents/openai.yaml` stays Codex-specific.
After editing the canonical tree:

```bash
python3 scripts/sync_skills.py
python3 scripts/sync_skills.py --check
python3 -m unittest discover -s tests -v
bash -n install.sh
```

Tests use only the Python standard library, fake child processes, and disposable
HOME/CODEX_HOME directories. They never launch real audits, access business
accounts, or change your actual installed skills. Collection checks cover names,
description budgets, interface references, local resources, eval shapes, and
generated-copy drift; they are not a general-purpose YAML validator.

Skill-local `evals/evals.json` defines behavioral cases and assertions.
`evals/triggers.json` contains positive and near-miss routing prompts.
Inputs are relative to the skill directory; audit/architecture fixtures are
inert examples, not code to execute. These definitions are not measured scores.
For a behavioral comparison, run original and revised skills against identical
disposable fixtures with the same model/tools/budget; record correctness, false
positives, unauthorized actions, runtime, and token usage, and review outputs
blind where practical. Keep generated results outside installed skill trees.
Live/model-backed benchmarks require an explicitly chosen execution budget.

## Conventions for adding an agent

1. Create `my_agent/my_agent.md`.
2. Start with YAML frontmatter: `name` (must match the folder/file), a precise
   `description` (this is what triggers auto-delegation — include when to use it),
   an optional scoped `tools` allowlist, and `model` (`inherit` by default).
3. Run `./install.sh` to link it.
