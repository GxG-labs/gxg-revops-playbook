![Skills](https://img.shields.io/badge/skills-9%20active-brightgreen)
![Domains](https://img.shields.io/badge/domains-3%20active-blue)
![Updated](https://img.shields.io/badge/updated-June%202026-lightgrey)

# GxG RevOps Playbook

**An LM-agnostic skill library covering the full Revenue Operations stack.**

Each skill is a ready-to-run workflow: invoke it, get the result.
Not instructions on how to think about RevOps — but how to execute right now.

---

## Why

- **Speed** — standard RevOps tasks solved in a single skill call, no prompt engineering required
- **Consistent standard** — everyone on the team works from the same GxG approach
- **Living knowledge base** — staging area for domain knowledge that hasn't become a skill yet
- **Evolving** — starting with sales-enablement, expanding to cover the full RevOps stack

---

## Quick Start

**1.** Start with the user-facing orchestrator:
```
gxg-revops
```

It routes RevOps requests to the right production skill.

**2.** Or call an active skill directly:
```
/writing-business-cases
/optimizing-linkedin-profile
/facilitating-brainstorming
/researching-content
/architecting-articles
/writing-articles
/optimizing-seo-aeo-geo-content
/auditing-content-quality
```

**3.** Use the curator only for maintaining the library:
```
/gxg-revops-curator — I need a skill for churn analysis, what's in the playbook?
```

---

## What's Inside

| Domain | Skills | Description |
|--------|--------|-------------|
| [demand-gen](./demand-gen/) | 5/5 | Content-led demand generation, Russian SEO/AEO/GEO article workflows, research, writing, optimization, and audit |
| [sales-enablement](./sales-enablement/) | 3/7 | Playbooks, battle cards, objection handling, brainstorming, LinkedIn optimization |
| [design](./design/) | 1/5 | Design DNA extraction from screenshots/URLs — tokens, style, visual effects |

---

## What Belongs Here

Add a workflow when it helps an agent perform a recurring RevOps task better than a generic answer.

Good candidates:

- produce a concrete artifact, decision, analysis, recommendation, or operating plan
- encode a repeatable process, not a one-time answer
- include enough context, examples, rules, or templates for an agent to execute without guessing
- reduce repeated explanation between a human and an agent
- improve consistency across similar tasks

Do not add material that is only generic advice, a prompt with no reusable process, copied vendor documentation, a one-off note, private customer data, or an idea with no clear user, input, and output.

If the idea is useful but unfinished, put it in `_staging/`. Do not call it a production skill.

Before adding anything, answer:

1. What recurring RevOps task does this improve?
2. Who will use the output?
3. What input does the agent need?
4. What output should the agent produce?
5. What rules or examples make this better than a generic response?
6. Will this be useful again after the current conversation ends?

---

## Repo Structure

```
GxG RevOps Playbook/
├── README.md               ← you are here
├── INDEX.md                ← full registry of all skills
├── CONTRIBUTING.md         ← how to add or improve a skill
├── _staging/               ← raw knowledge → future skills
├── .skills/                ← shared LM-agnostic orchestrators and curator workflows
├── .claude/skills/
│   ├── gxg-revops/         ← thin Claude adapter for the user-facing orchestrator
│   └── gxg-revops-curator/ ← thin Claude adapter for maintaining this repo
├── .agents/skills/
│   ├── gxg-revops/         ← thin agent adapter for the user-facing orchestrator
│   └── gxg-revops-curator/ ← thin agent adapter for maintaining this repo
├── demand-gen/             ← content-led demand generation skills
├── design/                 ← design-context skills
└── sales-enablement/       ← active domain with production skills
```

Source of truth:

- `.skills/` contains shared LM-agnostic orchestrator and curator logic.
- `{domain}/{skill-slug}/SKILL.md` contains production skill entry points.
- `.claude/skills/` and `.agents/skills/` are adapter folders only.
- `INDEX.md` is the master registry of active and deprecated skills.
- `.skills/config.yaml` and `.skills/revops-curator/taxonomy.md` define domains, coverage targets, tags, and quality gates.

---

## Adding a Skill or Knowledge

**Quick — add to staging** (2 minutes):
```
/gxg-revops-curator — add to staging: [describe what you know]
```

**Full skill** — see [CONTRIBUTING.md](./CONTRIBUTING.md).

The curator helps with taxonomy, scaffolding, and quality gates:
```
/gxg-revops-curator — I want to write a skill for X
```

To import an external skill from a URL or file and normalize it into this playbook:
```
/gxg-revops-curator — onboard this skill: [URL or file path]
```

---

## LM-Agnostic Architecture

This repo uses a single-source-of-truth pattern:

- Shared orchestrator logic lives in `.skills/revops/index.md`.
- Shared curator logic lives in `.skills/revops-curator/`.
- Production domain skills live in `{domain}/{skill-slug}/SKILL.md`.
- `.claude/skills/` and `.agents/skills/` are adapters. They point to shared instructions and should not duplicate workflow logic.

See `.skills/MULTI_LLM_SKILLS_GUIDE.md` before changing architecture.

---

## Auditing the Collection

```bash
# Full audit: skills + staging
python .skills/revops-curator/scripts/audit.py --root .

# Staging only
python .skills/revops-curator/scripts/audit.py --root . --staging-only

# Specific domain
python .skills/revops-curator/scripts/audit.py --root . --domain pipeline
```

---

*Maintained by `gxg-revops-curator` · Updated June 2026*
