---
id: context-atlas-mvp-task-7-1-budget-pressure-proof
title: Task 7.1 - Budget Pressure Proof PR Plan
summary: Defines the PR sequence for adding a stronger budget-constrained proof scenario to the MVP evidence set.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, proof, budget, compression]
related:
  - ../story_7_mvp_readiness_hardening.md
  - ../../../Reviews/MVP/mvp_readiness_assessment.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 7.1 - Budget Pressure Proof PR Plan

## Objective

Add an intentionally budget-constrained proof scenario that demonstrates Atlas making visible, defensible tradeoffs under pressure.

## Task Status

WORKING

## Inputs

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- current proof harness under `scripts/mvp_proof/`

## Proposed Work

### PR - A: Budget-Pressure Scenario Definition

- define the constrained scenario and the expected packet/trace signals
- update the evaluation rubric so the review looks for explicit budget tradeoffs rather than generic output quality
- choose which workflow or workflows should carry the constrained run first

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`
- `examples/mvp_proof/inputs/README.md`
- `docs/Reviews/MVP/mvp_readiness_assessment.md`

#### Update AI files
- `.`
- `scripts/`

### PR - B: Budget-Constrained Workflow Artifacts

- update supported workflow runners or proof inputs so the constrained scenario is reproducible
- ensure the proof artifact bundle preserves packet, trace, and rendered-context evidence for the constrained run
- keep the scenario on the supported engine path rather than a proof-only shortcut

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/run.py`
- `examples/docs_database_workflow/run.py`
- `examples/mvp_proof/README.md`
- `scripts/mvp_proof/capture_evidence.py`

#### Update AI files
- `.`
- `scripts/`
- `src/context_atlas/infrastructure/`

### PR - C: Budget-Pressure Validation And Review Reinforcement

- add focused tests or assertions around the constrained scenario
- reinforce the review guidance so packet and trace inspection remains the primary proof surface
- update the readiness assessment once the scenario artifacts exist

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_mvp_proof_capture.py`
- `tests/test_context_assembly_service.py`
- `docs/Reviews/MVP/mvp_readiness_assessment.md`
- `examples/mvp_proof/evidence/README.md`

#### Update AI files
- `.`
- `scripts/mvp_proof/`
- `tests/`

## Sequencing

- define the constrained scenario first
- generate or capture supported workflow artifacts second
- add validation and refresh the review surface last

## Risks And Unknowns

- An artificially tiny budget may produce noise instead of a useful tradeoff demonstration.
- A good constrained scenario may require changes to example inputs rather than only different CLI arguments.
- The proof may expose compression or budget-allocation weaknesses that require another hardening pass.

## Exit Criteria

- at least one supported workflow has a reproducible budget-constrained proof run
- packet and trace artifacts show meaningful budget tradeoffs
- the readiness assessment can cite concrete budget-pressure evidence

## Related Artifacts

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
