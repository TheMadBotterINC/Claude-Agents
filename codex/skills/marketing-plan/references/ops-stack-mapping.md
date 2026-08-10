# Marketing Operations Stack — Skills + Available Connectors per AARRR Stage

This doc maps every marketing skill and relevant connector/API capability to the AARRR stage(s) it primarily serves. It's the source for Section 11 of every plan.

> **Capability note.** Treat every tool below as optional. Verify that the connector, API, CLI, or browser capability is configured and authorized before using or naming it as current-state infrastructure. When a capability is unavailable, use a manual fallback where practical or mark it as future/not configured in Section 13. For browser work, use whichever user-authorized browser capability is available; for diagrams, use an available diagram capability or repository-native Markdown/Mermaid.

## The thesis

A small team + fCMO + agentic tooling may increase execution capacity, but any comparison with a 15–20-person traditional marketing org is a hypothesis that requires client-specific evidence. The skills and connectors encode workflows that previously required dedicated headcount per channel.

The plan's Section 11 makes this thesis explicit by:
1. Mapping skills to stages so the founder sees which skills execute which work
2. Mapping verified connectors/APIs to stages so the founder sees the tooling layer
3. Naming a concrete operational example that proves the stack works
4. Showing capability unlocks by funding stage (pre-seed → seed → Series A)

## Marketing skills mapped to AARRR

### Acquisition skills

| Skill | What it does | Primary use in Acquisition |
|---|---|---|
| `seo-audit` | Audit site for technical and on-page SEO | Quarterly site health checks |
| `ai-seo` | Optimize content for AI search engines / LLM citation | Future-proof content strategy |
| `programmatic-seo` | Build template-driven SEO pages at scale | Location, comparison, integration page systems |
| `schema` | Add structured data markup | Rich snippets, eligibility for AI citation |
| `content-strategy` | Plan content topics, pillars, cadence | Setting the editorial calendar |
| `competitors` | Build vs-pages and alternative-to-pages | Capture high-intent SERPs against competitors |
| `ads` | Plan and structure paid campaigns | Apple Search Ads, Meta, Google, LinkedIn |
| `ad-creative` | Generate ad variations and creative | Iterate ad creative across platforms |
| `social` | Plan and write social media content | LinkedIn, Twitter/X, Instagram, TikTok |
| `typefully` | Schedule/post tweets, threads, LinkedIn content | Cadence operations for founder-led channels |
| `cold-email` | Write B2B cold outreach + sequences | Outbound for B2B SaaS / hybrid businesses |
| `analytics` | Set up tracking, GA4, conversion events | Funnel instrumentation |
| `free-tools` | Plan engineering-as-marketing free tools | Build tools that generate links + leads |
| `marketing-website-design` | Design marketing sites with intention | Pillar/landing page design |
| `launch` | Plan and execute launches (Product Hunt, GA, feature launches) | GTM moments — strategy + tactical execution |

### Activation skills

| Skill | What it does | Primary use in Activation |
|---|---|---|
| `onboarding` | Optimize user onboarding flows | Onboarding rebuild, activation rate tests |
| `signup` | Optimize signup/registration | Reduce friction at top of activation |
| `cro` | Optimize any marketing page or form | Conversion testing across pages, forms, landing pages |
| `paywalls` | Optimize paywalls and upgrade screens | Trial → paid conversion (also Revenue) |
| `popups` | Optimize popups, modals, slide-ins | Lead capture + activation prompts |
| `copywriting` | Write marketing copy | Onboarding screens, paywall copy, CTAs |
| `copy-editing` | Edit and improve existing copy | Voice / clarity pass before ship |
| `copycraft` | Real-time copy variation overlay | Live copy iteration during reviews |
| `website-copy` | Write full website copy (stage-8 from CF process) | Comprehensive site copy production |
| `ab-testing` | Plan A/B tests | Structure for onboarding variant tests |
| `marketing-psychology` | Apply behavioral science to copy and CRO | Persuasion principles in activation moments |

### Retention skills

| Skill | What it does | Primary use in Retention |
|---|---|---|
| `emails` | Design email sequences | Customer.io / Mailchimp / Resend flow building |
| `churn-prevention` | Build cancellation flows, save offers, win-back | Reduce churn, recover failed payments |
| `copywriting` / `copy-editing` | Email copy production | Lifecycle email content |
| `paywalls` | (cross-cuts) — upgrade prompts in retention emails | Upsell within lifecycle |
| `ab-testing` | Test email variants | Subject line, CTA, timing tests |

### Referral skills

| Skill | What it does | Primary use in Referral |
|---|---|---|
| `referrals` | Plan and launch referral / affiliate / ambassador programs | Core skill for Section 7 |
| `social` | Create ambassador-shareable content | Talking points, post templates |
| `copywriting` | Ambassador / affiliate email copy | Recruitment, onboarding, communication |
| `marketing-website-design` | Per-ambassador landing pages | Attribution surface |
| `emails` | Ambassador lifecycle emails | Onboarding, monthly digest, payout notifications |

### Revenue skills

| Skill | What it does | Primary use in Revenue |
|---|---|---|
| `pricing` | Audit and optimize pricing | Plan tier structure, annual defaults, value metrics |
| `paywalls` | Paywall optimization | Trial → paid, free → paid conversion |
| `sales-enablement` | Build sales decks, one-pagers, demos | B2B sales support material |
| `revops` | Revenue operations, lead lifecycle | Marketing → sales handoff |
| `ab-testing` | Pricing experiments | Test annual default, intro pricing, tier consolidation |

### Cross-cutting / brand foundation skills

| Skill | What it does | Primary use |
|---|---|---|
| `product-marketing` | Set up the `.agents/product-marketing.md` context file (positioning, ICP, voice) | Foundational — run first; every section of the plan references this |
| `customer-research` | Conduct customer interviews + surveys | Section 2 + Section 3 (Current state) |
| `marketing-psychology` | Apply behavioral science | Cross-cuts copy, CRO, paywalls |
| `marketing-ideas` | The 139-idea library | Section 12 of plan (Idea bank) |

## Connectors and APIs mapped to AARRR

### Acquisition tooling

| Tool | What it provides | Availability / authorization check |
|---|---|---|
| **Ahrefs API** | SEO data: keyword research, backlinks, competitor analysis | Required `AHREFS_API_KEY` in `.env` |
| **DataForSEO API** | SERP data, keyword volume, competitor SERP analysis | Required API key |
| **GA4 connector/API** | Traffic by channel, conversion events, retention curves | Verify configured project and authorized credentials |
| **GitHub connector or CLI** | Repo work: marketing site (`site-name-promo` patterns), content authoring | Verify repository access and authorization |
| **Typefully connector/API** | Social posting (LinkedIn, X, Threads, Bluesky) | Verify account, API access, and posting authorization |
| **Google Ads connector/API** | Ad account management, campaign creation, performance pulls | Verify account access; changes require explicit authorization |
| **Configured browser automation** | Browser research, form assistance, screenshots, and permitted extraction | Verify capability, session authorization, and platform terms |
| **defuddle** | Clean markdown extraction from web pages | CLI install |
| **Notion** | Internal knowledge directory access | Notion API key |
| **Stripe connector/API** | LTV math, paid-CAC reconciliation (cross-cuts to Revenue) | Verify account access and least-privilege credentials |

### Activation tooling

| Tool | What it provides |
|---|---|
| **App Store Connect** | Conversion rate by listing variant, install funnel; use manual export or a configured browser/connector |
| **GitHub connector or CLI** | Mobile app repo for onboarding code edits |
| **Configured design connector** | Figma, Pencil, or another available design capability for onboarding iteration |
| **Customer.io connector/API** | In-app messaging + lifecycle email coordination |
| **Stripe connector/API** | Subscription state for paywall logic |
| **GA4 connector/API** | Activation events instrumentation |

### Retention tooling

| Tool | What it provides |
|---|---|
| **Customer.io connector/API** | The retention infrastructure — flow building, segmentation, sending |
| **Shopify** | Hardware buyer events as lifecycle triggers |
| **Stripe connector/API** | Subscription state, churn cohorts, plan changes |
| **GA4 connector/API** | Session events, retention curves |
| **Resend / Mailchimp / SendGrid** | Alternatives to Customer.io for different stacks |

### Referral tooling

| Tool | What it provides |
|---|---|
| **Dub.co** | Ambassador attribution, short links, per-ambassador tracking |
| **Stripe connector/API** | Commission accounting + payouts via Connect |
| **GitHub connector or CLI** | Per-ambassador landing pages |
| **Customer.io connector/API** | Ambassador lifecycle (recruitment → onboarding → monthly digest → payout notifications) |
| **Rewardful / Tolt / Mention Me** | Alternatives to Dub for affiliate management |

### Revenue tooling

| Tool | What it provides |
|---|---|
| **Stripe connector/API** | Pricing tests, subscription analytics, churn cohort analysis, blended CAC math |
| **Shopify** | Hardware transactions |
| **GA4 connector/API** | Revenue events |
| **Customer.io connector/API** | Paywall / pricing-related lifecycle |
| **Notion** | Commercial knowledge directory |

### Cross-cutting tooling

| Tool | What it provides |
|---|---|
| **Notion** | Shared knowledge base |
| **GitHub connector or CLI** | Shared context repo (`{client-org}/{client-context}`) |
| **defuddle** | Research extraction |
| **obsidian-cli** | Working notes for fCMO |
| **Configured design connector** | Pencil, Figma, or another available design-file capability |

## Capability unlocks by funding stage

The plan's Section 11 must include this table (or equivalent), specific to the client's current and projected funding stages.

| Stage | Headcount | Tooling | Channels live |
|---|---|---|---|
| **Pre-seed / bootstrapped** | fCMO + founder team | Current verified tooling + marketing-skills library + configured integration layer | Organic only (SEO, content, App Store, founder-led social, events, WOM, ambassador) |
| **Seed close** | + first marketing hire (lifecycle/content owner) | + paid ad accounts (Apple Search Ads, Meta, LinkedIn) + `ads` skill activated | + paid acquisition pilot ($5–15K/mo — see `funding-stage-unlocks.md` for canonical tiers) |
| **Seed deployment** | + designer (potentially fractional) | + analytics expansion (Mixpanel / Amplitude if needed) | + paid scaling ($20–50K/mo) + first launches (PH, GA) |
| **Series A** | + performance marketing lead + content lead | + dedicated tooling spend ($2–5K/mo software) + sponsored event budget | + paid scaling ($50–150K/mo) + international consideration + B2B vertical expansion |
| **Series B+** | Full-stack marketing org (10+ people) | + agency partnerships + PR firm | + brand campaigns + acquisitions + sponsorships at category level |

## The concrete-example test

Section 11 of the plan must include at least one concrete operational example that proves the stack thesis. The example should be:
- A specific event (not abstract claim)
- From this client's actual history if possible (most credible)
- Tied to a non-technical person executing via the stack (proves it works without dedicated engineering)

Examples from real engagements:
- *"On the kickoff call, Alex drafted a working Customer.io abandoned-cart flow live using the configured Customer.io connector. This provided evidence that a non-technical founder could use the skill pattern independently."*
- *"In two weeks, the team scaled from 0 to 14 ranking keywords using `programmatic-seo` with authorized Ahrefs and GitHub access — no dedicated SEO hire was required for that scoped result."*
- *"The first email campaign generated a 24% reply rate after `cold-email` plus authorized GA4 and Stripe data produced a verified target list of users with high LTV but no recent activity."*

If the client has no such moment in their history yet, frame the example as the *first move* — "Here's the demonstration the team will run in week one to validate the stack:"

## When the stack doesn't apply (yet)

For clients without the needed connectors set up, frame Section 11 differently:
- List the skills that DO apply with current tooling
- Name which connectors would unlock which sections of the plan
- Treat connector setup as a priority only when its value and operating cost justify it

A plan can't claim the agentic-stack thesis if the required capabilities are not configured and evidenced. Be honest about state.
