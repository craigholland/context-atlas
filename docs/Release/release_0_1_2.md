---
id: release-0-1-2
title: Release 0.1.2
summary: Records the context-assembly hardening release of Context Atlas, covering retrieval reuse, shared duplicate handling, shape-aware token estimation, truthful budget and compression semantics, and the aligned proof/doc surface.
doc_class: releases
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [releases, hardening, version-0-1-2, context-assembly, product-surface]
related:
  - ./release_0_1_1.md
  - ../Planning/completed/Hardening/context_assembly_hardening_product_definition.md
  - ../Guides/README.md
  - ../../README.md
supersedes:
  - ./release_0_1_1.md
---

# Release 0.1.2

## Context

This document records the context-assembly hardening release of Context Atlas.

`0.1.2` builds directly on the governed operating model introduced in `0.1.1`
and applies that same discipline to the shared engine itself. The release does
not introduce a brand-new workflow family. Instead, it hardens the existing
retrieval, ranking, budgeting, compression, rendering, and documentation
surfaces so the product story is more truthful, more reviewable, and less
dependent on MVP-era shortcuts.

This release is the point where the repository's outward docs, packet/trace
inspection surfaces, and regression story now align with the hardened shared
engine behavior rather than describing known compromises as if they were still
the intended long-term contract.

## Shipped Capabilities

### Retrieval Reuse And TF-IDF Index Ownership

`0.1.2` ships a clearer retrieval boundary under
`src/context_atlas/adapters/retrieval/`.

The shared lexical retriever now:

- keeps registry ownership explicit
- caches one revision-aligned lexical index snapshot
- reuses corpus-wide IDF state and per-document TF/TF-IDF vector state across
  repeated queries
- preserves repeated-query behavior without rebuilding the full source-side
  TF-IDF picture on every call

This keeps the starter retrieval path fast enough to stay honest as the
governed corpus grows, without moving the engine onto a second proof-only or
benchmark-only retrieval implementation.

### Shared Duplicate-Handling Baseline

`0.1.2` also ships a real shared duplicate-detection surface under
`src/context_atlas/domain/policies/deduplication.py`.

That surface now gives ranking and memory one bounded duplicate baseline built
around:

- normalized exact-key matching
- bounded front-matter-aware normalization
- normalized containment
- token-overlap comparison

This release explicitly rejects the earlier extremes of:

- exact full-text equality only
- prefix-heavy duplicate shortcuts

The shipped behavior is intentionally better than both, while still remaining
lexical and structural rather than silently drifting into hidden semantic
similarity work.

### Shape-Aware Starter Estimation And Tokenizer Seam

`0.1.2` hardens the starter token-estimation story.

The default path is now shape-aware instead of assuming one flat
`chars_per_token` ratio for every kind of content. The shared engine tightens
the estimate for obviously structured code/markup and for non-Latin-heavy text
while staying provider-agnostic.

The release also introduces a bounded outward token-estimator seam so:

- the starter heuristic remains the default
- custom token-estimation behavior can be composed from infrastructure
- provider-specific tokenizer ownership still stays outside the core engine

### Truthful Budget And Compression Semantics

`0.1.2` makes the budget and compression surface more truthful across the
shared engine, service metadata, and rendering layers.

The shipped contract now distinguishes:

- `fixed_reserved_tokens`
- `unreserved_tokens`
- `unallocated_tokens`

instead of leaning on one ambiguous `remaining_tokens` story for every stage of
allocation.

Compression semantics are also clearer now:

- `strategy_used` reflects the effective runtime strategy
- `configured_strategy` is preserved separately when fallback matters
- packet and trace views surface `compression_strategy` and optional
  `configured_compression_strategy` directly

This means reviewers no longer have to infer whether truncation actually
happened, or whether a budget field is pre-allocation headroom versus true
post-allocation remainder.

### Proof, Documentation, And Example Alignment

`0.1.2` also closes the first hardening loop on the evidence and product-facing
surfaces.

This release ships:

- a named Story 5 hardening regression anchor set across retrieval, duplicate
  handling, budgeting, compression, service metadata, and rendering
- a bounded human-readable proof inventory under `examples/mvp_proof/`
- updated guides and example READMEs that now describe the hardened packet,
  trace, retrieval, and compression story directly
- an integrated hardening closeout assessment in the planning stack so the
  original review findings now map cleanly to shipped behavior

### Versioned Package Surface

`0.1.2` also updates the package-facing version surfaces so release metadata is
consistent across:

- `pyproject.toml`
- `context_atlas.__version__`
- the installable CLI version test
- in-repo release history under `docs/Release/`

## Known Gaps

`0.1.2` materially hardens the shared engine, but it still leaves several
follow-on improvements intentionally open.

- The retrieval path now reuses in-memory index state, but it still does not
  provide a persistent on-disk indexing or cache layer.
- Duplicate handling is now bounded and shared, but it still does not attempt
  embedding-backed or provider-backed semantic similarity.
- The starter estimator is shape-aware and composable, but the repository still
  does not expose a provider-specific tokenizer selector or env-backed tokenizer
  integration.
- The hardening proof story is now cleaner, but it still intentionally relies
  on the named regression anchor set for several behaviors instead of adding a
  second demo-artifact family for every hardened surface.
- Release prep is cleaner than before, but the repository still relies on a
  relatively manual promotion/tag/release cadence rather than a fuller
  publication automation pipeline.

## Future State

The next phase after `0.1.2` should build on the hardened shared engine instead
of reopening the same semantic questions.

Near-term follow-on work should emphasize:

- broader scenario and integration coverage over the hardened engine path
- persistent retrieval indexing or cache strategies where they add real value
- richer duplicate-detection or tokenizer integration only through explicit new
  contracts
- continued strengthening of release/process automation without weakening the
  packet-and-trace-centered proof story

The key principle should remain the same: preserve the truthful hardened
surface, then expand from that stable contract rather than letting later work
reintroduce ambiguous budget fields, hidden fallback behavior, or proof drift.

## Related Artifacts

- [Release 0.1.1](./release_0_1_1.md)
- [Context Assembly Hardening Product Definition](../Planning/completed/Hardening/context_assembly_hardening_product_definition.md)
- [Guides Index](../Guides/README.md)
- [Repository README](../../README.md)
