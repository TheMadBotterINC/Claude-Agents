### Machine-Readable Files for AI Agents

> **Google's stance**: not required for AI Overviews or AI Mode. Their guide explicitly says you don't need new markup, AI files, or markdown to appear in generative AI search.
>
> **Why include them anyway**: extractable structure can help compatible clients consume content, but specific file conventions are not established universal visibility signals. Evaluate adoption, maintenance cost, and observed use.

AI agents aren't just answering questions — they're becoming buyers. When an AI agent evaluates tools on behalf of a user, it needs structured, parseable information. Opaque or inaccessible pricing may limit automated comparison; do not claim agents will necessarily skip the product or recommend a competitor.

Consider these optional files when they serve verified client needs; keep them synchronized with canonical information and stage changes for authorized publication:

**`/pricing.md` or `/pricing.txt`** — Structured pricing data for AI agents

```markdown
# Pricing — [Your Product Name]

## Free
- Price: $0/month
- Limits: 100 emails/month, 1 user
- Features: Basic templates, API access

## Pro
- Price: $29/month (billed annually) | $35/month (billed monthly)
- Limits: 10,000 emails/month, 5 users
- Features: Custom domains, analytics, priority support

## Enterprise
- Price: Custom — contact sales@example.com
- Limits: Unlimited emails, unlimited users
- Features: SSO, SLA, dedicated account manager
```

**Why this matters now:**
- AI agents increasingly compare products programmatically before a human ever visits your site
- Opaque pricing may constrain some automated buying journeys; validate behavior rather than assuming exclusion
- A simple markdown file is trivially parseable by any LLM — no rendering, no JavaScript, no login walls
- Same principle as `robots.txt` (for crawlers), `llms.txt` (for AI context), and `AGENTS.md` (for agent capabilities)

**Best practices:**
- Use consistent units (monthly vs. annual, per-seat vs. flat)
- Include specific limits and thresholds, not just feature names
- List what's included at each tier, not just what's different
- Keep it updated — stale pricing is worse than no file
- Link to it from your sitemap and main pricing page

**`/llms.txt`** — Context file for AI systems (see [llmstxt.org](https://llmstxt.org))

If relevant clients support the convention and maintenance is justified, propose an `llms.txt` that gives AI systems a quick overview of what your product does, who it's for, and links to key pages (including your pricing).

**`/okf/` — Open Knowledge Format bundle (Google-backed, v0.1)**

Google [introduced OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) in June 2026 — a markdown spec for representing site content as a directory of cross-linked files with YAML frontmatter, agent-readable without scraping. Built primarily for data-team catalog metadata; the site-readable-by-agents repurposing was popularized by Suganthan Mohanadasan. No confirmed AI-search ranking signal today — treat it as protocol-layer registration like early schema.org. **For the full breakdown, implementation paths (free generator, WordPress plugin, by-hand), hosting guidance, and when to skip, see [references/okf.md](okf.md).**

