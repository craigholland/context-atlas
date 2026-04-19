---
id: context-atlas-mvp-proof-evidence-bundles
title: MVP Proof Evidence Bundles
summary: Documents the reviewable directory layout and generation commands for MVP proof evidence bundles.
doc_class: guide
template_refs:
  metadata: base_metadata@1.0.0
  content: guide_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, proof, evidence, bundles, review]
related:
  - ../README.md
  - ../inputs/README.md
  - ../../../docs/Reviews/MVP/mvp_readiness_assessment.md
supersedes: []
---

# MVP Proof Evidence Bundles

This folder documents the preferred reviewable bundle shape for the current MVP
proof pass.

The evidence bundle is generated, not tracked. The recommended output root is
still a temporary working directory such as `tmp/mvp_proof/evidence`, but every
bundle should follow the same directory layout:

```text
<bundle-root>/
  <workflow>/
    <scenario>/
      atlas_packet.json
      atlas_rendered_context.txt
      atlas_trace.json
      baseline_rendered_context.txt
      evidence_package.json
```

That layout keeps two review surfaces together:

- the canonical copied artifacts that a reviewer may want to open directly
- the packaged JSON record that embeds the standard review order and rubric
  dimensions

## Generate One Bundle

After running one workflow and preparing one naive baseline rendered-context
artifact:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_governed_docs_update `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --input-summary "repo_root=.; docs_root=docs/Guides" `
  --baseline-rendered tmp\mvp_proof\baselines\codex_repository.txt `
  --atlas-artifact-dir tmp\mvp_proof\codex_repository `
  --bundle-root tmp\mvp_proof\evidence
```

That command writes the reviewable bundle at:

```text
tmp/mvp_proof/evidence/codex_repository/repo_governed_docs_update/
```

## Current Proof Set

Use the same bundle-root pattern for the current selected workflows:

- `codex_repository` / `repo_governed_docs_update`
- `docs_database_builder` / `builder_support_troubleshooting`
- `low_code_chatbot` / `low_code_validation`

Story 7 also adds one constrained hardening target:

- `codex_repository` / `repo_budget_pressure_tradeoffs`

That bundle should be packaged with `--expect-budget-pressure` so capture fails
unless the packet and trace artifacts show visible pressure metadata or
budget-pressure decisions.

Story 7 also adds one document-authority hardening target:

- `codex_repository` / `repo_document_authority_precedence`

That bundle should be packaged with `--expect-document-authority-contrast` so
capture fails unless the packet shows an authoritative document selected ahead
of lower-authority repository documents in the same scenario.

The canonical workflow commands and scenario inputs for generating the Atlas
artifact directories still live in
[examples/mvp_proof/inputs/README.md](/context-atlas/examples/mvp_proof/inputs/README.md).

The canonical human-readable assessment record that should reference these
bundles lives in
[docs/Reviews/MVP/mvp_readiness_assessment.md](/context-atlas/docs/Reviews/MVP/mvp_readiness_assessment.md).

## Current Assessment Run

The current Story 6 Task 6.3 assessment used the default temporary bundle root:

```text
tmp/mvp_proof/evidence
```

and reviewed these bundle paths:

- `tmp/mvp_proof/evidence/codex_repository/repo_governed_docs_update/`
- `tmp/mvp_proof/evidence/docs_database_builder/builder_support_troubleshooting/`
- `tmp/mvp_proof/evidence/low_code_chatbot/low_code_validation/`

Those bundle directories are generated, not tracked. Recreate them with the
commands in [../inputs/README.md](/context-atlas/examples/mvp_proof/inputs/README.md)
plus the `--bundle-root tmp/mvp_proof/evidence` capture step shown above.

## Story 7 Budget-Pressure Hardening Bundle

The first hardening bundle that should be added next is:

```text
tmp/mvp_proof/evidence/codex_repository/repo_budget_pressure_tradeoffs/
```

Package it with the constrained repository command from
[../inputs/README.md](/context-atlas/examples/mvp_proof/inputs/README.md) and:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_budget_pressure_tradeoffs `
  --query "What guidance should an engineer follow when updating repository planning docs or architecture guidance?" `
  --input-summary "repo_root=.; docs_root=docs/Guides; total_budget=64" `
  --baseline-rendered tmp\mvp_proof\baselines\codex_repository_budget_pressure.txt `
  --atlas-artifact-dir tmp\mvp_proof\codex_repository_budget_pressure `
  --expect-budget-pressure `
  --bundle-root tmp\mvp_proof\evidence
```

That keeps the hardening bundle on the same reviewable layout as the original
Story 6 proof set while making the constrained-budget expectation explicit.

## Story 7 Document-Authority Hardening Bundle

The first authority hardening bundle that should be added next is:

```text
tmp/mvp_proof/evidence/codex_repository/repo_document_authority_precedence/
```

Package it with the authority-rich repository command from
[../inputs/README.md](/context-atlas/examples/mvp_proof/inputs/README.md) and:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_document_authority_precedence `
  --query "When authoritative architecture guidance and planning docs both discuss repository process, which guidance should an engineer follow and how should planning docs be updated?" `
  --input-summary "repo_root=examples/codex_repository_workflow/sample_repo; docs_root=examples/codex_repository_workflow/sample_repo/docs" `
  --baseline-rendered tmp\mvp_proof\baselines\codex_repository_authority.txt `
  --atlas-artifact-dir tmp\mvp_proof\codex_repository_authority `
  --expect-document-authority-contrast `
  --bundle-root tmp\mvp_proof\evidence
```

That keeps the authority hardening bundle on the same reviewable layout as the
original proof set while making the expected document-authority contrast
explicit.
