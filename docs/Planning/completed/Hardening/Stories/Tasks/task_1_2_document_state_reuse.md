---
id: context-atlas-hardening-task-1-2-document-state-reuse
title: Task 1.2 - Document-State Reuse PR Plan
summary: Defines the PR sequence for reusing both corpus-wide statistics and per-document retrieval state instead of rebuilding most TF-IDF work on every query.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, retrieval, tfidf]
related:
  - ../story_1_retrieval_indexing_and_performance.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/adapters/retrieval/lexical.py
supersedes: []
---

# Task 1.2 - Document-State Reuse PR Plan

## Objective

Implement reusable lexical retrieval state so repeated queries can reuse both
corpus-wide document-frequency information and per-document token or
vector-building work rather than only caching one half of the TF-IDF path.

## Task Status

IMPLEMENTED

## Inputs

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)
- ownership and cache-shape decisions from Task 1.1
- current lexical retrieval tests in `tests/test_lexical_retrieval.py`

## Proposed Work

### PR - A: Corpus-Wide Statistic Reuse

- persist reusable document-frequency or IDF state for a static corpus
- keep corpus-wide statistic reuse aligned with the Task 1.1 ownership model
- prevent query-time recomputation of corpus-wide statistics when inputs have
  not changed

#### Expected New Files
- none expected
- If Task 1.1 extracts the registry or index ownership surface out of
  `lexical.py`, reuse work here may instead continue by updating that new file
  rather than treating "none expected" as a hard prohibition on prior
  extraction.

#### Expected Existing Files Updated
- `src/context_atlas/adapters/retrieval/lexical.py`
- `tests/test_lexical_retrieval.py`

#### Update AI files
- `src/context_atlas/adapters/`
- `tests/`

### PR - B: Per-Document State Reuse

- reuse per-document tokenization, term-frequency, or vector-building work
- keep the reusable state bounded to what repeated lexical retrieval actually
  needs
- prevent a "cached IDF, rebuilt documents" half-fix

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/retrieval/lexical.py`
- `tests/test_lexical_retrieval.py`

#### Update AI files
- `src/context_atlas/adapters/`
- `tests/`

### PR - C: Steady-State Reuse Reinforcement

- add targeted regressions or instrumentation-oriented assertions proving that
  both reuse layers are active
- keep the validation bounded to reuse semantics rather than benchmark theater
- align Story notes if the chosen reusable state shape becomes clearer than the
  original planning wording

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_lexical_retrieval.py`
- `docs/Planning/completed/Hardening/Stories/story_1_retrieval_indexing_and_performance.md`

#### Update AI files
- `tests/`

## Sequencing

- implement corpus-wide reuse first
- implement per-document reuse second
- reinforce with targeted validation third
- keep the file-touch expectation conditional on the Task 1.1 ownership outcome
  instead of assuming `lexical.py` remains the only implementation home

## Risks And Unknowns

- Per-document reuse can accidentally overcache state that should remain
  derived and lightweight.
- Tests can prove behavior too indirectly if they only check outputs and not
  reuse-relevant state transitions.
- Reuse logic can become brittle if invalidation assumptions remain implicit.

## Exit Criteria

- repeated lexical retrieval reuses both corpus-wide and per-document state
- Task 1.2 closes the "cache one side but rebuild the other" gap explicitly
- targeted tests prove both reuse layers without turning into benchmark suites

## Related Artifacts

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
