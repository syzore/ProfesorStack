> Draft (basic) — pending Aviv's review.

# P01 · Commercial/legal

Checklist: [the-checklist.md § Commercial/legal](../the-checklist.md)

## What this step decides
Which commercial and legal documents and rules apply: terms, privacy policy, refunds, consumer protection, tax, invoices, IP, licensing and open-source obligations.

## How to think about it
- Split into documents you must publish (Terms, Privacy Policy), money rules (refund, tax, invoice) and ownership rules (IP, copyright, trademark, content licensing, open-source).
- Tax and invoice duties depend on where you and the buyer are and on volume. A merchant-of-record payment provider can shift part of the load; confirm what it covers.
- Open-source obligations: list dependency licenses once; copyleft in a distributed app is the usual trap.
- Name check: search trademarks and domains before the name sticks.
- This guide is practical orientation, not legal advice. Where a legal point matters, confirm with counsel or Aviv.

## Options and trade-offs
| Choice | Pick when | Cost |
| --- | --- | --- |
| Template terms and policy, lawyer-reviewed once | Pre-revenue, low risk | One review fee |
| Merchant-of-record payments | Small volume, sells internationally | Higher fee per sale |
| Self-handle tax and invoices | Larger volume, accountant in place | Compliance work and risk |

## How to choose: solo founder / pre-revenue defaults
- Default: free product, short terms and policy from a reputable template, reviewed when money or user data starts.
- If you charge: pick the merchant-of-record route first and revisit at volume.
- Record license check as a dependency-list item in P5 and P6 supply chain.

## Human in the loop: escalate when
- First charge, refund policy, or any price or tax decision.
- Publishing or changing Terms or Privacy Policy.
- Trademark or name conflict, copyright or licensing exposure, user-uploaded content ownership.
- A copyleft or restrictive dependency license in shipped code.
- Anything counsel should read: put it on the P1 · Compliance deliverable list.

## Done means
- Each item answered or `[N/A]` with reason.
- Documents needed are listed with owner and when they must exist (usually before launch).

## Depends on / feeds into
Depends on: P0 · Business, P1 · Jurisdiction, P1 · Privacy. Feeds: P1 · Compliance deliverable, P4 · UX (terms acceptance, refund flows), P10 · Payments, P24 · Legal/business, P24 · Launch.
