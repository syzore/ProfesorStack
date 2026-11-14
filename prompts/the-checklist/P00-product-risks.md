> Draft (basic) — pending Aviv's review.

# P00 · Product risks

Checklist: [the-checklist.md § Product risks](../the-checklist.md)

## What this step decides
Which risks could kill the product, which assumptions carry them, and which experiments to run before building heavily.

## How to think about it
- List risks per category (product, technical, security, legal/compliance, operational, dependency/vendor) and keep each to one line plus a likelihood and impact guess.
- Single points of failure include people: the founder, one vendor, one API key, one domain registrar.
- Highest-risk assumptions are the ones that, if false, make the product pointless. Rank by "cost if wrong", not by how worried you feel.
- An experiment is a cheap test with a pass/fail line, e.g. "10 of 15 interviewed users do the primary action in a mockup". Prefer interviews, fake-door pages or a throwaway prototype over production code.

## Options and trade-offs
| Risk response | Pick when | Cost |
| --- | --- | --- |
| Experiment first | Assumption is unproven and the build is large | Days of delay |
| Mitigate in design | Risk is known and cheap to cover | Added scope |
| Accept and record | Low impact or reversible | Possible later rework |
| Drop the feature | Risk outweighs value | Smaller product |

## How to choose: solo founder / pre-revenue defaults
- Three to seven risks total. A long list hides the real ones.
- Always include the top vendor risk: for each external dependency, an owner, a failure mode and a replacement path (the checklist's operating rule).
- Run the cheapest experiment that could falsify the top assumption before P3 locks architecture.

## Human in the loop: escalate when
- A top risk has no mitigation and no experiment.
- A legal or compliance risk is named: it goes to P1 and probably to counsel.
- An experiment needs real users' data, money or outreach in Aviv's name.
- A risk implies a one-way door or a paid vendor.

## Done means
- Each category has at least one line or an `[N/A]` reason.
- Single points of failure are listed with who or what.
- Each high-risk assumption has an experiment or a recorded acceptance.

## Depends on / feeds into
Depends on: P0 · Product, P0 · Business. Feeds: P1 (legal risks seed discovery), P3 · Architecture and P3 · Architecture decisions (technical and dependency risks), P3 · Escalations, P6 · Application security, P24 · Operations.
