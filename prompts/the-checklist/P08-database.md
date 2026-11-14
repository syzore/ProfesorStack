> Draft (basic) — pending Aviv's review.

# P8 · Database

Checklist: [the-checklist.md § Database](../the-checklist.md)

## What this step decides

The schema and its operating rules: keys, relationships, constraints, indexes, how the app queries and writes (transactions), and how schema changes, seed data, backup and restore work.

## How to think about it

- Design from query patterns and invariants, not from a diagram. List the reads and writes the product makes, then check each has an index and each invariant has a constraint.
- Constraints (primary, foreign, unique, check) are the cheapest enforcement of the domain. A rule in the database cannot be bypassed by a new code path.
- Transaction boundaries follow the domain: what must succeed or fail together. Keep them short and keep external calls (email, payments, LLM) outside them.
- Backup is not done until restore is. A backup never restored is a guess, so rehearse it and record the time it took.
- Migrations need a strategy for rollbacks and for running against live data: additive first, backfill, then switch, then remove.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Engine | One managed relational database (e.g. Postgres) | Add a specialist store | A measured need the relational engine cannot meet |
| Keys | Surrogate ids, plus unique constraints on natural keys | Natural primary keys | Rarely worth it |
| Scale | Indexes, query fixes, a read replica | Sharding, caches | Measured bottleneck after simpler fixes |
| Migrations | Versioned, forward-only scripts, reviewed | Online-migration tooling | Large tables with no downtime window |

## How to choose: solo founder / pre-revenue defaults

- One managed relational database serves search, queues, and caching until measurements say otherwise. The checklist's own rule: prefer boring infrastructure and the smallest architecture.
- Add an index when a real query needs it, and check query plans on realistic data volumes.
- Turn on automated backups and point-in-time recovery if the provider offers it, then restore into a scratch database before launch.
- Seed data is code: repeatable, safe to rerun, and never contains real personal data.

## Human in the loop: escalate when

- A migration that deletes or rewrites data, or one that cannot run backward (irreversible).
- Choosing or changing the engine, hosting provider or region (one-way door, plus P7 transfer review).
- Introducing a second datastore, cache or queue, which is added cost and failure modes.
- Restore rehearsal fails or takes longer than the recovery target set in P3.
- Granting anything other than the app role write access to production.

## Done means

- Each table has keys and constraints for its invariants, and each known query has an index or a stated reason not to.
- Migrations apply on a copy of production-like data, a restore has been rehearsed with measured time, and seed data runs twice without harm.

## Depends on / feeds into

Depends on P3 · System Architecture, P4 · UX, UI, Accessibility and Internationalization, P5 · Engineering Foundation, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P8 · Domain. Feeds P6 · Data security (permissions, backups), P14 · Search / RAG / Indexing, P16 · Background Jobs (recovery after outage), P18 · Performance, P23 · Infrastructure / Reliability.
