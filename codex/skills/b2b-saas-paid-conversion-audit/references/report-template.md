# Paid-Conversion Audit Report Template

Use this exact section order. Omit an inapplicable route, but state why it was not observed. Keep the artifact concise and decision-oriented.

```markdown
# Paid Conversion Audit — [Product]

**Audit status:** Complete | Partial | Blocked
**Audit date:** YYYY-MM-DD
**Input:** [absolute URL or resolved repository root]
**Input mode:** Live URL | Repository root
**Scope:** Observable path to first paid conversion
**Report:** [absolute report path]

## Executive diagnosis

**Primary diagnosis:** [For an explicit homepage/bounce question, name the most plausible entry-page abandonment driver. Otherwise name the highest-priority observable friction. Use "Not established" when unsupported.]
**Route and stage:** [sales-led/self-serve; stage]
**Confidence:** High | Medium | Low | Not applicable
**Recommended first move:** [one sentence, or "Provide a reachable target"]

[Two to four sentences separating what was observed from the hypothesis about visitor behavior. For a bounce question, state that the conclusion applies to traffic landing on the evaluated page. Never call this "the reason visitors bounce" or "the bottleneck" without supplied outcome data.]

## Cold-visitor entry-page verdict

| First 5–10 second question | Visitor can answer | Evidence and implication |
|---|---|---|
| What is this? | Clearly / Partly / No | E... |
| Is it for me? | Clearly / Partly / No | E... |
| Why should I care now? | Clearly / Partly / No | E... |
| Why should I believe it? | Clearly / Partly / No | E... |
| What happens after the click? | Clearly / Partly / No | E... |

[Include this section only when a homepage or landing page is in scope. For a repository, base it on source-evident entry-page content and state that rendering is unverified. For another supplied surface or a blocked target, omit it.]

## Scope and limitations

- **Inspected:** [surfaces]
- **Not observable:** [downstream or blocked surfaces]
- **Paid-conversion boundary:** [closed-won/paid commitment and/or first successful self-serve payment]
- **Data limitation:** No analytics, CRM, billing, or causal performance data was used.

## Conversion path coverage

| Route | Stage | Status | Evidence | Material unknown |
|---|---|---|---|---|
| Sales-led | ... | Observed / Source-evident / Not observable | E1 | ... |
| Self-serve | ... | Observed / Source-evident / Not observable | E2 | ... |

## Evidence ledger

| ID | Label | Route and stage | Evidence | Source |
|---|---|---|---|---|
| E1 | Runtime-observed / Source-evident / User-provided / Hypothesis / Not observable | ... | ... | URL or `path:line` |

## Prioritized recommendations

[Include zero to three recommendations across both routes combined. Do not add quick wins, an idea bank, or secondary recommendations.]

### 1. [Specific recommendation]

- **Route and stage:**
- **Observable friction:**
- **Why it may impede the next paid-conversion step — Hypothesis:**
- **Evidence:** E...
- **Recommendation:**
- **Available-now version:** [specific page, copy, demonstration, offer, or route change that does not depend on unavailable analytics or customer proof]
- **Expected paid-conversion mechanism — Hypothesis:**
- **Confidence and reason:** High / Medium / Low — ...
- **Relative effort:** Small / Medium / Large
- **Minimal validation signal:** [proximate signal plus eventual first-paid outcome]
- **Handoff:** [specialist skill when available, otherwise manual capability]

## Minimal validation plan

| Priority | Smallest useful signal | Eventual paid outcome | Decision enabled |
|---|---|---|---|
| 1 | ... | ... | ... |

[Recommend signals only. Do not implement analytics or prescribe a full tracking stack. Measurement or future proof collection may validate a change, but must not replace the available-now intervention.]

## Unknowns that could change the ranking

| Unknown | Why it matters | How to resolve |
|---|---|---|
| ... | ... | ... |

[Do not turn unavailable analytics, testimonials, case studies, or customer outcomes into prerequisites. Include only unknowns that could change ranking or implementation.]

## Deferred observations

[Optional. Record material observations that were not selected. Do not include an action, test, or recommendation here.]

## Inspected surfaces

- [URL or repository-relative `path:line`]
```

For a blocked URL, keep the same metadata and include only:

- `## Access failure`
- The attempted URL, failure observed, and timestamp.
- `## Required next input`
- A reachable URL or existing repository root.

Use zero priorities in a blocked report.
