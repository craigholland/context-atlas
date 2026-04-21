---
id: context-atlas-context-assembly-hardening-product-definition
title: Context Atlas Context Assembly Hardening Product Definition
summary: Defines the post-MVP hardening epic for retrieval performance, duplicate-detection quality, token estimation, and truthful budget/compression behavior.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, planning, performance, retrieval, ranking, budgeting, compression]
related:
  - ../../Authoritative/Identity/Context-Atlas-Charter.md
  - ../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../../Authoritative/Canon/Ontology/Documentation-Ontology.md
  - ../MVP/mvp_product_defintiion.md
supersedes: []
---

# Context Atlas Context Assembly Hardening Product Definition

## Objective

Define the next post-MVP hardening epic for Context Atlas so that the shared
assembly engine remains credible as corpora, duplicate content, and budget
pressure become more realistic than the small-starter cases used during the MVP
phase.

This epic is successful only if Context Atlas improves four qualities together:

- retrieval performance on larger static corpora
- duplicate-detection quality across ranking and memory
- token-estimation realism and extensibility
- truthful budget and compression artifacts that accurately describe what the
  engine actually did

The goal is not to replace the current engine path. The goal is to harden the
same shared engine path so that its behavior stays performant, legible, and
trustworthy under more realistic use.

## Inputs

- [Context Atlas Charter](../../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Documentation Ontology](../../Authoritative/Canon/Ontology/Documentation-Ontology.md)
- [Context Atlas MVP Product Definition](../MVP/mvp_product_defintiion.md)
- current retrieval, ranking, budgeting, compression, and memory code under
  `src/context_atlas/`
- recent review findings covering:
  - TF-IDF recomputation on every query
  - naive content deduplication in ranking
  - overly blunt `chars_per_token = 4` budgeting/compression heuristic
  - ambiguous `ContextBudget.remaining_tokens` semantics for elastic slots
  - extractive-compression fallback reporting that can misstate actual behavior
  - fragile prefix-based memory deduplication

## Proposed Work

### Hardening Thesis

Context Atlas should remain one shared context-assembly engine, but that engine
should no longer rely on MVP-only shortcuts where they now create avoidable
friction or misleading artifacts.

The hardening work should treat the current review findings as directionally
valid, with three important refinements:

- the TF-IDF concern is a real performance issue, not just a style preference;
  repeated full-corpus recomputation should move to a precomputed or lazily
  cached index path
- the duplicate-detection concerns are also real, but the fix is not "reuse the
  current memory heuristic as-is"; ranking and memory should instead converge on
  one improved shared duplicate-detection surface
- the budget-slot concern is primarily a semantics and contract-truth issue
  rather than a happy-path allocator failure; the allocator mostly behaves
  sensibly today, but the exposed artifact names and meanings are easier to
  misunderstand than they should be

### Product Shape

This epic should preserve the current product shape:

- one shared retrieval, ranking, budgeting, memory, compression, and packet path
- one canonical packet and trace model
- one set of outward composition helpers in `infrastructure/` and `services/`
- one set of product-facing guides and examples built on top of that shared path

The hardening work should not fork the engine into a "fast path," "accurate
path," and "starter path." Instead, it should improve the single supported path
while preserving deterministic behavior and inspectable trace artifacts.

### Core Capability Areas

The epic should establish or strengthen these capability areas:

- precomputed or lazily cached lexical retrieval indexes for repeated queries,
  including both corpus-wide IDF statistics and reusable per-document token/TF
  state
- one shared duplicate-detection surface usable by both ranking and memory
- better handling of boilerplate, front matter, and near-duplicate content
- a more realistic starter token-estimation policy than one global
  `chars_per_token = 4` constant
- a provider-agnostic tokenizer injection seam that future integrations can bind
  without forcing provider-specific logic into the domain layer
- budget artifacts whose names and semantics stay truthful when elastic slots are
  present
- compression results that distinguish configured strategy from effective
  fallback behavior clearly enough for packet consumers and trace readers
- validation and documentation coverage that proves the hardened behavior rather
  than leaving it implicit in code

### Epic Structure

This document should be treated as a post-MVP hardening Epic.

The Epic consists of five Stories:

- Story 1: Retrieval Indexing And Performance
- Story 2: Duplicate Detection And Similarity Quality
- Story 3: Token Estimation And Tokenizer Seam
- Story 4: Budget And Compression Truthfulness
- Story 5: Validation, Documentation, And Hardening Proof

Each Story should preserve Craig Architecture boundaries:

- retrieval-index mechanics stay outward in adapters and composition layers
- duplicate-detection semantics that affect ranking and memory behavior should
  stay inward and reusable rather than fragmenting by workflow
- token-estimation contracts should remain provider-agnostic inward and bind to
  provider-specific tokenizers only at outer layers when those are introduced
- canonical packet, trace, budget, and compression artifacts should stay
  truthful rather than encoding hidden fallback or allocation assumptions
- later docs, guides, and proof updates should inherit the hardened semantics
  rather than narrating around stale artifacts

### Execution Model

This hardening Epic should execute through one long-lived Epic branch off
`development`, with one Story branch per Story and one Task feature branch per
Task.

The intended delivery path is:

- Epic branch: accumulates completed Story branches and carries the Epic PR into
  `development`
- Story branch: accumulates completed Task feature branches and carries the
  Story PR into the Epic branch once that Story is finished
- Task feature branch: carries the full Task implementation and receives the
  Task-level review gate before merge into the Story branch
- PR-slice branches: branch from the Task feature branch and merge back into the
  Task feature branch as bounded implementation slices

For this Epic, the review gate is at the Task feature PR rather than waiting
until the whole Story is complete. Story PRs should therefore be assembled from
Tasks that have already finished their Task-level implementation, preflight, and
review cycle.

### Target Users

The first target users for this epic are internal and integration-oriented.

`1. Atlas workflow integrator`

- Primary job: use the shared assembly engine against a growing governed corpus
- Value from this epic: repeated queries become cheaper, duplicate-heavy corpora
  become less noisy, and budget behavior stays easier to reason about

`2. Atlas maintainer`

- Primary job: evolve retrieval, ranking, budgeting, compression, and memory
  without losing trust in the packet and trace artifacts
- Value from this epic: better internal seams for indexing, duplicate
  detection, token estimation, and fallback reporting

`3. Reviewer or evaluator`

- Primary job: inspect packet, trace, and proof artifacts and decide whether the
  engine behaved correctly
- Value from this epic: compression, budget, and duplicate-handling outcomes are
  more truthful and less dependent on reading deep implementation details

`4. Product-facing guide and example maintainer`

- Primary job: keep guides, examples, and proof artifacts aligned with what the
  engine actually does
- Value from this epic: fewer hidden implementation shortcuts leaking into docs
  or requiring explanatory caveats

## Deliverables

This epic should ultimately produce:

- one retrieval indexing story that removes full TF-IDF recomputation from the
  steady-state repeated-query path, including reuse of both document-frequency
  state and per-document vector-building work
- one shared duplicate-detection surface that both ranking and memory can use
  without inheriting the current fragile prefix heuristic unchanged
- one starter token-estimation improvement plus a provider-agnostic tokenizer
  seam for future integrations
- one clarified budget and compression artifact story in which callers can tell
  what was reserved, what was allocated, and which compression behavior actually
  happened
- updated regression tests, proof artifacts, and product-facing docs for the
  hardened semantics

## Non-Goals For This Epic

- building a persistent on-disk search index or retrieval service
- replacing lexical retrieval with a broader vector or semantic retrieval stack
- shipping provider-specific tokenizers for every possible model family in this
  phase
- introducing embedding-based semantic duplicate detection as the new baseline
- redesigning the full packet model or assembly service into a new engine path
- broad connector work unrelated to the reviewed retrieval/ranking/budgeting/
  compression concerns

## Sequencing

`Story 1: Retrieval Indexing And Performance`

- Goal: remove repeated full-corpus TF-IDF recomputation from normal repeated
  query behavior.
- Primary implementation areas:
  - `adapters/retrieval/lexical.py`
  - registry/index ownership boundaries
  - retrieval tests and performance-oriented proof coverage
- Architectural intent:
  - the retriever should still consume canonical sources from the registry
  - precomputed index state should remain an outward retrieval concern rather
    than becoming a new domain model
- Expected outcome: repeated queries over a static in-memory corpus reuse
  indexed state instead of rebuilding document frequency, per-document token
  state, and per-document vectors on every call.

`Story 2: Duplicate Detection And Similarity Quality`

- Goal: improve duplicate handling in ranking and memory without depending on
  exact full-text matches or the current fragile prefix heuristic.
- Primary implementation areas:
  - `domain/policies/ranking.py`
  - `domain/policies/memory.py`
  - any shared duplicate-detection helper surface introduced for both
  - ranking and memory regression coverage
- Architectural intent:
  - duplicate-detection semantics should be shared where the meaning is shared
  - workflow-specific duplication logic should not fork silently between ranking
    and memory
  - the hardening work should improve memory dedup as well, not simply export
    today's memory heuristic into ranking
- Scope ceiling:
  - this Story should deliver one clearly bounded lexical/structural
    near-duplicate baseline for Atlas-owned text, not an open-ended semantic
    similarity initiative
  - this Story should not expand into embeddings, provider-specific similarity
    services, or a generalized content-clustering system
- Expected outcome: near-duplicate documents with minor wording changes are less
  likely to crowd the same packet, while boilerplate or front-matter prefixes
  alone no longer trigger easy false positives.

`Story 3: Token Estimation And Tokenizer Seam`

- Goal: replace the one-size-fits-all character heuristic with a more realistic
  starter estimation model while introducing a future-safe tokenizer seam.
- Required kickoff decision:
  - this Story must begin by deciding whether the implementation priority is
    `heuristic-first` or `tokenizer-seam-first`
  - contributors should not advance implementation until that decision is
    recorded at the Story or Task layer
- Primary implementation areas:
  - `domain/policies/compression.py`
  - settings/config wiring for estimation behavior
  - outer composition helpers where a tokenizer contract may be injected later
- Architectural intent:
  - the starter heuristic should stay provider-agnostic and deterministic
  - future provider tokenizers should bind outward through a contract rather
    than pulling provider logic into the domain layer
- Expected outcome: Atlas no longer assumes that prose, code, markdown, and
  other content all map cleanly to one global `chars_per_token` ratio, while
  still preserving a simple supported starter path.

`Story 4: Budget And Compression Truthfulness`

- Goal: make budget and compression artifacts describe actual behavior clearly,
  especially when elastic slots and fallback compression paths are involved.
- Primary implementation areas:
  - `domain/models/budget.py`
  - `domain/policies/budgeting.py`
  - `domain/models/transformations.py`
  - `domain/policies/compression.py`
  - service-layer trace/metadata expectations in `services/assembly.py`
- Architectural intent:
  - canonical artifacts should tell the truth about what was reserved,
    allocated, transformed, or reduced
  - result and trace semantics should not require consumers to infer actual
    behavior from secondary metadata keys alone
- Expected outcome: packet consumers and reviewers can tell whether a budget
  value represents reserved capacity, post-allocation remainder, or another
  concept, and can also tell whether extractive compression truly succeeded or
  actually fell back to truncation.

`Story 5: Validation, Documentation, And Hardening Proof`

- Goal: prove the hardened semantics through tests, proof artifacts, and docs.
- Dependency note:
  - this Story depends on Story 4 settling the canonical budget and compression
    semantics cleanly enough that validation and docs are not forced to target a
    moving contract
- Primary implementation areas:
  - tests covering retrieval index reuse, duplicate handling, token estimation,
    budget semantics, and compression truthfulness
  - relevant guides, examples, and release-facing docs
  - proof artifacts or reproducible demonstrations where those behaviors matter
- Architectural intent:
  - validation should confirm the shared engine path, not a bespoke proof-only
    path
  - docs should describe the hardened semantics directly rather than relying on
    implementation folklore
- Expected outcome: the repo can explain and validate the new behavior
  confidently without leaving the review findings as standing caveats.

## Risks And Unknowns

- Precomputed indexing can easily overcomplicate a starter adapter if cache
  ownership and invalidation rules are not kept small and explicit.
- Improving duplicate detection may change ranking and memory outcomes in ways
  that surface previously hidden assumptions in tests or guides.
- Story 2 can easily sprawl unless the project holds the line on one bounded
  shared near-duplicate baseline rather than treating this epic as a general
  semantic-similarity initiative.
- A tokenizer seam can become a layering leak if provider-specific assumptions
  move inward too early.
- Clarifying budget and compression semantics may require canonical model or
  trace metadata changes that ripple into renderers, examples, and proof
  artifacts.
- Story 3 should treat the `heuristic-first` versus `tokenizer-seam-first`
  choice as an explicit decision gate, not just a risk to monitor, so the epic
  does not deliver a half-improved heuristic and a half-formed seam in the same
  increment.

## Exit Criteria

- repeated lexical TF-IDF retrieval over a static registry no longer recomputes
  full corpus weights on every query
- ranking and memory duplicate handling use a shared improved semantic surface
  or contract rather than exact full-text matching on one side and a fragile
  prefix heuristic on the other
- the starter token-estimation story is more realistic than one global
  `chars_per_token = 4` constant and leaves a clean provider-agnostic seam for
  future tokenizer injection
- budget artifacts and compression artifacts truthfully describe actual runtime
  behavior without forcing consumers to reconstruct meaning from secondary
  metadata alone
- tests, docs, and proof artifacts are updated so the new behavior is visible,
  reproducible, and reviewable
