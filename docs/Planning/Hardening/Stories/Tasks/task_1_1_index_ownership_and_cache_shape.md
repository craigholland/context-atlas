---
id: context-atlas-hardening-task-1-1-index-ownership-and-cache-shape
title: Task 1.1 - Index Ownership And Cache Shape PR Plan
summary: Defines the PR sequence for deciding where lexical retrieval index state lives and how repeated-query cache ownership should be governed without creating a second engine path.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, retrieval, indexing]
related:
  - ../story_1_retrieval_indexing_and_performance.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 1.1 - Index Ownership And Cache Shape PR Plan

## Objective

Define the smallest supported in-memory indexing surface for lexical retrieval
so later performance work has one explicit ownership model for indexed state,
registry interaction, and invalidation.

## Task Status

IMPLEMENTED

## Inputs

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)
- [Craig Architecture](../../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current lexical retrieval and registry code in `src/context_atlas/adapters/retrieval/lexical.py`

## Proposed Work

### PR - A: Ownership Boundary And Baseline Shape

- document and codify the current lexical retriever and registry baseline
- decide whether index state remains attached to the existing `lexical.py`
  surfaces or is extracted into a dedicated outward helper under
  `src/context_atlas/adapters/retrieval/`
- keep the boundary explicit that retrieval index state is outward adapter
  state, not a new inward domain model

#### Expected New Files
- none required; if a helper is extracted, it should live under
  `src/context_atlas/adapters/retrieval/`

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_1_retrieval_indexing_and_performance.md`
- `src/context_atlas/adapters/retrieval/lexical.py`

#### Update AI files
- `src/context_atlas/adapters/`

### PR - B: Cache Shape And Invalidation Rules

- define the minimum cache shape needed for repeated-query reuse
- make invalidation or rebuild rules explicit and small
- prevent ambiguous mixed ownership between retriever-local state and
  registry-owned state

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/retrieval/lexical.py`
- `tests/test_lexical_retrieval.py`

#### Update AI files
- `src/context_atlas/adapters/`
- `tests/`

### PR - C: Story Reinforcement

- align planning and owner-file guidance with the chosen index boundary
- remove ambiguity about whether a separate registry file already exists
- leave a stable baseline for Task 1.2 document-state reuse

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_1_retrieval_indexing_and_performance.md`
- `__ai__.md`

#### Update AI files
- `.`

## Sequencing

- settle ownership boundary first
- define cache shape and invalidation second
- reinforce the Story and owner-file contract last

## Risks And Unknowns

- The implementation can drift into "helper sprawl" if the cache shape is not
  kept intentionally small.
- A partial extraction can make ownership less clear rather than more clear.
- Contributors may accidentally treat outward index state as a new domain
  concept if the boundary is not explicit.

## Exit Criteria

- index ownership is explicit and reviewable
- cache shape and invalidation rules are documented tightly enough to guide
  Task 1.2
- no second retrieval engine path is introduced

## Related Artifacts

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)

