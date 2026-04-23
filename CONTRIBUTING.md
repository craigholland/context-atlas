# Contributing

This repository uses a governed documentation ontology. If you want to add or
update a document, do not start by copying a random Markdown file and editing
it freehand.

Use this path instead.

## Start Here

1. Read [docs/README.md](./docs/README.md).
2. Read [docs/Authoritative/Canon/Ontology/README.md](./docs/Authoritative/Canon/Ontology/README.md).
3. Read [docs/Authoritative/Canon/Ontology/Documentation-Ontology.md](./docs/Authoritative/Canon/Ontology/Documentation-Ontology.md).

Those three documents tell you:

- what kinds of documents exist
- what each document class means
- which template surfaces to use
- where portable canon ends and Context Atlas-specific identity begins

## How To Add A Document

1. Decide the document class before you write.

Use the ontology, not gut feel:

- `Authoritative`: binding truth, safe-to-act-on guidance, canon, or project-specific identity
- `Planning`: intended future work, decomposition, sequencing, and PR-plan slices
- `Reviews`: findings, evidence, assessments, or readiness decisions
- `Exploratory`: speculative investigation, prototypes, or thought work that is not binding
- `Releases`: shipped version summaries and release-history artifacts

2. Put the file in the right part of the tree.

Examples:

- portable cross-project canon:
  - `docs/Authoritative/Canon/...`
- Context Atlas-specific binding:
  - `docs/Authoritative/Identity/...`
- forward-looking execution intent:
  - `docs/Planning/...`
- assessments and evidence:
  - `docs/Reviews/...`
- shipped release notes:
  - `docs/Release/...`

3. Start with the correct templates.

All downstream documents should begin with the shared metadata block from
[base_metadata.md](./docs/Authoritative/Canon/Ontology/base_metadata.md).

Then choose the class-appropriate content template:

- authoritative docs:
  - [authoritative_content.md](./docs/Authoritative/Canon/Ontology/authoritative_content.md)
- planning docs:
  - [planning_content.md](./docs/Authoritative/Canon/Ontology/planning_content.md)
- reviews, exploratory, and releases docs:
  - [general_content.md](./docs/Authoritative/Canon/Ontology/general_content.md)

4. Fill in the metadata honestly.

At minimum, review these fields carefully:

- `id`
- `title`
- `summary`
- `doc_class`
- `template_refs`
- `status`
- `created`
- `last_reviewed`
- `owners`
- `tags`
- `related`
- `supersedes`

The front matter is governed content, not decorative boilerplate.

5. Update the nearest index and neighboring docs if discoverability changed.

Examples:

- if you add a new guide, update the relevant guide index
- if you add a new canon file, update the canon README that indexes that set
- if you add a new release note, update `docs/Release/README.md`

6. Update the nearest `__ai__.md` files when the governed surface changed meaningfully.

Owner files should reflect new rules, files, or contributor expectations rather
than lagging behind the repo state.

7. Keep command examples cross-platform when shell syntax differs.

If you show PowerShell-specific launcher or environment syntax, add a nearby
Bash/Linux/macOS analog so the docs do not force contributors into Windows-only
workflows.

For repo-owned Python scripts such as `scripts/preflight.py`,
`scripts/materialize_codex_runtime.py`, or
`scripts/check_codex_materialization.py`, prefer `python ...` as the primary
documented command shape. Windows launcher variants such as `py -3` may still
be shown as local analogs when they add operator value, but they should not be
the repo's first-class truth-path examples.

## Common Pitfalls

- Do not put Context Atlas-specific choices into `docs/Authoritative/Canon/`.
- Do not put future intent into `Authoritative` docs when it belongs in `Planning`.
- Do not treat `Planning` as if it overrides `Authoritative`.
- Do not leave stale metadata after changing a document's meaning.
- Do not create a new document class ad hoc when an existing class already fits.
- Do not publish Windows-only command guidance without a Linux/macOS analog when shell syntax differs.
- Do not present `py -3` as the primary repo-wide command shape for repo-owned
  Python scripts when a portable `python ...` example would work.

## If You Are Unsure

When in doubt:

1. start from the ontology docs
2. choose the most truthful existing class
3. keep canon portable and bindings local
4. prefer updating a nearby index or metadata field rather than leaving a new document orphaned
