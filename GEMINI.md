# GxG RevOps Playbook - Gemini Instructions

Use the same shared project instructions as every other assistant.

Read order:

1. `README.md` for the project purpose and current coverage.
2. `PROJECT.md` for the project charter and criteria for what belongs in the collection.
3. `PROJECT_STRUCTURE.md` for how the repository is organized.
4. `.skills/MULTI_LLM_SKILLS_GUIDE.md` for the LM-agnostic skill architecture.
5. `.skills/revops/index.md` when the user wants to run or find a RevOps skill.
6. `.skills/revops-curator/index.md` when the user wants to add, import, audit, improve, stage, or deprecate skills.

Do not treat `GEMINI.md`, `AGENTS.md`, `.agents/`, or `.claude/` as the source of truth for skill behavior. They are adapters. Production skill behavior lives in the shared files they reference.
