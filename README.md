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

When application rows need field remapping before translation, the current MVP pattern is to use `context_atlas.adapters.StructuredRecordRowMapper`:

```python
from context_atlas.adapters import (
    StructuredRecordRowMapper,
    StructuredRecordSourceAdapter,
)

rows = fetch_rows_somewhere_outside_atlas()

mapper = StructuredRecordRowMapper(
    record_id_field="ticket_id",
    content_field="summary",
    title_field="title",
    metadata_fields=("team", "table"),
    provenance_fields=("database",),
    source_class="reviews",
    fixed_intended_uses=("triage",),
)

sources = StructuredRecordSourceAdapter().load_mapped_sources(
    rows,
    row_mapper=mapper,
)
```

That keeps Atlas responsible for shaping and canonical translation, while outer
integration code remains responsible for database access, vector-store access,
or API calls. The mapper names the outer row shape, and the adapter remains the
canonical crossing into `ContextSource` artifacts.

Future adapter work should preserve the same guardrails:

- Atlas adapters may validate and reshape already-fetched payloads
- Atlas adapters should translate payloads into canonical `ContextSource` artifacts
- Atlas adapters should not own connections, sessions, queries, or client lifecycles
- Atlas adapters should not become a general-purpose connector or ORM facade
- outer integration code should remain responsible for fetching rows, vectors, or API responses before Atlas sees them

See [examples/mixed_source_registry.py](/context-atlas/examples/mixed_source_registry.py) for the current mixed-source example that assembles filesystem documents and structured records through one shared registry and packet flow.

## Documents Plus Database Workflow Shape

The current Story 4 technical-builder scenario is intentionally specific: a builder wants to assemble chatbot context from governed documentation plus already-fetched support-style records such as tickets, policy rows, or product facts.

That workflow should currently look like this:

1. outer application code chooses the governed docs root
2. outer application code fetches rows or record payloads from its own database, vector store, or API client
3. `FilesystemDocumentSourceAdapter` translates the docs into canonical `ContextSource` artifacts
4. `StructuredRecordRowMapper` or validated `StructuredRecordInput` objects normalize the fetched record payloads into Atlas-ready record shapes
5. `StructuredRecordSourceAdapter` performs the canonical crossing into the same `ContextSource` model used by documents, including the one-step `load_mapped_sources(...)` path for already-fetched rows
6. one shared registry, retriever, assembly service, packet, and trace path operates over both source families together

That means Atlas is demonstrating a real pipeline-component role here:

- Atlas governs mixed-source context assembly
- Atlas does not own the database query surface
- Atlas does not own the vector-store client surface
- Atlas does not create a second packet path just because record-backed inputs are present

The current runnable example for that path lives at [examples/docs_database_workflow/README.md](/context-atlas/examples/docs_database_workflow/README.md).

The product-facing setup guide for that path now lives at [docs/Guides/docs_database_workflow.md](/context-atlas/docs/Guides/docs_database_workflow.md).

The runnable path now also includes a tracked sample record payload so a technical builder can evaluate the mixed-source packet and trace flow without first wiring a real database client.

## Low-Code Workflow Shape

The incoming low-code workflow is intentionally small. Its configuration surface
should let a less-technical builder declare:

- one preset name
- whether documents and/or structured records are enabled
- a docs root
- a record payload file

That means the low-code path is still a wrapper around the same engine:

- presets remain outer configuration, not domain truth
- low-code settings choose supported source inputs and starter defaults
- packet and trace artifacts remain canonical and shared with every other workflow
- low-code override merging should happen through validated infrastructure settings,
  not ad hoc example-script dictionaries
- low-code wrappers should build a resolved outer workflow plan and then hand
  canonical sources into the shared starter assembly seam rather than packing a
  second orchestration path

The current runtime surface for that path now lives in [`.env.example`](/context-atlas/.env.example)
under the `CONTEXT_ATLAS_LOW_CODE_*` keys. The broader assembly, compression,
and memory knobs remain available too, but the low-code path should prefer
presets plus a very small declarative source surface before exposing deeper
runtime tuning.

The first supported wrapper for that path now lives at
[examples/low_code_workflow/run.py](/context-atlas/examples/low_code_workflow/run.py).
It currently supports one preset, `chatbot_docs_records`, which keeps the
workflow intentionally concrete:

- governed guide docs
- a tracked JSON payload of already-fetched support-style records
- one shared `ContextPacket` and `ContextTrace` path after preset-driven source selection

That means the low-code path is still a real Atlas component integration, not a
forked engine mode. The preset chooses source-shaping defaults, but packet
assembly, budgeting, compression, and trace inspection still run through the
same shared starter engine path used by the other workflows.

The current low-code boundary is now intentionally explicit:

- `ContextAtlasSettings.with_low_code_overrides(...)` owns validated override
  merging for the wrapper path
- `build_low_code_workflow_plan(...)` owns preset resolution, repo-relative path
  resolution, and workflow-facing metadata assembly
- `assemble_with_starter_sources(...)` remains the shared starter seam from
  canonical sources into packet assembly
- low-code examples should not hand-pack packet metadata, re-merge runtime
  settings, or invent alternate packet/trace behavior for convenience

Run the current low-code example from the repository root:

```powershell
python examples/low_code_workflow/run.py
```

To inspect one source family in isolation, disable one side of the preset-driven
input surface:

```powershell
python examples/low_code_workflow/run.py --no-documents
python examples/low_code_workflow/run.py --no-records
```

Relative `--docs-root` and `--records-file` overrides are resolved from
`--repo-root`, so the wrapper stays explicit about its outer workflow boundary
instead of hiding source resolution inside the engine.

The product-facing guide for that path now lives at
[docs/Guides/low_code_workflow.md](/context-atlas/docs/Guides/low_code_workflow.md).

The example-oriented README for that path now lives at
[examples/low_code_workflow/README.md](/context-atlas/examples/low_code_workflow/README.md).

Tracked reference artifacts for the current low-code story now also live at:

- [examples/low_code_workflow/config.example.toml](/context-atlas/examples/low_code_workflow/config.example.toml)
- [examples/low_code_workflow/presets/basic.toml](/context-atlas/examples/low_code_workflow/presets/basic.toml)

If you are evaluating the low-code path for the first time, the recommended
order is:

1. `config.example.toml`
2. `presets/basic.toml`
3. `examples/low_code_workflow/README.md`
4. `examples/low_code_workflow/run.py`

That order is intentional. The tracked TOML files are reference surfaces for
the current MVP story, not hidden config loaders or a broader no-code platform.

## MVP Proof Direction

The current MVP proof work now has an explicit review rubric at
[docs/Reviews/MVP/mvp_evaluation_rubric.md](/context-atlas/docs/Reviews/MVP/mvp_evaluation_rubric.md).

That rubric is intentionally centered on:

- packet quality against a naive baseline
- trace legibility
- authority handling
- budget behavior
- workflow reproducibility

The proof story should stay packet-and-trace-centered. Atlas should not claim
MVP readiness based only on narrative impressions or polished screenshots.

The first reproducible packaging path for those artifacts now lives at
[examples/mvp_proof/README.md](/context-atlas/examples/mvp_proof/README.md) and
[scripts/mvp_proof/capture_evidence.py](/context-atlas/scripts/mvp_proof/capture_evidence.py).

The current proof pass is scoped to the three supported MVP workflows:

- `codex_repository` with the `repo_governed_docs_update` scenario
- `docs_database_builder` with the `builder_support_troubleshooting` scenario
- `low_code_chatbot` with the `low_code_validation` scenario

Those workflows are included because they already have runnable local paths,
packet and trace inspection, and reproducible tracked inputs. Workflows that
need live external services or unpublished setup steps should not be counted in
the current MVP proof pass.

Each selected workflow can now also emit the same standard Atlas proof
artifacts from its runnable example boundary when `--proof-artifacts-dir` is
supplied:

- `atlas_rendered_context.txt`
- `atlas_packet.json`
- `atlas_trace.json`

That shared artifact shape is what allows
[scripts/mvp_proof/capture_evidence.py](/context-atlas/scripts/mvp_proof/capture_evidence.py)
to package proof scenarios without workflow-specific file wiring. See
[examples/mvp_proof/inputs/README.md](/context-atlas/examples/mvp_proof/inputs/README.md)
for the current proof commands and scenario inputs.

## Canonical Source Semantics

Source families are outer ingestion concerns. Inside the Atlas domain, source meaning should converge into one canonical semantic model.

That means source class owns the default semantic posture for:

- authority
- durability
- intended uses

Adapters may still supply explicit overrides when the outer system knows better, but the shared defaults should remain domain-owned so filesystem documents, structured records, and future source families do not invent parallel semantic rules.

## Mixed-Source Boundary Model

The current mixed-source architecture should follow one explicit boundary:

- adapters own source-family-specific parsing, shaping, and provenance capture
- adapters resolve source meaning through domain-owned semantic profiles
- adapters cross into canonical sources through `ContextSource.from_semantics(...)`
- canonical source meaning then lives on `ContextSource` itself, not in adapter-local tags or source metadata echoes
- services and renderers should consume mixed-source identity through canonical source helpers and trace metadata rather than reaching back into provenance structure throughout the codebase

In practice, that means filesystem adapters may keep document-specific mechanics in provenance metadata, structured-record adapters may keep record-specific mechanics in validated inputs and provenance, and the rest of the engine should still work over one canonical `ContextSource` model.

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

## Codex Repository Workflow Shape

The flagship Codex repository workflow should currently be understood as a thin reference composition path over the same shared Atlas engine, not as a separate engine mode.

The current supported repository inputs are intentionally narrow:

- a repository root
- governed repository documents rooted at `<repo_root>/docs`
- an engineering question or task query

The current supported composition path is:

1. outer workflow code resolves the governed docs root from the repository
2. `FilesystemDocumentSourceAdapter` translates those docs into canonical `ContextSource` artifacts
3. `InMemorySourceRegistry` and `LexicalRetriever` produce the candidate flow
4. `assemble_with_starter_context_service(...)` or `build_starter_context_assembly_service(...).assemble(...)` wires the same shared policies and settings into the canonical assembly service path
5. the workflow renders Codex-facing context from the resulting `ContextPacket` and keeps packet/trace inspection visible

The outer workflow metadata that defines that path should remain inspectable too. If
workflow code supplies metadata such as `workflow`, `repo_root`, or `docs_root`,
the shared assembly service should preserve it in trace metadata rather than hiding
that context inside example-only print logic.

That means the current Codex repository story is repo-aware, but still honest about scope:

- it is governed-doc aware
- it is packet-and-trace aware
- it is not yet a general code crawler
- it does not yet own git history, issue systems, or arbitrary repository connectors

Those broader repository inputs can come later, but they should extend the same engine path rather than replacing it with Codex-specific orchestration.

Within `examples/codex_repository_workflow/`, `run.py` is now the authoritative outer workflow composition path. `show_trace.py` should stay a derived demonstration over that same parser and packet-assembly path rather than growing a second copy of repository workflow composition.

The product-facing setup guide for that path now lives at [docs/Guides/codex_repository_workflow.md](/context-atlas/docs/Guides/codex_repository_workflow.md).

The runnable reference example for that path now lives at [examples/codex_repository_workflow/README.md](/context-atlas/examples/codex_repository_workflow/README.md).

The minimal repository-shape reference for that path now lives at [examples/codex_repository_workflow/sample_repo/README.md](/context-atlas/examples/codex_repository_workflow/sample_repo/README.md).

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

Workflow-facing labels such as `Repository Context` should remain caller-supplied presentation at the example or app boundary. Generic renderers should default to generic labels rather than baking one workflow's vocabulary into canonical rendering behavior.

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
