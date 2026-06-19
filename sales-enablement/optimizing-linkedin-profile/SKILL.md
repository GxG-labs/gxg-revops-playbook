---
name: optimizing-linkedin-profile
description: "Optimizes LinkedIn profiles for recruiter visibility, career positioning, B2B sales, social selling, and executive credibility using LinkedIn export data, target-role/client research, section-by-section profile rewrites, content planning, networking actions, and analytics. USE WHEN the user wants to optimize a LinkedIn profile, process a LinkedIn data export, improve recruiter visibility, attract B2B clients, create a social selling plan, rewrite headline/About/Experience/Skills, or asks about \"LinkedIn SEO\", \"Open to Work\", \"LinkedIn profile\", \"recruiters\", \"B2B sales\", \"social selling\", \"LinkedIn export\"."
status: active
domain: sales-enablement
type: capability-uplift
tags: [sales-enablement, demand-gen, #playbook, #process, #template, #analysis, #p1]
version: 1.1.1
updated: 2026-06-19
author: GxG
allowed-tools: Read, Write, Bash, Glob, Grep
---

# Optimizing LinkedIn Profile

Creates a practical LinkedIn profile and activity plan for two outcomes: being found by recruiters and being trusted by B2B buyers.

## Runtime Compatibility

This is a vendor-neutral skill. It uses plain instructions, repository-relative paths, Markdown docs, and an optional Python helper script. Claude Code, Codex, Gemini, or any other file-reading LLM agent should be able to follow the same workflow.

Runtime notes:
- If local command execution is available, use the parser script for LinkedIn export summaries.
- If local command execution is not available, read the CSV files with any safe CSV parser available in that environment.
- If file access is not available, ask the user to paste the profile/export summary and continue with the same workflow.
- Do not rely on session memory for persistent state; write durable outputs to files when the user asks for saved artifacts.

## When to Use This Skill

Activate when:
- A user wants to optimize LinkedIn for recruiter visibility, job search, or inbound opportunities
- A user wants LinkedIn positioning for B2B sales, consulting, founder-led growth, RevOps, or social selling
- A user provides a LinkedIn data export, profile copy, resume/CV, target job descriptions, ICP, offer, or client profile
- A user asks for section-by-section rewrites: headline, About, Experience, Skills, Featured, Recommendations, Services, Activity
- A user wants the next-step plan after updating the profile: content, comments, networking, outreach, analytics, and iteration

Do NOT use when: the user only needs a generic resume rewrite with no LinkedIn component, a company LinkedIn Page strategy, paid LinkedIn ads, or scraping live LinkedIn pages.

---

## Core Principle

Treat LinkedIn as a funnel:

1. **Search visibility** - appear in LinkedIn Recruiter, Sales Navigator, people search, and AI-assisted search.
2. **Search-result conversion** - earn a click from the profile card: photo, headline, current role, location, mutuals.
3. **Profile conversion** - convert the viewer through proof: About, Experience, Featured, Skills, Recommendations.
4. **Ongoing distribution** - create repeated touchpoints through content, comments, DMs, and network signals.

Every recommendation must serve one of those four stages. Avoid cosmetic advice unless it changes searchability, trust, clarity, or conversion.

---

## Single-Run Behavior

When this skill is invoked, run the whole system. Do not ask the user to choose sub-skills or read internal docs.

1. **Infer the mode** from the user's words and files:
   - Recruiters, CV, resume, job search, vacancy, Open to Work -> career mode.
   - Clients, leads, founder, consultant, offer, ICP, social selling -> B2B sales mode.
   - Both career and clients, or unclear but both are plausible -> hybrid mode.
2. **Use whatever input exists**:
   - If a LinkedIn export path/zip is present, run the export workflow and parser.
   - If profile text is pasted, audit that directly.
   - If only a CV/resume is present, build a LinkedIn draft from it and mark LinkedIn-specific unknowns.
   - If only the target role/client is present, produce an intake checklist and a first-pass profile structure.
3. **Ask at most one intake block** when blocked. Keep it short:
   ```text
   To run this properly, send any of these:
   1. LinkedIn export zip/folder or pasted profile text
   2. CV/resume or career history
   3. Target role/vacancy or target client/offer
   ```
4. **After receiving inputs, proceed without asking more setup questions** unless a missing fact would create a false claim.
5. **Load only the docs needed for the inferred mode**:
   - Always: `positioning.md`, `profile-section-guide.md`
   - Export provided: `linkedin-export-processing.md`
   - Career mode: `career-mode.md`
   - B2B mode: `b2b-sales-mode.md`
   - Hybrid mode: both career and B2B docs
   - Always for final plan: `post-launch-plan.md`
6. **Return a ready-to-use profile plan**, not a list of internal next steps.

---

## Workflow Router

| Workflow | Trigger | Read |
|----------|---------|------|
| **Source Research** | "what is current best practice?" / "save the research" | [docs/research-2026.md](docs/research-2026.md), [docs/source-repositories.md](docs/source-repositories.md) |
| **Data Download Guide** | "how to download LinkedIn data" / "I don't have the export yet" | [docs/linkedin-export-processing.md](docs/linkedin-export-processing.md) — How to Download section |
| **LinkedIn Export Audit** | "process my LinkedIn export" / `Complete_LinkedInDataExport.zip` | [docs/linkedin-export-processing.md](docs/linkedin-export-processing.md) |
| **Positioning Strategy** | "target role", "target client", "position me" | [docs/positioning.md](docs/positioning.md) |
| **Profile Rewrite** | "rewrite my profile", "optimize headline/About/Experience" | [docs/profile-section-guide.md](docs/profile-section-guide.md) |
| **Career Mode** | "recruiters", "job search", "target vacancy" | [docs/career-mode.md](docs/career-mode.md) |
| **B2B Sales Mode** | "clients", "social selling", "consulting", "founder brand" | [docs/b2b-sales-mode.md](docs/b2b-sales-mode.md) |
| **After Profile Update** | "what to do after profile is created?" | [docs/post-launch-plan.md](docs/post-launch-plan.md) |
| **Checklists & Prompts** | "give me checklist", "make prompt", "audit rubric" | [templates/checklists-and-prompts.md](templates/checklists-and-prompts.md) |

---

## Workflow

### 1. Intake

Collect what is available. Do not block if some inputs are missing; produce conservative output and mark gaps.

Required for best work:
- Current LinkedIn profile text or export directory/zip
- Resume/CV or career/project history
- Target outcome: career, B2B sales, or both
- Target role, job descriptions, ICP, buyer persona, or offer
- Geography, language, remote/hybrid/on-site constraints
- Proof assets: portfolio, case studies, dashboards, publications, posts, talks, recommendations

If using a LinkedIn export, follow [docs/linkedin-export-processing.md](docs/linkedin-export-processing.md) and use the parser script when local command execution is available.

User-friendly starting prompts:

```text
Run optimizing-linkedin-profile on this LinkedIn export and CV. Goal: recruiter visibility for RevOps roles.
```

```text
Optimize my LinkedIn for B2B clients. ICP: B2B SaaS founders and CROs. Offer: RevOps cleanup and HubSpot/Salesforce systems.
```

```text
Here is my current profile. Make it work for both recruiters and consulting clients.
```

### 2. Choose Mode

Pick the primary mode:
- **Career mode**: optimize for recruiter search, job-fit proof, target role keywords, Open to Work, resume/profile alignment.
- **B2B sales mode**: optimize for buyer trust, ICP relevance, offer clarity, social proof, content authority, and DM conversion.
- **Hybrid mode**: build one profile with two audiences. Keep headline and About broad enough to avoid confusing either audience; use Featured and Activity to segment proof.

### 3. Build the Keyword and Proof Map

Create a table:

| Bucket | Career Mode | B2B Sales Mode |
|---|---|---|
| Target nouns | Role titles, seniority, tools, industry | Buyer role, pain, category, outcome |
| Search terms | Job descriptions, recruiter filters, skills | ICP language, Sales Navigator filters, problem terms |
| Proof | Metrics, projects, companies, systems | Cases, client outcomes, offers, POV |
| Conversion action | Recruiter InMail, referral, interview | Connection, call, reply, intro |

Use exact terms from target job descriptions or buyer language. Also write natural sentences for AI-assisted semantic search.

### 4. Rewrite the Profile

Follow [docs/profile-section-guide.md](docs/profile-section-guide.md) section by section. Output:
- Headline options
- About rewrite
- Experience rewrite guidance and suggested bullets
- Skills list and top skills
- Featured section plan
- Recommendations request plan
- Open to Work / Services / privacy / verification settings
- Gaps and risks

Never invent facts. Use `[PROOF NEEDED]`, `[METRIC NEEDED]`, or `[CONFIRM]` placeholders when evidence is missing.

### 5. Build the After-Update Plan

Follow [docs/post-launch-plan.md](docs/post-launch-plan.md). Create:
- 30-day activity plan
- Commenting targets
- Content pillars
- Weekly networking actions
- DM/referral/social-selling scripts
- Analytics loop using Search Appearances, profile views, DMs, replies, and meetings/interviews

### 6. Quality Gate

Before final output, verify:
- The profile names a clear audience and target outcome
- The headline contains target role/category terms and a proof signal
- The About opens with a memorable identity hook, not a generic professional summary
- The first two lines of About are strong enough before "see more"
- Experience uses outcomes, scope, systems, or concrete problems instead of responsibilities only
- Skills match the target role/client, not only the user's past
- Featured proves the claim made in the headline/About
- The profile supports both exact keyword search and semantic AI matching
- Post-launch actions are specific enough to execute this week

---

## Output Format

Use this structure unless the user asks for a narrower deliverable:

```markdown
# LinkedIn Profile Plan

## What I Used
- Inputs:
- Mode:
- Data limits:

## Strategy
- Primary outcome:
- Audience:
- Positioning:
- Search keywords:
- Proof themes:

## Profile Rewrite
### Headline
### About
### Experience
### Skills
### Featured
### Recommendations
### Settings

## Gaps

## 30-Day Activity Plan

## Metrics to Track

## What To Send Me Next
- Only include if the output had important [PROOF NEEDED] or [CONFIRM] gaps.

## Source Notes
```

---

## Examples

### Example 1: Career Optimization from Export and CV

**Input / Context:**
User provides `Complete_LinkedInDataExport.zip`, a CV, and three target roles: RevOps Manager, Sales Operations Manager, GTM Systems Lead.

**Output:**
- Parser summary of `Profile.csv`, `Positions.csv`, `Skills.csv`, `Certifications.csv` if present
- Keyword map from target roles: Salesforce, HubSpot, pipeline governance, forecasting, attribution, GTM systems
- Three headline options
- Rewritten About section with proof placeholders for missing metrics
- Experience bullets rewritten around scope, systems, tools, and outcomes
- Skills list with top 10 prioritized
- Recruiters-only Open to Work settings and target job titles
- 30-day networking and analytics plan

### Example 2: B2B Sales Profile for Consultant

**Input / Context:**
User is a fractional RevOps consultant targeting B2B SaaS founders and CROs. They have case notes but no polished LinkedIn profile.

**Output:**
- Positioning: "RevOps systems for B2B SaaS teams moving from founder-led sales to repeatable pipeline"
- Buyer-facing headline options
- About section with ICP, pain, proof, and call-to-action
- Featured plan: 2 case studies, 1 diagnostic checklist, 1 offer page, 1 dashboard sample
- Content pillars: pipeline visibility, CRM hygiene, AI-assisted outbound, forecasting, sales handoffs
- Commenting and DM plan for founder/CRO audiences

---

## Reference

- 2026 research pack: [docs/research-2026.md](docs/research-2026.md)
- External skill/repo references: [docs/source-repositories.md](docs/source-repositories.md)
- LinkedIn export workflow: [docs/linkedin-export-processing.md](docs/linkedin-export-processing.md)
- Positioning workflow: [docs/positioning.md](docs/positioning.md)
- Section guide: [docs/profile-section-guide.md](docs/profile-section-guide.md)
- Career mode: [docs/career-mode.md](docs/career-mode.md)
- B2B mode: [docs/b2b-sales-mode.md](docs/b2b-sales-mode.md)
- After-update plan: [docs/post-launch-plan.md](docs/post-launch-plan.md)
- Checklists and prompts: [templates/checklists-and-prompts.md](templates/checklists-and-prompts.md)
- Export parser: [scripts/linkedin_export_summary.py](scripts/linkedin_export_summary.py)

---

## Out of Scope

This skill does NOT:
- Scrape live LinkedIn pages, automate browsing, or bypass LinkedIn access controls
- Guarantee LinkedIn ranking; LinkedIn does not publish a full ranking formula
- Fabricate metrics, employers, certifications, recommendations, or endorsements
- Replace legal/privacy judgment about public job-search signaling
- Run paid LinkedIn ads or company-page marketing
- Send automated spam, connection farms, or non-consensual mass outreach

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.1.1 | 2026-06-19 | Added About/Summary identity hook guidance with examples and updated career/B2B templates plus audit checklist |
| 1.1.0 | 2026-06-17 | Integrated cosmo-hg/Linkedin-Profile-Optimization-Prompts: added LinkedIn data download guide, Perceived Identity analysis (Ad_Targeting.csv), two-phase Audit→Rebuild prompt workflow, dot-separated headline formula, 10-skills-per-role guideline |
| 1.0.0 | 2026-06-15 | Initial active skill with research pack, export parser, profile rewrite workflow, career mode, B2B sales mode, and after-update activity plan |
