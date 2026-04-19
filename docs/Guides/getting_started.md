# Getting Started

This guide walks through the current MVP starter path for Context Atlas.

The goal is to get from a local checkout to a first assembled packet using the supported starter surface, not to showcase every future workflow.

## What You Will Do

You will:

1. install Context Atlas into a Python environment
2. optionally configure runtime settings through `.env`
3. ingest a documentation directory
4. assemble a `ContextPacket`
5. inspect the rendered context, packet view, and trace view

## Prerequisites

- Python `3.14+`
- a local checkout of this repository

## Install

From the repository root:

```powershell
py -3.14 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -e .[dev]
```

If you prefer not to install the package into a virtual environment yet, the example below can also run with `PYTHONPATH=src`, but the editable install is the intended product-facing path.

## Configure Runtime Knobs

Context Atlas uses validated defaults, so you can run the starter example without setting every environment variable.

If you want a visible local configuration file:

```powershell
Copy-Item .env.example .env
```

The supported starter knobs are documented in [`.env.example`](../../.env.example). They are loaded through `load_settings_from_env()` and currently cover:

- logging behavior
- starter assembly defaults
- starter memory defaults

## Run The Starter Context Flow

The supported starter example is:

- [examples/starter_context_flow.py](../../examples/starter_context_flow.py)

Run it from the repository root:

```powershell
py -3 examples/starter_context_flow.py
```

That command uses the example defaults:

- `docs/` as the input directory
- `How should planning docs be treated?` as the starter query

If you want the repo-local no-install path instead:

```powershell
$env:PYTHONPATH = "src"
py -3 examples/starter_context_flow.py docs "How should planning docs be treated?"
```

For readability, the example defaults logging to `WARNING` unless you explicitly set `CONTEXT_ATLAS_LOG_LEVEL` yourself.

The example will:

- load validated settings from the environment
- ingest markdown docs from `docs/`
- retrieve candidates with the starter lexical retriever
- assemble a packet through the starter assembly service
- render:
  - packet context
  - packet inspection
  - trace inspection

## Supported Imports

For the starter flow, prefer:

```python
from context_atlas.api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    build_starter_context_assembly_service,
    load_settings_from_env,
    render_packet_context,
)
from context_atlas.rendering import (
    render_packet_inspection,
    render_trace_inspection,
)
```

That split is intentional:

- `context_atlas.api` is the curated starter namespace
- `context_atlas.rendering` is the supported home of derived packet/trace inspection views

## What To Look For

On a successful run, you should see:

- a rendered context block
- a packet summary that shows selected sources, budget state, and compression
- a trace summary that shows why sources were included, excluded, or transformed

If the output feels confusing, the root [README](../../README.md) and [examples/README.md](../../examples/README.md) should describe the same starter story. If they do not, the docs are drifting and should be corrected before adding more guidance.

The smaller [examples/starter_api_smoke.py](../../examples/starter_api_smoke.py) script is still useful for smoke validation, but `starter_context_flow.py` is the recommended onboarding path.
