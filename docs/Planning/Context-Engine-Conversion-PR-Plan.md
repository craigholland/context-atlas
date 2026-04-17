---
id: context-engine-conversion-pr-plan
title: Context Engine Conversion PR Plan
summary: Sequences the initial Context Atlas implementation PRs for translating the useful concepts from context-engine into Atlas-native architecture.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-17
owners: [core]
tags: [planning, migration, bootstrap, context-engine]
related:
  - ../Authoritative/Identity/Context-Atlas-Charter.md
  - ../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../Authoritative/Architecture/Craig-Architecture.md
  - ../Authoritative/Architecture/Craig-Architecture-Python.md
  - ../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Context Engine Conversion PR Plan

## Objective

Translate the useful concepts from the sibling `context-engine` prototype into fresh, Atlas-native implementation slices without copying its flat module structure, hardcoded heuristics, or prompt-first data model.

This plan assumes the following conversion posture:

- Adopt the conceptual decomposition around retrieval, memory, compression, budgeting, and packet assembly.
- Adapt the current starter heuristics only as temporary policy implementations.
- Reject the flat package shape, sibling-import structure, inline semantic strings, random embedding fallback, and prompt-ready packet as canonical output.
- Defer persistence backends, embedding providers, external tokenizers, and richer provider integrations until the core structured assembly path is stable.

## Inputs

- [Context Atlas Charter](../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture Python](../Authoritative/Architecture/Craig-Architecture-Python.md)
- [Documentation Ontology](../Authoritative/Ontology/Documentation-Ontology.md)
- Existing Atlas bootstrap packages under `src/context_atlas/`
- Existing Atlas governance surface:
  - repo-level [`.env.example`](../../.env.example)
  - [`src/context_atlas/domain/errors/`](../../src/context_atlas/domain/errors/)
  - [`src/context_atlas/domain/messages/`](../../src/context_atlas/domain/messages/)
  - [`src/context_atlas/infrastructure/config/`](../../src/context_atlas/infrastructure/config/)
  - [`src/context_atlas/infrastructure/logging/`](../../src/context_atlas/infrastructure/logging/)
  - local `__ai__.md` files at the repo root, package root, `domain/`, and `infrastructure/`
- Sibling specimen repo at `K:\keven\codex_repo\context-engine`, especially:
  - `retriever.py`
  - `memory.py`
  - `compressor.py`
  - `context_engineering.py`

## Proposed Work

### Cross-Cutting Rules For Every PR

- Reusable error text should not be introduced inline. Add stable error codes and message templates under `domain/errors` and `domain/messages`.
- Important lifecycle logging should not be introduced inline. Add stable log message constants under `domain/messages`, keep their event names stable, and emit them through `infrastructure/logging`.
- New runtime defaults should only become environment knobs when they are real supported settings. When that happens, update all of:
  - `infrastructure/config/settings.py`
  - `infrastructure/config/environment.py`
  - `.env.example`
  - `src/context_atlas/infrastructure/__ai__.md`
  - tests that prove parsing and default behavior
- New layer folders become governed as soon as they hold non-trivial implementation. If `services/`, `adapters/`, or `rendering/` gain real responsibilities, add local `__ai__.md` files in the same PR.
- Each PR should keep structured packets and traces canonical. Prompt-ready strings are derived outputs and should not become the primary internal model.
- Each PR should end with local verification through the repo preflight or the narrowest stronger equivalent that still protects the modified scope.

### PR 1: Canonical Core Domain Artifacts

**Goal**

Create the first durable Atlas-native domain model for context assembly so later PRs have real types to target.

**Main scope**

- Add canonical domain concepts for:
  - `ContextSource`
  - `ContextSourceClass`
  - `ContextSourceAuthority`
  - `ContextSourceDurability`
  - `ContextSourceProvenance`
  - `ContextCandidate`
  - `ContextBudget`
  - `ContextBudgetSlot`
  - `ContextPacket`
  - `ContextAssemblyDecision`
  - `ContextTrace`
- Add starter reason-code enums for inclusion, exclusion, budget pressure, and authority precedence.
- Separate canonical packet structure from derived rendering concerns.

**Cross-cutting updates**

- Extend `domain/errors` and `domain/messages` with validation and invariant errors for the new models.
- Extend `domain/messages` with starter assembly lifecycle messages such as `ASSEMBLY_STARTED`, `ASSEMBLY_COMPLETED`, and `PACKET_CREATED`, each carrying stable event names.
- Update `src/context_atlas/domain/__ai__.md` and `src/context_atlas/__ai__.md` to reflect the new domain surface.

**Verification**

- Domain unit tests for invariants and serialization-friendly structure.
- No new `.env.example` keys unless a real runtime default is introduced.

### PR 2: Configuration And Observability Backbone For Assembly

**Goal**

Expand the existing config and logging foundation so subsequent functional PRs can land without inventing ad hoc runtime knobs or log strings.

**Main scope**

- Expand `ContextAtlasSettings` with only the first justified assembly defaults, likely:
  - default total budget
  - default retrieval top-k
  - default compression strategy
- Keep these as defaults, not as a substitute for request-level policy inputs.
- Add logging helpers for structured assembly events and per-stage field emission.

**Cross-cutting updates**

- Add new settings parsing in `infrastructure/config/environment.py`.
- Add corresponding keys to `.env.example`.
- Add stable log message constants for:
  - candidate gathering
  - candidate ranking
  - budget allocation
  - compression applied
  - memory selection
- Update `src/context_atlas/infrastructure/__ai__.md` and repo-root `__ai__.md` if the visible runtime surface changes materially.

**Verification**

- Tests for new env parsing, defaults, and invalid values.
- Tests for structured logging emission using direct `LogMessage` constants and stable event-name fields.

### PR 3: Source Registry And Lexical Retrieval Starter Slice

**Goal**

Rebuild the useful retrieval concepts from `context-engine` without importing its module structure or baking retrieval assumptions into the assembly service.

**Main scope**

- Add an in-memory source registry or provider abstraction.
- Add lexical retrieval starter implementations inspired by keyword and TF-IDF modes.
- Return Atlas-native candidate artifacts instead of `ScoredDocument`.
- Keep embeddings out of the first retrieval slice.

**Cross-cutting updates**

- Add source-ingestion and retrieval-related error codes and messages.
- Add retrieval lifecycle log message constants and event-name fields.
- Create `src/context_atlas/adapters/__ai__.md` in this PR if `adapters/` gains real retrieval implementations.
- Update `src/context_atlas/__ai__.md` with the new adapter boundary and allowed imports.

**Verification**

- Tests for source registration, tokenization assumptions, lexical retrieval ranking, and empty-query behavior.
- Import-boundary checks should prove that retrieval implementations do not leak inward dependencies into `domain/`.

### PR 4: Ranking, Deduplication, And Decision Tracing

**Goal**

Replace the prototype's in-orchestrator reranking with explicit ranking and decision artifacts that are inspectable and auditable.

**Main scope**

- Add ranking policy contracts and a starter ranking implementation.
- Add deduplication of candidate sources or candidate payloads where appropriate.
- Record include/exclude decisions with explicit reason codes inside `ContextTrace`.
- Keep ranking logic out of service orchestration files.

**Cross-cutting updates**

- Extend `domain/messages` for `CANDIDATES_RANKED`, `CANDIDATES_DEDUPED`, and `DECISIONS_RECORDED`, keeping their event names stable.
- Add domain errors for invalid ranking inputs or malformed decision state.
- Update `domain/__ai__.md`, `adapters/__ai__.md`, and any new `services/__ai__.md` if services start orchestrating ranking.

**Verification**

- Tests for deterministic ranking order, tie behavior, deduplication rules, and trace contents.
- Logging assertions that emitted records use stable event-name fields and avoid inline message text.

### PR 5: Budget Allocation And Compression Policy Slice

**Goal**

Turn `context-engine`'s budget accounting and compression ideas into Atlas-native policy families with explicit slots and transformation records.

**Main scope**

- Implement `ContextBudget` and `ContextBudgetSlot` behavior beyond raw accounting.
- Support fixed and elastic slot thinking in the domain model.
- Add compression policy contracts and starter implementations based on:
  - truncate
  - sentence-preserving
  - extractive query-aware compression
- Record compression and budget decisions in `ContextTrace` and packet metadata.

**Cross-cutting updates**

- Add new `.env.example` keys only if default budget/compression values are now actually runtime-configurable.
- Extend config parsing and settings models to match.
- Add budget and compression error codes plus direct message/logging constants.
- Create `src/context_atlas/rendering/__ai__.md` if derived packet renderers land in this PR.

**Verification**

- Tests for slot reservation, budget exhaustion behavior, compression result structure, and strategy fallback behavior.
- Tests that canonical packets retain structured transformation metadata even when rendered text is produced.

### PR 6: Memory Entry Model And Retention Policy Slice

**Goal**

Translate the useful memory concepts from `context-engine` into Atlas-native memory artifacts and policy contracts without baking today's heuristics into permanent domain truth.

**Main scope**

- Add `ContextMemoryEntry` or equivalent domain model.
- Add retention/decay policy contracts.
- Implement starter selection behavior inspired by:
  - short-term always-include
  - decay over time
  - deduplication
  - relevance boost
- Keep auto-importance heuristics clearly marked as starter implementations, not canonical truth.

**Cross-cutting updates**

- Add settings and `.env.example` keys only for the memory defaults we truly expect operators to tune, likely:
  - short-term count
  - decay rate
  - dedup threshold
- Extend errors plus direct message/logging constants for memory selection and rejection.
- Update `domain/__ai__.md`, `infrastructure/__ai__.md`, and `services/__ai__.md` if memory orchestration crosses those boundaries.

**Verification**

- Tests for retention behavior, deduplication, decay sensitivity, and query-aware boosts.
- Tests that memory decisions are represented in structured packet traces rather than hidden in opaque strings.

### PR 7: End-To-End Context Assembly Service

**Goal**

Deliver the first real Atlas assembly path that integrates sources, ranking, budgeting, compression, memory, and trace generation into one structured packet workflow.

**Main scope**

- Add a `services/` orchestration path for context assembly.
- Compose source gathering, candidate creation, ranking, budget allocation, compression, memory selection, and packet finalization.
- Produce a canonical `ContextPacket` and `ContextTrace`.
- Keep prompt-ready rendering as an optional derived step under `rendering/`.

**Cross-cutting updates**

- Create `src/context_atlas/services/__ai__.md` if it does not already exist.
- Update package-root `__ai__.md` to reflect the now-real service orchestration boundary.
- Expand direct log message constants for full assembly start, finish, and failure paths, keeping their event names stable.

**Verification**

- End-to-end tests covering:
  - empty source set
  - useful candidate selection
  - budget pressure
  - compression activation
  - memory inclusion
  - packet trace completeness
- Preflight should run in full for this PR.

### PR 8: Documentation-Ontology-Aware Filesystem Source Adapter

**Goal**

Add the first clearly Atlas-specific source adapter so the system proves it is more than a generic rewrite of `context-engine`.

**Main scope**

- Add a filesystem or docs adapter that can ingest project docs as sources.
- Read enough path or front-matter metadata to classify sources by documentation ontology.
- Map `Authoritative`, `Planning`, `Reviews`, `Exploratory`, and `Releases` into source classification fields without flattening them into generic tags.
- Feed those classifications into the ranking and decision trace path.

**Cross-cutting updates**

- Add classification-related error codes and direct message/logging constants.
- Add adapter-specific config defaults only if a stable runtime need exists, such as a governed docs root.
- Update `.env.example` only for real supported knobs, not speculative future controls.
- Update `adapters/__ai__.md` with the new adapter boundary and responsibilities.

**Verification**

- Tests for ontology class detection, precedence-safe classification, and trace visibility of source class and provenance.
- Logging assertions for source classification events.

## Sequencing

The intended order is:

1. PR 1 establishes canonical domain artifacts.
2. PR 2 locks the runtime defaults and observability path before behavior multiplies.
3. PR 3 creates the first source-to-candidate path.
4. PR 4 makes ranking and decision reasoning explicit.
5. PR 5 adds budget and compression policy families.
6. PR 6 adds memory as a governed selection problem.
7. PR 7 integrates the prior slices into the first usable assembly workflow.
8. PR 8 proves Atlas-specific value through ontology-aware source handling.

This order is deliberate:

- It moves from canonical structures to policy implementations to orchestration.
- It introduces runtime knobs only when there is real backing behavior.
- It makes `domain/errors`, `domain/messages`, `infrastructure/config`, and `infrastructure/logging` foundational rather than cleanup work.
- It uses local `__ai__.md` files as active contracts as soon as a folder becomes semantically meaningful.

## Risks And Unknowns

- It is easy to recreate `context-engine` heuristics as permanent Atlas policy too early. Starter implementations should stay clearly replaceable.
- There is a risk of over-growing `.env.example` into a dumping ground. Only operator-relevant, real supported defaults should become environment knobs.
- Token estimation remains approximate until a tokenizer adapter is introduced.
- Source authority and ontology precedence may want richer policy shape than the first filesystem adapter can express.
- Memory retention heuristics are likely to change once real downstream usage appears.
- The split between `adapters/` and `infrastructure/` must stay crisp as retrieval and source adapters land.

## Exit Criteria

This plan is complete enough to supersede once the following are true:

- Context Atlas can assemble a structured packet from in-memory or filesystem-backed sources.
- The packet includes explicit inclusion and exclusion reasoning, budget state, and transformation trace.
- Retrieval, ranking, budgeting, compression, and memory exist as separate policy families or service steps rather than one monolithic engine file.
- Runtime defaults that truly matter are represented consistently across:
  - config models
  - env loading
  - `.env.example`
  - tests
  - local `__ai__.md` contracts
- `services/`, `adapters/`, and `rendering/` are governed by local `__ai__.md` files once they hold real responsibilities.
- No reusable errors or important lifecycle logs are being introduced as scattered inline strings.

## Related Artifacts

- [Context Atlas Charter](../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture Python](../Authoritative/Architecture/Craig-Architecture-Python.md)
- [Documentation Ontology](../Authoritative/Ontology/Documentation-Ontology.md)
