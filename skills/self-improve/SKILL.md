---
name: self-improve
description: Start-of-task memory read and end-of-task lesson check for every agent in the org. Use at the start and end of every delegated task.
---

# Self-improve

Your memory file is `~/.claude/agent-memory/<your-agent-name>/MEMORY.md`.

## Start of task

Read your memory file if it exists. Its lessons bind you like your own instructions.

## End of task

Before reporting, ask: what went wrong, what was slow, which assumption failed, what did the skill or my instructions miss, what capability did I lack? Sort each real **lesson** (one-offs are not lessons):

- **About how you work, in general** → append one dated line to your memory file. Merge with an existing line instead of adding a near-duplicate; keep the file under 100 lines by folding old lines together.
- **Should change a definition** (a `SKILL.md`, an agent file, the `org` roster) → a proposal. You never edit definitions yourself. Add to your report:

  ```
  ## Improvement proposals
  Target: <path>
  Problem: <what the definition gets wrong>
  Evidence: <what happened in this task>
  Change: <the exact edit>
  ```

- **About one project** (a repo's convention, a gotcha in its build) → it belongs in that project's `CLAUDE.md` or docs, not your memory. Mention it in your report.

End the report with `Lessons: none` when nothing qualified.
