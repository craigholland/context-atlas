# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 3e0be0b21d1c9cc01e29c36604f040ed777c9635
- timestamp_utc: 2026-04-19T14:24:42Z
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

## Known Gaps / Future-State Notes
- This folder now contains lexical retrieval plus a filesystem document adapter; embeddings and provider-backed adapters can land later as separate slices.
- This folder now also contains a structured-record adapter path over already-fetched record payloads; direct database-driver integration should still stay outside Atlas.
- Story 2 Task 2.1 should now also prove that the shared registry and lexical retrieval path stay source-family agnostic once canonical sources have been constructed.
- The current registry is intentionally in-memory and deterministic; persistence-backed source providers should arrive through separate adapters or infrastructure-backed ports later.
- Adapter outputs are now explicitly tested as immutable canonical artifacts so downstream services and renderers can trust their shape.
- The current starter API may re-export this package's supported exports, but deeper adapter modules should still stay out of the public surface unless they are intentionally stabilized.
- Story 2 Task 2.1 is now defining a minimal structured-record input contract; adapter-facing record shapes should stay small and validation-first rather than becoming a database access layer.
- Structured-record validation should now reject mapping-shaped `tags` and `intended_uses` inputs so integrations fail fast on malformed metadata instead of silently converting keys into canonical fields.
- Story 2 Task 2.2 should now remove duplicated source-semantics defaults from adapters where possible by consuming shared domain helpers instead of maintaining parallel normalization rules.
- Story 2 Task 2.2 now includes explicit semantic-consistency validation, so adapter changes should keep filesystem documents and structured records aligned on canonical authority, durability, and intended-use behavior when they share the same source class.
- Story 2 Task 2.3 is now making the adapter boundary explicit: Atlas may accept validated record inputs and mapping-shaped row payloads, but fetching/query execution should remain entirely outside this package.
- Story 2 Task 2.3 now also introduces a row-mapper pattern so application code can reshape already-fetched rows into validated record inputs without turning Atlas into a database or vector-store framework.
- Story 2 Task 2.3 now also reinforces that pattern through package exports and examples, so future adapter work should treat row shaping and canonical translation as the boundary rather than query execution.
- Story 2 Task 2.4 now also hardens the mixed-source boundary around `ContextSource.from_semantics(...)`, so adapters should preserve source-family mechanics in provenance while relying on the domain for canonical semantic meaning.
- Story 2 Task 2.4 now also reinforces that boundary in the repo-facing docs, so future adapter work should treat adapter-local tags or source metadata that restate canonical meaning as architectural drift, not convenience.
- Story 4 Task 4.1 is now defining the technical-builder docs-plus-database scenario, so adapter exports and docs should keep the already-fetched-record boundary explicit rather than implying Atlas owns database or vector-store access.
- Story 4 Task 4.2 now also exposes that scenario through a product-facing guide, so adapter docs and examples should keep explaining record translation as an after-fetch boundary rather than widening toward queries or client management.
- The runnable docs-plus-database example should keep demonstrating that `StructuredRecordRowMapper` and `StructuredRecordSourceAdapter` operate after row fetching, not as a query layer.
- Story 4 Task 4.2 now also includes tracked sample record payloads for the runnable workflow, so adapter-facing examples should treat those files as already-fetched outer inputs rather than as a reason to widen adapters into loaders or client wrappers.
- If examples add helper modules for resolving or loading tracked record payloads, that helper logic should remain outside this package and this owner file should keep the boundary explicit.

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
      py -3 -m compileall src/context_atlas/adapters

  - name: unit_tests
    run: |
      py -3 -m pytest tests/test_lexical_retrieval.py tests/test_filesystem_document_adapter.py tests/test_record_source_adapter.py tests/test_record_adapter_shape.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.adapters import FilesystemDocumentSourceAdapter, InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever, StructuredRecordInput, StructuredRecordRowMapper, StructuredRecordSourceAdapter; from context_atlas.adapters.records import StructuredRecordPayload"
```
