# Getting Started

This guide walks through the current MVP starter path for Context Atlas.

The goal is to get from a local checkout to a first assembled packet using the supported starter surface, not to showcase every future workflow.

The current starter path requires Python `3.12+` and a local checkout of this
repository.

If you want the broader user-help index first, start with
[Guides/README.md](./README.md).

If you want the broader system walkthrough before running the starter path,
start with [Context Atlas Tour](./context_atlas_tour.md).

## What You Will Do

You will:

1. install Context Atlas into a Python environment
2. optionally configure runtime settings through environment variables
3. ingest a documentation directory
4. assemble a `ContextPacket`
5. inspect the rendered context, packet view, and trace view

## Prerequisites

- Python `3.12+`
- a local checkout of this repository

## Install

From the repository root:

PowerShell:

```powershell
py -3.12 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -e .[dev]
```

Bash:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .[dev]
```

If you prefer not to install the package into a virtual environment yet, the example below can also run with `PYTHONPATH=src`, but the editable install is the intended product-facing path.

## Configure Runtime Knobs

Context Atlas uses validated defaults, so you can run the starter example without setting every environment variable.

If you want a visible local reference file:

PowerShell:

```powershell
Copy-Item .env.example .env
```

bash:

```bash
cp .env.example .env
```

The supported starter knobs are documented in [`.env.example`](../../.env.example). That file is the canonical example surface for supported settings, but `load_settings_from_env()` reads the live process environment, not `.env` files automatically.

Set variables explicitly before running the example if you want to override defaults.

```powershell
$env:CONTEXT_ATLAS_LOG_LEVEL = "INFO"
$env:CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET = "1024"
```

```bash
export CONTEXT_ATLAS_LOG_LEVEL="INFO"
export CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET="1024"
```

Those environment-backed settings currently cover:

- logging behavior
- starter assembly defaults
- starter compression defaults
- starter memory defaults

The current supported configuration surface is intentionally smaller than the
full set of starter constants in code:

- ranking authority tables and trace-signal constants stay internal
- memory retention semantics stay internal unless they are already exposed
  through documented env-backed defaults
- canonical slot identifiers stay internal

The starter memory-budget split is now the supported way to change the default
documents-vs-memory balance without turning canonical slot identifiers into
public config. That knob is exposed as
`CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION`.

`CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN` remains the supported baseline
control for the starter token-estimation heuristic. Atlas now tightens that
estimate automatically for obviously structured code/markup and non-Latin-heavy
text, so the runtime story is no longer "one global 4 chars per token"
everywhere. Atlas does not yet expose a provider-specific tokenizer selector as
an env-backed runtime knob. Advanced Python integrations may bind a custom
callable estimator through `build_starter_context_assembly_service(...)` or
`assemble_with_starter_context_service(...)`, but that stays an outward
composition seam rather than a starter operator setting.

When you inspect packet and trace output after a run, prefer the settled
Story 4 vocabulary:

- packet budget state should surface `fixed_reserved_tokens`,
  `unreserved_tokens`, and `unallocated_tokens`
- trace budget state should surface `budget_fixed_reserved_tokens`,
  `budget_unreserved_tokens`, and `budget_unallocated_tokens`
- compression state should surface the effective `compression_strategy`, plus
  `configured_compression_strategy` only when fallback or intent needs to be
  shown explicitly

## Run The Starter Context Flow

The current installable starter command is:

```bash
context-atlas-starter docs --query "How should planning docs be treated?"
```

That command works after an editable install and does not require you to run a
repository-local example script directly.

If you are not working from this repository, replace `docs` with the path to
your own governed documentation directory.

If you are working from a repository checkout, the supported runnable companion
example is:

- [examples/starter_context_flow.py](../../examples/starter_context_flow.py)

Run it from the repository root:

```bash
python examples/starter_context_flow.py
```

That command uses the example defaults:

- `docs/` as the input directory
- `How should planning docs be treated?` as the starter query

If you want the repo-local no-install path instead, set `PYTHONPATH` explicitly:

```powershell
$env:PYTHONPATH = "src"
python examples/starter_context_flow.py docs "How should planning docs be treated?"
```

```bash
export PYTHONPATH=src
python examples/starter_context_flow.py docs "How should planning docs be treated?"
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
- a packet summary that shows selected sources, truthful budget state, and
  compression
- a trace summary that shows why sources were included, excluded, or
  transformed

More concretely, the hardened starter path should now make it easy to point at:

- `fixed_reserved_tokens`, `unreserved_tokens`, and `unallocated_tokens` in the
  packet view when budgeting matters
- `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`, and
  `budget_unallocated_tokens` in the trace view when budgeting matters
- `compression_strategy` and optional `configured_compression_strategy` when
  compression fallback truth matters across either inspection view
- the shared packet/trace story rather than a second demo-only artifact path

If the output feels confusing, the root [README](../../README.md) and the
[Guides index](./README.md) should describe the same starter story. If they do
not, the product-facing docs are drifting and should be corrected before adding
more guidance.

The smaller [examples/starter_api_smoke.py](../../examples/starter_api_smoke.py)
script is still useful for smoke validation, but `starter_context_flow.py` is
the recommended repository-local companion example. The installable starter
command remains the smallest package-facing onboarding path.
