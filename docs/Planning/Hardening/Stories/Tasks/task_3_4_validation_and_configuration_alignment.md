---
id: context-atlas-hardening-task-3-4-validation-and-configuration-alignment
title: Task 3.4 - Validation And Configuration Alignment PR Plan
summary: Defines the PR sequence for validating the delivered Story 3 path and aligning runtime-surface documentation only where supported behavior actually changed.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [hardening, task, pr-plan, validation, configuration, token-estimation]
related:
  - ../story_3_token_estimation_and_tokenizer_seam.md
  - ../../context_assembly_hardening_product_definition.md
  - ../story_5_validation_documentation_and_hardening_proof.md
supersedes: []
---

# Task 3.4 - Validation And Configuration Alignment PR Plan

## Objective

Validate the Story 3 outcome against the actual chosen path and keep runtime
config or documentation surfaces honest about whether Atlas now exposes a new
supported knob, a seam, or only internal heuristic changes.

## Task Status

IMPLEMENTED

## Inputs

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
- Task 3.1 decision record
- outputs from Task 3.2 and Task 3.3 as applicable

## Proposed Work

### PR - A: Validation Coverage

- add or refine tests that prove the delivered Story 3 shape
- keep validation aimed at the actual chosen lead path rather than a
  hypothetical combined solution

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_budget_and_compression.py`
- `tests/test_config_observability.py`
- `tests/test_context_assembly_service.py`

#### Update AI files
- `tests/`

### PR - B: Configuration And Doc Truthfulness

- update configuration docs or runtime surfaces only if Story 3 actually
  changed supported behavior
- avoid creating new product-facing knob expectations just because internal
  estimation logic improved

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `.env.example`
- `README.md`
- `docs/Guides/getting_started.md`

#### Update AI files
- `.`

### PR - C: Story-To-Story Handoff

- align Story 3 closeout with Story 4 and Story 5 so later budget/compression
  truthfulness and proof work inherit the delivered estimation story
- remove ambiguity about what still remains intentionally deferred

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_3_token_estimation_and_tokenizer_seam.md`
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`
- `docs/Planning/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md`

#### Update AI files
- `.`

## Sequencing

- validate the delivered Story 3 path first
- align configuration and docs second
- hand the closed Story semantics to Stories 4 and 5 last

## Risks And Unknowns

- Docs can overclaim support if internal heuristic changes are mistaken for new
  runtime knobs.
- Story 4 may inherit a fuzzy estimation contract if Story 3 closeout is not
  explicit enough.

## Exit Criteria

- Story 3 has validation coverage that matches the actual chosen path
- runtime docs and config surfaces say only what the code now supports
- Stories 4 and 5 inherit a clear estimation/tokenizer baseline
- delivered shape:
  - packet-facing validation now proves the default starter path emits
    `starter_heuristic` and outward-bound custom estimators emit their bound
    label through packet and trace metadata
  - product-facing docs now state that
    `CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN` is the baseline control for the
    starter heuristic rather than a promise of one flat estimate everywhere
  - Atlas still exposes no env-backed tokenizer selector; the custom estimator
    seam remains an outward callable binding surface only

## Related Artifacts

- [Story 3 - Token Estimation And Tokenizer Seam](../story_3_token_estimation_and_tokenizer_seam.md)
- [Story 5 - Validation, Documentation, And Hardening Proof](../story_5_validation_documentation_and_hardening_proof.md)

