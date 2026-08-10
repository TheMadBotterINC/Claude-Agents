# Audit report conventions

Shared by this repo's audit-style Claude subagents (`activerecord_performance`,
`rails_code_quality`, `rails_security`, `ux_tester`, `web_performance`). Each
agent's own file states its specific report filename; everything else about
where and how to save a report lives here so it only needs updating once.

- **Location:** write the report under the project root at
  `docs/audits/<this agent's report filename>`, creating `docs/audits/` if it
  doesn't exist (`mkdir -p docs/audits`, or rely on `Write` creating parent
  dirs).
- **Collisions:** add a scope/date suffix if a run would otherwise overwrite a
  prior report.
- **Mounted engines:** when auditing a mounted engine / customer gem (source
  outside the host repo), save into the *host* app's `docs/audits/` instead,
  with a `gem_`-prefixed filename.
- **Always** also return the findings in your final message — the file is a
  durable copy, not a replacement for the response.
