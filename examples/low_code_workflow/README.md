# Low-Code Workflow Example

This example demonstrates the current low-code workflow for Context Atlas.

Current supported shape:

- one supported preset: `chatbot_docs_records`
- governed guide docs plus an already-fetched record payload file
- one shared packet and trace path through the same starter engine used by the
  other MVP workflows

The example is intentionally honest about scope:

- it uses one preset-driven wrapper over the shared engine
- it does not introduce a second packet path
- it does not open database connections or vector-store clients
- it does not claim a mature no-code product surface

## Run

After an editable install:

```powershell
python examples/low_code_workflow/run.py
```

Override the query:

```powershell
python examples/low_code_workflow/run.py --query "How should a low-code builder validate Atlas output?"
```

Resolve relative overrides from a chosen repo root:

```powershell
python examples/low_code_workflow/run.py --repo-root C:\repos\my-app --docs-root docs\Guides --records-file data\support_rows.json
```

Inspect one source family in isolation:

```powershell
python examples/low_code_workflow/run.py --no-documents
python examples/low_code_workflow/run.py --no-records
```

The output shows:

- the rendered chatbot-facing context block
- packet inspection
- trace highlights
- trace inspection

Tracked reference artifacts for this path also live here:

- [config.example.toml](./config.example.toml)
- [presets/basic.toml](./presets/basic.toml)

Those files are reference surfaces for the current MVP story. They are not
auto-loaded by Atlas today.

That makes the workflow suitable both for product-facing MVP evaluation and for
internal review of how the preset wrapper still delegates to the shared engine.
