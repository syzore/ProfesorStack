> Draft (basic) — pending Aviv's review.

# P23 · Infrastructure / Reliability

Checklist: [the-checklist.md § Infrastructure / Reliability](../the-checklist.md)

## What this step decides

Whether production can survive failure and load as P3 promised: environments, DNS/TLS, monitoring, limits, process count, connection budgets, scaling, DR, RTO/RPO, restore and failover drills, backpressure, error-budget policy, single points of failure.

## How to think about it

- P3 · Non-functional requirements sets the targets: availability SLO and error budget, RPO, RTO, blast radius, DR approach. This phase proves them. A target never tested is only a wish.
- Restore test, timed against RTO and checked against RPO. A backup you have not restored is not a backup.
- Connection math: app processes times pool size must stay under the database connection limit. More processes (needed for redundancy) multiply connections.
- Scale the database up before adding read replicas. Replicas add lag, failover work and read-your-writes bugs.
- Backpressure and load shedding (P3 · Trade-offs and options) need an overload test. Decide what is rejected first and see that it happens.
- The error-budget policy says what slows or stops when the budget is spent, e.g. freeze risky releases. Without it the SLO changes nothing.
- Single-point-of-failure review: list each one and either accept it with a reason or remove it. A solo founder may knowingly accept several.
- Failover drills apply only to components with a standby or replica.

## Options and trade-offs

| DR approach | Recovery speed | Cost / effort |
|---|---|---|
| Backups only, restore on demand | Slowest (hours) | Lowest |
| Warm standby or replica | Faster | Higher, plus drills |
| Multi-region active | Fastest | Highest, adds consistency and legal issues |

## How to choose: solo founder / pre-revenue defaults

- Managed database with automated backups and point-in-time recovery. Boring beats clever.
- Backups-only DR with a tested, timed restore unless the P3 RTO or RPO demands more.
- At least two app processes for the critical path, once the connection math allows.
- Single region. Single staging environment only if it earns its cost.
- Write the DR plan and recovery procedure as a short runbook an agent or Aviv can follow.

## Human in the loop: escalate when

- Accepting an RPO above zero for customer data, or changing RTO/RPO targets (P3 escalation).
- Cross-region deployment or data residency choices (legal and cost).
- Adding a paid or managed vendor, or a standby/replica with ongoing cost.
- Any change that weakens a security control, or that crosses the P3 cost threshold.
- A drill or restore that would touch production data.

## Done means

- Restore test result recorded with elapsed time versus RTO and data age versus RPO.
- Overload test shows the documented shedding behavior.
- Error-budget policy, SPOF list and monitoring for each listed resource exist.

## Depends on / feeds into

Depends on P3 · System architecture (non-functional requirements), P19 · Observability, P22 · Deployment / CI/CD. Fed by P18 · Performance (capacity ceiling). Feeds P24 · Data (restore tested) and P24 · Operations, P25 · Monthly/periodic (DR review).
