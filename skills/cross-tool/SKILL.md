---
name: cross-tool
description: Final check after adding or changing anything agent-facing (a skill, an agent file, project rules, global rules), so Claude Code and Cursor both load it and act on it the same way. Use as the last step of `hire`, `create-skill` and `compile-knowledge`.
---

# Cross-tool

Checks only. Creation stays with `hire`, `create-skill`, `compile-knowledge` and `writing-for-agents`.

Find the changed item's row and run every cell. Facts verified from cursor.com/docs, 2026-10-08.

| Item | Claude Code | Cursor |
| --- | --- | --- |
| Skill | Loads `~/.claude/skills`, `.claude/skills`. | Loads `~/.claude/skills`, `.claude/skills` too. Check: correct use never depends only on Claude-only frontmatter such as `disable-model-invocation` (agents read user-only skills directly, per `self-improve`). A cited skill is in one of those dirs; `<plugin>:<name>` and Claude Code built-ins (e.g. `run`) are Claude-only, so the citing line names a Cursor fallback or says `(Claude Code only)`. |
| Agent | Loads `~/.claude/agents`, `.claude/agents`; honours `skills:`, `tools`, `disallowedTools`. | Loads the same dirs; reads only `name`, `description`, `model`, `readonly`, `is_background`. Check: the body's first line runs every skill in `skills:`, in order; review-only roles have `readonly: true`; no rule rests only on a field Cursor ignores. Nesting stops at main → subagent → subagent. |
| Project rules | Reads `CLAUDE.md`. | Reads `AGENTS.md` (root and nested). Check: each `AGENTS.md` is a symlink to its sibling `CLAUDE.md` (`git ls-files -s AGENTS.md` shows mode `120000`); one copy only. No `CLAUDE.md` → report the gap. |
| Global rules | Reads `~/.claude/CLAUDE.md`. | No file. A User Rule (Cursor Settings → Rules) points at `~/.claude/CLAUDE.md` and `~/.claude/agents/co-founder.md`. Check: ask Aviv once per new machine that it still does; agents cannot read Cursor settings. |

A new tool (Codex, Gemini) is one new column.

Done when every cell in the changed item's row passes, or each failure is fixed or reported.
