# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: c9ee71f1d304f7d3ef5bac728a6c32f1fe47a7dc
- timestamp_utc: 2026-04-21T20:02:32Z
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
- `render_trace_highlights`:
  - concise product-facing summary renderer for canonical trace state

## File Index
- `__init__.py`:
  - responsibility: exposes the small rendering and inspection surface
- `context.py`:
  - responsibility: derives renderable text from canonical packet artifacts
  - invariants:
    - prefer structured compression results when available
    - retained memory should render from canonical packet state rather than a parallel service-only string field
    - do not mutate packet state during rendering
    - default section headers should stay generic to the renderer; workflow-specific labels should be passed in by the caller rather than baked into canonical rendering semantics
    - optional section headers may improve product-facing readability, but they should remain derived formatting rather than Codex-specific packet semantics
- `packet.py`:
  - responsibility: renders packet inspection sections for product-facing debugging and demos
  - invariants:
    - emphasize canonical packet state such as selected sources, memory, budget, and compression
    - budget inspection should prefer truthful budget vocabulary like `fixed_reserved_tokens` and `unreserved_tokens` instead of re-exporting legacy alias names as the primary display contract
    - packet inspection should show `unallocated_tokens` when the service provides that post-allocation remainder explicitly
    - reflect actual compression application state rather than just the presence of a `CompressionResult`
    - compression inspection should distinguish effective runtime strategy from optional configured strategy when fallback changed the actual behavior
    - remain a read-only formatter over canonical packet artifacts
- `trace.py`:
  - responsibility: renders ordered trace-decision and metadata sections for product-facing debugging and demos
  - invariants:
    - emphasize included, excluded, transformed, and deferred decisions plus trace metadata
    - concise highlight views should stay derived from canonical trace metadata and counts rather than introducing a second summary model
    - trace-facing summaries should prefer the settled top-level service metadata keys for budget and compression semantics instead of forcing readers through duplicated prefixed stage metadata
    - remain a read-only formatter over canonical trace artifacts

## Known Gaps / Future-State Notes
- Rendering is still intentionally text-first and terminal-oriented; richer UI-facing, structured-machine, or web presentation surfaces remain future work.
- Generic renderers continue to avoid workflow-specific vocabulary; applications and examples remain responsible for labels and presentation framing.
- If output modes expand materially beyond the current packet/trace text views, this package may need deeper subdivision so the rendering surface does not flatten into one broad folder.

## Cross-Folder Contracts
- `domain/`: packet and compression semantics stay canonical there; rendering only derives text from them.

## Verification Contract
```yaml
steps:
  - name: compile_rendering
    run: |
      # Linux/macOS analog: python3 -m compileall src/context_atlas/rendering
      py -3 -m compileall src/context_atlas/rendering

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest tests/test_budget_and_compression.py tests/test_context_assembly_service.py tests/test_packet_rendering.py tests/test_trace_rendering.py
      py -3 -m pytest tests/test_budget_and_compression.py tests/test_context_assembly_service.py tests/test_packet_rendering.py tests/test_trace_rendering.py

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "from context_atlas.rendering import render_packet_context, render_packet_inspection, render_trace_inspection"
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.rendering import render_packet_context, render_packet_inspection, render_trace_inspection"
```
