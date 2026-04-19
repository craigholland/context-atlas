---
id: context-atlas-mvp-task-6-2-workflows-under-test
title: Task 6.2 - Workflows Under Test PR Plan
summary: Defines the PR sequence for selecting and preparing the workflows that will be used in MVP proof.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, proof, workflows, evaluation]
related:
  - ../story_6_mvp_proof.md
  - ../../mvp_product_defintiion.md
  - ../story_3_codex_repository_workflow.md
  - ../story_4_documents_plus_database_workflow.md
  - ../story_5_low_code_workflow.md
supersedes: []
---

# Task 6.2 - Workflows Under Test PR Plan

## Objective

Select and prepare the actual workflows that will be evaluated during MVP proof so the assessment is grounded in real Atlas usage paths.

## Task Status

WORKING

## Inputs

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Story 3 - Codex Repository Workflow](../story_3_codex_repository_workflow.md)
- [Story 4 - Documents Plus Database Workflow](../story_4_documents_plus_database_workflow.md)
- [Story 5 - Low-Code Workflow](../story_5_low_code_workflow.md)

## Proposed Work

### PR - A: Workflow Selection

- decide which workflows are mature enough for proof
- define which scenarios will be used for each selected workflow
- make the inclusion and exclusion criteria explicit

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_evaluation_rubric.md`
- `README.md`

#### Update AI files
- `.`

### PR - B: Reproducible Input Preparation

- prepare the source inputs, prompts, and scenarios for each selected workflow
- ensure the runs can be repeated later
- avoid hand-picked one-off examples with hidden setup

#### Expected New Files
- `examples/mvp_proof/inputs/README.md`

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/run.py`
- `examples/docs_database_workflow/run.py`
- `examples/low_code_workflow/run.py`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`
- `tests/`

### PR - C: Workflow Proof Execution

- run the selected workflows under the agreed proof setup
- capture packet, trace, and rendered outputs for each
- verify that the results are comparable across workflows

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `scripts/mvp_proof/capture_evidence.py`
- `examples/mvp_proof/inputs/README.md`
- `README.md`

#### Update AI files
- `.`
- `scripts/`

## Sequencing

- select workflows first
- prepare reproducible inputs second
- execute the proof runs third

## Risks And Unknowns

- The low-code workflow may not be mature enough for the first proof pass.
- Reproducibility may be harder than expected if examples still contain hidden assumptions.
- The selected scenarios may bias the proof if they are too narrow.

## Exit Criteria

- there is a clear list of workflows under test
- the selected workflows have reproducible proof inputs
- proof runs can be executed and compared across workflows

## Related Artifacts

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
