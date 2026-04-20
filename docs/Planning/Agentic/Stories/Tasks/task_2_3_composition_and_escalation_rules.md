---
id: context-atlas-agentic-task-2-3-composition-and-escalation-rules
title: Task 2.3 - Composition And Escalation Rules PR Plan
summary: Defines the PR sequence for deciding when to add a skill, introduce a specialist, or keep responsibility parent-owned.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, composition, escalation]
related:
  - ../story_2_agent_and_skill_structure.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.3 - Composition And Escalation Rules PR Plan

## Objective

Define the decision rules for when a new need should be handled by adding a skill, introducing a specialist, or keeping the work parent-owned.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- the parent/specialist and skill contract work from Tasks 2.1 and 2.2

## Proposed Work

### PR - A: Composition Decision Record

- define the first-pass decision tree for skill addition, specialist creation, and parent-owned responsibility
- capture anti-patterns such as creating a specialist for every new work slice
- ensure the rules are project-usable without becoming runtime-specific

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Composition-Decision-Model.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_2_agent_and_skill_structure.md`

#### Update AI files
- `.`

### PR - B: Escalation And Return-Contract Constraints

- define the escalation conditions that should keep work parent-owned or return it to the parent
- tie composition decisions to bounded specialist authority and explicit return contracts
- prevent specialist sprawl by making escalation a first-class structural concern

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Escalation-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/AgenticDevelopment/Composition-Decision-Model.md`
- `docs/Authoritative/AgenticDevelopment/Delegation-Model.md`

#### Update AI files
- `.`

### PR - C: Story-Layer Reinforcement

- align the structural Story docs with the new decision rules
- make later role and protocol Stories assume the same escalation boundaries
- call out any unresolved cases that must be handled in later protocol work

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_2_agent_and_skill_structure.md`
- `docs/Planning/Agentic/Stories/story_3_context_atlas_role_model.md`
- `docs/Planning/Agentic/Stories/story_5_protocol_model.md`

#### Update AI files
- `.`

## Sequencing

- define the composition decision tree first
- bind escalation and return-contract constraints second
- reinforce downstream Story assumptions third

## Risks And Unknowns

- Specialist sprawl may still happen if the decision tree stays too soft.
- Parent-owned work may become overloaded if delegation triggers are underspecified.
- Escalation rules may drift into workflow-protocol concerns if structural boundaries are weak.

## Exit Criteria

- the skill vs specialist vs parent-owned decision rules are explicit
- escalation and return-contract constraints reinforce the composition model
- downstream Stories reference one stable structural decision model

## Related Artifacts

- [Story 2 - Agent And Skill Structure](../story_2_agent_and_skill_structure.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
