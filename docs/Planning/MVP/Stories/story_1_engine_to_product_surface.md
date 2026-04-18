---
id: context-atlas-mvp-story-1-engine-to-product-surface
title: Story 1 - Engine To Product Surface
summary: Defines how Context Atlas should turn its current starter engine into a supported MVP-facing product surface.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, story, surface, api, inspection]
related:
  - ../mvp_product_defintiion.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 1 - Engine To Product Surface

## Objective

Make the current starter implementation feel like a supported product surface rather than a collection of internal parts that a user must discover manually.

## Inputs

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
- Current package surface in `src/context_atlas/`
- Current runtime settings surface in `.env.example`

## Proposed Tasks

### Task 1: Supported Entry Surface

- define the intended public imports a new user should reach for first
- tighten package exports so the starter assembly path is obvious
- reduce the need to import deep internal modules just to assemble a first packet

### Task 2: Packet And Trace Inspection

- add a first-class inspection surface for packets and traces
- keep inspection as a derived rendering concern rather than polluting canonical domain objects with presentation formatting
- make the packet/trace view usable by both humans and future demos

### Task 3: Product-Facing Guidance

- add a clear golden-path setup flow that shows installation, environment setup, assembly, and inspection
- align examples, runtime knobs, and docs so they describe one supported starter path rather than several partial paths

### Task 4: Craig Architecture Alignment

- `domain/` remains the home of canonical packet, trace, budget, memory, and source artifacts
- `services/` remains the home of orchestration
- `infrastructure/` owns supported starter wiring and settings loading
- `rendering/` owns human-readable packet and trace presentation
- the story should not move policy into services or hide core state inside string renderers

## Sequencing

- identify the intended public API and current friction points
- tighten the exported starter assembly path
- add packet and trace inspection helpers
- update examples and setup guidance to use the supported entrypoints
- validate that the golden path can be followed without reaching into arbitrary internals

## Risks And Unknowns

- It is easy to improve examples without actually stabilizing the product surface.
- There is a risk of over-exposing internal modules as public API too early.
- A packet inspector can drift into becoming the canonical representation if rendering and domain responsibilities are blurred.

## Exit Criteria

- a new user can identify the supported starter imports quickly
- a packet and its trace can be inspected without reading raw internal model dumps
- the setup path from install to first packet is documented and coherent
- the implementation still respects Craig Architecture layer boundaries

## Related Artifacts

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
