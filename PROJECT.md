# GxG RevOps Playbook — Project Charter

This file defines what this repository collects and how to decide whether something belongs here.

This is not the taxonomy. Folder structure, naming rules, metadata, and audit checks live in [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [.skills/revops-curator/taxonomy.md](.skills/revops-curator/taxonomy.md).

---

## Purpose

This repository collects reusable Revenue Operations workflows for AI agents.

The goal is to make recurring RevOps work executable: an agent should be able to take a business request, ask for the missing inputs, apply the right process, and produce a concrete output.

This is not a knowledge base for general RevOps theory. It is a playbook for repeated execution.

## What Belongs Here

Add a workflow when it helps an agent perform a recurring RevOps task better than a generic answer.

Good candidates are workflows that:

- produce a concrete artifact, decision, analysis, recommendation, or operating plan
- encode a repeatable process, not a one-time answer
- include enough context, examples, rules, or templates for an agent to execute without guessing
- reduce repeated explanation between a human and an agent
- improve consistency across similar tasks
- can be maintained as the team learns

Examples of valid material:

- a pipeline review workflow
- a forecast inspection checklist
- a lead scoring method
- a CRM data audit process
- a dashboard definition framework
- a QBR preparation workflow
- a pricing exception review process
- a business case writing workflow

## What Does Not Belong

Do not add material that is only:

- generic RevOps advice
- a prompt with no reusable process
- a copy of vendor documentation
- a one-off project note
- a private customer data dump
- an idea with no clear user, input, or output
- a workflow so broad that it cannot be executed
- a workflow so narrow that it will not be reused

If the idea is useful but unfinished, put it in `_staging/`. Do not call it a production skill.

## Standard For A Good Workflow

A good workflow answers these questions:

| Question | Required Answer |
|----------|-----------------|
| When should it run? | Clear trigger or user request. |
| What inputs does it need? | Required and optional inputs are explicit. |
| What should it produce? | Output format is concrete. |
| What process should it follow? | Steps are specific enough to execute. |
| What judgment should it apply? | Rules, criteria, examples, or scoring logic are stated. |
| What is out of scope? | Boundaries prevent misuse. |

If a workflow does not answer these, it is not ready.

## Ideal Collection

The ideal collection covers the recurring work needed to operate a revenue system:

- pipeline and forecasting
- demand generation
- sales enablement
- CRM and data operations
- revenue analytics
- customer success operations
- revenue technology
- pricing and packaging
- territory and quota
- marketing operations

Coverage is useful, but quality matters more. Ten strong workflows are better than fifty generic ones.

## Good Result

The project is in good shape when:

- users can ask for a RevOps outcome in plain language
- the agent can route the request to the right workflow
- active workflows produce useful outputs with little extra prompting
- repeated work becomes faster and more consistent
- unfinished ideas are kept in staging, not mixed with production workflows
- duplicate and generic ideas are rejected or merged
- the repository stays understandable to a new human or agent reading it for the first time

## Decision Rule

Before adding anything, answer:

1. What recurring RevOps task does this improve?
2. Who will use the output?
3. What input does the agent need?
4. What output should the agent produce?
5. What rules or examples make this better than a generic response?
6. Will this be useful again after the current conversation ends?

If the answers are strong, make it a skill. If the answers are incomplete, stage it. If the answers are weak, do not add it.
