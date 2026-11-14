> Draft (basic) — pending Aviv's review.

# P02 · Data inventory

Checklist: [the-checklist.md § Data inventory](../the-checklist.md)

## What this step decides
A complete list of stored entities and fields, with the reason, owner, sensitivity, retention, access and third-party exposure for each. It is the source for privacy, security and the schema.

## How to think about it
- Work entity by entity, then field by field. One row per field in a table is fine.
- "Why does it exist?" is the filter. A field with no use does not get stored.
- Sensitivity classes can be simple: public, internal, personal, sensitive. The class drives access, retention and encryption.
- Mark each field as user-generated, derived or analytics, and whether any third party receives it. Derived data can usually be regenerated, so it has softer retention.
- For read, modify and delete rights, name roles from P2 · Users.

## Options and trade-offs
| Column | Why it exists |
| --- | --- |
| Entity, field | Completeness |
| Reason | Cut unneeded collection |
| Sensitivity | Drives controls |
| Owner, retention, deletion | Feeds P2 · Data lifecycle |
| Read/modify/delete roles | Authorization rules |
| Third-party recipients | Privacy and vendor list |

## How to choose: solo founder / pre-revenue defaults
- Default: store less, derive more. Do not store what you can compute cheaply.
- Prefer a managed database's schema file as the source and generate the table from it so the inventory does not drift.
- Keep sensitive fields in separate tables or columns so access can be narrower.

## Human in the loop: escalate when
- Adding a sensitive, children's, biometric or location field.
- A field newly sent to a third party.
- Changing retention or deletion in a way that loses data (irreversible).
- Any field that touches money or identity.
- A purpose that was not in the privacy answers from P1 (scope change).

## Done means
- Every entity and field has all columns filled or an `[N/A]` reason.
- No field without a reason.
- Third-party recipients match the vendor list in P3 · Architecture.

## Depends on / feeds into
Depends on: P2 · Users, P1 · Privacy, P1 · Compliance deliverable. Feeds: P2 · Data lifecycle, P3 · Architecture (database choice), P3 · Scale (storage growth), P8 · Database, P6 · Data security.
