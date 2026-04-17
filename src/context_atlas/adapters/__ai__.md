# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b688100f1e7fcbf13e3f98d934e2f899eab7cda3
- timestamp_utc: 2026-04-17T19:29:23Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

## Scope
- folder: src/context_atlas/adapters
- included:
  - "__init__.py"
  - "retrieval/**/*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds adapter-layer implementations that translate external or storage-facing inputs into Atlas-native artifacts.
- Provides the first retrieval-oriented adapter slice for turning registered `ContextSource` objects into ranked `ContextCandidate` outputs.
- Keeps lexical retrieval behavior outside the semantic core while still consuming domain-stable codes, events, messages, and canonical models.

## Architectural Rules
- Adapters may depend on `context_atlas.domain`, but `context_atlas.domain` must never import adapter implementations.
- Keep translation-heavy retrieval mechanics here rather than embedding tokenization or ranking implementation details into `domain/`.
- Adapter code should emit stable domain event ids and message templates rather than inventing inline semantic logger text.
- Do not let adapters import `context_atlas.infrastructure` by default just for convenience; prefer domain-stable contracts plus standard-library mechanics unless a specific outer dependency is justified.

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
- `retrieval`:
  - `InMemorySourceRegistry`: in-memory registry for canonical sources
  - `LexicalRetrievalMode`: supported keyword/TF-IDF retrieval modes
  - `LexicalRetriever`: Atlas-native lexical candidate builder

## File Index
- `__init__.py`:
  - responsibility: exposes the starter retrieval adapter surface for package-local use
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
    - `context_atlas.domain.events`
    - `context_atlas.domain.messages`
    - `context_atlas.domain.models`
  - invariants:
    - retrieval should return Atlas-native `ContextCandidate` artifacts, not prototype-specific DTOs
    - empty queries should fail soft with no candidates rather than inventing placeholder data
    - source registration should preserve stable source identifiers and reject duplicate ids

## Known Gaps / Future-State Notes
- This folder currently contains only lexical retrieval; embeddings, filesystem/doc adapters, and provider-backed adapters can land later as separate slices.
- The current registry is intentionally in-memory and deterministic; persistence-backed source providers should arrive through separate adapters or infrastructure-backed ports later.

## Cross-Folder Contracts
- `domain/`: adapters may consume canonical source/candidate artifacts plus stable error/event/message contracts, but may not redefine those semantics locally.
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
      py -3 -m pytest tests/test_lexical_retrieval.py

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "from context_atlas.adapters import InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever"
```
