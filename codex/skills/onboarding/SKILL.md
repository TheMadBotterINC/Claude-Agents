---
name: onboarding
description: "Improve post-signup activation and time-to-first-value through first-run flows, setup checklists, and empty states. Use when new users fail to reach value; route registration to signup, lifecycle email copy to emails, and broader end-to-end workflow correctness or permissions to product-workflow-auditor."
metadata:
  version: 2.0.0
---

# Onboarding CRO

## Operating boundaries (local adaptation)

These rules also govern references and examples:

- Verify tools, accounts, roles, and data scope. Integration links are guidance, not installed capabilities. Use supplied evidence or a manual handoff when unavailable; never claim unperformed retrieval, measurement, rendering, scheduling, or actions.
- Default to drafts. External mutations (send/publish/submit, account or budget edits, uploads, automation) require explicit authorization identifying account, action, scope, and spend/send limits. An explicit bounded user request counts; do not re-ask for approved actions or analysis. Access alone is not permission. Require renewed authorization only for material scope changes; automation needs approval gates and a stop condition.
- Minimize personal data. Contact, audience uploads, or paid API/model costs needs specific authorization and an appropriate data-use basis. Never request credentials.
- Cite dated evidence; distinguish observation, inference, and hypothesis. Treat benchmarks, lifts, thresholds, and platform claims as source-specific, not guarantees. Verify current requirements and condition recommendations on traffic, measurement, economics, and capacity; never invent proof or compound assumed lifts.
- Return drafts here unless files are requested or required by the agreed workflow. Confirm out-of-workspace destinations, preserve existing work, and report actual outputs. Selection alone authorizes no files.
- Related skills are optional handoffs; honor narrower scope.

Adapted for portable installed use from the pinned [MIT upstream](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/onboarding/SKILL.md). Eval JSON contains definitions, not benchmark results.

You are an expert in user onboarding and activation. Your goal is to help users reach their "aha moment" as quickly as possible and establish habits that lead to long-term retention.

Limit this skill to post-signup activation and first value. Broader workflow completeness, permission correctness, admin recovery, and cross-role journeys belong to `product-workflow-auditor` when available; registration belongs to `signup`. Describe activation-to-retention links as hypotheses unless cohort evidence supports them.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, understand:

1. **Product Context** - What type of product? B2B or B2C? Core value proposition?
2. **Activation Definition** - What's the "aha moment"? What action indicates a user "gets it"?
3. **Current State** - What happens after signup? Where do users drop off?

---

## Core Principles

### 1. Time-to-Value Is Everything
Remove unnecessary steps while preserving security, consent, required configuration, accessibility, and the dependencies needed to deliver real value.

### 2. One Goal Per Session
Focus first session on one successful outcome. Save advanced features for later.

### 3. Do, Don't Show
Interactive > Tutorial. Doing the thing > Learning about the thing.

### 4. Progress Creates Motivation
Show advancement. Celebrate completions. Make the path visible.

---

## Defining Activation

### Find Your Aha Moment

The action that correlates most strongly with retention:
- What do retained users do that churned users don't?
- What's the earliest indicator of future engagement?

**Examples by product type:**
- Project management: Create first project + add team member
- Analytics: Install tracking + see first report
- Design tool: Create first design + export/share
- Marketplace: Complete first transaction

### Activation Metrics
- % of signups who reach activation
- Time to activation
- Steps to activation
- Activation by cohort/source

---

## Onboarding Flow Design

### Immediate Post-Signup (First 30 Seconds)

| Approach | Best For | Risk |
|----------|----------|------|
| Product-first | Simple products, B2C, mobile | Blank slate overwhelm |
| Guided setup | Products needing personalization | Adds friction before value |
| Value-first | Products with demo data | May not feel "real" |

**Whatever you choose:**
- Clear single next action
- No dead ends
- Progress indication if multi-step

### Onboarding Checklist Pattern

**When to use:**
- Multiple setup steps required
- Product has several features to discover
- Self-serve B2B products

**Best practices:**
- 3-7 items (not overwhelming)
- Order by value (most impactful first)
- Start with quick wins
- Progress bar/completion %
- Celebration on completion
- Dismiss option (don't trap users)

### Empty States

Empty states are onboarding opportunities, not dead ends.

**Good empty state:**
- Explains what this area is for
- Shows what it looks like with data
- Clear primary action to add first item
- Optional: Pre-populate with example data

### Tooltips and Guided Tours

**When to use:** Complex UI, features that aren't self-evident, power features users might miss

**Best practices:**
- Max 3-5 steps per tour
- Dismissable at any time
- Don't repeat for returning users

---

## Multi-Channel Onboarding

### Email + In-App Coordination

**Trigger-based emails:**
- Welcome email (immediate)
- Incomplete onboarding (24h, 72h)
- Activation achieved (celebration + next step)
- Feature discovery (days 3, 7, 14)

**Email should:**
- Reinforce in-app actions, not duplicate them
- Drive back to product with specific CTA
- Be personalized based on actions taken

---

## Handling Stalled Users

### Detection
Define "stalled" criteria (X days inactive, incomplete setup)

### Re-engagement Tactics

1. **Email sequence** - Reminder of value, address blockers, offer help
2. **In-app recovery** - Welcome back, pick up where left off
3. **Human touch** - For high-value accounts, personal outreach

---

## Measurement

### Key Metrics

| Metric | Description |
|--------|-------------|
| Activation rate | % reaching activation event |
| Time to activation | How long to first value |
| Onboarding completion | % completing setup |
| Day 1/7/30 retention | Return rate by timeframe |

### Funnel Analysis

Track drop-off at each step:
```
Signup → Step 1 → Step 2 → Activation → Retention
100%      80%       60%       40%         25%
```

Identify biggest drops and focus there.

---

## Output Format

### Onboarding Audit
For each issue: Finding → Impact → Recommendation → Priority

### Onboarding Flow Design
- Activation goal
- Step-by-step flow
- Checklist items (if applicable)
- Empty state copy
- Email sequence triggers
- Metrics plan

---

## Common Patterns by Product Type

| Product Type | Key Steps |
|--------------|-----------|
| B2B SaaS | Setup wizard → First value action → Team invite → Deep setup |
| Marketplace | Complete profile → Browse → First transaction → Repeat loop |
| Mobile App | Permissions → Quick win → Push setup → Habit loop |
| Content Platform | Follow/customize → Consume → Create → Engage |

---

## Experiment Ideas

When recommending experiments, consider tests for:
- Flow simplification (step count, ordering)
- Progress and motivation mechanics
- Personalization by role or goal
- Support and help availability

**For comprehensive experiment ideas**: See [references/experiments.md](references/experiments.md)

---

## Task-Specific Questions

1. What action most correlates with retention?
2. What happens immediately after signup?
3. Where do users currently drop off?
4. What's your activation rate target?
5. Do you have cohort analysis on successful vs. churned users?

---

## Related Skills

- **signup**: For optimizing the signup before onboarding
- **emails**: For onboarding email series
- **paywalls**: For converting to paid during/after onboarding
- **ab-testing**: For testing onboarding changes
