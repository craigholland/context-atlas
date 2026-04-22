# Guides

This directory is the primary user-facing help surface for Context Atlas.

If you are evaluating, installing, or wiring Context Atlas into a workflow,
start here before dropping into `examples/` or deeper architecture docs.

If you want the repo-level map first, start with the root
[README](../../README.md).

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
