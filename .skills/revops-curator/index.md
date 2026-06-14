# GxG RevOps Playbook — Curator

Manages the **entire lifecycle** of the GxG RevOps Playbook: raw knowledge → staging → skill → active → deprecated. Enforces taxonomy, maintains the master index, and ensures every skill meets quality standards before it goes live.

Configuration (domain targets, thresholds): read `.skills/config.yaml`.

---

## Routing Table

| Intent | Trigger phrases | Where to go |
|--------|----------------|-------------|
| **Audit** the playbook | "audit", "health check", "quality score", "review all", "аудит" | [lifecycle.md](lifecycle.md) §Audit |
| **Create** a new skill | "new skill", "add skill", "scaffold", "write a skill for", "новый скилл", "создай скилл" | [lifecycle.md](lifecycle.md) §Create |
| **Improve** an existing skill | "improve", "fix description", "optimize trigger", "strengthen", "улучши скилл" | [lifecycle.md](lifecycle.md) §Improve |
| **Gap analysis** | "gaps", "missing", "what's not covered", "coverage", "покрытие" | [taxonomy.md](taxonomy.md) §Coverage |
| **Update index** | "update index", "refresh registry", "rebuild index" | §Index Management below |
| **Deprecate** a skill | "retire", "deprecate", "archive", "sunset", "устарел" | [lifecycle.md](lifecycle.md) §Deprecate |
| **Taxonomy questions** | "categories", "tags", "naming", "where does X go", "таксономия" | [taxonomy.md](taxonomy.md) |
| **README** | "напиши readme", "обнови readme", "readme для репо", "readme score" | [readme-workflows.md](readme-workflows.md) |
| **Add to staging** | "add to staging", "сохрани знание", "save for later", "база знаний" | [staging.md](staging.md) §Add |
| **Scan staging** | "scan staging", "что в staging", "staging status" | [staging.md](staging.md) §Scan |
| **Refine staging note** | "refine {note}", "help structure {note}", "доработай заметку" | [staging.md](staging.md) §Refine |
| **Promote to skill** | "promote {note}", "make skill from {note}", "promote to skill" | [staging.md](staging.md) §Promote |

---

## Knowledge Flow

```
Raw knowledge (meeting, doc, conversation)
        ↓
  _staging/{note}.md       ← status: raw → refining → ready
        ↓ promote
  {domain}/{slug}/SKILL.md ← status: draft → active
        ↓ retire
  status: deprecated → archived
```

---

## Playbook Root Structure

```
GxG RevOps Playbook/
├── INDEX.md                    ← Master registry
├── CONTRIBUTING.md             ← Standards for skill authors
├── CLAUDE.md                   ← Claude Code adapter
├── AGENTS.md                   ← Codex / Gemini adapter
├── _staging/                   ← Knowledge staging area
│   ├── README.md
│   ├── _template.md
│   └── {note-slug}.md
├── .skills/                    ← Shared skill content (LLM-agnostic)
│   ├── MULTI_LLM_SKILLS_GUIDE.md
│   ├── config.yaml             ← Single config for all settings
│   └── revops-curator/         ← This skill
│       ├── index.md            ← This file
│       ├── taxonomy.md
│       ├── lifecycle.md
│       ├── staging.md
│       ├── readme-workflows.md
│       └── templates/
├── .claude/skills/
│   └── gxg-revops-curator/
│       └── SKILL.md            ← Thin adapter for Claude Code
│
├── pipeline/                   ← Domain folders (see taxonomy.md)
├── demand-gen/
├── sales-enablement/
├── crm-ops/
├── rev-analytics/
├── cs-ops/
├── rev-tech/
├── pricing-packaging/
├── territory-quota/
└── mktg-ops/
```

---

## Skill Quality Gates

Every skill must pass all 7 before status → `active`:

| Gate | Criterion |
|------|-----------|
| **G1 — Name** | kebab-case, gerund+noun, ≤64 chars |
| **G2 — Description** | third-person, USE WHEN, ≥5 trigger keywords, ≤1024 chars |
| **G3 — Body** | SKILL.md ≤500 lines, routes to docs/ for detail |
| **G4 — Examples** | ≥2 concrete input → output examples |
| **G5 — Boundaries** | "Out of scope" section present |
| **G6 — Taxonomy** | Correct domain folder, `tags:` in frontmatter |
| **G7 — Metadata** | All required frontmatter fields present |

---

## Description Optimizer

```
[Core capability, third person]. [Secondary capabilities].
Use when [scenario 1], [scenario 2], or when user mentions
"[keyword1]", "[keyword2]", "[keyword3]", "[keyword4]", "[keyword5]".
```

Rules: third-person only · lead with differentiator · keywords = how users actually ask.

---

## Index Management

Rebuild `INDEX.md` on every create / improve / deprecate.

Row format:
```
| [skill-name](domain/slug/SKILL.md) | Domain | Status | Tags | Description ≤120 chars |
```

One `##` section per domain + Coverage Summary table at top.

---

## Staging Health (quick check)

Read `.skills/config.yaml` for thresholds (staging_ready_warning_days, etc.).

| Signal | Action |
|--------|--------|
| `ready` note > 30 days old | Offer to promote |
| `parked` note > 90 days | Offer to delete or reconsider |
| >5 `ready` notes | Alert: backlog building up |
| >20 notes total | Alert: staging inbox overflowing |

---

## Proactive Behavior

Check README freshness after every change to the skill collection — without being asked.

| Event | Curator action |
|-------|---------------|
| Skill → `active` | Check README → offer update if stale |
| Skill → `deprecated` | Check README → offer update if stale |
| Staging note promoted to skill | Check README → offer update if stale |
| Full audit run | Always include README freshness in the report |

Propose in one line, as a postscript:

> README is stale (skills: 3 → 4). Update now?

- If yes → run Update README workflow from [readme-workflows.md](readme-workflows.md)
- If "later" / no response → don't repeat in this session
- **Never interrupt the main workflow** for this check

---

## Out of Scope

This skill does NOT:
- Execute the skills it curates
- Replace domain expertise — enforces structure, not content accuracy
- Manage MCP connectors or plugin configs
- Handle file formats outside Markdown
