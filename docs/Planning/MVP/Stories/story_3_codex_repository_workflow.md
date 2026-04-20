---
id: context-atlas-mvp-story-3-codex-repository-workflow
title: Story 3 - Codex Repository Workflow
summary: Defines the flagship engineering workflow that uses Context Atlas as a repo-aware context-governance layer for Codex.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, story, codex, repository, workflow]
related:
  - ../mvp_product_defintiion.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 3 - Codex Repository Workflow

## Objective

Deliver the flagship workflow that shows Context Atlas improving repository-aware context for an engineer using Codex.

## Inputs

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- filesystem docs adapter and starter assembly service

## Proposed Tasks

### Task 1: Workflow Shape

- point Atlas at a repository's governed docs and related artifacts
- assemble a packet for an engineering question or task
- render the packet into a Codex-facing context block
- expose the trace so the engineer can inspect why material was included, excluded, or compressed

### Task 2: Product Deliverables

- one polished setup guide for the Codex repository path
- one runnable example or example directory
- one demonstration that shows packet plus trace output rather than only final rendered text

### Task 3: Architectural Shape

- keep repository-specific source collection in outer adapters or example wiring
- use the shared assembly service rather than creating a Codex-specific engine path
- keep Codex-facing formatting in rendering or example composition layers
- preserve the canonical packet and trace as the source of truth

## Sequencing

- define the minimum governed repository inputs for the workflow
- build or refine the example composition path
- write the setup guide
- validate that the workflow produces coherent packets and trace output for realistic engineering questions

## Risks And Unknowns

- The workflow can drift into being overly tailored to a single repository layout.
- There is a risk of conflating Codex integration with Context Atlas itself.
- Without clear trace output, the workflow may look like ordinary prompt assembly rather than governed context selection.

## Exit Criteria

- a Python engineer can follow the guide and run the Codex repository workflow
- the workflow uses the shared Atlas engine rather than bespoke logic
- packet and trace inspection are part of the workflow, not an afterthought
- the workflow convincingly shows Atlas as a repo-aware pipeline component

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

