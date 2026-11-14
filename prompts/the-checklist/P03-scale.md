> Draft (basic) — pending Aviv's review.

# P03 · Scale

Checklist: [the-checklist.md § Scale](../the-checklist.md)

## What this step decides
Rough numbers for load and cost: users, requests per second, peak traffic, storage and database growth, bandwidth, background work, third-party and LLM volume, worst-case cost, expected bottlenecks and the threshold at which the design changes.

## How to think about it
- Do back-of-envelope math with round numbers and show the steps. Users x actions per user per day / 86,400 gives average requests per second; assume peak is some multiple of that (e.g. 5x to 10x) and write the multiplier.
- Storage growth: records per day x bytes per record x retention, with an index and backup overhead factor.
- Third-party and LLM volume need cost per call. Worst-case cost assumes abuse or a spike, and must sit under the P0 · Business ceiling or the product needs a cap.
- Find the likely first bottleneck (database writes, an API quota, an LLM bill) and say what you would do at the threshold.
- Numbers here feed the targets in P3 · Non-functional requirements and the cost threshold in P3 · Escalations.

## Options and trade-offs
| Estimate | How | Example input (e.g.) |
| --- | --- | --- |
| Users and requests/s | Users x actions/day / 86,400, times a peak multiplier | 1,000 users x 20 actions: under 1 request/s average |
| Storage and DB growth | Rows/day x bytes x retention x overhead | 50 MB a month |
| Bandwidth | Requests x payload size | Mostly under provider free tiers |
| Third-party / LLM volume | Calls per user x price per call | Cap calls per user per day |
| Worst-case cost | Abuse or spike case x price | Compare with the ceiling |

## How to choose: solo founder / pre-revenue defaults
- Default: assume one small managed database and one app instance handle the first 12 months; prove it with the arithmetic.
- Set a scaling threshold with a number and a first action, e.g. "database CPU over 60% sustained: add an index, then a read replica".
- Put hard per-user and global caps on paid API and LLM use so worst-case cost has a bound.

## Human in the loop: escalate when
- Worst-case cost estimate above the recorded threshold (P3 · Escalations).
- An estimate showing the chosen stack cannot meet the NFRs: the answer may be a bigger bill or a re-architecture.
- Reliance on a third-party quota the vendor can change.
- Paid scaling decisions (a bigger plan, replica, new vendor).
- Bring: numbers, assumptions, cost per option.

## Done means
- Every estimate has inputs, math and a result, or `[N/A]` with reason.
- Bottlenecks and a scaling threshold with a first action are named.
- Worst-case cost is compared with the ceiling.

## Depends on / feeds into
Depends on: P0 · Product (expected scale, usage frequency), P0 · Business (cost ceilings), P3 · Architecture. Feeds: P3 · Non-functional requirements (throughput, cost), P3 · Trade-offs and options, P3 · Escalations, P18 · Performance, P25 · Monthly/periodic.
