---
name: gxg-revops-curator
description: Curates and maintains the GxG RevOps Playbook skill collection. Audits existing skills for quality and coverage, scaffolds new skills with correct taxonomy, improves descriptions and structure, manages the full skill lifecycle (draft → active → deprecated), operates the staging knowledge base for half-formed domain knowledge, and generates gap reports across the RevOps stack. Use when adding a new RevOps skill, auditing the playbook, improving skill quality, checking coverage gaps, updating the index, saving domain knowledge to staging, promoting a staging note to a skill, or when user mentions "playbook", "curator", "audit skills", "new skill", "revops skill", "gap analysis", "skill lifecycle", "taxonomy", "staging", "база знаний", "сохрани знание", "promote to skill", "readme", "напиши readme", "обнови readme".
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# GxG RevOps Playbook — Curator

Read `.skills/revops-curator/index.md` for full instructions and the workflow routing table.

Sub-files for specific workflows (all in `.skills/revops-curator/`):
- `lifecycle.md` — create, audit, improve, deprecate
- `staging.md` — add, scan, refine, promote, park
- `taxonomy.md` — domains, tags, naming rules
- `readme-workflows.md` — README creation and updates

Configuration (domain targets, thresholds): `.skills/config.yaml`
