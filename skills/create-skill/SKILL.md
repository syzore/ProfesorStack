---
name: create-skill
description: Use when creating a new skill — decides where the skill lives and how it gets installed.
---

# Create Skill

Every new skill is created inside the ProfesorStack repo and installed globally.

1. Write it to `~/dev/ProfesorStack/skills/<skill-name>/SKILL.md`
   (repo: https://github.com/syzore/ProfesorStack/tree/main/skills).
2. Install it globally by symlinking it into `~/.claude/skills/`:

   ```bash
   ln -s ~/dev/ProfesorStack/skills/<skill-name> ~/.claude/skills/<skill-name>
   ```

3. Commit and push the new skill from `~/dev/ProfesorStack` (the repo is `syzore`'s,
   so push with that account active).
