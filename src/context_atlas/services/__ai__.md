# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: e27504eb8ee3693420e8fa26702d62e024303de4
- timestamp_utc: 2026-04-19T22:31:06Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: src/context_atlas/services
- included:
  - "__init__.py"
  - "*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds service-layer orchestration for Context Atlas workflows.
- Composes retrieval, ranking, memory selection, budget allocation, compression, and packet finalization into canonical packet outputs.
- Keeps orchestration logic out of `domain/` while also refusing to let concrete adapter or infrastructure mechanics define system behavior.
- Surfaces selected source classification and provenance collectors in trace metadata so adapter-origin semantics remain inspectable downstream.
- Assigns stable 1-based decision positions so trace inspection surfaces can present an ordered assembly story without mutating trace state later.
- Preserves caller-supplied workflow metadata in trace metadata so outer workflow composition remains inspectable without inventing a second debug channel.

## Architectural Rules
- Services may depend on `context_atlas.domain`, but must not import `context_atlas.adapters`, `context_atlas.infrastructure`, or `context_atlas.rendering`.
- Services orchestrate stage sequencing and canonical artifact assembly; deterministic ranking, budgeting, compression, and memory-selection rules should remain inward in `domain/`.
- Services should assume public policy request/result objects are validated Pydantic models and should not reintroduce dataclass-era positional-construction assumptions at those boundaries.
- Services may depend on inward-safe contracts such as retriever protocols, but should not instantiate or import concrete adapter implementations directly.
- Services should emit stable domain-owned log messages through injected loggers rather than inventing inline semantic strings.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas.domain`
  - sibling modules within `context_atlas.services`
- must not depend on:
  - `context_atlas.adapters`
  - `context_atlas.infrastructure`
  - `context_atlas.rendering`

## Public API / Key Exports
- `ContextAssemblyService`:
  - starter orchestration service for building canonical `ContextPacket` artifacts
- `CandidateRetriever`:
  - inward-safe retrieval contract consumed by the service layer

## File Index
- `__init__.py`:
  - responsibility: exposes the intentionally small service surface
- `assembly.py`:
  - responsibility: sequences retrieval, ranking, memory, budget, compression, and packet finalization
  - defines:
    - `CandidateRetriever`
    - `ContextAssemblyService`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
    - `context_atlas.domain.policies`
  - invariants:
    - orchestration should produce canonical packets and traces, not prompt-first strings
    - packet assembly should stay explainable through structured trace metadata and decisions
    - service-level trace metadata may summarize selected source classes and collectors, but canonical source semantics still belong on the sources themselves
    - mixed-source trace metadata should consume domain-owned source helpers rather than reaching directly into provenance internals throughout the service
    - mixed-source trace metadata may expose stable family or collector count summaries when that improves workflow inspection, but it should remain derived from canonical source helpers rather than adapter-specific reach-through
    - service metadata should distinguish transformation presence from transformation application when packet/rendering behavior depends on that semantic difference
    - service-facing budget metadata should surface truthful budget vocabulary (`fixed_reserved_tokens`, `unreserved_tokens`, `unallocated_tokens`) rather than re-exporting ambiguous legacy `remaining_tokens` labels as the preferred caller contract
    - service-level top-summary budget fields must remain canonical even when prefixed budget-stage trace metadata is also present; stage-prefixed budget metadata must not overwrite the service-computed `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`, or `budget_unallocated_tokens` summary fields
    - service-owned zero-budget compression outcomes should report the effective runtime strategy truthfully instead of re-exporting the configured compression strategy as if it had actually run
    - service-owned zero-budget compression outcomes should normalize loosely typed configured strategy values defensively before exposing configured-strategy metadata so custom policy implementations do not fail on plain-string strategy fields
    - service packet and trace metadata should surface top-level `compression_strategy` plus optional `configured_compression_strategy` when compression is present, so renderers and docs do not have to infer effective strategy truth from prefixed stage metadata alone
    - caller-supplied request metadata should stay opaque outer-workflow context; services may preserve it for inspection but should not interpret it as workflow-specific engine behavior
    - outer low-code or product wrappers should pass that metadata through shared infrastructure seams instead of teaching this service about presets, wrapper modes, or workflow-specific source toggles
    - service defaults should remain thin until real downstream usage proves broader knobs are necessary
    - the starter memory-budget split may be injected as a thin constructor default, but canonical slot names should remain internal service constants rather than env-backed config names
    - memory-slot trimming must preserve the priority order returned by domain memory policies instead of re-ranking memory locally
    - service-produced trace decisions should keep stable positions so rendering can inspect ordered decision flow without re-sequencing it
    - caller-supplied workflow metadata should remain visible in trace metadata so supported workflow examples can explain which outer path produced a packet

## Known Gaps / Future-State Notes
- The current service layer is still a starter orchestration path over canonical sources, starter policies, and in-memory retrieval rather than a richer provider-aware or persistence-backed application service surface.
- Trace metadata is currently optimized for local explainability and supported workflow review, not long-term audit storage or broader observability backends.
- If workflow-specific branching starts accumulating here instead of staying in outer composition layers, this package should be decomposed further rather than absorbing more example-specific orchestration.

## Cross-Folder Contracts
- `domain/`: services consume canonical artifacts and pure policies from there; they must not redefine semantic models locally.
- `domain/`: services should consume mixed-source identity through canonical source helpers and domain trace semantics rather than walking provenance structure directly in multiple places.
- `adapters/`: retrieval implementations may satisfy `CandidateRetriever`, but service code must stay adapter-agnostic.
- `infrastructure/`: outer-layer factories may assemble this service with runtime settings and logger setup, but service code must remain inward-safe.
- `rendering/`: rendering may derive text from packets produced here, but rendering must not become an alternate orchestration path.

## Verification Contract
```yaml
steps:
  - name: compile_services
    run: |
      # Linux/macOS analog: python3 -m compileall src/context_atlas/services
      py -3 -m compileall src/context_atlas/services

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest tests/test_context_assembly_service.py
      py -3 -m pytest tests/test_context_assembly_service.py

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "from context_atlas.services import CandidateRetriever, ContextAssemblyService"
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.services import CandidateRetriever, ContextAssemblyService"
```
