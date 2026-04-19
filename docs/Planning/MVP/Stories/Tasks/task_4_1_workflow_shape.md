---
id: context-atlas-mvp-task-4-1-workflow-shape
title: Task 4.1 - Workflow Shape PR Plan
summary: Defines the PR sequence for shaping the documents-plus-database workflow around the shared Atlas engine.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, chatbot, docs, database, workflow]
related:
  - ../story_4_documents_plus_database_workflow.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 4.1 - Workflow Shape PR Plan

## Objective

Define the actual mixed-source workflow that a technical builder will use when assembling chatbot context from documents and database-backed records.

## Task Status

IMPLEMENTED

## Inputs

- [Story 4 - Documents Plus Database Workflow](../story_4_documents_plus_database_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- outputs from Story 2 source-coverage work

## Proposed Work

### PR - A: Mixed-Source Scenario Definition

- choose the example scenario and data shape for the technical-builder workflow
- define the supported path for docs plus record-backed inputs
- keep the scenario representative but not overly broad

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `README.md`
- `examples/README.md`
- `src/context_atlas/adapters/records/__init__.py`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`

### PR - B: Mixed-Source Workflow Implementation

- implement the example composition path for docs plus database-backed records
- ensure both source families enter the same packet path
- preserve packet and trace inspection for the full workflow

#### Expected New Files
- `examples/docs_database_workflow/README.md`
- `examples/docs_database_workflow/run.py`

#### Expected Existing Files Updated
- `src/context_atlas/adapters/records/structured.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/rendering/context.py`

#### Update AI files
- `.`
- `src/context_atlas/adapters/`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/rendering/`
- `tests/`

### PR - C: Workflow Validation

- validate the workflow against realistic chatbot questions
- inspect packet and trace output for mixed-source coherence
- refine the example if it still looks stitched together rather than shared-engine-driven

#### Expected New Files
- `tests/test_docs_database_workflow.py`

#### Expected Existing Files Updated
- `examples/docs_database_workflow/run.py`
- `src/context_atlas/services/assembly.py`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/services/`
- `tests/`

## Sequencing

- define the mixed-source scenario first
- implement the workflow second
- validate and refine the workflow third

## Risks And Unknowns

- The scenario may be too abstract if the record source is not concrete enough.
- Mixed-source ranking may reveal new policy assumptions.
- It may be tempting to hide complexity in the example instead of clarifying boundaries.

## Exit Criteria

- there is a concrete docs-plus-db workflow shape
- both source families flow through one shared packet path
- packet and trace outputs make sense for the mixed-source scenario

## Related Artifacts

- [Story 4 - Documents Plus Database Workflow](../story_4_documents_plus_database_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
