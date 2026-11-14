> Draft (basic) — pending Aviv's review.

# P02 · Data lifecycle

Checklist: [the-checklist.md § Data lifecycle](../the-checklist.md)

## What this step decides
What happens to data across its life: collection, validation, storage, processing, caching, backups, replication, export, deletion, disaster recovery, vendor deletion and log deletion.

## How to think about it
- Walk each stage for each sensitive entity from P2 · Data inventory. Most gaps hide in the later stages: backups, caches, logs and vendors keep copies after "delete".
- Deletion has to reach every copy. Write the order: primary data, caches, derived data, backups (by expiry), vendors (by request or API), logs.
- Backups and disaster recovery set targets that P3 · Non-functional requirements turns into RPO and RTO. Ask "how much loss can I live with" before picking a tool.
- Validation at collection is cheaper than cleanup later.

## Options and trade-offs
| Stage | Common trap | Mitigation |
| --- | --- | --- |
| Caching | Stale or undeleted copies | TTLs, delete-on-delete |
| Backups | Deleted data persists | Fixed retention, document it |
| Vendors | Data stays at third parties | Deletion API or request, record it |
| Logs | Personal data in logs | Avoid logging it; set log retention |

## How to choose: solo founder / pre-revenue defaults
- Default: one primary database, managed automated backups with point-in-time recovery if the provider has it, and a restore test once before launch.
- Log without personal data and give logs a short retention.
- Prefer deletion by expiry to custom purge jobs where the law allows; confirm with counsel.

## Human in the loop: escalate when
- Retention longer than the privacy policy or the P1 answers.
- Choosing an RPO above zero for customer data (see P3 · Escalations).
- Any irreversible deletion or migration of live data.
- Deletion that cannot reach a vendor.
- Backup or DR approach that adds cost or cross-region copies.

## Done means
- Each stage is answered for each data class.
- A tested path exists for deletion and for restore, with evidence.
- Vendor and log deletion are written with owner.

## Depends on / feeds into
Depends on: P2 · Data inventory, P1 · Privacy. Feeds: P3 · Non-functional requirements (durability, privacy), P3 · Architecture (backup, queue, cache), P3 · Escalations, P6 · Data security, P24 · Operations.
