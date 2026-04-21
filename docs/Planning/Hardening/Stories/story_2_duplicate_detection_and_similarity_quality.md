---
id: context-atlas-hardening-story-2-duplicate-detection-and-similarity-quality
title: Story 2 - Duplicate Detection And Similarity Quality
summary: Defines how ranking and memory should converge on one bounded improved duplicate-detection surface without inheriting the weaknesses of either current heuristic unchanged.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [hardening, story, deduplication, ranking, memory, similarity]
related:
  - ../context_assembly_hardening_product_definition.md
  - ./story_1_retrieval_indexing_and_performance.md
  - ./story_3_token_estimation_and_tokenizer_seam.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../../../../src/context_atlas/domain/policies/ranking.py
  - ../../../../src/context_atlas/domain/policies/memory.py
supersedes: []
---

# Story 2 - Duplicate Detection And Similarity Quality

## Objective

Improve duplicate handling so ranking and memory share one bounded
near-duplicate surface that is stronger than exact full-text matching and
stronger than the current fragile prefix heuristic, while still staying small,
deterministic, and Atlas-owned.

## Inputs

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Story 1 - Retrieval Indexing And Performance](./story_1_retrieval_indexing_and_performance.md)
- [Story 3 - Token Estimation And Tokenizer Seam](./story_3_token_estimation_and_tokenizer_seam.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current ranking and memory policies under `src/context_atlas/domain/policies/`
- current regression coverage in `tests/test_candidate_ranking.py` and
  `tests/test_memory_policy.py`

## Proposed Tasks

### Task 1: Shared Duplicate-Detection Surface

- define one reusable duplicate-detection contract or helper surface for both
  ranking and memory
- treat the current intended home for that shared surface as `domain/policies/`
  or a directly adjacent inward helper module so contributors do not have to
  infer package placement during Task decomposition
- treat `domain/policies/deduplication.py` as the baseline inward home once
  Task 2.1 lands, so later tasks extend one shared helper surface instead of
  re-inventing duplicate logic inside ranking or memory separately
- keep the shared semantics inward and reusable rather than letting workflow
  logic fork silently between ranking and memory
- make the supported baseline explicitly lexical or structural rather than
  leaving room for hidden semantic-similarity assumptions
- Task 2.1 should close with one explicit baseline only: normalized exact-key
  matching, normalized containment, and token overlap; later tasks may refine
  normalization and integration, but they should not silently introduce new
  comparison families

### Task 2: Boilerplate And Front-Matter Handling

- improve normalization so common boilerplate or governed document headers do
  not dominate similarity decisions
- make it explicit how front matter, repeated templates, and shared prefixes
  should be treated before duplicate logic is applied
- avoid preserving the current prefix-equality shortcut as a standing baseline
- Task 2.2 should close with one bounded normalization rule only:
  top-of-file front matter may be stripped, and pairwise comparison may
  discount a bounded shared leading line prefix when both sides still retain
  meaningful body content
- Task 2.2 should not introduce format-specific stripping matrices, mid-document
  boilerplate removal, or template encyclopedias; those remain intentionally
  unsupported unless the Story boundary changes first

### Task 3: Ranking And Memory Integration

- replace ranking's exact full-text duplicate gate with the new shared surface
- replace or constrain memory's fragile prefix-heavy behavior with the same
  improved contract
- keep the integration deterministic and reviewable instead of introducing a
  fuzzy scoring scheme that is hard to reason about
- Task 2.3 should close with one explicit integration rule: ranking uses the
  shared duplicate assessment through an explicit `dedup_threshold` and remains
  source-family-aware, while memory exposes the shared duplicate match kind
  directly in duplicate decisions instead of hiding a second local shortcut

### Task 4: Scope Ceiling And Regression Proof

- define a bounded acceptance bar for "good enough" near-duplicate handling in
  Atlas-owned text
- make it explicit that this Story is not an embeddings, semantic-clustering,
  or provider-similarity initiative
- add regressions that prove the new shared surface is better than both prior
  approaches on the targeted failure cases
- Task 2.4 should close with one explicit acceptance bar: Atlas should
  collapse near-duplicate text when the meaningful body differs only by
  case/whitespace normalization, bounded top-of-file front matter,
  normalized containment, or reordered lexical tokens within the configured
  threshold
- the same acceptance bar should preserve distinct text when the apparent
  similarity is driven mostly by shared boilerplate/header material,
  metadata-only front matter, or cross-source-family provenance in ranking
- exact full-text equality and the former prefix-equality shortcut are now
  historical failure baselines, not acceptable standing duplicate strategies
  or fallback modes

## Sequencing

- define the shared duplicate-detection surface first
- settle boilerplate and front-matter handling before wiring it into both
  policies
- integrate ranking and memory after the bounded semantic surface is explicit
- lock the Story with regressions that prove the new baseline is better than
  both prior heuristics
- keep Task 2.1 focused on defining and proving the shared lexical baseline
  before boilerplate handling or full ranking integration begins

## Risks And Unknowns

- This Story can sprawl quickly if contributors treat "improved similarity" as
  permission to pursue a generalized semantic-dedup initiative.
- Boilerplate handling can become too clever if the implementation starts
  encoding document-type-specific special cases instead of a bounded baseline.
- Ranking and memory may expose different edge cases once they share one
  duplicate surface, so test changes may need careful interpretation.

## Exit Criteria

- ranking and memory use one shared improved duplicate-detection surface or
  contract
- the shared surface is clearly better than exact full-text matching and better
  than the current fragile prefix heuristic on the reviewed failure modes
- boilerplate or front-matter prefixes alone no longer dominate duplicate
  decisions
- the Story leaves one explicit acceptance bar naming what should collapse and
  what must remain distinct, so later work does not reopen Story 2 implicitly
- the Story remains bounded to one lexical or structural near-duplicate
  baseline rather than drifting into a broader semantic-similarity initiative

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- duplicate-detection semantics stay shared and inward rather than being
  re-forked by ranking versus memory behavior
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [Context Assembly Hardening Product Definition](../context_assembly_hardening_product_definition.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
