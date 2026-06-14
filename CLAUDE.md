# GxG RevOps Playbook — Claude Code Instructions

This is the GxG RevOps Playbook — a collection of AI agent skills covering the full Revenue Operations stack.

## Shared Skill Content

All skill knowledge lives in **`.skills/`** — this is the single source of truth, readable by any LLM.

| Path | What it contains |
|------|-----------------|
| `.skills/config.yaml` | Domain targets, thresholds, all configurable settings |
| `.skills/revops-curator/` | Curator skill content (routing, lifecycle, taxonomy, staging) |
| `.skills/MULTI_LLM_SKILLS_GUIDE.md` | How to write skills that work across Claude, Codex, Gemini |

## Available Claude Code Skills

### gxg-revops-curator
Registered at `.claude/skills/gxg-revops-curator/SKILL.md`.
Invoke with `/gxg-revops-curator` or by describing a playbook management task.

The SKILL.md is a thin adapter — when invoked, it loads the full instructions from `.skills/revops-curator/index.md`.

Full curator content:
- `.skills/revops-curator/index.md` — routing table, quality gates, overview
- `.skills/revops-curator/lifecycle.md` — create, audit, improve, deprecate workflows
- `.skills/revops-curator/staging.md` — staging area workflows
- `.skills/revops-curator/taxonomy.md` — domains, tags, naming rules
- `.skills/revops-curator/readme-workflows.md` — README creation and update
- `.skills/revops-curator/scripts/audit.py` — programmatic audit script
- `.skills/revops-curator/templates/` — skill template, audit report, repo README

## Playbook Root

```
GxG RevOps Playbook/
├── INDEX.md          ← master skill registry
├── CONTRIBUTING.md   ← skill authoring standards
├── README.md         ← public-facing repo page
├── _staging/         ← raw knowledge awaiting promotion
├── .skills/          ← shared skill content (this is the SSoT)
├── .claude/skills/   ← Claude Code adapters (thin wrappers)
│
├── pipeline/         ← domain skill folders
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

## For Other LLMs

- **Codex / OpenAI**: see `AGENTS.md`
- **Gemini**: see `AGENTS.md` (or create `GEMINI.md` following the same pattern)
- **Architecture guide**: `.skills/MULTI_LLM_SKILLS_GUIDE.md`
