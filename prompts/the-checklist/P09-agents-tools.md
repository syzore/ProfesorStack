> Draft (basic) — pending Aviv's review.

# P9 · Agents / tools

Checklist: [the-checklist.md § Agents / tools](../the-checklist.md)

## What this step decides

What a model-driven agent is allowed to do: the tools it can call, with what permissions and arguments, within what limits, and who approves dangerous steps.

## How to think about it

- Excessive agency is the risk: too many tools, too much permission, too much autonomy. Begin by listing tools, then cut the list.
- For each tool, decide its permission (least privilege), its argument validation, and whether the result is trusted. Tool results are untrusted input, since they can carry injected instructions.
- Bound every run: maximum action count, budget, timeout, loop detection. An agent without these is an unbounded loop with your credit card.
- Side effects need protection: dry run, confirmation, idempotency keys, undo where possible. Dangerous actions need human approval by design, not by exception.
- Keep an audit log of every action: who asked, what the agent did, with what arguments.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Control flow | Fixed workflow calling the model for steps | Open-ended agent loop | The task cannot be expressed as steps |
| Tools | Read-only first | Write tools with approval | A feature needs to act |
| Approval | Human approves every side effect | Approve by risk tier | Volume and an observed safe record |

## How to choose: solo founder / pre-revenue defaults

- Prefer a fixed workflow with model-filled steps over a free-roaming agent.
- Ship read-only tools first. Add write tools one at a time, each with approval.
- Hard caps on steps, tokens and cost per run, and an audit log from day one.

## Human in the loop: escalate when

- Giving an agent any write, send, spend, delete or deploy capability.
- Reducing or removing an approval step, or raising an action or budget cap.
- Tools that reach other users' data or external systems with real consequences (email, payments, publishing).
- Loop or runaway spend observed in production.
- The agent operates on credentials that could cause irreversible changes.

## Done means

- Tool inventory with permission, validation and side-effect protection per tool.
- Tested limits (action count, budget, timeout) that abort a run, dangerous actions blocked without approval, and an audit log that reconstructs a run.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P9 · Prompting and P9 · Output safety. Feeds P9 · Evaluation, P16 · Background Jobs / Cron / Agents, P6 · Operational security (audit logging).
