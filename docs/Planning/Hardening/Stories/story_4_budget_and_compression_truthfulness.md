---
id: context-atlas-hardening-story-4-budget-and-compression-truthfulness
title: Story 4 - Budget And Compression Truthfulness
summary: Defines how Context Atlas should make budget and compression artifacts describe actual runtime behavior clearly when elastic slots and fallback paths are involved.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, story, budgeting, compression, semantics, trace]
related:
  - ../context_assembly_hardening_product_definition.md
  - ./story_3_token_estimation_and_tokenizer_seam.md
  - ./story_5_validation_documentation_and_hardening_proof.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../../../../src/context_atlas/domain/models/budget.py
  - ../../../../src/context_atlas/domain/models/transformations.py
  - ../../../../src/context_atlas/domain/policies/budgeting.py
  - ../../../../src/context_atlas/domain/policies/compression.py
  - ../../../../src/context_atlas/services/assembly.py
supersedes: []
---

# Story 4 - Budget And Compression Truthfulness

## Objective

Make canonical budget and compression artifacts truthfully describe what Context
Atlas reserved, allocated, retained, or fell back to, so packet consumers and
reviewers do not have to reconstruct actual behavior from ambiguous names or
secondary metadata keys.

## Inputs

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Story 3 - Token Estimation And Tokenizer Seam](./story_3_token_estimation_and_tokenizer_seam.md)
- [Story 5 - Validation, Documentation, And Hardening Proof](./story_5_validation_documentation_and_hardening_proof.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current budget models, policies, compression models, and service trace code
  under `src/context_atlas/domain/` and `src/context_atlas/services/`
- current packet/trace rendering expectations under `src/context_atlas/rendering/`
- current derived renderers in:
  - `src/context_atlas/rendering/context.py`
  - `src/context_atlas/rendering/packet.py`
  - `src/context_atlas/rendering/trace.py`

## Proposed Tasks

### Task 1: Budget Artifact Semantics

- define the truthful meaning of budget values exposed through canonical models
- make it explicit which values represent reservations, which represent actual
  allocations, and which represent post-allocation remainder
- resolve the current elastic-slot tension without narrating around misleading
  property names
- current delivered Task 4.1 result:
  - `ContextBudget` now distinguishes fixed-slot reservation
    (`fixed_reserved_tokens`) from pre-allocation unreserved capacity
    (`unreserved_tokens`)
  - `BudgetAllocationOutcome` now exposes true post-allocation remainder as
    `unallocated_tokens`
  - compatibility aliases remain temporarily in place for
    `reserved_tokens` and `remaining_tokens` so Task 4.2 can finish the
    caller-facing contract cleanup without breaking downstream Story work

### Task 2: Elastic Slot Behavior And Caller Contracts

- make the elastic-slot story explicit enough that callers and future tests do
  not misread the budget model
- preserve the existing allocator's sensible behavior where it is already
  correct
- change names, properties, or trace semantics where contract truth requires
  it rather than leaving the ambiguity in place
- Task 4.2 should treat `ContextBudget.reserved_tokens`,
  `ContextBudget.remaining_tokens`, and outward `remaining_tokens` metadata keys
  as legacy compatibility surfaces rather than the preferred caller contract

### Task 3: Compression Result Truthfulness

- define how configured compression strategy and effective fallback behavior are
  represented in canonical compression results
- prevent a result surface from claiming extractive behavior when the effective
  runtime action was truncation
- keep fallback visibility in the primary artifact surface rather than hiding it
  only in secondary metadata
- Task 4.3 should make `strategy_used` truthful for the effective runtime
  strategy and use a separate configured-strategy surface only where fallback
  needs to remain visible

### Task 4: Trace, Renderer, And Service Alignment

- align service-layer trace metadata, packet surfaces, and derived renderers
  with the clarified budget and compression semantics
- treat `rendering/context.py`, `rendering/packet.py`, and
  `rendering/trace.py` as explicit in-scope renderer surfaces rather than
  leaving renderer impact implied
- keep the canonical truth in the domain and service artifacts, with renderers
  consuming rather than redefining those meanings
- settle these semantics cleanly enough that Story 5 can validate and document
  them without targeting a moving contract

## Sequencing

- clarify budget artifact semantics first
- settle elastic-slot caller contracts before adjusting trace or renderer output
- define compression result truthfulness next
- align service, trace, and rendering surfaces last once the canonical
  semantics are stable

## Risks And Unknowns

- This Story has the widest ripple potential because packet, trace, renderer,
  test, and guide surfaces all depend on the same semantics.
- It is easy to preserve happy-path behavior while still leaving contract names
  misleading if the work stops at implementation and avoids artifact truth.
- Compression fallback reporting can become overcomplicated if the Story tries
  to expose every internal decision instead of the minimum truthful result
  surface.

## Exit Criteria

- budget artifacts truthfully distinguish reservation, allocation, and
  remainder semantics where those concepts differ
- elastic-slot behavior is legible enough that callers are not nudged toward
  incorrect assumptions by misleading property names
- compression artifacts truthfully represent effective runtime behavior,
  including fallback from configured strategy to actual strategy
- service, trace, and rendering surfaces inherit the clarified semantics
  instead of compensating for ambiguity with informal notes

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- canonical truth stays in the shared budget, compression, packet, and trace
  surfaces rather than in renderer-specific interpretation
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
