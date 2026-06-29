---
name: writing-articles
description: "Writes Russian long-form article drafts in the GxG style from an approved outline, using practical explanations, short paragraphs, examples, tables, mistakes, checklists, FAQ, and restrained native product or vacancy references. Use when drafting Russian content, turning an outline into an article, matching GxG voice, writing SEO/AEO/GEO-ready sections, or when user mentions \"напиши статью\", \"черновик\", \"GxG voice\", \"русский стиль\", \"Коротко\", \"FAQ\", \"чеклист\"."
status: active
domain: demand-gen
type: encoded-preference
tags: [demand-gen, #template, #playbook, #process, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read
---

# Writing Articles

Writes practical Russian article drafts from a research brief and outline while preserving the GxG voice and avoiding unsupported claims.

## When to Use This Skill

Activate when:
- A user provides an approved outline and wants a complete Russian article draft
- A draft needs to sound practical, clear, and GxG-like rather than generic or promotional
- A content workflow needs the writing step after `researching-content` and `architecting-articles`
- The article should include `Коротко`, examples, tables, mistakes, checklist, FAQ, and restrained native insertion

Do NOT use when: the user has not done research for a fact-sensitive topic, needs only an outline, or needs SEO editing rather than drafting.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Full draft** | "write the article" / "напиши черновик" | See §Full Draft |
| **Section draft** | "write this section" / "распиши H2" | See §Section Draft |

---

## Instructions

### Full Draft

1. Start from the approved outline. If no outline is present, create a brief assumed outline and label assumptions.
2. Write in Russian unless the user asks for another language.
3. Write H1 and the `Коротко:` block first.
4. Open with a recognizable failure, change, or practical confusion rather than a generic introduction.
5. Expand each H2 with:
   - Direct answer
   - Explanation in plain language
   - Example, consequence, or tradeoff
   - Practical next step when useful
6. Use tables for comparisons, stages, formats, channels, metrics, tools, or criteria.
7. Add native insertion only where it supports the reader's task and does not interrupt the explanation.
8. End with a practical summary, not a sales pitch.
9. Do not invent numbers. If a claim needs proof, either omit it or mark it for verification.

### Section Draft

1. Identify the section's job in the article: definition, comparison, mechanism, mistake, example, checklist, FAQ, or summary.
2. Start with a direct claim or answer.
3. Add 1-2 short explanatory paragraphs.
4. Include an example, list, or table if it improves scanability.
5. Close with the implication for the reader.

---

## Style Rules

- Use calm, direct, useful Russian.
- Prefer concrete business, marketing, product, career, or operational situations over abstract advice.
- Explain terms simply, then show how they behave in practice.
- Use contrasts such as "не X, а Y" only when they clarify the point.
- Keep paragraphs short, usually 2-5 sentences.
- Do not mention AI generation.
- Do not overpromise rankings, traffic, salary, or conversion.
- Keep brand mentions natural and sparse.

---

## Examples

### Example 1: Full Article Draft

**Input / Context:**
An approved outline for "GEO vs SEO для B2B SaaS в 2026 году" with research notes and FAQ.

**Output:**
A Russian article draft with H1, `Коротко`, direct definitions, comparison table, practical implementation section, mistakes, checklist, FAQ, and cautious wording around trends and performance claims.

---

### Example 2: Section Draft

**Input / Context:**
The user asks to write only the section "Какие метрики смотреть в retention-маркетинге".

**Output:**
A concise Russian H2 section that explains why retention should not be judged by open rate alone, adds a table of metrics such as repeat purchase, churn, activation, cohort retention, and LTV, and closes with a practical measurement warning.

---

## Reference

- GxG voice guide: [docs/gxg-voice.md](docs/gxg-voice.md)

---

## Out of Scope

This skill does NOT:
- Research current facts or sources
- Design the article outline from scratch when the user needs a robust architecture step
- Perform full SEO/AEO/GEO optimization after drafting
- Audit the article for publication readiness
- Copy existing GxG wording verbatim

---

## Import Notes

- Source: `_input/gxg-aeo-seo-geo-content-skills/gxg-style-writer/SKILL.md`
- Adapted: 2026-06-29
- Changes: normalized frontmatter, mapped to `demand-gen`, added section-level workflow, examples, and explicit quality boundaries.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial production import from GxG content skills |
