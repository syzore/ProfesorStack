> Draft (basic) — pending Aviv's review.

# P6 · Supply chain

Checklist: [the-checklist.md § Supply chain](../the-checklist.md)

## What this step decides

How much you trust the code you did not write and the pipeline that ships your own: dependencies, lock files, scanners, update policy, licenses, CI permissions and secrets, images, and build integrity.

## How to think about it

- The risk is two-sided. Third-party packages can be malicious or vulnerable, and your CI can be abused to ship something you did not write. CI permissions and CI secrets are often the weaker side.
- An inventory and lock files make the rest possible: you cannot scan or update what you cannot list or reproduce.
- Update strategy is a policy choice between staying current (more churn) and staying pinned (more exposure). Decide it once and write it down.
- Package review is judgement, not a scan: age, maintainers, install scripts, how much it does versus how much you need.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Scanning | Platform-native dependency alerts | Dedicated SCA tool | Many dependencies or customers ask for reports |
| Updates | Grouped automated PRs, reviewed weekly | Manual quarterly | Few dependencies, stable product |
| CI permissions | Read-only default token, grant per job | Org-wide policy engine | Several repos or contributors |
| Provenance | Skip, record as DEFER | Signed builds and attestations | Distributing software or a customer requires it |

## How to choose: solo founder / pre-revenue defaults

- Commit lock files, turn on the platform's dependency alerts and secret scanning, and run an automated update bot with grouped PRs.
- Prefer fewer, well-known dependencies. Before adding one for a few lines of code, write the lines.
- Set CI tokens to least privilege and keep deploy credentials in environment-scoped secrets that PRs from forks cannot read.
- `[DEFER]` provenance and image signing with a trigger (first enterprise customer, distributing binaries). Run license scanning once before launch for copyleft surprises.

## Human in the loop: escalate when

- A new paid scanner or registry vendor.
- Granting CI a new write permission, a production deploy credential, or access to secrets from untrusted triggers.
- A critical vulnerability with no patched version in a package that handles auth, payments or user data.
- A license that looks restrictive (copyleft in a distributed app): confirm with counsel or Aviv, do not interpret it yourself.
- Pinning, forking or replacing a core dependency (one-way-door risk).

## Done means

- Inventory and lock files are in the repo and CI fails if they drift.
- Alerts for vulnerabilities and leaked secrets are on and routed to a named owner.
- CI permissions and secrets have been reviewed and the result recorded, with the update policy written down.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P5 · Engineering Foundation. Feeds P5 · Configuration, P22 · Deployment / CI/CD, P27 · Project Maintenance / Agent Hygiene (update cadence).
