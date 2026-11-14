> Draft (basic) — pending Aviv's review.

# P9 · Prompting

Checklist: [the-checklist.md § Prompting](../the-checklist.md)

## What this step decides

How prompts are structured, versioned, tested and rolled back, and how untrusted text (user input, retrieved documents) is kept from acting as instructions.

## How to think about it

- A prompt is code that ships behavior. Treat it with the same discipline: in version control, versioned by id, tested, and reversible.
- Prompt injection cannot be fully prevented by wording. Treat it as a design constraint: assume hostile text will sometimes steer the model, and make sure that steering cannot reach anything valuable (see the Output safety and Agents / tools guides).
- Separate channels: system instructions, user input and retrieved content go in clearly delimited places, and secrets never go in a prompt the model can echo.
- System-prompt leakage review: assume the prompt will be extracted. If its contents would hurt you, move them out.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Storage | Prompt files in the repo | Prompt management platform | Non-engineers edit prompts often |
| Rollout | Deploy with code, switch by flag | Experiment platform | You A/B test prompts with real traffic |
| Injection defense | Delimiting plus least-privilege design | Classifier or guard model | Observed attacks and a high-impact surface |

## How to choose: solo founder / pre-revenue defaults

- Prompts in files with a version id logged on every call, a golden-set test before changes, rollback as a revert.
- No secrets, keys or other users' data in the prompt, ever.
- Design for the worst case: if the model followed an attacker, what is the worst thing it can do? Cap that.

## Human in the loop: escalate when

- A prompt change affects safety behavior, refusals, or what data a model can see.
- A prompt would include personal data, secrets or another user's content.
- Observed successful injection or system-prompt extraction.
- Adding a guard model or vendor (new cost and new data recipient).

## Done means

- Prompts are versioned and each call logs the version.
- A change cannot ship without passing the golden set, rollback has been exercised once, and an injection test set exists and is run.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P9 · Model layer. Feeds P9 · Output safety, P9 · Agents / tools, P9 · Evaluation, P17 · Testing (AI testing).
