---
id: context-atlas-mvp-story-2-shared-source-coverage
title: Story 2 - Shared Source Coverage
summary: Defines how Context Atlas should support more than one source family while preserving one canonical governance model.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, story, sources, adapters, records]
related:
  - ../mvp_product_defintiion.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 2 - Shared Source Coverage

## Objective

Prove that Context Atlas governs multiple source families through one canonical source model rather than behaving like a docs-only engine.

## Inputs

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
- current filesystem docs adapter in `adapters/docs/`

## Proposed Tasks

### Task 1: Source Families

- retain the filesystem docs adapter as the first mature source path
- introduce a structured-record adapter shape for database-backed records or query results
- ensure both source families arrive as canonical `ContextSource` artifacts with comparable provenance and metadata

### Task 2: Canonical Semantics

- keep source classification, authority, durability, intended use, and provenance inside the inward canonical model
- treat adapters as translation surfaces, not as alternate semantic models
- avoid introducing parallel source object hierarchies for each ingestion path

### Task 3: Adapter Shape

- prefer adapter inputs that accept already-fetched record payloads or structured rows
- avoid turning Atlas into a full database access framework
- keep DB-driver or vector-store specifics in outer integration code where possible

### Task 4: Craig Architecture Alignment

- adapters own source-specific parsing and translation
- domain owns source semantics
- services should consume already-canonical sources and candidates
- infrastructure may own runtime wiring for source adapters but should not own source meaning

## Sequencing

- identify the minimum structured-record shape needed for the MVP
- create a database-backed record adapter or adapter-ready record contract
- map record inputs into canonical source semantics
- validate mixed-source candidate generation and packet assembly
- document the intended mixed-source ingestion path

## Risks And Unknowns

- Structured-record ingestion can become too database-specific too early.
- Vector-derived records and relational rows may need slightly different adapter affordances.
- There is a risk of leaking source-family quirks into the canonical source model.

## Exit Criteria

- Atlas can ingest both filesystem documents and structured records
- both source families converge into canonical `ContextSource` artifacts
- mixed-source packet assembly works through the shared engine
- the implementation preserves clear adapter-versus-domain responsibility

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md` files in the same slice
- the supported docs, examples, and runtime knobs stay aligned with the implemented surface
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- any deviations from Craig Architecture boundaries are documented explicitly rather than left implicit

## Related Artifacts

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
