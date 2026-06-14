# GxG RevOps Playbook — Taxonomy

Canonical reference for domains, slugs, tags, naming rules, and coverage targets.
Every skill in the playbook must conform to this taxonomy.
Coverage targets are also in `.skills/config.yaml` — that file is the machine-readable source of truth.

---

## Domains

Ten primary domains cover the full RevOps stack. Each maps to a top-level folder.

| Folder | Domain | Scope |
|--------|--------|-------|
| `pipeline/` | Pipeline & Forecasting | Stage management, deal hygiene, forecast models, pipeline reviews, commit/upside logic |
| `demand-gen/` | Demand Generation | Inbound/outbound strategy, ICP definition, lead scoring, MQL/SQL criteria, ABM |
| `sales-enablement/` | Sales Enablement | Playbooks, call frameworks, battle cards, objection handling, win/loss analysis |
| `crm-ops/` | CRM & Data Ops | Salesforce/HubSpot admin, data quality, field governance, workflow automation, deduplication |
| `rev-analytics/` | Revenue Analytics | KPI definitions, attribution models, dashboards, cohort analysis, revenue reporting |
| `cs-ops/` | Customer Success Ops | Health scoring, QBR frameworks, expansion playbooks, churn analysis, renewal process |
| `rev-tech/` | Revenue Tech Stack | Tool evaluation, integration design, vendor management, RevOps tooling decisions |
| `pricing-packaging/` | Pricing & Packaging | CPQ setup, pricing tiers, discount governance, deal desk process, packaging decisions |
| `territory-quota/` | Territory & Quota | Territory design, quota setting, ramp plans, performance management, comp plans |
| `mktg-ops/` | Marketing Operations | Campaign operations, marketing automation, lead routing, attribution, MOps stack |

---

## Domain README Structure

Each `{domain}/README.md` must contain:
1. **Domain overview** — what it covers, what it doesn't (1–2 paragraphs)
2. **Coverage map** — table of all skills in this domain with status
3. **Key metrics** — the 3–5 most important metrics for this domain
4. **Stack references** — relevant tools in GxG's tech stack for this domain
5. **Coverage targets** — how many skills are needed (see below)

---

## Coverage Targets

| Domain | Min Active Skills | Priority Skills (build first) |
|--------|-----------------|-------------------------------|
| `pipeline` | 6 | forecasting-pipeline, reviewing-pipeline, defining-stages |
| `demand-gen` | 5 | scoring-leads, defining-icp, qualifying-mqls |
| `sales-enablement` | 7 | building-battlecards, handling-objections, running-discovery |
| `crm-ops` | 6 | auditing-crm-data, managing-duplicates, designing-workflows |
| `rev-analytics` | 5 | defining-metrics, building-dashboards, modeling-attribution |
| `cs-ops` | 5 | scoring-health, running-qbrs, analyzing-churn |
| `rev-tech` | 4 | evaluating-tools, mapping-integrations |
| `pricing-packaging` | 4 | governing-discounts, designing-tiers |
| `territory-quota` | 4 | designing-territories, setting-quotas |
| `mktg-ops` | 5 | routing-leads, running-campaigns, attributing-revenue |

Total target: **51 active skills** covering the full RevOps stack.

---

## Naming Conventions

### Skill Slug (folder name)

Pattern: `{verb}-{object}` in kebab-case

- Use **gerund** (verb+-ing) as the verb: `scoring`, `forecasting`, `building`, `reviewing`
- Object is the RevOps noun: `leads`, `pipeline`, `churn`, `quota`, `dashboards`
- Always lowercase, hyphens only — no underscores, no spaces
- Maximum 48 characters
- Examples:
  - ✅ `scoring-leads`
  - ✅ `forecasting-pipeline`
  - ✅ `building-battlecards`
  - ✅ `auditing-crm-data`
  - ❌ `LeadScoring` (PascalCase)
  - ❌ `lead_scoring` (underscores)
  - ❌ `score` (no object)

### Skill Name (frontmatter `name:`)

Same as the slug. Must be identical to the folder name.

### File names inside skill folders

| File | Purpose |
|------|---------|
| `SKILL.md` | Entry point — always uppercase |
| `docs/` | Reference documentation (e.g. `docs/salesforce-fields.md`) |
| `templates/` | Reusable output templates |
| `scripts/` | Python/bash scripts the agent can execute |

---

## Tags

Tags are declared in frontmatter as `tags: [tag1, tag2]`. Every skill must have at least one domain tag and one type tag.

### Domain Tags (use the folder name)

`pipeline`, `demand-gen`, `sales-enablement`, `crm-ops`, `rev-analytics`, `cs-ops`, `rev-tech`, `pricing-packaging`, `territory-quota`, `mktg-ops`

### Type Tags

| Tag | Meaning |
|-----|---------|
| `#framework` | Decision frameworks, scoring models, evaluation criteria |
| `#process` | Step-by-step operational processes |
| `#template` | Reusable doc/spreadsheet/deck templates |
| `#metric` | KPI definitions, measurement methodology |
| `#automation` | Anything involving workflow automation or scripting |
| `#integration` | Cross-system data flows, API connections |
| `#analysis` | Analytical approaches, data interpretation |
| `#playbook` | End-to-end motion (combines process + content) |
| `#onboarding` | Rep ramp, customer onboarding, tool onboarding |
| `#reporting` | Reports, dashboards, stakeholder updates |

### Stack Tags (optional — tag if skill is tool-specific)

`salesforce`, `hubspot`, `gong`, `outreach`, `salesloft`, `apollo`, `marketo`, `pardot`, `clari`, `looker`, `tableau`, `gainsight`, `churnzero`, `ironclad`, `docusign`

### Priority Tags

| Tag | Meaning |
|-----|---------|
| `#p0` | Critical — foundational skill, needed before others can run |
| `#p1` | High priority — covers a frequent RevOps use case |
| `#p2` | Normal — solid addition, not urgent |

---

## Frontmatter Template

Every SKILL.md must include:

```yaml
---
name: {skill-slug}
description: {optimized description with USE WHEN}
status: draft | active | deprecated
domain: {folder-name}
tags: [{domain-tag}, {type-tag}, {optional-stack-tag}, {priority-tag}]
version: 1.0.0
updated: YYYY-MM-DD
author: GxG
---
```

---

## Skill Types (two categories)

### Capability Uplift Skills
Give the agent the ability to do something it couldn't do alone — tool-specific workflows, proprietary processes, custom integrations.
Examples: `auditing-crm-data` (Salesforce-specific), `forecasting-pipeline` (Clari-specific)

### Encoded Preference Skills
Capture GxG's specific way of doing something the agent already knows — our scoring model, our stage definitions, our qualification criteria.
Examples: `scoring-leads` (GxG's ICP scoring matrix), `defining-icp` (GxG's ICP criteria)

Both types are valid. Label which type in the skill's frontmatter with `type: capability-uplift | encoded-preference`.

---

## Cross-Domain Skills

Some skills span multiple domains. Use the **primary** domain as the folder, add secondary domain tags.

Example: `rev-analytics/attributing-revenue/SKILL.md`
```yaml
domain: rev-analytics
tags: [rev-analytics, mktg-ops, #metric, #analysis, #p1]
```

---

## Coverage Map (track in INDEX.md)

Coverage percentage formula:
```
coverage% = (active skills / coverage target) × 100
```

Target: ≥80% coverage per domain before the playbook is considered "production-ready".
Full stack coverage requires all domains at ≥80%.
