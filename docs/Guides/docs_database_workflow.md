# Documents Plus Database Workflow

This guide walks through the current technical-builder workflow for Context Atlas.

The goal is to show how a builder can combine governed documents with
already-fetched record payloads, assemble one packet, and inspect the resulting
context, packet, and trace outputs without turning Atlas into a database access
framework.

If you want the broader user-help index first, start with
[Guides/README.md](./README.md).

## What You Will Do

You will:

1. install Context Atlas into a Python environment
2. optionally set runtime knobs through environment variables
3. point the workflow at a governed docs directory
4. hand Atlas already-fetched record rows through the supported record adapter boundary
5. run the documents-plus-database example
6. inspect the rendered chatbot context, packet view, and trace view

## Supported Workflow Shape

The current workflow is intentionally narrow:

- ingest governed filesystem documents
- translate already-fetched record payloads into canonical Atlas sources
- assemble one packet and one trace through the shared engine
- render a chatbot-facing context block plus packet and trace inspection

This workflow does not yet:

- open database connections
- execute queries or vector searches inside Atlas
- own ORM sessions, query builders, or client lifecycles

## Prerequisites

- Python `3.12+`
- a local checkout of this repository

## Install

From the repository root:

PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

Bash:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .[dev]
```

## Configure Runtime Knobs

The documents-plus-database workflow uses the same supported runtime knobs as the
starter and repository workflows. Those settings are documented in
[`.env.example`](../../.env.example).

`load_settings_from_env()` reads the live process environment. The example file is a
reference surface for supported settings, not an automatically loaded dotenv file.

If you want a visible local reference file:

PowerShell:

```powershell
Copy-Item .env.example .env
```

bash:

```bash
cp .env.example .env
```

Set a few values explicitly if you want to override defaults:

```powershell
$env:CONTEXT_ATLAS_LOG_LEVEL = "INFO"
$env:CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET = "1024"
$env:CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K = "8"
```

```bash
export CONTEXT_ATLAS_LOG_LEVEL="INFO"
export CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET="1024"
export CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K="8"
```

## Atlas Boundary For Records

The current technical-builder path is explicit about ownership:

- your application fetches rows or payloads from a database, vector store, or API
- Atlas accepts those already-fetched payloads
- Atlas validates and translates them into canonical `ContextSource` artifacts

The narrow adapter surface is:

- `StructuredRecordInput` for validated record objects
- `StructuredRecordRowMapper` for renaming already-fetched row fields
- `StructuredRecordSourceAdapter` for translation into canonical sources

For already-fetched row batches, the current preferred crossing is:

- keep the row mapper visible in outer workflow code
- let `StructuredRecordSourceAdapter.load_mapped_sources(...)` perform the
  mapper-plus-translation step into canonical sources

The example also keeps simple payload-file loading in
`examples/docs_database_workflow/record_feed.py`. That helper is part of the
outer workflow boundary, not the Atlas adapter layer.

That keeps Atlas responsible for context governance and packet assembly rather than
query execution.

## Run The Documents Plus Database Workflow

The current runnable example is:

- [examples/docs_database_workflow/run.py](../../examples/docs_database_workflow/run.py)
- [examples/docs_database_workflow/sample_records.json](../../examples/docs_database_workflow/sample_records.json)

From the repository root:

```bash
python examples/docs_database_workflow/run.py
```

By default, that run uses this repository's `docs/Guides/` tree plus the
tracked `examples/docs_database_workflow/sample_records.json` payload.

Override the docs root or chatbot question:

```bash
python examples/docs_database_workflow/run.py --docs-root /repos/my-app/docs --query "How should a builder configure Atlas and troubleshoot preflight failures?"
```

Override the sample record payload with your own already-fetched rows:

```bash
python examples/docs_database_workflow/run.py --records-file /repos/my-app/data/support_rows.json
```

If you want one run to make budget tradeoffs more obvious:

```bash
python examples/docs_database_workflow/run.py --total-budget 128
```

If you want the standard proof artifacts for the same run:

```bash
python examples/docs_database_workflow/run.py --proof-artifacts-dir tmp/mvp_proof/docs_database_demo
```

## What The Workflow Does

The current supported composition path is:

1. resolve a governed docs root
2. translate docs into canonical `ContextSource` artifacts
3. define the row-field mapping for already-fetched records in outer workflow code
4. let `StructuredRecordSourceAdapter.load_mapped_sources(...)` translate those rows into the same canonical `ContextSource` model
5. assemble one packet and one trace through the shared starter assembly service
6. render:
   - chatbot-facing context
   - packet inspection
   - trace highlights
   - trace inspection

That composition boundary is intentional:

- docs-root selection stays in outer workflow code
- the runnable example uses a tracked JSON payload file as a stand-in for outer application fetching
- payload-file loading stays in example-level workflow code, not in Atlas adapters
- row fetching stays in outer workflow code
- row-field mapping stays visible in outer workflow code, while the adapter package keeps the canonical row-to-source crossing in one place
- one-shot demo/proof overrides such as `--total-budget` and
  `--proof-artifacts-dir` stay at the runnable workflow boundary rather than
  becoming hidden adapter behavior
- packet and trace remain the authoritative outputs

## What To Look For

On a successful run, you should see:

- `=== Chatbot Context ===`
- `=== Packet Inspection ===`
- `=== Trace Highlights ===`
- `=== Trace Inspection ===`

The trace output should also make the workflow itself inspectable. Metadata such as
`request_workflow`, `request_docs_root`, `request_record_batch`, and
`request_record_origin` should remain visible so the example can explain which outer
path produced the packet.

If this guide, [README](../../README.md), and the
[Guides index](./README.md) stop telling the same story, the product-facing
documentation is drifting and should be corrected before new guidance is added.
