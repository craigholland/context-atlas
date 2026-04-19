---
id: context-atlas-mvp-task-7-2-document-authority-proof
title: Task 7.2 - Document Authority Proof PR Plan
summary: Defines the PR sequence for strengthening proof inputs so authority handling is demonstrated through governed documents.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, proof, authority, documents]
related:
  - ../story_7_mvp_readiness_hardening.md
  - ../../../Reviews/MVP/mvp_readiness_assessment.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 7.2 - Document Authority Proof PR Plan

## Objective

Strengthen the MVP proof inputs so authority handling is demonstrated through governed document sources rather than mainly through structured records.

## Task Status

IMPLEMENTED

## Inputs

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
- Story 2 source-semantics outcomes
- Story 6 proof artifacts and review notes

## Proposed Work

### PR - A: Authority-Rich Document Scenario Design

- define the document-side authority contrast that the proof should exercise
- identify which supported workflow samples need stronger authoritative and lower-authority document inputs
- make the scenario inspectable through canonical source semantics rather than folder-name folklore alone

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`
- `examples/codex_repository_workflow/sample_repo/README.md`
- `examples/mvp_proof/inputs/README.md`

#### Update AI files
- `.`

### PR - B: Authority-Proof Inputs And Evidence Refresh

- add or adjust supported sample documents so authority precedence can be observed in packet selection and trace reasoning
- refresh the proof workflow artifacts using those stronger inputs
- keep the proof path on the same shared engine and canonical source model

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/sample_repo/README.md`
- `examples/codex_repository_workflow/run.py`
- `examples/mvp_proof/evidence/README.md`
- `scripts/mvp_proof/capture_evidence.py`

#### Update AI files
- `.`
- `scripts/`

### PR - C: Authority Review Reinforcement

- update the readiness assessment and supporting review docs to call out the stronger authority proof
- add focused tests where authority precedence is now expected to be visible
- keep the product-facing guidance honest about what the proof does and does not yet cover

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_readiness_assessment.md`
- `tests/test_codex_repository_workflow.py`
- `README.md`

#### Update AI files
- `.`
- `tests/`

## Sequencing

- define the authority scenario first
- update supported proof inputs second
- refresh assessment and validation last

## Risks And Unknowns

- Stronger authority contrast may expose weak source classification or ranking behavior.
- The most convincing authority proof may require changes in example content, not only review wording.
- There is a risk of overfitting the proof to one sample corpus.

## Exit Criteria

- the proof evidence shows authority handling through governed documents
- the readiness assessment no longer depends mainly on structured-record authority examples
- packet and trace inspection make the authority rationale visible

## Implemented Outcome

- The authority-rich repository scenario `codex_repository / repo_document_authority_precedence` is now a reviewed standing-proof artifact.
- The proof set now shows a `binding` authoritative document staying ahead of lower-authority planning and review documents with explicit authority-aware trace reasons.

## Related Artifacts

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
