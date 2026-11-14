> Draft (basic) — pending Aviv's review.

# P03 · Architecture

Checklist: [the-checklist.md § Architecture](../the-checklist.md)

## What this step decides
Which technologies and providers make up the system: frontend, backend, database, optional components (cache, object storage, queue, search, vector database) and providers (hosting, DNS, CDN, proxy, email, auth, payment, analytics, monitoring, logging).

## How to think about it
- Choose from the NFRs and the data inventory, not from fashion. Each component is a dependency with an owner, a failure mode and a replacement path (checklist rule).
- "If necessary" items default to no. Add a cache, queue, search or vector database only when a measured need from P3 · Scale or an NFR requires it.
- Fewer vendors means fewer outages, bills and data-sharing agreements. Prefer one provider that does several jobs.
- Check each provider against P1: where does it host and process data, and what does it see?
- Every paid capability needs billing-failure behavior; every external API needs quota and error behavior.

## Options and trade-offs
| Component | Smallest choice | Add something bigger when |
| --- | --- | --- |
| Database | One relational database, managed | Access pattern or scale a measurement shows it cannot meet |
| Cache | None | Hot reads measured too slow or costly |
| Queue | None; run a job table or the host's scheduler | Bursts, retries or fan-out need buffering |
| Search | Database full-text search | Relevance or scale beyond it |
| Vector database | Database vector extension, if needed at all | Large embedding corpus with latency targets |
| Object storage | Provider's bucket | Only when files exist |
| Hosting | One managed platform | Needs it cannot meet |

## How to choose: solo founder / pre-revenue defaults
- Default: a monolith on one managed platform, one managed relational database, managed auth, a CDN from the host, and one provider each for email, payments (only if charging), analytics and monitoring.
- Pick the stack you already know. Switching cost is your time.
- Prefer providers with data export, so a replacement path exists.
- Write each choice in a table with owner, failure mode and replacement path.

## Human in the loop: escalate when
- Any new paid or managed vendor (new cost, dependency and data-sharing).
- A provider that stores or processes data outside the target region.
- Choosing a payment, auth or email provider (money, identity, delivery of account mail).
- A choice that is hard to reverse: data stored in a proprietary format, a database engine switch.
- Cost estimate above the recorded threshold.
- Bring: options, monthly cost, data shared, exit path.

## Done means
- Each item is chosen with a reason, or `[N/A]` with reason.
- Each external dependency has owner, failure mode, replacement path, and monitoring plan.
- The choice is recorded in an ADR where it is meaningful.

## Depends on / feeds into
Depends on: P3 · Non-functional requirements, P2 · Data inventory, P1 · Compliance deliverable. Feeds: P3 · Architecture decisions, P3 · Trade-offs and options, P3 · Escalations, P4 · UX (platform), P5 · Repository and P5 · Configuration.
