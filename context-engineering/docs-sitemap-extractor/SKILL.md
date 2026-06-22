---
name: docs-sitemap-extractor
description: Extracts a complete, deduplicated list of every page URL in a documentation or help site, grouped by the site's own sidebar/nav sections. Use this whenever the user gives a docs URL and asks for "all the links," "every page," "a full list of docs pages," wants to map the complete structure of a documentation site, or needs URLs grouped by section to paste into another tool. Trigger even on a short request like "get me every link from these docs" — a single homepage fetch only ever surfaces a fraction of the real page count, especially when the sidebar is JS-rendered, paginated, or has collapsed sub-sections.
---

# Docs Sitemap Extractor

## Why a single fetch isn't enough

A docs homepage almost never links to every page directly — most pages are reached only through sidebar navigation, and a lot of modern doc sites render that sidebar with JavaScript, so a plain fetch of the page returns the shell without the nav links. Collapsed sections compound this: a "Guides" group might show one visible link while hiding eight more behind a toggle that never gets expanded in static HTML. Treat the homepage fetch as a starting point for section names, not as the page list itself.

## Workflow

### Step 1: Find the sitemap first

Before crawling anything by hand, check for a sitemap — it's the fastest way to get a ground-truth list of every page that exists on the site:

- `{domain}/sitemap.xml`
- `{domain}/sitemap_index.xml` (a sitemap of sitemaps on larger sites — fetch each child sitemap listed inside it too)
- `{docs-path}/sitemap.xml` if the docs live on a subpath, e.g. `https://example.com/docs/sitemap.xml`
- `/robots.txt` — many sites declare `Sitemap:` there even when it's not at a default path

A sitemap gives you a flat URL list, but treat it as a *starting* checklist, not ground truth — sitemaps are frequently incomplete (it's common for auto-generated sitemaps to omit a third or more of real doc pages, especially ones added recently or behind dynamic routes). It also won't give you the section grouping the user wants. Use it in Step 4 to catch pages your sidebar walk missed — never as a substitute for actually walking the sidebar.

Also check for a JSON search index, which several doc frameworks expose and which often mirrors the sidebar hierarchy directly (URLs AND section structure in one shot): paths like `/search-index.json`, an Algolia DocSearch config, or a Mintlify `mint.json` / `docs.json` nav config. If you find one, it's the single best source — prefer it over manual crawling.

| Framework (check page source / meta generator tag) | Best shortcut |
|---|---|
| Docusaurus | `/sitemap.xml`; also look for an Algolia DocSearch index |
| Mintlify | `/sitemap.xml`; `mint.json` or `docs.json` often lists the full nav tree |
| GitBook | `/sitemap.xml` |
| ReadMe.io | `/sitemap.xml` |
| Nextra | `/sitemap.xml`; nav data is otherwise baked into JS chunks and hard to parse — fall back to Step 3 |

If you're unsure which framework it is, try `/sitemap.xml` anyway — it works on the large majority of doc sites regardless of framework.

### Step 2: Fetch the docs landing page

Fetch the main docs index/homepage and record:
- Every top-level sidebar section name, in the order it appears
- Any page links that show up directly in the fetched content

If section labels are visible but their links aren't (a sign of a JS-rendered nav), don't guess at URLs — move to Step 3 for those sections.

### Step 3: Cross-reference with search for anything JS-rendered or paginated

For sections where the fetch didn't surface real links, use web search to fill the gap — search the section name together with the product/docs name (e.g. "Acme docs API reference pages"). Because the user has explicitly asked for comprehensive single-site coverage, it's appropriate here (atypically) to scope searches to the docs domain to avoid noise. Cross-check anything you find this way against the Step 1 sitemap list — the sitemap should confirm the page actually exists.

Don't skip commonly-missed sections just because they didn't appear in your first pass — explicitly check for: Getting Started / Quickstart, Guides, API Reference, Examples / Cookbook, Changelog / Release Notes, SDKs, Migration Guides, FAQ, Troubleshooting. These often live in a secondary nav or a collapsed group that's easy to miss.

### Step 4: Walk every top-level section

For each top-level section from Step 2:
- Fetch the section's own index page if it has one, and enumerate every child link
- For nested/collapsed sub-sections, fetch each one individually — "collapsed" in the rendered UI doesn't mean the links are absent from fetched markdown, so check first before assuming you need to search
- Cross-reference against the Step 1 sitemap: any sitemap URL whose path prefix matches this section (e.g. everything under `/docs/api/`) that isn't in your list yet is a miss — add it

### Step 5: Normalize and deduplicate

- Pick one trailing-slash convention and apply it consistently
- Strip URL fragments (`#some-anchor`) unless the user specifically wants anchor-level granularity
- Drop tracking query params (`utm_*` etc.); keep query params only when they change which content loads (e.g. `?version=2`)
- Remove exact duplicates after normalization
- If the same page is reachable via two paths (alias or redirect), list it once, filed under whichever section the sidebar itself uses

### Step 6: Output format

Group by section using the **same headings the site's own sidebar uses** — don't invent your own taxonomy or reorder them. For each section, output a heading followed by a code block of bare URLs, one per line, no markdown link syntax or descriptions, in the sidebar's own order:

```markdown
## Getting Started
\`\`\`
https://example.com/docs/introduction
https://example.com/docs/quickstart
\`\`\`

## API Reference
\`\`\`
https://example.com/docs/api/overview
https://example.com/docs/api/authentication
\`\`\`
```

### Step 7: Flag what you couldn't fully verify

Always end with an explicit confidence note. Call out:
- Any section where you suspect there are more pages than you found (e.g. the sitemap had URLs you couldn't confidently place into a section, or an index page hinted at sub-items you couldn't enumerate)
- Any section that was entirely JS-rendered, where your list rests mostly on search results rather than a direct fetch
- A reminder that the sitemap itself can't be trusted as complete — if a sidebar walk and sitemap disagree, the gap is worth flagging either way, not silently resolved in the sitemap's favor
- An offer to re-check if the user shares a screenshot of the live sidebar

Never present a partial list as if it were certainly complete — for JS-heavy docs sites, flagging real uncertainty is more useful than overclaiming.
