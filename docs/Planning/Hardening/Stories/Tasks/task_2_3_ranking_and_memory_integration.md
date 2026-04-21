---
id: context-atlas-hardening-task-2-3-ranking-and-memory-integration
title: Task 2.3 - Ranking And Memory Integration PR Plan
summary: Defines the PR sequence for replacing the current ranking and memory duplicate gates with the shared improved surface while preserving deterministic policy behavior.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, ranking, memory, integration]
related:
  - ../story_2_duplicate_detection_and_similarity_quality.md
  - ../../context_assembly_hardening_product_definition.md
supersedes: []
---

# Task 2.3 - Ranking And Memory Integration PR Plan

## Objective

Integrate the shared duplicate-detection surface into both ranking and memory
so Atlas stops using exact full-text matching in one path and fragile
prefix-heavy logic in the other.

## Task Status

PLANNED

## Inputs

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
- Task 2.1 shared duplicate surface
- Task 2.2 boilerplate normalization decisions

## Proposed Work

### PR - A: Ranking Integration

- replace ranking's exact full-text duplicate gate with the shared surface
- keep ranking outcomes deterministic and reviewable
- ensure ranking still respects the broader candidate scoring semantics around
  the duplicate decision

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/ranking.py`
- `tests/test_candidate_ranking.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - B: Memory Integration

- replace or constrain memory's fragile prefix-heavy behavior with the same
  shared surface
- preserve the memory policy's broader retention and boost semantics where they
  remain valid
- keep the memory integration transparent rather than hiding a second special
  duplicate path inside the policy

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/memory.py`
- `tests/test_memory_policy.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Cross-Policy Consistency Reinforcement

- add targeted coverage or notes that prove ranking and memory now consume the
  same duplicate semantics
- reduce the chance of silent future drift between the two policies

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_candidate_ranking.py`
- `tests/test_memory_policy.py`
- `src/context_atlas/domain/__ai__.md`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

## Sequencing

- integrate ranking first
- integrate memory second
- reinforce cross-policy consistency third

## Risks And Unknowns

- One policy may expose edge cases the other did not, even with a shared
  surface.
- Determinism can regress if the integration quietly adds fuzzy thresholds or
  ordering ambiguity.

## Exit Criteria

- ranking and memory both consume the shared duplicate surface
- exact full-text matching and prefix-heavy shortcuts are no longer the
  standing duplicate gates
- tests make cross-policy consistency visible enough to review

## Related Artifacts

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)

