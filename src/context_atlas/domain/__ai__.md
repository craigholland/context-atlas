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
  - "events/**/*.py"
  - "messages/**/*.py"
  - "models/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds the current semantic core for Context Atlas.
- Provides stable machine-facing identifiers and human-facing message templates for early error and logging contracts.
- Establishes the dependency-clean foundation for canonical source, candidate, budget, packet, decision, and trace artifacts.

## Architectural Rules
- This folder is the inward-most project layer and must not import from `services/`, `adapters/`, `infrastructure/`, or `rendering/`.
- Code here should represent semantic meaning, not runtime environment mechanics.
- Error codes, event identifiers, and centralized message templates belong here because they are cross-layer semantic contracts, not logging/config implementation details.
- Canonical source, budget, packet, decision, and trace artifacts belong here rather than in `services/` or `rendering/`.
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
- `events`:
  - `LogEvent`: stable event identifiers for meaningful operational events
- `messages`:
  - `format_error_message`: formats a stable error code using centralized templates
  - `get_error_message`: fetches the registered error template
  - `get_log_message`: fetches the registered log-event template
- `models`:
  - canonical source, candidate, budget, packet, decision, and trace artifacts
  - starter reason-code enums for inclusion, exclusion, budget pressure, and authority precedence

## File Index
- `errors/codes.py`:
  - responsibility: defines stable machine-facing error identifiers
  - defines:
    - `ErrorCode`: string enum for reusable error categories
  - invariants:
    - codes should be stable once referenced by higher layers or tests
    - prefer semantic identifiers over incidental implementation wording
- `errors/exceptions.py`:
  - responsibility: defines domain exception classes built on stable codes and templates
  - defines:
    - `ContextAtlasError`: base coded exception
    - `ConfigurationError`: configuration-specific exception type
  - depends_on:
    - `context_atlas.domain.errors.codes`
    - `context_atlas.domain.messages`
  - footguns:
    - do not let exception types begin importing infrastructure config or logger implementations
- `events/log_events.py`:
  - responsibility: defines stable event identifiers for structured logging and future tracing
  - defines:
    - `LogEvent`: string enum of meaningful system events
  - invariants:
    - event ids should be machine-stable even if message wording changes
- `messages/error_messages.py`:
  - responsibility: centralizes reusable human-facing error templates
  - defines:
    - `ErrorMessageTemplate`
    - `get_error_message`
    - `format_error_message`
  - footguns:
    - avoid turning this into a dumping ground for trivial one-off strings
- `messages/log_messages.py`:
  - responsibility: centralizes reusable log templates keyed by stable event ids
  - defines:
    - `LogMessageTemplate`
    - `get_log_message`
  - invariants:
    - templates here are semantic contracts consumed by logging infrastructure
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
- `models/budget.py`:
  - responsibility: defines canonical budget and budget-slot artifacts
  - defines:
    - `ContextBudget`
    - `ContextBudgetSlot`
    - `ContextBudgetSlotMode`
  - invariants:
    - fixed-slot reservations must not silently exceed total budget
    - slot names must stay unique within a single budget
- `models/assembly.py`:
  - responsibility: defines canonical assembly decisions, traces, and packets
  - defines:
    - `ContextAssemblyDecision`
    - `ContextTrace`
    - `ContextPacket`
    - `ContextDecisionAction`
  - footguns:
    - do not add prompt-ready string rendering fields here as canonical state
- `models/reason_codes.py`:
  - responsibility: defines starter structured reason-code enums for assembly decisions
  - invariants:
    - reason codes should stay machine-stable even as heuristics evolve

## Known Gaps / Future-State Notes
- Some current names are intentionally starter-oriented and may evolve as richer domain concepts harden.
- The current model set is canonical structure, not yet full policy behavior.
- The distinction between domain events and future richer audit projections is still intentionally thin.

## Cross-Folder Contracts
- `infrastructure/`: may use `ErrorCode`, `ConfigurationError`, `LogEvent`, and centralized message templates, but must not redefine those semantics locally.
- `services/`: future orchestration code should consume `ContextPacket`, `ContextTrace`, `ContextBudget`, and related decision artifacts rather than inventing parallel packet state.
- `adapters/`: future adapter translation boundaries may log with domain `LogEvent` identifiers, but provider-specific payload wording must stay out of domain templates.
- `rendering/`: may render domain semantics for humans, but must not become the place where semantic identifiers are invented.

## Verification Contract
```yaml
steps:
  - name: compile_domain
    run: |
      py -3 -m compileall src/context_atlas/domain

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_bootstrap_layers.py tests/test_domain_models.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.domain.errors import ErrorCode, ContextAtlasError; from context_atlas.domain.events import LogEvent; from context_atlas.domain.messages import format_error_message; from context_atlas.domain.models import ContextSource, ContextBudget, ContextPacket"
```
