---
id: context-atlas-mvp-task-2-1-source-families
title: Task 2.1 - Source Families PR Plan
summary: Defines the PR sequence for supporting multiple source families through one Atlas governance model.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, sources, adapters]
related:
  - ../story_2_shared_source_coverage.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Identity/Context-Atlas-System-Model.md
supersedes: []
---

# Task 2.1 - Source Families PR Plan

## Objective

Extend Atlas beyond filesystem documents so the MVP clearly supports more than one source family.

## Task Status

WORKING

## Inputs

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- current filesystem docs adapter

## Proposed Work

### PR - A: Structured-Record Source Contract

- define the minimum structured-record shape Atlas needs to support
- decide which record metadata is required to produce canonical sources
- keep the contract small enough to work across multiple integration styles

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/__init__.py`
- `src/context_atlas/domain/models/sources.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/domain/`

### PR - B: Structured-Record Adapter Implementation

- implement an adapter or adapter-ready ingestion surface for record-backed sources
- convert records into canonical `ContextSource` artifacts
- preserve provenance and intended-use metadata

#### Expected New Files
- `src/context_atlas/adapters/records/__init__.py`
- `src/context_atlas/adapters/records/structured.py`
- `tests/test_record_source_adapter.py`

#### Expected Existing Files Updated
- `src/context_atlas/adapters/__init__.py`
- `src/context_atlas/domain/models/sources.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Mixed-Source Validation

- validate that documents and structured records can coexist in one registry and packet flow
- add examples or tests that prove the shared path
- ensure source-family differences remain outward concerns

#### Expected New Files
- `examples/mixed_source_registry.py`

#### Expected Existing Files Updated
- `src/context_atlas/adapters/retrieval/lexical.py`
- `tests/test_record_source_adapter.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `tests/`

## Sequencing

- define the structured-record contract first
- implement the adapter second
- validate mixed-source use last

## Risks And Unknowns

- The record contract may become too specific to one database style.
- Provenance fields for records may require iteration once real examples exist.
- Mixed-source retrieval may expose assumptions that were hidden in docs-only flows.

## Exit Criteria

- Atlas supports at least two source families
- structured records can become canonical sources
- mixed-source packets can be assembled through the shared engine

## Related Artifacts

- [Story 2 - Shared Source Coverage](../story_2_shared_source_coverage.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
