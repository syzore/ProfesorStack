> Draft (basic) — pending Aviv's review.

# P03 · Non-functional requirements

Checklist: [the-checklist.md § Non-functional requirements](../the-checklist.md)

## What this step decides
The qualities the system must have while it does its job: how consistent, available, fast, big, durable, safe, observable, cheap and maintainable. This step turns each quality into a number or a test. Those numbers pick the architecture in the rest of P3; without them, "fast" and "reliable" justify anything.

## How to think about it
- Each NFR runs the same chain: name the quality, put a number on it, pick the design lever that meets it, name what the lever costs. Stop at the number if no lever is needed.
- Targets come from the user and the business, not from the engineer's taste. Ask what a user notices (slow page, lost entry) and what the P0 · Business ceilings allow.
- Many NFRs pull against each other: consistency against availability and latency, durability against write latency, security and compliance against speed and cost. Choose a side per data domain, out loud, and write it.
- Set the target for the first 12 months, not for a hypothetical success. Re-estimate at a named scaling threshold (P3 · Scale).
- The last item rules: every requirement gets a number or a test. "Highly available" fails; "99.5% monthly on sign-in" passes.
- All numbers below are examples (e.g.) for a small pre-revenue product. Replace them with your own estimates.

## Options and trade-offs
| NFR | How to pick the target | Example target (small pre-revenue product) |
| --- | --- | --- |
| CAP/PACELC per data domain | Ask what is worse in a partition: refusing, or serving stale or divergent data. Money and identity lean CP; feeds and counters lean AP. When healthy, ask whether the domain waits for replicas (consistency) or answers fast (latency) | e.g. accounts and payments: refuse rather than diverge; activity feed: serve stale |
| Consistency model per domain | Strong where a stale read causes harm; read-your-writes where a user must see their own change; eventual where lag is invisible | e.g. strong for balances, read-your-writes for profile edits, eventual for counts |
| Availability SLO and error budget | Pick per user-facing path from what an outage costs. Budget = 100% minus SLO over a month | e.g. 99.5% (about 3.6 hours a month) for the main path, none for an admin page |
| Scalability axis | Name what grows (users, data, writes, reads, tenants) and the multiplier | e.g. users 10x in 12 months, data 20x |
| p50 and p99 latency per key path | Users feel the slow tail. Anchor to the interaction type: tap response, page load, report | e.g. read path p50 under 150 ms, p99 under 800 ms; heavy report p99 under 5 s |
| Peak read and write throughput | Busiest-hour requests per second from the usage guess in P0 · Product and P3 · Scale; assume peak is a multiple of average | e.g. 20 reads/s and 2 writes/s at peak |
| Durability: RPO, write ack, replication | Ask how much recent data you can lose. A write is acknowledged only after it is durable | e.g. RPO under 5 minutes via managed point-in-time recovery; zero for payments |
| Fault tolerance: RTO, blast radius, DR | Ask how long you can be down and what one failure takes with it. Isolate non-critical features so they fail alone | e.g. RTO 4 hours; one provider failure degrades only its feature; restore from backup |
| Security | Fix authentication, authorization, encryption (in transit and at rest) and audit from P2 and P6; list privileged actions | e.g. managed auth, TLS everywhere, encryption at rest by the provider, audit log of admin actions |
| Privacy and compliance | Copy regimes in scope, residency and retention from P1 and P2 | e.g. one region, deletion within the policy period, retention per field |
| Environment constraints | List budget, team size, cloud limits, legacy | e.g. one person, one region, managed services only |
| Observability | List what must be measurable and alertable per path | e.g. error rate and p99 per path; alert on SLO burn |
| Cost ceiling per month and per user | Derive from P0 · Business limits | e.g. a monthly cap you would shrug at, and a per-user number below price |
| Maintainability | Who operates it, on-call load, upgrade cadence | e.g. no pager at night; one upgrade window a month |

## How to choose: solo founder / pre-revenue defaults
- Default stance for a solo pre-revenue product: AP-leaning for non-critical content, CP for money and identity, a single region, managed database with backups, and a 99.5%-style SLO. Boring and small.
- Pick fewer, looser targets rather than many tight ones. Tight targets add cost and moving parts.
- Do not set a target you will not measure. Each one needs a test or a monitor in P19 · Metrics or P19 · Alerts.
- Where two NFRs conflict, record the winner and the reason in an ADR (P3 · Architecture decisions).

## Human in the loop: escalate when
- CAP or consistency choice for money or identity data: AP over CP needs Aviv (P3 · Escalations).
- RPO above zero for customer data.
- Any SLO or latency target that implies paid infrastructure, multi-region or a new vendor.
- Cost ceiling: setting it, or an estimate above it.
- Weakening a security target or changing compliance scope.
- Data residency or cross-region needs.
- Bring: the options, the number each implies, cost, and reversibility.

## Done means
- Every item has a number, a test or an `[N/A]` reason; no adjectives remain.
- Each number says how it will be measured.
- Conflicts between NFRs are resolved and recorded.

## Depends on / feeds into
Depends on: P0 · Product (scale, platforms), P0 · Business (cost ceilings), P1 · Compliance deliverable (regimes, residency), P2 · Data inventory and P2 · Data lifecycle (sensitivity, retention, RPO). Feeds: P3 · Architecture, P3 · Architecture decisions, P3 · Trade-offs and options, P3 · Scale, P3 · Escalations, P19 · Metrics, P19 · Alerts, P24 · Operations.
