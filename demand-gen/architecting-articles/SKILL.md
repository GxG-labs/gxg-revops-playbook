---
name: architecting-articles
description: "Designs Russian long-form article outlines in the GxG style, turning research briefs into practical H1/H2/H3 structure, answer-first sections, tables, mistakes, tools, checklists, FAQ, and native insertion points. Use when planning a content outline, structuring a Russian SEO article, turning research into article architecture, preparing a writer handoff, or when user mentions \"outline\", \"структура статьи\", \"план статьи\", \"Коротко\", \"FAQ\", \"чеклист\", \"GxG style\"."
status: active
domain: demand-gen
type: encoded-preference
tags: [demand-gen, #template, #process, #playbook, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read
---

# Architecting Articles

Turns a research brief into a practical Russian article structure that matches GxG content patterns and supports SEO/AEO/GEO readability.

## When to Use This Skill

Activate when:
- A user has a topic or research brief and needs a detailed article outline
- A Russian long-form article needs a `Коротко` block, section logic, FAQ, checklist, and useful tables
- A writer needs a precise handoff before drafting
- A draft feels generic because its section order does not match the reader's actual task

Do NOT use when: the user needs source gathering, full drafting, SEO editing, or final publication audit.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Article outline** | "make an outline" / "собери структуру" | See §Article Outline |
| **Structure repair** | "this outline is weak" / "улучши план" | See §Structure Repair |

---

## Instructions

### Article Outline

1. Confirm or infer the inputs:
   - Topic
   - Target reader
   - Research brief or known facts
   - Desired category: explanation, comparison, checklist, guide, tool review, career guide, or opinionated playbook
   - Whether a native vacancy, product, or resource block belongs in the article
2. Use this default skeleton unless the topic clearly needs another order:
   - H1: topic plus practical pain or outcome
   - Date placeholder if the article is time-sensitive
   - `## Содержание`
   - `Коротко:` with 4-6 useful bullets
   - Opening scene: concrete problem, mistake, or market change
   - Definition in plain language
   - Distinction from adjacent concepts
   - Mechanism: how it works in practice
   - Segments, stages, metrics, or process
   - Example, table, or scenario
   - Typical mistakes
   - Native insertion block if relevant
   - Tools or resources
   - Checklist
   - Advanced or implementation section
   - FAQ
   - Final summary with practical next steps
3. Make every H2 answer a reader question or remove practical confusion.
4. Include at least one table or comparison when the topic has categories, stages, tools, or tradeoffs.
5. Include a checklist and FAQ for answer extraction.
6. Return a detailed outline, not a full article.

### Structure Repair

1. Identify where the current outline loses the reader: missing definition, weak order, generic H2s, no examples, no action step, or repetitive FAQ.
2. Reorder sections into problem -> definition -> mechanism -> application -> mistakes -> action.
3. Replace generic headings with question- or outcome-led headings.
4. Add missing tables, examples, checklist items, FAQ, and native insertion placement.

---

## Output Format

```markdown
# Article Outline

## H1

## Коротко

## Sections

## Tables / Lists To Include

## Native Insert Placement

## FAQ

## Notes For Writer
```

---

## Examples

### Example 1: Retention Marketing Outline

**Input / Context:**
Research brief for "retention-маркетинг для EdTech", audience: marketing leads and founders.

**Output:**
An outline with a practical H1, a `Коротко` block, sections on definition, lifecycle mechanics, metrics, examples for EdTech cohorts, common mistakes, tool categories, checklist, FAQ, and notes for the writer about cautious claims.

---

### Example 2: Weak SEO Outline Repair

**Input / Context:**
An outline has headings like "Introduction", "Benefits", "Conclusion", and no examples.

**Output:**
A repaired structure with concrete H2s such as "Что такое GEO простыми словами", "Чем GEO отличается от SEO и AEO", "Какие блоки помогают статье попадать в ответы", "Ошибки, из-за которых GEO-оптимизация выглядит искусственно", plus table, checklist, FAQ, and writer notes.

---

## Reference

- GxG structure patterns: [docs/gxg-structure.md](docs/gxg-structure.md)

---

## Out of Scope

This skill does NOT:
- Conduct source research or verify unstable facts
- Write the full article draft
- Perform final SEO/AEO/GEO editing
- Audit publication readiness
- Force the default skeleton when the reader's task requires a different order

---

## Import Notes

- Source: `_input/gxg-aeo-seo-geo-content-skills/gxg-article-architect/SKILL.md`
- Adapted: 2026-06-29
- Changes: normalized naming, mapped to `demand-gen`, added structure repair workflow, examples, and explicit out-of-scope boundaries.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial production import from GxG content skills |
