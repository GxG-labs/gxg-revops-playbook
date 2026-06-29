---
name: researching-content
description: "Builds compact research briefs for Russian SEO/AEO/GEO articles, separating search intent, verified facts, source-backed examples, risky claims, and FAQ opportunities before outlining or drafting. Use when preparing content briefs, researching Russian long-form articles, validating SEO or GEO claims, mapping search intent, or when user mentions \"content research\", \"research brief\", \"SEO article\", \"AEO\", \"GEO\", \"источники\", \"ресерч статьи\", \"факты для статьи\"."
status: active
domain: demand-gen
type: capability-uplift
tags: [demand-gen, #analysis, #process, #playbook, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read, WebSearch
---

# Researching Content

Prepares evidence-based research briefs for Russian long-form content before the article is outlined, written, or optimized.

## When to Use This Skill

Activate when:
- A user wants to prepare a Russian SEO/AEO/GEO article and needs research before writing
- A topic depends on current market context, tools, salary data, legal or financial claims, or 2026 trends
- A draft needs sources, examples, FAQ angles, or risky claims identified before publication
- A content workflow needs a handoff brief for `architecting-articles`, `writing-articles`, or `optimizing-seo-aeo-geo-content`

Do NOT use when: the user already has a verified brief and only needs structure, writing, editing, or final audit.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Research brief** | "research this article" / "собери ресерч" | See §Research Brief |
| **Claim check** | "verify these claims" / "проверь факты" | See §Claim Check |

---

## Instructions

### Research Brief

1. Define the article job:
   - Target reader
   - Reader's decision, confusion, or task
   - Primary query and 5-10 secondary queries
   - Article type: explanation, comparison, checklist, career guide, marketing guide, tool guide, or process guide
2. Search for current information when the topic is time-sensitive, market-specific, legal, financial, salary-related, tool-related, or trend-related.
3. Separate evidence into:
   - Verified facts with source names and URLs
   - Common expert practice
   - Assumptions requiring cautious wording
   - Claims to avoid because they are outdated, unverifiable, or too broad
4. Build an intent map:
   - `what is`
   - `why it matters`
   - `how it works`
   - `how to do it`
   - `mistakes`
   - `tools`
   - `metrics`
   - `FAQ`
5. Capture concrete examples, numbers, product context, and search-language variants.
6. Return the brief in Russian unless the user requests another language.

### Claim Check

1. Extract each factual, numerical, comparative, legal, financial, salary, or trend claim.
2. Label every claim as `supported`, `needs source`, `soften wording`, or `avoid`.
3. For unstable facts, verify against current or primary sources.
4. Suggest safe wording for claims that are plausible but not proven.

---

## Output Format

```markdown
# Research Brief

## Working Title

## Reader And Job-To-Be-Done

## Search Intent Map

## Facts To Use

## Examples And Scenarios

## SEO/AEO/GEO Opportunities

## Risky Claims And Safe Wording

## Suggested FAQ

## Sources
```

---

## Examples

### Example 1: GEO vs SEO Article

**Input / Context:**
The user asks for a research brief for a Russian article: "GEO vs SEO для B2B SaaS в 2026 году", audience: founders and marketers.

**Output:**
A Russian research brief with reader job-to-be-done, primary and secondary queries, verified definitions for SEO/AEO/GEO, current source list, comparison angles, FAQ candidates, and warnings against unsupported ranking or traffic claims.

---

### Example 2: Risky Salary Claims

**Input / Context:**
The user has a draft claiming that "retention marketers earn 30% more in 2026" without a source.

**Output:**
An audit of the claim as `needs source`, recommended source types to check, and safer wording such as "в вакансиях retention-маркетинг часто описывают как роль на стыке CRM, аналитики и продукта" if no reliable salary benchmark is found.

---

## Reference

- SEO/AEO/GEO research principles: [docs/seo-aeo-geo.md](docs/seo-aeo-geo.md)

---

## Out of Scope

This skill does NOT:
- Write the article draft
- Build the final article outline
- Invent statistics, rankings, salaries, or market claims
- Replace `optimizing-seo-aeo-geo-content` for editing an existing draft
- Replace `auditing-content-quality` for final publication readiness checks

---

## Import Notes

- Source: `_input/gxg-aeo-seo-geo-content-skills/gxg-content-researcher/SKILL.md`
- Adapted: 2026-06-29
- Changes: normalized frontmatter, mapped to `demand-gen`, added examples and out-of-scope boundaries, preserved source research principles in `docs/`.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial production import from GxG content skills |
