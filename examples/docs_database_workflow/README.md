# Documents Plus Database Workflow Example

This example demonstrates the current technical-builder workflow for Context Atlas.

For product-facing setup guidance, start with
[docs/Guides/docs_database_workflow.md](/context-atlas/docs/Guides/docs_database_workflow.md).
This README is the runnable companion artifact for that guide.

Current supported shape:

- point Atlas at a governed docs directory
- fetch rows or payloads outside Atlas using your own database, vector-store, or API client
- keep any row-field naming choices visible at the outer workflow boundary
- let the adapter package perform the mapped-row to canonical-source crossing
- assemble one packet and one trace through the shared engine

The runnable demo stays honest about the boundary:

- filesystem documents come from this repository's `docs/Guides/` tree by default
- support-style records come from the tracked `sample_records.json` artifact by default
- Atlas shapes and translates those rows, but it does not execute the database query
- `StructuredRecordSourceAdapter.load_mapped_sources(...)` is the current one-step crossing from already-fetched rows plus a row mapper into canonical sources
- `record_feed.py` keeps payload-file loading at the outer workflow boundary rather than inside Atlas adapters

## Run

After an editable install:

```bash
python examples/docs_database_workflow/run.py
```

Override the docs root or chatbot question:

```bash
python examples/docs_database_workflow/run.py --docs-root /repos/my-app/docs --query "How should I configure Atlas and troubleshoot preflight failures?"
```

Point the example at your own already-fetched rows:

```bash
python examples/docs_database_workflow/run.py --records-file /repos/my-app/data/support_rows.json
```

The output shows:

- the rendered chatbot-facing context block
- packet inspection
- trace highlights
- full trace inspection

Use the hardened top-level packet and trace fields when reviewing those
inspection surfaces:

- `fixed_reserved_tokens`
- `unreserved_tokens`
- `unallocated_tokens`
- `compression_strategy`
- optional `configured_compression_strategy`

## Intended Architectural Reading

This example should teach one specific lesson:

- Atlas can operate as a real pipeline component over mixed source families
- the engine path stays shared with the rest of the product
- the starter estimator is shape-aware by default rather than one flat global
  chars-per-token assumption
- database access remains an outer application concern
- payload-file loading remains an outer workflow concern too
- packet and trace remain the authoritative outputs
