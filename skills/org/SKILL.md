---
name: org
description: The agent org chart and routing rules. Use when routing a task to a manager or agent, when no agent or skill fits a task, or when collecting improvement proposals.
---

# Org

Aviv talks to one agent, the **co-founder**. Work flows down a strict chain:

```
co-founder → manager → specialist
           ↘ hr (hires agents, applies approved improvements)
```

**Agents are who does the work. Skills are how.** Every task names both.

## Rules

1. Every task is handled by an agent and uses at least one existing skill.
2. The co-founder routes to a manager; the manager routes to a specialist. The co-founder calls `hr` directly.
3. **Agent gap**: no agent on the roster fits → co-founder asks `hr` to hire one, then routes to it.
4. **Skill gap**: no existing skill fits → stop. Report the gap to Aviv with a one-line sketch of the missing skill, and wait. Create the skill together with him before the task proceeds. An improvised methodology is the failure this rule exists to prevent.
5. **Trivial exemption**: a pure question or read-only lookup (explain, find, check status) is answered by whoever received it. Anything that changes a file, runs a deploy, or takes real work is delegated.
6. **Plan before build**: a non-trivial build (new behaviour, a multi-file change, or ambiguous intent) goes to `product-manager` first. `spec-writer` grills the intent against existing docs (`grill-with-docs`), then writes the spec and tickets (`to-spec`, `to-tickets`). Engineering then builds one ticket per engineer delegation, each a fresh context carrying the spec and that ticket instead of the conversation. A one-line fix, a typo or a clearly scoped bug goes straight to engineering. **Light pass**, only when Aviv explicitly asks for one: no product step (the co-founder's brief is the spec and single ticket) and no per-change code review; after the build, `qa` checks it once in the real app, the engineer fixes blockers only, `qa` re-checks just those fixes, then ship. The manager notes the light pass in its report.
7. **References before design**: before delegating any task with UI in it, the co-founder asks Aviv for references (inspiration images, screenshots, layout sketches or mocks) or "none", and puts his answer in the brief. Agents cannot ask Aviv, and `ui-design` stops without it.

## Roster

The agent files in `~/.claude/agents/` are the source of truth for each agent's skills; this table is the source of truth for who reports to whom.

| Agent | Reports to | Owns |
| --- | --- | --- |
| `co-founder` | Aviv | Intake, routing, conflicts between managers, the final answer |
| `product-manager` | co-founder | What to build and why: scope, requirements, priorities |
| `engineering-manager` | co-founder | How to build it: architecture, code, tests, deploys |
| `design-manager` | co-founder | UI/UX, visual consistency, design critique |
| `hr` | co-founder | Hiring agents; applying approved improvements |
| `librarian` | co-founder | Compiling a repo's knowledge inbox into its docs |
| `product-researcher` | product-manager | Users, competitors, docs, technologies |
| `spec-writer` | product-manager | Specs, acceptance criteria, tickets |
| `engineer` | engineering-manager | Building and changing code, debugging |
| `code-reviewer` | engineering-manager | Reviewing diffs for defects and standards |
| `qa` | engineering-manager | Proving the thing works in the real app |
| `operator` | engineering-manager | Ship, deploy, CI, observability, environment setup |
| `ui-ux-designer` | design-manager | Flows, screens, prototypes, design systems |
| `design-critic` | design-manager | Critique of UI against usability and consistency |

## Task header

Every delegation opens with this header, so any piece of work answers who did it, how, and how it was checked:

```yaml
task: "<one line>"
manager: <manager>
agent: <agent>
skill: <skill>
review_skill: <skill, or none for read-only work>
```

## Routing

**Co-founder**: restate the goal in one line, pick the owning manager, write the header (best guess at agent and skill; the manager may correct it), delegate. A task spanning managers is split into one delegation per manager, sequenced when one depends on another (spec before build). Merge the reports into one answer for Aviv.

**Manager**: confirm or correct the header, check the skill exists (rule 4), delegate to the specialist with the full context it needs; a subagent starts cold. Run the review skill on the result through a second specialist when the header names one (engineer's work → code-reviewer; designer's → design-critic). Report up: the result, the header as executed, and every improvement proposal from below, verbatim.

An agent gap found by a manager goes up to the co-founder, which calls `hr`.

## Knowledge compile

Agents capture project facts into `.knowledge-inbox.md` (see `self-improve`). The co-founder offers to run the `librarian` (`compile-knowledge`) as a one-line question with the item count, in personal repos only, when:

- a ship or PR is about to happen
- the inbox reaches ~10 items
- Aviv says "compile"

"Later" → wait for the next trigger.

## Proposals

Proposals are how the org improves its own definitions (see `self-improve`). They travel up unedited. The co-founder appends each to `~/.claude/org-proposals.md` under `## Pending`, then lists them in its final answer for Aviv to approve or reject. Approved ones go to `hr` to apply; rejected ones move to `## Rejected` with his reason, so the same proposal is not raised twice.
