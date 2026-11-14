> Draft (basic) — pending Aviv's review.

# P03 · Architecture decisions

Checklist: [the-checklist.md § Architecture decisions](../the-checklist.md)

## What this step decides
How the chosen parts fit together: boundaries (system, service, API, database, trust, network, failure), public versus private components, sync and async flows, jobs and events, and the cross-cutting rules (idempotency, transactions, consistency, concurrency, rate limiting, retries, timeouts, fallbacks).

## How to think about it
- Draw the boundaries before writing rules. Trust boundaries (where input is untrusted) and failure boundaries (where one failure stops) matter most.
- For every flow, say sync or async and why. Anything slow, retried or optional is a candidate for async; anything the user waits on and must be right stays sync.
- Every background process needs retry, timeout, idempotency and failure behavior (checklist rule). Write all four or it is not designed.
- Retries need idempotency, and timeouts need a fallback. These rules work as a set.
- Keep modules few. A modular monolith with clear internal boundaries covers most small products.

## Options and trade-offs
| Decision | Smallest option | Cost of going bigger |
| --- | --- | --- |
| Service split | One deployable, modules inside | Network calls, deploys, debugging |
| Async flows | Job table polled by a worker | Queue broker to operate |
| Rate limiting | Provider or gateway default | Custom logic to maintain |
| Retries | Exponential backoff with jitter and a cap | Retry storms if unbounded |
| Circuit breaking | Only on flaky external calls | Complexity everywhere else |

## How to choose: solo founder / pre-revenue defaults
- Default: one backend, one database, transaction boundaries inside single requests, jobs recorded in the database, timeouts on every outbound call, bounded retries with idempotency keys for money-moving calls.
- Add rate limiting on public and auth endpoints first.
- Record consistency requirements per domain from P3 · Non-functional requirements; do not restate them differently here.

## Human in the loop: escalate when
- Boundary or trust-boundary choices that weaken a security control.
- Making a flow async where data could be lost or duplicated (money or identity).
- Splitting into services (a one-way door in practice).
- Idempotency or transaction rules for payments.
- Public exposure of a component previously private.
- Bring: diagram, failure behavior, reversibility.

## Done means
- Each item answered; boundaries drawn in P3 · Architecture documentation.
- Each background job lists retry, timeout, idempotency and failure behavior.
- Meaningful decisions have ADRs with rejected alternatives.

## Depends on / feeds into
Depends on: P3 · Architecture, P3 · Non-functional requirements. Feeds: P3 · Trade-offs and options, P3 · Architecture documentation, P5 (conventions), P6 · Application security, P8 · API, P8 · Database.
