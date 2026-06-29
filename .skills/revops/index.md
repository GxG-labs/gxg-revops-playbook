# GxG RevOps Orchestrator

Routes RevOps requests to the right production skill, staging workflow, or curator workflow.

This is the user-facing master skill for the playbook. It should answer "which skill should handle this?" and then load that skill's instructions. It does not replace domain skills.

Configuration and coverage targets live in `.skills/config.yaml`.

---

## Routing Table

| Intent | Trigger phrases | Route |
|--------|-----------------|-------|
| Write or improve a business case | "business case", "case study", "success story", "proof of value", "ROI story", "portfolio case" | Read `sales-enablement/writing-business-cases/SKILL.md` |
| Find a skill for a RevOps task | "what skill handles", "do we have a skill for", "find skill", "which workflow" | Check `INDEX.md`, then route to the matching skill |
| Add, import, or improve a skill | "new skill", "import skill", "onboard this skill", "adapt this skill", "причеши скилл" | Read `.skills/revops-curator/index.md` |
| Save incomplete knowledge | "add to staging", "save for later", "база знаний", "сохрани знание" | Read `.skills/revops-curator/staging.md` |
| Audit or update the playbook | "audit", "coverage", "update index", "update README", "taxonomy" | Read `.skills/revops-curator/index.md` |

---

## How to Route

1. Read the user's request and identify the RevOps job-to-be-done.
2. Check the routing table above for an exact route.
3. If no route is obvious, read `INDEX.md` and match by domain, tags, and description.
4. If a production skill exists, read its `SKILL.md` and follow it.
5. If no production skill exists:
   - route maintenance requests to `.skills/revops-curator/index.md`
   - offer to add useful but incomplete knowledge to `_staging/`
   - say clearly that no active production skill exists yet

Do not invent a skill that is not in `INDEX.md` or the domain folders.

---

## Skill Architecture

This repository uses a master-skill pattern adapted from GTM skill libraries:

```text
Shared orchestrator
  .skills/revops/index.md
        |
        v
Production domain skills
  {domain}/{skill-slug}/SKILL.md
        |
        v
Supporting docs/templates/scripts
  {domain}/{skill-slug}/docs/
  {domain}/{skill-slug}/templates/
  {domain}/{skill-slug}/scripts/
```

The orchestrator is LM-agnostic. It uses repo-root-relative paths and plain instructions rather than vendor-specific tool syntax.

---

## Current Active Skills

| Skill | Domain | Use when |
|-------|--------|----------|
| `researching-content` | `demand-gen` | The user needs a research brief for a Russian SEO/AEO/GEO article. |
| `architecting-articles` | `demand-gen` | The user needs a GxG-style article outline. |
| `writing-articles` | `demand-gen` | The user needs a Russian long-form article draft. |
| `optimizing-seo-aeo-geo-content` | `demand-gen` | The user needs SEO/AEO/GEO editing for an article draft. |
| `auditing-content-quality` | `demand-gen` | The user needs a final publication-readiness audit. |
| `writing-business-cases` | `sales-enablement` | The user needs a business case, case study, success story, proof-of-value narrative, or ROI story. |
| `optimizing-linkedin-profile` | `sales-enablement` | The user needs LinkedIn profile positioning or rewrite support. |
| `facilitating-brainstorming` | `sales-enablement` | The user needs a structured brainstorming session. |
| `extracting-design-context` | `design` | The user needs design DNA extracted from screenshots or a URL. |

For the authoritative list, read `INDEX.md`.

---

## Out of Scope

This orchestrator does NOT:
- Execute every RevOps task directly.
- Store production skill content in vendor-specific adapter folders.
- Replace `gxg-revops-curator` for repository maintenance.
- Route to inactive, draft, or imagined skills unless the user explicitly wants to create one.
