---
name: public-relations
description: "Plan earned-media strategy and draft press materials, journalist pitches, and reporter responses. Use for public relations, not code pull requests; route product-directory listings to directory-submissions, releases to launch, and sales outreach to cold-email. Sending requires authorization."
metadata:
  version: 1.0.0
---

# Public Relations & Earned Media

## Operating boundaries (local adaptation)

Apply these boundaries throughout this skill and its references; procedural examples do not grant access or permission.

- Verify available tools, authenticated accounts, roles, and data scope before using them. Provider links and tool names are optional integration guidance, not installed capabilities. If a capability is unavailable, use supplied evidence or provide a manual handoff; state what was not checked. Never claim a scrape, measurement, image/video render, scheduled task, or account action happened without evidence.
- Default to analysis and drafts. Before any external mutation—publishing, sending messages, submitting forms/listings, changing ads or budgets, editing CRM/billing/analytics, uploading audiences, or enabling automation—obtain explicit authorization for the account, exact action, scope, and spend/send limits. Tool access alone is not permission. Previously approved automation must have bounded actions, approval gates, and a stop condition; ask again for material scope changes.
- Use permitted, minimum-necessary data. Do not seek credentials, collect sensitive audience identifiers, contact people, upload personal data, or incur paid API/model costs without specific authorization. Prefer supplied exports, anonymized research, and public sources.
- Ground findings in dated sources or supplied data; separate observation, inference, and hypothesis. Numerical lifts, benchmarks, sample outputs, platform rules, and thresholds below are illustrative or source-specific, not guarantees or universal decision rules. Verify current platform requirements where relevant. Never fabricate proof, customers, testimonials, scarcity, or results.
- Condition recommendations on baseline performance, eligible traffic/conversion volume, measurement quality, audience fit, margins, budget, and implementation capacity. If data is missing, state assumptions and propose a bounded validation step. Do not prescribe fixed simultaneous test counts, automatic scaling, or additive/compounded lifts without supporting evidence.
- Return drafts in the response unless the user requests files or the agreed workflow explicitly requires them. Confirm destinations before writing outside the workspace, preserve existing work, and report what was actually created. Skill selection alone does not authorize artifact creation.
- Related skills are optional handoffs, not assumed installations. Stay within this skill's description boundaries and honor narrower user scope.

Local adaptations retain the pinned [upstream source](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/public-relations/SKILL.md) and MIT attribution; selection, capability, authorization, evidence, and artifact rules are adapted for portable installed use. Trigger and behavior eval JSON are test definitions, not executed benchmark results.

You are an expert in earned media for software products. Your goal is to help the user get covered by journalists, podcasts, and newsletters — efficiently, with respect for the people on the other end of the pitch.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

---

## Core Philosophy

PR is not a substitute for distribution. It's a multiplier for it.

- **Earned media doesn't drive direct conversions.** A TechCrunch hit will not give you 1,000 paying customers. It will give you backlinks, brand legitimacy, AI-citation surface area, and ammo for sales conversations.
- **Pitch journalists like you'd pitch a customer:** specific, useful, fast, and never about you.
- **The story is not your product. The story is the trend, the data, the conflict, or the human.** Your product is the evidence.
- **Speed beats polish on reactive PR.** A B+ pitch in the first hour of a story beats an A+ pitch on day three.

### When PR is worth it

- You have **a real story** — proprietary data, a strong opinion, a milestone, a customer with a sharp before/after, or a fresh angle on a trending topic
- You have **founder/exec time** — journalists want quotes from people with skin in the game, not from a PR rep
- You have **a destination** — a press page, blog post, or product launch that converts attention into something useful

### When to skip PR (for now)

- Pre-launch with no story beyond "we exist"
- No one on the team can sustain pitching for 4–6 weeks (PR is a momentum game)
- You don't have a clear ICP — journalists ask "who reads my piece because of this?" and if you can't answer, neither can they

---

## The PR Mix

Four modes. Most teams over-index on one. Run at least three.

| Mode | What it is | Effort | Speed to coverage |
|------|------------|--------|-------------------|
| **Reactive (newsjacking)** | Inject your POV into trending news | Low–medium | Hours to days |
| **Proactive (pitching)** | Build a media list, pitch original stories | High | 2–8 weeks |
| **Inbound (press requests)** | Respond to journalist queries on HARO/Qwoted/Featured | Low | Days to weeks |
| **Owned (press page + media kit)** | Make it easy for journalists to find you | One-time setup | N/A |

**For the reactive newsjacking workflow** — see [references/newsjacking.md](references/newsjacking.md)

**For proactive journalist pitching** — see [references/journalist-pitching.md](references/journalist-pitching.md)

**For inbound press-request platforms (HARO, Qwoted, etc.)** — see [references/press-platforms.md](references/press-platforms.md)

**For where to pitch (media outlets, podcasts, newsletters)** — see [references/media-outlets.md](references/media-outlets.md). For startup/SaaS/AI directories, use the separate `directory-submissions` skill — different intent, different list.

---

## Owned: Press Page + Media Kit

Set this up once. It's the cheapest PR investment with the highest ROI on every future story.

**Press page (`/press` or `/newsroom`) should include:**
- One-paragraph company description (copy/paste ready)
- Founder bios with headshots (high-res, downloadable)
- Logo pack (SVG + PNG, light + dark, with usage guidelines)
- Product screenshots (high-res)
- Recent coverage list (social proof for the next journalist)
- Founding date, employee count, funding (if disclosed)
- Press contact email (not a form — journalists hate forms)
- Recent press releases / announcements

**One sentence at the top:** "For interview requests or assets, email press@yourcompany.com — we respond within 24 hours."

Then *actually* respond within 24 hours.

---

## Quick Reference: Pitch Quality Bar

Before sending any pitch, the answer to all of these should be yes:

- [ ] Does this journalist cover this beat? (Check their last 5 articles.)
- [ ] Is there a clear news hook — something that just happened or is about to?
- [ ] Could this journalist write a complete story from this email alone? (Data, quotes, customer name, contact.)
- [ ] Is the subject line specific enough to predict the article's headline?
- [ ] Is the pitch under 150 words?
- [ ] Did you avoid the words "revolutionary," "game-changing," "disruptive," and "synergy"?
- [ ] Is the ask clear? (Interview? Embargo? Exclusive? Quote?)

If any answer is no, don't send.

---

## Measurement

What to track:

| Metric | Why |
|--------|-----|
| **Coverage count** (placements / month) | Activity baseline |
| **Domain rating of placements** | Backlink value |
| **Referral traffic from coverage** | Did anyone actually click? |
| **Brand search lift** | Did people search you after reading? |
| **AI citation rate** (ChatGPT, Perplexity quote your brand?) | The new measurement that matters |
| **Sales conversations citing the article** | The only one that matters for revenue |

What not to obsess over: AVE (advertising value equivalency) — it's a vanity metric PR firms invented.

---

## Common Workflows

### "Help me newsjack [trending story]"
Go to [newsjacking.md](references/newsjacking.md), run the scoring rubric, draft 2–3 angles, pick the best, draft the pitch.

### "Find journalists who cover [beat]"
Go to [journalist-pitching.md](references/journalist-pitching.md), use the discovery checklist plus an available browser or public web search to research recent articles, then build a scored list. Do not contact journalists without explicit authorization.

### "What's worth pitching this week?"
Combine: recent product milestones + active news cycles + any data you've collected. Score each potential story by the quality bar above.

### "Respond to this HARO query"
Go to [press-platforms.md](references/press-platforms.md), use the response template, keep it under 200 words.

### "Build my press page"
Use the checklist above. Most companies do this in an afternoon and forget about it for a year — that's fine.
