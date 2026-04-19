---
id: context-atlas-mvp-task-2-3-adapter-shape
title: Task 2.3 - Adapter Shape PR Plan
summary: Defines the PR sequence for shaping MVP source adapters without turning Atlas into a database or connector framework.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, adapters, database, records]
related:
  - ../story_2_shared_source_coverage.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.3 - Adapter Shape PR Plan

## Objective

Design the adapter shape for non-document sources so Atlas remains a governance engine rather than a general-purpose data-access framework.

## Task Status

PLANNED

## Inputs

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- evolving structured-record adapter work

## Proposed Work

### PR - A: Adapter-Boundary Decision

- decide whether Atlas adapters should accept raw rows, normalized records, or both
- define what stays outside Atlas in application-specific integration code
- keep the adapter boundary narrow and testable

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/records/structured.py`
- `README.md`
- `examples/README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`

### PR - B: MVP Adapter Implementation Pattern

- implement the chosen adapter shape for the MVP
- add clear examples of how application code should feed data into Atlas
- avoid coupling the adapter directly to one DB or vector-store client

#### Expected New Files
- `src/context_atlas/adapters/records/mappers.py`
- `tests/test_record_adapter_shape.py`

#### Expected Existing Files Updated
- `src/context_atlas/adapters/records/structured.py`
- `src/context_atlas/adapters/__init__.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `tests/`

### PR - C: Adapter Guidance And Guardrails

- document how to build future adapters without violating the boundary
- add focused checks or examples that discourage turning Atlas into a query framework
- keep the outward/inward separation legible in examples

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `README.md`
- `examples/mixed_source_registry.py`
- `src/context_atlas/adapters/records/__init__.py`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`

## Sequencing

- decide the boundary first
- implement the MVP pattern second
- document and reinforce the boundary third

## Risks And Unknowns

- A too-flexible adapter contract can become vague and hard to govern.
- A too-rigid adapter contract may not fit multiple future data sources.
- Integration examples may pressure Atlas toward owning too much database logic.

## Exit Criteria

- the adapter shape is clear and documented
- Atlas accepts structured records without becoming a data-access framework
- future adapter work has a legible pattern to follow

## Related Artifacts

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
