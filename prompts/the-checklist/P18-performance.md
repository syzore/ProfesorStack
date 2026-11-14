> Draft (basic) — pending Aviv's review.

# P18 · Performance

Checklist: [the-checklist.md § Performance](../the-checklist.md)

## What this step decides

Whether the system meets the P3 non-functional targets in practice: latency p50/p99, peak throughput, capacity ceiling, cache hit rate, and behavior when a dependency degrades.

## How to think about it

- P3 · Non-functional requirements sets the numbers. This phase measures against them. Without P3 numbers, a performance budget is a guess.
- Measure first. Profile before adding a cache, queue or index (the checklist: add caching and async only where justified).
- Look at p99, not the average. Tail latency is what users feel and where slow queries and lock waits show up.
- Find the first thing that saturates (database CPU, connection pool, a single hot key). That is the real capacity ceiling.
- Hot partitions and hot keys only show under skewed load, so test with realistic skew, not uniform traffic.
- Test degraded dependencies and peak behavior, linking to the backpressure and load-shedding decision in P3 · Trade-offs and options.

## Options and trade-offs

| Lever | Helps | Cost / risk |
|---|---|---|
| Fix N+1 and add an index | Read latency | Write cost, storage |
| Cache (with invalidation rule) | Read latency, load | Stale data, extra moving part |
| Pagination | Memory, payload size | Client changes |
| Async processing | Request latency | Complexity, eventual results |
| Scale the database up | Almost everything early | Money, ceiling still exists |

## How to choose: solo founder / pre-revenue defaults

- Set budgets from P3 targets, e.g. API p99 under 500 ms, then check them.
- Load test on a production-like copy at the P3 peak throughput, e.g. 3x expected busiest hour for headroom.
- Fix queries and indexes before adding a cache. Scale the database up before adding replicas.
- One cheap load test (e.g. k6 or similar) kept in the repo, not a performance platform.

## Human in the loop: escalate when

- A fix needs a new paid vendor or CDN tier.
- Load testing would hit production, third-party APIs with quotas, or paid LLM calls.
- Meeting a target needs weakening consistency or durability set in P3.
- The P3 target itself looks unreachable at the cost ceiling.

## Done means

- Measured p50/p99 are recorded against each P3 key-path target, with the result stated as met or not.
- The capacity ceiling and what saturates first are written down.
- Hot-key, cache hit-rate and degraded-dependency checks have results.

## Depends on / feeds into

Depends on functional implementation (P8 and conditional modules) and on P3 numbers. Feeds P23 · Infrastructure / reliability (capacity, limits), P19 · Metrics (the same latency series) and P24 · Launch readiness.
