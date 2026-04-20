---
id: context-atlas-agentic-task-8-2-codex-folder-and-file-conventions
title: Task 8.2 - Codex Folder And File Conventions PR Plan
summary: Defines the PR sequence for mapping abstract agentic concepts onto Codex-discoverable folders and file surfaces.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, codex, folders]
related:
  - ../story_8_codex_materialization_for_context_atlas.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Identity/AgenticDevelopment/codex/README.md
supersedes: []
---

# Task 8.2 - Codex Folder And File Conventions PR Plan

## Objective

Define the folder and file conventions that let Codex discover materialized agentic assets without collapsing abstract concepts into one file type.

## Task Status

IMPLEMENTED

## Inputs

- [Story 8 - Codex Materialization For Context Atlas](../story_8_codex_materialization_for_context_atlas.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Codex Binding README](../../../../Authoritative/Identity/AgenticDevelopment/codex/README.md)
- the generic discovery and template models from Story 7

## Proposed Work

### PR - A: Codex Discovery Surface Mapping

- map abstract concepts like parent agents, specialists, skills, modes, and protocols onto Codex-discoverable surfaces
- keep the mapping explicit enough that later file creation is mechanical
- prevent Codex folder rules from being mistaken for the abstract model itself

#### Expected New Files
- `docs/Authoritative/Identity/AgenticDevelopment/codex/folder_layout.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`

#### Update AI files
- `.`

### PR - B: Naming Convention Rules

- define naming conventions for Codex folders and files
- make it explicit how the conventions satisfy Codex discovery while staying traceable to the abstract concepts
- prepare the later template Task to write concrete assets consistently

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Authoritative/Identity/AgenticDevelopment/codex/folder_layout.md`
- `docs/Authoritative/Identity/AgenticDevelopment/codex/README.md`

#### Update AI files
- `.`

### PR - C: Story Reinforcement

- align the generic and Codex Stories with the new folder and naming conventions
- ensure Story 8 continues to present Codex layout as derived from the generic model
- document any open questions reserved for the template-creation Task

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_7_platform_materialization_model.md`
- `docs/Planning/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md`

#### Update AI files
- `.`

## Sequencing

- map discovery surfaces first
- define naming conventions second
- reinforce the Story layer third

## Risks And Unknowns

- Codex folder rules may leak backward into the generic model if not bounded.
- Naming conventions may become inconsistent if not tied to abstract concepts clearly enough.
- Later asset-generation work may drift if this mapping is weak.

## Exit Criteria

- Codex folder and file conventions are explicit
- the conventions are traceable back to abstract concepts
- later asset-creation work can build on one stable layout model

## Related Artifacts

- [Story 8 - Codex Materialization For Context Atlas](../story_8_codex_materialization_for_context_atlas.md)
- [Codex Binding README](../../../../Authoritative/Identity/AgenticDevelopment/codex/README.md)
