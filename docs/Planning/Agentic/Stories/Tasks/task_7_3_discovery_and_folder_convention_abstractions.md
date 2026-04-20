---
id: context-atlas-agentic-task-7-3-discovery-and-folder-convention-abstractions
title: Task 7.3 - Discovery And Folder Convention Abstractions PR Plan
summary: Defines the PR sequence for separating abstract runtime-discovery needs from platform-specific folder conventions.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, discovery, folders]
related:
  - ../story_7_platform_materialization_model.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/AgenticDevelopment/Template-Model.md
supersedes: []
---

# Task 7.3 - Discovery And Folder Convention Abstractions PR Plan

## Objective

Define abstract runtime-discovery needs without prematurely coupling them to Codex or any other platform’s folder conventions.

## Task Status

PLANNED

## Inputs

- [Story 7 - Platform Materialization Model](../story_7_platform_materialization_model.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Template Model](../../../../Authoritative/AgenticDevelopment/Template-Model.md)
- the materialization and boundary work from Tasks 7.1 and 7.2

## Proposed Work

### PR - A: Abstract Discovery Model

- define what a runtime needs to discover in order to use materialized agentic assets
- keep discovery requirements abstract and vendor-neutral
- separate discovery concepts from any concrete folder names

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Discovery-Model.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_7_platform_materialization_model.md`

#### Update AI files
- `.`

### PR - B: Folder-Convention Abstraction Rules

- define how abstract discovery needs may later map to platform-specific folder conventions
- make it explicit what belongs in the generic materialization model versus later platform stories
- reduce the chance that Codex-specific folder shapes leak backward into Story 7

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Authoritative/AgenticDevelopment/Discovery-Model.md`
- `docs/Authoritative/AgenticDevelopment/Template-Model.md`
- `docs/Authoritative/AgenticDevelopment/Platform-Materialization-Model.md`

#### Update AI files
- `.`

### PR - C: Story Reinforcement

- align Story 7 and Story 8 with the discovery abstraction model
- make later platform work explicitly downstream of this abstraction layer
- document any discovery questions that should remain platform-specific

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_7_platform_materialization_model.md`
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`
- `docs/Planning/Agentic/Stories/story_9_validation_governance_and_drift_control.md`

#### Update AI files
- `.`

## Sequencing

- define abstract discovery needs first
- define folder-convention abstraction rules second
- reinforce Story usage third

## Risks And Unknowns

- Discovery may become too vague if the abstraction is not concrete enough.
- Folder conventions may still leak into the generic layer if boundary rules stay weak.
- Later platform stories may misread the abstraction if Story reinforcement is inconsistent.

## Exit Criteria

- abstract discovery needs are documented
- the boundary between discovery abstractions and folder conventions is explicit
- later platform stories can bind to one discovery model

## Related Artifacts

- [Story 7 - Platform Materialization Model](../story_7_platform_materialization_model.md)
- [Template Model](../../../../Authoritative/AgenticDevelopment/Template-Model.md)
