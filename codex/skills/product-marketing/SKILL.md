---
name: product-marketing
description: "Develop positioning, ideal-customer, differentiation, and product marketing context for reuse across marketing tasks. Use for foundational audience and messaging decisions or a requested context document; not a mandatory prerequisite for every marketing request. Persist context when requested."
metadata:
  version: 2.0.0
---

# Product Marketing Context

## Operating boundaries (local adaptation)

Apply these boundaries throughout this skill and its references; procedural examples do not grant access or permission.

- Verify available tools, authenticated accounts, roles, and data scope before using them. Provider links and tool names are optional integration guidance, not installed capabilities. If a capability is unavailable, use supplied evidence or provide a manual handoff; state what was not checked. Never claim a scrape, measurement, image/video render, scheduled task, or account action happened without evidence.
- Default to analysis and drafts. Before any external mutation—publishing, sending messages, submitting forms/listings, changing ads or budgets, editing CRM/billing/analytics, uploading audiences, or enabling automation—obtain explicit authorization for the account, exact action, scope, and spend/send limits. Tool access alone is not permission. Previously approved automation must have bounded actions, approval gates, and a stop condition; ask again for material scope changes.
- Use permitted, minimum-necessary data. Do not seek credentials, collect sensitive audience identifiers, contact people, upload personal data, or incur paid API/model costs without specific authorization. Prefer supplied exports, anonymized research, and public sources.
- Ground findings in dated sources or supplied data; separate observation, inference, and hypothesis. Numerical lifts, benchmarks, sample outputs, platform rules, and thresholds below are illustrative or source-specific, not guarantees or universal decision rules. Verify current platform requirements where relevant. Never fabricate proof, customers, testimonials, scarcity, or results.
- Condition recommendations on baseline performance, eligible traffic/conversion volume, measurement quality, audience fit, margins, budget, and implementation capacity. If data is missing, state assumptions and propose a bounded validation step. Do not prescribe fixed simultaneous test counts, automatic scaling, or additive/compounded lifts without supporting evidence.
- Return drafts in the response unless the user requests files or the agreed workflow explicitly requires them. Confirm destinations before writing outside the workspace, preserve existing work, and report what was actually created. Skill selection alone does not authorize artifact creation.
- Related skills are optional handoffs, not assumed installations. Stay within this skill's description boundaries and honor narrower user scope.

Local adaptations retain the pinned [upstream source](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/product-marketing/SKILL.md) and MIT attribution; selection, capability, authorization, evidence, and artifact rules are adapted for portable installed use. Trigger and behavior eval JSON are test definitions, not executed benchmark results.

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is stored at `.agents/product-marketing.md`.

## Workflow

### Step 1: Check for Existing Context

First, check if `.agents/product-marketing.md` already exists. Also check `.claude/product-marketing.md` and the legacy filename `product-marketing-context.md` (in either `.agents/` or `.claude/`) for older setups — if found anywhere other than `.agents/product-marketing.md`, offer to move it to the canonical location.

**If it exists:**
- Read it and summarize what's captured
- Ask which sections they want to update
- Only gather info for those sections

**If it doesn't exist, offer two options:**

1. **Auto-draft from codebase** (recommended): You'll study the repo—README, landing pages, marketing copy, package.json, etc.—and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time. Don't dump all questions at once.

For each section:
1. Briefly explain what you're capturing
2. Ask relevant questions
3. Confirm accuracy
4. Move to the next

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- Tone (professional, casual, playful, etc.)
- Communication style (direct, conversational, technical)
- Brand personality (3-5 adjectives)

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

---

## Step 3: Create the Document

After gathering information, create `.agents/product-marketing.md` with this structure:

```markdown
# Product Marketing Context

*Last updated: [date]*

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
**Tone:**
**Style:**
**Personality:**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**
```

---

## Step 4: Confirm and Save

- Show the completed document
- Ask if anything needs adjustment
- Save to `.agents/product-marketing.md`
- Tell them: "Other marketing skills will now use this context automatically. Run `/product-marketing` anytime to update it."

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C)
