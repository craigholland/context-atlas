# Documents Plus Database Workflow

This guide walks through the current technical-builder workflow for Context Atlas.

The goal is to show how a builder can combine governed documents with
already-fetched record payloads, assemble one packet, and inspect the resulting
context, packet, and trace outputs without turning Atlas into a database access
framework.

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

- Python `3.14+`
- a local checkout of this repository

## Install

From the repository root:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

## Configure Runtime Knobs

The documents-plus-database workflow uses the same supported runtime knobs as the
starter and repository workflows. Those settings are documented in
[`.env.example`](../../.env.example).

`load_settings_from_env()` reads the live process environment. The example file is a
reference surface for supported settings, not an automatically loaded dotenv file.

If you want a visible local reference file:

```powershell
Copy-Item .env.example .env
```

If you want to set a few values explicitly in PowerShell:

```powershell
$env:CONTEXT_ATLAS_LOG_LEVEL = "INFO"
$env:CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET = "1024"
$env:CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K = "8"
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

That keeps Atlas responsible for context governance and packet assembly rather than
query execution.

## Run The Documents Plus Database Workflow

The current runnable example is:

- [examples/docs_database_workflow/run.py](../../examples/docs_database_workflow/run.py)

From the repository root:

```powershell
python examples/docs_database_workflow/run.py
```

Override the docs root or chatbot question:

```powershell
python examples/docs_database_workflow/run.py --docs-root C:\repos\my-app\docs --query "How should a builder configure Atlas and troubleshoot preflight failures?"
```

## What The Workflow Does

The current supported composition path is:

1. resolve a governed docs root
2. translate docs into canonical `ContextSource` artifacts
3. reshape already-fetched record rows into validated record inputs
4. translate those record inputs into the same canonical `ContextSource` model
5. assemble one packet and one trace through the shared starter assembly service
6. render:
   - chatbot-facing context
   - packet inspection
   - trace highlights
   - trace inspection

That composition boundary is intentional:

- docs-root selection stays in outer workflow code
- row fetching stays in outer workflow code
- record shaping and translation happen through the supported adapter boundary
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

If this guide, [README](../../README.md), and [examples/README.md](../../examples/README.md)
stop telling the same story, the product-facing documentation is drifting and should
be corrected before new guidance is added.
