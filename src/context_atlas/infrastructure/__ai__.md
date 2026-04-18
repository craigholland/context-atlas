# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: ae64a1f063eef27588ca8e6d4af0f7fd18cb2ab4
- timestamp_utc: 2026-04-18T21:42:30Z
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
- If infrastructure grows persistence backends, audit stores, or memory stores later, they must continue to translate external/runtime details before they cross inward.

## Allowed Dependencies
- may depend on:
  - Python standard library
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
  - `CompressionStrategy`: domain-owned compression-strategy names re-exported for runtime settings
  - `load_settings_from_env`: environment-backed settings loader
- `logging`:
  - `configure_logger`: package logger setup helper
  - `get_logger`: package or child logger accessor
  - `log_message`: structured logging helper keyed by direct `LogMessage` constants
  - `log_assembly_stage_message`: helper for emitting assembly-stage messages with consistent trace fields
- `assembly`:
  - `build_starter_context_assembly_service`: compose starter policies, settings, and logger setup into the supported starter assembly service

## File Index
- `config/settings.py`:
  - responsibility: defines Pydantic runtime settings models for infrastructure concerns
  - defines:
    - `LoggingSettings`: logger configuration model
    - `AssemblySettings`: default assembly-budget/retrieval/compression settings
    - `MemorySettings`: starter memory-retention settings
    - `ContextAtlasSettings`: top-level infrastructure settings container
  - invariants:
    - keep settings focused on runtime/config concerns
    - do not move domain policy toggles here without an explicit architectural decision
    - import canonical strategy enums from `context_atlas.domain` rather than redefining them locally
    - memory tuning knobs should stay limited to operator-facing starter defaults until real orchestration proves broader settings are justified
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
  - depends_on:
    - `context_atlas.domain.policies`
    - `context_atlas.infrastructure.config`
    - `context_atlas.infrastructure.logging`
    - `context_atlas.services`
  - invariants:
    - keep this as an outer composition boundary, not a second orchestration layer
    - starter settings should influence service defaults through constructor wiring rather than through hidden globals
    - current MVP-facing docs should treat this helper as the supported starter entrypoint rather than reaching into deeper service wiring

## Known Gaps / Future-State Notes
- Infrastructure currently covers only config and logging; future persistence, audit, memory-store, and lineage implementations will likely live here as the system grows.
- The current logger setup is intentionally minimal and stdlib-based; richer sinks or structured emitters can be added later without changing domain message names.
- `ContextAtlasSettings` is intentionally small and may expand as real adapters and stores are introduced.
- The assembly defaults here are starter runtime knobs; they are not a substitute for explicit request-level policy inputs once services land.
- The starter assembly factory now makes those defaults operational without forcing `services/` to import infrastructure modules.
- Compression strategy semantics now live in the domain layer; infrastructure only configures which canonical strategy should be used by default.
- Memory retention semantics now live in the domain layer; infrastructure only configures which starter defaults are used when callers do not override them.
- The starter assembly factory now also wires validated ranking/compression/memory policy settings through to the Pydantic policy models instead of relying on hidden defaults.
- The current supported starter entry surface still lives here; a broader curated package-level API may later wrap or re-export it, but should not bypass this composition boundary semantically.
- The current starter entry helper is now also re-exported through `context_atlas.api`; future API expansion should continue to preserve this module as the real composition boundary rather than moving wiring inward.

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
      py -3 -c "from context_atlas.infrastructure import build_starter_context_assembly_service; from context_atlas.infrastructure.config import AssemblySettings, CompressionStrategy, MemorySettings, load_settings_from_env; from context_atlas.infrastructure.logging import configure_logger, log_assembly_stage_message, log_message"
```
