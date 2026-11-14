> Draft (basic) — pending Aviv's review.

# P16 · Background Jobs / Cron / Agents

Checklist: [the-checklist.md § Background Jobs / Cron / Agents](../the-checklist.md)

## What this step decides

Everything that runs without a user waiting: the job inventory, scheduling, workers, and the safety properties each job needs. Phase-level guide, which also applies to scheduled agents.

## How to think about it

- The rules say every background process needs retry, timeout, idempotency and failure behavior. This phase is where those become concrete.
- Begin with the job inventory: for each job, trigger, input, owner, side effects, and what happens on failure. Jobs nobody listed become silent outages.
- Idempotency and deduplication make retries safe. Design each job so running it twice is harmless, using a unique key or a state check.
- Failure handling is a ladder: retry with backoff, then dead-letter, then alert a human. Concurrency and resource limits stop one job from starving the app or exhausting a quota.
- Operability: job observability (what ran, how long, what failed), manual replay and cancellation, and graceful shutdown so a deploy does not kill half-done work.
- Recovery is the test of the design: after a deployment, a database outage, a provider outage, does the system catch up correctly without duplicates?
- Scheduled agents add the P9 limits (budget, action count, approval) on top.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Queue | Database-backed job table or platform cron | Dedicated broker | Throughput or latency exceeds the database approach |
| Workflow | Plain jobs with state columns | Durable workflow engine | Long multi-step processes with human waits |
| Scheduling | Platform scheduler | Distributed scheduler | Several instances need exactly-one-run |
| Replay | Admin command with an idempotency key | Full replay UI | Operator volume warrants it |

## How to choose: solo founder / pre-revenue defaults

- A jobs table with status, attempts, next-run time and a unique key, claimed with row locking, covers most solo products.
- Set a timeout on every job, a retry cap with backoff, and a dead-letter state that alerts.
- Make shutdown cooperative: finish or release the job, and let the claim expire.

## Human in the loop: escalate when

- A job that sends messages, charges money, deletes data or calls a paid API at scale.
- Replaying or cancelling jobs that already caused external side effects.
- Introducing a broker or workflow engine (new infrastructure, new vendor).
- A dead-letter backlog or a runaway retry storm in production.
- A scheduled agent gaining new tools or a higher budget.

## Done means

- Every job is in the inventory with its limits and failure behavior, and a retry-twice test shows no duplicate side effects.
- The dead-letter path alerts a human, replay and cancel work, and recovery after a deploy and an outage have each been rehearsed.

## Depends on / feeds into

Depends on P3 · System Architecture, P5 · Engineering Foundation, P8 · Core Product Implementation. Feeds P9 · Agents / tools, P10 · Payments (reconciliation), P12 · Email / Notifications, P13 · Files / Media, P19 · Observability, P23 · Infrastructure / Reliability.
