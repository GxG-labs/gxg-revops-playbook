<!-- 
  TEMPLATE: GxG RevOps Playbook — root README.md
  Fill in {placeholders} with real data before using.
  Run audit.py to get current numbers for badges and coverage.
-->

<!-- BADGES — update whenever a new active skill is added -->
![Skills](https://img.shields.io/badge/skills-{ACTIVE_COUNT}%20active-{COVERAGE_COLOR})
![Domains](https://img.shields.io/badge/domains-{DOMAIN_COUNT}%20active-blue)
![Updated](https://img.shields.io/badge/updated-{MONTH}%20{YEAR}-lightgrey)

# GxG RevOps Playbook

**A minimal, LM-agnostic skill library for Revenue Operations workflows.**

Each skill is a ready-to-run workflow: invoke it, follow the instructions, produce the artifact.

---

## Why

- **Speed** — standard RevOps tasks solved in a single skill call, no prompt engineering required
- **Consistent standard** — everyone on the team works from the same GxG approach
- **Clean lifecycle** — unfinished knowledge stays in `_staging/` until it is ready
- **Full stack** — {ACTIVE_COUNT} skills across {DOMAIN_COUNT} domains from pipeline to CS ops

---

## Quick Start

**1.** Start with the user-facing orchestrator:
```
gxg-revops
```

**2.** Or open an active skill directly:
```
/scoring-leads
/forecasting-pipeline
/auditing-crm-data
```

**3.** Or ask the curator to find what you need:
```
gxg-revops-curator — I need a skill for churn analysis, what's in the playbook?
```

---

## What's Inside

| Domain | Skills | Coverage | Description |
|--------|--------|----------|-------------|
| [pipeline](./pipeline/) | {N}/6 | {%}% | Pipeline management, forecasting, stage hygiene |
| [demand-gen](./demand-gen/) | {N}/5 | {%}% | ICP, lead scoring, MQL/SQL criteria, ABM |
| [sales-enablement](./sales-enablement/) | {N}/7 | {%}% | Playbooks, battle cards, objection handling |
| [crm-ops](./crm-ops/) | {N}/6 | {%}% | Salesforce/HubSpot, data quality, automation |
| [rev-analytics](./rev-analytics/) | {N}/5 | {%}% | KPIs, attribution, dashboards, ARR/NRR/GRR |
| [cs-ops](./cs-ops/) | {N}/5 | {%}% | Health scoring, QBR, retention, expansion |
| [rev-tech](./rev-tech/) | {N}/4 | {%}% | Tool evaluation, integrations, vendor selection |
| [pricing-packaging](./pricing-packaging/) | {N}/4 | {%}% | CPQ, tiers, deal desk, discount governance |
| [territory-quota](./territory-quota/) | {N}/4 | {%}% | Territories, quotas, ramp plans, comp |
| [mktg-ops](./mktg-ops/) | {N}/5 | {%}% | Campaign ops, automation, lead routing |
| **Total** | **{ACTIVE}/{TARGET}** | **{COVERAGE_PCT}%** | |

---

## Repo Structure

```
GxG RevOps Playbook/
├── README.md               ← here
├── INDEX.md                ← full registry of all skills
├── CONTRIBUTING.md         ← how to add/improve a skill
├── _staging/               ← lightweight notes before promotion
│   └── {note}.md
├── .skills/                ← shared LM-agnostic orchestrators and curator workflows
│   ├── config.yaml         ← single config for all settings
│   └── revops-curator/     ← curator meta-skill
│
├── pipeline/               ← {N} skills
├── demand-gen/             ← {N} skills
├── sales-enablement/       ← {N} skills
├── crm-ops/                ← {N} skills
├── rev-analytics/          ← {N} skills
├── cs-ops/                 ← {N} skills
├── rev-tech/               ← {N} skills
├── pricing-packaging/      ← {N} skills
├── territory-quota/        ← {N} skills
└── mktg-ops/               ← {N} skills
```

---

## Add a Skill or Knowledge

**Quick — add to staging** (takes 2 minutes):
```
Use the gxg-revops-curator skill: add to staging: [describe what you know]
```

**Full skill** — see [CONTRIBUTING.md](./CONTRIBUTING.md).

The curator helps with taxonomy, template, and quality gates:
```
Use gxg-revops-curator: I want to write a skill for X
```

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

*Maintained by `gxg-revops-curator` · Updated {MONTH} {YEAR}*
