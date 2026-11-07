---
name: ads
description: "Plan and review paid-media campaigns, targeting, bidding, budgets, CPA, and ROAS using available evidence. Use for PPC and paid acquisition decisions; route creative production to ad-creative and post-click page diagnosis to cro. Account changes require explicit authorization."
metadata:
  version: 2.2.0
---

# Paid Ads

## Operating boundaries (local adaptation)

These rules also govern references and examples:

- Verify tools, accounts, roles, and data scope. Integration links are guidance, not installed capabilities. Use supplied evidence or a manual handoff when unavailable; never claim unperformed retrieval, measurement, rendering, scheduling, or actions.
- Default to drafts. External mutations (send/publish/submit, account or budget edits, uploads, automation) require explicit authorization identifying account, action, scope, and spend/send limits. An explicit bounded user request counts; do not re-ask for approved actions or analysis. Access alone is not permission. Require renewed authorization only for material scope changes; automation needs approval gates and a stop condition.
- Minimize personal data. Contact, audience uploads, or paid API/model costs needs specific authorization and an appropriate data-use basis. Never request credentials.
- Cite dated evidence; distinguish observation, inference, and hypothesis. Treat benchmarks, lifts, thresholds, and platform claims as source-specific, not guarantees. Verify current requirements and condition recommendations on traffic, measurement, economics, and capacity; never invent proof or compound assumed lifts.
- Return drafts here unless files are requested or required by the agreed workflow. Confirm out-of-workspace destinations, preserve existing work, and report actual outputs. Selection alone authorizes no files.
- Related skills are optional handoffs; honor narrower scope.

Adapted for portable installed use from the pinned [MIT upstream](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/ads/SKILL.md). Eval JSON contains definitions, not benchmark results.

Help plan, review, and improve paid campaigns using supplied exports or explicitly authorized account capabilities. Do not assume direct account access. Strategy and draft recommendations do not authorize campaign creation, budget changes, audience uploads, or launches.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Campaign Goals
- What's the primary objective? (Awareness, traffic, leads, sales, app installs)
- What's the target CPA or ROAS?
- What's the monthly/weekly budget?
- Any constraints? (Brand guidelines, compliance, geographic)

### 2. Product & Offer
- What are you promoting? (Product, free trial, lead magnet, demo)
- What's the landing page URL?
- What makes this offer compelling?

### 3. Audience
- Who is the ideal customer?
- What problem does your product solve for them?
- What are they searching for or interested in?
- Do you have existing customer data for lookalikes?

### 4. Current State
- Have you run ads before? What worked/didn't?
- Do you have existing pixel/conversion data?
- What's your current funnel conversion rate?

---

## Reference Routing

This skill's depth lives in references — load by intent. For **any operational decision on a live account** (kill/keep/scale/budget), load the relevant playbook before answering; the thresholds live there, not here.

| User intent | Load | Covers |
|---|---|---|
| B2B strategy, funnel stages, budget splits, kill rules, lead quality, breakeven math | [b2b-paid-playbook.md](references/b2b-paid-playbook.md) | Demand lifecycle, leading/lagging signals, kill rules, offline conversion loop, U/B/F lead scoring, scaling quadrant |
| Meta operations: when to kill/graduate/scale an ad, fatigue, testing structure | [meta-decision-system.md](references/meta-decision-system.md) | TCPL-anchored decision tree, ad-count ceiling, 80/20 CBO structure, fatigue bands, lead forms, Advantage+ transition |
| LinkedIn operations: bidding, audience sizing, scaling, benchmarks, TLAs, formats | [linkedin-b2b-playbook.md](references/linkedin-b2b-playbook.md) | Bidding progression, penetration scaling, sizing rules, funnel benchmarks, document/conversation ads, audit shortlist |
| Google Search: what to spend on first, structure, match types, negatives, PMax | [google-search-playbook.md](references/google-search-playbook.md) | Intent ladder, account structure, match-type gates, negatives, bidding by volume, offline conversions, PMax guardrails |
| Named-account targeting, pipeline acceleration, cross-channel retargeting | [abm-playbook.md](references/abm-playbook.md) | LinkedIn/Meta ABM, list mechanics, acceleration campaigns, UTM cross-channel remarketing, ABM measurement |
| Generating Google RSAs | [rsa-output-spec.md](references/rsa-output-spec.md) | Mandatory output spec — limits, sidecars, template, self-check |
| Audience setup, tracking setup, launch checklists, copy formulas | [audience-targeting.md](references/audience-targeting.md) · [conversion-tracking.md](references/conversion-tracking.md) · [platform-setup-checklists.md](references/platform-setup-checklists.md) · [ad-copy-templates.md](references/ad-copy-templates.md) | Existing foundations |

---

## Platform Selection Guide

| Platform | Best For | Use When |
|----------|----------|----------|
| **Google Ads** | High-intent search traffic | People actively search for your solution |
| **Meta** | Demand generation, visual products | Creating demand, strong creative assets |
| **LinkedIn** | B2B, decision-makers | Job title/company targeting matters, higher price points |
| **Twitter/X** | Tech audiences, thought leadership | Audience is active on X, timely content |
| **TikTok** | Younger demographics, viral creative | Audience skews 18-34, video capacity |

---

## Campaign Structure Best Practices

### Account Organization

```
Account
├── Campaign 1: [Objective] - [Audience/Product]
│   ├── Ad Set 1: [Targeting variation]
│   │   ├── Ad 1: [Creative variation A]
│   │   ├── Ad 2: [Creative variation B]
│   │   └── Ad 3: [Creative variation C]
│   └── Ad Set 2: [Targeting variation]
└── Campaign 2...
```

### Naming Conventions

```
[Platform]_[Objective]_[Audience]_[Offer]_[Date]

Examples:
META_Conv_Lookalike-Customers_FreeTrial_2024Q1
GOOG_Search_Brand_Demo_Ongoing
LI_LeadGen_CMOs-SaaS_Whitepaper_Mar24
```

### Budget Allocation

**Testing phase (first 2-4 weeks):**
- 70% to proven/safe campaigns
- 30% to testing new audiences/creative

**Scaling phase:**
- Consolidate budget into winning combinations
- Propose gradual budget changes only when conversion quality, marginal acquisition cost, cash runway, and platform-specific learning constraints support them.
- Treat a 20% step and 3-5 day observation window as examples, not universal rules; obtain approval before changing spend.

---

## Ad Copy Frameworks

### Key Formulas

**Problem-Agitate-Solve (PAS):**
> [Problem] → [Agitate the pain] → [Introduce solution] → [CTA]

**Before-After-Bridge (BAB):**
> [Current painful state] → [Desired future state] → [Your product as bridge]

**Social Proof Lead:**
> [Impressive stat or testimonial] → [What you do] → [CTA]

**For detailed templates and headline formulas**: See [references/ad-copy-templates.md](references/ad-copy-templates.md)

---

## Audience Understanding & Targeting

Understand relevant audience needs, jobs, objections, and language using permitted research. Collect only the minimum necessary, consented data; do not gather sensitive identifiers or upload customer lists without explicit authorization and a valid use basis.

What's changed in 2026 is **where you apply that knowledge.** As ad-platform algorithms have gotten dramatically better at finding the right person, jamming all your audience identifiers into the platform's *targeting filters* underperforms feeding those same identifiers into the *creative* (headlines, copy, visuals, hooks, examples).

The discipline now: **audience knowledge → creative first, targeting filters second.** How much that ratio tips toward "creative" varies meaningfully by platform.

### Platform-by-platform: where to apply audience knowledge

| Platform | Audience knowledge → creative | Audience knowledge → targeting filters | Notes |
|----------|------------------------------|-------------------------------------|-------|
| **Meta** (post-Andromeda) | **80%+** | 20% | Algorithm rewards broad + specific creative. See [Meta creative patterns](references/meta-creative-patterns.md) below for the full reframe. Interest-stacking now actively hurts. |
| **Google Search** | 40% | **60%** | Keywords are still the dominant signal — match-types, search-intent layering, and negative keywords still drive performance. Creative (RSA headlines) matters but is downstream of the keyword. |
| **Google Performance Max / Demand Gen** | **70%** | 30% | Audience signals are advisory, not deterministic. Creative + product feed quality dominate. |
| **LinkedIn** | 40% | **60%** | Job-title / company / industry filters still produce real precision because LinkedIn's identity data is high-quality. Creative makes the click; firmographics make the *right person* see it. |
| **TikTok** | **70%** | 30% | Algorithm is closer to Meta's model — broad targeting + native-feeling creative wins. Some audience interests help but creative dominates. |
| **Twitter/X** | 50% | 50% | Interest + follower targeting still meaningful, but creative differentiation is high-leverage given lower competition. |

These ratios are directional, not precise. Test in your actual account.

### Applying audience knowledge to creative

Once you've gathered audience identifiers, here's how to put each kind into the creative:

- **Demographic identifiers** (age, location, occupation) → embed as identity-trigger keywords in headlines (see [[#The one-keyword hack (identity-trigger keywords)]])
- **Pain points + fears** → headline + first line of body copy (Sabri Suby's framing: "the verbatim words your customers use about the problem")
- **Hopes / desired outcomes** → transformation copy + CTAs
- **Objections + "why they didn't buy last time"** → objection-handling retargeting ads (see [[#The 4-component retargeting framework]])
- **Their language / vocabulary** → the entire copy voice — never use industry jargon they don't
- **Existing customer base** → still feed it for lookalike audiences (see Key Concepts below)
- **Niche / segment they identify with** → identity-trigger keywords in headline ("for dentists" / "for B2B founders" / "for parents of toddlers")

### Key Concepts (still apply)

- **Lookalikes**: Base on best customers (by LTV), not all customers. Still high-value across platforms.
- **Retargeting**: Segment by funnel stage (visitors vs. cart abandoners). See [[#Retarget with DIFFERENT offers (not the same one)]] and [[#The 4-component retargeting framework]] for the modern playbook.
- **Exclusions**: Exclude existing customers and recent converters — showing ads to people who already bought wastes spend.

### Common failure mode

Trying to make up for weak creative with hyper-precise targeting. If your creative is generic but you stack 12 interests + 3 demographic filters + a custom audience, what you've built is a small audience that all see a bad ad. Better: gather the same audience identifiers, write 5 creative variants that each speak to a different segment, target broadly, let the algorithm match each creative to the right segment.

**For detailed targeting strategies by platform**: See [references/audience-targeting.md](references/audience-targeting.md)

---

## Meta creative patterns

For Meta-specific format, targeting, and variant hypotheses, read [Meta creative patterns](references/meta-creative-patterns.md) only when that platform is in scope. Use account evidence and the decision-system reference rather than treating practitioner anecdotes as universal rules.

## Creative Best Practices

### Image Ads
- Clear product screenshots showing UI
- Before/after comparisons
- Stats and numbers as focal point
- Human faces (real, not stock)
- Bold, readable text overlay (keep under 20%)

### Video Ads Structure (15-30 sec)
1. Hook (0-3 sec): Pattern interrupt, question, or bold statement
2. Problem (3-8 sec): Relatable pain point
3. Solution (8-20 sec): Show product/benefit
4. CTA (20-30 sec): Clear next step

**Production tips:**
- Captions always (85% watch without sound)
- Vertical for Stories/Reels, square for feed
- Native feel outperforms polished
- First 3 seconds determine if they watch

### Creative Testing Hierarchy
1. Concept/angle (biggest impact)
2. Hook/headline
3. Visual style
4. Body copy
5. CTA

---

## Campaign Optimization

For hard kill/keep/scale thresholds, use the platform playbooks (see Reference Routing): the kill rules and breakeven CPL/CPC math live in [b2b-paid-playbook.md](references/b2b-paid-playbook.md), and Meta's full decision tree lives in [meta-decision-system.md](references/meta-decision-system.md).

### Key Metrics by Objective

| Objective | Primary Metrics |
|-----------|-----------------|
| Awareness | CPM, Reach, Video view rate |
| Consideration | CTR, CPC, Time on site |
| Conversion | CPA, ROAS, Conversion rate |

### Optimization Levers

**If CPA is too high:**
1. Check landing page (is the problem post-click?)
2. Tighten audience targeting
3. Test new creative angles
4. Improve ad relevance/quality score
5. Adjust bid strategy

**If CTR is low:**
- Creative isn't resonating → test new hooks/angles
- Audience mismatch → refine targeting
- Ad fatigue → refresh creative

**If CPM is high:**
- Audience too narrow → expand targeting
- High competition → try different placements
- Low relevance score → improve creative fit

### Bid Strategy Progression
1. Start with manual or cost caps
2. Gather conversion data (50+ conversions)
3. Switch to automated with targets based on historical data
4. Monitor and adjust targets based on results

---

## Retargeting Strategies

### Funnel-Based Approach

| Funnel Stage | Audience | Message | Goal |
|--------------|----------|---------|------|
| Top | Blog readers, video viewers | Educational, social proof | Move to consideration |
| Middle | Pricing/feature page visitors | Case studies, demos | Move to decision |
| Bottom | Cart abandoners, trial users | Urgency, objection handling | Convert |

### Retargeting Windows

| Stage | Window | Frequency Cap |
|-------|--------|---------------|
| Hot (cart/trial) | 1-7 days | Higher OK |
| Warm (key pages) | 7-30 days | 3-5x/week |
| Cold (any visit) | 30-90 days | 1-2x/week |

### Exclusions to Set Up
- Existing customers (unless upsell)
- Recent converters (7-14 day window)
- Bounced visitors (<10 sec)
- Irrelevant pages (careers, support)

### Retarget with DIFFERENT offers (not the same one)

Practitioner frameworks suggest testing a different offer when research indicates offer mismatch. Do not assume it is the main reason for non-purchase; timing, trust, fit, price, usability, and measurement errors may also explain the observed behavior.

Instead, retarget with **different** products, services, or offers from your catalog:
- Visitor clicked on protein powder, didn't buy → retarget with creatine (totally different category)
- Visitor downloaded a lead magnet, didn't book a call → retarget with a different lead magnet on a related topic
- Visitor viewed pricing, didn't sign up → retarget with a free audit or assessment instead

A different offer is a hypothesis, not an expected ROAS lift. Compare contribution margin and qualified conversions at sufficient volume before expanding it.

### The 4-component retargeting framework

Choose from these four retargeting concepts according to audience size, budget, evidence, and test isolation; they need not run simultaneously:

1. **Objection-handling ad** — addresses reasons supported by consented interviews, support themes, or supplied research. Any customer contact needs authorization; do not call every lead or assume permission to reuse quotations.
2. **Proof testimonial carousel** — multi-image/multi-slide carousel of testimonials and proof that supports the claims of your original ad
3. **Other-offers CBO** — your other best-performing ads for other products/services in one CBO, retargeted to the same audience
4. **Value-first audit/assessment ad** — wraps your call in a free piece of value. Whether they buy or not, they leave with something useful. Lowers the friction to engage.

Avoid audience overlap and fragmented delivery. Evaluate incremental qualified conversions and economics; these concepts do not guarantee a funnel-wide lift.

---

## Landing Page Alignment (the headline-mirror trick)

Ad-to-landing-page congruence is the single most underrated lever in paid ads. Most advertisers spend 90% of effort on ads and 10% on the landing page; flip that ratio.

### Headline mirroring

Ad headline results can suggest message-match hypotheses, but delivery optimization, audience selection, and clicks are not randomized landing-page conversion evidence. Evaluate downstream outcomes and use a controlled page test where traffic permits.

The play:

1. Select a manageable number of headline variants based on traffic, conversion volume, budget, and a predeclared test design
2. Identify the best-performing headline (by CTR + downstream conversion)
3. **Mirror that winning headline on your landing page** — exact wording in the H1, sub-headline, and lead-in copy of the body
4. Measure the page-level effect against a control, with uncertainty and guardrails. No minimum lift is promised; the change may be neutral or harmful.

Consistent promises may reduce confusion, but exact wording is not always best. Keep claims truthful and test whether message match improves the intended conversion for the evaluated traffic.

### Match testing cadence to evidence and capacity

Maintain a prioritized experiment backlog, not a mandatory number of simultaneous tests. Check baseline rates, minimum detectable effect, eligible sample size, duration, interference, budget, and implementation capacity before launching.

Low-volume funnels may support only one test or qualitative research first. Parallel tests need independent populations or an explicit interaction-aware design. Do not multiply assumed lifts; use measured effects and uncertainty.

## Reporting & Analysis

### Weekly Review
- Spend vs. budget pacing
- CPA/ROAS vs. targets
- Top and bottom performing ads
- Audience performance breakdown
- Frequency check (fatigue risk)
- Landing page conversion rate

### Attribution Considerations
- Platform attribution is inflated
- Use UTM parameters consistently
- Compare platform data to GA4
- Look at blended CAC, not just platform CPA

### Scaling discipline (net cash > ROAS percentage)

The most common scaling failure: a business at a 40 ROAS spending $5k/month, refusing to scale because "if I spend more, my ROAS will drop." This is the wrong frame.

**Net cash flow > ROAS percentage at the business level:**
- ROAS dropping from 10 → 5 sounds bad
- Higher spend can increase or decrease profit; compare incremental gross profit after ad costs, delivery costs, refunds, and cash constraints.
- The number to optimize is **blended ROAS at the business level**, not per-ad-set ROAS
- Even better: optimize **net free cash flow**, not ROAS at all

**Find your break-even ROAS:**
1. Calculate the absolute maximum you can pay to acquire a customer and still be profitable (factoring LTV)
2. That's your break-even ROAS / CPA ceiling
3. Propose a bounded scaling test only if marginal economics, lead quality, payback, cash runway, and uncertainty support it; obtain approval before spend changes.

**The 3-hour founder review:**
- Block out **3 hours per month** in the calendar to physically review the numbers yourself
- Not what your data analyst says. Not what your media buyer says. You, going through the actual data
- The confidence this generates is irreplaceable — and confidence is what lets you scale with conviction
- "Data gives you confidence. Confidence gives you speed."

**Outbound-call your leads who didn't convert:**
- Invite a relevant, consented sample to research only when outreach is authorized; do not assume that downloading content authorizes a sales call
- Ask why they didn't book, what was confusing, what the actual blocker was
- These verbatim answers become objection-handling ads (see Retargeting section)
- Massive insight-to-creative loop that most advertisers skip

---

## Platform Setup

Before launching campaigns, ensure proper tracking and account setup.

**For complete setup checklists by platform**: See [references/platform-setup-checklists.md](references/platform-setup-checklists.md)

**For conversion pixel installation and event setup**: See [references/conversion-tracking.md](references/conversion-tracking.md)

### Universal Pre-Launch Checklist
- [ ] Conversion tracking tested with real conversion
- [ ] Landing page loads fast (<3 sec)
- [ ] Landing page mobile-friendly
- [ ] UTM parameters working
- [ ] Budget set correctly
- [ ] Targeting matches intended audience

---

## Google RSA Output Spec (mandatory when generating RSAs)

When the user requests Google Ads RSAs, load [references/rsa-output-spec.md](references/rsa-output-spec.md) and follow it exactly — hard character limits, required sidecar artifacts (ad groups, negatives, sitelinks, callouts), output order, template shape, CFM medical compliance, and the pre-send self-check. Do not output any RSA that violates it.

---

## Common Mistakes to Avoid

### Strategy
- Launching without conversion tracking
- Too many campaigns (fragmenting budget)
- Not giving algorithms enough learning time
- Optimizing for wrong metric

### Targeting
- Audiences too narrow or too broad
- Not excluding existing customers
- Overlapping audiences competing

### Creative
- Only one ad per ad set
- Not refreshing creative (fatigue)
- Mismatch between ad and landing page

### Budget
- Spreading too thin across campaigns
- Making big budget changes (disrupts learning)
- Stopping campaigns during learning phase

---

## Task-Specific Questions

1. What platform(s) are you currently running or want to start with?
2. What's your monthly ad budget?
3. What does a successful conversion look like (and what's it worth)?
4. Do you have existing creative assets or need to create them?
5. What landing page will ads point to?
6. Do you have pixel/conversion tracking set up?

---

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/REGISTRY.md). Key advertising platforms:

| Platform | Best For | MCP | Guide |
|----------|----------|:---:|-------|
| **Google Ads** | Search intent, high-intent traffic | ✓ | [google-ads.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/google-ads.md) |
| **Meta Ads** | Demand gen, visual products, B2C | - | [meta-ads.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/meta-ads.md) |
| **LinkedIn Ads** | B2B, job title targeting | - | [linkedin-ads.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/linkedin-ads.md) |
| **TikTok Ads** | Younger demographics, video | - | [tiktok-ads.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/tiktok-ads.md) |

For tracking setup, see [references/conversion-tracking.md](references/conversion-tracking.md), [ga4.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/ga4.md), [segment.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/segment.md)

---

## Related Skills

- **ad-creative**: For generating and iterating ad headlines, descriptions, and creative at scale
- **revops**: For the CRM side of ABM — lead scoring, routing, and the offline conversion loop
- **customer-research**: For the voice-of-customer inputs that feed ad copy and creative angles
- **copywriting**: For landing page copy that converts ad traffic
- **analytics**: For proper conversion tracking setup
- **ab-testing**: For landing page testing to improve ROAS
- **cro**: For optimizing post-click conversion rates
