> Draft (basic) — pending Aviv's review.

# P6 · Data security

Checklist: [the-checklist.md § Data security](../the-checklist.md)

## What this step decides

How data is protected where it sits and moves: encryption, secrets and keys, who and what can read the database and object storage, and what leaks through backups and logs.

## How to think about it

- Work from the P2 data inventory. Each field already has a reason to exist and a sensitivity; this step decides the protection that matches.
- Separate three questions: can an outsider read it (encryption in transit and at rest), can an insider or a compromised service read more than it needs (database and object-storage permissions, production-data access review), and does it leak sideways (backups, logs, redaction, PII exposure review).
- Secrets and keys are their own risk class. Decide where each lives, who can read it, how it rotates, and how it is revoked.
- Backups and logs copy data out of your normal controls. They need the same classification as the source.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Encryption at rest | Provider default disk and storage encryption | Application-level field encryption | Field is highly sensitive or contract requires it |
| Secrets | Platform secret store or env vars set by CI | Dedicated secrets manager | Several services or rotation needs grow |
| Keys | Provider-managed keys | Customer-managed keys (KMS) | Compliance or customer demands it |
| DB access | One least-privilege role per service | Per-tenant roles, row-level security | Multi-tenant data with real isolation risk |

## How to choose: solo founder / pre-revenue defaults

- Rely on provider-managed encryption and TLS everywhere. Record that it is on rather than building anything.
- One database role per service, no shared superuser in app config. Humans use short-lived or personal access, not the app role.
- Redact at the logging layer by default (deny-list of fields), and review a sample of real logs once before launch.
- Secrets never in the repo, never in client bundles, never in logs. Scan for them in CI.

## Human in the loop: escalate when

- Moving from provider-managed to self-managed keys, or any change to where secrets live.
- Granting a human or a new service read access to production personal data.
- Any plan to copy production data to a laptop, staging or a vendor.
- A suspected secret leak: rotate first, then involve Aviv; never decide to skip rotation alone.
- Disabling or weakening encryption, redaction or an access restriction, even temporarily.
- The data inventory shows a new sensitive category (health, financial, children's data), which may change compliance scope.

## Done means

- Every store in the data inventory has a stated at-rest and in-transit protection, with how it was checked.
- A list of who and what can read each store, with a reason per entry.
- Backups are covered by the same access and encryption statement, and a log sample shows no sensitive values.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P5 · Engineering Foundation. Feeds P7 · Privacy and Data Governance (log scrubbing, retention, backup deletion), P8 · Database, P13 · Files / Media, P19 · Observability (log content), P23 · Infrastructure / Reliability (backups).
