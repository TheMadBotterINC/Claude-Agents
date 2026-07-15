# Capability and Optional Provider Reference for Competitor Profiling

Use whichever public-web, browser, scraping, and SEO-data capabilities are
configured and authorized in the current environment. This document preserves
Firecrawl and DataForSEO names as optional provider mappings; it does not imply
that either connector is installed. If an equivalent provider is available,
map the capability by purpose. If quantitative SEO data is unavailable, report
that limitation rather than estimating it.

## Contents
- Site discovery and retrieval (optional Firecrawl mapping)
- SEO and market data (optional DataForSEO mapping)
- Recommended Execution Order
- Error Handling

---

## Site Discovery and Retrieval — Optional Firecrawl Mapping

### firecrawl_map
**Purpose**: Discover all URLs on a competitor's site to identify key pages.
**When to use**: First step for every competitor — before scraping individual pages.
**Key output**: List of URLs with their page types/paths.
**Tip**: Look for paths containing `/pricing`, `/features`, `/about`, `/customers`, `/integrations`, `/blog`, `/changelog`.

### firecrawl_scrape
**Purpose**: Extract content from a single page as clean markdown.
**When to use**: After mapping, scrape each key page individually.
**Key output**: Page content in markdown format — headlines, body text, structured data.
**Tip**: Scrape homepage first — it reveals positioning, audience, and social proof in one shot.

### firecrawl_search
**Purpose**: Search the web for specific content about a competitor.
**When to use**: Finding review pages, press coverage, or competitor mentions not on their own site.
**Example queries**:
- `"[Competitor Name]" site:g2.com`
- `"[Competitor Name]" review`
- `"[Competitor Name]" funding OR raised`

### firecrawl_crawl
**Purpose**: Crawl multiple pages from a site in one operation.
**When to use**: Deep profiles where you want to analyze many pages (e.g., all feature pages, all blog posts). More expensive — use selectively.
**Tip**: Set page limits to avoid crawling entire sites. Target specific URL patterns.

### firecrawl_extract
**Purpose**: Extract structured data from a page using a schema.
**When to use**: When you need specific data points in a consistent format (e.g., pricing tier details, feature lists).
**Tip**: Define a clear schema for what you want extracted — more reliable than parsing raw markdown.

---

## SEO and Market Data — Optional DataForSEO Mapping

### Domain-Level Intelligence

#### backlinks_summary
**Purpose**: Get domain authority, total backlinks, referring domains, spam score.
**Input**: Target domain (e.g., `competitor.com`)
**Key metrics**: `domain_rank`, `total_backlinks`, `referring_domains`, `backlinks_spam_score`

#### backlinks_referring_domains
**Purpose**: List top referring domains — shows where their link equity comes from.
**Input**: Target domain + limit
**Key metrics**: Per-domain: `rank`, `backlinks`, `domain` name

#### dataforseo_labs_google_domain_rank_overview
**Purpose**: Organic search overview — traffic, keywords, traffic value.
**Input**: Target domain
**Key metrics**: `organic_count` (keywords), `organic_traffic` (estimated monthly), `organic_cost` (traffic value in $)

#### dataforseo_labs_google_ranked_keywords
**Purpose**: What keywords a domain ranks for, with positions.
**Input**: Target domain
**Key metrics**: Per-keyword: `keyword`, `position`, `search_volume`, `url` (ranking page)
**Tip**: Sort by traffic to find their highest-value keywords.

#### dataforseo_labs_google_keywords_for_site
**Purpose**: Keywords relevant to a domain — broader than ranked keywords, includes opportunities.
**Input**: Target domain
**Key metrics**: `keyword`, `search_volume`, `competition`, `cpc`

### Competitive Analysis

#### dataforseo_labs_google_competitors_domain
**Purpose**: Find a domain's closest organic competitors by keyword overlap.
**Input**: Target domain
**Key metrics**: `domain`, `avg_position`, `intersections` (shared keywords), `full_domain_rank`
**Tip**: May reveal competitors the user hasn't considered.

#### dataforseo_labs_google_domain_intersection
**Purpose**: Find keywords where two domains both rank — shows direct competition.
**Input**: Two target domains
**Key metrics**: `keyword`, position for each domain, `search_volume`
**Tip**: Use this to compare the user's domain vs. each competitor.

#### dataforseo_labs_google_relevant_pages
**Purpose**: Find a domain's most important pages by organic traffic.
**Input**: Target domain
**Key metrics**: `page`, `metrics` (traffic, keywords per page)
**Tip**: Reveals their content strategy — which pages drive the most value.

### Technology Detection

#### domain_analytics_technologies_domain_technologies
**Purpose**: Detect the technology stack a domain uses.
**Input**: Target domain
**Key metrics**: Technologies grouped by category (CMS, analytics, marketing, payments, etc.)

### Backlink Deep Dive

#### backlinks_backlinks
**Purpose**: List individual backlinks to a domain.
**Input**: Target domain + limit
**Key metrics**: `url_from`, `url_to`, `anchor`, `domain_from_rank`, `is_new`

#### backlinks_bulk_ranks
**Purpose**: Compare domain ranks across multiple domains at once.
**Input**: Array of target domains
**Key metrics**: `domain_rank` per domain
**Tip**: Use this for the summary comparison table.

---

## Recommended Execution Order

### Quick Scan (per competitor)

```
1. Discover or map the site's key URLs
2. In parallel:
   a. Retrieve the homepage
   b. Retrieve the pricing page
   c. Pull a domain organic overview when an SEO provider is configured
   d. Pull a backlink/domain summary when an SEO provider is configured
3. Synthesize into abbreviated profile
```

### Deep Profile (per competitor)

```
1. Discover or map the site's key URLs
2. In parallel (batch 1 — scraping):
   a. Retrieve the homepage
   b. Retrieve the pricing page
   c. Retrieve feature page(s)
   d. Retrieve the about page
   e. Retrieve customers/case-studies pages
   f. Retrieve the integrations page
3. In parallel (batch 2 — SEO data):
   a. Domain organic overview
   b. Ranked keywords
   c. Backlink/domain summary
   d. Referring domains
   e. Relevant/top pages
   f. Organic competitors
4. In parallel (batch 3 — optional extras):
   a. Technology detection
   b. Public web search → G2/Capterra reviews
   c. Domain intersection (vs. user's domain)
5. Synthesize into full profile
```

### Multi-Competitor (3+ competitors)

```
1. Map all competitor sites in parallel
2. Scrape all homepages in parallel, then pricing pages in parallel
3. Pull domain_rank_overview for all in parallel
4. Pull backlinks_bulk_ranks for all at once
5. Build profiles in sequence (synthesis requires focus)
6. Build summary comparison last
```

---

## Error Handling

| Issue | Action |
|-------|--------|
| Static retrieval returns empty/blocked | Try an available JavaScript-capable browser; if still blocked, record the gap and do not bypass access controls |
| Pricing page not found in map | Search for `/pricing`, `/plans`, `/packages` — some sites use different paths |
| SEO provider returns no data for domain | Domain may be too new or too small — note "insufficient data" in profile |
| Rate limits hit | Space out requests; prioritize highest-value data first |
| Review page retrieval blocked | Use public web search to find accessible alternative review sources; do not bypass access controls |
