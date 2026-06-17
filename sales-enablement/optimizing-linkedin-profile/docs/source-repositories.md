# External Repositories and Prior Art

Use these as inspiration and implementation references. Do not copy blindly; adapt to the user's audience and facts.

## Recommended Base References

### dan323 / cv-linkedin

URL: <https://github.com/dan323/easier-life-skills/tree/master/plugins/cv-linkedin>

Use for:
- CV plus official LinkedIn export workflow
- Structured reading of `Profile.csv`, `Positions.csv`, `Education.csv`, `Skills.csv`
- LinkedIn headline, About, Experience, Skills, CV alignment
- Career-oriented profile improvement

Limits:
- Primarily software/PM/engineering-role oriented.
- Needs expansion for RevOps, B2B sales, founder, consultant, and social-selling use cases.

### dbhat93 / job-search-os

URL: <https://github.com/dbhat93/job-search-os>

Use for:
- Career-search system thinking
- Job-search workflows beyond profile rewrite
- Networking, referral, and target-role discipline

Limits:
- Broader job-search workflow, not a LinkedIn export-first profile skill.

### BrianRWagner / ai-marketing-claude-code-skills

URL: <https://github.com/BrianRWagner/ai-marketing-claude-code-skills>

Use for:
- B2B sales and profile-positioning layer
- LinkedIn profile optimizer
- Authority building
- Cold outreach sequence
- Case study and testimonial workflows

Limits:
- Less career-counseling depth.
- Not centered on LinkedIn export processing.

### abhijayarora93 / linkedin-crm-skill

URL: <https://github.com/abhijayarora93/linkedin-crm-skill>

Use for:
- LinkedIn connections/messages/invitations as a networking and CRM surface
- Warm paths, referral targets, DM drafts, relationship activation

Limits:
- Not a profile optimization system.
- Better as a post-profile outbound/networking sub-skill.

### agentkit-seo / agentkit-seo

URL: <https://github.com/agentkit-seo/agentkit-seo>

Use for:
- AI/search discoverability framing
- Cross-surface profile consistency: LinkedIn, CV, GitHub, portfolio
- Evidence-based professional presence

Limits:
- Not specific to LinkedIn export or B2B LinkedIn sales.

### cosmo-hg / LinkedIn-Profile-Optimization-Prompts

URL: <https://github.com/cosmo-hg/Linkedin-Profile-Optimization-Prompts>

Use for:
- **Perceived Identity analysis** — auditing `Ad_Targeting.csv` and `Inferences_about_you.csv` to reveal how LinkedIn's algorithm categorizes the user before any rewrite.
- **Two-phase chained workflow**: Phase 1 Audit (open Claude Code in export folder) → Phase 2 Rebuild (add resume, generate full rewrites).
- **Dot-separated headline formula**: `[Role] | [Keyword] · [Keyword] · [Keyword] | [Credibility anchor]`.
- **10 exact skills per experience role** using LinkedIn's official skill nomenclature.
- **2026 content strategy**: 4 post concepts, 3 high-performing formats, daily algorithmic training tactics.
- **Specific certification recommendations** with providers and relevance justification.

Adapted: 2026-06-17
Changes: Extracted the workflow, Perceived Identity concept, and headline/skills guidelines; integrated into `linkedin-export-processing.md`, `profile-section-guide.md`, and `checklists-and-prompts.md`. Generalized away from single-LLM (Claude) framing.

## Useful but Secondary

### juanmanueldaza / linkedin2md

URL: <https://github.com/juanmanueldaza/linkedin2md>

Use for:
- Converting `Complete_LinkedInDataExport.zip` into Markdown/PDF before LLM analysis.

Limits:
- Utility only, not a strategy or rewrite skill.

### Michael Banks LinkedIn Export AI Profile Skill

URL: <https://www.michaelbanks.org/blog/linkedin-export-ai-profile-skill>

Use for:
- Turning LinkedIn export into AI profile, speaker sheet, and narrative assets.
- Privacy-aware profile narrative workflow.

Limits:
- Article/workflow, not necessarily a full open repository.

### sickn33 linkedin-profile-optimizer

URL: <https://github.com/sickn33/antigravity-awesome-skills/blob/main/skills/linkedin-profile-optimizer/SKILL.md>

Use for:
- Simple profile optimizer reference.

Limits:
- Generic; less export-aware and less strategic.

### davila7 linkedin-profile-optimizer

URL: <https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/linkedin-profile-optimizer/SKILL.md>

Use for:
- Claude Code template reference.

Limits:
- Generic profile optimization; not a complete LinkedIn profile workflow.

## Design Decision for This Skill

This skill combines:
- `cv-linkedin` style export/CV structure
- `job-search-os` style career operating discipline
- B2B authority and outreach patterns from marketing skills
- LinkedIn Recruiter and Reddit 2026 research
- A concrete after-update plan so the user knows what to do after the profile is rewritten
