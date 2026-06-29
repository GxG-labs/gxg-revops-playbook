---
name: optimizing-seo-aeo-geo-content
description: "Edits Russian article drafts for SEO, AEO, and GEO visibility while preserving human usefulness, GxG voice, answer-first structure, entities, citations, internal links, FAQ, schema candidates, and natural readability. Use when optimizing article drafts, improving answer-engine readiness, editing GEO content, preparing SEO metadata, or when user mentions \"SEO редактура\", \"AEO\", \"GEO\", \"answer engine\", \"meta title\", \"schema\", \"внутренние ссылки\"."
status: active
domain: demand-gen
type: capability-uplift
tags: [demand-gen, #process, #analysis, #playbook, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read
---

# Optimizing SEO AEO GEO Content

Improves an existing Russian article draft for search engines, answer engines, and generative answer extraction without making the text robotic.

## When to Use This Skill

Activate when:
- A user has a draft and wants SEO/AEO/GEO editing
- Headings, definitions, FAQ, citations, schema ideas, or internal links need improvement
- The article should become easier to cite, summarize, and extract into AI-generated answers
- The user needs metadata, slug, FAQ schema candidates, or a precise edit plan

Do NOT use when: there is no draft yet, the task is pure research, or the user needs final publication audit rather than editing.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Full edit** | "edit this article" / "отредактируй под SEO/AEO/GEO" | See §Full Edit |
| **Edit plan** | "tell me what to fix" / "дай план правок" | See §Edit Plan |

---

## Instructions

### Full Edit

1. Identify the primary intent and check whether the article answers it in the first 150-250 words.
2. Improve H1/H2/H3 headings so they match real reader questions and article promises.
3. Add answer-first paragraphs to definition, comparison, process, and FAQ sections.
4. Ensure key entities, tools, concepts, roles, and metrics are named consistently.
5. Add or improve:
   - Comparison table
   - Checklist
   - FAQ
   - Mistakes section
   - Tools or resources section
   - Date-sensitive caveats
6. Strengthen evidence quality through:
   - Source-backed claims
   - Clear limits
   - Examples
   - Transparent uncertainty
   - No fake expertise or unsupported authority
7. Suggest internal links and schema markup only when supported by visible page content.
8. Produce an edited version plus notes, unless the user asks only for an edit plan.

### Edit Plan

1. Review the article against SEO, AEO, GEO, evidence, and readability criteria.
2. Group recommendations into critical, important, and optional changes.
3. Include specific replacement examples for headings, definitions, FAQ, metadata, and unsupported claims.
4. Avoid rewriting the whole article unless asked.

---

## Output Format

For full editing:

```markdown
# Edited Article

...

# SEO/AEO/GEO Notes

## Meta Title
## Meta Description
## Suggested Slug
## FAQ Schema Candidates
## Internal Link Ideas
## Claims To Verify
```

---

## Examples

### Example 1: Full GEO Edit

**Input / Context:**
A Russian draft about "AI search optimization" has generic headings, no FAQ, and several unsupported claims about traffic growth.

**Output:**
An edited article with clearer H2s, direct definitions, a comparison table, self-contained FAQ answers, softer wording for unsupported traffic claims, metadata, slug, schema candidates, and a claims-to-verify list.

---

### Example 2: Edit Plan Only

**Input / Context:**
The user asks for an SEO/AEO/GEO plan without rewriting the article.

**Output:**
A prioritized edit plan covering early answer quality, heading rewrites, missing entities, FAQ gaps, internal links, schema candidates, and risky claims.

---

## Reference

- Editor checklist: [docs/editor-checklist.md](docs/editor-checklist.md)

---

## Out of Scope

This skill does NOT:
- Keyword-stuff articles
- Add unsupported statistics, claims, or fake expertise
- Suggest structured data that is not supported by visible content
- Replace source research for time-sensitive claims
- Replace `auditing-content-quality` for final publication readiness

---

## Import Notes

- Source: `_input/gxg-aeo-seo-geo-content-skills/seo-aeo-geo-editor/SKILL.md`
- Adapted: 2026-06-29
- Changes: normalized slug, mapped to `demand-gen`, added edit-plan workflow, examples, and stricter publication-safety boundaries.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial production import from GxG content skills |
