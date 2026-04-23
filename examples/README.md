# Examples

This directory holds runnable companion artifacts for the supported MVP
surfaces.

If you are looking for setup or workflow help, start with
[docs/Guides/README.md](/context-atlas/docs/Guides/README.md). Guides are the
primary user-facing help surface; `examples/` is where the runnable scripts,
sample payloads, and proof inputs live.

Current examples should prefer the curated `context_atlas.api` surface rather
than deep internal imports.

## Starter Flow

The recommended first example is:

```bash
python examples/starter_context_flow.py
```

That flow is the runnable companion to
[docs/Guides/getting_started.md](/context-atlas/docs/Guides/getting_started.md).

It demonstrates:

- supported starter imports from `context_atlas.api`
- validated settings loaded from the environment
- rendered context output
- packet inspection output
- trace inspection output

This is the intended runnable companion after an editable install. It defaults
to the checked-in sample repository docs under
`examples/codex_repository_workflow/sample_repo/docs` and a starter query, and
it keeps logs quieter unless you explicitly raise
`CONTEXT_ATLAS_LOG_LEVEL`.

## Smoke Flow

Run the starter smoke example against a docs directory:

PowerShell:

```powershell
$env:PYTHONPATH = "src"
py -3 examples/starter_api_smoke.py examples/codex_repository_workflow/sample_repo/docs "How should planning docs be treated?"
```

bash:

```bash
export PYTHONPATH=src
python examples/starter_api_smoke.py examples/codex_repository_workflow/sample_repo/docs "How should planning docs be treated?"
```

The smoke example demonstrates the supported MVP path:

- load validated settings from the environment
- ingest markdown docs with `FilesystemDocumentSourceAdapter`
- retrieve candidates with the starter lexical retriever
- assemble a `ContextPacket` through `build_starter_context_assembly_service`
- render packet context and inspect the resulting packet/trace surfaces

For the repo-local product path, prefer the checked-in sample repository docs
as the first-run corpus. The repo root `docs/` tree is broader than the
starter sample and should not be treated as the default smoke/evaluator input.

This sequence should stay aligned with the root `README.md` golden path and the
guides index. If examples start requiring extra hidden setup or deep internal
imports, the example surface should be corrected before more product-facing
guidance is added.

The shared hardening story now applies here too:

- the starter engine uses a shape-aware token-estimation heuristic by default
  rather than one flat chars-per-token assumption
- packet inspection should prefer the truthful budget vocabulary
  `fixed_reserved_tokens`, `unreserved_tokens`, and `unallocated_tokens`
- trace inspection should prefer the matching metadata keys
  `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`, and
  `budget_unallocated_tokens`
- packet and trace inspection should also prefer the truthful compression
  vocabulary `compression_strategy` and optional
  `configured_compression_strategy`
- retrieval index reuse and duplicate-acceptance review stay anchored by the
  named Story 5 baseline regressions rather than by a second proof-only example
  family

## Codex Repository Workflow Shape

The flagship Codex repository workflow currently uses the same shared starter engine, but with a repository-oriented outer composition boundary:

- start from a repository root
- point Atlas at the repository's governed docs under `<repo_root>/docs`
- assemble a packet for an engineering question
- render Codex-facing context plus packet/trace inspection from the canonical outputs

At this stage, the repository workflow should stay explicit about what it is not doing:

- it is not crawling arbitrary source files by default
- it is not reading git history or issue trackers automatically
- it is not introducing a Codex-specific engine path separate from the shared assembly service

The dedicated runnable example for that workflow lands in the Story 3 task slices under `examples/codex_repository_workflow/`.

Run the repository-oriented example directly:

```bash
python examples/codex_repository_workflow/run.py --repo-root .
```

When reviewing packet and trace output for this workflow, prefer the truthful
top-level budget and compression fields introduced by the hardening pass:

- packet: `fixed_reserved_tokens`, `unreserved_tokens`, `unallocated_tokens`
- trace: `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`,
  `budget_unallocated_tokens`
- either view: `compression_strategy`
- optional `configured_compression_strategy`

The current product-facing setup guide for that path is [docs/Guides/codex_repository_workflow.md](/context-atlas/docs/Guides/codex_repository_workflow.md).

See [examples/codex_repository_workflow/README.md](/context-atlas/examples/codex_repository_workflow/README.md) for the current supported repository path.

## Mixed-Source Flow

Run the mixed-source example after an editable install:

```bash
python examples/mixed_source_registry.py
```

This example demonstrates that filesystem documents and structured records can coexist in one registry and one packet-assembly flow without introducing a second canonical source model.

For structured records, the example boundary should stay narrow: outer application code fetches rows or payloads using its own database, vector-store, or API client, then hands Atlas either a validated `StructuredRecordInput` or a mapping-shaped record payload for translation into canonical sources. Atlas should not become the query framework in these examples.

The current Story 4 technical-builder scenario builds on that same boundary. It treats the mixed-source workflow as a chatbot-oriented path over:

- governed filesystem documents
- already-fetched support-style records such as tickets, product facts, or policy rows
- one shared packet and trace path after those inputs have crossed into canonical Atlas sources

The dedicated runnable example for that path now lives at [examples/docs_database_workflow/README.md](/context-atlas/examples/docs_database_workflow/README.md).

The product-facing setup guide for that same workflow now lives at [docs/Guides/docs_database_workflow.md](/context-atlas/docs/Guides/docs_database_workflow.md).

That mixed-source inspection story should use the same truthful top-level
budget and compression fields:

- packet: `fixed_reserved_tokens`, `unreserved_tokens`, `unallocated_tokens`
- trace: `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`,
  `budget_unallocated_tokens`
- either view: `compression_strategy`
- optional `configured_compression_strategy`
