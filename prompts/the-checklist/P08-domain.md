> Draft (basic) — pending Aviv's review.

# P8 · Domain

Checklist: [the-checklist.md § Domain](../the-checklist.md)

## What this step decides

The rules of the product independent of any screen or table: entities, what must always be true, allowed state changes, who may do what, and what happens when things go wrong or collide.

## How to think about it

- Write the domain down before the API and schema. The API and database sections are projections of it.
- Start with entities and invariants (what can never be false). Then state machines and lifecycle transitions: each state, the events that move it, and who may trigger them (permissions).
- The tail of the list is where bugs live: error cases, edge cases, concurrency cases and idempotency behavior. For each mutation ask: what if it runs twice, what if two run at once, what if it half-finishes.
- Use the project's GLOSSARY terms for entity names. One concept, one name.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Lifecycle | Status column plus allowed-transition table | Event sourcing | Audit or replay is a product requirement |
| Concurrency | Database constraints and transactions | Distributed locks | Several writers outside one database |
| Idempotency | Unique key per client action | Stored request log | Payments or other external side effects |
| Rules location | Plain functions in one domain module | Rules engine | Rules change without deploys |

## How to choose: solo founder / pre-revenue defaults

- One page: entity list, invariant list, one state diagram per entity with a status, and a permission table.
- Enforce invariants in the database where possible (constraints), and in one domain function where not.
- Prefer a status column and a transition table over event sourcing, queues or a rules engine.

## Human in the loop: escalate when

- An invariant that protects money, identity or irreversible data, if you are changing or relaxing it.
- A lifecycle transition that cannot be undone (delete, merge, publish, charge).
- A permission model change: new role, delegated access, anything where one user acts on another's data.
- Behavior in an edge case that is a product call (who wins when two users edit at once), not a technical one.

## Done means

- Each entity has invariants and a state diagram, and each mutation names its error cases, concurrency behavior and idempotency behavior.
- Invariants map to a test or a constraint, and permissions map to the P6 authorization model.

## Depends on / feeds into

Depends on P3 · System Architecture, P4 · UX, UI, Accessibility and Internationalization, P5 · Engineering Foundation, P6 · Security Foundation, P7 · Privacy and Data Governance. Feeds P8 · API, P8 · Database, P10 · Payments (entitlements), P16 · Background Jobs (idempotency), P17 · Testing.
