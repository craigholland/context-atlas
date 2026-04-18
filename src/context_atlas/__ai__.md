# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: ae64a1f063eef27588ca8e6d4af0f7fd18cb2ab4
- timestamp_utc: 2026-04-18T21:42:30Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
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
- Makes it explicit that canonical domain artifacts now standardize on frozen Pydantic models inside the `context_atlas` namespace.
- Makes it explicit that public policy inputs, outputs, and configurable starter policies now follow the same validated-model direction.
- Makes it explicit that the current supported MVP surface is a curated `context_atlas.api` module plus a small set of stable subpackage imports rather than a broad root-level barrel.

## Architectural Rules
- This package is a standalone library package; downstream code should import through the `context_atlas` namespace rather than treating layer folders as top-level packages.
- `domain/` is the semantic core and must not depend on `services/`, `adapters/`, `infrastructure/`, or `rendering/`.
- `services/` orchestrates workflows and may depend on `domain/` but must not let provider or framework vocabulary define application behavior.
- `services/` is now a real orchestration layer and should stay focused on sequencing canonical stages rather than growing policy logic of its own.
- `infrastructure/` and `adapters/` are outer concerns; they may depend inward, but inward layers must not import their concrete implementations.
- `rendering/` is for derived outputs only and must not become the canonical home of packet, decision, or trace semantics.
- Empty layer folders are intentional placeholders; do not collapse their responsibilities into unrelated packages just because the current bootstrap is small.
- Non-trivial canonical data artifacts should favor frozen Pydantic models over mixed dataclass/Pydantic patterns so validation and constructor semantics stay predictable across the package.
- Non-trivial public policy surfaces should avoid dataclass-era positional construction assumptions for the same reason.
- The package root should stay intentionally thin even after a curated public API is introduced; current user-facing guidance should prefer `context_atlas.api` for the starter flow and only reach for stable subpackage imports when architectural seams matter.

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
  - `api`: curated starter API namespace re-export
  - package docstring: describes the current MVP-supported import surface
- `api.py`:
  - curated starter-facing exports for adapters, settings loading, assembly wiring, and rendering
- `domain/`:
  - semantic core for error codes, log events, messages, canonical domain artifacts, and pure policy logic
  - canonical artifacts now use frozen Pydantic models with explicit domain validation
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
    - `api`: curated starter API namespace
  - depends_on:
    - `context_atlas.api`
  - invariants:
    - keep the package root lightweight
    - do not turn `__init__.py` into a service locator or broad re-export barrel
    - prefer curating starter exports through `api.py` rather than widening the package root directly
- `api.py`:
  - responsibility: curates the supported starter import surface without flattening the entire layer structure
  - used_by:
    - MVP-facing examples and guides
  - invariants:
    - keep the export set small and intentional
    - re-export only the starter flow pieces that are explicitly supported for MVP users
    - examples should validate this module as the first import stop before they reach for stable subpackage paths
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
    - canonical artifacts should keep one validated constructor style so services/adapters/tests are not forced to guess between dataclass and Pydantic semantics
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
- The package root still intentionally avoids broad direct exports even though `context_atlas.api` now provides a curated starter namespace.
- The current curated API is intentionally small; later slices should only widen it when examples and real workflows prove additional exports deserve to stabilize.
- The current curated API is now exercised by the starter smoke example under `examples/`, which should stay aligned with the supported starter flow.
- The canonical model package now uses frozen Pydantic artifacts; later hardening should reduce remaining non-trivial dataclasses in adjacent policy layers as those boundaries stabilize.
- The remaining dataclasses in the package should now be limited to clearly private helper structs or exception mechanics that do not define the package's public structured-data surface.

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
