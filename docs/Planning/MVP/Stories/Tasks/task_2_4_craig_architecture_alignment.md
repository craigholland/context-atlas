---
id: context-atlas-mvp-task-2-4-craig-architecture-alignment
title: Task 2.4 - Craig Architecture Alignment PR Plan
summary: Defines the PR sequence for keeping mixed-source support aligned with Craig Architecture boundaries.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, craig-architecture, sources, boundaries]
related:
  - ../story_2_shared_source_coverage.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.4 - Craig Architecture Alignment PR Plan

## Objective

Keep the multi-source expansion work aligned with Craig Architecture by ensuring semantics stay inward and source mechanics stay outward.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current and planned source adapters

## Proposed Work

### PR - A: Source-Boundary Audit

- inspect the current and planned source path for boundary leaks
- identify domain semantics currently embedded in adapters
- identify source-specific mechanics drifting inward

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/docs/filesystem.py`
- `src/context_atlas/adapters/records/structured.py`
- `src/context_atlas/domain/models/sources.py`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/domain/`

### PR - B: Boundary Refactor For Mixed Sources

- move leaked semantics into canonical domain structures or policies
- move source-family-specific parsing back outward into adapters
- preserve service orchestration as source-family-agnostic

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/docs/filesystem.py`
- `src/context_atlas/adapters/records/structured.py`
- `src/context_atlas/services/assembly.py`
- `src/context_atlas/domain/models/sources.py`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/domain/`
- `src/context_atlas/services/`
- `tests/`

### PR - C: Boundary Reinforcement

- update docs, examples, or local contracts to reflect the intended pattern
- add tests or examples that exercise mixed-source assembly without layer inversion
- ensure the MVP source path demonstrates the correct architecture

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `__ai__.md`
- `src/context_atlas/adapters/__ai__.md`
- `src/context_atlas/domain/__ai__.md`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/domain/`
- `src/context_atlas/services/`

## Sequencing

- audit first
- refactor second
- reinforce third

## Risks And Unknowns

- Mixed-source support may tempt the project into ad hoc convenience shortcuts.
- Some duplication may be acceptable temporarily during exploration but still needs clear direction of travel.
- Future adapters may reopen the same boundary issues unless the pattern is explicit.

## Exit Criteria

- mixed-source support remains aligned with Craig Architecture
- adapter logic and domain semantics are clearly separated
- the supported source-coverage path demonstrates the intended boundary model

## Related Artifacts

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Craig Architecture](../../../../Authoritative/Canon/Architecture/Craig-Architecture.md)

