![Skills](https://img.shields.io/badge/skills-1%20active-yellow)
![Coverage](https://img.shields.io/badge/coverage-2%25-red)
![Domains](https://img.shields.io/badge/domains-10-blue)
![Updated](https://img.shields.io/badge/updated-June%202026-lightgrey)

# GxG RevOps Playbook

**A collection of Claude skills covering the full Revenue Operations stack.**

Each skill is a ready-to-run workflow: invoke it, get the result.
Not instructions on how to think about RevOps — but how to execute right now.

---

## Why

- ✅ **Speed** — standard RevOps tasks solved in a single skill call, no prompt engineering required
- ✅ **Consistent standard** — everyone on the team works from the same GxG approach
- ✅ **Living knowledge base** — staging area for domain knowledge that hasn't become a skill yet
- ✅ **Full stack** — target: 51 skills across 10 domains from pipeline to CS ops

---

## Quick Start

**1.** Make sure `gxg-revops-curator` is active in your Claude.

**2.** Call any skill directly:
```
/writing-business-cases
/scoring-leads
/forecasting-pipeline
```

**3.** Or ask the curator to find what you need:
```
/gxg-revops-curator — I need a skill for churn analysis, what's in the playbook?
```

---

## What's Inside

| Domain | Skills | Coverage | Description |
|--------|--------|----------|-------------|
| [pipeline](./pipeline/) | 0/6 | 0% | Pipeline management, forecasting, stage hygiene |
| [demand-gen](./demand-gen/) | 0/5 | 0% | ICP, lead scoring, MQL/SQL criteria, ABM |
| [sales-enablement](./sales-enablement/) | 1/7 | 14% | Playbooks, battle cards, objection handling |
| [crm-ops](./crm-ops/) | 0/6 | 0% | Salesforce/HubSpot, data quality, automation |
| [rev-analytics](./rev-analytics/) | 0/5 | 0% | KPIs, attribution, dashboards, ARR/NRR/GRR |
| [cs-ops](./cs-ops/) | 0/5 | 0% | Health scoring, QBRs, retention, expansion |
| [rev-tech](./rev-tech/) | 0/4 | 0% | Tool evaluation, integrations, vendor management |
| [pricing-packaging](./pricing-packaging/) | 0/4 | 0% | CPQ, tiers, deal desk, discount governance |
| [territory-quota](./territory-quota/) | 0/4 | 0% | Territories, quotas, ramp plans, compensation |
| [mktg-ops](./mktg-ops/) | 0/5 | 0% | Campaign ops, automation, lead routing |
| **Total** | **1/51** | **2%** | |

---

## Repo Structure

```
GxG RevOps Playbook/
├── README.md               ← you are here
├── INDEX.md                ← full registry of all skills
├── CONTRIBUTING.md         ← how to add or improve a skill
├── _staging/               ← raw knowledge → future skills
├── .claude/skills/
│   └── gxg-revops-curator/ ← meta-skill for maintaining this repo
├── pipeline/
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

---

## Auditing the Collection

```bash
# Full audit: skills + staging
python .claude/skills/gxg-revops-curator/scripts/audit.py --root .

# Staging only
python .claude/skills/gxg-revops-curator/scripts/audit.py --root . --staging-only

# Specific domain
python .claude/skills/gxg-revops-curator/scripts/audit.py --root . --domain pipeline
```

---

*Maintained by `gxg-revops-curator` · Updated June 2026*
