> Draft (basic) — pending Aviv's review.

# P6 · Application security

Checklist: [the-checklist.md § Application security](../the-checklist.md)

## What this step decides

Which attacks the app must resist, and the concrete control and acceptance test for each. The section runs from the threat model through the per-vulnerability protections (injection, XSS, CSRF, SSRF, path traversal, open redirect) to the edge items (CORS, headers, CSP, cookies, TLS, rate limiting, edge proxy).

## How to think about it

- Start with the threat model and the trust-boundary review. Every later item is a response to something found there. An item with no named threat is a checkbox, not a control.
- Group by boundary: who can call what (authentication, authorization, object-level authorization, privilege escalation), what enters (input validation, injection, file upload, SSRF), what leaves (output encoding, XSS, CSP), and how the session is held (cookies, tokens, fixation).
- Object-level authorization is the item most often missed: every read and write of a record by id needs an owner check, not just a login check.
- Per the checklist rules, every privileged action needs an authorization rule and every security requirement needs an acceptance criterion. Write the test first: a request that must fail, and how you know it failed.
- Mark `[N/A]` with a reason when a surface does not exist (no cookies means no CSRF item, no uploads means no upload item). Do not leave them blank.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Auth | Managed identity provider | Self-built auth | Never at pre-revenue |
| Rate limiting | Provider or edge proxy limits plus a per-user counter | Dedicated gateway | Abuse is observed or endpoints cost money |
| WAF / DDoS | Edge proxy with managed rules | Self-run WAF | Compliance requires it |
| Validation | Schema validation at the boundary | Per-handler hand checks | Never |

## How to choose: solo founder / pre-revenue defaults

- Use the managed identity provider, framework defaults for cookies and CSRF, and an edge proxy for TLS, DDoS and per-IP limits.
- Validate at one boundary layer with schemas. Reject, do not repair.
- Use ASVS (the checklist names it) as the detailed layer only for the levels that match the product's risk. Pre-revenue, a short list of must-pass tests beats the full catalogue.
- Never write your own crypto, password hashing or token format.

## Human in the loop: escalate when

- A change would weaken an existing control (looser CORS, CSP `unsafe-*`, disabled CSRF, relaxed rate limit).
- Auth model changes: new login method, new role, account linking, any impersonation or admin override path.
- A new paid vendor appears in the security path (WAF, bot protection, identity).
- A feature accepts user-supplied URLs or files from untrusted users for the first time (SSRF and upload scope grow).
- Anything touching payments or stored sensitive data is in scope and the threat model has not been reviewed by a human.

## Done means

- A written threat model exists, with each threat mapped to a control or to an `[N/A]` reason.
- Each applicable item has an acceptance test that fails before the control and passes after (status VERIFIED, not just IMPLEMENTED).
- Authorization tests cover another user's object id for every endpoint that takes one.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P5 · Engineering Foundation. Feeds P6 · Data security, P8 · API, P9 · Prompting and Output safety (injection), P13 · Files / Media, P15 · Realtime (connection auth), P17 · Testing (security testing).
