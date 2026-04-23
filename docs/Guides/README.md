# Guides

This directory is the primary user-facing help surface for Context Atlas.

Use the entry surfaces intentionally:

- the root [README](../../README.md) is the repo-wide map
- [docs/README.md](../README.md) is the documentation route splitter
- this file is the product guide hub

If you are evaluating, installing, or wiring Context Atlas into a workflow,
start here before dropping into `examples/` or deeper architecture docs.

You do not need the generated Codex runtime assets under `.codex/` or
`.agents/skills/`, and you do not need to learn the repo's `__ai__.md`
governance model, to follow the product route in this directory.

If you are here for contributor governance, generated runtime inspection, or
Canon/Identity binding work, return to the root [README](../../README.md) or
[docs/README.md](../README.md). This directory is intentionally the product
route, not the repo-governance or runtime-materialization index.

## Start Here

- [Getting Started](./getting_started.md)
  - first-run installation, starter configuration, and the installable starter CLI
- [Context Atlas Tour](./context_atlas_tour.md)
  - system-level walkthrough of current source families, workflow shapes,
    boundaries, packet/trace inspection, and proof surfaces

## Workflow Guides

- [Codex Repository Workflow](./codex_repository_workflow.md)
  - repo-aware workflow over governed repository docs
- [Documents Plus Database Workflow](./docs_database_workflow.md)
  - technical-builder mixed-source workflow over docs plus already-fetched records
- [Low-Code Workflow](./low_code_workflow.md)
  - preset-driven wrapper over the shared starter engine

## Relationship To `examples/`

The `examples/` directory now holds runnable companion artifacts:

- Python scripts
- sample payloads
- proof inputs and evidence packaging helpers

Use Guides as the authoritative setup and workflow-help surface. Use
`examples/` when you want the runnable companion artifact for a guide.
