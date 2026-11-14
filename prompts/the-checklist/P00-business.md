> Draft (basic) — pending Aviv's review.

# P00 · Business

Checklist: [the-checklist.md § Business](../the-checklist.md)

## What this step decides
How the product earns, or why it does not, and the cost ceilings that bound every later technical choice.

## How to think about it
- Pick the model first (free, subscription, one-time, usage-based, ads, affiliate, marketplace), then B2B, B2C or B2B2C. B2B changes support, security review and invoicing; marketplace changes payments and legal.
- Cost ceilings are the real output: maximum infrastructure cost per month and maximum API/LLM cost, each tied to a revenue or budget number. P3 · Non-functional requirements turns them into a monthly and per-user cost ceiling.
- Support and refund expectations are promises. Write what you can actually keep alone.
- Gross margin only matters when a per-use cost exists (LLM calls, SMS, payment fees). Do the arithmetic for one active user.

## Options and trade-offs
| Model | Pick when | Cost to the founder |
| --- | --- | --- |
| Free | Learning phase, no price signal needed | Pays all infra; needs a cap |
| Subscription | Repeated value, recurring cost | Billing, dunning, tax, cancellation flows |
| One-time | Simple tool, low upkeep | No recurring revenue to cover recurring cost |
| Usage-based | Cost scales per use (LLM, API) | Metering, billing failure behavior |
| Ads / affiliate | Large audience, low price tolerance | Privacy and consent load, low yield early |

## How to choose: solo founder / pre-revenue defaults
- Default pre-revenue: free, with a hard cap on infra and API spend. Choose a paid model only when the checklist's P1 commercial items are answered.
- Prefer the payment provider that handles tax and invoices as merchant of record, if volume is small. Confirm tax treatment with Aviv or an accountant.
- Set ceilings low (e.g. a monthly number you would shrug at losing) and let the guide in P3 · Escalations govern raising it.

## Human in the loop: escalate when
- Any real-money flow: first charge, payout, refund policy, price change.
- Choosing or switching the business model.
- A cost ceiling is set, raised, or an estimate exceeds it.
- A paid vendor is needed to make the model work (payment, billing).
- Refund or support promises with legal weight; confirm with Aviv and counsel.

## Done means
- Model, classification and ceilings are written with numbers.
- Support and refund expectations match what one person can deliver.
- Margin is computed for one typical user where per-use costs exist.

## Depends on / feeds into
Depends on: P0 · Product (user, problem). Feeds: P1 · Commercial/legal (tax, refund, consumer rules), P3 · Non-functional requirements (cost ceiling), P3 · Scale (worst-case cost), P3 · Escalations (cost threshold).
