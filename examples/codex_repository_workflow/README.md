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

Read those packet and trace surfaces using the hardened top-level vocabulary:

- packet: `fixed_reserved_tokens`, `unreserved_tokens`, `unallocated_tokens`
- trace: `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`,
  `budget_unallocated_tokens`
- either view: `compression_strategy`
- optional `configured_compression_strategy`

That makes the workflow suitable both for local experimentation and for internal MVP review.

The shared hardening story is the same one described in the guides:

- the repository workflow still runs through the shared starter engine
- the starter estimator is shape-aware by default
- retrieval reuse and duplicate-acceptance proof remain regression-backed
  rather than moving into a second demonstration-only artifact family

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
