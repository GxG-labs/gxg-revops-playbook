# LinkedIn Export Processing Sub-Skill

Use this when the user provides `Complete_LinkedInDataExport.zip`, an unzipped LinkedIn export directory, or CSV files from LinkedIn's "Get a copy of your data" feature.

## How to Download Your LinkedIn Data

If the user does not have the export yet, give them these exact steps:

1. Open [linkedin.com](https://www.linkedin.com) and log in.
2. Click your profile photo → **Settings & Privacy**.
3. In the left sidebar, click **Data Privacy**.
4. Click **Get a copy of your data**.
5. Select **Want something in particular? → Request a data archive**.
6. Check the box for **Select all** (or pick specific categories — see below).
7. Click **Request archive**.
8. LinkedIn emails a download link within 10 minutes (basic) to 24 hours (full archive).
9. Download the ZIP and place it anywhere on your machine.
10. Share the path (or unzipped folder) with the agent.

**Recommended categories to select:**
- Profile
- Positions
- Education
- Skills
- Certifications
- Connections
- Invitations
- Ad Targeting (reveals LinkedIn's algorithmic perception of you)
- Inferences about you
- Messages (optional — only if you want network/outreach analysis)
- Learning (optional — shows skill development trajectory)
- Company Follows (optional — reveals inferred interests)

> The full archive may take up to 24 hours. For a fast first pass, request only Profile, Positions, Education, Skills, and Ad Targeting — these arrive in ~10 minutes.

---

## Privacy and Boundary

Use official user-provided export files. Do not scrape live LinkedIn pages or ask for cookies. Do not infer private facts not present in the export or supplied by the user.

## Required Inputs

Best inputs:
- LinkedIn export zip or unzipped directory
- Resume/CV or career history
- Target roles or target client profile
- Optional: target job descriptions, ICP, offer, portfolio, case studies

Minimum export files:
- `Profile.csv`
- `Positions.csv`
- `Education.csv`
- `Skills.csv`

Useful optional files:
- `Certifications.csv`
- `Languages.csv`
- `Projects.csv`
- `Volunteering.csv`
- `Recommendations_Received.csv`
- `Connections.csv`
- `Messages.csv`
- `Invitations.csv`
- `Ad_Targeting.csv`
- `Inferences_about_you.csv`

## Deterministic Parser

When local command execution is available, run:

```bash
python sales-enablement/optimizing-linkedin-profile/scripts/linkedin_export_summary.py /path/to/export-or-zip
```

The parser:
- Uses Python's `csv` module, not string splitting
- Handles UTF-8 BOM
- Handles multiline descriptions
- Accepts `.zip` or directory
- Emits Markdown summary

If command execution is not available, use the same file list and parsing rules with the runtime's safest available CSV reader. Do not split CSV files on raw commas or newlines.

## Audit Pass

### 1. Profile

Extract:
- Name
- Headline
- Summary/About
- Industry
- Location
- Websites
- Contact hints

Check:
- Is headline default title/company only?
- Does headline contain target role/category keywords?
- Does About open with a clear identity and proof?
- Does location match target market?
- Does industry match target career/client audience?
- Are portfolio/contact links present?

### 2. Positions

For each role:
- Company
- Title
- Start/end date
- Location
- Description

Check:
- Missing descriptions
- Titles inconsistent with resume
- Missing target keywords in current/recent roles
- Responsibility-only wording
- No tools, systems, scope, or outcomes
- Gaps or mismatched chronology

### 3. Skills

Extract all skill names.

Check:
- Missing target role/client skills
- Too many generic soft skills
- Important tools absent
- Old skills dominating current positioning
- Top skill candidates for target outcome

### 4. Education, Certifications, Languages

Check:
- Degree/certification relevance to target role
- Missing certifications that the user actually has
- Languages relevant to location/client market
- Expired or unverified credentials

### 5. Projects and Featured Candidates

Projects, publications, links, recommendations, and strong posts can become Featured proof.

Select 3-5:
- Best case study
- Best technical or operational proof
- Best client/result proof
- Best writing/thought-leadership proof
- Best credential

### 6. Connections and Messages

Use only if the user asks for networking/outreach.

Analyze:
- Recruiter connections
- Former colleagues
- Buyer personas
- Referral paths
- Warm intros
- Dormant relationships

Do not expose private message content in final output unless needed and approved.

### 7. Ad Targeting / Inferences — Perceived Identity Analysis

`Ad_Targeting.csv` and `Inferences_about_you.csv` reveal how LinkedIn's algorithm currently classifies the user. This is valuable because recruiters and Sales Navigator users often see an algorithmically filtered version of your profile — not the one you think you're showing.

Run a **Perceived Identity** analysis:

1. Extract all targeting categories from `Ad_Targeting.csv` (columns: `Category`, `Value`).
2. Group into clusters: industry, seniority, function, skills/tools, interests, company type, geography.
3. Extract member attributes from `Inferences_about_you.csv` if present.
4. Summarize as a "Perceived Identity" statement: what profile LinkedIn thinks this person has.

Output format:
```markdown
## Perceived Identity (LinkedIn Algorithmic View)

**Industry signal:** {what LinkedIn thinks your industry is}
**Seniority signal:** {what LinkedIn infers about your level}
**Function signal:** {department/role LinkedIn places you in}
**Skills/tools signal:** {tools and capabilities LinkedIn associates with you}
**Interest signal:** {topics and content LinkedIn links to you}
**Company type signal:** {B2B/B2C/startup/enterprise inference}

**Gap analysis:**
| What LinkedIn thinks | What you want to be seen as | Severity |
|---------------------|----------------------------|----------|
| {category mismatch} | {desired positioning} | High/Med/Low |
```

5. Use the gap table to prioritize profile rewrites — sections that correct high-severity mismatches get the most keyword and proof investment.

Do not overfit to ad categories. Ad targeting is a probabilistic system, not a recruiter ranking input. Treat it as a directional signal, not ground truth.

## Output

```markdown
## LinkedIn Export Audit

### Files Found

### Current Profile Snapshot

### Searchability Issues

### Profile Conversion Issues

### Skills and Keyword Gaps

### CV vs LinkedIn Alignment

### Featured Proof Candidates

### Recommendations

### Data Limits
```
