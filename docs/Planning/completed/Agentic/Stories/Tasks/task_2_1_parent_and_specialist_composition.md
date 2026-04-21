---
id: context-atlas-agentic-task-2-1-parent-and-specialist-composition
title: Task 2.1 - Parent And Specialist Composition PR Plan
summary: Defines the PR sequence for establishing the parent-versus-specialist structural model for Context Atlas agentic development.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, parent-agent, specialist]
related:
  - ../story_2_agent_and_skill_structure.md
  - ../../agentic_development_product_definition.md
  - ../../../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.1 - Parent And Specialist Composition PR Plan

## Objective

Define the structural difference between parent agents and specialist agents so delegation does not blur accountability or workflow ownership.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture](../../../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- the portable authority and glossary model from Story 1

## Proposed Work

### PR - A: Structural Boundary Decision

- define why Context Atlas uses parent agents plus specialists rather than a flat worker list
- identify the workflow responsibilities that must remain parent-owned
- document the scope limits that keep specialists bounded

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Delegation-Model.md`

#### Expected Existing Files Updated
- `docs/Planning/completed/Agentic/Stories/story_2_agent_and_skill_structure.md`

#### Update AI files
- `.`

### PR - B: Parent And Specialist Contract Shape

- define the expected contract shape for parent agents and specialist agents
- capture authority, entry conditions, escalation rules, and return-contract differences
- prevent specialist definitions from growing into alternate parent agents

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Agent-Composition-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/Canon/AgenticDevelopment/Agent-Authority-Model.md`
- `docs/Authoritative/Canon/AgenticDevelopment/Delegation-Model.md`

#### Update AI files
- `.`

### PR - C: Structural Reinforcement

- align Story docs and canon wording around the parent-versus-specialist boundary
- ensure later role and protocol work inherits the same structural assumptions
- call out any remaining ambiguity that must be resolved before role binding begins

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/completed/Agentic/Stories/story_2_agent_and_skill_structure.md`
- `docs/Planning/completed/Agentic/Stories/story_3_context_atlas_role_model.md`
- `docs/Planning/completed/Agentic/Stories/story_5_protocol_model.md`

#### Update AI files
- `.`

## Sequencing

- define the boundary first
- define the contract shape second
- reinforce the structure across downstream Stories third

## Risks And Unknowns

- Specialists may inherit too much lifecycle authority if parent boundaries stay vague.
- A flat-worker mental model may still leak in if the parent contract is underspecified.
- Later protocol work may reintroduce ambiguity if the structural model is not reinforced early.

## Exit Criteria

- the parent-versus-specialist boundary is explicit
- contract differences between parent and specialist agents are documented
- later Stories can build on a stable delegation structure

## Related Artifacts

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)

