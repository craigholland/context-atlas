---
id: context-atlas-013-cleanup-task-1-1-product-entry-surface-and-runtime-floor-visibility
title: Task 1.1 - Product Entry Surface And Runtime-Floor Visibility PR Plan
summary: Defines the PR sequence for making the product entry surface faster to scan and surfacing the real Python/runtime prerequisites before evaluators hit setup friction.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, onboarding, readme, runtime]
related:
  - ../story_1_product_evaluator_on_ramp_and_output_clarity.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../README.md
  - ../../../../../docs/Guides/getting_started.md
supersedes: []
---

# Task 1.1 - Product Entry Surface And Runtime-Floor Visibility PR Plan

## Objective

Make the first product-facing entry surface clearer by foregrounding the mental
model and the real Python/runtime floor before a new evaluator is forced into
setup failure or contributor-only detail.

## Task Status

IMPLEMENTED

## Inputs

- [Story 1 - Product Evaluator On-Ramp And Output Clarity](../story_1_product_evaluator_on_ramp_and_output_clarity.md)
- [013 Cleanup Product Definition](../../013_cleanup_product_definition.md)
- [README](../../../../../README.md)
- [Getting Started Guide](../../../../../docs/Guides/getting_started.md)

## Proposed Work

### PR - A: Root Product Entry And Runtime-Floor Callout

- tighten the root product-facing route so the mental model and runtime floor
  are visible early
- keep the README acting as the repo map rather than reopening a full tour
- ensure any needed `Codex` mention remains outsider-friendly and brief

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`

#### Update AI files

- `.`

### PR - B: Guide Entry Alignment

- align the guide path so the runtime floor and first-step expectations match
  the root README
- keep shared setup steps visible before workflow-specific divergence
- remove any wording that obscures the starter product route

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Guides/getting_started.md`
- `docs/Guides/README.md`

#### Update AI files

- `.`

### PR - C: Story Reinforcement

- align Story 1 with the settled entry-surface contract
- document any remaining follow-on concerns that belong to later tasks rather
  than stretching this task's scope

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_1_product_evaluator_on_ramp_and_output_clarity.md`

#### Update AI files

- `.`

## Sequencing

- settle the root entry surface first
- align the guide entry second
- reinforce Story language last

## Risks And Unknowns

- The README can drift back into a tour if runtime-floor visibility is added
  without keeping the map boundary intact.
- Guide cleanup can become repetitive if runtime requirements are duplicated
  mechanically instead of placed intentionally.

## Exit Criteria

- the root product route states the real runtime floor clearly
- the guide entry path matches that same prerequisite story
- Story 1 reflects the final entry-surface contract

## Completed Outcome

- the root README now frames Atlas as provider-agnostic first, explains
  `Codex` briefly as a repository/runtime binding, and surfaces the current
  Python `3.12+` starter floor near the top of the repo map
- the guide entry surface now repeats that same Python `3.12+` prerequisite
  early in both the guides index and the getting-started path so evaluators do
  not learn it only after dropping into setup detail

## Related Artifacts

- [Story 1 - Product Evaluator On-Ramp And Output Clarity](../story_1_product_evaluator_on_ramp_and_output_clarity.md)
- [README](../../../../../README.md)
- [Getting Started Guide](../../../../../docs/Guides/getting_started.md)

