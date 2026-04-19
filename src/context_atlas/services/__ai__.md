# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b2c4bb6cea24adea91711da005a3c49614016376
- timestamp_utc: 2026-04-19T02:42:50Z
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
    - service metadata should distinguish transformation presence from transformation application when packet/rendering behavior depends on that semantic difference
    - service defaults should remain thin until real downstream usage proves broader knobs are necessary
    - memory-slot trimming must preserve the priority order returned by domain memory policies instead of re-ranking memory locally
    - service-produced trace decisions should keep stable positions so rendering can inspect ordered decision flow without re-sequencing it

## Known Gaps / Future-State Notes
- The current service is a starter orchestration path over in-memory retrieval plus starter policies.
- The current service now also surfaces selected source classes and provenance collectors in trace metadata for downstream inspection.
- The current service now also surfaces selected source families in trace metadata while consuming collector and family information through domain-owned source helpers instead of raw provenance reach-through.
- The current service now also assigns sequential decision positions so trace renderers can present ordered decision flow consistently.
- Story 2 Task 2.4 now also treats source-family trace summaries as part of the mixed-source contract, so future service changes should keep that visibility without reintroducing provenance reach-through.
- Story 1 Task 1.4 PR B now distinguishes `compression_present` from `compression_applied` so downstream renderers do not need to guess whether a transform artifact actually changed packet content.
- Richer source providers, persistence-backed memory, and tokenizer-aware budgeting can arrive later through additional ports and outer-layer composition.

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
