> Draft (basic) — pending Aviv's review.

# P03 · Trade-offs and options

Checklist: [the-checklist.md § Trade-offs and options](../the-checklist.md)

## What this step decides
For each of the design decisions in this section: the options considered, the one chosen and why. The point is the recorded reasoning, so a later change knows what was traded away. Each choice feeds an ADR in P3 · Architecture decisions.

## How to think about it
- Name at least two options for every decision, even when one is obviously right. Writing the loser down forces the reason.
- Tie each choice to a number in P3 · Non-functional requirements (consistency, latency, throughput, cost). A trade-off with no NFR behind it is taste.
- Most of these choices favor the simpler option until a measurement says otherwise. Cheap to reverse: choose fast. One-way door: slow down and escalate (P3 · Escalations).
- Most small products never need sharding, multi-leader replication, a stream pipeline or services. Record "not needed, because X" and move on.
- Postgres first: indexes, batching, connection pooling and read replicas go a long way before a different architecture is justified. Measure with the database's own statistics, then change architecture only when tuning stops helping.
- Tables below give option, when to pick it and its cost. Costs are directions, not prices.

## Options and trade-offs
### SQL vs NoSQL (per data domain)
| Option | Pick when | Cost |
| --- | --- | --- |
| Relational (SQL) | Related entities, transactions, ad-hoc queries | Schema migrations; scaling writes needs planning |
| Document or key-value | Access by key, flexible shape, huge write volume | Weak joins and transactions; you model queries up front |

**Solo default:** one relational database for everything. Add NoSQL only for a measured need.

### Sync vs async (queue)
| Option | Pick when | Cost |
| --- | --- | --- |
| Sync | The user waits and the result must be right | Slow dependency slows the user |
| Async via queue or job table | Slow, retryable or optional work | Needs idempotency, status tracking, a worker |

**Solo default:** sync by default; a job table for slow or retryable work.

### Push vs pull, fan-out on write vs read
| Option | Pick when | Cost |
| --- | --- | --- |
| Fan-out on write | Reads far outnumber writes, few followers per writer | Write cost and storage multiply; hot writers hurt |
| Fan-out on read | Many followers per writer, or reads are rare | Read cost rises with followers; slow reads |
| Pull / push of updates | Pull when freshness is loose; push when it matters | Push needs connections and delivery handling |

**Solo default:** fan-out on read with a query; revisit at the scaling threshold.

### Cache strategy and invalidation
| Option | Pick when | Cost |
| --- | --- | --- |
| Cache-aside | Read-heavy, tolerates short staleness | Stale reads; cache miss storms |
| Write-through | Reads must see recent writes | Slower writes; cache holds data you may not read |
| Write-behind | Write bursts, loss of a few writes tolerable | Data-loss window; complexity |

**Solo default:** no cache until measured; then cache-aside with a TTL as the invalidation rule.

### Sharding or partition key
| Option | Pick when | Cost |
| --- | --- | --- |
| No sharding | Data fits one database | None now; harder move later |
| Hash of a key (e.g. user id) | Even load, lookups by key | Range and cross-key queries get expensive |
| Range (e.g. by time) | Time-ordered data, easy retention by dropping a range | Hot newest range |

**Solo default:** none. Write down the likely key and the queries it would hurt, for later.

### Replication model
| Option | Pick when | Cost |
| --- | --- | --- |
| Leader-follower | Most apps; reads can scale on followers | Replica lag; failover handling |
| Multi-leader | Writes in several regions | Conflict resolution |
| Leaderless / quorum | Very high availability needs | Tuning, read repair, eventual consistency |

**Solo default:** the managed provider's single leader with automatic failover.

### Batch vs stream vs micro-batch
| Option | Pick when | Cost |
| --- | --- | --- |
| Batch | Results can wait minutes to hours | Stale until the run; spiky load |
| Stream | Results needed in seconds | Always-on infrastructure; ordering and late data |
| Micro-batch | Near-real-time with fewer moving parts | Latency of the interval; buffering |

**Solo default:** batch jobs on a schedule.

### Strong vs eventual consistency (per domain)
| Option | Pick when | Cost |
| --- | --- | --- |
| Strong | Money, identity, inventory | Higher latency; unavailable during a partition |
| Read-your-writes | Users must see their own edits | Session routing or reads from leader |
| Eventual | Counts, feeds, analytics | Visible lag; merge rules |

**Solo default:** strong for money and identity, eventual where lag is invisible.

### Build vs managed (per component)
| Option | Pick when | Cost |
| --- | --- | --- |
| Managed service | Small team, standard need | Per-use price; lock-in; data sharing |
| Self-run | Special need, or cost at large scale | Your time, on-call, upgrades |

**Solo default:** managed, e.g. a managed queue before self-run Kafka. Each new vendor goes to Aviv.

### Monolith vs services
| Option | Pick when | Cost |
| --- | --- | --- |
| Modular monolith | One team, early product | Must keep module boundaries disciplined |
| Services | Separate scaling or teams | Network calls, deploys, tracing, data ownership |

**Solo default:** modular monolith.

### Polling vs WebSockets vs SSE
| Option | Pick when | Cost |
| --- | --- | --- |
| Polling | Updates every few seconds or slower are fine | Wasted requests; delay |
| SSE | One-way server updates | Open connections; proxy limits |
| WebSockets | Two-way, frequent updates | Stateful connections, scaling, reconnect logic |

**Solo default:** polling; SSE if one-way and live matters.

### Which indexes to add
| Option | Pick when | Cost |
| --- | --- | --- |
| Few, query-driven | Measured slow queries | Write and storage cost on each index |
| Many up front | Never as a default | Slows every write; most go unused |

**Solo default:** primary keys, foreign keys and indexes proven by a slow query. Drop unused ones.

### Idempotency keys: where, scope, expiry
| Option | Pick when | Cost |
| --- | --- | --- |
| Required | Payments, sign-up, any retried write | Key table; storage until expiry |
| Not needed | Naturally repeatable reads or overwrites | Must confirm repeat is harmless |

**Solo default:** required for any money or account write; scope per user and operation; expiry longer than the longest retry window.

### Backpressure and load shedding
| Option | Pick when | Cost |
| --- | --- | --- |
| Reject new work (429) | Protect the core | Users see errors at peak |
| Delay (queue) | Work can wait | Queue grows; staleness |
| Drop low-priority | Analytics, optional work | Data gaps |

**Solo default:** order of loss: drop analytics first, delay background jobs, then rate-limit; never drop money or identity writes.

### Hot partition mitigation
| Option | Pick when | Cost |
| --- | --- | --- |
| Cache the hot key | Reads concentrate on a few keys | Staleness |
| Key salting or splitting | Writes concentrate on a key | Reads must gather the parts |
| Do nothing | Load is far below capacity | Risk at growth |

**Solo default:** do nothing and note the likely hot key; act when measured.

## How to choose: solo founder / pre-revenue defaults
- Take the **Solo default** under each table unless a number from P3 · Non-functional requirements says otherwise.
- Write the decision as: options considered, choice, reason, what would make you revisit (a named threshold).
- Never decide these purely by what is popular. Boring infrastructure wins ties.

## Human in the loop: escalate when
- Choosing AP over CP, or a lower consistency level, for money or identity data.
- A sharding key, replication model or database engine that is hard to change later (one-way door).
- Build over managed, or any new paid vendor.
- A cache or queue that holds data whose loss would cost money.
- A load-shedding rule that drops or rejects a user's money or identity action.
- Bring: options, cost, reversibility, and your recommendation.

## Done means
- Every item has options, choice and reason, or `[N/A]` with reason.
- Each choice is tied to an NFR or a recorded constraint.
- One-way doors are flagged and approved.

## Depends on / feeds into
Depends on: P3 · Non-functional requirements, P3 · Architecture, P3 · Architecture decisions. Feeds: P3 · Escalations, P3 · Architecture documentation (ADRs, rejected alternatives), P5 · Code quality (conventions), P8 · Database, P8 · API.
