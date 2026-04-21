---
id: context-atlas-hardening-task-2-4-scope-ceiling-and-regression-proof
title: Task 2.4 - Scope Ceiling And Regression Proof PR Plan
summary: Defines the PR sequence for locking Story 2 to one bounded duplicate-handling baseline and proving that baseline is better than both prior heuristics.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, deduplication, scope, proof]
related:
  - ../story_2_duplicate_detection_and_similarity_quality.md
  - ../../context_assembly_hardening_product_definition.md
  - ../story_5_validation_documentation_and_hardening_proof.md
supersedes: []
---

# Task 2.4 - Scope Ceiling And Regression Proof PR Plan

## Objective

Close Story 2 with one explicit acceptance bar for Atlas-owned near-duplicate
handling and enough regression proof to prevent later scope creep into broader
semantic-similarity ambitions.

## Task Status

PLANNED

## Inputs

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
- Tasks 2.1 through 2.3 outcomes
- [Story 5 - Validation, Documentation, And Hardening Proof](../story_5_validation_documentation_and_hardening_proof.md)

## Proposed Work

### PR - A: Acceptance Bar And Non-Goal Reinforcement

- define a bounded "good enough" acceptance bar for Atlas-owned text
- restate the Story's non-goal of embeddings, semantic clustering, or provider
  similarity services
- make that boundary explicit enough that later Tasks do not reopen it

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_2_duplicate_detection_and_similarity_quality.md`
- `docs/Planning/Hardening/context_assembly_hardening_product_definition.md`

#### Update AI files
- `.`

### PR - B: Regression Proof Against Prior Baselines

- add or tighten regressions that prove the new duplicate surface is better
  than exact full-text matching and better than the fragile prefix heuristic on
  the targeted cases
- keep the proof focused on the reviewed failure modes

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_candidate_ranking.py`
- `tests/test_memory_policy.py`

#### Update AI files
- `tests/`

### PR - C: Story-To-Story Handoff Reinforcement

- align Story 2 closeout language with Story 5's later validation/proof work
- ensure the duplicate-handling acceptance bar is ready to be inherited rather
  than rediscovered

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_2_duplicate_detection_and_similarity_quality.md`
- `docs/Planning/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md`

#### Update AI files
- `.`

## Sequencing

- define the acceptance bar first
- prove improvement against both prior baselines second
- hand the closed boundary cleanly to Story 5 last

## Risks And Unknowns

- The acceptance bar can still be too vague if it names goals but not target
  failure cases.
- Story 5 could end up reinventing the duplicate-handling proof bar if Story 2
  does not close with explicit inheritance guidance.

## Exit Criteria

- Story 2 has a clear bounded acceptance bar
- regressions prove the new baseline is better than both prior heuristics on
  the targeted cases
- Story 5 can inherit the duplicate-handling proof surface without reopening
  scope

## Related Artifacts

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
- [Story 5 - Validation, Documentation, And Hardening Proof](../story_5_validation_documentation_and_hardening_proof.md)

