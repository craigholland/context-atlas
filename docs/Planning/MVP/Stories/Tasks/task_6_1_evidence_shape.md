---
id: context-atlas-mvp-task-6-1-evidence-shape
title: Task 6.1 - Evidence Shape PR Plan
summary: Defines the PR sequence for deciding what evidence Atlas must produce to justify an MVP claim.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, proof, evidence, evaluation]
related:
  - ../story_6_mvp_proof.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Identity/Context-Atlas-System-Model.md
supersedes: []
---

# Task 6.1 - Evidence Shape PR Plan

## Objective

Define what kinds of evidence Atlas must produce in order to make a grounded MVP readiness claim.

## Inputs

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- outputs from Stories 1 through 5

## Proposed Work

### PR - A: MVP Evaluation Rubric

- define what evidence matters for MVP readiness
- include packet quality, trace legibility, authority handling, and budget behavior
- avoid reducing the evaluation to vague narrative impressions

#### Expected New Files
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`

#### Expected Existing Files Updated
- `README.md`
- `docs/Planning/MVP/mvp_product_defintiion.md`

#### Update AI files
- `.`

### PR - B: Evidence Capture Shape

- decide which artifacts must be captured for comparison
- standardize how packet, trace, and rendered outputs are recorded
- keep the evidence shape reproducible

#### Expected New Files
- `scripts/mvp_proof/capture_evidence.py`
- `examples/mvp_proof/README.md`

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`
- `README.md`

#### Update AI files
- `.`
- `scripts/`

### PR - C: Evidence Review Path

- define how the captured evidence will be reviewed and compared
- make it possible to tell whether Atlas improved over a naive baseline
- prepare the proof story for repeatable use rather than one-off observation

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`
- `examples/mvp_proof/README.md`
- `scripts/mvp_proof/capture_evidence.py`

#### Update AI files
- `.`
- `scripts/`

## Sequencing

- define the rubric first
- define the evidence capture shape second
- define the review path third

## Risks And Unknowns

- An overly broad rubric may become hard to use.
- An overly narrow rubric may miss what actually makes Atlas valuable.
- It may still be difficult to distinguish product value from demo polish.

## Exit Criteria

- the MVP proof effort has a clear evaluation rubric
- required evidence artifacts are defined
- the review path is reproducible enough for later proof work

## Related Artifacts

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
