---
name: compile-knowledge
description: Compile a repo's `.knowledge-inbox.md` into its durable docs (CONTEXT.md, ADRs, CLAUDE.md, docs/). Use when the librarian runs, or Aviv says "compile".
---

# Compile knowledge

Input: `<repo root>/.knowledge-inbox.md`, one fact per line with a source pointer (format in `self-improve`). Personal repos only: `origin` is `github.com/pureclaim/*` or `github.com/syzore/*`.

## Steps

1. **Verify** each line against the current code via its source pointer. Drop it if now false.
2. **Route** each surviving line to exactly one home:

   | Fact | Home | Via |
   | --- | --- | --- |
   | Domain term | `CONTEXT.md` | `domain-modeling` |
   | Hard-to-reverse decision with a real trade-off | `docs/adr/` | `domain-modeling` |
   | Rule every agent must obey | project `CLAUDE.md` (keep under ~150 lines) | `writing-for-agents` |
   | How a subsystem works | `docs/<topic>.md`, plus a one-line pointer in `CLAUDE.md` | `writing-for-agents` |
   | One-off | dropped | — |

3. **Health-check** every touched file and fix on the spot:
   - **stale** (contradicted by code or the new fact) → fix
   - **duplicate** (same meaning in two files) → merge into one
   - **orphan** (nothing points to it) → add a pointer, or delete
4. **Approve**: show Aviv the doc diff. Commit only after he approves, removing the compiled lines from the inbox in the same commit.

Done when every inbox line has a home or is marked a one-off, every touched file passes the health check, and the inbox is empty.

Last, run `cross-tool`'s Project rules row on the repo.
