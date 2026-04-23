# Context Atlas Tour

This guide is the system-level walkthrough for Context Atlas.

Use the root [README](../../README.md) as the map. Use this guide when you want
the next layer down: what Atlas currently owns, which workflow shapes are real,
which boundaries are intentional, and where to go for a deeper workflow guide.

If you want installation and first-run setup first, start with
[Getting Started](./getting_started.md).

## Mental Model

Context Atlas is a context-governance and context-assembly engine.

It takes one or more governed source inputs, applies authority, retrieval,
ranking, memory, budgeting, compression, and assembly rules, and produces:

- a `ContextPacket`
- a `ContextTrace`
- derived rendered views over those canonical artifacts

That means Atlas is not trying to be "just retrieval." It is trying to make
context decisions inspectable, reproducible, and reviewable.

## What Atlas Owns

Atlas currently owns:

- canonical source shaping into one shared `ContextSource` model
- retrieval, ranking, budgeting, compression, and memory behavior
- packet assembly
- trace production
- derived packet and trace inspection views

That shared packet-and-trace path is the center of the system. Workflow wrappers
and examples are supposed to stay thin and visible around it, not replace it.

## What Atlas Does Not Own

Atlas does **not** currently own:

- database connections, query execution, vector-store clients, or ORM sessions
- general-purpose connectors or connector lifecycle management
- broad code crawling, git history ingestion, or issue-system integration
- a visual builder, drag-and-drop UI, or a broader no-code orchestration
  platform

That boundary is deliberate. Atlas should act like a reusable governed pipeline
component, not a god framework.

## Current Source Families

The current source-family direction is intentionally small:

- governed filesystem documents as the first mature source family
- already-fetched structured records as the next adapter-facing source family
- one canonical `ContextSource` model regardless of ingestion path

For structured records, the current narrow adapter boundary is:

- `StructuredRecordInput` for validated record objects
- `StructuredRecordRowMapper` for visible outer row-field remapping
- `StructuredRecordSourceAdapter` for the canonical crossing into sources

That means application code still fetches rows or payloads outside Atlas. Atlas
accepts those already-fetched payloads, validates and reshapes them, and
translates them into the same canonical source model used by documents.

## Canonical Source And Mixed-Source Semantics

Source families are outer ingestion concerns. Inside Atlas, source meaning
should converge into one canonical semantic model.

That means:

- source class owns the default semantic posture for authority, durability, and
  intended use
- adapters may supply explicit overrides when outer workflow code knows better
- canonical source meaning should live on `ContextSource` itself rather than in
  adapter-local tags or provenance-only echoes

The current mixed-source boundary should remain explicit:

- adapters own source-family-specific parsing, shaping, and provenance capture
- adapters resolve source meaning through domain-owned semantic profiles
- adapters cross into canonical sources through `ContextSource.from_semantics(...)`
- services and renderers should consume mixed-source identity through canonical
  source helpers and trace metadata rather than reaching back into provenance
  structure everywhere

## Current Workflow Shapes

Context Atlas currently supports three real workflow surfaces.

### Starter Path

The supported MVP starter path is the smallest package-facing surface:

- install or check out the repo
- ingest a governed docs directory
- assemble a packet through the starter service
- render context plus packet/trace inspection

The current starter entry surfaces are:

- `context-atlas-starter`
- [Getting Started](./getting_started.md)

Treat that starter route as the baseline onboarding path. The workflow guides
below build on the same shared engine, but they are not the place to learn the
first-run setup story.

### Codex Repository Workflow

The flagship repository workflow is currently a thin composition path over the
same shared engine, not a separate engine mode.

It currently expects:

- a repository root
- governed docs rooted at `<repo_root>/docs`
- an engineering question or task query

It is repo-aware, but still intentionally narrow:

- it is governed-doc aware
- it is packet-and-trace aware
- it is not yet a general code crawler
- it does not yet own git history, issue systems, or arbitrary repository
  connectors

Deeper guide:

- [Codex Repository Workflow](./codex_repository_workflow.md)

### Documents Plus Database Workflow

The mixed-source technical-builder workflow is also intentionally narrow.

It currently shows how to:

- ingest governed documents
- hand Atlas already-fetched record rows or payloads
- translate both source families into one canonical source model
- assemble one packet and one trace through the shared engine

It does **not** turn Atlas into a database-access framework.

Deeper guide:

- [Documents Plus Database Workflow](./docs_database_workflow.md)

### Low-Code Workflow

The current low-code path is intentionally small.

It is a preset-driven wrapper over the same starter engine, not a broader
no-code platform. Today that means:

- one supported preset
- one governed docs root
- one already-fetched record payload file
- one shared packet and trace path

Deeper guide:

- [Low-Code Workflow](./low_code_workflow.md)

## Packet And Trace Inspection

Context Atlas inspection surfaces are derived views over canonical artifacts,
not replacements for them.

For practical review, packet inspection should make it easy to see:

- selected candidates
- retained memory entries
- budget state
- whether compression was applied

Trace inspection should make it easy to see:

- inclusion, exclusion, transformation, and deferred decisions
- why a source was rejected or transformed
- metadata explaining ranking, budgeting, compression, and memory behavior

The current truthful inspection vocabulary matters:

- packet budget state:
  - `fixed_reserved_tokens`
  - `unreserved_tokens`
  - `unallocated_tokens`
- trace budget state:
  - `budget_fixed_reserved_tokens`
  - `budget_unreserved_tokens`
  - `budget_unallocated_tokens`
- compression state:
  - `compression_strategy`
  - optional `configured_compression_strategy`

Those views should remain read-only derived renderings over `ContextPacket` and
`ContextTrace`.

For one concrete starter-facing example, see
[starter_context_flow_sample_output.md](../../examples/starter_context_flow_sample_output.md).
That checked-in sample uses the same bounded corpus as the current
[Getting Started](./getting_started.md) path and shows rendered context,
packet inspection, and trace inspection together without introducing a second
demo vocabulary.

## Runtime Knobs

The tracked [`.env.example`](../../.env.example) file is the canonical example
surface for supported environment-backed runtime settings.

The supported surface is intentionally narrow:

- logging behavior
- starter assembly defaults
- starter compression defaults
- starter memory defaults
- low-code wrapper inputs

Some important things are intentionally not part of the supported public
runtime-knob surface yet:

- ranking authority tables and ranking signal names
- memory-scoring semantics
- canonical slot identifiers

`CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN` is still the baseline control for
the starter token-estimation heuristic, but Atlas no longer treats all content
as one flat ratio. The starter path now tightens estimates automatically for
obviously structured code/markup and non-Latin-heavy text while staying
provider-agnostic.

## Proof And Review Surface

The current MVP proof story is intentionally packet-and-trace centered.

Atlas should not claim readiness based only on narrative impressions or
polished screenshots. The reviewable evidence path should come from canonical
packet, trace, and rendered-context artifacts emitted by supported workflow
runs.

The main proof and review surfaces are:

- [docs/Reviews/MVP/mvp_readiness_assessment.md](../Reviews/MVP/mvp_readiness_assessment.md)
- [docs/Reviews/MVP/mvp_evaluation_rubric.md](../Reviews/MVP/mvp_evaluation_rubric.md)
- [examples/mvp_proof/README.md](../../examples/mvp_proof/README.md)

The current recommendation in the review record is `MVP Ready`.

## Where To Go Next

- if you want a first run: [Getting Started](./getting_started.md)
- if you want the flagship workflow: [Codex Repository Workflow](./codex_repository_workflow.md)
- if you want mixed-source records plus docs: [Documents Plus Database Workflow](./docs_database_workflow.md)
- if you want the preset-driven wrapper: [Low-Code Workflow](./low_code_workflow.md)
- if you want runnable companions: [examples/README.md](../../examples/README.md)
