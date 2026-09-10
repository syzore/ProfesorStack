---
name: product-council
description: "Use for /product-council, \"convene the council\", \"review this product\", or before committing to build something — seats specialist advisors on a product idea or an existing repo, then makes a call on whether it should exist."
disable-model-invocation: true
---

# Product council

Advisors, not voters. The council exists to surface disagreement worth resolving,
not to produce the average opinion of eleven agents.

## A seat has to beat the generalist

Measured on a salted product brief (broken unit economics, one deletable feature,
a consent problem): an eleven-seat council found the planted flaws — and lost to a
single agent asked to review the same brief with no roles at all.

The generalist won on the findings no seat owned. It connected finite camera-roll
backlog to churn to *the subscription is the wrong shape*, and it priced against
StoryWorth and Chatbooks. The council's seats each stayed in lane and echoed the
same three findings in eleven vocabularies.

Two consequences, and they govern everything below:

**Partitioning destroys cross-cutting insight.** The best finding in a product
review usually lives between two seats. Nobody assigned to a lane goes and gets it.
That is the Founder's job, and it is most of the Founder's job.

**A seat earns its cost only by bringing something the generalist can't** — a
number, a comparable, a competitor's actual behaviour, a failure mode from its
domain. A seat that reasons from the brief alone is a rephrasing engine. Cut it.

## Point it at something

| What you're given | What to read first |
| --- | --- |
| An idea in conversation or a doc | The brief as stated. Do not improve it silently — the gaps are findings. |
| A repo or a shipped product | Code, README, docs, recent commits. Seats critique what exists, not what's described. |

State which mode you're in before seating anyone. In repo mode, a seat that never
opened the code is guessing.

## Triage before you spawn

Read the product. Decide what it's actually uncertain about. Seat only those.

A pricing question does not need a Brand seat. A CLI does not need Design. Seating
everyone is how you get eleven agents agreeing at length, which the test above
shows is worse than one agent thinking hard.

**Always seated**

| Seat | Job |
| --- | --- |
| Generalist | Same brief, no lane, no persona. The control. |
| Adversarial Critic | Try to kill it. Assumptions, perverse incentives, failure modes, why someone abandons it. |
| Simplicity Editor | Delete things. Every feature, screen, setting and abstraction justifies itself or dies. |

**Seated when the product is uncertain there**

| Group | Seats |
| --- | --- |
| Desirability | User Advocate · UX · Psychology · Design |
| Strategy | Product Strategist · Competitive Intelligence · Brand & Narrative |
| Viability | Business & Economics · Growth · Marketing |
| Feasibility | Technical Architect · AI Architect · Security & Trust |
| Truth | Data & Experimentation |

The User Advocate is not UX. UX designs the experience; the Advocate fights for the
confused, impatient, skeptical user against the person who built it.

Growth is not Marketing. Marketing gets someone in. Growth makes the product spread.

Spawn the seated ones in parallel, one agent each. Parallel is not an optimisation —
run in sequence they read each other and defer instead of arguing. In the test, the
sequential Adversarial Critic wrote "the economics, covered above" and moved on.

## What a seat returns

Every seat returns these four, in this order:

1. **Finding** — the one thing that most changes the decision. Not a survey of the domain.
2. **Evidence** — a number, a comparable product's real pricing, a competitor's actual
   behaviour, a measured cost. From outside the brief. A seat with no outside evidence
   says so, in those words, and that absence is itself reportable.
3. **Contradiction** — the premise or the seat it disagrees with, named.
4. **Cost of being wrong** — what it costs to ignore this.

A seat may add a second finding. It may not add a third.

**Design seat, conditional:** if the repo root has `PRODUCT.md` and `DESIGN.md`, it has
[impeccable](https://github.com/pbakaus/impeccable) installed — run its review commands
(`critique`, `audit`) and report what they flag. If those files are absent, review by
eye and move on. Do not propose installing it in a CLI, a data pipeline, or anything
with no user-facing frontend.

## The Founder's synthesis

You are not trying to satisfy the council. You are trying to build the best product.
Resolve disagreement by identifying the underlying uncertainty and deciding what
evidence would settle it.

The write-up is exactly this, in this order:

1. **The call** — build, don't build, or build this narrower thing. First line, before any reasoning.
2. **What the seats disagreed about** — the real conflicts, and which way you went on each. If no two seats conflicted, say that; it means the council told you nothing and the Generalist's finding stands alone.
3. **What the Generalist found that no seat did** — and what that says about the seats you chose.
4. **The uncertainty underneath** — the thing you don't know that would change the call.
5. **The evidence that settles it** — the experiment, the number to go find, the thing to build and watch.
6. **The cut list** — what dies, from the Simplicity Editor.

**Required before it goes on screen:** run the write-up through **unslop**. A verdict
that reads like AI filler gets dismissed regardless of what it found.

## When the council splits on taste

Seats arguing about what something should feel like will not converge by arguing
longer. That is a question, and **prototype** exists to answer questions with
throwaway code — a state model you can drive, UI variants behind a URL param, or
variants shipped with the clicks counted.

Deadlock on fact is different. Fact deadlock resolves by going and getting the fact.

## Landing it

Print the verdict and stop. Do not name a repo you never opened. In testing, a run
that had correctly declared "no repo" at the top still closed by offering to file
issues against a specific one it had invented.

## Failure modes

| Symptom | What it means |
| --- | --- |
| Every seat agrees | You seated eleven rephrasings of one opinion. The council added nothing; say so. |
| Seats cite only the brief | Nobody went outside. The findings are the brief reflected back. |
| Synthesis summarises the seats | Not a synthesis. No call, no uncertainty, no evidence — start the write-up over. |
| A seat wrote an essay | Contract is four parts. Essays hide the finding. |
| The Generalist won | Report it. Fewer, better-chosen seats next time. |
| Council proposes features | The Simplicity Editor is asleep. Its default answer is "can we delete this?" |
