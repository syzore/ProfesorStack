> Draft (basic) — pending Aviv's review.

# P21 · SEO / Discoverability

Checklist: [the-checklist.md § SEO / Discoverability](../the-checklist.md)

## What this step decides

How a public web product is found and shared: domain, HTTPS, canonical URLs, metadata, sitemap, robots, structured data, redirects, indexing, public/private pages, search console, social previews.

## How to think about it

- Only applies to public web products. A logged-in-only app is `[N/A]`, with that reason.
- Decide first which pages should be indexed and which must not (private, duplicate, staging). That decision drives canonical URLs, robots and the sitemap.
- Rendering matters. Pages a crawler cannot read without running heavy JavaScript may not index well (P3 frontend choice).
- Most items are one-time setup. Ongoing SEO content work is P26 · Growth.

## Options and trade-offs

| Rendering | Good for SEO | Cost |
|---|---|---|
| Static or server-rendered pages | Yes | Build or server setup |
| Client-rendered app | Weaker | Needs prerender or a separate marketing site |

## How to choose: solo founder / pre-revenue defaults

- Use a static or server-rendered marketing site, with the app behind login and excluded from indexing.
- Add title, description, Open Graph, sitemap, robots, canonical, a real 404. Search console once, free.
- Block staging from indexing.

## Human in the loop: escalate when

- Changing the primary domain or a large URL structure (hard to reverse, loses ranking).
- Buying paid SEO tools or services.
- Any structured data or claims that could be misleading or regulated.

## Done means

- Public pages are indexable and private pages are not, verified.
- Sharing a link shows the right preview.
- Search console is set up and reports no critical errors.

## Depends on / feeds into

Depends on P4 · UX, UI, accessibility and i18n and P8. Feeds P26 · Growth (SEO) and P24 · Launch (domain and HTTPS).
