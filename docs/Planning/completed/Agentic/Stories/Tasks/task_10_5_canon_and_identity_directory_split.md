---
id: context-atlas-agentic-task-10-5-canon-and-identity-directory-split
title: Task 10.5 - Canon And Identity Directory Split PR Plan
summary: Defines the follow-up PR sequence for separating reusable top-tier canon under docs/Authoritative/Canon from the project-specific Identity layer.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, canon, identity, refactor]
related:
  - ../story_10_validation_governance_and_drift_control.md
  - ../../agentic_development_product_definition.md
  - ../../../../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md
supersedes: []
---

# Task 10.5 - Canon And Identity Directory Split PR Plan

## Objective

Refactor the top-tier authoritative layout so reusable canon lives under
`docs/Authoritative/Canon/` and the project-specific binding layer remains under
`docs/Authoritative/Identity/`.

## Task Status

IMPLEMENTED

## Inputs

- [Story 10 - Validation, Governance, And Drift Control](../story_10_validation_governance_and_drift_control.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture - Planning And Decomposition](../../../../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- the already-established distinction between portable canon and project-specific identity bindings

## Proposed Work

### PR - A: Introduce Canon Directory

- create `docs/Authoritative/Canon/`
- move the reusable `Architecture`, `AgenticDevelopment`, `RepoManagement`, and
  `Ontology` directories beneath it
- keep `Identity/` as the sibling project-binding layer

#### Expected New Files
- `docs/Authoritative/Canon/README.md`

#### Expected Existing Files Updated
- `docs/README.md`
- `__ai__.md`

#### Update AI files
- `.`

### PR - B: Repair Cross-Links And Owner Contracts

- update path references, relative links, and owner-file folder contracts to the
  new `Canon/` layout
- keep canon/identity cross-links explicit so the new split is discoverable to
  contributors and validation tooling

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Authoritative/Canon/Architecture/README.md`
- `docs/Authoritative/Canon/AgenticDevelopment/__ai__.md`
- `docs/Authoritative/Canon/RepoManagement/__ai__.md`
- `docs/Planning/**/*.md`

#### Update AI files
- `.`

### PR - C: Align Runnable Fixtures And Validation

- update sample repositories, tests, and validation-related config to reflect
  the new authoritative path shape
- keep the refactor structural rather than changing runtime semantics

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `examples/codex_repository_workflow/sample_repo/**`
- `tests/test_codex_repository_workflow.py`
- `tests/test_filesystem_document_adapter.py`
- `pyproject.toml`

#### Update AI files
- `.`

## Sequencing

- move the canon directories first
- repair links and owner-file contracts second
- align runnable fixtures and validation third

## Risks And Unknowns

- A structural move can leave behind stale path references that only show up in
  tests or examples if the cleanup pass is incomplete.
- Owner-file verification commands may silently drift if governed roots are not
  updated along with the folder move.
- The sample repository and workflow tests may continue encoding the old layout
  unless runnable fixtures are updated together with the prose docs.

## Exit Criteria

- reusable top-tier canon lives under `docs/Authoritative/Canon/`
- `docs/Authoritative/Identity/` remains the sibling project-binding layer
- authoritative indexes, owner files, planning docs, examples, and tests all
  reflect the new split
- The repository preflight command passes after the refactor

## Related Artifacts

- [Story 10 - Validation, Governance, And Drift Control](../story_10_validation_governance_and_drift_control.md)
- [Craig Architecture - Planning And Decomposition](../../../../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
