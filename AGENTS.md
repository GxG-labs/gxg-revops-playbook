# GxG RevOps Playbook — Agent Instructions

This file provides guidance to Codex, Gemini, and other LLM agents working in this repository.

## What This Repo Is

A collection of AI agent skills covering the full Revenue Operations stack. Skills live in domain folders (`pipeline/`, `demand-gen/`, `sales-enablement/`, etc.) as `SKILL.md` files.

All shared skill infrastructure is in `.skills/`. Configuration is in `.skills/config.yaml`.

---

## RevOps Curator Skill

**When to activate:** user asks about skill curation, playbook audit, adding a skill, gap analysis, staging knowledge, taxonomy questions, or updating the index or README. Trigger phrases include: "audit", "new skill", "scaffold", "gap analysis", "staging", "playbook", "taxonomy", "coverage", "deprecate", "promote to skill", "add to staging", "update index", "update readme", "база знаний", "новый скилл", "аудит скиллов".

**To use this skill:**
1. Read `.skills/revops-curator/index.md` — it contains the routing table that maps user intent to the right sub-workflow
2. Follow the routing table to the appropriate sub-file
3. Read `.skills/config.yaml` for domain targets and configurable thresholds

Sub-files (all in `.skills/revops-curator/`):

| File | Contents |
|------|----------|
| `index.md` | Routing table, quality gates, knowledge flow, overview |
| `lifecycle.md` | Create / Audit / Improve / Deprecate workflows |
| `staging.md` | Add to staging, scan, refine, promote, park |
| `taxonomy.md` | Domains, tags, naming rules, coverage targets |
| `readme-workflows.md` | README creation and update workflows |
| `scripts/audit.py` | Programmatic audit — run with `python .skills/revops-curator/scripts/audit.py --root .` |
| `templates/new-skill.md` | Scaffold template for new skills |
| `templates/audit-report.md` | Audit report template |

---

## Writing-Business-Cases Skill

Located at `sales-enablement/writing-business-cases/SKILL.md`. Activate when user asks to write, structure, or improve a business case document.

---

## General Conventions

- All skill entry points are `SKILL.md` files in `{domain}/{skill-slug}/` folders
- Skill frontmatter always has: `name`, `description`, `status`, `domain`, `tags`, `version`, `updated`, `author`
- Only skills with `status: active` are production-ready
- The master index is `INDEX.md` at the repo root — rebuild it after any create/deprecate
- Staging notes are in `_staging/{slug}.md` — use the curator to manage them

---

## Multi-LLM Architecture

This repo follows the Single Source of Truth pattern for multi-LLM skills. See `.skills/MULTI_LLM_SKILLS_GUIDE.md` for the full guide on how skills are structured to work identically across Claude, Codex, Gemini, and other agents.
