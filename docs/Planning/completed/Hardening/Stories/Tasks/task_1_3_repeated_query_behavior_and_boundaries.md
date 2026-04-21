---
id: context-atlas-hardening-task-1-3-repeated-query-behavior-and-boundaries
title: Task 1.3 - Repeated-Query Behavior And Boundaries PR Plan
summary: Defines the PR sequence for proving the repeated-query path stays on one shared registry-driven retrieval surface while using the indexed state established earlier in the Story.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, retrieval, boundaries]
related:
  - ../story_1_retrieval_indexing_and_performance.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/adapters/retrieval/lexical.py
supersedes: []
---

# Task 1.3 - Repeated-Query Behavior And Boundaries PR Plan

## Objective

Lock the repeated-query path to the same shared registry-driven lexical
retrieval surface while proving that indexed reuse does not create a separate
engine mode or bypass governed source loading.

## Task Status

IMPLEMENTED

## Inputs

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
- current lexical retrieval path and registry usage
- Task 1.1 and Task 1.2 outcomes

## Proposed Work

### PR - A: Shared Registry Path Reinforcement

- keep repeated-query retrieval consuming canonical sources from the same
  registry path as cold retrieval
- make it explicit that indexed reuse does not bypass governed source loading
- reinforce retrieval boundaries if helper extraction created ambiguity

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/adapters/retrieval/lexical.py`
- `tests/test_lexical_retrieval.py`

#### Update AI files
- `src/context_atlas/adapters/`
- `tests/`

### PR - B: Deterministic Behavior Coverage

- prove that the same query and corpus still produce deterministic outcomes
  after the indexed path lands
- ensure reuse changes the work performed, not the public retrieval semantics
- catch boundary regressions where mutable cached state could skew later calls

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_lexical_retrieval.py`

#### Update AI files
- `tests/`

### PR - C: Boundary Documentation Reinforcement

- align the Story and local owner guidance with the final repeated-query path
- make it explicit that the retriever still owns lexical mechanics while the
  registry remains the governed source boundary
- reduce the chance that later hardening work treats the indexed path as a new
  engine family

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/completed/Hardening/Stories/story_1_retrieval_indexing_and_performance.md`
- `src/context_atlas/adapters/__ai__.md`

#### Update AI files
- `src/context_atlas/adapters/`

## Sequencing

- reinforce registry-path boundaries first
- prove deterministic repeated-query behavior second
- reinforce docs and owner files last

## Risks And Unknowns

- Cached state can create subtle order dependence if determinism is not checked
  explicitly.
- Later contributors may still misread the indexed path as a second mode unless
  the boundary docs say so directly.

## Exit Criteria

- repeated-query retrieval stays on the shared registry-driven path
- indexed reuse does not create a second engine mode
- deterministic retrieval semantics are preserved

## Related Artifacts

- [Story 1 - Retrieval Indexing And Performance](../story_1_retrieval_indexing_and_performance.md)
