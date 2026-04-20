---
id: context-atlas-mvp-story-5-low-code-workflow
title: Story 5 - Low-Code Workflow
summary: Defines the simplified preset-driven workflow that exposes Context Atlas to a lower-code builder without creating a separate engine.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, story, low-code, presets, configuration]
related:
  - ../mvp_product_defintiion.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 5 - Low-Code Workflow

## Objective

Create a simplified configuration and preset-driven path that lets a lower-code builder use Context Atlas without custom composition code for every step.

## Inputs

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- Stories 1 through 4, especially the stabilized product surface and source adapters

## Proposed Tasks

### Task 1: Workflow Shape

- allow a user to declare source roots, source types, and basic runtime knobs through configuration
- provide one or more presets that select sane defaults for assembly behavior
- produce the same packet and trace artifacts as the technical workflows

### Task 2: Product Deliverables

- one low-code setup guide
- one example preset or profile surface
- one minimal wrapper or entry surface that avoids custom Python composition for ordinary setup

### Task 3: Architectural Shape

- presets and low-code configuration belong to outer configuration, infrastructure, or example surfaces
- canonical policy and packet semantics remain shared with every other workflow
- the low-code path must not become a forked engine with different internal behavior

## Sequencing

- identify the smallest configuration surface that makes the workflow meaningfully lower-code
- define one or more presets
- wire the presets into the supported starter composition path
- write and validate the low-code setup guide

## Risks And Unknowns

- The low-code path could accidentally become a second product instead of a wrapper around the same engine.
- Too many presets too early could freeze weak abstractions.
- A simplified workflow can hide too much unless packet and trace inspection remain visible.

## Exit Criteria

- a lower-code user can reach a working Atlas flow without assembling every component manually
- the workflow still produces canonical packet and trace artifacts
- presets remain clearly outer-layer configuration rather than domain truth
- the workflow reinforces Atlas as a reusable component rather than a separate low-code product

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md` files in the same slice
- the supported docs, examples, and runtime knobs stay aligned with the implemented surface
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives `@codex review`, and any review findings are resolved on that same feature branch before human merge
- any deviations from Craig Architecture boundaries are documented explicitly rather than left implicit

## Related Artifacts

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)

