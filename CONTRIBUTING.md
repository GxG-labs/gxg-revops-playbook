# Contributing to the GxG RevOps Playbook

This document defines the standards every skill in the playbook must meet. The `gxg-revops-curator` skill enforces these rules automatically — run it to scaffold, audit, and improve skills.

---

## Before You Start

1. Check `README.md` §What Belongs Here — does this belong in the collection?
2. Check `INDEX.md` — does a skill for this already exist?
3. If yes: improve the existing skill instead of creating a duplicate.
4. If no: proceed below.

---

## Creating a Skill

### Step 1 — Pick a domain

See `taxonomy.md` §Domains. Every skill lives in exactly one domain folder. If unsure, ask the curator: "where does a skill for X go?"

### Step 2 — Generate a slug

Pattern: `{verb-ing}-{object}` — e.g. `scoring-leads`, `forecasting-pipeline`, `building-battlecards`

Rules:
- kebab-case, all lowercase
- gerund verb (ends in -ing)
- ≤48 characters
- No tool names in the slug (use a stack tag instead)

### Step 3 — Scaffold

Copy `.skills/revops-curator/templates/new-skill.md` to `{domain}/{slug}/SKILL.md` and fill in every `{placeholder}`.

### Step 4 — Write a high-quality description

The description is the most important part — it determines whether an LLM activates the skill.

**Formula:**
```
[What it does, third person]. Use when [scenario], [scenario],
or when user mentions "[keyword]", "[keyword]", "[keyword]", "[keyword]", "[keyword]".
```

**Checklist:**
- [ ] No "I", "you", "we" — third person only
- [ ] Contains "Use when" or "USE WHEN"
- [ ] ≥5 quoted trigger keywords
- [ ] ≤1024 characters
- [ ] Passes the "would the right LLM pick this?" test

### Step 5 — Quality gates

All 7 gates must pass before status → `active`:

| Gate | Check |
|------|-------|
| G1 | Name is kebab-case, gerund+noun, ≤64 chars |
| G2 | Description: third-person, USE WHEN, ≥5 keywords, ≤1024 chars |
| G3 | SKILL.md body ≤500 lines |
| G4 | ≥2 concrete examples (input → output format) |
| G5 | "Out of Scope" section present |
| G6 | `domain:` + `tags:` in frontmatter, domain matches folder |
| G7 | All required frontmatter fields present |

Run the audit script to check automatically:
```bash
python .skills/revops-curator/scripts/audit.py --domain {domain}
```

### Step 6 — Set status

- First submission: `status: draft`
- After curator review + all gates pass: `status: active`
- Never self-promote to `active`

### Step 7 — Update INDEX.md

Add a row under the correct domain section. Format:
```
| [skill-name](domain/slug/SKILL.md) | active | #tag1 #tag2 | One-line description ≤120 chars |
```

---

## Improving a Skill

1. Never change another skill's `name` or `domain` without curator review — this breaks references.
2. Bump `version` on every change (patch for content, minor for structure, major for rewrites).
3. Update `updated: YYYY-MM-DD` in frontmatter.
4. Update INDEX.md description if it changed.

---

## Deprecating a Skill

Do not delete skills. Set `status: deprecated`, add the deprecation notice block at the top of SKILL.md, and move the index row to the Deprecated section. See `lifecycle.md` §Deprecate.

---

## Style Guide

| Element | Rule |
|---------|------|
| Voice | Imperative ("Run", "Check", "Define") — not passive |
| Length | SKILL.md ≤500 lines. Route to docs/ for anything longer |
| Headers | `##` for major sections, `###` for subsections — no deeper |
| Tables | Use for routing maps, comparisons, quick references |
| Code blocks | Use for exact commands, templates, output formats |
| Links | Use relative paths within the playbook |
| Emojis | Allowed sparingly in status indicators only (✅ ⚠️ 🔧 🚫) |

---

## What Makes a Great Skill

**Strong:** concrete examples that show real GxG-specific inputs and outputs, tight scope, description that triggers on actual user language, clear "Out of Scope" that prevents mistriggers.

**Weak:** generic instructions an LLM already knows, vague trigger language, no examples, no scope boundaries.

**Reject criteria:**
- Duplicates an existing active skill
- Tool-specific instructions that are just vendor docs (link to vendor docs instead)
- No real GxG context — if it works equally well for any company, it's not a playbook skill

---

## Questions?

Run the curator: `/gxg-revops-curator` and describe what you're trying to do. It will route you to the right workflow.
