# Low-Code Workflow

This guide walks through the current low-code workflow for Context Atlas.

The goal is to show how a less-technical builder can reach a working Atlas flow
through one supported preset-driven path without implying that Atlas is already
a broad no-code platform.

If you want the broader user-help index first, start with
[Guides/README.md](./README.md).

## What You Will Do

You will:

1. install Context Atlas into a Python environment
2. optionally set a small number of runtime knobs through environment variables
3. run the supported low-code workflow example
4. inspect the rendered chatbot context, packet view, and trace view

## Recommended Order

If you are evaluating this path for the first time, use the files in this
order:

1. [examples/low_code_workflow/config.example.toml](../../examples/low_code_workflow/config.example.toml)
2. [examples/low_code_workflow/presets/basic.toml](../../examples/low_code_workflow/presets/basic.toml)
3. [examples/low_code_workflow/README.md](../../examples/low_code_workflow/README.md)
4. [examples/low_code_workflow/run.py](../../examples/low_code_workflow/run.py)

That sequence keeps the product story honest:

- `config.example.toml` shows the tiny runtime-selection surface
- `presets/basic.toml` shows what the one supported preset actually means
- the example README shows how to run the workflow
- `run.py` is the runnable wrapper over the shared engine

## Supported Workflow Shape

The current low-code path is intentionally small:

- one supported preset: `chatbot_docs_records`
- one governed docs root
- one already-fetched record payload file
- one shared packet and trace path over the same starter engine used by the
  other MVP workflows

This workflow does not yet:

- discover sources automatically
- open database connections or vector-store clients
- own a visual builder, drag-and-drop UI, or no-code orchestration surface
- replace packet and trace inspection with opaque prompt strings

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

The low-code workflow uses the same supported runtime-knob surface documented in
[`.env.example`](../../.env.example). The current low-code-specific keys are:

- `CONTEXT_ATLAS_LOW_CODE_PRESET`
- `CONTEXT_ATLAS_LOW_CODE_DOCS_ROOT`
- `CONTEXT_ATLAS_LOW_CODE_RECORDS_FILE`
- `CONTEXT_ATLAS_LOW_CODE_INCLUDE_DOCUMENTS`
- `CONTEXT_ATLAS_LOW_CODE_INCLUDE_RECORDS`

Those keys are intentionally narrow. They choose a supported preset and source
inputs, but they do not redefine packet, trace, or policy semantics.

`load_settings_from_env()` reads the live process environment. `.env.example` is
a reference surface for supported settings, not an automatically loaded dotenv
file.

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
$env:CONTEXT_ATLAS_LOW_CODE_PRESET = "chatbot_docs_records"
$env:CONTEXT_ATLAS_LOW_CODE_DOCS_ROOT = "docs/Guides"
$env:CONTEXT_ATLAS_LOW_CODE_RECORDS_FILE = "examples/docs_database_workflow/sample_records.json"
```

```bash
export CONTEXT_ATLAS_LOG_LEVEL="INFO"
export CONTEXT_ATLAS_LOW_CODE_PRESET="chatbot_docs_records"
export CONTEXT_ATLAS_LOW_CODE_DOCS_ROOT="docs/Guides"
export CONTEXT_ATLAS_LOW_CODE_RECORDS_FILE="examples/docs_database_workflow/sample_records.json"
```

The same hardening semantics from the shared starter engine still apply here:

- `CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN` is a baseline control for the
  shape-aware starter estimator, not a promise of one flat ratio everywhere
- packet and trace views should prefer truthful budget/compression labels
- packet budget state should surface `fixed_reserved_tokens`,
  `unreserved_tokens`, and `unallocated_tokens`
- trace budget state should surface `budget_fixed_reserved_tokens`,
  `budget_unreserved_tokens`, and `budget_unallocated_tokens`
- compression state should surface `compression_strategy` and optional
  `configured_compression_strategy`

## Run The Low-Code Workflow

The current runnable example is:

- [examples/low_code_workflow/run.py](../../examples/low_code_workflow/run.py)
- [examples/low_code_workflow/README.md](../../examples/low_code_workflow/README.md)
- [examples/low_code_workflow/config.example.toml](../../examples/low_code_workflow/config.example.toml)
- [examples/low_code_workflow/presets/basic.toml](../../examples/low_code_workflow/presets/basic.toml)

The tracked TOML files are reference artifacts for the current MVP story:

- `config.example.toml` shows the tiny runtime-selection surface a host app can
  carry
- `presets/basic.toml` shows the single supported preset contract in a readable
  product-facing form

Neither file is auto-loaded by Atlas today. They are meant to make the current
supported low-code shape visible, not to imply a hidden config-loader or a
broader no-code platform.

The current single supported preset is also the workflow default, so `--preset`
is optional but supported when you want the invocation to be explicit:

```bash
python examples/low_code_workflow/run.py --preset chatbot_docs_records
```

From the repository root:

```bash
python examples/low_code_workflow/run.py
```

Override the query:

```bash
python examples/low_code_workflow/run.py --query "How should a low-code builder validate Atlas output?"
```

Override the docs root or records file relative to `--repo-root`:

```bash
python examples/low_code_workflow/run.py --repo-root /repos/my-app --docs-root docs/Guides --records-file data/support_rows.json
```

Inspect one source family in isolation:

```bash
python examples/low_code_workflow/run.py --no-documents
python examples/low_code_workflow/run.py --no-records
```

If you want the standard proof artifacts for the same run:

```bash
python examples/low_code_workflow/run.py --proof-artifacts-dir tmp/mvp_proof/low_code_demo
```

## What The Workflow Does

The current supported composition path is:

1. resolve one supported preset
2. resolve the configured docs root and/or records file from `--repo-root`
3. translate enabled source inputs into canonical `ContextSource` artifacts
4. assemble one packet and one trace through the shared starter engine
5. render:
   - chatbot-facing context
   - packet inspection
   - trace highlights
   - trace inspection

That boundary is intentional:

- preset selection is an outer workflow convenience
- docs and record payload choices are still explicit
- one-shot proof-artifact emission stays at the runnable workflow boundary
- packet and trace remain canonical outputs
- Atlas still does not own record fetching or connector lifecycles

## What To Look For

On a successful run, you should see:

- `=== Chatbot Context ===`
- `=== Packet Inspection ===`
- `=== Trace Highlights ===`
- `=== Trace Inspection ===`

The hardened low-code path should now make it easy to point at:

- packet budget state through `fixed_reserved_tokens`,
  `unreserved_tokens`, and `unallocated_tokens`
- trace budget state through `budget_fixed_reserved_tokens`,
  `budget_unreserved_tokens`, and `budget_unallocated_tokens`
- truthful compression state through `compression_strategy` and optional
  `configured_compression_strategy`
- low-code workflow metadata such as `request_workflow`,
  `request_low_code_preset`, `request_docs_root`, and `request_records_file`

The trace output should also make the workflow itself inspectable. Metadata such
as `request_workflow`, `request_low_code_preset`, `request_docs_root`, and
`request_records_file` should remain visible so the example can explain which
outer path produced the packet.

If this guide, [README](../../README.md), and the
[Guides index](./README.md) stop telling the same story, or if the tracked TOML
artifacts start implying a loader Atlas does not actually provide, the
low-code product surface is drifting and should be corrected before more
presets or wrapper behavior are added.
