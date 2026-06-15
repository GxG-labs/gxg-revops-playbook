# Multi-LLM Skills — Best Practices Guide

A skill that only works in one AI assistant is a liability. This guide covers how to write, structure, and maintain skills that run identically in Claude Code, Codex, Gemini, and any future LLM that can read files and follow instructions.

---

## The Core Problem

Every major LLM has its own "instruction loading" convention:

| Agent | Where it reads instructions | How skills are invoked |
|-------|----------------------------|----------------------|
| Claude Code | `.claude/skills/{name}/SKILL.md` loaded on `/skill-name` | `/skill-name` slash command |
| Codex (OpenAI) | `AGENTS.md` at repo root, loaded at session start | Natural language trigger |
| Gemini CLI | `GEMINI.md` at repo root, loaded at session start | Natural language trigger |
| Custom agents | Any file the agent reads on boot | Depends on implementation |

If skill knowledge lives inside `.claude/skills/`, Codex never sees it. If it lives in `AGENTS.md`, Claude Code won't use it when invoked. The naive solution — copy the text into both files — creates two sources of truth that drift apart.

---

## Principle 1: Single Source of Truth

**All skill knowledge lives in a neutral folder.** LLM-specific entry points are thin adapters that reference the shared folder.

```
repo/
├── CLAUDE.md           ← adapter: tells Claude Code where skills live
├── AGENTS.md           ← adapter: tells Codex/Gemini where skills live
├── GEMINI.md           ← adapter: tells Gemini where skills live (optional)
├── .skills/            ← shared: orchestrators, curator workflows, config
│   ├── config.yaml     ← single config for all skills
│   └── {skill-name}/
│       ├── index.md    ← entry point: routing table + overview
│       ├── *.md        ← sub-workflows, each ≤200 lines
│       ├── templates/
│       └── scripts/
├── {domain}/
│   └── {skill-slug}/
│       └── SKILL.md    ← production domain skill, written LM-agnostically
└── .claude/
    └── skills/
        └── {skill-name}/
            └── SKILL.md  ← adapter: frontmatter + "read .skills/{skill-name}/index.md"
```

**Rule:** If you edit a workflow, you edit `.skills/{skill-name}/*.md`. You never touch the adapter files for content changes.

For production domain skills in this playbook, `{domain}/{skill-slug}/SKILL.md` is also shared source content. It must stay LM-agnostic and must not reference one vendor unless the skill itself is explicitly about that vendor.

---

## Principle 2: LLM-Agnostic Writing

Shared files in `.skills/` must contain zero LLM-specific syntax.

### Do NOT write:
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

### DO write:
```markdown
Read the file `.skills/revops-curator/taxonomy.md`.
Run `python .skills/revops-curator/scripts/audit.py`.
Write the result to `{domain}/{slug}/SKILL.md`.
```

**Rule:** Use imperative plain-English verbs for all file and tool operations. Every LLM maps these to its own tools automatically.

---

## Principle 3: Thin Adapters

An adapter's only jobs are:
1. Register the skill with the LLM's invocation system (frontmatter, keywords)
2. Point to the shared entry file
3. Nothing else

### Claude Code adapter (`.claude/skills/{name}/SKILL.md`):

```markdown
---
name: {skill-name}
description: {trigger description with keywords — Claude Code reads this to decide when to activate}
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Read `.skills/{skill-name}/index.md` for full instructions and workflow routing.
```

That's the entire body. No duplicated content.

### Codex/Gemini adapter (`AGENTS.md` / `GEMINI.md`):

```markdown
## {Skill Name}

When the user asks about {domain}: read `.skills/{skill-name}/index.md` and follow the routing table there.
```

Two to four lines. No duplicated content.

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
| Skill body inside `.claude/skills/` | Codex/Gemini can't see it | Move to `.skills/`, adapter just references it |
| Same content in CLAUDE.md and AGENTS.md | Drifts over time | Single `.skills/` source; adapters reference it |
| Hardcoded numbers in both YAML and instructions | Inconsistency | Config YAML is the single source; instructions reference it |
| Relative paths from adapter location | Break when structure changes | Use repo-root-relative paths in shared content |
| LLM-specific tool syntax in shared files | Other LLMs ignore/misread | Plain English imperatives only |
| Monolithic `index.md` >300 lines | Hard to navigate, slow to load | Split into named sub-files, route from index |
| Trigger phrases only in adapter | Works in Claude Code, silent in Codex | Also put trigger phrases in `index.md` routing table |

---

## Checklist: New Multi-LLM Skill

Before marking a skill active, verify:

- [ ] Knowledge is in `.skills/{name}/`, not inside `.claude/` or `AGENTS.md`
- [ ] `.claude/skills/{name}/SKILL.md` has only frontmatter + one-line reference to `.skills/`
- [ ] `AGENTS.md` has a 2–4 line entry pointing to `.skills/{name}/index.md`
- [ ] `index.md` has a routing table and stays under 150 lines
- [ ] All paths in `.skills/` files are repo-root-relative
- [ ] No LLM-specific syntax in `.skills/` files
- [ ] All configurable thresholds are in `.skills/config.yaml`
- [ ] Trigger phrases appear in both adapter description and `index.md` routing table
- [ ] All state changes write to files (nothing kept only in session memory)
- [ ] Tested by reading the skill from a different LLM's entry point (or simulated)
