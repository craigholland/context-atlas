# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 6ef14c06116e1920b24d556978aaac1dd9080d37
- timestamp_utc: 2026-04-19T14:50:49Z
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
  - `StructuredRecordPayload`: supported record-adapter input union for validated inputs or mapping-shaped payloads
  - `StructuredRecordRowMapper`: application-facing mapper for shaping already-fetched rows into validated record inputs
  - `StructuredRecordSourceAdapter`: translates record inputs into canonical sources

## File Index
- `__init__.py`:
  - responsibility: exposes the supported starter adapter surface for package-local use and curated public re-export
  - invariants:
    - keep adapter exports deliberate and small
- `retrieval/registry.py`:
  - responsibility: owns canonical in-memory source registration plus the revision boundary later retrieval reuse can key from
  - defines:
    - `InMemorySourceRegistry`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - source registration should preserve stable source identifiers and reject duplicate ids
    - registry revision should remain a small outward invalidation signal rather than expanding into a second retrieval engine
- `retrieval/indexing.py`:
  - responsibility: defines the baseline lexical index shape separate from source ownership
  - defines:
    - `LexicalIndexSnapshot`
    - `build_lexical_index_snapshot`
  - depends_on:
    - `context_atlas.domain.models`
  - invariants:
    - index snapshots should stay outward adapter helpers rather than new inward domain artifacts
    - the baseline snapshot should remain the smallest shape needed for later reuse work
    - corpus-wide document-frequency and inverse-document-frequency state should be computed once per registry revision inside the snapshot rather than rebuilt during each retrieval call
    - reusable per-document TF-IDF vectors and norms may live in the snapshot when they stay tied to the same registry revision and do not create a parallel retrieval engine surface
- `retrieval/lexical.py`:
  - responsibility: produces lexical retrieval candidates from registry-owned sources and retrieval-owned index helpers
  - defines:
    - `LexicalRetrievalMode`
    - `LexicalRetriever`
  - depends_on:
    - `context_atlas.adapters.retrieval.indexing`
    - `context_atlas.adapters.retrieval.registry`
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - retrieval should return Atlas-native `ContextCandidate` artifacts, not prototype-specific DTOs
    - empty queries should fail soft with no candidates rather than inventing placeholder data
    - lexical retrieval should consume canonical sources through the registry surface rather than owning source registration itself
    - the retriever may cache one baseline index snapshot, but it should invalidate that cache strictly through the registry revision rather than inventing a second source-tracking mechanism
    - repeated-query retrieval should still enter through one fresh registry source listing per call even when the index snapshot is warm, so cache reuse cannot become a hidden second source-loading path
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
    - inferred source authority/durability should flow through shared domain source-semantics helpers rather than adapter-local default tables
    - provenance should preserve file identity and classification source so later traces can explain where a source came from
    - filesystem documents should now identify themselves as the `document` source family in canonical provenance
    - filesystem adapters should cross into canonical sources through `ContextSource.from_semantics(...)` rather than restating semantic fields piecemeal
    - adapter-local tags and source metadata should not restate canonical source class or other domain-owned meaning when provenance already carries the source-family-specific mechanics
- `records/structured.py`:
  - responsibility: validates structured-record inputs and translates them into canonical sources
  - defines:
    - `StructuredRecordInput`
    - `StructuredRecordPayload`
    - `StructuredRecordSourceAdapter`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - record adapters should accept already-fetched payloads rather than becoming a database access layer
    - record adapters may accept validated `StructuredRecordInput` objects or mapping-shaped record payloads, but richer client, session, cursor, or query objects should stay outside Atlas
    - record provenance should preserve source-family identity and adapter collector name
    - canonical `record_id` should remain authoritative in provenance metadata even when callers supply extra provenance fields
    - invalid `tags` or `intended_uses` container shapes should fail fast through shared domain source-semantics helpers rather than adapter-local coercion
    - record adapters should resolve fallback authority, durability, and intended uses through shared domain semantics rather than adapter-local defaults
    - record translation should emit canonical `ContextSource` artifacts without inventing a second source object hierarchy
    - record translation should now also cross through one resolved semantic profile rather than passing individual semantic fields into canonical sources
- `records/mappers.py`:
  - responsibility: shapes already-fetched row mappings into validated structured-record inputs before translation
  - defines:
    - `StructuredRecordRowMapper`
  - depends_on:
    - `context_atlas.domain.errors`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - row mappers should translate already-fetched mapping payloads only; they must not open connections, execute queries, or own client lifecycles
    - row mappers should stay small and validation-first so application integrations can rename fields without widening Atlas into a connector framework
    - row mappers should emit `StructuredRecordInput` objects so later translation still converges through one canonical source path
    - row mappers should construct those record inputs through the validated `StructuredRecordInput` surface rather than keeping a parallel ad hoc row schema alive inside adapters
    - when examples need one-step row-to-source translation, that crossing should still run through the adapter package rather than by rebuilding a parallel translation seam in workflow scripts

## Known Gaps / Future-State Notes
- This package currently covers filesystem documents, structured records, and in-memory lexical retrieval; provider-backed retrieval, embeddings, and broader live connector integration remain future work.
- Lexical retrieval hardening now separates source ownership, index-shape construction, and retrieval behavior, and the repeated-query TF-IDF path stays on one registry-driven retrieval surface instead of creating a second warm-cache engine mode.
- The current retrieval baseline now caches corpus-wide IDF state plus source-side TF-IDF vector state inside one registry-revision-aligned snapshot while still taking one fresh registry source listing per retrieval call; deeper observability/proof work and broader retrieval backends still remain future work.
- Structured-record adapters still assume already-fetched payloads and do not own query execution, sessions, vector-store clients, or connector lifecycles.
- If source-family coverage expands materially, this folder may need deeper package splits or nested owner files to stay governable.

## Cross-Folder Contracts
- `domain/`: adapters may consume canonical source/candidate artifacts plus stable error/message contracts, but may not redefine those semantics locally.
- `domain/`: candidate reranking, deduplication, and decision tracing now harden inward there; adapters should stop at source registration and candidate production.
- `domain/`: filesystem document adapters may classify source authority and durability, but those classifications should be expressed through canonical `ContextSource` fields rather than local enums or ad hoc tags.
- `domain/`: adapters may parse source-family-specific hints, but shared sequence coercion and fallback semantics should now come from `models/source_semantics.py` rather than adapter-local helper tables.
- `domain/`: adapters should carry source-family-specific mechanics in provenance or validated adapter inputs, then cross inward through one resolved semantic profile rather than copying semantic meaning into adapter-local tags or source metadata.
- `domain/`: source-family provenance may be expressed through canonical provenance fields, but structured-record input contracts should remain adapter-facing rather than becoming a second canonical source model.
- `domain/`: structured-record adapters may default source semantics when outer integrations do not supply them, but those defaults must still surface through canonical source fields and provenance.
- `services/`: future services should orchestrate retrieval through inward-safe contracts rather than by embedding lexical scoring logic directly.
- `infrastructure/`: adapters should not depend on infrastructure helpers unless a concrete runtime concern truly requires it.

## Verification Contract
```yaml
steps:
  - name: compile_adapters
    run: |
      # Linux/macOS analog: python3 -m compileall src/context_atlas/adapters
      py -3 -m compileall src/context_atlas/adapters

  - name: unit_tests
    run: |
      # Linux/macOS analog: python3 -m pytest tests/test_lexical_retrieval.py tests/test_filesystem_document_adapter.py tests/test_record_source_adapter.py tests/test_record_adapter_shape.py
      py -3 -m pytest tests/test_lexical_retrieval.py tests/test_filesystem_document_adapter.py tests/test_record_source_adapter.py tests/test_record_adapter_shape.py

  - name: import_sanity
    run: |
      # Linux/macOS analog:
      # export PYTHONPATH=src
      # python3 -c "from context_atlas.adapters import FilesystemDocumentSourceAdapter, InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever, StructuredRecordInput, StructuredRecordRowMapper, StructuredRecordSourceAdapter; from context_atlas.adapters.records import StructuredRecordPayload"
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.adapters import FilesystemDocumentSourceAdapter, InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever, StructuredRecordInput, StructuredRecordRowMapper, StructuredRecordSourceAdapter; from context_atlas.adapters.records import StructuredRecordPayload"
```
