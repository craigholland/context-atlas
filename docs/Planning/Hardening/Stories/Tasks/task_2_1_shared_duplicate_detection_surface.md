---
id: context-atlas-hardening-task-2-1-shared-duplicate-detection-surface
title: Task 2.1 - Shared Duplicate-Detection Surface PR Plan
summary: Defines the PR sequence for establishing one shared bounded duplicate-detection surface for ranking and memory in the inward policy layer.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, deduplication, ranking, memory]
related:
  - ../story_2_duplicate_detection_and_similarity_quality.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/domain/policies/ranking.py
  - ../../../../../src/context_atlas/domain/policies/memory.py
supersedes: []
---

# Task 2.1 - Shared Duplicate-Detection Surface PR Plan

## Objective

Define one shared duplicate-detection surface in the inward policy layer so
ranking and memory can reuse the same bounded lexical or structural semantics
instead of drifting apart.

## Task Status

PLANNED

## Inputs

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)
- current ranking and memory policy code

## Proposed Work

### PR - A: Shared Surface And Placement Decision

- define the shared duplicate-detection contract or helper surface
- keep its intended home explicit in `domain/policies/` or a directly adjacent
  inward helper module
- prevent later Tasks from inferring package placement ad hoc

#### Expected New Files
- none required; if a helper is extracted, it should live under
  `src/context_atlas/domain/policies/`

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_2_duplicate_detection_and_similarity_quality.md`
- `src/context_atlas/domain/policies/ranking.py`
- `src/context_atlas/domain/policies/memory.py`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Shared Semantics Baseline

- define the supported lexical or structural baseline explicitly
- keep semantic-similarity or embeddings assumptions out of the shared surface
- make the shared contract reviewable enough that later Tasks can build on it
  without redefining it

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/ranking.py`
- `src/context_atlas/domain/policies/memory.py`
- `tests/test_candidate_ranking.py`
- `tests/test_memory_policy.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Story Reinforcement

- align Story 2 language around the chosen shared surface and package home
- reduce the chance that later implementation forks the contract silently
- reinforce the scope ceiling before boilerplate handling and integration work

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_2_duplicate_detection_and_similarity_quality.md`
- `src/context_atlas/domain/__ai__.md`

#### Update AI files
- `src/context_atlas/domain/`

## Sequencing

- define shared placement and contract first
- define the bounded semantics baseline second
- reinforce Story and owner guidance last

## Risks And Unknowns

- The shared surface can become too abstract if it avoids making package
  placement and scope explicit.
- Contributors may smuggle semantic-similarity assumptions back in if the
  baseline is not named clearly.

## Exit Criteria

- one shared duplicate-detection surface exists in the intended inward layer
- package placement is explicit
- the bounded lexical or structural baseline is documented tightly enough for
  later Tasks to implement against it

## Related Artifacts

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
