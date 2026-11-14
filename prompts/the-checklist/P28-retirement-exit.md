> Draft (basic) — pending Aviv's review.

# P28 · Retirement / exit

Checklist: [the-checklist.md § Retirement / exit](../the-checklist.md)

## What this step decides

How to end the project cleanly: announce, final access date, export and delete user data, stop sign-ups and payments, cancel subscriptions, revoke secrets and keys, archive, shut down infrastructure, DNS, vendors, domains, retention duties, lessons.

## How to think about it

- Runs when the project is killed, replaced, sold or archived. Order matters: users first, money second, access third, infrastructure last.
- Stop new registrations and payments before cancelling subscriptions, so no new obligations appear.
- Retention duties (tax, legal, contract) may require keeping some records and backups. Confirm with counsel or Aviv before deleting.
- Revoke secrets and keys, and remove production access, so a forgotten account is not a way in later.
- Use the inventory from P25 and P27 to be sure nothing is left running and billing.

## Options and trade-offs

| Exit type | Key difference | Risk |
|---|---|---|
| Shutdown | Delete data, cancel everything | Obligations to users, retention law |
| Sale or handover | Transfer data, accounts, domain | Privacy and contract terms, credential handover |
| Archive | Freeze source and records | Residual costs, stale credentials |

## How to choose: solo founder / pre-revenue defaults

- Write a dated shutdown plan from the checklist order. Give users notice and an export window.
- Archive the source and a final architecture note. Record lessons learned.
- Cancel domains last, after email and DNS dependencies are gone.

## Human in the loop: escalate when

- Any user-data deletion or export at scale (irreversible).
- Cancelling subscriptions, refunds, or anything that moves money.
- Transfer of data or accounts to a buyer (privacy and contract scope).
- Cancelling a domain or vendor that cannot be recovered.
- Any retention question; confirm with counsel.

## Done means

- Users were notified and data export or deletion done as required.
- All secrets, keys, accounts and infrastructure are revoked or shut down, verified.
- Retention duties are recorded and satisfied; lessons are written.

## Depends on / feeds into

Depends on the decision to end the project. Uses inventories from P25 · Monthly/periodic and P27. Revisits P1 · Applicability / compliance discovery and P7 for data duties.
