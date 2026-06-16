# LinkedIn Export Processing Sub-Skill

Use this when the user provides `Complete_LinkedInDataExport.zip`, an unzipped LinkedIn export directory, or CSV files from LinkedIn's "Get a copy of your data" feature.

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

### 7. Ad Targeting / Inferences

If present, use as weak signal only. It may reveal how LinkedIn ad systems classify the user, but it is not a recruiter-ranking source of truth.

Use for:
- Detecting mismatch between desired positioning and platform-inferred categories
- Finding old industries or irrelevant interests polluting the user's market signal

Do not overfit to ad categories.

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
