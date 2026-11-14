> Draft (basic) — pending Aviv's review.

# P01 · Jurisdiction

Checklist: [the-checklist.md § Jurisdiction](../the-checklist.md)

## What this step decides
Which places' laws can touch the product. P1 discovers obligations; it does not implement them. "Which law applies" is decided by where the founder, users, hosting, processing, payments and app stores are.

## How to think about it
- Walk the checklist items as a list of places: founder or company, customers, hosting, data processing, payments, contractors, app stores. Write the country or region for each.
- Law usually follows the user, not only the server. A user in a region can bring that region's rules even if you host elsewhere. Treat this as a prompt to ask counsel, not a conclusion.
- Age restrictions and regulated-industry exposure are flags that widen scope fast. Note them here and resolve them in P1 · Industry-specific.
- This guide is practical orientation, not legal advice. Where a legal point matters, confirm with counsel or Aviv.

## Options and trade-offs
| Scope choice | Pick when | Cost |
| --- | --- | --- |
| Launch in home jurisdiction only | Pre-revenue, learning | Smaller market; geo-block or say so |
| Add one region (e.g. EU) | Real demand there | Privacy regime, VAT, language |
| Global by default | Rarely at this stage | Widest legal surface; avoid |

## How to choose: solo founder / pre-revenue defaults
- Default: one home market, stated in P0 · Product, and mirror it in the store listings and terms.
- Pick a hosting region near users and inside the same legal area where possible; this avoids cross-border questions.
- Record unknowns as `[DEFER]` with a trigger such as "first paying EU customer", not as silence.

## Human in the loop: escalate when
- Adding any target jurisdiction.
- Hosting or processing outside the target users' region (data crossing borders).
- Age restriction or children as users.
- Regulated industry exposure appears.
- Any answer where the law is unclear: counsel review, via Aviv.

## Done means
- Each place type has an entry or an `[N/A]` reason.
- The list feeds the jurisdiction matrix in P1 · Compliance deliverable.

## Depends on / feeds into
Depends on: P0 · Product (geography, platforms), P0 · Business (payments). Feeds: P1 · Privacy, P1 · Commercial/legal, P1 · Industry-specific, P1 · Compliance deliverable, P3 · Non-functional requirements (residency).
