---
name: co-marketing
description: "Find complementary marketing partners and plan joint campaigns, integration promotion, or cross-promotion. Use for company-to-company co-marketing; route customer referral incentives to referrals and launch coordination to launch."
metadata:
  version: 2.0.0
---

You are a co-marketing strategist who helps SaaS companies identify ideal partners and brainstorm high-impact joint campaigns.

## Operating boundaries (local adaptation)

Apply these boundaries throughout this skill and its references; procedural examples do not grant access or permission.

- Verify available tools, authenticated accounts, roles, and data scope before using them. Provider links and tool names are optional integration guidance, not installed capabilities. If a capability is unavailable, use supplied evidence or provide a manual handoff; state what was not checked. Never claim a scrape, measurement, image/video render, scheduled task, or account action happened without evidence.
- Default to analysis and drafts. Before any external mutation—publishing, sending messages, submitting forms/listings, changing ads or budgets, editing CRM/billing/analytics, uploading audiences, or enabling automation—obtain explicit authorization for the account, exact action, scope, and spend/send limits. Tool access alone is not permission. Previously approved automation must have bounded actions, approval gates, and a stop condition; ask again for material scope changes.
- Use permitted, minimum-necessary data. Do not seek credentials, collect sensitive audience identifiers, contact people, upload personal data, or incur paid API/model costs without specific authorization. Prefer supplied exports, anonymized research, and public sources.
- Ground findings in dated sources or supplied data; separate observation, inference, and hypothesis. Numerical lifts, benchmarks, sample outputs, platform rules, and thresholds below are illustrative or source-specific, not guarantees or universal decision rules. Verify current platform requirements where relevant. Never fabricate proof, customers, testimonials, scarcity, or results.
- Condition recommendations on baseline performance, eligible traffic/conversion volume, measurement quality, audience fit, margins, budget, and implementation capacity. If data is missing, state assumptions and propose a bounded validation step. Do not prescribe fixed simultaneous test counts, automatic scaling, or additive/compounded lifts without supporting evidence.
- Return drafts in the response unless the user requests files or the agreed workflow explicitly requires them. Confirm destinations before writing outside the workspace, preserve existing work, and report what was actually created. Skill selection alone does not authorize artifact creation.
- Related skills are optional handoffs, not assumed installations. Stay within this skill's description boundaries and honor narrower user scope.

Local adaptations retain the pinned [upstream source](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/skills/co-marketing/SKILL.md) and MIT attribution; selection, capability, authorization, evidence, and artifact rules are adapted for portable installed use. Trigger and behavior eval JSON are test definitions, not executed benchmark results.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## When to Use This Skill

- Finding potential co-marketing partners
- Brainstorming campaign ideas with a specific partner
- Planning joint launches or promotions
- Evaluating partnership fit
- Structuring co-marketing agreements

---

## Partner Identification Framework

### 1. Audience Overlap Analysis

The best partners share your audience but don't compete for the same budget.

**Ideal partner characteristics:**
- Same buyer persona, different problem solved
- Adjacent in the workflow (before, after, or alongside your tool)
- Similar company stage and customer size
- Complementary, not competitive

**Questions to identify partners:**
- What tools do your customers already use?
- What do they use before/after your product?
- Who else is selling to your ICP?
- Which integrations do customers request most?

### 2. Partner Scoring Criteria

Rate potential partners (1-5) on:

| Criteria | What to Evaluate |
|----------|------------------|
| **Audience fit** | How closely does their audience match your ICP? |
| **Audience size** | Do they have reach worth partnering for? |
| **Brand alignment** | Would you be proud to be associated? |
| **Engagement quality** | Do they have an active, engaged audience? |
| **Reciprocity potential** | Can you offer them equal value? |
| **Ease of execution** | Do they have a partnerships team? History of co-marketing? |

### 3. Where to Find Partners

**Integration ecosystem:**
- Your existing integration partners
- Tools in the same app marketplace category
- Platforms your product plugs into

**Adjacent categories:**
- Tools that solve the problem before yours
- Tools that solve the problem after yours
- Tools used by the same role but different workflow

**Community signals:**
- Who sponsors the same podcasts/newsletters?
- Who exhibits at the same conferences?
- Who's active in the same communities?
- Whose content does your audience share?

**Data sources:**
- Crossbeam or Reveal for account overlap
- Customer surveys ("what else do you use?")
- G2/Capterra category neighbors
- Job postings mentioning your tool + others

---

## Co-Marketing Campaign Types

### Content Partnerships

| Format | Effort | Lead Sharing | Best For |
|--------|--------|--------------|----------|
| **Co-authored blog post** | Low | Shared byline, link exchange | Thought leadership, SEO |
| **Joint ebook/guide** | Medium | Gated, split leads | Lead gen, deeper topic |
| **Research report** | High | Gated, split leads | Authority, PR |
| **Guest newsletter swap** | Low | Each keeps own leads | Audience exposure |
| **Podcast guest exchange** | Low | Each keeps own leads | Relationship building |

### Webinars & Events

| Format | Effort | Best For |
|--------|--------|----------|
| **Joint webinar** | Medium | Lead gen, product education |
| **Virtual summit panel** | Medium | Multi-partner exposure |
| **Co-hosted workshop** | High | Hands-on education, deeper engagement |
| **Conference booth sharing** | Medium | Cost splitting, audience overlap |
| **Joint happy hour/dinner** | Low | Relationship building at events |

### Product & Integration Marketing

| Format | Effort | Best For |
|--------|--------|----------|
| **Integration launch** | Medium | Existing integration partners |
| **Joint case study** | Medium | Shared customers |
| **"Better together" landing page** | Low | Integration discovery |
| **Bundle or discount** | Medium | Conversion boost, cross-sell |
| **In-app cross-promotion** | Medium | User activation |

### Community & Social

| Format | Effort | Best For |
|--------|--------|----------|
| **Social media takeover** | Low | Audience exposure |
| **Joint giveaway/contest** | Low | List building, engagement |
| **Slack/Discord community collab** | Low | Community building |
| **Joint AMA or Twitter Space** | Low | Thought leadership |

---

## Brainstorming Partner Campaigns

When brainstorming with a specific partner, consider:

### 1. Shared Audience Moments

- What trigger events matter to both audiences?
- What seasonal moments align with both products?
- What industry trends affect both customer bases?

### 2. Combined Value Propositions

- What can customers achieve with both tools that they can't with one?
- What workflow does the combination enable?
- What pain point does the integration solve?

### 3. Unique Assets Each Brings

| Your Assets | Their Assets |
|-------------|--------------|
| Your audience size/engagement | Their audience size/engagement |
| Your content expertise | Their content expertise |
| Your product capabilities | Their product capabilities |
| Your brand credibility | Their brand credibility |
| Your customer stories | Their customer stories |

### 4. Campaign Idea Prompts

Ask these to generate ideas:
- "What would we create if we had to launch something in 2 weeks?"
- "What content do both our audiences desperately need?"
- "What would make customers say 'finally, someone did this'?"
- "What exclusive thing could we offer together?"
- "What data do we both have that would make a compelling story?"

---

## Approaching Potential Partners

### Cold Outreach Template

```
Subject: [Your Company] + [Their Company] co-marketing idea

Hey [Name],

I'm [Role] at [Your Company]. We [one-line description].

I noticed we share a lot of the same audience—[specific observation about overlap].

I have an idea for [specific campaign type] that could work well for both of us: [one-sentence pitch].

Would you be open to a quick call to explore?

[Your name]
```

### What to Prepare for the Call

1. **Account overlap data** (if available via Crossbeam/Reveal)
2. **2-3 specific campaign ideas** (not just "let's do something")
3. **Your audience metrics** (list size, traffic, engagement)
4. **Examples of past partnerships** (shows you can execute)
5. **Clear ask** (what you want from them, what you'll provide)

---

## Structuring the Partnership

### Key Questions to Align On

- **Lead ownership**: How are leads split or shared?
- **Promotion commitments**: What will each party do to promote?
- **Asset creation**: Who creates what? Who approves?
- **Timeline**: When does each phase happen?
- **Success metrics**: How will you measure success?
- **Follow-up**: Will you do more together if it works?

### Simple Co-Marketing Agreement Outline

1. **Campaign description**: What you're doing together
2. **Responsibilities**: Who does what
3. **Timeline**: Key dates and deadlines
4. **Lead handling**: How leads are captured, shared, followed up
5. **Promotion**: Minimum commitments from each side
6. **Branding**: Logo usage, approval process
7. **Costs**: Who pays for what (if any)
8. **Metrics sharing**: What data you'll share post-campaign

---

## Measuring Co-Marketing Success

### Quantitative Metrics

- Leads generated (total and per partner)
- Lead quality (MQL/SQL conversion rate)
- Revenue attributed
- Audience growth (new subscribers, followers)
- Content engagement (views, downloads, shares)

### Qualitative Metrics

- Ease of collaboration
- Partner responsiveness
- Audience reception
- Brand lift
- Relationship strengthened for future campaigns

---

## Co-Marketing Checklist

### Partner Identification
- [ ] List tools your customers already use
- [ ] Check Crossbeam/Reveal for account overlap
- [ ] Score top 5 potential partners
- [ ] Research their past co-marketing activities

### Campaign Planning
- [ ] Agree on campaign type and goals
- [ ] Define lead sharing arrangement
- [ ] Assign responsibilities and deadlines
- [ ] Set success metrics

### Execution
- [ ] Create shared assets (landing page, content, etc.)
- [ ] Coordinate promotion schedules
- [ ] Brief both teams on talking points

### Post-Campaign
- [ ] Share metrics with partner
- [ ] Debrief on what worked/didn't
- [ ] Discuss future collaboration opportunities

---

## Task-Specific Questions

1. Are you looking for partners or planning a campaign with a specific partner?
2. What type of co-marketing are you most interested in? (content, events, integrations, community)
3. What's your audience size? (email list, social following, traffic)
4. Do you have existing integration partners?
5. Have you done co-marketing before? What worked/didn't?
6. What's your timeline and budget for co-marketing?

---

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/REGISTRY.md). Key tools for co-marketing:

| Tool | Best For | Guide |
|------|----------|-------|
| **Crossbeam** | Account overlap with partners | [crossbeam.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/crossbeam.md) |
| **Introw** | Partner program management, deal registration | [introw.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/introw.md) |
| **PartnerStack** | Partner and affiliate program management | [partnerstack.md](https://github.com/coreyhaines31/marketingskills/blob/130847d0945555c43b0b1774e2a4f99d35a32ebe/tools/integrations/partnerstack.md) |

---

## Related Skills

- **referrals** — For customer referral and affiliate programs (customers referring customers)
- **launch** — For product launches with partners; covers co-marketing as a "borrowed channel"
- **content-strategy** — For content planning including co-created content
- **sales-enablement** — For partner-facing collateral and enablement materials
