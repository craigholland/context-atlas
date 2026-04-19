# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 6ef14c06116e1920b24d556978aaac1dd9080d37
- timestamp_utc: 2026-04-19T14:50:49Z
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
    - caller-supplied request metadata should stay opaque outer-workflow context; services may preserve it for inspection but should not interpret it as workflow-specific engine behavior
    - outer low-code or product wrappers should pass that metadata through shared infrastructure seams instead of teaching this service about presets, wrapper modes, or workflow-specific source toggles
    - service defaults should remain thin until real downstream usage proves broader knobs are necessary
    - memory-slot trimming must preserve the priority order returned by domain memory policies instead of re-ranking memory locally
    - service-produced trace decisions should keep stable positions so rendering can inspect ordered decision flow without re-sequencing it
    - caller-supplied workflow metadata should remain visible in trace metadata so supported workflow examples can explain which outer path produced a packet

## Known Gaps / Future-State Notes
- The current service is a starter orchestration path over in-memory retrieval plus starter policies.
- The current service now also surfaces selected source classes and provenance collectors in trace metadata for downstream inspection.
- The current service now also surfaces selected source families in trace metadata while consuming collector and family information through domain-owned source helpers instead of raw provenance reach-through.
- The current service now also surfaces stable source-family and collector count summaries in trace metadata so mixed-source workflows can prove coherence without walking selected candidates by hand.
- The current service now also assigns sequential decision positions so trace renderers can present ordered decision flow consistently.
- The current service should now also preserve caller-supplied workflow metadata in trace metadata so supported examples can prove which outer workflow path was used without adding parallel debug state.
- Story 2 Task 2.4 now also treats source-family trace summaries as part of the mixed-source contract, so future service changes should keep that visibility without reintroducing provenance reach-through.
- Story 1 Task 1.4 PR B now distinguishes `compression_present` from `compression_applied` so downstream renderers do not need to guess whether a transform artifact actually changed packet content.
- Story 4 Task 4.3 is now auditing the docs-plus-database workflow against Craig Architecture boundaries, so service code should keep treating workflow metadata as opaque outer context while remaining source-family agnostic once canonical sources enter the engine path.
- Product-facing docs for mixed-source workflows should continue to present this package as the shared engine path after adapter translation, not as the home of row-mapping or data-access behavior.
- Richer source providers, persistence-backed memory, and tokenizer-aware budgeting can arrive later through additional ports and outer-layer composition.
- Supported example workflows should share this service path instead of duplicating stage sequencing in multiple scripts once a reference workflow composition helper exists.
- Product-facing examples should describe this module as the shared engine path and should not present alternate scripts as separate service modes once they are only changing inspection output.
- Story 5 Task 5.3 now also expects this service to keep caller metadata opaque and normalized, so outer low-code wrappers do not need to hand-pack every metadata value as a string just to stay on the shared engine path.
- Story 5 Task 5.3 now also expects low-code workflow reinforcement to happen outside this package; if future low-code growth needs richer plan logic, that belongs in outer config/infrastructure seams rather than in service-specific branches here.

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
      py -3 -m compileall src/context_atlas/services

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_context_assembly_service.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.services import CandidateRetriever, ContextAssemblyService"
```
