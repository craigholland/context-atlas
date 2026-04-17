# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

## Scope
- folder: src/context_atlas
- included:
  - "__init__.py"
  - "domain/**/*.py"
  - "services/**/*.py"
  - "adapters/**/*.py"
  - "infrastructure/**/*.py"
  - "rendering/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Defines the primary Python package namespace for Context Atlas.
- Establishes the Craig-style layer spine for the standalone library layout under `src/context_atlas/`.
- Provides the top-level dependency and public-surface rules that all nested layer packages must follow.
- Makes it explicit that infrastructure now carries both logging/config mechanics and the first small set of assembly and memory runtime knobs.

## Architectural Rules
- This package is a standalone library package; downstream code should import through the `context_atlas` namespace rather than treating layer folders as top-level packages.
- `domain/` is the semantic core and must not depend on `services/`, `adapters/`, `infrastructure/`, or `rendering/`.
- `services/` orchestrates workflows and may depend on `domain/` but must not let provider or framework vocabulary define application behavior.
- `services/` is now a real orchestration layer and should stay focused on sequencing canonical stages rather than growing policy logic of its own.
- `infrastructure/` and `adapters/` are outer concerns; they may depend inward, but inward layers must not import their concrete implementations.
- `rendering/` is for derived outputs only and must not become the canonical home of packet, decision, or trace semantics.
- Empty layer folders are intentional placeholders; do not collapse their responsibilities into unrelated packages just because the current bootstrap is small.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - sibling packages inside `context_atlas` when the dependency direction is inward-safe
- must not depend on:
  - direct imports that reverse Craig Architecture layer direction
  - provider SDK packages from `domain/`
  - runtime environment/config loading from `domain/`

## Public API / Key Exports
- `__init__.py`:
  - `__version__`: package version marker for the standalone library namespace
- `domain/`:
  - semantic core for error codes, log events, messages, canonical domain artifacts, and pure policy logic
- `infrastructure/`:
  - runtime configuration and logging implementation details for the current bootstrap
  - early assembly and memory default settings plus structured observability helpers
- `rendering/`:
  - derived text/rendering helpers for canonical packets and transformations
- `services/`:
  - orchestration for end-to-end packet assembly from retrieval through packet finalization

## File Index
- `__init__.py`:
  - responsibility: defines the package root and current public version export
  - defines:
    - `__version__`: current package version string
  - depends_on:
    - no project-local modules
  - invariants:
    - keep the package root lightweight
    - do not turn `__init__.py` into a service locator or broad re-export barrel
- `domain/`:
  - responsibility: holds semantic core contracts and canonical domain artifacts
  - used_by:
    - `services/`
    - `infrastructure/`
    - future `adapters/` and `rendering/`
  - invariants:
    - inward-most project layer
    - may remain small early, but must stay dependency-clean
    - canonical packet, budget, source, decision, and trace artifacts should live here rather than in outer layers
    - pure ranking, deduplication, memory-retention, and decision-recording policy logic may live here when it is deterministic and dependency-light
- `services/`:
  - responsibility: orchestrates retrieval, ranking, budgeting, compression, memory inclusion, and packet finalization
  - used_by:
    - outer composition boundaries such as `context_atlas.infrastructure`
  - invariants:
    - may depend on `domain/` only
    - should consume inward-safe contracts rather than importing concrete adapters or infrastructure helpers
    - should produce canonical packets and traces rather than prompt-ready strings
- `infrastructure/`:
  - responsibility: holds runtime configuration and logging implementation details
  - used_by:
    - package bootstrap and future entry/composition points
  - invariants:
    - may depend on `domain/`
    - must not be imported inward by `domain/`
    - operator-facing assembly defaults should stay narrow until real services prove they are worth stabilizing

## Known Gaps / Future-State Notes
- `services/` now carries the first real orchestration slice, but richer provider-backed composition and persistence are still intentionally deferred.
- `adapters/` and `rendering/` now hold real slices, but their public surfaces should stay intentionally narrow while the starter assembly path hardens.
- The package root does not yet define a curated broader public API beyond `__version__`.
- Future migration work from `context-engine` should add `__ai__.md` files for subfolders once they gain enough local complexity to justify their own contracts.

## Cross-Folder Contracts
- `domain/`: semantic codes, events, message templates, and canonical domain artifacts defined there are stable contracts for higher layers and must not import outward.
- `domain/`: canonical source, candidate, budget, packet, and trace artifacts should be consumed inward-out, not redefined in `services/` or `rendering/`.
- `domain/`: deterministic ranking and decision policies should harden inward here instead of being embedded in adapters or later service orchestration.
- `infrastructure/`: runtime config and logging may depend on domain identifiers and message templates, but domain code must not depend on infrastructure implementation.
- `infrastructure/`: supported `.env.example` keys should remain a thin mirror of real config loader behavior, not speculative future controls.
- `infrastructure/`: starter assembly and memory defaults should stay operator-facing and limited until a real assembly service proves broader tuning is necessary.
- `services/`: future service orchestration should depend on domain semantics and inward-owned contracts rather than importing concrete adapter or infrastructure implementations.
- `services/`: orchestration may now assemble packets from retrieval, budget, compression, and memory slices, but those stage rules should continue to harden inward in `domain/`.
- `adapters/`: retrieval/source-ingestion implementations may translate external or stored source material into canonical `ContextSource`/`ContextCandidate` artifacts, but must keep that translation logic out of `domain/`.
- `rendering/`: derived renderers may consume canonical packet/decision/trace artifacts, but must not become the source of canonical semantics.
- `rendering/`: derived renderers may consume canonical compression artifacts, but those artifacts must stay attached to packets rather than being replaced by raw strings.

## Verification Contract
```yaml
steps:
  - name: compile
    run: |
      py -3 -m compileall src tests

  - name: unit_tests
    run: |
      py -3 -m pytest

  - name: import_boundaries
    run: |
      py -3 scripts/check_import_boundaries.py --repo-root . --config scripts/import_boundary_rules.toml

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "import context_atlas, context_atlas.domain, context_atlas.infrastructure, context_atlas.services"
```
