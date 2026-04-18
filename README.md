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

See [examples/README.md](/context-atlas/examples/README.md) and [examples/starter_api_smoke.py](/context-atlas/examples/starter_api_smoke.py) for the current golden-path smoke flow.

## Packet And Trace Inspection Contract

Context Atlas inspection surfaces are derived views over canonical artifacts, not replacements for them.

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

## Runtime Knobs

The tracked [`.env.example`](/context-atlas/.env.example) file is the canonical example surface for supported environment-backed runtime settings. As Context Atlas grows, new top-level environment knobs should be added there deliberately rather than appearing ad hoc in code or local-only setup.

## License

MPL-2.0
