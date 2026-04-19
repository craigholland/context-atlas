---
id: context-atlas-mvp-task-6-4-architectural-shape
title: Task 6.4 - Architectural Shape PR Plan
summary: Defines the PR sequence for ensuring MVP proof evaluates the real shared engine rather than bespoke demo shortcuts.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, proof, architecture, reproducibility]
related:
  - ../story_6_mvp_proof.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 6.4 - Architectural Shape PR Plan

## Objective

Ensure the MVP proof path evaluates the real Atlas architecture and supported engine rather than hidden demo-specific shortcuts.

## Task Status

IMPLEMENTED

## Inputs

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- outputs from Tasks 6.1 through 6.3

## Proposed Work

### PR - A: Proof-Path Architecture Audit

- inspect proof scripts, examples, and evidence capture for architecture shortcuts
- identify cases where the proof path bypasses the supported engine or packet/trace model
- ensure the proof story evaluates the real product surface

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `scripts/mvp_proof/capture_evidence.py`
- `examples/mvp_proof/README.md`
- `README.md`

#### Update AI files
- `.`
- `scripts/`

### PR - B: Proof-Harness Refactor

- refactor proof utilities that do not respect the shared engine path
- keep evaluation composition outward and evidence artifacts canonical
- preserve reproducibility and inspectability

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `scripts/mvp_proof/capture_evidence.py`
- `examples/codex_repository_workflow/run.py`
- `examples/docs_database_workflow/run.py`
- `examples/low_code_workflow/run.py`

#### Update AI files
- `.`
- `scripts/`
- `src/context_atlas/infrastructure/`

### PR - C: Architecture Reinforcement For Proof

- document the proof-path architecture clearly
- add focused checks or examples that keep the proof honest over time
- ensure the proof itself exemplifies Craig Architecture discipline

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `__ai__.md`
- `scripts/__ai__.md`
- `README.md`

#### Update AI files
- `.`
- `scripts/`

## Sequencing

- audit the proof path first
- refactor any shortcuts second
- reinforce the architecture in docs and checks third

## Risks And Unknowns

- Demo-oriented proof harnesses often accumulate special-case shortcuts.
- Reproducibility work may surface new product-surface gaps.
- The proof path may require more outer tooling than currently expected.

## Exit Criteria

- the proof path evaluates the real shared engine
- proof harnesses do not depend on hidden shortcuts
- MVP proof remains aligned with Craig Architecture and canonical Atlas artifacts

## Related Artifacts

- [Story 6 - MVP Proof](../story_6_mvp_proof.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
