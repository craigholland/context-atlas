---
id: context-atlas-hardening-task-4-4-trace-renderer-and-service-alignment
title: Task 4.4 - Trace, Renderer, And Service Alignment PR Plan
summary: Defines the PR sequence for aligning service traces and derived renderers with the clarified budget and compression semantics after the canonical artifacts settle.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, trace, rendering, services]
related:
  - ../story_4_budget_and_compression_truthfulness.md
  - ../../context_assembly_hardening_product_definition.md
  - ../../../../../src/context_atlas/services/assembly.py
  - ../../../../../src/context_atlas/rendering/context.py
  - ../../../../../src/context_atlas/rendering/packet.py
  - ../../../../../src/context_atlas/rendering/trace.py
supersedes: []
---

# Task 4.4 - Trace, Renderer, And Service Alignment PR Plan

## Objective

Align service-layer trace output and derived renderers with the settled budget
and compression semantics so review surfaces consume canonical truth instead of
quietly preserving stale field assumptions.

## Task Status

IMPLEMENTED

## Inputs

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
- completed canonical semantics from Tasks 4.1 through 4.3
- current service and rendering files:
  - `src/context_atlas/services/assembly.py`
  - `src/context_atlas/rendering/context.py`
  - `src/context_atlas/rendering/packet.py`
  - `src/context_atlas/rendering/trace.py`

## Proposed Work

### PR - A: Service Trace Alignment

- align service-layer trace and packet metadata with the settled budget and
  compression semantics
- keep the canonical truth in service outputs rather than patching around it in
  renderers

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/services/assembly.py`
- `tests/test_context_assembly_service.py`

#### Update AI files
- `src/context_atlas/services/`
- `tests/`

### PR - B: Renderer Alignment

- update `rendering/context.py`, `rendering/packet.py`, and `rendering/trace.py`
  to consume the clarified canonical fields and semantics
- make renderer behavior fail-safe against the renamed or clarified artifact
  surfaces
- ensure tests and smoke-style rendering expectations reflect the new truth

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/rendering/context.py`
- `src/context_atlas/rendering/packet.py`
- `src/context_atlas/rendering/trace.py`
- `tests/test_packet_rendering.py`
- `tests/test_trace_rendering.py`

#### Update AI files
- `src/context_atlas/rendering/`
- `tests/`

### PR - C: Story And Proof Handoff

- align Story 4 and Story 5 with the settled service and rendering surfaces
- reduce the chance that Story 5 documents old field names or stale renderer
  expectations

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_4_budget_and_compression_truthfulness.md`
- `docs/Planning/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md`

#### Update AI files
- `.`

## Sequencing

- align service traces first
- align derived renderers second
- hand the settled surface cleanly to Story 5 last

## Risks And Unknowns

- Renderer files can silently preserve stale assumptions even when domain and
  service changes type-check cleanly.
- Story 5 can document outdated field names if the final handoff is skipped.

## Exit Criteria

- service traces reflect the settled budget and compression truth
- renderers consume the clarified canonical surfaces correctly
- Story 5 inherits stable trace and renderer semantics for later proof/docs work

## Current Delivered Result

- service packet and trace metadata now surface truthful top-level compression
  strategy fields (`compression_strategy` and optional
  `configured_compression_strategy`) instead of requiring renderer consumers to
  infer them only from prefixed stage metadata
- packet inspection rendering now shows `unallocated_tokens` when the service
  provides it and distinguishes `effective_strategy` from
  `configured_strategy`
- trace highlight and inspection rendering now expose the settled budget and
  compression semantics directly enough that Story 5 can document those
  surfaces without referring back to stale field assumptions

## Related Artifacts

- [Story 4 - Budget And Compression Truthfulness](../story_4_budget_and_compression_truthfulness.md)
- [Story 5 - Validation, Documentation, And Hardening Proof](../story_5_validation_documentation_and_hardening_proof.md)
