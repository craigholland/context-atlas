---
id: context-atlas-013-cleanup-task-1-3-guide-path-cleanup-and-wording-normalization
title: Task 1.3 - Guide Path Cleanup And Wording Normalization PR Plan
summary: Defines the PR sequence for removing internal execution residue from the product-facing guide path and tightening the starter flow into one truthful story.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, guides, wording, onboarding]
related:
  - ../story_1_product_evaluator_on_ramp_and_output_clarity.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../docs/Guides/getting_started.md
  - ../../../../../docs/Guides/context_atlas_tour.md
  - ../../../../../docs/Guides/README.md
supersedes: []
---

# Task 1.3 - Guide Path Cleanup And Wording Normalization PR Plan

## Objective

Remove internal planning residue and starter-path wording drift from the guide
layer so the product route reads like one intentional onboarding story rather
than a mix of execution leftovers.

## Task Status

PLANNED

## Inputs

- [Story 1 - Product Evaluator On-Ramp And Output Clarity](../story_1_product_evaluator_on_ramp_and_output_clarity.md)
- current guide surfaces under `docs/Guides/`
- the current root README map/tour split

## Proposed Work

### PR - A: Internal Residue Removal

- remove Story-number or execution-history residue from product-facing guides
- preserve only vocabulary that is genuinely helpful to product evaluators
- keep the cleanup bounded to user-facing wording rather than deep technical
  explanation

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Guides/getting_started.md`
- `docs/Guides/context_atlas_tour.md`

#### Update AI files

- `.`

### PR - B: Starter-Flow Tightening

- tighten the guide sequence so shared setup happens before workflow-specific
  divergence
- align the guide index and tour openings with the same starter story
- keep the product path readable without collapsing important differences

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Guides/README.md`
- `docs/Guides/getting_started.md`
- `docs/Guides/context_atlas_tour.md`

#### Update AI files

- `.`

### PR - C: Story Reinforcement

- align Story 1 with the cleaned guide path
- document any wording or example work intentionally deferred to Task 1.4

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_1_product_evaluator_on_ramp_and_output_clarity.md`

#### Update AI files

- `.`

## Sequencing

- remove internal residue first
- tighten the guide flow second
- reinforce Story language third

## Risks And Unknowns

- Wording cleanup can become subjective churn if not tied to the product path's
  real onboarding job.
- Tightening the guide flow can accidentally hide legitimate workflow
  differences if over-compressed.

## Exit Criteria

- product-facing guides no longer contain internal execution residue
- the guide path reads as one intentional starter story
- Story 1 reflects that cleaned guide route clearly

## Related Artifacts

- [Story 1 - Product Evaluator On-Ramp And Output Clarity](../story_1_product_evaluator_on_ramp_and_output_clarity.md)
- [Guides README](../../../../../docs/Guides/README.md)
- [Getting Started Guide](../../../../../docs/Guides/getting_started.md)

