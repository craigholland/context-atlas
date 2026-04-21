---
id: context-atlas-hardening-task-4-3-compression-result-truthfulness
title: Task 4.3 - Compression Result Truthfulness PR Plan
summary: Defines the PR sequence for making compression results truthfully represent effective runtime behavior, including fallback from configured strategy to actual strategy.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, compression, fallback, semantics]
related:
  - ../story_4_budget_and_compression_truthfulness.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/domain/models/transformations.py
  - ../../../../../src/context_atlas/domain/policies/compression.py
supersedes: []
---

# Task 4.3 - Compression Result Truthfulness PR Plan

## Objective

Ensure compression results truthfully show the effective runtime strategy,
especially when extractive compression falls back to truncation, so packet and
trace consumers do not have to infer actual behavior from secondary metadata.

## Task Status

PLANNED

## Inputs

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
- current compression result and fallback behavior
- current packet and trace expectations around compression metadata

## Proposed Work

### PR - A: Result-Surface Semantics

- define how configured strategy and effective strategy should appear in
  canonical compression results
- decide what belongs in the primary result surface versus secondary metadata
- keep the result surface truthful without becoming overly verbose

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/models/transformations.py`
- `src/context_atlas/domain/policies/compression.py`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Fallback Behavior Alignment

- align extractive fallback behavior with the clarified result semantics
- ensure the actual runtime strategy is represented correctly when fallback
  occurs
- update tests that currently rely on the older behavior

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/compression.py`
- `tests/test_budget_and_compression.py`
- `tests/test_context_assembly_service.py`

#### Update AI files
- `src/context_atlas/domain/`
- `tests/`

### PR - C: Story Reinforcement

- align Story 4 wording around configured versus effective compression
  behavior
- reduce the chance that later trace or renderer work preserves stale fallback
  assumptions

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`
- `docs/Planning/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md`

#### Update AI files
- `.`

## Sequencing

- settle result-surface semantics first
- align fallback behavior and tests second
- reinforce Story wording last

## Risks And Unknowns

- The result surface can become noisy if it tries to expose too much internal
  detail instead of the minimum truthful distinction.
- Packet and trace expectations may still lag behind if Story reinforcement is
  skipped.

## Exit Criteria

- compression results truthfully distinguish configured versus effective
  strategy where fallback happens
- extractive fallback no longer appears as pure extractive success in the
  primary result surface
- Story 4 and its tests share the same fallback semantics

## Related Artifacts

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
