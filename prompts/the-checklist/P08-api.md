> Draft (basic) — pending Aviv's review.

# P8 · API

Checklist: [the-checklist.md § API](../the-checklist.md)

## What this step decides

The external contract: the shape of requests and responses, who may call what, how errors, lists and limits behave, and how the contract changes over time.

## How to think about it

- The contract comes first: write the schema (request, response, error) before handlers. Authentication and authorization are part of each endpoint's contract, not middleware you hope is there.
- List behavior (pagination, filtering, sorting) is cheap to define now and painful to change once clients depend on it.
- The cost-and-reach item matters: any endpoint that spends money (LLM calls, paid APIs) or contacts a person (email, feedback) needs a per-user limit, apart from generic rate limiting. Name the limit, the identity it keys on, and the behavior when exceeded.
- Error schema is for machines (stable codes) and humans (safe messages). Errors must not leak internals or confirm account existence.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Style | REST/JSON with a generated schema | GraphQL or RPC framework | Many client shapes or a typed multi-language need |
| Pagination | Cursor for growing lists, offset for small | Keyset with total counts | Stable ordering across heavy writes |
| Versioning | Additive changes only, version when breaking | URL version per resource | Public or third-party clients |
| Docs | Generated from the schema | Hand-written portal | External developers |

## How to choose: solo founder / pre-revenue defaults

- Generate documentation from the schema so it cannot drift. Add fields, never repurpose them.
- Version only when you must break a client, and pre-revenue with your own client you can usually ship both sides together.
- Per-user limits first on the money and reach endpoints, in a simple counter with a clear error.

## Human in the loop: escalate when

- A public API, or a client you do not control (third-party, mobile versions in the wild), is introduced.
- A breaking change to a contract with live clients.
- A per-user limit is raised or removed on an endpoint that costs money or messages people.
- An endpoint exposes data across users or tenants, or accepts a new kind of credential.

## Done means

- Every endpoint has request, response and error schemas, an authorization rule and a rate-limit decision.
- Contract tests or schema validation fail on drift, and the cost-bearing endpoints demonstrably refuse requests over the limit.

## Depends on / feeds into

Depends on P3 · System Architecture, P4 · UX, UI, Accessibility and Internationalization, P5 · Engineering Foundation, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P8 · Domain. Feeds P9 · Model layer (per-user limits), P12 · Email / Notifications, P17 · Testing (API), P18 · Performance.
