---
name: gxg-revops-curator
description: Curates and maintains the GxG RevOps Playbook skill collection. Audits existing skills for quality and coverage, scaffolds new skills with correct taxonomy, improves descriptions and structure, manages the full skill lifecycle (draft → active → deprecated), operates the staging knowledge base for half-formed domain knowledge, and generates gap reports across the RevOps stack. Use when adding a new RevOps skill, auditing the playbook, improving skill quality, checking coverage gaps, updating the index, saving domain knowledge to staging, promoting a staging note to a skill, or when user mentions "playbook", "curator", "audit skills", "new skill", "revops skill", "gap analysis", "skill lifecycle", "taxonomy", "staging", "база знаний", "сохрани знание", "promote to skill".
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# GxG RevOps Playbook — Curator

Manages the **entire lifecycle** of the GxG RevOps Playbook: raw knowledge → staging → skill → active → deprecated. Enforces taxonomy, maintains the master index, and ensures every skill meets quality standards before it goes live.

## Workflow Routing

| Intent | Trigger phrases | Reference |
|--------|----------------|-----------|
| **Audit** the playbook | "audit", "health check", "quality score", "review all" | [lifecycle.md](lifecycle.md) §Audit |
| **Create** a new skill | "new skill", "add skill", "scaffold", "write a skill for" | [lifecycle.md](lifecycle.md) §Create |
| **Improve** an existing skill | "improve", "fix description", "optimize trigger", "strengthen" | [lifecycle.md](lifecycle.md) §Improve |
| **Gap analysis** | "gaps", "missing", "what's not covered", "coverage" | [taxonomy.md](taxonomy.md) §Coverage |
| **Update index** | "update index", "refresh registry", "rebuild index" | §Index Management below |
| **Deprecate** a skill | "retire", "deprecate", "archive", "sunset" | [lifecycle.md](lifecycle.md) §Deprecate |
| **Taxonomy questions** | "categories", "tags", "naming", "where does X go" | [taxonomy.md](taxonomy.md) |
| **Add to staging** | "add to staging", "сохрани знание", "save for later" | [staging.md](staging.md) §Add |
| **Scan staging** | "scan staging", "что в staging", "staging status" | [staging.md](staging.md) §Scan |
| **Refine staging note** | "refine {note}", "help structure {note}" | [staging.md](staging.md) §Refine |
| **Promote to skill** | "promote {note}", "make skill from {note}" | [staging.md](staging.md) §Promote |

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
├── _staging/                   ← Knowledge staging area
│   ├── README.md
│   ├── _template.md
│   └── {note-slug}.md          ← Staging notes
├── .claude/skills/
│   └── gxg-revops-curator/
│       ├── SKILL.md            ← This file
│       ├── taxonomy.md
│       ├── lifecycle.md
│       ├── staging.md          ← Staging workflows
│       └── templates/
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

Rebuild INDEX.md on every create / improve / deprecate.

Row format:
```
| [skill-name](domain/slug/SKILL.md) | Domain | Status | Tags | Description ≤120 chars |
```

One `##` section per domain + Coverage Summary table at top.

---

## Staging Health (quick check)

| Signal | Action |
|--------|--------|
| `ready` note > 30 days old | Offer to promote |
| `parked` note > 90 days | Offer to delete or reconsider |
| >5 `ready` notes | Alert: backlog building up |
| >20 notes total | Alert: staging inbox overflowing |

---

## Out of Scope

This skill does NOT:
- Execute the skills it curates
- Replace domain expertise — enforces structure, not content accuracy
- Manage MCP connectors or plugin configs
- Handle file formats outside Markdown
