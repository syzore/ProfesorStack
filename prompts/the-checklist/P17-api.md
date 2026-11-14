> Draft (basic) — pending Aviv's review.

# P17 · API

Checklist: [the-checklist.md § API](../the-checklist.md)

## What this step decides

The request-level contract tests: happy paths, invalid input, unauthorized access, forbidden access, missing resources, duplicate requests, rate limiting, timeouts, provider failures.

## How to think about it

- Each endpoint needs the same small matrix: works, bad input, no identity (401), wrong identity (403), not found, repeated.
- Unauthorized and forbidden are different tests. Anyone can pass 401 and still leak data on 403.
- Duplicate requests test idempotency: retries of a payment or job must not double-apply (see idempotency strategy in P3).
- Timeouts and provider failures check that the API returns a defined error and does not hang or leak internals.

## Options and trade-offs

| Style | Good for | Cost |
|---|---|---|
| Contract/schema tests | Shape of responses, versioning | Does not prove behavior |
| Request tests against a test server | Auth, status codes, side effects | Needs database setup |

## How to choose: solo founder / pre-revenue defaults

- Generate the matrix from the API spec so each new endpoint gets it for free.
- Test status codes and error bodies, not only 200s.
- Rate-limit tests use a small configured limit, not real volume.

## Human in the loop: escalate when

- A test reveals an endpoint that returns data it should not (treat as a security incident, P6).
- The error contract is about to change for existing clients.

## Done means

- Every endpoint in P8 · API has the matrix, or `[N/A]` with reason.
- Duplicate-request tests pass for every non-idempotent write.
- Error responses never expose stack traces or secrets.

## Depends on / feeds into

Phase depends on P8 · Core product implementation and every relevant conditional module (P9 to P16). Feeds P17 · Security testing and P22 · Deployment / CI/CD.
