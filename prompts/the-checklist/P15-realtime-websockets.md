> Draft (basic) — pending Aviv's review.

# P15 · Realtime / WebSockets

Checklist: [the-checklist.md § Realtime / WebSockets](../the-checklist.md)

## What this step decides

Whether the product needs live, two-way updates, and if so how connections are secured, bounded, recovered and scaled. Phase-level guide.

## How to think about it

- Persistent connections change the failure model: state lives in the server, clients disconnect constantly, and one slow client can hurt many.
- First ask whether polling or server-sent events would do. Most notification and feed updates do not need a bidirectional socket.
- Authenticate when the connection opens and re-check authorization per message or subscription. A connection stays open long after a session or permission changes.
- Bound everything: connections per user, message size, message rate. Add heartbeats to detect dead peers.
- Define behavior for the ugly cases: reconnect (resume or resync from a source of truth), duplicate and out-of-order messages, backpressure when a client reads slowly, and disconnect cleanup.
- Presence and horizontal scaling are costly features. Decide whether you need them at all.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Transport | Polling or server-sent events | WebSockets | Low-latency two-way traffic, such as collaboration or games |
| Hosting | Managed realtime service or single instance | Self-run cluster with pub/sub | Connection count outgrows one instance |
| Delivery | At-least-once with idempotent handlers and resync | Ordered exactly-once design | Strict ordering is a product requirement |
| Presence | Skip or approximate | Tracked presence | Product feature demands it |

## How to choose: solo founder / pre-revenue defaults

- Start with a single instance, sequence numbers on messages, and a resync-on-reconnect endpoint that returns full state.
- Cap per-user connections and message size, and rate-limit messages.
- Defer horizontal scaling with a trigger, e.g. connection count near one instance's limit.

## Human in the loop: escalate when

- Choosing a managed realtime vendor (new paid vendor, data recipient).
- A scaling approach that changes architecture, such as shared pub/sub or sticky sessions.
- Allowing connections from unauthenticated users, or broadcasting data across users or tenants.
- Relaxing connection, size or rate limits.

## Done means

- Auth, authorization, size and rate limits each have a failing test.
- Reconnect, duplicate and out-of-order scenarios have been tested, a load test shows the connection ceiling, and a disconnect leaves no leaked state.

## Depends on / feeds into

Depends on P3 · System Architecture, P6 · Security Foundation, P8 · Core Product Implementation. Feeds P18 · Performance, P19 · Observability, P23 · Infrastructure / Reliability (scaling).
