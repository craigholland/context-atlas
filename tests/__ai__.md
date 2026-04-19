# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 5e81b8b70e247003f4710cf8b505af6d165cdd01
- timestamp_utc: 2026-04-19T01:47:46Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: tests
- included:
  - "test_*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds automated tests for the standalone Context Atlas package.
- Verifies bootstrap contracts and guards early architectural seams from silent drift.
- Provides the first executable safety net for domain and infrastructure bootstrap behavior.
- Provides end-to-end orchestration coverage now that the first real assembly service has landed.
- Verifies that env-backed runtime defaults and structured observability helpers stay aligned with the documented repo surface.
- Verifies that the repo's direct message-constant pattern and Pydantic-backed config surface stay stable as the package evolves.
- Verifies that canonical domain artifacts now follow the frozen Pydantic modeling standard rather than a mixed constructor pattern.
- Verifies that public policy inputs, outputs, and configurable starter policies follow the same validated-model direction.
- Verifies that infrastructure composition, adapters, and renderers can consume those immutable validated models without mutating them.
- Verifies that the curated `context_atlas.api` starter surface remains importable and sufficient for MVP-facing examples.

## Architectural Rules
- Tests may import internal project modules to verify behavior, but they must not become an alternate runtime API or hide bad package boundaries.
- Keep fast unit tests here; broader integration or environment-specific test suites should be introduced deliberately rather than mixed in by accident.
- Test helpers should not reimplement production semantics when assertions can exercise the real code directly.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas`
- must not depend on:
  - ad hoc `PYTHONPATH` tricks outside declared verification commands
  - hidden environment assumptions not documented in local owner files

## Public API / Key Exports
- `test_bootstrap_layers.py`:
  - `BootstrapLayerTests`: verifies direct error/log message constants, config loading, and structured log output
- `test_domain_models.py`:
  - `DomainModelTests`: verifies canonical source, budget, decision, trace, and packet artifacts
- `test_config_observability.py`:
  - `ConfigAndObservabilityTests`: verifies Pydantic-backed env defaults and structured assembly-stage logging helpers
- `test_lexical_retrieval.py`:
  - `LexicalRetrievalTests`: verifies in-memory source registration and lexical retrieval behavior
- `test_candidate_ranking.py`:
  - `CandidateRankingTests`: verifies ranking, deduplication, and decision-trace behavior
- `test_budget_and_compression.py`:
  - `BudgetAndCompressionTests`: verifies budget allocation, compression policy, and derived rendering behavior
- `test_memory_policy.py`:
  - `MemoryPolicyTests`: verifies canonical memory entries, starter retention behavior, and trace visibility
- `test_context_assembly_service.py`:
  - `ContextAssemblyServiceTests`: verifies end-to-end assembly orchestration, packet output, and trace completeness
- `test_filesystem_document_adapter.py`:
  - `FilesystemDocumentSourceAdapterTests`: verifies ontology-aware filesystem document classification and integration

## File Index
- `test_bootstrap_layers.py`:
  - responsibility: verifies the current package bootstrap and shared semantic/runtime contracts
  - defines:
    - `BootstrapLayerTests`: bootstrap test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should stay fast and deterministic
    - assertions should track centralized message constants rather than ad hoc inline strings
    - tests should prove the base coded exception now carries a validated payload rather than a dataclass-style surface
    - tests should prove the curated `context_atlas.api` surface exposes the supported starter flow without requiring deep imports
- `test_domain_models.py`:
  - responsibility: verifies canonical domain artifacts and their starter invariants
  - defines:
    - `DomainModelTests`: domain model test suite
  - depends_on:
    - `context_atlas.domain`
  - invariants:
    - tests should verify structured artifacts remain canonical and machine-usable
    - tests should verify frozen Pydantic behavior explicitly enough that a future contributor cannot mistake dataclasses for the preferred model style
- `test_config_observability.py`:
  - responsibility: verifies Pydantic-backed configuration defaults and observability helpers
  - defines:
    - `ConfigAndObservabilityTests`: configuration/observability test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove `.env.example`-backed settings remain parseable and validated
    - assertions should verify structured event-name fields rather than ad hoc log text alone
- `test_lexical_retrieval.py`:
  - responsibility: verifies PR 3 source registration and lexical retrieval behavior
  - defines:
    - `LexicalRetrievalTests`: lexical retrieval test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
  - invariants:
    - tests should prove adapter retrieval returns canonical `ContextCandidate` artifacts
    - empty-query and invalid-request behavior should stay explicit and deterministic
- `test_candidate_ranking.py`:
  - responsibility: verifies PR 4 ranking, deduplication, and decision tracing
  - defines:
    - `CandidateRankingTests`: ranking-policy test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove ranking remains deterministic for identical inputs
    - exclusion decisions should be trace-visible rather than silent side effects
- `test_budget_and_compression.py`:
  - responsibility: verifies PR 5 budget/compression policies and packet rendering derivation
  - defines:
    - `BudgetAndCompressionTests`: budget/compression test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.rendering`
  - invariants:
    - tests should prove compression results remain structured even when rendered text is produced
    - budget reductions and compression fallback should remain explicit and deterministic
    - tests should prove short-but-valid candidates are not dropped just because they fall below the starter compression chunk threshold
    - tests should prove non-applied compression artifacts do not silently replace canonical selected-candidate content in starter rendering
- `test_packet_rendering.py`:
  - responsibility: verifies packet inspection rendering stays derived and product-facing
  - defines:
    - `PacketRenderingTests`: packet inspection rendering test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.rendering`
  - invariants:
    - tests should verify packet inspection highlights selected sources, retained memory, budget state, and compression
    - tests should verify packet inspection distinguishes actual compression application from mere compression-result presence
    - tests should verify packet inspection stays read-only over canonical packet artifacts
- `test_trace_rendering.py`:
  - responsibility: verifies trace inspection rendering stays derived, ordered, and useful for debugging
  - defines:
    - `TraceRenderingTests`: trace inspection rendering test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
    - `context_atlas.rendering`
  - invariants:
    - tests should verify trace inspection groups included, excluded, transformed, and deferred decisions clearly
    - tests should verify service-produced traces carry stable decision positions for inspection renderers
- `test_memory_policy.py`:
  - responsibility: verifies PR 6 memory artifacts, starter retention scoring, and trace visibility
  - defines:
    - `MemoryPolicyTests`: memory policy test suite
  - depends_on:
    - `context_atlas.domain`
  - invariants:
    - tests should prove short-term retention, decay sensitivity, deduplication, and query boosts remain deterministic
    - tests should prove the short-term retention window is ordered newest-first before downstream budget trimming occurs
    - memory decisions should stay visible in structured traces rather than collapsing into opaque prompt strings
- `test_context_assembly_service.py`:
  - responsibility: verifies the starter service orchestration and settings-driven infrastructure factory
  - defines:
    - `ContextAssemblyServiceTests`: end-to-end assembly test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
    - `context_atlas.rendering`
  - invariants:
    - tests should prove services orchestrate canonical packets and traces rather than inventing parallel string state
    - tests should prove infrastructure settings are used through the outer composition helper rather than through hidden globals
    - tests should prove short-term retained memory survives ahead of lower-priority long-term memory when the memory slot is tight
    - tests should prove service trace metadata distinguishes compression presence from actual compression application
- `test_filesystem_document_adapter.py`:
  - responsibility: verifies ontology-aware filesystem document ingestion, classification, and downstream ranking impact
  - defines:
    - `FilesystemDocumentSourceAdapterTests`: filesystem adapter test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove documentation ontology classes map into canonical source authority and durability fields
    - tests should prove classified source provenance remains visible enough to influence downstream packet traces

## Known Gaps / Future-State Notes
- The suite now covers both bootstrap contracts and the first canonical domain artifacts.
- The suite now also covers env-backed assembly defaults and the assembly-stage observability surface.
- The suite now also covers lexical source registration and keyword/TF-IDF retrieval ranking.
- The suite now also covers inward ranking policy behavior, deduplication, and decision recording.
- The suite now also covers budget allocation, compression policy behavior, and rendering derived from structured packet state.
- The suite now also covers canonical memory entries and starter retention policy behavior.
- The suite now also covers the first real end-to-end assembly path plus the starter infrastructure composition helper.
- The suite now also covers ontology-aware filesystem document ingestion and its downstream effect on ranking and packet traces.
- The suite now also covers the direct `LogMessage`/`ErrorMessage` pattern and the Pydantic config refactor.
- The suite now also covers the Pydantic-backed exception payload behind the coded domain error surface.
- The suite now also covers the frozen Pydantic domain-model refactor for canonical artifacts.
- The suite now also covers the public policy-surface conversion to validated Pydantic models.
- The suite now also covers short-candidate compression passthrough/fallback behavior and newest-first ordering for the short-term memory window.
- The suite now also covers importability of the curated `context_atlas.api` starter namespace.
- The example smoke script under `examples/` currently relies on that same curated namespace, so bootstrap coverage should keep guarding against accidental API drift.
- The suite now also covers the first product-facing packet inspection renderer.
- The suite now also covers the first product-facing trace inspection renderer plus ordered decision positions from the assembly service.
- Bootstrap coverage should continue to guard the imports used by the getting-started guide and starter context-flow example so product-facing docs do not drift away from the supported surface.
- As services, adapters, and richer domain models arrive, this folder will likely need more granular owner files or sub-suites.

## Cross-Folder Contracts
- `src/context_atlas/`: tests exercise internal modules directly, but the package layout should remain understandable without depending on tests to explain it.
- `scripts/`: verification scripts invoke this suite and should keep the invocation contract stable or update it deliberately.

## Verification Contract
```yaml
steps:
  - name: compile_tests
    run: |
      py -3 -m compileall tests

  - name: unit_tests
    run: |
      py -3 -m pytest

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "import tests.test_bootstrap_layers, tests.test_budget_and_compression, tests.test_candidate_ranking, tests.test_config_observability, tests.test_context_assembly_service, tests.test_domain_models, tests.test_filesystem_document_adapter, tests.test_lexical_retrieval, tests.test_memory_policy"
```
