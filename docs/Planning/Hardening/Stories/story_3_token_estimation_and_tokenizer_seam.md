---
id: context-atlas-hardening-story-3-token-estimation-and-tokenizer-seam
title: Story 3 - Token Estimation And Tokenizer Seam
summary: Defines how Context Atlas should improve starter token estimation and introduce a future-safe provider-agnostic tokenizer seam without solving both concerns halfway.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, story, token-estimation, tokenizer, budgeting, compression]
related:
  - ../context_assembly_hardening_product_definition.md
  - ./story_4_budget_and_compression_truthfulness.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../../../../src/context_atlas/domain/policies/compression.py
  - ../../../../src/context_atlas/infrastructure/config/settings.py
supersedes: []
---

# Story 3 - Token Estimation And Tokenizer Seam

## Objective

Replace the blunt one-size-fits-all `chars_per_token` assumption with a more
truthful starter story for token estimation while also defining a clean
provider-agnostic tokenizer seam for later integrations, and force an explicit
decision about which of those two concerns leads implementation.

## Inputs

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Story 4 - Budget And Compression Truthfulness](./story_4_budget_and_compression_truthfulness.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current estimation and compression behavior under
  `src/context_atlas/domain/policies/compression.py`
- current settings and composition surfaces under
  `src/context_atlas/infrastructure/config/` and `src/context_atlas/infrastructure/`

## Proposed Tasks

### Task 1: Kickoff Decision Gate

- record an explicit Story-level decision of `heuristic-first` or
  `tokenizer-seam-first` before implementation begins
- record that decision in this Story doc before Task 2 starts, and restate it
  in the first Task-level plan or PR slice that implements the chosen path
- define what success means for the chosen lead path
- prevent the Story from delivering a half-improved heuristic and a half-formed
  seam in the same increment

### Task 2: Starter Estimation Improvement

- define a bounded improved starter heuristic that better distinguishes prose,
  code, markdown-heavy content, or other obvious content-shape differences
- keep the starter estimation deterministic and provider-agnostic
- avoid turning the heuristic into a hidden provider-specific token model

### Task 3: Tokenizer Contract Seam

- define where a future tokenizer contract belongs and where it must not leak
  inward
- keep provider-specific tokenizer bindings outward in composition or
  infrastructure layers
- make the seam explicit enough that a future integration can bind to it
  without reworking domain-layer policy semantics

### Task 4: Validation And Configuration Alignment

- validate the chosen estimation path through tests and packet-facing behavior
- update runtime-surface or configuration docs only if the Story actually
  introduces a supported operator-facing knob
- keep the Story's docs honest about whether Atlas is using an improved
  heuristic, a tokenizer seam, or both

## Sequencing

- record the kickoff decision gate first
- implement the chosen lead path next
- introduce the complementary seam or heuristic only insofar as the decision
  allows
- finish with validation and doc alignment against the actual delivered shape

## Risks And Unknowns

- The fastest failure mode is trying to solve the heuristic concern and the
  tokenizer-seam concern equally at once.
- A more realistic heuristic can still become misleading if it quietly encodes
  provider assumptions instead of content-shape assumptions.
- A tokenizer seam can become a layering leak if provider-specific concepts
  move inward too early.

## Exit Criteria

- the Story records whether the implementation is `heuristic-first` or
  `tokenizer-seam-first`
- Atlas no longer relies exclusively on one global `chars_per_token = 4`
  assumption for all starter estimation behavior
- a provider-agnostic tokenizer contract seam exists or is explicitly bounded
  by the kickoff decision without leaking provider specifics into the domain
  layer
- tests and docs make the delivered estimation story legible enough that
  callers do not need to infer it from implementation details

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- token-estimation behavior remains provider-agnostic inward and binding-aware
  outward
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
