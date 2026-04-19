# Documents Plus Database Workflow Example

This example demonstrates the current technical-builder workflow for Context Atlas.

Current supported shape:

- point Atlas at a governed docs directory
- fetch rows or payloads outside Atlas using your own database, vector-store, or API client
- shape those already-fetched rows into validated Atlas record inputs
- translate both source families into one canonical `ContextSource` model
- assemble one packet and one trace through the shared engine

The runnable demo stays honest about the boundary:

- filesystem documents come from this repository's `docs/Guides/` tree by default
- support-style records are represented as already-fetched in-memory rows inside the script
- Atlas shapes and translates those rows, but it does not execute the database query

## Run

After an editable install:

```powershell
python examples/docs_database_workflow/run.py
```

Override the docs root or chatbot question:

```powershell
python examples/docs_database_workflow/run.py --docs-root C:\repos\my-app\docs --query "How should I configure Atlas and troubleshoot preflight failures?"
```

The output shows:

- the rendered chatbot-facing context block
- packet inspection
- trace highlights
- full trace inspection

## Intended Architectural Reading

This example should teach one specific lesson:

- Atlas can operate as a real pipeline component over mixed source families
- the engine path stays shared with the rest of the product
- database access remains an outer application concern
- packet and trace remain the authoritative outputs
