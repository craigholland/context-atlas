# Codex Repository Workflow

This guide walks through the current flagship repository workflow for Context Atlas.

The goal is to show how a Python engineer can point Atlas at a repository's governed
docs, assemble a packet for a real engineering question, and inspect the resulting
context, packet, and trace outputs.

## What You Will Do

You will:

1. install Context Atlas into a Python environment
2. optionally set runtime knobs through environment variables
3. point the workflow at a repository root and governed docs directory
4. run the Codex repository example
5. inspect the rendered context, packet view, and trace view

## Supported Workflow Shape

The current repository workflow is intentionally narrow:

- start from a repository root
- ingest governed docs rooted at `<repo_root>/docs`
- assemble a packet for an engineering question or task
- render a Codex-facing context block
- inspect packet and trace output

This workflow does not yet:

- crawl arbitrary source files
- read git history automatically
- connect to issue trackers or external repository systems

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

The Codex repository workflow uses the same supported runtime knobs as the starter
flow. Those settings are documented in [`.env.example`](../../.env.example).

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
$env:CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K = "6"
```

The current knobs cover:

- logging behavior
- starter assembly defaults
- starter compression defaults
- starter memory defaults

## Run The Repository Workflow

The current runnable example is:

- [examples/codex_repository_workflow/run.py](../../examples/codex_repository_workflow/run.py)

From the repository root:

```powershell
python examples/codex_repository_workflow/run.py --repo-root .
```

Override the engineering question:

```powershell
python examples/codex_repository_workflow/run.py --repo-root . --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?"
```

If you want to point at an explicit docs directory, use `--docs-root`. Relative
values are resolved from the selected repository root:

```powershell
python examples/codex_repository_workflow/run.py --repo-root C:\repos\my-repo --docs-root docs
```

If you want one run to make budget tradeoffs more obvious, the workflow also
supports a one-shot total-budget override:

```powershell
python examples/codex_repository_workflow/run.py --repo-root . --total-budget 128
```

If you want the standard proof artifacts for the same run:

```powershell
python examples/codex_repository_workflow/run.py --repo-root . --proof-artifacts-dir tmp\mvp_proof\codex_repository_demo
```

## Minimal Repository Layout

If you want a concrete reference for the current supported repository shape, see:

- [examples/codex_repository_workflow/sample_repo/README.md](../../examples/codex_repository_workflow/sample_repo/README.md)

That artifact describes the smallest governed-doc repository layout this workflow is
intended to support today.

## What The Workflow Does

The current supported composition path is:

1. resolve a repository root and governed docs root
2. translate governed docs into canonical `ContextSource` artifacts
3. retrieve candidate sources through the shared lexical retriever
4. build a packet through `assemble_with_starter_context_service(...)`
5. render:
   - Codex-facing context
   - packet inspection
   - trace inspection

That composition boundary is intentional:

- repository-root and docs-root selection stay in outer workflow code
- `assemble_with_starter_context_service(...)` remains the current
  workflow-facing convenience over the same shared starter assembly service
- one-shot demo/proof overrides such as `--total-budget` and
  `--proof-artifacts-dir` stay at the runnable workflow boundary rather than
  widening the core starter API
- packet and trace inspection remain derived views over canonical artifacts

## What To Look For

On a successful run, you should see:

- `=== Codex Context ===`
- `=== Packet Inspection ===`
- `=== Trace Inspection ===`

The trace output should make the workflow itself inspectable too. Metadata such as
`request_workflow`, `request_repo_root`, and `request_docs_root` should remain
visible so the example can explain which outer path produced the packet.

If this guide, [README](../../README.md), and [examples/README.md](../../examples/README.md)
stop telling the same story, the product-facing documentation is drifting and should
be corrected before new guidance is added.

## Demonstration Path

If you want a more review-oriented output than the main runnable example, use:

- [examples/codex_repository_workflow/show_trace.py](../../examples/codex_repository_workflow/show_trace.py)

Run it from the repository root:

```powershell
python examples/codex_repository_workflow/show_trace.py --repo-root .
```

That path keeps the same canonical packet/trace flow, but presents the results as:

- rendered Codex context
- concise trace highlights
- full trace inspection
