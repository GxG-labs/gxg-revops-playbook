---
name: auditing-content-quality
description: "Runs final publication-readiness audits for Russian SEO/AEO/GEO articles, checking reader value, factual safety, GxG structure and tone, headings, FAQ, checklists, unsupported claims, metadata, and native insert quality. Use when reviewing content before publishing, checking article quality, finding factual risks, auditing SEO/AEO/GEO readiness, or when user mentions \"content audit\", \"проверь статью\", \"готово к публикации\", \"quality review\", \"fact claims\", \"финальный чеклист\"."
status: active
domain: demand-gen
type: capability-uplift
tags: [demand-gen, #analysis, #process, #reporting, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read
---

# Auditing Content Quality

Reviews Russian SEO/AEO/GEO articles before publication and returns a concise, actionable readiness audit.

## When to Use This Skill

Activate when:
- A user has a near-final article and wants to know whether it is ready to publish
- The article needs checks for usefulness, factual reliability, structure, readability, FAQ, checklist, and metadata
- The team needs a quality gate after writing and SEO/AEO/GEO editing
- A draft may contain unsupported claims, weak native insertion, or generic sections

Do NOT use when: the user needs source research, article architecture, drafting, or full SEO editing instead of final review.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Final audit** | "audit this article" / "проверь перед публикацией" | See §Final Audit |
| **Focused audit** | "check facts only" / "проверь FAQ" | See §Focused Audit |

---

## Instructions

### Final Audit

Review in this order:

1. Reader value: does the article solve a real task or decision?
2. Structure: does it follow a clear GxG-like progression?
3. Accuracy: are claims sourced, safe, or clearly caveated?
4. SEO/AEO/GEO: is the content answer-ready and extractable?
5. Style: is the Russian natural, practical, and non-generic?
6. Conversion or native insert: is it helpful rather than intrusive?
7. Publication package: title, slug, meta description, FAQ, schema candidates, and final checklist.

Then score each area from 1 to 5:
- Usefulness
- Factual reliability
- GxG style match
- Structure
- SEO/AEO/GEO readiness
- Readability

Lead with actionable issues. Do not rewrite the whole article unless asked.

### Focused Audit

1. Confirm the requested focus: facts, style, structure, FAQ, SEO/AEO/GEO, native insert, metadata, or readiness.
2. Review only that dimension unless a severe publication risk appears elsewhere.
3. Provide specific fixes and one short improved example when the issue is stylistic.

---

## Output Format

```markdown
# Content Audit

## Verdict
Ready / Needs edits / Not ready

## Scores

## Critical Fixes

## Important Improvements

## Minor Polish

## SEO/AEO/GEO Status

## Fact Claims To Verify

## Final Publication Checklist
```

---

## Examples

### Example 1: Publication Gate

**Input / Context:**
A final Russian article about GEO for B2B SaaS with metadata, FAQ, and internal link ideas.

**Output:**
A verdict such as `Needs edits`, 1-5 scores, critical fixes around unsupported market claims, important improvements to answer-first definitions, minor style polish, SEO/AEO/GEO status, claims to verify, and a final checklist.

---

### Example 2: Focused Fact Audit

**Input / Context:**
The user asks only to check factual claims in an article about salary trends.

**Output:**
A claim-by-claim list showing which statements need sources, which should be softened, and which can stay as common practice or qualitative framing.

---

## Out of Scope

This skill does NOT:
- Conduct full research for missing sources
- Rewrite the whole article by default
- Replace the article architecture or drafting steps
- Guarantee search rankings, citations, traffic, conversion, or AI answer inclusion
- Approve unsupported numbers simply because they sound plausible

---

## Import Notes

- Source: `_input/gxg-aeo-seo-geo-content-skills/content-quality-auditor/SKILL.md`
- Adapted: 2026-06-29
- Changes: normalized slug and metadata, mapped to `demand-gen`, added focused audit workflow, examples, scoring detail, and out-of-scope boundaries.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial production import from GxG content skills |
