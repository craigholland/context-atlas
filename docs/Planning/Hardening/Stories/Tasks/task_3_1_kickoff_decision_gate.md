---
id: context-atlas-hardening-task-3-1-kickoff-decision-gate
title: Task 3.1 - Kickoff Decision Gate PR Plan
summary: Defines the PR sequence for recording and enforcing the Story-level `heuristic-first` versus `tokenizer-seam-first` decision before implementation proceeds.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, token-estimation, tokenizer, decision-gate]
related:
  - ../story_3_token_estimation_and_tokenizer_seam.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 3.1 - Kickoff Decision Gate PR Plan

## Objective

Force an explicit implementation choice between `heuristic-first` and
`tokenizer-seam-first` before Story 3 proceeds, so later PR slices do not try
to solve both concerns halfway in the same increment.

## Task Status

PLANNED

## Inputs

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)
- current estimation behavior in `src/context_atlas/domain/policies/compression.py`

## Proposed Work

### PR - A: Decision Record In Story Layer

- record the Story-level decision directly in Story 3 before implementation
  work starts
- define what success means for the chosen leading path
- make the choice visible enough that later Task and PR work cannot bypass it

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`

#### Update AI files
- `.`

### PR - B: Task And PR-Plan Reinforcement

- restate the decision in the first execution-facing Task or PR slice that
  implements the chosen path
- make the non-leading concern explicitly bounded rather than silently absent
- keep the Story-level decision and Task-level execution wording aligned

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/Tasks/task_3_2_starter_estimation_improvement.md`
- `docs/Planning/Hardening/Stories/Tasks/task_3_3_tokenizer_contract_seam.md`

#### Update AI files
- `.`

### PR - C: Story Boundary Reinforcement

- align Story 3 and neighboring planning docs with the recorded choice
- reduce the chance that Story 4 or Story 5 assumes a different lead path than
  Story 3 actually chose

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`

#### Update AI files
- `.`

## Sequencing

- record the Story-level decision first
- reinforce it in execution-facing Task docs second
- align neighboring Story boundaries last

## Risks And Unknowns

- The decision can still be toothless if it is recorded vaguely or without a
  success bar.
- Later Tasks may drift if the non-leading concern is not explicitly bounded.

## Exit Criteria

- Story 3 records either `heuristic-first` or `tokenizer-seam-first`
- the decision is visible in both Story and Task layers
- later Task execution cannot plausibly proceed without acknowledging the
  decision

## Related Artifacts

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)

