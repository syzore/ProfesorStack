> Draft (basic) — pending Aviv's review.

# P25 · Monthly/periodic

Checklist: [the-checklist.md § Monthly/periodic](../the-checklist.md)

## What this step decides

The slower reviews: access, secrets and credentials, vendors, compliance, privacy, disaster recovery, dependency licenses, domain and certificates, architecture, plus deleting stale data, unused infrastructure, unused accounts.

## How to think about it

- These catch slow drift: people and keys that should no longer have access, vendors you no longer use, licenses that changed.
- Disaster-recovery review means rerunning a restore test and checking RTO and RPO still hold as data grows.
- Deleting stale data, unused infrastructure and accounts reduces risk and cost. Deletion is irreversible, so confirm first.
- Architecture review compares reality with the P3 decisions and non-functional targets, then updates the ADRs.

## Options and trade-offs

| Cadence | Good for | Cost |
|---|---|---|
| Monthly | Access, secrets, cost vendors | Time |
| Quarterly or yearly | Compliance, architecture, DR drill | Easy to skip, put in calendar |

## How to choose: solo founder / pre-revenue defaults

- Calendar reminders per item with a one-line checklist each.
- Rotate credentials that are due; remove any account or key with no owner.

## Human in the loop: escalate when

- Deleting data or infrastructure that is not clearly unused.
- Compliance or privacy scope change; confirm with counsel.
- A vendor change or new paid vendor.
- Any change that weakens an access control.

## Done means

- Each review has a dated record and its follow-up items.
- Unused accounts and infrastructure are removed or justified.

## Depends on / feeds into

Phase depends on P24 · Launch readiness. Fed by P6, P7, P23, P27. Feeds P28 · Retirement / exit (vendor and account inventory).
