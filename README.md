# Context Atlas

Context Atlas is a standalone context-governance and context-assembly engine for Codex-powered systems and other provider-agnostic applications.

It exists to answer questions such as:

- What information should actually enter model context?
- Under what authority and trust rules should it be used?
- How should limited context budget be allocated?
- What should be retained, compressed, transformed, or excluded?
- How should inclusion decisions remain auditable and reproducible?

## Status

This repository has completed its initial architecture and governance bootstrap. Context Atlas now has a first end-to-end starter implementation for canonical source modeling, retrieval, ranking, budgeting, compression, memory retention, packet assembly, and ontology-aware filesystem document ingestion.

The current focus is implementation hardening rather than feature breadth: tightening model surfaces, standardizing validated Pydantic contracts, strengthening error and logging semantics, and continuing to refine the starter policies and adapter boundaries before broader expansion.

## Principles

- Standalone and reusable
- Provider-agnostic, while explicitly supporting Codex-powered systems
- Craig Architecture from day one
- Canonical structured packets before prompt rendering
- Authority-aware context governance, not just retrieval

## Initial Repository Layout

- `docs/` for project documentation and documentation ontology
- `src/context_atlas/` for the package source
- `tests/` for automated tests
- `examples/` for usage examples and demonstrations

## Starter Source Families

The shared engine is no longer intended to be docs-only. The current source-family direction is:

- filesystem documents as the first mature source family
- structured records as the next adapter-facing input family
- one canonical `ContextSource` model regardless of ingestion path

For structured records, the current minimum adapter contract is `context_atlas.adapters.StructuredRecordInput`. It stays intentionally small so outer integrations can adapt database rows, vector-search payloads, or already-fetched record objects into one validated record shape before translating them into canonical sources.

The current translation surface for those inputs is `context_atlas.adapters.StructuredRecordSourceAdapter`. It accepts:

- validated `StructuredRecordInput` objects
- mapping-shaped row payloads that outer integration code already fetched

It does not own query execution, database clients, ORM sessions, or vector-store client lifecycles. Those stay outside Atlas and should hand Atlas a normalized record-shaped payload only after data access has already happened.

Within that boundary, the adapter preserves provenance and intended-use metadata and emits the same canonical `ContextSource` artifacts the rest of the engine already understands.

See [examples/mixed_source_registry.py](/context-atlas/examples/mixed_source_registry.py) for the current mixed-source example that assembles filesystem documents and structured records through one shared registry and packet flow.

## Canonical Source Semantics

Source families are outer ingestion concerns. Inside the Atlas domain, source meaning should converge into one canonical semantic model.

That means source class owns the default semantic posture for:

- authority
- durability
- intended uses

Adapters may still supply explicit overrides when the outer system knows better, but the shared defaults should remain domain-owned so filesystem documents, structured records, and future source families do not invent parallel semantic rules.

## Supported MVP Entry Surface

The current supported MVP starter path is intentionally explicit.

Prefer imports like:

```python
from context_atlas.api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    build_starter_context_assembly_service,
    load_settings_from_env,
    render_packet_context,
)
```

The package root currently remains intentionally thin. User-facing docs and examples should prefer `context_atlas.api` for the starter flow, and only reach for stable subpackage imports when they are intentionally teaching the architecture.

That split is part of the supported architecture:

- `context_atlas.api` is the curated starter namespace for ingestion, settings, and assembly wiring
- `context_atlas.rendering` is the supported home of derived packet and trace views
- the package root should not become a broad convenience barrel that hides those distinctions

The recommended first run is [examples/starter_context_flow.py](/context-atlas/examples/starter_context_flow.py). It is designed to be the first user-facing run after an editable install. [examples/starter_api_smoke.py](/context-atlas/examples/starter_api_smoke.py) remains useful as a smaller smoke example, but it is no longer the primary onboarding path.

See [examples/README.md](/context-atlas/examples/README.md) for the current starter-flow index.

## MVP Golden Path

The current MVP onboarding story should read as one clear sequence:

1. install Context Atlas into a Python environment
2. configure supported runtime knobs through environment settings
3. ingest governed repository documents
4. assemble a `ContextPacket` through the supported starter service
5. render packet context and inspect packet/trace output

This repository does not yet present every future workflow. The current user-facing guidance should stay centered on that starter path so a new evaluator can get from installation to a first packet without inferring the product shape from internal modules.

The current starter walkthrough lives in [docs/Guides/getting_started.md](/context-atlas/docs/Guides/getting_started.md).

## Packet And Trace Inspection Contract

Context Atlas inspection surfaces are derived views over canonical artifacts, not replacements for them.

An attached transformation artifact does not replace canonical packet content unless the transformation was actually applied. If compression metadata is present but `was_applied` is false, starter rendering should continue to derive candidate content from the canonical selected candidates.

For MVP users, packet inspection should emphasize:

- selected source candidates
- retained memory entries
- budget state
- whether compression was applied

Trace inspection should emphasize:

- inclusion, exclusion, transformation, and deferred decisions
- why a source was rejected or transformed
- trace metadata that explains ranking, budgeting, compression, and memory behavior

Those inspection surfaces should live under `context_atlas.rendering` and remain read-only views over `ContextPacket` and `ContextTrace`.

Current packet inspection lives at:

```python
from context_atlas.rendering import render_packet_inspection
```

Current trace inspection lives at:

```python
from context_atlas.rendering import render_trace_inspection
```

## Runtime Knobs

The tracked [`.env.example`](/context-atlas/.env.example) file is the canonical example surface for supported environment-backed runtime settings. For the current MVP path, those knobs should help a new user understand logging, assembly defaults, compression behavior, and memory behavior without reading internal implementation modules first.

`load_settings_from_env()` reads the live process environment. The example file is a reference surface for supported settings, not an automatically loaded dotenv path.

As Context Atlas grows, new top-level environment knobs should be added there deliberately rather than appearing ad hoc in code or local-only setup.

## License

MPL-2.0
