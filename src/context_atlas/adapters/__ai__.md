# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 8a54dd6e5780dab2dd099109facf48768b99fd00
- timestamp_utc: 2026-04-19T03:28:59Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: src/context_atlas/adapters
- included:
  - "__init__.py"
  - "docs/**/*.py"
  - "records/**/*.py"
  - "retrieval/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds adapter-layer implementations that translate external or storage-facing inputs into Atlas-native artifacts.
- Provides the first retrieval-oriented adapter slice for turning registered `ContextSource` objects into raw `ContextCandidate` outputs.
- Provides an ontology-aware filesystem document adapter for turning markdown docs into classified `ContextSource` artifacts.
- Provides a structured-record adapter path for turning already-fetched record payloads into canonical `ContextSource` artifacts.
- Keeps lexical retrieval behavior outside the semantic core while still consuming domain-stable codes, messages, and canonical models.
- Makes it explicit that this package is part of the supported starter surface and may be re-exported through `context_atlas.api`.

## Architectural Rules
- Adapters may depend on `context_atlas.domain`, but `context_atlas.domain` must never import adapter implementations.
- Keep translation-heavy retrieval mechanics here rather than embedding tokenization or ranking implementation details into `domain/`.
- Adapters may produce raw candidates, but deterministic reranking and decision-recording policy should stay inward in `context_atlas.domain`.
- Adapter code should emit stable domain message constants rather than inventing inline semantic logger text.
- Do not let adapters import `context_atlas.infrastructure` by default just for convenience; prefer domain-stable contracts plus standard-library mechanics unless a specific outer dependency is justified.
- Adapters should treat canonical source/candidate artifacts as immutable validated models once constructed; translation should happen before model creation, not through later mutation.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas.domain`
  - sibling modules within `context_atlas.adapters`
- must not depend on:
  - `context_atlas.services`
  - `context_atlas.rendering`
  - imports that cause `context_atlas.domain` to depend back on adapters

## Public API / Key Exports
- `docs`:
  - `FilesystemDocumentSourceAdapter`: loads markdown documents as classified Atlas sources
- `retrieval`:
  - `InMemorySourceRegistry`: in-memory registry for canonical sources
  - `LexicalRetrievalMode`: supported keyword/TF-IDF retrieval modes
  - `LexicalRetriever`: Atlas-native lexical candidate builder
- `records`:
  - `StructuredRecordInput`: minimal validated record input contract
  - `StructuredRecordSourceAdapter`: translates record inputs into canonical sources

## File Index
- `__init__.py`:
  - responsibility: exposes the supported starter adapter surface for package-local use and curated public re-export
  - invariants:
    - keep adapter exports deliberate and small
- `retrieval/lexical.py`:
  - responsibility: registers canonical sources and produces lexical retrieval candidates
  - defines:
    - `InMemorySourceRegistry`
    - `LexicalRetrievalMode`
    - `LexicalRetriever`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - retrieval should return Atlas-native `ContextCandidate` artifacts, not prototype-specific DTOs
    - empty queries should fail soft with no candidates rather than inventing placeholder data
    - source registration should preserve stable source identifiers and reject duplicate ids
- `docs/filesystem.py`:
  - responsibility: turns filesystem markdown documents into ontology-aware canonical sources
  - defines:
    - `FilesystemDocumentSourceAdapter`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - document classification should prefer explicit front matter over path inference when both are present
    - inferred source authority/durability should follow the documentation ontology rather than flattening docs into generic tags
    - provenance should preserve file identity and classification source so later traces can explain where a source came from
    - filesystem documents should now identify themselves as the `document` source family in canonical provenance
- `records/structured.py`:
  - responsibility: validates structured-record inputs and translates them into canonical sources
  - defines:
    - `StructuredRecordInput`
    - `StructuredRecordSourceAdapter`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - record adapters should accept already-fetched payloads rather than becoming a database access layer
    - record provenance should preserve source-family identity and adapter collector name
    - canonical `record_id` should remain authoritative in provenance metadata even when callers supply extra provenance fields
    - invalid `tags` or `intended_uses` container shapes should fail fast rather than being silently normalized into misleading metadata
    - record translation should emit canonical `ContextSource` artifacts without inventing a second source object hierarchy

## Known Gaps / Future-State Notes
- This folder now contains lexical retrieval plus a filesystem document adapter; embeddings and provider-backed adapters can land later as separate slices.
- This folder now also contains a structured-record adapter path over already-fetched record payloads; direct database-driver integration should still stay outside Atlas.
- Story 2 Task 2.1 should now also prove that the shared registry and lexical retrieval path stay source-family agnostic once canonical sources have been constructed.
- The current registry is intentionally in-memory and deterministic; persistence-backed source providers should arrive through separate adapters or infrastructure-backed ports later.
- Adapter outputs are now explicitly tested as immutable canonical artifacts so downstream services and renderers can trust their shape.
- The current starter API may re-export this package's supported exports, but deeper adapter modules should still stay out of the public surface unless they are intentionally stabilized.
- Story 2 Task 2.1 is now defining a minimal structured-record input contract; adapter-facing record shapes should stay small and validation-first rather than becoming a database access layer.
- Structured-record validation should now reject mapping-shaped `tags` and `intended_uses` inputs so integrations fail fast on malformed metadata instead of silently converting keys into canonical fields.

## Cross-Folder Contracts
- `domain/`: adapters may consume canonical source/candidate artifacts plus stable error/message contracts, but may not redefine those semantics locally.
- `domain/`: candidate reranking, deduplication, and decision tracing now harden inward there; adapters should stop at source registration and candidate production.
- `domain/`: filesystem document adapters may classify source authority and durability, but those classifications should be expressed through canonical `ContextSource` fields rather than local enums or ad hoc tags.
- `domain/`: source-family provenance may be expressed through canonical provenance fields, but structured-record input contracts should remain adapter-facing rather than becoming a second canonical source model.
- `domain/`: structured-record adapters may default source semantics when outer integrations do not supply them, but those defaults must still surface through canonical source fields and provenance.
- `services/`: future services should orchestrate retrieval through inward-safe contracts rather than by embedding lexical scoring logic directly.
- `infrastructure/`: adapters should not depend on infrastructure helpers unless a concrete runtime concern truly requires it.

## Verification Contract
```yaml
steps:
  - name: compile_adapters
    run: |
      py -3 -m compileall src/context_atlas/adapters

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_lexical_retrieval.py tests/test_filesystem_document_adapter.py tests/test_record_source_adapter.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.adapters import FilesystemDocumentSourceAdapter, InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever, StructuredRecordInput, StructuredRecordSourceAdapter"
```
