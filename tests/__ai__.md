# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: fb63d8a1fb704e7d42749b583fb7f8382a8ac3c2
- timestamp_utc: 2026-04-21T00:14:07Z
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
- Verifies that the installable starter CLI remains aligned with the MVP starter surface rather than drifting into a separate execution path.

## Architectural Rules
- Tests may import internal project modules to verify behavior, but they must not become an alternate runtime API or hide bad package boundaries.
- Keep fast unit tests here; broader integration or environment-specific test suites should be introduced deliberately rather than mixed in by accident.
- Test helpers should not reimplement production semantics when assertions can exercise the real code directly.
- Release-facing tests should keep the exported package version aligned with `pyproject.toml` and the current shipped release note rather than freezing a stale version expectation.
- Cross-platform path-safety tests should cover both Windows-style and POSIX-style traversal inputs when the production code is expected to guard against either form.

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
- `test_cli.py`:
  - `StarterCliTests`: verifies the installable starter CLI and current release-version surface
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
- `test_record_source_adapter.py`:
  - `StructuredRecordSourceAdapterTests`: verifies structured-record input validation and record-to-source translation
- `test_source_semantics.py`:
  - `SourceSemanticsTests`: verifies canonical semantic consistency across supported source families
- `test_codex_repository_workflow.py`:
  - `CodexRepositoryWorkflowTests`: verifies the flagship Codex repository example against a temporary governed-doc repo
- `test_docs_database_workflow.py`:
  - `DocsDatabaseWorkflowTests`: verifies the technical-builder docs-plus-database example against temporary docs plus tracked sample-style record payloads
- `test_mvp_proof_capture.py`:
  - `MvpProofCaptureTests`: verifies MVP proof evidence capture remains idempotent and reviewable

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
- `test_cli.py`:
  - responsibility: verifies the installable starter CLI stays aligned with the supported starter flow
  - defines:
    - `StarterCliTests`: starter CLI test suite
  - depends_on:
    - `context_atlas`
  - invariants:
    - tests should prove the installable starter CLI can assemble a packet from a docs directory without relying on repository-only helper scripts
    - tests should prove the package version surface stays aligned with the current MVP release contract
- `test_domain_models.py`:
  - responsibility: verifies canonical domain artifacts and their starter invariants
  - defines:
    - `DomainModelTests`: domain model test suite
  - depends_on:
    - `context_atlas.domain`
  - invariants:
    - tests should verify structured artifacts remain canonical and machine-usable
    - tests should verify frozen Pydantic behavior explicitly enough that a future contributor cannot mistake dataclasses for the preferred model style
    - tests should verify canonical per-class source semantics stay domain-owned and merge overrides consistently before adapters consume them
    - tests should verify canonical sources can be built from one resolved semantic profile instead of adapter-style piecemeal semantic arguments
- `test_config_observability.py`:
  - responsibility: verifies Pydantic-backed configuration defaults and observability helpers
  - defines:
    - `ConfigAndObservabilityTests`: configuration/observability test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove `.env.example`-backed settings remain parseable and validated
    - tests should prove the env-backed starter memory-budget split stays aligned across settings loading and starter assembly behavior
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
    - tests should prove the starter token-estimation heuristic tightens only for bounded content-shape differences such as structured code/markup and non-Latin-heavy text, and that compression fit checks consume the same estimate
    - tests should prove compressed output is trimmed back under budget when output shape is denser than the original input shape that seeded the initial character cap
    - tests should prove an outward-bound custom token estimator can tighten compression behavior without introducing provider-specific logic into domain policy tests
    - tests should prove custom token-estimator labels are rejected when no estimator is actually bound and auto-labeled truthfully when a direct policy caller binds a custom estimator without naming it
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
    - tests should verify generic packet-context rendering defaults stay generic while workflow-facing labels remain caller-supplied
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
    - tests should verify any concise trace-highlight surface remains derived from canonical trace metadata and counts
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
    - tests should prove any one-shot infrastructure assembly helper remains a convenience wrapper over the same shared service path
    - tests should prove shared proof-artifact emission stays on one infrastructure helper rather than drifting into per-example writer implementations
    - tests should prove short-term retained memory survives ahead of lower-priority long-term memory when the memory slot is tight
    - tests should prove service trace metadata distinguishes compression presence from actual compression application
    - tests should prove the configured starter memory-budget split affects both default budget creation and custom-budget memory-slot augmentation
    - tests should prove caller-supplied workflow metadata remains opaque passthrough context rather than workflow-specific service behavior
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
    - tests should prove authoritative filesystem fixtures continue to use the `Authoritative/Canon/...` path shape rather than drifting back to a flattened authoritative root
    - tests should prove filesystem documents now consume shared domain source-semantics helpers rather than adapter-local default tables
    - tests should prove classified source provenance remains visible enough to influence downstream packet traces
    - tests should prove filesystem adapters do not restate canonical source class through adapter-local tags when that meaning already lives in canonical source semantics
- `test_record_source_adapter.py`:
  - responsibility: verifies structured-record input validation and record-to-source translation
  - defines:
    - `StructuredRecordSourceAdapterTests`: structured-record adapter test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
  - invariants:
    - tests should prove record adapters emit canonical `ContextSource` artifacts with the structured-record source family
    - tests should prove record provenance and intended-use metadata survive translation into canonical sources
    - tests should prove record-backed sources pick up fallback authority, durability, and intended uses from shared domain semantics when outer inputs omit them
    - tests should prove canonical `record_id` stays authoritative in provenance metadata even when callers provide overlapping provenance fields
    - tests should prove Atlas rejects richer non-mapping outer row or handle objects so data-access concerns stay outside the adapter boundary
    - tests should prove mapping-shaped `tags` or `intended_uses` payloads fail fast instead of being silently coerced
    - tests should prove documents and structured records can coexist in one shared registry and packet flow
- `test_record_adapter_shape.py`:
  - responsibility: verifies the MVP row-mapper pattern for shaping already-fetched rows into validated record inputs
  - defines:
    - `StructuredRecordRowMapperTests`: row-mapper test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
  - invariants:
    - tests should prove row mappers emit validated `StructuredRecordInput` objects before translation into canonical sources
    - tests should prove row mappers can batch-shape already-fetched mapping payloads without introducing database or vector-store client ownership
    - tests should prove missing mapped fields fail through the coded adapter-input surface instead of silent partial normalization
- `test_source_semantics.py`:
  - responsibility: verifies mixed-source semantic consistency across filesystem documents and structured records
  - defines:
    - `SourceSemanticsTests`: source-semantics consistency test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove supported source families can differ in provenance family while sharing one canonical semantic model
    - tests should prove explicit intended-use overrides merge consistently across source families instead of replacing canonical defaults in only one adapter path
  - `test_codex_repository_workflow.py`:
    - responsibility: verifies the supported Codex repository workflow remains a real integration path over the shared engine
  - defines:
    - `CodexRepositoryWorkflowTests`: repository workflow validation test suite
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.infrastructure`
    - `context_atlas.services`
  - invariants:
    - tests should prove the workflow example can assemble packet, trace, and rendered context from a temporary governed-doc repository
    - tests should prove the sample-repo and temporary governed-doc fixtures stay aligned with the `Authoritative/Canon/...` directory split used by the repo's top-tier canon
    - tests should prove supported workflow metadata remains visible in trace inspection output instead of being hidden in example-only print logic
    - tests should prove relative `--docs-root` arguments resolve from the selected repository root instead of the caller's shell working directory
    - tests should prove the CLI help surface points back to the minimal sample-repo artifact so the documented workflow shape stays discoverable
    - tests should prove demonstration-oriented workflow scripts still render canonical context plus derived trace output instead of inventing a second workflow state model
    - tests should prove repository-facing scripts apply repository-specific labels at the example boundary rather than through canonical rendering defaults
    - tests should prove the runnable and demonstration scripts share one supported parser/composition path instead of drifting into parallel example-specific workflow wiring
    - tests should prove the demonstration script can still run via `python -m examples.codex_repository_workflow.show_trace` without import-path regressions
    - tests should prove the runnable repository workflow can emit the standard MVP-proof Atlas artifact filenames when asked
    - tests should prove explicit total-budget overrides remain visible in workflow trace metadata and surface real pressure signals when constrained proof scenarios are run
    - tests should prove unsupported repository-workflow total-budget overrides fail through the same validated settings path as env-backed assembly configuration
    - tests should prove the tracked sample-repo authority scenario keeps authoritative documents ahead of lower-authority planning and review docs for the same repository question
  - `test_docs_database_workflow.py`:
    - responsibility: verifies the supported docs-plus-database workflow remains a real mixed-source integration path over the shared engine
  - defines:
    - `DocsDatabaseWorkflowTests`: docs-plus-database workflow validation test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.services`
  - invariants:
    - tests should prove the workflow assembles packets containing both document and structured-record source families
    - tests should prove supported record metadata stays visible in trace output as outer-workflow context rather than hidden in example-only print logic
    - tests should prove the example continues to describe record rows as already-fetched outer inputs rather than implying Atlas owns database access
    - tests should prove the runnable mixed-source workflow can emit the standard MVP-proof Atlas artifact filenames when asked
    - tests should prove explicit total-budget overrides remain visible in mixed-source trace metadata and surface real pressure signals when constrained proof scenarios are run
    - tests should prove unsupported mixed-source total-budget overrides fail through the same validated settings path as env-backed assembly configuration
  - `test_mvp_proof_capture.py`:
    - responsibility: verifies proof capture remains safe to rerun against an existing evidence bundle directory
  - defines:
    - `MvpProofCaptureTests`: MVP proof capture test suite
  - depends_on:
    - Python standard library
  - invariants:
    - tests should prove `--refresh-bundle` removes stale files from an existing workflow/scenario bundle before regenerated proof artifacts are written
    - tests should prove `--refresh-bundle` still preserves the regenerated canonical artifact files when the source artifacts already live inside the bundle being refreshed
    - tests should prove proof capture can regenerate a workflow/scenario bundle without failing when the source artifacts already sit at the bundle target paths
    - tests should verify the evidence package remains written in the same bundle directory after regeneration
    - tests should prove proof capture rejects unsafe workflow/scenario bundle components before refresh logic can target paths outside the declared bundle root
    - tests should prove proof capture rejects packet/trace inputs whose workflow metadata no longer matches the declared supported workflow
    - tests should prove `--expect-budget-pressure` rejects artifact sets without visible pressure signals and accepts constrained bundles that expose packet- or trace-level pressure evidence
    - tests should prove `--expect-document-authority-contrast` rejects artifact sets without an authoritative-versus-lower-authority document contrast and accepts bundles that preserve that packet order
    - tests should prove document-authority proof validation follows canonical `source.authority` semantics even when document class labels and authority overrides diverge
- `test_low_code_workflow.py`:
  - responsibility: verifies the supported low-code workflow remains a real preset-driven integration path over the shared engine
  - defines:
    - `LowCodeWorkflowTests`: low-code workflow validation test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should prove the workflow can assemble packets containing both documents and structured records through one preset-driven wrapper
    - tests should prove disabling one source family still preserves the same canonical packet and trace path
    - tests should prove the CLI help and stdout keep the low-code boundary visible rather than hiding source resolution or packet inspection behavior
    - tests should prove tracked low-code config/preset artifacts stay aligned with the supported preset catalog and declared workflow surface
    - tests should prove low-code override merging stays in validated config surfaces rather than being reimplemented ad hoc in the runnable example
    - tests should prove the runnable low-code workflow can emit the standard MVP-proof Atlas artifact filenames when asked

## Known Gaps / Future-State Notes
- The suite is strong for the current local MVP workflows, but it is still centered on tracked local examples and sample artifacts rather than broader external-service or production-style integration coverage.
- The current workflow tests prove supported boundaries and artifact shapes, but they do not yet represent load, concurrency, or long-running operational behavior.
- As test volume grows further, this folder may need more granular owner files or sub-suites so one local contract does not become too broad to govern well.

## Cross-Folder Contracts
- `src/context_atlas/`: tests exercise internal modules directly, but the package layout should remain understandable without depending on tests to explain it.
- `scripts/`: verification scripts invoke this suite and should keep the invocation contract stable or update it deliberately.

## Verification Contract
```yaml
steps:
  - name: compile_tests
    run: |
      # Linux/macOS analog: python3 -m compileall tests
      py -3 -m compileall tests

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest
      py -3 -m pytest

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "import tests.test_bootstrap_layers, tests.test_budget_and_compression, tests.test_candidate_ranking, tests.test_codex_repository_workflow, tests.test_config_observability, tests.test_context_assembly_service, tests.test_docs_database_workflow, tests.test_domain_models, tests.test_filesystem_document_adapter, tests.test_lexical_retrieval, tests.test_low_code_workflow, tests.test_memory_policy, tests.test_record_adapter_shape, tests.test_record_source_adapter, tests.test_source_semantics"
      $env:PYTHONPATH='src'
      py -3 -c "import tests.test_bootstrap_layers, tests.test_budget_and_compression, tests.test_candidate_ranking, tests.test_codex_repository_workflow, tests.test_config_observability, tests.test_context_assembly_service, tests.test_docs_database_workflow, tests.test_domain_models, tests.test_filesystem_document_adapter, tests.test_lexical_retrieval, tests.test_low_code_workflow, tests.test_memory_policy, tests.test_record_adapter_shape, tests.test_record_source_adapter, tests.test_source_semantics"
```
