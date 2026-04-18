# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 00f5ed5518d18fc1d03c8394e95eef41bab0c31f
- timestamp_utc: 2026-04-17T19:51:13Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

## Scope
- folder: src/context_atlas/rendering
- included:
  - "__init__.py"
  - "*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds derived output renderers for Context Atlas artifacts.
- Provides the first minimal packet renderer without turning prompt-ready text into the canonical storage model.
- Renders both retained memory and candidate/compression content from canonical packet state.
- Owns the product-facing packet/trace inspection surfaces as derived read-only views over canonical artifacts.

## Architectural Rules
- Rendering may depend on `context_atlas.domain`, but canonical packet, budget, decision, and compression semantics must remain defined there.
- Renderers should be pure formatting/derivation code, not hidden orchestration or policy engines.
- Renderers should not mutate packet or compression models; tests should be able to compare packet snapshots before and after rendering.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas.domain`
  - sibling modules within `context_atlas.rendering`
- must not depend on:
  - `context_atlas.adapters`
  - `context_atlas.infrastructure`
  - `context_atlas.services`

## Public API / Key Exports
- `render_packet_context`:
  - derived text renderer for canonical packets

## File Index
- `__init__.py`:
  - responsibility: exposes the small rendering and inspection surface
- `context.py`:
  - responsibility: derives renderable text from canonical packet artifacts
  - invariants:
    - prefer structured compression results when available
    - retained memory should render from canonical packet state rather than a parallel service-only string field
    - do not mutate packet state during rendering

## Known Gaps / Future-State Notes
- Rendering is intentionally minimal even now that the assembly service has landed.
- Richer packet sections or role-specific renderers can arrive later, but they should still derive from canonical packet state.
- The current renderer is now explicitly exercised as a read-only view over frozen Pydantic packet artifacts.
- Upcoming packet/trace inspectors should stay text-first and product-facing while continuing to derive from canonical packet/trace state rather than inventing parallel DTOs.

## Cross-Folder Contracts
- `domain/`: packet and compression semantics stay canonical there; rendering only derives text from them.

## Verification Contract
```yaml
steps:
  - name: compile_rendering
    run: |
      py -3 -m compileall src/context_atlas/rendering

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_budget_and_compression.py tests/test_context_assembly_service.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.rendering import render_packet_context"
```
