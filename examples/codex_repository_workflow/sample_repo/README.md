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
      Canon/
        Architecture/
          Repo-Guidance.md
    Planning/
      Current-Work.md
    Reviews/
      Review-Notes.md
```

## Example Content Shape

The current workflow is most useful when the governed docs include:

- at least one authoritative architecture or identity artifact
- at least one planning or task-oriented artifact
- optionally one review or exploratory artifact that overlaps the same topic but should not outrank the authoritative document
- plain markdown content with normal headings and prose
- tracked markdown files under `sample_repo/docs/` so the example can be run directly for proof work

For the Story 7 authority-hardening pass, the sample shape should make the
document-side authority contrast explicit:

- `Authoritative/Canon/Architecture/Repo-Guidance.md`
  - should describe the binding or preferred repository guidance that should win
    when the same question is answered from multiple document classes
- `Planning/Current-Work.md`
  - should mention current implementation plans or work-in-progress notes that
    may overlap the authoritative topic but should not override it
- `Reviews/Review-Notes.md`
  - may mention findings or follow-up concerns about the same topic so the
    packet and trace can show lower-authority material remaining visible without
    displacing the authoritative guidance

The goal is not to rely on folder names alone. The proof should make it easy
for a reviewer to see the canonical source-class and authority meaning survive
translation into packet and trace output.

This sample repo now includes that tracked authority contrast under:

- `sample_repo/docs/Authoritative/Canon/Architecture/Repo-Guidance.md`
- `sample_repo/docs/Planning/Current-Work.md`
- `sample_repo/docs/Reviews/Review-Notes.md`

## Example Command

```bash
python examples/codex_repository_workflow/run.py --repo-root /repos/my-repo
```

If the docs live somewhere other than `<repo_root>/docs`, pass `--docs-root`.
Relative `--docs-root` values are resolved from `--repo-root`.

For the authority-hardening proof scenario, the supported repository workflow
should point at an authority-rich docs tree, typically the full `docs/` root,
instead of only one advisory subfolder.

You can run that authority-proof scenario directly with:

```bash
python examples/codex_repository_workflow/run.py \
  --repo-root examples/codex_repository_workflow/sample_repo \
  --query "When authoritative architecture guidance and planning docs both discuss repository process, which guidance should an engineer follow and how should planning docs be updated?"
```

## Why This Exists

This artifact is not a second workflow. It is a concrete layout reference so the
guide, CLI help, and runnable example all describe the same minimal repository
shape before broader repository inputs arrive later.

