---
id: context-atlas-hardening-task-3-2-starter-estimation-improvement
title: Task 3.2 - Starter Estimation Improvement PR Plan
summary: Defines the PR sequence for improving the starter estimation baseline when Story 3 chooses to lead with heuristic hardening.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, token-estimation, heuristic]
related:
  - ../story_3_token_estimation_and_tokenizer_seam.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/domain/policies/compression.py
supersedes: []
---

# Task 3.2 - Starter Estimation Improvement PR Plan

## Objective

Improve the starter token-estimation heuristic in a bounded, provider-agnostic
way when Story 3 leads with heuristic hardening, so Atlas stops treating prose,
code, and markup-heavy content as one global ratio.

## Task Status

PLANNED

## Inputs

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
- Story 3 kickoff decision from Task 3.1
- current compression and estimation behavior under
  `src/context_atlas/domain/policies/compression.py`

## Proposed Work

### PR - A: Heuristic Baseline Definition

- define the bounded improved starter heuristic for content-shape differences
- keep the heuristic deterministic and provider-agnostic
- make it explicit which content distinctions are intentionally in scope

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/compression.py`
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Heuristic Integration

- wire the improved heuristic into the current estimation path
- preserve the shared packet and compression path while changing the estimation
  behavior underneath it
- avoid smuggling provider-specific token knowledge inward

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/compression.py`
- `tests/test_budget_and_compression.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Validation And Story Reinforcement

- add or refine validation proving the heuristic behaves as intended on the
  supported content shapes
- keep the Story explicit about what remains for the tokenizer seam to solve
  later

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_budget_and_compression.py`
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`

#### Update AI files
- `tests/`

## Sequencing

- define the improved heuristic first
- integrate it second
- reinforce validation and Story boundaries last

## Risks And Unknowns

- A heuristic can still become misleading if it quietly encodes provider
  assumptions.
- Content-shape distinctions can sprawl if the baseline is not kept bounded.

## Exit Criteria

- Atlas no longer depends solely on one global `chars_per_token = 4` rule for
  the starter path
- the improved heuristic remains provider-agnostic and bounded
- tests make the new heuristic behavior visible enough to review

## Related Artifacts

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
