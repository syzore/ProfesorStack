> Draft (basic) — pending Aviv's review.

# P14 · Search / RAG / Indexing

Checklist: [the-checklist.md § Search / RAG / Indexing](../the-checklist.md)

## What this step decides

How users or models find content: the search engine, the index and query models, ranking, filtering, permissions, keeping the index in sync, and surviving failure. Phase-level guide.

## How to think about it

- Search is a derived copy of your data. Every item here is a consequence of that: the copy goes stale, can leak what the source protects, and can be lost.
- Start from the queries users run and the fields they match, not from the engine. Many products are served by database full-text search.
- Access control is the sharp edge. Enforce permissions at query time, using the same rules as the source, and keep tenant isolation in the index structure or filters.
- Update strategy and delete propagation decide freshness and privacy: how a change reaches the index (same transaction, outbox, periodic sync), and how a deletion removes the entry.
- Reindexing and failure recovery: you must be able to rebuild the index from the source at any time. If you cannot, the index has become a database.
- Overlaps with P9 · RAG when the consumer is a model; keep one index policy for both.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Engine | Database full-text search (and vector extension) | Dedicated search service | Measured relevance, scale or feature limits |
| Sync | Index in the write path or an outbox | Change-data-capture pipeline | Several sources or high write volume |
| Ranking | Simple text rank plus filters | Learned ranking | Analytics show relevance is the retention problem |
| Abuse | Per-user limits and query size caps | Bot management | Scraping or load observed |

## How to choose: solo founder / pre-revenue defaults

- Use the database you already run until a measured limit appears. A second system adds cost, sync bugs, and another permission model.
- Write the rebuild-from-source command before launch and run it.
- Cap query length, page depth and rate.

## Human in the loop: escalate when

- Introducing a dedicated search service (new vendor and datastore, hard to unwind).
- Indexing data with differing visibility, or any change to the access-control filter.
- Bulk reindex or delete on production indexes that users rely on.
- Indexing personal data into a third-party hosted service (P7 vendor review).

## Done means

- Queries, ranking and filters are defined on a fixed test set with expected results.
- A permission test shows one user never sees another's hidden content, deletes propagate within the stated time, and a full reindex from source has been run.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P8 · Core Product Implementation. Feeds P9 · RAG, P8 · Database, P16 · Background Jobs (index updates), P18 · Performance, P20 · Analytics and Experimentation (search analytics).
