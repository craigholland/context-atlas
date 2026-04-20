---
id: context-atlas-agentic-task-2-2-skill-contract-and-attachment-model
title: Task 2.2 - Skill Contract And Attachment Model PR Plan
summary: Defines the PR sequence for treating skills as atomic reusable units and for specifying how they attach to parent and specialist agents.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, skills, composition]
related:
  - ../story_2_agent_and_skill_structure.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.2 - Skill Contract And Attachment Model PR Plan

## Objective

Define skills as the atomic reusable unit of agentic capability and specify how skills attach to parent and specialist agents without becoming alternate role or protocol definitions.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- the portable glossary and authority model from Story 1

## Proposed Work

### PR - A: Skill Contract Definition

- define what a skill may and may not contain
- make it explicit that skills are atomic reusable procedures or knowledge packs
- prevent skill docs from silently absorbing role, mode, or protocol responsibilities

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Skill-Contract.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_2_agent_and_skill_structure.md`

#### Update AI files
- `.`

### PR - B: Skill Attachment And Consumption Model

- define how parent agents and specialists attach to and consume skills
- clarify whether skills are mandatory, optional, or contextual for an agent definition
- make attachment rules portable enough to survive later platform materialization

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Skill-Attachment-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/AgenticDevelopment/Skill-Contract.md`
- `docs/Authoritative/AgenticDevelopment/Agent-Composition-Model.md`

#### Update AI files
- `.`

### PR - C: Structural Reinforcement

- align downstream Story docs so they consistently treat skills as atomic units
- reduce the chance that later role, mode, or Codex materialization work redefines skills
- identify any remaining ambiguous boundary cases for later Task planning

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_2_agent_and_skill_structure.md`
- `docs/Planning/Agentic/Stories/story_5_protocol_model.md`
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`

#### Update AI files
- `.`

## Sequencing

- define the skill contract first
- define attachment and consumption rules second
- reinforce downstream usage assumptions third

## Risks And Unknowns

- Skills may become oversized if the atomic-unit concept is not enforced.
- Attachment rules may become platform-shaped too early.
- Later platform materialization may misinterpret skills if the portable contract is weak.

## Exit Criteria

- the skill contract is explicit
- the attachment model for parent and specialist agents is defined
- later Stories consistently treat skills as atomic reusable units

## Related Artifacts

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
