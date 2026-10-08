---
name: hire
description: Write a new agent into the org, or apply an approved improvement proposal to an agent or skill. Use when the co-founder reports an agent gap or hands over approved proposals.
---

# Hire

## Hiring an agent

1. Define the role in one line: what it owns that no current agent owns. If a current agent could own it with one more skill, propose that change instead of hiring.
2. Pick its manager from the `org` roster.
3. Pick its skills from the existing skill list. A needed skill that does not exist is a skill gap: report it to the co-founder and stop.
4. Write `~/.claude/agents/<name>.md` from the template below, following `writing-for-agents`.
5. Add its row to the roster in the `org` skill.
6. Commit: the agent file in `~/.claude` (syzore/claude-config), the roster in `~/dev/ProfesorStack` (syzore/ProfesorStack). Push both with the `syzore` account.
7. Report the new agent's name and one-line role.

```markdown
---
name: <kebab-name>
description: <What it does, as a trigger.> Called by <manager>.
skills: [self-improve]
---

Start by running the `self-improve` skill.

You are the <role> in Aviv's org. You report to <manager>.

## Mission
<one or two lines>

## Skills
- `<skill>` — <when>

## Hand back
<what goes outside this role, and to whom>

## Known failure modes
<empty until a proposal adds one>
```

The same files load in Cursor, which reads only `name`, `description`, `model`, `readonly` and `is_background`. It ignores `skills:`, `tools` and `disallowedTools`. So:

- The body's first line runs every skill listed in `skills:`, in that order. Keep `skills:` too, for Claude Code. A manager also preloads `org`: `skills: [org, self-improve]`.
- A review-only role gets `disallowedTools: Edit, Write, NotebookEdit` and `readonly: true`.
- A role kept from editing by `tools:` that must still delegate (managers) gets the body line "In Cursor your edit tools are not removed; delegate every file change anyway." and no `readonly`.

## Applying an approved proposal

1. Resolve the target's real path: `realpath <target>`. Skills are symlinks into their source repo.
2. Edit it there:
   - `~/dev/ProfesorStack/...` or `~/.claude/...` → edit, commit and push in that repo.
   - `~/.agents/skills/...` is vendored from `mattpocock/skills` and an update overwrites it. Put the lesson in the agent file that uses the skill (`Known failure modes`) instead.
3. Move the proposal from `## Pending` to `## Applied` in `~/.claude/org-proposals.md`, with the commit hash, in the same `~/.claude` commit.

Last, after a hire or an applied proposal, run `cross-tool` on every agent file and skill you changed.
