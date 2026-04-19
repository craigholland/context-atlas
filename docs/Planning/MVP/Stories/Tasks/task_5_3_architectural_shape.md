---
id: context-atlas-mvp-task-5-3-architectural-shape
title: Task 5.3 - Architectural Shape PR Plan
summary: Defines the PR sequence for keeping the low-code workflow as a thin outer product surface over the shared Atlas engine.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, task, pr-plan, low-code, architecture, configuration]
related:
  - ../story_5_low_code_workflow.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 5.3 - Architectural Shape PR Plan

## Objective

Ensure the low-code workflow remains an outer product surface and preset layer, not a second Atlas engine with its own semantics.

## Task Status

PLANNED

## Inputs

- [Story 5 - Low-Code Workflow](../story_5_low_code_workflow.md)
- [Context Atlas MVP Product Definition](../../mvp_product_defintiion.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- outputs from Tasks 5.1 and 5.2

## Proposed Work

### PR - A: Preset And Wrapper Boundary Audit

- inspect the low-code flow for logic that has drifted inward
- identify preset or wrapper behavior that is acting like hidden policy
- confirm which configuration decisions belong to outer layers only

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/infrastructure/config/presets.py`
- `src/context_atlas/infrastructure/assembly.py`
- `examples/low_code_workflow/run.py`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`

### PR - B: Boundary-Conforming Refactor

- move hidden policy or semantic behavior back to the correct layer
- keep presets and wrappers in configuration or composition surfaces
- preserve the same canonical packet, trace, and service contracts used elsewhere

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/infrastructure/config/presets.py`
- `src/context_atlas/infrastructure/config/settings.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/services/assembly.py`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/services/`
- `tests/`

### PR - C: Architecture Reinforcement

- document how low-code surfaces should be built without forking the engine
- add focused checks or examples that reinforce the boundary
- ensure future low-code extensions inherit the right pattern

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `__ai__.md`
- `src/context_atlas/infrastructure/__ai__.md`
- `src/context_atlas/services/__ai__.md`
- `README.md`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/services/`

## Sequencing

- audit first
- refactor second
- reinforce guidance and checks third

## Risks And Unknowns

- Low-code convenience paths can hide policy decisions very easily.
- Presets may start behaving like alternate domain truth unless kept outward.
- The simplest user experience may not always align with the cleanest architecture.

## Exit Criteria

- the low-code workflow remains an outer-layer wrapper over the shared engine
- presets do not replace or fork canonical policy semantics
- the workflow remains aligned with Craig Architecture

## Related Artifacts

- [Story 5 - Low-Code Workflow](../story_5_low_code_workflow.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
