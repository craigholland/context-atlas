# Codex Repository Workflow Example

This example demonstrates the current flagship repository workflow for Context Atlas.

For product-facing setup guidance, start with
[docs/Guides/codex_repository_workflow.md](/context-atlas/docs/Guides/codex_repository_workflow.md).
This README is the runnable companion artifact for that guide.

Current supported shape:

- start from a repository root
- use the governed docs rooted at `<repo_root>/docs`
- assemble a packet for an engineering question
- render a Codex-facing context block
- inspect the packet and trace so the workflow stays explainable

The example is intentionally honest about scope:

- it uses governed repository docs only
- it uses the shared starter assembly service
- it does not crawl arbitrary source files
- it does not integrate with git history, issue trackers, or external connectors

## Run

After an editable install:

```bash
python examples/codex_repository_workflow/run.py --repo-root .
```

Override the engineering question:

```bash
python examples/codex_repository_workflow/run.py --repo-root . --query "What should planning docs be treated as during implementation?"
```

When `--docs-root` is relative, it is resolved from the selected `--repo-root`:

```bash
python examples/codex_repository_workflow/run.py --repo-root /repos/my-repo --docs-root docs
```

The output shows:

- the rendered Codex-facing context block
- packet inspection
- trace inspection

That makes the workflow suitable both for local experimentation and for internal MVP review.

## Demo-Focused Trace View

For a more demonstration-oriented output that keeps rendered context plus trace
visibility front and center:

```bash
python examples/codex_repository_workflow/show_trace.py --repo-root .
```

That script keeps the same shared engine path, but presents the output as:

- rendered Codex context
- concise trace highlights
- full trace inspection
