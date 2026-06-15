# GxG RevOps Playbook - Project Structure

This repository is an LM-agnostic skill library for Revenue Operations.

The core rule is:

> Separate shared skill logic, vendor adapters, production domain skills, staging knowledge, and registry documentation.

## Source Of Truth

| Area | Purpose |
|------|---------|
| `.skills/` | Shared LM-agnostic operating layer. Curator workflows, orchestrators, config, templates, scripts, and architecture guides live here. |
| `{domain}/{skill-slug}/SKILL.md` | Production domain skill entry points. These are written in plain instructions and should work for Claude, Codex, Gemini, or any LLM that can read files. |
| `.claude/skills/` | Claude Code adapters only. These register slash-command skills and point back to `.skills/` or production domain skills. |
| `.agents/skills/` | Agent/Codex-style adapters only. These mirror activation metadata and point back to shared instructions. |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Thin root adapters for different assistants. They explain what to read, not the full skill behavior. |

## Top-Level Structure

```text
GxG RevOps Playbook/
  README.md
  PROJECT.md
  PROJECT_STRUCTURE.md
  INDEX.md
  CONTRIBUTING.md
  AGENTS.md
  CLAUDE.md
  GEMINI.md

  .skills/
    MULTI_LLM_SKILLS_GUIDE.md
    config.yaml
    revops/
      index.md
    revops-curator/
      index.md
      lifecycle.md
      onboarding.md
      staging.md
      taxonomy.md
      readme-workflows.md
      scripts/
      templates/

  .claude/skills/
    gxg-revops/
    gxg-revops-curator/

  .agents/skills/
    gxg-revops/
    gxg-revops-curator/

  _staging/
    README.md
    _template.md
    {note-slug}.md

  pipeline/
  demand-gen/
  sales-enablement/
  crm-ops/
  rev-analytics/
  cs-ops/
  rev-tech/
  pricing-packaging/
  territory-quota/
  mktg-ops/
```

## Orchestrators And Sub-Skills

This repo uses two orchestrators:

| Orchestrator | Audience | Shared source |
|--------------|----------|---------------|
| `gxg-revops` | Users running RevOps work | `.skills/revops/index.md` |
| `gxg-revops-curator` | Maintainers adding, importing, auditing, or improving skills | `.skills/revops-curator/index.md` |

Domain skills are the sub-skills. They live in the domain folders and are registered in `INDEX.md`.

## File Placement Rules

- Put active production skills in `{domain}/{skill-slug}/SKILL.md`.
- Put incomplete source knowledge in `_staging/{slug}.md`.
- Put reusable supporting material inside the skill folder: `docs/`, `templates/`, or `scripts/`.
- Put shared curator/orchestrator logic in `.skills/`.
- Keep vendor-specific folders as adapters only.
- Create folders lazily. Do not add empty domain or support folders unless a real file needs them.

## What A New LLM Should Do First

1. Read `README.md`.
2. Read `PROJECT.md` for the charter and collection criteria.
3. Read this file.
4. Read `.skills/MULTI_LLM_SKILLS_GUIDE.md`.
5. For user RevOps work, read `.skills/revops/index.md`.
6. For repository maintenance, read `.skills/revops-curator/index.md`.
