# Sample Repository Layout

This document shows the smallest repository shape the current Codex repository
workflow is designed to understand.

The workflow expects:

- a repository root
- governed docs under `<repo_root>/docs`
- an engineering question or task query

## Minimal Shape

```text
sample_repo/
  docs/
    Authoritative/
      Architecture/
        Repo-Guidance.md
    Planning/
      Current-Work.md
```

## Example Content Shape

The current workflow is most useful when the governed docs include:

- at least one authoritative architecture or identity artifact
- at least one planning or task-oriented artifact
- plain markdown content with normal headings and prose

## Example Command

```powershell
python examples/codex_repository_workflow/run.py --repo-root C:\repos\my-repo
```

If the docs live somewhere other than `<repo_root>/docs`, pass `--docs-root`.
Relative `--docs-root` values are resolved from `--repo-root`.

## Why This Exists

This artifact is not a second workflow. It is a concrete layout reference so the
guide, CLI help, and runnable example all describe the same minimal repository
shape before broader repository inputs arrive later.
