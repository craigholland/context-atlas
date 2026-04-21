---
id: context-atlas-hardening-story-1-retrieval-indexing-and-performance
title: Story 1 - Retrieval Indexing And Performance
summary: Defines how Context Atlas should remove repeated full-corpus lexical recomputation from the steady-state repeated-query path while preserving one shared retrieval surface.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, story, retrieval, indexing, performance, tf-idf]
related:
  - ../context_assembly_hardening_product_definition.md
  - ./story_2_duplicate_detection_and_similarity_quality.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../../../../src/context_atlas/adapters/retrieval/lexical.py
  - ../../../../src/context_atlas/adapters/retrieval/registry.py
  - ../../../../src/context_atlas/adapters/retrieval/indexing.py
supersedes: []
---

# Story 1 - Retrieval Indexing And Performance

## Objective

Harden lexical retrieval so repeated queries over a stable in-memory corpus no
longer rebuild the full TF-IDF working set on every call, while still keeping
Context Atlas on one shared retrieval path rather than introducing a separate
"fast mode" engine.

## Inputs

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Story 2 - Duplicate Detection And Similarity Quality](./story_2_duplicate_detection_and_similarity_quality.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- current lexical retrieval, registry, and index-shape code under
  `src/context_atlas/adapters/retrieval/`
- current lexical retrieval regression coverage in `tests/test_lexical_retrieval.py`

## Proposed Tasks

### Task 1: Index Ownership And Cache Shape

- define the smallest supported in-memory index surface needed for repeated
  lexical retrieval
- make it explicit which reusable state belongs to the retriever versus the
  source registry versus a dedicated helper object
- keep canonical source ownership in the registry surface while letting the
  baseline lexical index shape live in a dedicated outward retrieval helper
  instead of hiding both concerns in one file
- treat the current `registry.py` plus `indexing.py` split as the baseline
  outward adapter surface established by Task 1.1, with `lexical.py`
  remaining the consumer/orchestrator rather than reclaiming both concerns
- keep the index outward in the adapter layer rather than inventing a new
  inward domain artifact for retrieval mechanics

### Task 2: Document-State Reuse

- ensure repeated queries can reuse both corpus-wide document-frequency/IDF
  state and reusable per-document token or vector-building work
- prevent a partial fix that caches the IDF table but still rebuilds
  per-document TF/vector state on every query
- keep invalidation or rebuild rules explicit and small
- treat the supported steady-state reuse shape as one registry-revision-aligned
  lexical snapshot carrying corpus-wide IDF plus source-side TF-IDF vectors and
  norms, rather than parallel caches split across multiple adapter surfaces

### Task 3: Repeated-Query Behavior And Boundaries

- prove the steady-state repeated-query path no longer performs full-corpus
  recomputation for every call
- keep the lexical retriever consuming canonical sources from the same shared
  registry model rather than bypassing governed source loading
- make the warm-cache path explicitly re-enter the retrieval flow through one
  fresh registry source listing per call rather than acting like a second
  hidden source-loading mode
- preserve deterministic ranking semantics for the same query/corpus input

### Task 4: Validation And Performance-Facing Proof

- update regression coverage so the indexed path is visible and reviewable
- add bounded proof or instrumentation surfaces that show reuse behavior
  without turning this Story into a benchmark framework initiative
- refresh the nearest docs or owner files if retrieval ownership boundaries or
  expectations change

## Sequencing

- define index ownership and cache shape first
- implement reusable per-document and corpus-wide retrieval state next
- settle invalidation and repeated-query behavior before broad test changes
- prove the indexed path last through tests and bounded review surfaces

## Risks And Unknowns

- Index ownership can sprawl quickly if the registry starts absorbing unrelated
  retrieval behavior instead of just owning canonical sources plus bounded index
  state.
- It is easy to "solve" the review finding halfway by caching document
  frequency while still rebuilding most of the expensive per-document work.
- Performance-oriented proof can drift into benchmark theater unless it stays
  focused on index reuse and architectural trustworthiness.

## Exit Criteria

- repeated lexical retrieval over a static registry no longer recomputes the
  full TF-IDF working set on every query
- reusable retrieval state covers both corpus-wide statistics and per-document
  vector-building work rather than only one side of the problem
- retrieval indexing remains an outward adapter concern and does not create a
  second engine path
- tests and review surfaces make the indexed behavior visible enough to verify
  it without relying on implementation folklore

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- retrieval indexing remains on the shared lexical retrieval path instead of
  forking into a second unsupported engine mode
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- `src/context_atlas/adapters/retrieval/registry.py`
- `src/context_atlas/adapters/retrieval/indexing.py`
