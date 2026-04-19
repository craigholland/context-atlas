# Examples

This directory holds small, focused usage examples for the supported MVP starter path.

Current examples should prefer the curated `context_atlas.api` surface rather than deep internal imports.

## Starter Flow

The recommended first example is:

```powershell
python examples/starter_context_flow.py
```

That flow is also documented in [docs/Guides/getting_started.md](/context-atlas/docs/Guides/getting_started.md).

It demonstrates:

- supported starter imports from `context_atlas.api`
- validated settings loaded from the environment
- rendered context output
- packet inspection output
- trace inspection output

This is the intended onboarding example after an editable install. It defaults to the repository `docs/` directory and a starter query, and it keeps logs quieter unless you explicitly raise `CONTEXT_ATLAS_LOG_LEVEL`.

## Smoke Flow

Run the starter smoke example against a docs directory:

```powershell
$env:PYTHONPATH = "src"
py -3 examples/starter_api_smoke.py docs "How should planning docs be treated?"
```

The smoke example demonstrates the supported MVP path:

- load validated settings from the environment
- ingest markdown docs with `FilesystemDocumentSourceAdapter`
- retrieve candidates with the starter lexical retriever
- assemble a `ContextPacket` through `build_starter_context_assembly_service`
- render packet context and inspect the resulting packet/trace surfaces

This sequence should stay aligned with the root `README.md` golden path. If examples start requiring extra hidden setup or deep internal imports, the example surface should be corrected before more product-facing guidance is added.

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

```powershell
python examples/codex_repository_workflow/run.py --repo-root .
```

The current product-facing setup guide for that path is [docs/Guides/codex_repository_workflow.md](/context-atlas/docs/Guides/codex_repository_workflow.md).

See [examples/codex_repository_workflow/README.md](/context-atlas/examples/codex_repository_workflow/README.md) for the current supported repository path.

## Mixed-Source Flow

Run the mixed-source example after an editable install:

```powershell
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
