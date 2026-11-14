> Draft (basic) — pending Aviv's review.

# P11 · Ads / Monetization

Checklist: [the-checklist.md § Ads / Monetization](../the-checklist.md)

## What this step decides

Whether and how advertising or tracking-supported revenue works: providers, placements, consent and personalization, failure and blocker behavior, restrictions, and the privacy and accessibility cost. Phase-level guide.

## How to think about it

- Applies only if advertising or tracking-supported monetization exists. Otherwise `[N/A]` with a reason.
- Ads are a privacy decision first and a revenue decision second. Consent, tracking, personalization and the non-personalized fallback must be settled before provider choice, because jurisdiction (P1) decides what is allowed.
- Minors and age restrictions can change the whole model. Decide early whether any user could be a minor.
- Weigh the UX and performance cost against expected revenue. Compare against a realistic estimate, not the provider's headline numbers.
- Define failure behavior: what the layout does when an ad fails, loads slowly, or is blocked. The product must work without ads.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Ads | None; revenue from payments | Ad network | Traffic is large and free usage is core |
| Personalization | Non-personalized or contextual ads | Personalized with consent | Revenue gap justifies the compliance load |
| Provider | One network via a consent-management tool | Mediation and header bidding | Fill rate or revenue measured as the limit |
| Placement | Few, fixed slots | Dynamic placement | Tested to improve revenue without harming retention |

## How to choose: solo founder / pre-revenue defaults

- Delay ads. At pre-revenue, record `[DEFER]` with a trigger such as a traffic threshold, or `[N/A]`.
- If used, start non-personalized, one provider, a few slots, with a consent tool the provider supports.
- Measure retention and performance before and after.

## Human in the loop: escalate when

- Any decision to add ads or third-party tracking at all.
- Choosing a provider or consent platform (new vendor, new data recipients).
- Enabling personalization, or serving ads to a population that may include minors.
- Content categories shown or blocked, since brand and trust call.
- A change in consent behavior or compliance scope.

## Done means

- The advertising model, consent matrix per jurisdiction and fallback behavior are written down.
- Ad failure and blocker states are tested, performance and accessibility impact are measured, and the privacy policy reflects the ad data flows.

## Depends on / feeds into

Depends on P1 · Applicability / Compliance Discovery, P2 · Users, Trust and Data Model, P4 · UX, UI, Accessibility and Internationalization, P7 · Privacy and Data Governance, P8 · Core Product Implementation. Feeds P20 · Analytics and Experimentation, P18 · Performance, P24 · Launch Readiness.
