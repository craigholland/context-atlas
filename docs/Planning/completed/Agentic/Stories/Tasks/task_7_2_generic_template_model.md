---
id: context-atlas-agentic-task-7-2-generic-template-model
title: Task 7.2 - Generic Template Model PR Plan
summary: Defines the PR sequence for establishing the platform-agnostic template surfaces used for later runtime materialization.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, templates, materialization]
related:
  - ../story_7_platform_materialization_model.md
  - ../../agentic_development_product_definition.md
  - ../../../../../Authoritative/Canon/AgenticDevelopment/Platform-Materialization-Model.md
supersedes: []
---

# Task 7.2 - Generic Template Model PR Plan

## Objective

Define the generic template surfaces used to represent agents, skills, modes, protocols, and related runtime guidance before any platform-specific binding is introduced.

## Task Status

IMPLEMENTED

## Inputs

- [Story 7 - Platform Materialization Model](../story_7_platform_materialization_model.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Platform Materialization Model](../../../../../Authoritative/Canon/AgenticDevelopment/Platform-Materialization-Model.md)
- the materialization-boundary model from Task 7.1

## Proposed Work

### PR - A: Template Surface Inventory

- identify the generic template surfaces the project needs
- keep the surfaces abstract enough to map into multiple runtime environments
- avoid baking any vendor folder conventions into the template layer

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Template-Model.md`

#### Expected Existing Files Updated
- `docs/Planning/completed/Agentic/Stories/story_7_platform_materialization_model.md`

#### Update AI files
- `.`

### PR - B: Template Contracts

- define what information each generic template type must carry
- tie the template contracts back to the role, mode, protocol, and skill models
- keep templates traceable to the upstream canon and project bindings

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Templates/README.md`

#### Expected Existing Files Updated
- `docs/Authoritative/Canon/AgenticDevelopment/Template-Model.md`
- `docs/Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md`

#### Update AI files
- `.`

### PR - C: Story Reinforcement

- align the platform-materialization and Codex Stories with the generic template model
- document any template questions that should remain platform-specific later
- reduce the chance that runtime bindings invent alternate generic template shapes

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/completed/Agentic/Stories/story_7_platform_materialization_model.md`
- `docs/Planning/completed/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`

#### Update AI files
- `.`

## Sequencing

- inventory template surfaces first
- define the template contracts second
- reinforce Story usage third

## Risks And Unknowns

- Template surfaces may become too abstract to use if they are not concrete enough.
- The template layer may become platform-shaped if folder conventions leak into it.
- Later runtime bindings may invent duplicate templates if the generic model is weak.

## Exit Criteria

- the generic template model exists
- template contracts are explicit and traceable to the canon
- later platform stories can bind to one template surface instead of inventing their own

## Related Artifacts

- [Story 7 - Platform Materialization Model](../story_7_platform_materialization_model.md)
- [Platform Materialization Model](../../../../../Authoritative/Canon/AgenticDevelopment/Platform-Materialization-Model.md)

