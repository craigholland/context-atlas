# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

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
- Base exceptions here may format messages through local domain message templates, but must remain framework-neutral and dependency-light.
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
  - `ContextAtlasError`: base exception carrying a stable code and formatted message
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
  - responsibility: defines domain exception classes built on stable codes and direct message constants
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
  - responsibility: defines canonical source, provenance, and candidate artifacts
  - defines:
    - `ContextSource`
    - `ContextSourceProvenance`
    - `ContextCandidate`
    - source classification/authority/durability enums
  - invariants:
    - source identifiers and content must normalize cleanly
    - candidate scoring metadata must remain machine-usable and deterministic
    - canonical source/candidate artifacts should stay frozen Pydantic models with immutable metadata maps
- `models/base.py`:
  - responsibility: provides shared frozen-model and immutable metadata helpers for canonical artifacts
  - defines:
    - `CanonicalDomainModel`
    - `FrozenStringMap`
  - invariants:
    - helper code here should stay thin and model-focused rather than becoming a general utility bucket
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
- `policies/memory.py`:
  - responsibility: retains memory entries through deterministic starter scoring, deduplication, and trace recording
  - defines:
    - `MemoryRetentionPolicy`
    - `MemorySelectionOutcome`
    - `StarterMemoryRetentionPolicy`
  - invariants:
    - short-term inclusion, decay, deduplication, and query boosts should remain replaceable starter logic
    - memory selection decisions should stay trace-visible rather than hidden in transcript strings
    - retained entries should be returned in priority order so later budget trimming cannot evict the short-term keep window behind older long-term memory
    - `_ScoredMemoryEntry` may remain a private dataclass helper while it stays local, validation-light, and absent from the package surface

## Known Gaps / Future-State Notes
- Some current names are intentionally starter-oriented and may evolve as richer domain concepts harden.
- The current model set is canonical structure, not yet full policy behavior.
- The current canonical model set now uses frozen Pydantic artifacts with immutable metadata helpers, and the public policy surface now follows the same validated-model direction.
- The only remaining dataclasses in `domain/` should be either the coded exception type or private helper structs that do not act as serialization or package-boundary surfaces.
- The distinction between domain message constants and future richer audit projections is still intentionally thin.
- The current message surface now includes starter observability for candidate gathering, ranking, budget allocation, compression, and memory selection ahead of service orchestration.
- The current message surface now also includes the expanded starter settings-load summary so ranking, compression, and memory policy defaults stay visible when infrastructure loads them.
- The current error/message surface now also covers source registration and retrieval completion for the lexical adapter slice.
- The current error/message surface now also covers filesystem source-adapter validation and unsupported document-class failures for the ontology-aware docs adapter.
- The current domain policy surface now includes a starter ranking policy; more advanced or provider-aware ranking should remain replaceable rather than becoming hardcoded truth.
- The current domain policy surface now also includes starter budget-allocation and compression policies; richer strategies should remain replaceable.
- The current domain policy surface now also includes a starter memory-retention policy; richer importance, freshness, or persistence-backed behavior should remain replaceable.

## Cross-Folder Contracts
- `infrastructure/`: may use `ErrorCode`, `ConfigurationError`, and centralized message constants, but must not redefine those semantics locally.
- `services/`: future orchestration code should consume `ContextPacket`, `ContextTrace`, `ContextBudget`, and related decision artifacts rather than inventing parallel packet state.
- `adapters/`: retrieval adapters may return raw candidates, but they should hand off reranking and decision recording to inward domain policy rather than embedding those rules locally.
- `adapters/`: future adapter translation boundaries may log with domain `LogMessage` constants, but provider-specific payload wording must stay out of domain messages.
- `adapters/`: filesystem document adapters may classify ontology meaning, but they should still surface that meaning through canonical source fields and domain-owned codes/messages.
- `rendering/`: may render domain semantics for humans, but must not become the place where semantic identifiers are invented.
- `services/`: future assembly orchestration may attach memory traces to packets, but memory-retention logic itself should stay inward here while it remains deterministic.
- `services/`: service orchestration may now include retained memory entries in canonical packets, but service-layer filtering should still consume domain-owned packet and decision semantics rather than redefining them.

## Verification Contract
```yaml
steps:
  - name: compile_domain
    run: |
      py -3 -m compileall src/context_atlas/domain

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_budget_and_compression.py tests/test_candidate_ranking.py tests/test_domain_models.py tests/test_memory_policy.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.domain.errors import ErrorCode, ContextAtlasError; from context_atlas.domain.messages import ErrorMessage, LogMessage; from context_atlas.domain.models import CompressionResult, CompressionStrategy, ContextMemoryEntry, ContextSource, ContextBudget, ContextPacket; from context_atlas.domain.policies import StarterBudgetAllocationPolicy, StarterCandidateRankingPolicy, StarterCompressionPolicy, StarterMemoryRetentionPolicy"
```
