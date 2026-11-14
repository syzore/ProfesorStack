> Draft (basic) — pending Aviv's review.

# P10 · Payments

Checklist: [the-checklist.md § Payments](../the-checklist.md)

## What this step decides

Everything that changes when money moves: provider, pricing model, checkout, failure paths, webhooks, refunds, entitlements, reconciliation, tax and accounting. The phase has no sub-sections, so this guide covers it all.

## How to think about it

- Applies only if money changes hands. If not, mark the phase `[N/A]` with that reason.
- The system of record for payments is the provider. Your database holds a mirror, and your job is to keep the mirror correct and to turn it into entitlements (what the user may use).
- Think in events and failure, not the happy path. Group the items: setup (provider, merchant account, currency, product and price model), flows (checkout, trials, coupons, upgrades, downgrades, proration, cancellation), failure (declines, failed renewal, chargebacks, refunds), the webhook plumbing (authentication, idempotency), and the back office (invoices, tax, reconciliation, reporting, accounting).
- Webhooks arrive late, twice, or out of order. Verify the signature, store the event id, make handlers idempotent, and reconcile against the provider on a schedule.
- Per the rules, every paid capability needs billing failure behavior: say what the user keeps or loses when payment fails, and for how long.
- Taxes and invoicing law depend on where you and your customers are. Do not guess; use a provider feature that handles it, and confirm the setup with an accountant or Aviv.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Provider | Hosted checkout from a major provider | Custom payment form | Hosted flow blocks a required experience |
| Merchant of record | Consider one for global digital sales | Direct merchant account | Volume justifies handling tax yourself |
| Billing | Provider-managed subscriptions and portal | Own billing engine | Pricing too custom for the provider |
| Entitlements | One table written only by webhook handlers | Provider queried live | Low volume and stale risk is acceptable |

## How to choose: solo founder / pre-revenue defaults

- Use hosted checkout and the provider's customer portal. Never store card data.
- Keep pricing simple: one or two plans, one currency, until sales show otherwise.
- Build entitlement as a single derived table with one writer, so revocation has one path.
- Test in provider sandbox with failure cases: decline, expired card, duplicate webhook, refund after cancel.

## Human in the loop: escalate when

- Choosing or switching the payment provider or merchant structure, a one-way door with legal and tax consequences.
- Setting or changing prices, currencies, trial or refund policy.
- Any live-money action: issuing refunds outside the written policy, manual entitlement overrides, data fixes to payment records.
- Tax, invoicing and accounting setup. Confirm with an accountant or Aviv.
- A chargeback, a dispute, or a reconciliation mismatch.
- Any change that moves card data into your systems (compliance scope change).

## Done means

- Every failure path has defined user-facing behavior and a test in sandbox.
- Webhooks verify signature and are idempotent (replay test), entitlements are granted and revoked from events only, and a reconciliation job or report matches provider totals to your records.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance, P8 · Core Product Implementation. Feeds P16 · Background Jobs (reconciliation), P12 · Email / Notifications (receipts), P24 · Launch Readiness (Legal/business), P25 · Post-Launch Operations.
