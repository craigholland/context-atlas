# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

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
- Demonstrates how infrastructure may depend on domain identifiers and templates while preserving inward dependency direction.
- Carries the first supported runtime defaults for early assembly behavior and the structured observability helpers that later services will reuse.
- Re-exports the domain-owned `CompressionStrategy` through infrastructure config so runtime defaults can stay aligned with canonical semantics.

## Architectural Rules
- This folder is an outer layer and may depend on `context_atlas.domain`, but domain code must never import its concrete implementations.
- Keep runtime environment loading, settings models, logger factories, handlers, and emission helpers here rather than in the semantic core.
- Infrastructure code may reuse stable domain error codes, exceptions, events, and message templates instead of inventing semantic strings locally.
- Do not let logger setup or config parsing become a backdoor for embedding business/domain policy.
- If infrastructure grows persistence backends, audit stores, or memory stores later, they must continue to translate external/runtime details before they cross inward.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas.domain`
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
  - `CompressionStrategy`: domain-owned compression-strategy names re-exported for runtime settings
  - `load_settings_from_env`: environment-backed settings loader
- `logging`:
  - `configure_logger`: package logger setup helper
  - `get_logger`: package or child logger accessor
  - `log_event`: structured logging helper keyed by stable `LogEvent` identifiers
  - `log_assembly_stage_event`: helper for emitting assembly-stage events with consistent trace fields

## File Index
- `config/settings.py`:
  - responsibility: defines runtime settings models for infrastructure concerns
  - defines:
    - `LoggingSettings`: logger configuration model
    - `AssemblySettings`: default assembly-budget/retrieval/compression settings
    - `ContextAtlasSettings`: top-level infrastructure settings container
  - invariants:
    - keep settings focused on runtime/config concerns
    - do not move domain policy toggles here without an explicit architectural decision
    - import canonical strategy enums from `context_atlas.domain` rather than redefining them locally
- `config/environment.py`:
  - responsibility: loads settings from environment variables
  - defines:
    - `load_settings_from_env`: environment-backed settings loader
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.events`
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
    - `context_atlas.domain.events`
    - `context_atlas.infrastructure.logging.emit`
    - `context_atlas.infrastructure.config.settings`
  - invariants:
    - logger setup belongs here, not in domain
- `logging/emit.py`:
  - responsibility: emits structured log lines using stable event ids and centralized templates
  - defines:
    - `log_event`
    - `log_assembly_stage_event`
  - depends_on:
    - `context_atlas.domain.events`
    - `context_atlas.domain.messages`
  - footguns:
    - prefer stable event ids plus structured fields over ad hoc inline message strings

## Known Gaps / Future-State Notes
- Infrastructure currently covers only config and logging; future persistence, audit, memory-store, and lineage implementations will likely live here as the system grows.
- The current logger setup is intentionally minimal and stdlib-based; richer sinks or structured emitters can be added later without changing domain event ids.
- `ContextAtlasSettings` is intentionally small and may expand as real adapters and stores are introduced.
- The assembly defaults here are starter runtime knobs; they are not a substitute for explicit request-level policy inputs once services land.
- Compression strategy semantics now live in the domain layer; infrastructure only configures which canonical strategy should be used by default.

## Cross-Folder Contracts
- `domain/`: infrastructure may consume domain-coded errors, events, and message templates, but must never require domain code to import infrastructure implementation modules.
- `services/`: future services should receive infrastructure capabilities through inward-safe contracts or composition boundaries, not by letting services become logger/config factories.
- `adapters/`: future adapters may rely on infrastructure helpers for runtime concerns, but translation-heavy provider code should remain outside generic config/logging helpers.
- repo root: supported env-backed assembly defaults must stay mirrored in `.env.example`.
- package root `context_atlas/`: root-level imports may expose infrastructure helpers selectively, but should not re-export enough internals to blur the layer boundary.

## Verification Contract
```yaml
steps:
  - name: compile_infrastructure
    run: |
      py -3 -m compileall src/context_atlas/infrastructure

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_config_observability.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.infrastructure.config import AssemblySettings, CompressionStrategy, load_settings_from_env; from context_atlas.infrastructure.logging import configure_logger, log_assembly_stage_event, log_event"
```
