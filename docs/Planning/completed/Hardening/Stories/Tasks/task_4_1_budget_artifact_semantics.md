---
id: context-atlas-hardening-task-4-1-budget-artifact-semantics
title: Task 4.1 - Budget Artifact Semantics PR Plan
summary: Defines the PR sequence for making canonical budget artifacts tell the truth about reservation, allocation, and remainder semantics.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [hardening, task, pr-plan, budgeting, semantics, artifacts]
related:
  - ../story_4_budget_and_compression_truthfulness.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/domain/models/budget.py
  - ../../../../../src/context_atlas/domain/policies/budgeting.py
supersedes: []
---

# Task 4.1 - Budget Artifact Semantics PR Plan

## Objective

Clarify the canonical meaning of budget artifacts so reservation, actual
allocation, and remainder concepts are represented truthfully instead of being
blurred behind misleading names.

## Task Status

IMPLEMENTED

## Inputs

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
- [Context Assembly Hardening Product Definition](../../context_assembly_hardening_product_definition.md)
- current budget model and policy code

## Proposed Work

### PR - A: Canonical Budget Vocabulary

- define the truthful vocabulary for budget reservation, allocation, and
  remainder
- decide which current field or property names should be preserved versus
  clarified
- keep the canonical truth in domain artifacts rather than in renderer notes

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/budget.py`
- `src/context_atlas/domain/policies/budgeting.py`
- `docs/Planning/completed/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Model And Policy Alignment

- align model fields and budgeting behavior with the chosen vocabulary
- preserve the allocator's sensible happy-path behavior where it is already
  correct
- remove or rename misleading semantics where contract truth requires it

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/budget.py`
- `src/context_atlas/domain/policies/budgeting.py`
- `tests/test_budget_and_compression.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Story Reinforcement

- align Story 4 wording with the settled budget vocabulary
- reduce the chance that later Tasks still rely on the old ambiguous reading of
  budget fields

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/completed/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`
- `src/context_atlas/domain/__ai__.md`

#### Update AI files
- `src/context_atlas/domain/`

## Sequencing

- define canonical vocabulary first
- align models and policies second
- reinforce Story and owner guidance last

## Risks And Unknowns

- Renaming or clarifying semantics can ripple into packet, trace, and renderer
  surfaces quickly.
- The work can stop too early if implementation preserves behavior but leaves
  misleading names intact.

## Exit Criteria

- budget artifacts truthfully distinguish reservation, allocation, and
  remainder semantics
- domain models and policies align with that vocabulary
- later Story 4 Tasks inherit one stable budget language
- delivered shape:
  - `ContextBudget` now exposes `fixed_reserved_tokens` and
    `unreserved_tokens` as the truthful pre-allocation budget vocabulary
  - `BudgetAllocationOutcome` now exposes `unallocated_tokens` as the truthful
    post-allocation remainder
  - compatibility aliases remain in place temporarily for
    `reserved_tokens` and `remaining_tokens` until Task 4.2 finishes the
    caller-facing contract cleanup

## Related Artifacts

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
