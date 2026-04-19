---
id: context-atlas-mvp-proof-inputs
title: MVP Proof Inputs
summary: Documents the reproducible workflow commands and scenario names used for the current MVP proof pass.
doc_class: guide
template_refs:
  metadata: base_metadata@1.0.0
  content: guide_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, proof, workflows, examples, inputs]
related:
  - ../README.md
  - ../../../docs/Reviews/MVP/mvp_evaluation_rubric.md
  - ../../../README.md
supersedes: []
---

# MVP Proof Inputs

This folder records the reproducible Atlas-side workflow commands for the
current MVP proof pass.

The selected workflows and scenarios are:

- `codex_repository`: `repo_governed_docs_update`
- `docs_database_builder`: `builder_support_troubleshooting`
- `low_code_chatbot`: `low_code_validation`

The first Story 7 budget-pressure hardening target is:

- `codex_repository`: `repo_budget_pressure_tradeoffs`

That hardening scenario is intentionally centered on the flagship repository
workflow so the budget evidence is easy to compare against the current default
proof pass. The scenario keeps the same governed-doc workflow shape while
reducing the available budget enough that packet and trace review show concrete
compression tradeoffs and an explicitly reduced document-slot allocation.

Each supported workflow runner can now emit the same Atlas artifact filenames
when `--proof-artifacts-dir` is supplied:

- `atlas_rendered_context.txt`
- `atlas_packet.json`
- `atlas_trace.json`

These commands generate only the Atlas-side artifacts. A naive baseline
rendered-context artifact should still be prepared separately for the same
scenario before packaging evidence with
[`scripts/mvp_proof/capture_evidence.py`](/context-atlas/scripts/mvp_proof/capture_evidence.py).

## Repository Workflow

Scenario: `repo_governed_docs_update`

```powershell
python examples/codex_repository_workflow/run.py `
  --repo-root . `
  --docs-root docs/Guides `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --proof-artifacts-dir tmp\mvp_proof\codex_repository
```

For the current proof pass, the repository workflow intentionally points at
`docs/Guides` instead of the full repository `docs/` tree so the scenario stays
within the currently supported governed-doc classes of the flagship workflow.

## Docs Plus Database Workflow

Scenario: `builder_support_troubleshooting`

```powershell
python examples/docs_database_workflow/run.py `
  --query "How should a builder configure Context Atlas and troubleshoot preflight or environment-loading issues in a chatbot pipeline?" `
  --proof-artifacts-dir tmp\mvp_proof\docs_database_builder
```

The default command intentionally uses the tracked sample records payload from
`examples/docs_database_workflow/sample_records.json` so later proof runs do not
depend on unpublished setup.

## Low-Code Workflow

Scenario: `low_code_validation`

```powershell
python examples/low_code_workflow/run.py `
  --repo-root . `
  --query "How should a low-code builder configure Context Atlas and troubleshoot environment or preflight issues in a chatbot workflow?" `
  --proof-artifacts-dir tmp\mvp_proof\low_code_chatbot
```

The current low-code proof path intentionally stays on the tracked default
preset and tracked sample record payload so the workflow remains reproducible.

## Package One Proof Scenario

After a workflow run has produced the standard Atlas artifacts, package that run
with one naive baseline rendered-context artifact:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_governed_docs_update `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --input-summary "repo_root=.; docs_root=docs/Guides" `
  --baseline-rendered tmp\mvp_proof\baselines\codex_repository.txt `
  --atlas-artifact-dir tmp\mvp_proof\codex_repository `
  --output tmp\mvp_proof\evidence\repo_governed_docs_update.json
```

Use the same pattern for the other selected workflows by changing:

- `--workflow`
- `--scenario`
- `--query`
- `--input-summary`
- the baseline rendered artifact path
- the Atlas artifact directory

## Story 7 Hardening Target

The constrained repository scenario for Story 7 should use this supported run:

- workflow id: `codex_repository`
- scenario id: `repo_budget_pressure_tradeoffs`
- purpose: show that Atlas makes visible, governed tradeoffs when the starter
  budget is intentionally constrained
- expected review outcome:
  - packet inspection should show the lower budget explicitly
  - trace inspection should show compression, exclusion, or budget-pressure
    reasoning that is easy to point at explicitly
  - the evidence package should make the sacrificed or transformed context
    visible enough to compare against the naive baseline

```powershell
python examples/codex_repository_workflow/run.py `
  --repo-root . `
  --docs-root docs/Guides `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --total-budget 64 `
  --proof-artifacts-dir tmp\mvp_proof\codex_repository_budget_pressure
```

Package that constrained run with:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_budget_pressure_tradeoffs `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --input-summary "repo_root=.; docs_root=docs/Guides; total_budget=64" `
  --baseline-rendered tmp\mvp_proof\baselines\codex_repository_budget_pressure.txt `
  --atlas-artifact-dir tmp\mvp_proof\codex_repository_budget_pressure `
  --expect-budget-pressure `
  --output tmp\mvp_proof\evidence\repo_budget_pressure_tradeoffs.json
```
