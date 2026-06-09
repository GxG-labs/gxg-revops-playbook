---
name: writing-business-cases
description: "Produces B2B business cases in a four-level pyramid format — one-line essence, one-paragraph case, one-slide case, and full web-page version — using a blend of Meta-style success story, MBA-style case logic, and B2B sales proof patterns. USE WHEN the user wants to turn a project, implementation, AI system, campaign, or business result into a compelling case; when preparing portfolio cases, sales decks, executive presentations, or buyer enablement materials; or when the user mentions \"business case\", \"case study\", \"portfolio case\", \"success story\", \"proof of value\", \"sales proof\", \"roi story\", \"case write-up\", \"executive summary\"."
status: active
domain: sales-enablement
type: capability-uplift
tags: [sales-enablement, #template, #playbook, #framework, #p1]
version: 1.0.0
updated: 2026-06-09
author: GxG
allowed-tools: Read
---

# Writing Business Cases

Turns any project, implementation, AI system, campaign, or business result into a sharp B2B business case — ready for a slide, a portfolio, or a buyer conversation.

## When to Use This Skill

Activate when:
- A user describes a project or initiative and wants to document its business impact
- A user needs a case for a sales deck, portfolio, executive presentation, or internal buy-in
- A user has a weak draft that starts with tools instead of business outcomes
- A user asks to write a "case study", "success story", "proof of value", or "ROI story"
- A user needs a one-slide case for a deck or a full web-page version for a website

Do NOT use when: the user needs an investor pitch deck (different structure), a financial model or spreadsheet ROI calculator, or technical product documentation.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Full pyramid** | "write a business case for X" | See §Full Pyramid |
| **Single format** | "write a one-slide case" / "write a one-pager" | See §Single Format |
| **Rewrite** | "improve this case" / "rewrite this draft" | See §Rewrite |

---

## Instructions

### Full Pyramid

1. Run the intake checklist — extract all available facts from the user's input:
   - Product or project name
   - Client, company, or sector
   - Business challenge and constraints
   - Solution design and role of AI, automation, team, or process
   - Adoption path and timeframe
   - Metrics before and after (or qualitative outcomes if metrics are missing)
   - Audience and buying committee relevance (CEO, CFO, CRO, CMO, COO, VP Sales, RevOps, CS)

2. If key facts are missing: proceed with conservative wording. Ask only if the missing fact changes meaning or could create a false claim.

3. Produce all four pyramid levels in order:

   **Level 1 — One-Line Essence**
   One sentence: `[Action] helped [team/company] solve [business constraint] and achieve [measurable or qualitative outcome].`
   Must work as a slide subtitle, portfolio caption, or case card.

   **Level 2 — One-Paragraph Case**
   Five to seven sentences: Context → Challenge → Decision or core insight → Solution → Adoption → Result → Reusable lesson (if useful).

   **Level 3 — One-Slide Case**
   ```
   [CASE TITLE]
   [FUNCTION / BUSINESS MOTION]

   BUSINESS PROBLEM
   [3–5 lines: business problem, stakes, revenue or efficiency constraint, deeper bottleneck]

   WHAT CHANGED
   [3–5 lines: what was built or changed, who used it, why it fit, how daily work changed]

   BUSINESS IMPACT
   [2–4 short result lines — metrics first, no filler]
   ```

   **Level 4 — Full Web-Page Case**
   Sections: Outcome-led headline → At a Glance (client, function, challenge, solution, result, timeframe) → The Challenge → The Insight → The Solution → How It Worked → Results → Why It Worked

4. Apply the quality bar before finalising:
   - A CEO can understand the value in 10 seconds
   - A skeptical operator can see what actually changed
   - The result is connected to the intervention, not just placed after it
   - The slide version stands alone without speaker notes
   - Language is dense, concrete, and human — no hype

### Single Format

1. Run the intake checklist (same as above).
2. Produce only the requested format.
3. Still apply the quality bar.

### Rewrite

1. Read the draft. Identify which quality bar checks it fails.
2. Apply the rewrite procedure:
   - Preserve true facts and useful phrases
   - Remove generic claims ("improve efficiency", "better quality")
   - Replace tool-first language with business-first language
   - Compress repeated context
   - Move metrics to the top or Results section
   - Make Challenge and Solution parallel in scale
   - End with outcomes, not explanation
3. Output the rewritten version. Flag any metric gaps or false causality claims found in the original.

---

## Reference

- Case format templates and B2B patterns: [docs/case-formats.md](docs/case-formats.md)

---

## Examples

### Example 1: AI Implementation Case

**Input / Context:**
> We built an AI outreach personalisation system for a 40-rep sales team. Reps used to spend 45 min per prospect on research. Now it takes 5 min. Reply rates went from 3% to 8%. Deployed in 6 weeks.

**Output:**

**One-Line Essence**
An AI-powered research and personalisation system helped a 40-rep sales team cut prospect research time by 89% and grow reply rates from 3% to 8%.

**One-Paragraph Case**
A mid-market B2B sales team of 40 reps was generating outbound pipeline manually — each rep spending up to 45 minutes researching a single prospect before writing a personalised message. The process could not scale without hiring, and inconsistent research quality was compressing reply rates and pipeline conversion. The team built an AI system that automated prospect research, synthesised buying signals, and drafted personalised outreach copy for rep review. Integration with their CRM and sequencing tool meant reps could act in minutes rather than hours. Adoption reached full team coverage within the first month of rollout. Reply rates increased from 3% to 8% and per-rep research time dropped from 45 minutes to under 5 minutes — effectively giving the team the output capacity of a much larger org. The case shows how automating the research layer, not the sending layer, is where outbound leverage compounds.

**One-Slide Case**
```
AI OUTREACH PERSONALISATION
Sales Productivity / New Pipeline Creation

BUSINESS PROBLEM
A 40-rep outbound team could not scale pipeline without growing headcount.
Each rep spent 45 minutes per prospect on research — inconsistent quality,
compressed reply rates, and a ceiling on weekly activity volume.

WHAT CHANGED
Built an AI system that automates prospect research and drafts personalised
outreach for rep review. Connected to CRM and sequencing tools. Full team
adoption in week four. Reps shifted from research mode to review-and-send.

BUSINESS IMPACT
89% reduction in prospect research time (45 min → under 5 min)
Reply rate increased from 3% to 8%
40 reps now operating at the output capacity of a significantly larger team
```

**Full Web-Page Case**

# 40-Rep Sales Team Triples Reply Rate by Automating Prospect Research

A mid-market B2B sales team rebuilt their outbound motion around AI research automation — cutting per-prospect prep time by 89% and driving reply rates from 3% to 8% across the full team.

## At a Glance
- Client / context: Mid-market B2B, 40-rep outbound sales team
- Function: Sales productivity, new pipeline creation
- Challenge: Manual research was capping outbound capacity and compressing reply rates
- Solution: AI system automating prospect research and personalised outreach drafts
- Result: 89% reduction in research time; reply rate 3% → 8%
- Timeframe: 6-week implementation; full team adoption by week 4

## The Challenge
The team was generating outbound pipeline entirely by hand. Each rep spent up to 45 minutes researching a single prospect — pulling company news, role context, LinkedIn signals, and recent triggers — before writing a personalised first message. At this rate, weekly activity volume had a hard ceiling, and research quality varied widely by rep. The inconsistency was visible in results: a 3% reply rate, well below the team's pipeline targets.

## The Insight
The bottleneck was not rep effort or message quality — it was the research layer. Reps who spent more time on research wrote better messages, but the time cost made that impossible at scale. Automating research and synthesising buying signals, while keeping the rep in control of the final message, could compress prep time without removing human judgment from the send decision.

## The Solution
An AI system was built to automate prospect research — pulling data from CRM enrichment, LinkedIn, news feeds, and intent signals — and generate a structured research brief plus a draft personalised opening for each prospect. The system integrated with the team's CRM and outbound sequencing tool. Reps reviewed and approved drafts before sending; no message went out without human sign-off.

## How It Worked
1. Prospect enters CRM queue.
2. AI system pulls enrichment, news, role signals, and intent data.
3. System generates research brief and personalised draft message.
4. Rep reviews, edits if needed, approves.
5. Message sends through existing sequencing tool.

## Results
- Prospect research time: 45 minutes → under 5 minutes (89% reduction)
- Reply rate: 3% → 8% across the full 40-rep team
- Full team adoption reached by week 4 of a 6-week rollout

## Why It Worked
Automating the research layer — not the send layer — preserved the human judgment that makes personalisation credible while eliminating the time cost that made it unscalable. The architecture kept reps in control of the final message, which drove adoption: reps felt augmented, not replaced.

---

### Example 2: Rewriting a Weak Draft

**Input / Context:**
> Draft: "We implemented an AI tool for the sales team that improved efficiency and helped reps be more productive. The tool used NLP and GPT-4 to generate content. Results were good and the team liked it."

**Output (rewritten):**

**One-Line Essence**
An AI-assisted content generation system helped a B2B sales team produce consistent, on-message outreach at scale — reducing content creation time and improving rep adoption of approved messaging.

**One-Paragraph Case**
*(Note: key metrics were not provided in the original draft — conservative qualitative outcomes used below. Confirm specific metrics if available.)*

The sales team was producing outbound content manually, with inconsistent messaging quality across reps. Variation in message quality was creating uneven pipeline results and making it difficult to scale good rep behaviour across the full team. The team implemented an AI system to generate on-brand sales content for rep review and customisation. The solution removed the blank-page problem for reps and encoded approved messaging patterns into the workflow. Adoption was positive — reps used the system as part of their daily outreach process. Content consistency improved and the time reps spent on content creation decreased. The case shows how AI works best in sales content workflows when reps remain in control of the final output rather than being bypassed.

*(Flagged: no baseline metrics, no quantified results, no timeframe in the original. Rewritten with conservative language. Recommend adding: reply rate before/after, content creation time saved, team size, and rollout duration.)*

---

## Out of Scope

This skill does NOT:
- Build financial models, ROI spreadsheets, or TCO calculators
- Write investor pitch decks or fundraising materials (different structure and audience)
- Produce technical product documentation or capability specs
- Run win/loss analysis — for that, use the `analyzing-win-loss` skill (when available)
- Write RFP responses or proposal documents

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-09 | Initial addition — adapted from `write-business-case` source skill |
