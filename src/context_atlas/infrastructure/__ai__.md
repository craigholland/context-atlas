# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: e27504eb8ee3693420e8fa26702d62e024303de4
- timestamp_utc: 2026-04-19T22:31:06Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: src/context_atlas/infrastructure
- included:
  - "__init__.py"
  - "config/**/*.py"
  - "logging/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds outer-layer runtime implementations for Context Atlas.
- Provides environment-backed settings loading and logger setup without pushing those concerns into the domain layer.
- Demonstrates how infrastructure may depend on domain identifiers and messages while preserving inward dependency direction.
- Carries the first supported runtime defaults for early assembly and memory behavior plus the structured observability helpers that later services will reuse.
- Carries the supported runtime defaults for early assembly, ranking, compression, and memory behavior plus the structured observability helpers that later services will reuse.
- Provides the starter composition boundary for wiring validated settings and logger setup into the real assembly service.
- Re-exports the domain-owned `CompressionStrategy` through infrastructure config so runtime defaults can stay aligned with canonical semantics.
- Uses Pydantic/Pydantic Settings for validated runtime configuration instead of unconstrained dataclasses.
- Makes it explicit that `build_starter_context_assembly_service` is the supported MVP starter composition entrypoint.
- Makes it explicit that the curated `context_atlas.api` surface may re-export the starter composition helper without changing its role as an outer composition boundary.

## Architectural Rules
- This folder is an outer layer and may depend on `context_atlas.domain`, but domain code must never import its concrete implementations.
- Keep runtime environment loading, settings models, logger factories, handlers, and emission helpers here rather than in the semantic core.
- Infrastructure code may reuse stable domain error codes, exceptions, and direct message constants instead of inventing semantic strings locally.
- Do not let logger setup or config parsing become a backdoor for embedding business/domain policy.
- Keep low-code presets and declarative workflow settings in this outer layer rather than leaking them into domain models or service orchestration semantics.
- If infrastructure grows persistence backends, audit stores, or memory stores later, they must continue to translate external/runtime details before they cross inward.
- `assembly.py` should stop at starter wiring and configured orchestration; it must not absorb rendering or packet-inspection responsibilities for convenience.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas.adapters`
  - `context_atlas.domain`
  - `context_atlas.services`
  - sibling modules within `context_atlas.infrastructure`
- must not depend on:
  - imports that cause `context_atlas.domain` to depend back on infrastructure
  - direct provider SDK leakage into `context_atlas.domain`
  - UI, CLI, or app-entrypoint code that belongs outside the library package

## Public API / Key Exports
- `config`:
  - `ContextAtlasSettings`: top-level runtime settings model
  - `LoggingSettings`: logging configuration model
  - `AssemblySettings`: runtime defaults for early assembly behavior
  - `MemorySettings`: runtime defaults for starter memory retention behavior
  - `LowCodeWorkflowSettings`: validated low-code preset/source-selection settings
  - `LowCodeWorkflowPreset`: one supported low-code preset definition
  - `CompressionStrategy`: domain-owned compression-strategy names re-exported for runtime settings
  - `get_low_code_workflow_preset`: preset lookup for the current low-code workflow wrapper
  - `list_low_code_workflow_presets`: stable supported low-code preset names
  - `load_settings_from_env`: environment-backed settings loader
- `logging`:
  - `configure_logger`: package logger setup helper
  - `get_logger`: package or child logger accessor
  - `log_message`: structured logging helper keyed by direct `LogMessage` constants
  - `log_assembly_stage_message`: helper for emitting assembly-stage messages with consistent trace fields
- `assembly`:
  - `build_starter_context_assembly_service`: compose starter policies, settings, and logger setup into the supported starter assembly service
  - `assemble_with_starter_context_service`: build the supported starter assembly service and immediately assemble one canonical packet
  - `assemble_with_low_code_workflow`: low-code outer wrapper over the same starter engine path
  - `write_standard_proof_artifacts`: write the canonical proof-artifact set from one already-assembled packet plus rendered context

## File Index
- `config/settings.py`:
  - responsibility: defines Pydantic runtime settings models for infrastructure concerns
  - defines:
    - `LoggingSettings`: logger configuration model
    - `AssemblySettings`: default assembly-budget/retrieval/compression settings
    - `MemorySettings`: starter memory-retention settings
    - `LowCodeWorkflowSettings`: declarative low-code workflow settings
    - `ContextAtlasSettings`: top-level infrastructure settings container
  - invariants:
    - keep settings focused on runtime/config concerns
    - do not move domain policy toggles here without an explicit architectural decision
    - import canonical strategy enums from `context_atlas.domain` rather than redefining them locally
    - memory tuning knobs should stay limited to operator-facing starter defaults until real orchestration proves broader settings are justified
    - the starter memory-budget split is now part of that operator-facing assembly surface and should stay mirrored across validated settings, `.env.example`, and starter assembly wiring
    - low-code settings should stay declarative and small; they may choose sources and presets, but they should not redefine packet, trace, or domain semantics
    - validated override helpers should reuse model validation rather than `model_copy(update=...)` when changing user-facing assembly defaults such as total budget
- `config/environment.py`:
  - responsibility: loads settings from environment variables through a Pydantic Settings model
  - defines:
    - `load_settings_from_env`: environment-backed settings loader
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.infrastructure.config.settings`
  - footguns:
    - avoid accreting unrelated config parsing for future adapters unless it remains clearly outer-layer
    - only promote true operator-facing defaults into the env surface and `.env.example`
    - low-code env keys should stay limited to preset/source selection plus a tiny amount of workflow configuration; deeper tuning still belongs to the existing assembly/memory settings surface
- `config/presets.py`:
  - responsibility: defines the supported low-code preset catalog without turning presets into domain semantics
  - defines:
    - `LowCodeWorkflowPreset`: preset definition model
    - `get_low_code_workflow_preset`
    - `list_low_code_workflow_presets`
  - depends_on:
    - `context_atlas.adapters`
    - `context_atlas.domain`
  - invariants:
    - presets should stay few, explicit, and product-facing
    - preset definitions may shape adapter defaults, but they must not redefine canonical packet or source semantics
    - preset path resolution should stay relative to an outer workflow root rather than assuming one repo layout globally
- `logging/factory.py`:
  - responsibility: configures package loggers and default formatters
  - defines:
    - `configure_logger`
    - `get_logger`
  - depends_on:
    - `context_atlas.domain.messages`
    - `context_atlas.infrastructure.logging.emit`
    - `context_atlas.infrastructure.config.settings`
  - invariants:
    - logger setup belongs here, not in domain
- `logging/emit.py`:
  - responsibility: emits structured log lines using direct message constants and stable event names
  - defines:
    - `log_message`
    - `log_assembly_stage_message`
  - depends_on:
    - `context_atlas.domain.messages`
  - footguns:
    - prefer direct `LogMessage` constants plus structured fields over ad hoc inline message strings
- `assembly.py`:
  - responsibility: wires validated runtime settings and logger setup into the starter assembly service
  - defines:
    - `build_starter_context_assembly_service`
    - `assemble_with_starter_context_service`
    - `assemble_with_low_code_workflow`
    - `write_standard_proof_artifacts`
  - depends_on:
    - `context_atlas.domain.policies`
    - `context_atlas.infrastructure.config`
    - `context_atlas.infrastructure.logging`
    - `context_atlas.services`
  - invariants:
    - keep this as an outer composition boundary, not a second orchestration layer
    - starter settings should influence service defaults through constructor wiring rather than through hidden globals
    - current MVP-facing docs should treat this helper as the supported starter entrypoint rather than reaching into deeper service wiring
    - repository-specific source collection should remain outside this module; callers should hand this helper an already-built retriever over canonical Atlas sources
    - one-shot packet assembly helpers here must remain workflow-agnostic convenience wrappers over the same shared service path rather than growing provider- or workflow-specific branches
    - low-code convenience here may choose a supported preset, docs root, and payload file, but it should still cross into the same registry/retriever/service path rather than creating alternate packet semantics
    - low-code wrappers should prefer `ContextAtlasSettings.with_low_code_overrides(...)`, `build_low_code_workflow_plan(...)`, and `assemble_with_starter_sources(...)` over wrapper-local setting merges or metadata packing
    - proof-artifact writing should stay on one shared outer helper here rather than being duplicated across runnable workflow examples

## Known Gaps / Future-State Notes
- Infrastructure currently covers only config and logging; future persistence, audit, memory-store, and lineage implementations will likely live here as the system grows.
- The current logger setup is intentionally minimal and stdlib-based; richer sinks or structured emitters can be added later without changing domain message names.
- `ContextAtlasSettings` is intentionally small and may expand as real adapters and stores are introduced.
- The assembly defaults here are starter runtime knobs; they are not a substitute for explicit request-level policy inputs once services land.
- The starter assembly factory now makes those defaults operational without forcing `services/` to import infrastructure modules.
- Story 1 Task 1.4 is now auditing the starter surface; changes here should make the composition boundary clearer, not more magical.
- Product-facing getting-started guidance should only document runtime knobs that are actually supported by `load_settings_from_env()` and the current starter assembly factory.
- The supported assembly env surface now includes the starter memory-budget split; future contributors should keep that one visible without promoting ranking authority tables or canonical slot names into runtime config.
- Product-facing docs for the starter assembly surface should now name `CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION` explicitly and should keep explaining that ranking authority tables and canonical slot names remain internal.
- Compression strategy semantics now live in the domain layer; infrastructure only configures which canonical strategy should be used by default.
- Memory retention semantics now live in the domain layer; infrastructure only configures which starter defaults are used when callers do not override them.
- The starter assembly factory now also wires validated ranking/compression/memory policy settings through to the Pydantic policy models instead of relying on hidden defaults.
- The current supported starter entry surface still lives here; a broader curated package-level API may later wrap or re-export it, but should not bypass this composition boundary semantically.
- The current starter entry helper is now also re-exported through `context_atlas.api`; future API expansion should continue to preserve this module as the real composition boundary rather than moving wiring inward.
- Story 3 Task 3.1 now also treats this module as the engine-side stop for the Codex repository workflow: repository-root and docs-root choices stay outside, while shared service wiring stays here.
- The runnable Codex repository example should keep using this module as the composition boundary rather than inlining policy wiring inside `examples/`.
- The runnable and demonstration-oriented Codex repository scripts should share one outer workflow composition path over this module rather than duplicating build-plus-assemble wiring in multiple example files.
- The runnable repository script should remain the authoritative outer composition path; demonstration scripts may layer alternate inspection output on top of it but should not fork the composition boundary.
- The product-facing Codex repository guide should only document runtime knobs that actually flow through `load_settings_from_env()` and this module's starter assembly wiring.
- Product-facing sample-repo artifacts and CLI help should still describe this module as the real composition boundary rather than implying that `examples/` owns the policy wiring.
- Story 4 Task 4.1 now also uses this module as the shared composition boundary for the technical-builder docs-plus-database example; outer workflow code may fetch rows and choose docs roots, but policy wiring should still stop here.
- Story 4 Task 4.3 now also reinforces that boundary: outer workflows may still choose row mappers and already-fetched row batches, but this module must not absorb that row-shaping or translation logic just to make examples shorter.
- Product-facing workflow guides should keep describing this module as the shared assembly boundary after adapter translation, not as a place where mixed-source workflows hide mapper or data-access decisions.
- Story 5 Task 5.1 is now introducing the low-code workflow shape, so presets and declarative source settings should remain outer-layer conveniences over the same shared engine instead of creating a second orchestration stack.
- Story 5 Task 5.1 now also includes the first runnable low-code wrapper path; future growth should extend the preset catalog or example/docs surface deliberately rather than accreting ad hoc low-code branches in `assembly.py`.
- The low-code wrapper should now stay test-backed as a real integration path; future refactors should preserve docs-plus-records behavior and one-source-family evaluation without turning presets into hidden orchestration branches.
- Story 5 Task 5.2 now also expects the product-facing low-code guide and example README to stay aligned with the supported preset catalog and low-code env surface rather than implying hidden presets or deeper runtime magic.
- Story 5 Task 5.2 now also expects tracked low-code config/preset artifacts to stay aligned with the supported preset catalog and declarative setting defaults rather than becoming a second source of truth.
- Story 5 Task 5.2 now also expects surrounding docs to present those artifacts in a stable order: reference config, reference preset, then runnable wrapper, so the low-code path stays understandable without implying hidden infrastructure behavior.
- Story 5 Task 5.3 is now auditing that boundary more directly, so low-code preset meaning and repo-relative source selection should stay visible as resolved outer-layer plan state instead of being hidden inside the wrapper path.
- Story 5 Task 5.3 now also expects low-code override merging and starter source-to-packet assembly to live on shared infrastructure seams rather than being reimplemented inside the runnable example.
- The low-code example wrapper should now be treated as a thin composition layer over those shared seams; future refactors should make the resolved workflow plan more explicit, not less.

## Cross-Folder Contracts
- `domain/`: infrastructure may consume domain-coded errors and message constants, but must never require domain code to import infrastructure implementation modules.
- `services/`: future services should receive infrastructure capabilities through inward-safe contracts or composition boundaries, not by letting services become logger/config factories.
- `services/`: the starter assembly factory is the current composition boundary for injecting runtime settings and logger setup into the assembly service.
- `adapters/`: future adapters may rely on infrastructure helpers for runtime concerns, but translation-heavy provider code should remain outside generic config/logging helpers.
- repo root: supported env-backed assembly and memory defaults must stay mirrored in `.env.example`.
- package root `context_atlas/`: root-level imports may expose infrastructure helpers selectively, but should not re-export enough internals to blur the layer boundary.

## Verification Contract
```yaml
steps:
  - name: compile_infrastructure
    run: |
      py -3 -m compileall src/context_atlas/infrastructure

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_config_observability.py tests/test_context_assembly_service.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.infrastructure import build_starter_context_assembly_service, write_standard_proof_artifacts; from context_atlas.infrastructure.assembly import assemble_with_low_code_workflow; from context_atlas.infrastructure.config import AssemblySettings, CompressionStrategy, LowCodeWorkflowSettings, MemorySettings, get_low_code_workflow_preset, load_settings_from_env, list_low_code_workflow_presets; from context_atlas.infrastructure.logging import configure_logger, log_assembly_stage_message, log_message"
```
