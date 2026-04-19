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
