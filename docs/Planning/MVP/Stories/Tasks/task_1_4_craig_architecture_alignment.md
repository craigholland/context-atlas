---
id: context-atlas-mvp-task-1-4-craig-architecture-alignment
title: Task 1.4 - Craig Architecture Alignment PR Plan
summary: Defines the PR sequence for keeping Story 1 product-surface changes aligned with Craig Architecture.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, craig-architecture, boundaries]
related:
  - ../story_1_engine_to_product_surface.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 1.4 - Craig Architecture Alignment PR Plan

## Objective

Ensure that MVP-facing product-surface work strengthens, rather than erodes, the project’s Craig Architecture boundaries.

## Inputs

- [Story 1 - Engine To Product Surface](../story_1_engine_to_product_surface.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- current layer responsibilities across `domain`, `services`, `infrastructure`, and `rendering`

## Proposed Work

### PR - A: Boundary Audit For MVP Surface Changes

- review current MVP-facing modules for boundary leaks
- identify where convenience or examples are encouraging wrong-layer behavior
- decide which issues must be corrected during Story 1

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/__init__.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/rendering/context.py`

#### Update AI files
- `.`
- `src/context_atlas/`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/rendering/`

### PR - B: Refactor Product-Surface Boundary Violations

- move misplaced orchestration, formatting, or configuration behavior back to the correct layer
- keep derived views in `rendering/` and canonical state in `domain/`
- preserve inward dependency direction throughout

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/assembly.py`
- `src/context_atlas/services/assembly.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/rendering/context.py`

#### Update AI files
- `.`
- `src/context_atlas/domain/`
- `src/context_atlas/services/`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/rendering/`
- `tests/`

### PR - C: Contract And Guidance Reinforcement

- update local guidance or planning docs where needed
- ensure the supported MVP path demonstrates the intended architecture rather than bypassing it
- add focused validation where architecture drift is likely

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `__ai__.md`
- `src/context_atlas/__ai__.md`
- `src/context_atlas/rendering/__ai__.md`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/`
- `src/context_atlas/rendering/`
- `tests/`

## Sequencing

- audit first
- refactor second
- reinforce contracts and guidance last

## Risks And Unknowns

- Convenience-oriented product work may pressure the project toward shortcuts that later harden into design debt.
- Some current starter paths may already be slightly more exploratory than ideal.
- Over-correcting too early can add unnecessary surface complexity.

## Exit Criteria

- Story 1 changes remain aligned with Craig Architecture
- no new MVP-facing boundary leaks are introduced
- the supported surface demonstrates the intended layer model

## Related Artifacts

- [Story 1 - Engine To Product Surface](../story_1_engine_to_product_surface.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
