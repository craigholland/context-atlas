---
id: context-atlas-mvp-task-3-3-architectural-shape
title: Task 3.3 - Architectural Shape PR Plan
summary: Defines the PR sequence for keeping the Codex repository workflow aligned with Atlas architecture rather than turning it into a special-case engine.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, codex, architecture, boundaries]
related:
  - ../story_3_codex_repository_workflow.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 3.3 - Architectural Shape PR Plan

## Objective

Ensure the Codex repository workflow remains a thin reference experience built on the shared Atlas engine, not a forked workflow engine.

## Task Status

WORKING

## Inputs

- [Story 3 - Codex Repository Workflow](../story_3_codex_repository_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- outputs from Tasks 3.1 and 3.2

## Proposed Work

### PR - A: Workflow Boundary Audit

- inspect the Codex workflow composition for wrong-layer logic
- identify repo-specific decisions that should remain at the composition boundary
- ensure Codex-facing presentation is not leaking into canonical domain objects

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/run.py`
- `src/context_atlas/rendering/context.py`
- `src/context_atlas/services/assembly.py`

#### Update AI files
- `.`
- `src/context_atlas/rendering/`
- `src/context_atlas/services/`

### PR - B: Boundary-Conforming Refactor

- move any misplaced logic back into adapters, services, infrastructure, or rendering as appropriate
- keep the shared assembly engine provider-agnostic
- preserve the packet and trace as the workflow's authoritative outputs

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/run.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/rendering/context.py`
- `src/context_atlas/services/assembly.py`

#### Update AI files
- `.`
- `src/context_atlas/services/`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/rendering/`
- `tests/`

### PR - C: Workflow Architecture Reinforcement

- update docs or local contracts so the workflow teaches the right architecture
- add focused checks or examples where boundary drift is likely
- ensure the flagship workflow reinforces, rather than contradicts, Craig Architecture

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `__ai__.md`
- `src/context_atlas/services/__ai__.md`
- `src/context_atlas/rendering/__ai__.md`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/services/`
- `src/context_atlas/rendering/`
- `src/context_atlas/infrastructure/`

## Sequencing

- audit first
- refactor second
- reinforce docs and contracts third

## Risks And Unknowns

- Codex-specific convenience paths may pressure the project toward one-off abstractions.
- Example code is especially prone to boundary shortcuts.
- Product polish can mask architecture drift unless reviewed deliberately.

## Exit Criteria

- the Codex repository workflow uses the shared engine
- Codex-specific concerns stay at the outer boundary
- the workflow remains aligned with Craig Architecture

## Related Artifacts

- [Story 3 - Codex Repository Workflow](../story_3_codex_repository_workflow.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
