---
id: context-atlas-agentic-task-8-3-codex-templates-and-creation-guidance
title: Task 8.3 - Codex Templates And Creation Guidance PR Plan
summary: Defines the PR sequence for creating the project-specific Codex templates and instructions used to materialize runtime assets.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, codex, templates]
related:
  - ../story_8_codex_materialization_for_context_atlas.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Identity/AgenticDevelopment/codex/folder_layout.md
supersedes: []
---

# Task 8.3 - Codex Templates And Creation Guidance PR Plan

## Objective

Define the concrete Codex templates and creation guidance that transform the abstract/project model into actual Codex runtime assets.

## Task Status

IMPLEMENTED

## Inputs

- [Story 8 - Codex Materialization For Context Atlas](../story_8_codex_materialization_for_context_atlas.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Codex Folder Layout](../../../../Authoritative/Identity/AgenticDevelopment/codex/folder_layout.md)
- the generic template model from Story 7

## Proposed Work

### PR - A: Codex Template Surface

- define which Codex-specific templates or template instructions the project needs
- keep the templates clearly subordinate to the generic template model
- make the creation path explicit enough for an AI contributor to follow repeatedly

#### Expected New Files
- `docs/Authoritative/Identity/AgenticDevelopment/codex/AGENTS.template.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/agent.template.toml`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/mode.template.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/skill.template.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/role.template.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/protocol.template.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`

#### Update AI files
- `.`

### PR - B: Creation Instructions

- define how a contributor should create or refresh Codex assets from the authoritative docs
- make it explicit what content is copied, adapted, or derived
- keep the instructions project-specific without turning them into the canon themselves

#### Expected New Files
- `docs/Authoritative/Identity/AgenticDevelopment/codex/creation_guidance.md`

#### Expected Existing Files Updated
- `docs/Authoritative/Identity/AgenticDevelopment/codex/README.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/AGENTS.template.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/skill.template.md`

#### Update AI files
- `.`

### PR - C: Story Reinforcement

- align Story 8 and Story 9 with the Codex template and creation model
- reduce the chance that future Codex assets are created ad hoc from memory
- document any template-generation questions that should wait for validation work

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`
- `docs/Planning/Agentic/Stories/story_9_validation_governance_and_drift_control.md`

#### Update AI files
- `.`

## Sequencing

- define the Codex template surface first
- define creation instructions second
- reinforce the Story layer third

## Risks And Unknowns

- Codex templates may drift away from the generic model if the relationship stays implicit.
- Creation guidance may become too procedural and lose the architectural rationale.
- Later validation may be hard if creation steps do not record what is derived from where.

## Exit Criteria

- Codex templates or template instructions exist
- Codex creation guidance is explicit
- later asset work can build on one repeatable Codex creation path

## Related Artifacts

- [Story 8 - Codex Materialization For Context Atlas](../story_8_codex_materialization_for_context_atlas.md)
- [Codex Folder Layout](../../../../Authoritative/Identity/AgenticDevelopment/codex/folder_layout.md)
