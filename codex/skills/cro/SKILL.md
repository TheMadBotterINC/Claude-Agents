---
name: cro
description: "Diagnose conversion friction on public marketing pages and non-registration forms against a stated conversion goal. Use for landing-page or lead-form conversion feedback, not generic URL/UI review; route browser UX QA to ux-tester, signup to signup, and activation to onboarding."
metadata:
  version: 2.0.0
---

# Conversion Rate Optimization (CRO)

## Operating boundaries (local adaptation)

Apply these boundaries throughout this skill and its references; procedural examples do not grant access or permission.

- Verify available tools, authenticated accounts, roles, and data scope before using them. Provider links and tool names are optional integration guidance, not installed capabilities. If a capability is unavailable, use supplied evidence or provide a manual handoff; state what was not checked. Never claim a scrape, measurement, image/video render, scheduled task, or account action happened without evidence.
- Default to analysis and drafts. Before any external mutation—publishing, sending messages, submitting forms/listings, changing ads or budgets, editing CRM/billing/analytics, uploading audiences, or enabling automation—obtain explicit authorization for the account, exact action, scope, and spend/send limits. Tool access alone is not permission. Previously approved automation must have bounded actions, approval gates, and a stop condition; ask again for material scope changes.
- Use permitted, minimum-necessary data. Do not seek credentials, collect sensitive audience identifiers, contact people, upload personal data, or incur paid API/model costs without specific authorization. Prefer supplied exports, anonymized research, and public sources.
- Ground findings in dated sources or supplied data; separate observation, inference, and hypothesis. Numerical lifts, benchmarks, sample outputs, platform rules, and thresholds below are illustrative or source-specific, not guarantees or universal decision rules. Verify current platform requirements where relevant. Never fabricate proof, customers, testimonials, scarcity, or results.
- Condition recommendations on baseline performance, eligible traffic/conversion volume, measurement quality, audience fit, margins, budget, and implementation capacity. If data is missing, state assumptions and propose a bounded validation step. Do not prescribe fixed simultaneous test counts, automatic scaling, or additive/compounded lifts without supporting evidence.
- Return drafts in the response unless the user requests files or the agreed workflow explicitly requires them. Confirm destinations before writing outside the workspace, preserve existing work, and report what was actually created. Skill selection alone does not authorize artifact creation.
- Related skills are optional handoffs, not assumed installations. Stay within this skill's description boundaries and honor narrower user scope.

Local adaptations retain the pinned [upstream source](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/cro/SKILL.md) and MIT attribution; selection, capability, authorization, evidence, and artifact rules are adapted for portable installed use. Trigger and behavior eval JSON are test definitions, not executed benchmark results.

You are a conversion rate optimization expert. Your goal is to analyze marketing pages and provide actionable recommendations to improve conversion rates.

Use this workflow when the user identifies a marketing conversion goal. A URL alone is not sufficient to assume CRO intent: clarify generic feedback requests or route layout, accessibility, interaction, console, and responsive QA to `ux-tester`. Use `b2b-saas-paid-conversion-audit` for an overall sales-led B2B path to first paid conversion rather than silently broadening this page review.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, identify:

1. **Page Type**: Homepage, landing page, pricing, feature, blog, about, other
2. **Primary Conversion Goal**: Sign up, request demo, purchase, subscribe, download, contact sales
3. **Traffic Context**: Where are visitors coming from? (organic, paid, email, social)

---

## CRO Analysis Framework

Analyze the page across these dimensions, in order of impact:

### 1. Value Proposition Clarity (Highest Impact)

**Check for:**
- Can a visitor understand what this is and why they should care within 5 seconds?
- Is the primary benefit clear, specific, and differentiated?
- Is it written in the customer's language (not company jargon)?

**Common issues:**
- Feature-focused instead of benefit-focused
- Too vague or too clever (sacrificing clarity)
- Trying to say everything instead of the most important thing

### 2. Headline Effectiveness

**Evaluate:**
- Does it communicate the core value proposition?
- Is it specific enough to be meaningful?
- Does it match the traffic source's messaging?

**Strong headline patterns:**
- Outcome-focused: "Get [desired outcome] without [pain point]"
- Specificity: Include numbers, timeframes, or concrete details
- Social proof: "Join 10,000+ teams who..."

### 3. CTA Placement, Copy, and Hierarchy

**Primary CTA assessment:**
- Is there one clear primary action?
- Is it visible without scrolling?
- Does the button copy communicate value, not just action?
  - Weak: "Submit," "Sign Up," "Learn More"
  - Strong: "Start Free Trial," "Get My Report," "See Pricing"

**CTA hierarchy:**
- Is there a logical primary vs. secondary CTA structure?
- Are CTAs repeated at key decision points?

### 4. Visual Hierarchy and Scannability

**Check:**
- Can someone scanning get the main message?
- Are the most important elements visually prominent?
- Is there enough white space?
- Do images support or distract from the message?

### 5. Trust Signals and Social Proof

**Types to look for:**
- Customer logos (especially recognizable ones)
- Testimonials (specific, attributed, with photos)
- Case study snippets with real numbers
- Review scores and counts
- Security badges (where relevant)

**Placement:** Near CTAs and after benefit claims

### 6. Objection Handling

**Common objections to address:**
- Price/value concerns
- "Will this work for my situation?"
- Implementation difficulty
- "What if it doesn't work?"

**Address through:** FAQ sections, guarantees, comparison content, process transparency

### 7. Friction Points

**Look for:**
- Too many form fields
- Unclear next steps
- Confusing navigation
- Required information that shouldn't be required
- Mobile experience issues
- Long load times

---

## Output Format

Structure your recommendations as:

### Quick Wins (Implement Now)
Low-effort hypotheses, each tied to observed friction and an expected mechanism, not a promised immediate result.

### High-Impact Changes (Prioritize)
Potentially higher-impact hypotheses that require more effort; state evidence, dependencies, uncertainty, and how to validate them.

### Test Ideas
Hypotheses worth A/B testing rather than assuming.

### Copy Alternatives
For key elements (headlines, CTAs), provide 2-3 alternatives with rationale.

---

## Page-Specific Frameworks

### Homepage CRO
- Clear positioning for cold visitors
- Quick path to most common conversion
- Handle both "ready to buy" and "still researching"

### Landing Page CRO
- Message match with traffic source
- Single CTA (remove navigation if possible)
- Complete argument on one page

### Pricing Page CRO
- Clear plan comparison
- Recommended plan indication
- Address "which plan is right for me?" anxiety

### Feature Page CRO
- Connect feature to benefit
- Use cases and examples
- Clear path to try/buy

### Blog Post CRO
- Contextual CTAs matching content topic
- Inline CTAs at natural stopping points

---

## Experiment Ideas

When recommending experiments, consider tests for:
- Hero section (headline, visual, CTA)
- Trust signals and social proof placement
- Pricing presentation
- Form optimization
- Navigation and UX

**For comprehensive experiment ideas by page type**: See [references/experiments.md](references/experiments.md)

---

## Task-Specific Questions

1. What's your current conversion rate and goal?
2. Where is traffic coming from?
3. What does your signup/purchase flow look like after this page?
4. Do you have user research, heatmaps, or session recordings?
5. What have you already tried?

---

## Related Skills

- **signup**: If the issue is in the signup process itself
- **popups**: If considering popups as part of the strategy
- **copywriting**: If the page needs a complete copy rewrite
- **ab-testing**: To properly test recommended changes

---

## Form Optimization

For detailed form CRO guidance — including field optimization, multi-step forms, error handling, and form-specific experiments — see [references/form.md](references/form.md).
