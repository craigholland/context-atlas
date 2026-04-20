---
id: context-atlas-agentic-story-3-context-atlas-role-model
title: Story 3 - Context Atlas Role Model
summary: Defines the project-specific role model for Context Atlas, including role accountabilities, ownership boundaries, and the initial named role set.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, roles, accountability, governance]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ./story_2_agent_and_skill_structure.md
  - ../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md
  - ../../../Authoritative/AgenticDevelopment/Agent-Authority-Model.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
supersedes: []
---

# Story 3 - Context Atlas Role Model

## Objective

Define the Context Atlas project-specific role model so the repository has a
clear answer for who is accountable for planning, backend delivery, frontend
delivery, QA review, and DevOps-oriented operational work, while keeping it
explicit that a role is the accountability concept embodied by a parent agent
rather than the runtime actor itself.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 2 - Agent And Skill Structure](./story_2_agent_and_skill_structure.md)
- [Agentic Development Glossary](../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md)
- [Agent Authority Model](../../../Authoritative/AgenticDevelopment/Agent-Authority-Model.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- Current repo delivery expectations around planning, implementation, review, merge, and release work

## Proposed Tasks

### Task 1: Initial Role Set

- define the initial Context Atlas top-level roles:
  - Planner/Decomp
  - Backend
  - Frontend
  - QA
  - DevOps
- explain why those roles exist as distinct project accountabilities instead of
  falling back to a generic implementation role
- keep the role set small enough to govern clearly at the MVP stage

### Task 2: Role Accountabilities And Ownership

- define what each role is primarily responsible for
- identify which artifacts and decisions each role may own directly
- make it explicit that specialists do not define an alternate project role set
  and instead operate as bounded delegates under parent-agent accountability
- ensure the role model reflects real repository work rather than aspirational
  job titles

### Task 3: Role Authority Boundaries

- define which roles may:
  - decompose work
  - implement changes
  - request or perform review
  - approve merge/release actions
  - own operational workflow changes
- make the role-level authority boundaries explicit before protocol docs define
  the workflow sequences that use them

### Task 4: Role Binding To Agent Structure

- map the project role model onto the structural agent-and-skill model from
  Story 2
- keep the distinction explicit between:
  - a role as project accountability
  - a parent agent as the runtime/materialized actor that embodies that role
  - a specialist as a bounded delegate rather than a parallel role definition
- position later mode and protocol stories to reference roles without
  redefining them

## Sequencing

- define the initial role set and why it exists
- assign core accountabilities and ownership expectations
- lock the authority boundaries between roles
- bind the role model to the agent structure without yet materializing it into
  runtime files

## Risks And Unknowns

- Role docs could collapse into workflow protocols if they start describing too
  much sequence instead of accountability.
- The role model could drift into runtime implementation details if it starts
  naming vendor-specific artifacts too early.
- DevOps responsibilities could remain ambiguous if merges, workflow changes,
  and release actions are not clearly separated from ordinary implementation.

## Exit Criteria

- Context Atlas has a documented project-specific role set
- each role has clear accountabilities and ownership expectations
- the distinction between role, parent agent, and specialist is explicit
- authority boundaries between planning, implementation, QA, and DevOps are
  explicit
- later stories can reference roles as stable project concepts

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the role model stays project-specific without absorbing runtime-specific file
  conventions
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives `@codex review`, and any review findings are
  resolved on that same feature branch before human merge
- any role-to-agent mapping introduced by the Story preserves the distinction
  between project accountability and runtime materialization

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 2 - Agent And Skill Structure](./story_2_agent_and_skill_structure.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
