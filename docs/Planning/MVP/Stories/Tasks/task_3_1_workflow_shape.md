---
id: context-atlas-mvp-task-3-1-workflow-shape
title: Task 3.1 - Workflow Shape PR Plan
summary: Defines the PR sequence for shaping the flagship Codex repository workflow around the shared Atlas engine.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, codex, workflow, repository]
related:
  - ../story_3_codex_repository_workflow.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 3.1 - Workflow Shape PR Plan

## Objective

Define and implement the actual flow of the Codex repository workflow so it uses the shared Atlas engine rather than ad hoc demo logic.

## Task Status

PLANNED

## Inputs

- [Story 3 - Codex Repository Workflow](../story_3_codex_repository_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- current filesystem docs adapter and starter assembly service

## Proposed Work

### PR - A: Reference Workflow Definition

- choose the supported repository inputs for the Codex workflow
- define the minimal composition path from governed repo artifacts to packet assembly
- keep repo-specific wiring outside the canonical engine

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `README.md`
- `examples/README.md`
- `src/context_atlas/infrastructure/assembly.py`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`

### PR - B: Workflow Example Implementation

- implement the example composition path for the Codex repository workflow
- ensure the flow produces a packet, trace, and rendered context
- keep the example close to the supported public API

#### Expected New Files
- `examples/codex_repository_workflow/README.md`
- `examples/codex_repository_workflow/run.py`

#### Expected Existing Files Updated
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/rendering/context.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/rendering/`
- `tests/`

### PR - C: Workflow Validation

- validate the workflow against realistic engineering questions
- capture packet and trace output for sanity checking
- refine the composition path if the result still feels like a demo instead of a supported flow

#### Expected New Files
- `tests/test_codex_repository_workflow.py`

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/run.py`
- `src/context_atlas/services/assembly.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/services/`
- `tests/`

## Sequencing

- define the reference workflow first
- implement the example second
- validate and refine the workflow third

## Risks And Unknowns

- A single reference repository shape may not generalize perfectly.
- The example may become too customized if repo assumptions are not made explicit.
- Workflow validation may expose missing product-surface work from Story 1.

## Exit Criteria

- the Codex repository workflow has a concrete supported shape
- it produces packet, trace, and rendered context through the shared engine
- the flow is recognizable as a real integration path rather than demo glue

## Related Artifacts

- [Story 3 - Codex Repository Workflow](../story_3_codex_repository_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
