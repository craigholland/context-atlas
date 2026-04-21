---
id: context-atlas-hardening-task-3-3-tokenizer-contract-seam
title: Task 3.3 - Tokenizer Contract Seam PR Plan
summary: Defines the PR sequence for introducing a provider-agnostic tokenizer contract seam without leaking provider specifics into the domain layer.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [hardening, task, pr-plan, tokenizer, seam, contracts]
related:
  - ../story_3_token_estimation_and_tokenizer_seam.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/infrastructure/config/settings.py
supersedes: []
---

# Task 3.3 - Tokenizer Contract Seam PR Plan

## Objective

Define and introduce a provider-agnostic tokenizer contract seam so future
integrations can bind real tokenizers outward without dragging provider logic
into the domain layer.
If Task 3.1 instead records a heuristic-first kickoff decision, this Task
should stay complementary and bounded rather than expanding into a second
parallel primary track.
Task 3.1 has now recorded `heuristic-first`, so this Task is explicitly the
bounded complementary follow-on path rather than the primary Story 3 track.

## Task Status

PLANNED

## Inputs

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
- Story 3 kickoff decision from Task 3.1
- recorded kickoff decision: `heuristic-first`
- recorded Task 3.1 decision showing whether the seam is the lead path or the
  bounded follow-on path
- current domain and infrastructure estimation surfaces

## Proposed Work

### PR - A: Seam Placement And Contract Shape

- define where the tokenizer contract belongs and where it must not leak
- keep provider-specific bindings outward in infrastructure or composition
  layers
- make the seam explicit enough to be reviewable before any real tokenizer is
  bound to it
- size the seam according to the Task 3.1 decision instead of assuming it is
  always the lead implementation path

#### Expected New Files
- none required; if a dedicated contract helper is extracted, it should remain
  provider-agnostic and outside provider-specific integration folders

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`
- `src/context_atlas/infrastructure/config/settings.py`

#### Update AI files
- `src/context_atlas/infrastructure/`

### PR - B: Outward Binding Integration

- wire the contract seam into outward composition points without changing the
  inward policy boundary
- keep the starter path working even if no external tokenizer is supplied
- ensure the seam does not imply broader provider integration than the code
  actually supports
- if heuristic-first was chosen, keep this binding slice deliberately narrow and
  complementary to that decision

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/domain/policies/compression.py`
- `tests/test_config_observability.py`
- `tests/test_budget_and_compression.py`

#### Update AI files
- `src/context_atlas/infrastructure/`
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Boundary Reinforcement

- document what the seam enables later and what it does not enable yet
- keep Story 3 clear about the difference between a tokenizer seam and a full
  provider integration

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`
- `__ai__.md`

#### Update AI files
- `.`

## Sequencing

- define seam placement and contract shape first
- wire the outward binding integration second
- reinforce boundaries and non-goals last
- treat this Task as the bounded complementary follow-on path because Task 3.1
  recorded heuristic-first at the Story layer

## Risks And Unknowns

- A tokenizer seam can become architecture theater if it exists only on paper
  and does not actually shape outward composition.
- The seam can become a layering leak if provider assumptions appear in domain
  policy code or model names.

## Exit Criteria

- a provider-agnostic tokenizer seam exists
- the seam binds outward without leaking provider specifics inward
- the starter path remains truthful about what is and is not supported

## Related Artifacts

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
