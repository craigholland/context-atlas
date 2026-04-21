# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: e27504eb8ee3693420e8fa26702d62e024303de4
- timestamp_utc: 2026-04-19T22:31:06Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: src/context_atlas/domain
- included:
  - "__init__.py"
  - "errors/**/*.py"
  - "messages/**/*.py"
  - "models/**/*.py"
  - "policies/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds the current semantic core for Context Atlas.
- Provides stable machine-facing identifiers and human-facing message constants for early error and logging contracts.
- Establishes the dependency-clean foundation for canonical source, candidate, budget, packet, decision, and trace artifacts.
- Establishes a frozen Pydantic standard for canonical source, candidate, budget, packet, decision, and trace artifacts.
- Establishes the same validated-model direction for public policy inputs, outputs, and configurable starter policy objects.
- Keeps packet state canonical even as packets begin carrying both ranked source candidates and retained memory entries.
- Carries the starter log message surface that infrastructure logging can reuse without inventing local semantics.
- Carries deterministic ranking, deduplication, memory-retention, and decision-trace policy logic that should not drift outward into adapters or later orchestration.

## Architectural Rules
- This folder is the inward-most project layer and must not import from `services/`, `adapters/`, `infrastructure/`, or `rendering/`.
- Code here should represent semantic meaning, not runtime environment mechanics.
- Error codes and centralized message constants belong here because they are cross-layer semantic contracts, not logging/config implementation details.
- Canonical source, budget, packet, decision, and trace artifacts belong here rather than in `services/` or `rendering/`.
- Non-trivial canonical artifacts in `models/` should use frozen Pydantic models with explicit domain validation instead of mixed dataclass and BaseModel patterns.
- Non-trivial public policy surfaces in `policies/` should also use validated Pydantic models when they shape orchestration inputs, outputs, or configurable behavior.
- Deterministic ranking and decision-recording policies belong here when they can remain pure and dependency-light.
- Base exceptions here should carry a validated Pydantic-backed payload, format through local domain message templates, and remain framework-neutral and dependency-light.
- Do not move environment loading, logger setup, provider DTOs, or persistence shapes into this folder just because they are utility-like.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - sibling modules within `context_atlas.domain`
- must not depend on:
  - `context_atlas.infrastructure`
  - `context_atlas.services`
  - `context_atlas.adapters`
  - `context_atlas.rendering`
  - provider SDKs, ORM packages, or runtime config libraries

## Public API / Key Exports
- `errors`:
  - `ErrorCode`: stable machine-facing error identifiers
  - `ContextAtlasError`: base exception carrying a stable code and a validated payload
  - `ConfigurationError`: configuration-specific exception type
- `messages`:
  - `ErrorMessage`: direct error-message constants keyed by `ErrorCode.name`
  - `LogMessage`: direct log-message constants that carry their own stable event names
- `models`:
  - canonical source, candidate, budget, packet, decision, and trace artifacts
  - starter reason-code enums for inclusion, exclusion, budget pressure, and authority precedence
  - canonical compression result and strategy artifacts
  - canonical retained-memory entry artifacts
- `policies`:
  - `CandidateRankingPolicy`: ranking-policy contract
  - `StarterCandidateRankingPolicy`: starter deterministic ranking/deduplication implementation
  - `CandidateRankingOutcome`: ranked-candidate plus trace result artifact
  - budget allocation, compression, and memory-retention policy contracts plus starter implementations

## File Index
- `errors/codes.py`:
  - responsibility: defines stable machine-facing error identifiers
  - defines:
    - `ErrorCode`: string enum for reusable error categories
  - invariants:
    - codes should be stable once referenced by higher layers or tests
    - prefer semantic identifiers over incidental implementation wording
    - source-registration and retrieval-request failures should get stable codes here before adapters raise them
    - filesystem adapter path/front-matter failures should also land here as stable source-adapter or document-class errors
- `errors/exceptions.py`:
  - responsibility: defines domain exception classes built on stable codes and validated message payloads
  - defines:
    - `ContextAtlasError`: base coded exception
    - `ConfigurationError`: configuration-specific exception type
  - depends_on:
    - `context_atlas.domain.errors.codes`
    - `context_atlas.domain.messages`
  - footguns:
    - do not let exception types begin importing infrastructure config or logger implementations
- `messages/error_messages.py`:
  - responsibility: centralizes reusable human-facing error messages
  - defines:
    - `ErrorMessage`
  - invariants:
    - message constants should stay grouped by their primary consuming surface so contributors can locate the right contract quickly
    - within each consumer grouping, message constants should stay alphabetized for reviewability
    - new service-level validation wording should land here before outer layers introduce fresh inline exception text
  - footguns:
    - avoid turning this into a dumping ground for trivial one-off strings
    - retrieval and source-registration errors should resolve through these constants rather than inline adapter text
- `messages/log_messages.py`:
  - responsibility: centralizes reusable log messages keyed directly by class variable name
  - defines:
    - `LogMessage`
  - invariants:
    - messages here are semantic contracts consumed by logging infrastructure
    - each constant should carry a stable event name without needing a separate event enum or lookup table
    - expanded settings and stage-event wording should be updated here, not introduced inline in outer layers
- `models/sources.py`:
  - responsibility: defines canonical source, provenance, and candidate artifacts that consume the shared semantic enums/helpers
  - defines:
    - `ContextSource`
    - `ContextSourceProvenance`
    - `ContextCandidate`
  - invariants:
    - source identifiers and content must normalize cleanly
    - source artifacts should consume shared semantic enums/helpers rather than redefining canonical defaults locally
    - adapters should cross into canonical source creation through one resolved semantic profile instead of passing source-class, authority, durability, and intended-use pieces independently
    - source artifacts may expose small helper accessors for services and renderers when those helpers preserve canonical meaning without leaking provenance structure outward
    - candidate scoring metadata must remain machine-usable and deterministic
    - canonical source/candidate artifacts should stay frozen Pydantic models with immutable metadata maps
- `models/source_semantics.py`:
  - responsibility: defines canonical source-semantic enums, defaults, and normalization helpers
  - defines:
    - `ContextSourceClass`
    - `ContextSourceAuthority`
    - `ContextSourceDurability`
    - `ContextSourceFamily`
    - `ContextSourceSemanticsProfile`
    - `coerce_source_text_sequence`
    - `merge_source_text_groups`
    - `get_default_source_semantics`
    - `resolve_source_semantics`
  - invariants:
    - canonical source-class defaults for authority, durability, and intended uses should remain defined inward here rather than duplicated across adapters
    - helper functions here should stay source-semantics-focused and must not turn into a general utility bucket
- `models/base.py`:
  - responsibility: provides shared frozen-model and immutable metadata helpers for canonical artifacts
  - defines:
    - `CanonicalDomainModel`
    - `FrozenStringMap`
  - invariants:
    - helper code here should stay thin and model-focused rather than becoming a general utility bucket
    - shared text-sequence normalization helpers should remain small and canonical-model-focused rather than growing into general-purpose utilities
    - immutable metadata helpers should preserve canonical state without importing outer-layer libraries
- `models/budget.py`:
  - responsibility: defines canonical budget and budget-slot artifacts
  - defines:
    - `ContextBudget`
    - `ContextBudgetSlot`
    - `ContextBudgetSlotMode`
  - invariants:
    - fixed-slot reservations must not silently exceed total budget
    - slot names must stay unique within a single budget
    - budget artifacts should reject invalid state during Pydantic model initialization rather than through later service checks
- `models/assembly.py`:
  - responsibility: defines canonical assembly decisions, traces, and packets
  - defines:
    - `ContextAssemblyDecision`
    - `ContextTrace`
    - `ContextPacket`
    - `ContextDecisionAction`
  - footguns:
    - do not add prompt-ready string rendering fields here as canonical state
    - packet item counts should reflect canonical included artifacts, not just one source family
    - inspection-oriented helpers here should remain machine-usable summaries rather than presentation formatting
    - packet-inspection renderers may consume packet summary properties from here, but human-readable section layout must stay in `rendering/`
    - semantic helpers such as whether compression was actually applied may live here when they clarify canonical packet state without introducing presentation formatting
- `models/reason_codes.py`:
  - responsibility: defines starter structured reason-code enums for assembly decisions
  - invariants:
    - reason codes should stay machine-stable even as heuristics evolve
- `models/transformations.py`:
  - responsibility: defines canonical compression/transformation artifacts
  - defines:
    - `CompressionStrategy`
    - `CompressionResult`
  - invariants:
    - compression artifacts should remain structured and packet-attachable rather than collapsing into raw prompt strings
- `models/memory.py`:
  - responsibility: defines canonical retained-memory entry artifacts
  - defines:
    - `ContextMemoryEntry`
  - invariants:
    - memory entries should stay canonical structured artifacts rather than ad hoc transcript strings
    - retention metadata should remain deterministic and dependency-light
- `policies/ranking.py`:
  - responsibility: ranks candidates, deduplicates them, and records structured decisions
  - defines:
    - `CandidateRankingPolicy`
    - `StarterCandidateRankingPolicy`
    - `CandidateRankingOutcome`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.models`
  - invariants:
    - ranking should stay deterministic for identical inputs
    - deduplication should record explicit exclusion decisions rather than silently dropping candidates
    - `_RankableCandidate` may remain a private dataclass helper while it stays local, validation-light, and absent from the package surface
- `policies/budgeting.py`:
  - responsibility: allocates token demand across fixed and elastic slots
  - defines:
    - `BudgetRequest`
    - `BudgetAllocation`
    - `BudgetAllocationOutcome`
    - `ContextBudgetAllocationPolicy`
    - `StarterBudgetAllocationPolicy`
  - invariants:
    - slot-allocation reductions should be visible through structured decisions
    - duplicate or unknown slot requests should fail explicitly
    - `StarterBudgetAllocationPolicy` is intentionally a plain behavior class because it currently carries no structured configuration state of its own
- `policies/compression.py`:
  - responsibility: compresses candidate content into structured compression results
  - defines:
    - `CompressionOutcome`
    - `CompressionPolicy`
    - `StarterCompressionPolicy`
    - `estimate_tokens`
  - invariants:
    - fallback behavior should remain explicit in metadata and trace
    - compressed text is a transformation artifact, not the canonical packet itself
    - candidates that are below the starter compression chunk threshold must not be silently dropped from packet rendering when they still fit the active budget
    - starter token estimation should remain provider-agnostic and bounded to content-shape distinctions such as prose baseline, structured code/markup tightening, and non-Latin-heavy tightening rather than hidden tokenizer tables
    - final compression output must still fit the requested token budget according to the output text's own estimated token shape, even when the compressed text is denser than the original input
    - prefix-budget helpers for compression must not assume token-estimator monotonicity; Story 3's shape-aware starter heuristic and outward callable estimators may both change regimes across prefixes, so longest-fitting-prefix logic must stay correctness-first
    - any tokenizer seam consumed inward here must remain a generic callable token-estimation contract; provider SDKs, model names, or tokenizer-selection policy must stay outside the domain layer
    - token-estimator labels emitted from compression metadata must reflect a real bound estimator; direct policy use should default custom callables to `external_binding` rather than falsely claiming `starter_heuristic`
- `policies/memory.py`:
  - responsibility: retains memory entries through deterministic starter scoring, deduplication, and trace recording
  - defines:
    - `MemoryRetentionPolicy`
    - `MemorySelectionOutcome`
    - `StarterMemoryRetentionPolicy`
  - invariants:
    - short-term inclusion, decay, deduplication, and query boosts should remain replaceable starter logic
    - memory selection decisions should stay trace-visible rather than hidden in transcript strings
    - the short-term keep window should be returned newest-first so downstream budget trimming preserves recency priority
    - retained entries should be returned in priority order so later budget trimming cannot evict the short-term keep window behind older long-term memory
    - `_ScoredMemoryEntry` may remain a private dataclass helper while it stays local, validation-light, and absent from the package surface

## Known Gaps / Future-State Notes
- Some names and policies remain intentionally starter-oriented and may evolve as richer domain concepts harden.
- The current domain layer provides canonical structures plus starter policies, but it is not yet a full long-term domain model for every future provider, storage, or workflow surface.
- The message/error surface is still pragmatic and relatively thin; richer audit projections or more formal event/read-model patterns remain future work.

## Cross-Folder Contracts
- `infrastructure/`: may use `ErrorCode`, `ConfigurationError`, and centralized message constants, but must not redefine those semantics locally.
- `services/`: future orchestration code should consume `ContextPacket`, `ContextTrace`, `ContextBudget`, and related decision artifacts rather than inventing parallel packet state.
- `adapters/`: retrieval adapters may return raw candidates, but they should hand off reranking and decision recording to inward domain policy rather than embedding those rules locally.
- `adapters/`: future adapter translation boundaries may log with domain `LogMessage` constants, but provider-specific payload wording must stay out of domain messages.
- `adapters/`: filesystem document adapters may classify ontology meaning, but they should still surface that meaning through canonical source fields and domain-owned codes/messages.
- `adapters/`: mixed-source adapters should carry source-family-specific mechanics in provenance or validated outer inputs, then cross inward through canonical semantic profiles rather than leaking source meaning into adapter-local tags or source metadata.
- `rendering/`: may render domain semantics for humans, but must not become the place where semantic identifiers are invented.
- `services/`: future assembly orchestration may attach memory traces to packets, but memory-retention logic itself should stay inward here while it remains deterministic.
- `services/`: service orchestration may now include retained memory entries in canonical packets, but service-layer filtering should still consume domain-owned packet and decision semantics rather than redefining them.
- `services/`: mixed-source service metadata should consume source-family and collector information through canonical source helpers defined here rather than digging back into provenance structure throughout the service layer.

## Verification Contract
```yaml
steps:
  - name: compile_domain
    run: |
      # Linux/macOS analog: python3 -m compileall src/context_atlas/domain
      py -3 -m compileall src/context_atlas/domain

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest tests/test_bootstrap_layers.py tests/test_budget_and_compression.py tests/test_candidate_ranking.py tests/test_domain_models.py tests/test_memory_policy.py
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_budget_and_compression.py tests/test_candidate_ranking.py tests/test_domain_models.py tests/test_memory_policy.py

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "from context_atlas.domain.errors import ErrorCode, ContextAtlasError; from context_atlas.domain.messages import ErrorMessage, LogMessage; from context_atlas.domain.models import CompressionResult, CompressionStrategy, ContextMemoryEntry, ContextSource, ContextBudget, ContextPacket; from context_atlas.domain.policies import StarterBudgetAllocationPolicy, StarterCandidateRankingPolicy, StarterCompressionPolicy, StarterMemoryRetentionPolicy"
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.domain.errors import ErrorCode, ContextAtlasError; from context_atlas.domain.messages import ErrorMessage, LogMessage; from context_atlas.domain.models import CompressionResult, CompressionStrategy, ContextMemoryEntry, ContextSource, ContextBudget, ContextPacket; from context_atlas.domain.policies import StarterBudgetAllocationPolicy, StarterCandidateRankingPolicy, StarterCompressionPolicy, StarterMemoryRetentionPolicy"
```
