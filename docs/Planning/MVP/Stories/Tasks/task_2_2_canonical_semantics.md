---
id: context-atlas-mvp-task-2-2-canonical-semantics
title: Task 2.2 - Canonical Semantics PR Plan
summary: Defines the PR sequence for keeping mixed-source semantics canonical and inward-owned.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, semantics, domain, sources]
related:
  - ../story_2_shared_source_coverage.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 2.2 - Canonical Semantics PR Plan

## Objective

Ensure that all supported source families converge into one shared semantic model inside the Atlas domain.

## Inputs

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- current `ContextSource` and provenance semantics

## Proposed Work

### PR - A: Canonical Mapping Rules

- define how documents and structured records map into source class, authority, durability, provenance, and intended use
- identify any missing canonical fields or normalization rules
- keep the canonical model provider-agnostic

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/sources.py`
- `src/context_atlas/domain/models/base.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/domain/`

### PR - B: Shared Semantics Helpers

- implement or refine inward helpers for repeated normalization and metadata freezing
- remove duplicated semantics from adapters where possible
- keep source-family-specific parsing outside the domain

#### Expected New Files
- `src/context_atlas/domain/models/source_semantics.py`

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/sources.py`
- `src/context_atlas/adapters/docs/filesystem.py`
- `src/context_atlas/adapters/records/structured.py`

#### Update AI files
- `.`
- `src/context_atlas/domain/`
- `src/context_atlas/adapters/`

### PR - C: Semantic Consistency Validation

- add tests or examples that compare semantics across source families
- verify that mixed-source packets carry coherent metadata and provenance
- ensure that adapter-specific quirks do not leak inward

#### Expected New Files
- `tests/test_source_semantics.py`

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/sources.py`
- `src/context_atlas/adapters/docs/filesystem.py`
- `src/context_atlas/adapters/records/structured.py`

#### Update AI files
- `.`
- `src/context_atlas/domain/`
- `src/context_atlas/adapters/`
- `tests/`

## Sequencing

- agree on mapping rules first
- consolidate semantics helpers second
- validate consistency last

## Risks And Unknowns

- It may be tempting to add source-family-specific fields to the canonical model.
- Provenance semantics may need refinement once more adapters exist.
- Semantic helper modules can become accidental junk drawers if not scoped carefully.

## Exit Criteria

- source semantics are shared across supported source families
- canonical semantics remain inward-owned
- mixed-source packets expose coherent source metadata

## Related Artifacts

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
