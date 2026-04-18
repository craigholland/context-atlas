---
id: context-atlas-mvp-task-1-1-supported-entry-surface
title: Task 1.1 - Supported Entry Surface PR Plan
summary: Defines the PR sequence for stabilizing the supported public entry surface for Context Atlas MVP users.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, api, surface]
related:
  - ../story_1_engine_to_product_surface.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 1.1 - Supported Entry Surface PR Plan

## Objective

Define and stabilize the public package entry surface that a new MVP user should reach for first.

## Inputs

- [Story 1 - Engine To Product Surface](../story_1_engine_to_product_surface.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- current exports under `src/context_atlas/`

## Proposed Work

### PR - A: Public API Inventory And Supported-Surface Decision

- inventory current imports that a new user must reach for
- decide which imports are intentionally public for the MVP
- identify deep-import paths that should become unnecessary

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `README.md`
- `src/context_atlas/__init__.py`
- `src/context_atlas/infrastructure/assembly.py`

#### Update AI files
- `.`
- `src/context_atlas/`
- `src/context_atlas/infrastructure/`

### PR - B: Export And Entry-Surface Tightening

- update package exports and supported starter entrypoints
- make the starter composition path discoverable from the package root or a clear top-level namespace
- keep provider-specific and adapter-specific mechanics out of the public surface unless they are intentionally supported

#### Expected New Files
- `src/context_atlas/api.py`

#### Expected Existing Files Updated
- `src/context_atlas/__init__.py`
- `src/context_atlas/adapters/__init__.py`
- `src/context_atlas/infrastructure/assembly.py`
- `tests/test_bootstrap_layers.py`

#### Update AI files
- `.`
- `src/context_atlas/`
- `src/context_atlas/adapters/`
- `src/context_atlas/infrastructure/`
- `tests/`

### PR - C: Golden-Path Consumption Cleanup

- update examples and usage docs to consume the supported public API
- remove or de-emphasize internal import paths in user-facing materials
- verify that the public path is sufficient for the starter MVP flow

#### Expected New Files
- `examples/starter_api_smoke.py`

#### Expected Existing Files Updated
- `README.md`
- `examples/README.md`
- `src/context_atlas/api.py`

#### Update AI files
- `.`
- `src/context_atlas/`
- `tests/`

## Sequencing

- decide the intended public surface first
- update exports second
- migrate docs and examples last so they validate the new shape

## Risks And Unknowns

- Over-exporting internal modules too early may freeze weak package boundaries.
- Under-exporting can leave the product surface hard to discover.
- There may be tension between convenience imports and preserving clear layer semantics.

## Exit Criteria

- the package has a clear supported entry surface
- the MVP starter flow can be assembled without arbitrary deep imports
- examples and guides use the same supported imports

## Related Artifacts

- [Story 1 - Engine To Product Surface](../story_1_engine_to_product_surface.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
