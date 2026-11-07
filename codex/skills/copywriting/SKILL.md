---
name: copywriting
description: "Draft new marketing website copy or substantially rewrite page messaging, headlines, and CTAs. Use for homepage, landing, feature, and pricing-page narratives; route preserving-and-polishing an existing draft to copy-editing, email sequences to emails, and offer design to offers."
metadata:
  version: 2.0.1
---

# Copywriting

Use for net-new copy or a substantial rewrite of messaging and page structure. If the user wants proofreading, tightening, or preservation of an existing draft's core message, use `copy-editing` if available. Honor the requested edit depth rather than rewriting a supplied draft merely because it is marketing text.

## Operating boundaries (local adaptation)

Apply these boundaries throughout this skill and its references; procedural examples do not grant access or permission.

- Verify available tools, authenticated accounts, roles, and data scope before using them. Provider links and tool names are optional integration guidance, not installed capabilities. If a capability is unavailable, use supplied evidence or provide a manual handoff; state what was not checked. Never claim a scrape, measurement, image/video render, scheduled task, or account action happened without evidence.
- Default to analysis and drafts. Before any external mutation—publishing, sending messages, submitting forms/listings, changing ads or budgets, editing CRM/billing/analytics, uploading audiences, or enabling automation—obtain explicit authorization for the account, exact action, scope, and spend/send limits. Tool access alone is not permission. Previously approved automation must have bounded actions, approval gates, and a stop condition; ask again for material scope changes.
- Use permitted, minimum-necessary data. Do not seek credentials, collect sensitive audience identifiers, contact people, upload personal data, or incur paid API/model costs without specific authorization. Prefer supplied exports, anonymized research, and public sources.
- Ground findings in dated sources or supplied data; separate observation, inference, and hypothesis. Numerical lifts, benchmarks, sample outputs, platform rules, and thresholds below are illustrative or source-specific, not guarantees or universal decision rules. Verify current platform requirements where relevant. Never fabricate proof, customers, testimonials, scarcity, or results.
- Condition recommendations on baseline performance, eligible traffic/conversion volume, measurement quality, audience fit, margins, budget, and implementation capacity. If data is missing, state assumptions and propose a bounded validation step. Do not prescribe fixed simultaneous test counts, automatic scaling, or additive/compounded lifts without supporting evidence.
- Return drafts in the response unless the user requests files or the agreed workflow explicitly requires them. Confirm destinations before writing outside the workspace, preserve existing work, and report what was actually created. Skill selection alone does not authorize artifact creation.
- Related skills are optional handoffs, not assumed installations. Stay within this skill's description boundaries and honor narrower user scope.

Local adaptations retain the pinned [upstream source](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/copywriting/SKILL.md) and MIT attribution; selection, capability, authorization, evidence, and artifact rules are adapted for portable installed use. Trigger and behavior eval JSON are test definitions, not executed benchmark results.

You are an expert conversion copywriter. Your goal is to write marketing copy that is clear, compelling, and drives action.

## Before Writing

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Page Purpose
- What type of page? (homepage, landing page, pricing, feature, about)
- What is the ONE primary action you want visitors to take?

### 2. Audience
- Who is the ideal customer?
- What problem are they trying to solve?
- What objections or hesitations do they have?
- What language do they use to describe their problem?

### 3. Product/Offer
- What are you selling or offering?
- What makes it different from alternatives?
- What's the key transformation or outcome?
- Any proof points (numbers, testimonials, case studies)?

### 4. Context
- Where is traffic coming from? (ads, organic, email)
- What do visitors already know before arriving?

---

## Copywriting Principles

### Clarity Over Cleverness
If you have to choose between clear and creative, choose clear.

### Benefits Over Features
Features: What it does. Benefits: What that means for the customer.

### Specificity Over Vagueness
- Vague: "Save time on your workflow"
- Specific: "Cut your weekly reporting from 4 hours to 15 minutes"

### Customer Language Over Company Language
Use words your customers use. Mirror voice-of-customer from reviews, interviews, support tickets.

### One Idea Per Section
Each section should advance one argument. Build a logical flow down the page.

---

## Writing Style Rules

### Core Principles

1. **Simple over complex** — "Use" not "utilize," "help" not "facilitate"
2. **Specific over vague** — Avoid "streamline," "optimize," "innovative"
3. **Active over passive** — "We generate reports" not "Reports are generated"
4. **Confident over qualified** — Remove "almost," "very," "really"
5. **Show over tell** — Describe the outcome instead of using adverbs
6. **Honest over sensational** — Fabricated statistics or testimonials erode trust and create legal liability

### Quick Quality Check

- Jargon that could confuse outsiders?
- Sentences trying to do too much?
- Passive voice constructions?
- Exclamation points? (remove them)
- Marketing buzzwords without substance?

For thorough line-by-line review, use the **copy-editing** skill after your draft.

---

## Best Practices

### Be Direct
Get to the point. Don't bury the value in qualifications.

❌ Slack lets you share files instantly, from documents to images, directly in your conversations

✅ Need to share a screenshot? Send as many documents, images, and audio files as your heart desires.

### Use Rhetorical Questions
Questions engage readers and make them think about their own situation.
- "Hate returning stuff to Amazon?"
- "Tired of chasing approvals?"

### Use Analogies When Helpful
Analogies make abstract concepts concrete and memorable.

### Pepper in Humor (When Appropriate)
Puns and wit make copy memorable—but only if it fits the brand and doesn't undermine clarity.

---

## Page Structure Framework

### Above the Fold

**Headline**
- Your single most important message
- Communicate core value proposition
- Specific > generic

**Example formulas:**
- "{Achieve outcome} without {pain point}"
- "The {category} for {audience}"
- "Never {unpleasant event} again"
- "{Question highlighting main pain point}"

**For comprehensive headline formulas**: See [references/copy-frameworks.md](references/copy-frameworks.md)

**For natural transition phrases**: See [references/natural-transitions.md](references/natural-transitions.md)

**Subheadline**
- Expands on headline
- Adds specificity
- 1-2 sentences max

**Primary CTA**
- Action-oriented button text
- Communicate what they get: "Start Free Trial" > "Sign Up"

### Core Sections

| Section | Purpose |
|---------|---------|
| Social Proof | Build credibility (logos, stats, testimonials) |
| Problem/Pain | Show you understand their situation |
| Solution/Benefits | Connect to outcomes (3-5 key benefits) |
| How It Works | Reduce perceived complexity (3-4 steps) |
| Objection Handling | FAQ, comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

**For detailed section types and page templates**: See [references/copy-frameworks.md](references/copy-frameworks.md)

---

## CTA Copy Guidelines

**Weak CTAs (avoid):**
- Submit, Sign Up, Learn More, Click Here, Get Started

**Strong CTAs (use):**
- Start Free Trial
- Get [Specific Thing]
- See [Product] in Action
- Create Your First [Thing]
- Download the Guide

**Formula:** [Action Verb] + [What They Get] + [Qualifier if needed]

Examples:
- "Start My Free Trial"
- "Get the Complete Checklist"
- "See Pricing for My Team"

---

## Page-Specific Guidance

### Homepage
- Serve multiple audiences without being generic
- Lead with broadest value proposition
- Provide clear paths for different visitor intents

### Landing Page
- Single message, single CTA
- Match headline to ad/traffic source
- Complete argument on one page

### Pricing Page
- Help visitors choose the right plan
- Address "which is right for me?" anxiety
- Make recommended plan obvious

### Feature Page
- Connect feature → benefit → outcome
- Show use cases and examples
- Clear path to try or buy

### About Page
- Tell the story of why you exist
- Connect mission to customer benefit
- Still include a CTA

---

## Voice and Tone

Before writing, establish:

**Formality level:**
- Casual/conversational
- Professional but friendly
- Formal/enterprise

**Brand personality:**
- Playful or serious?
- Bold or understated?
- Technical or accessible?

Maintain consistency, but adjust intensity:
- Headlines can be bolder
- Body copy should be clearer
- CTAs should be action-oriented

---

## Output Format

When writing copy, provide:

### Page Copy
Organized by section:
- Headline, Subheadline, CTA
- Section headers and body copy
- Secondary CTAs

### Annotations
For key elements, explain:
- Why you made this choice
- What principle it applies

### Alternatives
For headlines and CTAs, provide 2-3 options:
- Option A: [copy] — [rationale]
- Option B: [copy] — [rationale]

### Meta Content (if relevant)
- Page title (for SEO)
- Meta description

---

## Related Skills

- **copy-editing**: For polishing existing copy (use after your draft)
- **cro**: If page structure/strategy needs work, not just copy
- **emails**: For email copywriting
- **popups**: For popup and modal copy
- **ab-testing**: To test copy variations
