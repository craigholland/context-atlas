# Examples

This directory holds small, focused usage examples for the supported MVP starter path.

Current examples should prefer the curated `context_atlas.api` surface rather than deep internal imports.

## Starter Flow

Run the starter smoke example against a docs directory:

```powershell
$env:PYTHONPATH = "src"
py -3 examples/starter_api_smoke.py docs "How should planning docs be treated?"
```

The smoke example demonstrates the supported MVP path:

- load validated settings from the environment
- ingest markdown docs with `FilesystemDocumentSourceAdapter`
- retrieve candidates with the starter lexical retriever
- assemble a packet through `build_starter_context_assembly_service`
- render context and inspect trace metadata
