---
id: context-atlas-hardening-task-4-2-elastic-slot-behavior-and-caller-contracts
title: Task 4.2 - Elastic Slot Behavior And Caller Contracts PR Plan
summary: Defines the PR sequence for making elastic-slot behavior legible enough that callers and tests do not misread remaining budget semantics.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, budgeting, elastic-slots, caller-contracts]
related:
  - ../story_4_budget_and_compression_truthfulness.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/domain/models/budget.py
supersedes: []
---

# Task 4.2 - Elastic Slot Behavior And Caller Contracts PR Plan

## Objective

Make elastic-slot behavior explicit enough that callers, tests, and later
packet consumers do not infer the wrong meaning from "remaining" budget
surfaces.

## Task Status

IMPLEMENTED

## Inputs

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
- Task 4.1 budget vocabulary
- current elastic-slot behavior in budgeting and service code

## Proposed Work

### PR - A: Caller-Visible Contract Clarification

- define what caller-facing budget surfaces should and should not promise when
  elastic slots are present
- make explicit whether "remaining" means post-fixed reservation or actual
  post-allocation remainder
- keep the clarification aligned with Task 4.1 vocabulary

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/budget.py`
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Elastic-Slot Behavior Alignment

- align elastic-slot behavior and exposed contract surfaces with the clarified
  caller meaning
- avoid changing allocator behavior unnecessarily where only naming or exposed
  contract truth is at issue
- update regression coverage for elastic-slot interpretation
- current delivered Task 4.2 result:
  - `ContextBudget.reserved_tokens` and `ContextBudget.remaining_tokens` remain
    temporary legacy aliases, but they now warn and no longer define the
    preferred caller contract
  - `BudgetAllocationOutcome` now treats `unallocated_tokens` as the truthful
    primary surface, with `remaining_tokens` retained only as a legacy alias
  - budget trace and packet-facing service metadata now surface
    `fixed_reserved_tokens`, `unreserved_tokens`, and `unallocated_tokens`
    explicitly instead of leaning on ambiguous `remaining_tokens` keys

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/budget.py`
- `src/context_atlas/domain/policies/budgeting.py`
- `tests/test_budget_and_compression.py`
- `tests/test_context_assembly_service.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Contract Reinforcement

- reinforce the settled caller contract in Story 4 and neighboring docs
- reduce the chance that later Tasks or guides still use the old ambiguous
  reading of elastic-slot remainder

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`
- `docs/Planning/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md`

#### Update AI files
- `.`

## Sequencing

- clarify caller-visible semantics first
- align elastic-slot behavior and tests second
- reinforce downstream contract wording last

## Risks And Unknowns

- Caller contract fixes can be mistaken for allocator redesign if naming and
  behavior are not separated clearly.
- Story 5 could inherit stale budget terminology if the contract reinforcement
  step is skipped.

## Exit Criteria

- caller-facing elastic-slot semantics are explicit
- exposed budget surfaces no longer encourage the wrong "available for
  documents" reading
- tests cover the clarified elastic-slot contract

## Related Artifacts

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
