# Multi-LLM Skills - Best Practices Guide

A skill that only works in one AI assistant is a liability. This guide explains how to keep GxG skills readable by Claude, Codex, Gemini, and any future LLM that can read files and follow instructions.

---

## Core Principle

The repository stores only shared skill knowledge and production workflows. Assistant-specific entrypoints are local convenience files, not source-of-truth documentation.

If a local assistant needs an adapter (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/skills/`, `.agents/skills/`), that adapter should point back to shared files in this repository. The adapter itself should stay local and is ignored by Git.

---

## Principle 1: Single Source of Truth

**All skill knowledge lives in neutral folders.**

```
repo/
├── .skills/            ← shared: orchestrators, curator workflows, config
│   ├── config.yaml     ← single config for all skills
│   └── revops-curator/
│       ├── index.md    ← entry point: routing table + overview
│       ├── *.md        ← sub-workflows, each ≤200 lines
│       ├── templates/
│       └── scripts/
├── {domain}/
│   └── {skill-slug}/
│       └── SKILL.md    ← production domain skill, written LM-agnostically
└── INDEX.md            ← public skill registry
```

**Rule:** If you edit a shared workflow, edit `.skills/**/*.md`. If you edit a production skill, edit `{domain}/{skill-slug}/SKILL.md`.

For production domain skills in this playbook, `{domain}/{skill-slug}/SKILL.md` is also shared source content. It must stay LM-agnostic and must not reference one vendor unless the skill itself is explicitly about that vendor.

---

## Principle 2: LLM-Agnostic Writing

Shared files in `.skills/` must contain zero LLM-specific syntax.

### Do not write:
```markdown
<!-- Claude-specific -->
<claude:read file=".skills/config.yaml" />
Use your Read tool to load taxonomy.md.
Call the Bash tool to run audit.py.

<!-- Codex-specific -->
Use the code_interpreter to run audit.py.

<!-- Gemini-specific -->
Use gemini.read_file("taxonomy.md").
```

### Write:
```markdown
Read the file `.skills/revops-curator/taxonomy.md`.
Run `python .skills/revops-curator/scripts/audit.py`.
Write the result to `{domain}/{slug}/SKILL.md`.
```

**Rule:** Use imperative plain-English verbs for all file and tool operations. Every LLM maps these to its own tools automatically.

---

## Principle 3: Local Adapters Are Optional

Assistant adapters are useful on a local machine, but they are not required for the public repository.

An adapter's only jobs are:
1. Register the skill with the LLM's invocation system (frontmatter, keywords)
2. Point to the shared entry file
3. Nothing else

Example local Claude Code adapter:

```markdown
---
name: {skill-name}
description: {trigger description with keywords — Claude Code reads this to decide when to activate}
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Read `.skills/{skill-name}/index.md` for full instructions and workflow routing.
```

Example local root instruction:

```markdown
## {Skill Name}

When the user asks about {domain}: read `.skills/{skill-name}/index.md` and follow the routing table there.
```

Keep local adapters untracked. The repository `.gitignore` excludes `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agents/`, and `.claude/`.

---

## Principle 4: Explicit Absolute-ish Paths

Always write paths relative to the **repo root**, not relative to the calling file. This makes paths unambiguous regardless of where the adapter file lives.

```markdown
✅  Read `.skills/revops-curator/lifecycle.md`
✅  Read `.skills/revops-curator/templates/new-skill.md`
❌  Read `lifecycle.md`               ← ambiguous from adapter locations
❌  Read `../../../lifecycle.md`      ← fragile, breaks on restructure
```

The one exception: files within `.skills/{name}/` referencing **siblings** may use relative paths, since they never move independently.

---

## Principle 5: Config in YAML, Not Hardcoded

Every number, threshold, or constant that appears in both the LLM instructions and a script must live in a single YAML file.

```yaml
# .skills/config.yaml
settings:
  stale_threshold_days: 90
  max_skill_lines: 500
```

- LLM reads: "The stale threshold is in `.skills/config.yaml` under `settings.stale_threshold_days`."
- Scripts read: `yaml.safe_load(open(".skills/config.yaml"))`

**Rule:** Never hardcode a threshold that also appears in instructions. If the number changes, it changes in one place.

---

## Principle 6: Skill Entry Point Structure (`index.md`)

Every skill's `index.md` follows this structure:

```markdown
# {Skill Name}

{One sentence: what this skill does.}

## Routing Table

| Intent | Trigger phrases | Read next |
|--------|----------------|-----------|
| Audit  | "audit", "health check" | [lifecycle.md](lifecycle.md) §Audit |
| Create | "new skill", "scaffold" | [lifecycle.md](lifecycle.md) §Create |

## Quick Context

{Key facts the LLM needs before reading sub-files.}
{Point to config.yaml for configurable values.}

## Out of Scope

{What this skill explicitly does NOT do.}
```

Keep `index.md` under 150 lines. All detailed workflows go in named sub-files.

---

## Principle 7: Trigger Phrase Coverage

Trigger phrases must appear in **both** the adapter AND the `index.md` routing table. The adapter activates the skill; the routing table routes it.

- **Adapter**: covers activation triggers ("how does Claude/Codex know to use this skill?")
- **Routing table**: covers sub-workflow triggers ("once activated, what does the user want?")
- Include multilingual triggers if the team uses multiple languages

```markdown
# In adapter description (Claude):
Use when user mentions "audit", "new skill", "gap analysis", "аудит скиллов", "новый скилл"

# In index.md routing table:
| Audit | "audit", "health check", "аудит" | lifecycle.md §Audit |
```

---

## Principle 8: File-Based State Only

Skills must not rely on LLM session memory for state. All persistent state lives in files:
- Skill metadata → YAML frontmatter in each `SKILL.md`
- Staging notes → `_staging/{slug}.md`
- Index → `INDEX.md`
- Audit results → write to a file, don't assume the LLM remembers them

This ensures that running the same skill in Claude vs. Codex vs. Gemini produces the same observable file changes.

---

## Principle 9: Version the Shared Content, Not the Adapters

Adapters almost never change (only when the skill's trigger phrases change). Version the `index.md` and sub-files in the skill's frontmatter. The adapter's job is fixed.

```yaml
# index.md frontmatter (for tracking)
version: 1.2.0
updated: 2026-06-13
```

---

## Anti-Patterns

| Anti-pattern | Why it breaks | Fix |
|--------------|--------------|-----|
| Skill body inside a local adapter | Other agents cannot see it | Move the body to `.skills/` or `{domain}/{slug}/SKILL.md` |
| Same content copied into multiple adapters | Drifts over time | Keep one shared source; adapters only reference it |
| Hardcoded numbers in both YAML and instructions | Inconsistency | Config YAML is the single source; instructions reference it |
| Relative paths from adapter location | Break when structure changes | Use repo-root-relative paths in shared content |
| LLM-specific tool syntax in shared files | Other LLMs ignore or misread it | Plain English imperatives only |
| Monolithic `index.md` >300 lines | Hard to navigate, slow to load | Split into named sub-files, route from index |
| Trigger phrases only in a local adapter | Public repo loses discoverability | Put trigger phrases in shared descriptions and routing tables |

---

## Checklist: New Multi-LLM Skill

Before marking a skill active, verify:

- [ ] Knowledge is in `.skills/` or `{domain}/{slug}/SKILL.md`, not inside a local adapter
- [ ] `index.md` has a routing table and stays under 150 lines
- [ ] All paths in `.skills/` files are repo-root-relative
- [ ] No LLM-specific syntax in `.skills/` files
- [ ] All configurable thresholds are in `.skills/config.yaml`
- [ ] Trigger phrases appear in shared descriptions and routing tables
- [ ] All state changes write to files (nothing kept only in session memory)
- [ ] Tested by reading the skill directly from the shared file path
