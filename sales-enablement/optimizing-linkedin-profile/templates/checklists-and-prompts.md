# Checklists and Prompts

Use these as reusable sub-skill prompts and quality gates.

## One-Command User Prompts

Career:

```text
Run optimizing-linkedin-profile. Use my LinkedIn export at {path} and CV at {path}. Goal: recruiter visibility for {target roles}. Build the profile rewrite and 30-day plan.
```

B2B:

```text
Run optimizing-linkedin-profile for B2B sales. ICP: {buyer/company type}. Offer: {offer}. Use my current profile below and give me the rewrite, Featured plan, content topics, and DM plan.
```

Hybrid:

```text
Run optimizing-linkedin-profile in hybrid mode. I want recruiter visibility for {roles} and client visibility for {ICP}. Use these inputs: {profile/CV/export/offer}.
```

Minimal input:

```text
Run optimizing-linkedin-profile. I do not have the export yet. Give me the shortest intake checklist and a first-pass profile structure for {target role/client}.
```

## LinkedIn Profile Audit Checklist

Score each 0-2:

| Item | Score |
|------|-------|
| Clear target audience | |
| Headline includes target role/category | |
| Headline includes specialty/tools/proof | |
| Photo is current and professional | |
| Banner supports positioning | |
| Location matches target market | |
| About first two lines are specific | |
| About includes proof and CTA | |
| Current role contains searchable keywords | |
| Experience bullets show scope/outcomes | |
| Skills match target roles/clients | |
| Featured contains 3-5 proof assets | |
| Recommendations support credibility | |
| Contact path is clear | |
| Open to Work/Services settings intentional | |
| Resume/profile consistency checked | |
| Analytics baseline recorded | |

Interpretation:
- 28-34: strong
- 20-27: usable but needs conversion work
- 12-19: search or proof gaps
- 0-11: rebuild positioning first

## LLM Prompt: Export Audit

```text
You are auditing my LinkedIn profile for recruiter visibility and B2B trust.

Inputs:
- LinkedIn export summary:
{paste parser output}
- CV/resume:
{paste or path}
- Target roles or target clients:
{list}

Tasks:
1. Identify searchability gaps.
2. Identify profile conversion gaps.
3. Compare LinkedIn against CV.
4. Build a keyword map.
5. Recommend headline, About, Experience, Skills, Featured, and settings changes.
6. Mark any missing proof with [PROOF NEEDED].
```

## LLM Prompt: Target Vacancy Optimization

```text
Optimize my LinkedIn profile for these target vacancies.

Target job descriptions:
{paste 3-10 JDs}

Current profile:
{paste profile text}

Return:
1. Repeated keywords and skills by frequency.
2. Missing keywords.
3. Headline options.
4. About rewrite.
5. Experience bullet rewrites.
6. Skills list.
7. Open to Work target titles.
8. Resume/LinkedIn mismatch risks.
Do not invent facts.
```

## LLM Prompt: B2B Social Selling Profile

```text
Build my LinkedIn profile for B2B sales and trust.

Offer:
{offer}

ICP:
{buyer roles, company type, market}

Proof:
{case studies, metrics, client types}

Current profile:
{profile}

Return:
1. Positioning statement.
2. Buyer-facing headline options.
3. About rewrite with CTA.
4. Featured section plan.
5. Services section suggestions.
6. Content pillars.
7. First 10 posts/comments/DM angles.
```

## Recommendation Request Prompt

```text
Could you write a short LinkedIn recommendation about our work on {project}? It would help if you mentioned:
- the problem we were solving
- what I contributed
- the result or change you saw
- what it was like working with me

No need for anything long; 4-6 sentences is perfect.
```

## Weekly Operating Checklist

- Review Search Appearances
- Review profile views
- Check if search terms match desired positioning
- Comment on 30-50 target-market posts
- Publish 1-2 useful posts or one strong proof post
- Send 5-10 warm DMs
- Add one new proof asset or improve one Featured item
- Follow up with open recruiter/buyer/referral conversations
