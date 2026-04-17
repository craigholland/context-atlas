# Context Atlas

Context Atlas is a standalone context-governance and context-assembly engine for Codex-powered systems and other provider-agnostic applications.

It exists to answer questions such as:

- What information should actually enter model context?
- Under what authority and trust rules should it be used?
- How should limited context budget be allocated?
- What should be retained, compressed, transformed, or excluded?
- How should inclusion decisions remain auditable and reproducible?

## Status

This repository is in architecture bootstrap. The initial focus is on authoritative documentation, ontology, package boundaries, and thin implementation slices rather than feature breadth.

## Principles

- Standalone and reusable, not an MAE submodule
- Provider-agnostic, while explicitly supporting Codex-powered systems
- Craig Architecture from day one
- Canonical structured packets before prompt rendering
- Authority-aware context governance, not just retrieval

## Initial Repository Layout

- `docs/` for project documentation and documentation ontology
- `src/context_atlas/` for the package source
- `tests/` for automated tests
- `examples/` for usage examples and demonstrations

## Runtime Knobs

The tracked [`.env.example`](K:/keven/codex_repo/context-atlas/.env.example) file is the canonical example surface for supported environment-backed runtime settings. As Context Atlas grows, new top-level environment knobs should be added there deliberately rather than appearing ad hoc in code or local-only setup.

## License

MPL-2.0
