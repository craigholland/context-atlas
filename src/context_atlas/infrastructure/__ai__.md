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
    - outward tokenizer-binding defaults may be named here for composition clarity, but they must not become a provider-selection or SDK-binding surface unless the supported runtime contract expands first
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
    - tokenizer seams bound here must stay provider-agnostic at the function signature level and must default cleanly to the starter heuristic when no external estimator is supplied

## Known Gaps / Future-State Notes
- Infrastructure still focuses on config, logging, and shared assembly helpers; persistence, audit sinks, memory stores, and broader integration infrastructure remain future work.
- The supported env-backed configuration surface remains intentionally narrow even though more internal policy constants exist.
- If workflow wrappers or proof helpers continue to accumulate here, this package may need deeper subdivision so config, assembly, and workflow-facing utilities do not flatten into one broad infrastructure folder.

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
      # Linux/macOS analog: python3 -m compileall src/context_atlas/infrastructure
      py -3 -m compileall src/context_atlas/infrastructure

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest tests/test_bootstrap_layers.py tests/test_config_observability.py tests/test_context_assembly_service.py
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_config_observability.py tests/test_context_assembly_service.py

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "from context_atlas.infrastructure import build_starter_context_assembly_service, write_standard_proof_artifacts; from context_atlas.infrastructure.assembly import assemble_with_low_code_workflow; from context_atlas.infrastructure.config import AssemblySettings, CompressionStrategy, LowCodeWorkflowSettings, MemorySettings, get_low_code_workflow_preset, load_settings_from_env, list_low_code_workflow_presets; from context_atlas.infrastructure.logging import configure_logger, log_assembly_stage_message, log_message"
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.infrastructure import build_starter_context_assembly_service, write_standard_proof_artifacts; from context_atlas.infrastructure.assembly import assemble_with_low_code_workflow; from context_atlas.infrastructure.config import AssemblySettings, CompressionStrategy, LowCodeWorkflowSettings, MemorySettings, get_low_code_workflow_preset, load_settings_from_env, list_low_code_workflow_presets; from context_atlas.infrastructure.logging import configure_logger, log_assembly_stage_message, log_message"
```
