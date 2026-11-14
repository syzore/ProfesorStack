> Draft (basic) — pending Aviv's review.

# P01 · Privacy

Checklist: [the-checklist.md § Privacy](../the-checklist.md)

## What this step decides
Whether the product handles personal data, which kinds, and what that implies for consent, retention, deletion, access and cookies. This decides obligations, not mechanisms.

## How to think about it
- Start with the data, not the law: personal, sensitive, children's, location, behavioral/analytics, payment. Each yes brings extra duties.
- Third-party processors and cross-border transfers are separate questions. Every vendor that sees user data is a processor to list.
- Retention, deletion, access/export and consent are obligations to record now so P2 can design them in rather than retrofit.
- Cookie and tracking rules differ by region and by whether the cookie is strictly needed. The `compliance` skill covers web items. Use it when a banner, analytics snippet or login session is added.
- This guide is practical orientation, not legal advice. Where a legal point matters, confirm with counsel or Aviv.

## Options and trade-offs
| Data stance | Pick when | Cost |
| --- | --- | --- |
| Collect nothing personal | Tool works anonymously | No accounts, no personalization |
| Minimal (email + needed fields) | Accounts needed | Privacy policy, deletion and export flows |
| Analytics on | You will act on the numbers | Consent or disclosure, a processor |

## How to choose: solo founder / pre-revenue defaults
- Default: collect the least. Every user-data field needs a reason to exist (checklist rule), so refuse fields with no use.
- Prefer privacy-preserving or first-party analytics over a tracking stack until a decision depends on the data.
- Do not collect sensitive or children's data pre-revenue unless the product is about it.

## Human in the loop: escalate when
- Sensitive data, children's data, location, or biometrics appear.
- Data would cross a border or go to a new third party.
- Consent wording, retention periods or deletion promises with legal weight.
- Any change that widens collected data after launch (compliance scope change).
- Policy text itself: Aviv or counsel approves.

## Done means
- Every item answered yes/no with the source of the answer.
- Yeses are carried into P2 · Data inventory and P2 · Data lifecycle.

## Depends on / feeds into
Depends on: P0, P1 · Jurisdiction. Feeds: P1 · Commercial/legal (Privacy Policy), P1 · Compliance deliverable, P2 · Data inventory, P2 · Data lifecycle, P3 · Non-functional requirements (privacy and compliance), P4 · UX (consent UI).
