# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: eace5c6161693122ee13f8772d61a312c018c6fe
- timestamp_utc: 2026-04-19T00:47:16Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
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
- `render_packet_context` should derive output from canonical packet state or an attached canonical transformation artifact; it must not become a service-like assembly step.
- when a transformation artifact is attached but was not applied, rendering should continue to derive starter context from canonical selected candidates rather than treating the transform artifact as new canonical state

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
- `render_packet_inspection`:
  - human-readable packet inspection renderer for canonical packet state
- `render_trace_inspection`:
  - human-readable trace inspection renderer for canonical trace state

## File Index
- `__init__.py`:
  - responsibility: exposes the small rendering and inspection surface
- `context.py`:
  - responsibility: derives renderable text from canonical packet artifacts
  - invariants:
    - prefer structured compression results when available
    - retained memory should render from canonical packet state rather than a parallel service-only string field
    - do not mutate packet state during rendering
- `packet.py`:
  - responsibility: renders packet inspection sections for product-facing debugging and demos
  - invariants:
    - emphasize canonical packet state such as selected sources, memory, budget, and compression
    - reflect actual compression application state rather than just the presence of a `CompressionResult`
    - remain a read-only formatter over canonical packet artifacts
- `trace.py`:
  - responsibility: renders ordered trace-decision and metadata sections for product-facing debugging and demos
  - invariants:
    - emphasize included, excluded, transformed, and deferred decisions plus trace metadata
    - remain a read-only formatter over canonical trace artifacts

## Known Gaps / Future-State Notes
- Rendering is intentionally minimal even now that the assembly service has landed.
- Richer packet sections or role-specific renderers can arrive later, but they should still derive from canonical packet state.
- The current renderer is now explicitly exercised as a read-only view over frozen Pydantic packet artifacts.
- Upcoming packet/trace inspectors should stay text-first and product-facing while continuing to derive from canonical packet/trace state rather than inventing parallel DTOs.
- Packet inspection now has a first-class renderer; later trace inspection should align with it instead of inventing a different product vocabulary.
- Trace inspection now also has a first-class renderer; packet and trace views should continue to feel like one inspection surface rather than two unrelated outputs.
- Story 1 Task 1.4 is now auditing the starter rendering path; rendering changes should make layer boundaries clearer without reintroducing prompt-first canonical thinking.

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
      py -3 -m pytest tests/test_budget_and_compression.py tests/test_context_assembly_service.py tests/test_packet_rendering.py tests/test_trace_rendering.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.rendering import render_packet_context, render_packet_inspection, render_trace_inspection"
```
