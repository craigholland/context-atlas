---
id: release-0-1-0
title: Release 0.1.0
summary: Records the first MVP release of Context Atlas, including its shipped capabilities, known gaps, and immediate future-state direction.
doc_class: releases
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [releases, mvp, version-0-1-0, product-surface]
related:
  - ../Reviews/MVP/mvp_readiness_assessment.md
  - ../Reviews/MVP/mvp_evaluation_rubric.md
  - ../Guides/README.md
  - ../../README.md
supersedes: []
---

# Release 0.1.0

## Context

This document records the first MVP release of Context Atlas.

`0.1.0` is the first shipped version that the repository describes as `MVP Ready`.
It establishes Context Atlas as a reusable context-governance component with:

- canonical source modeling
- auditable packet and trace artifacts
- governed document and structured-record ingestion
- three supported workflow surfaces
- reproducible MVP proof artifacts

This document is meant to capture what `0.1.0` actually shipped, where its
current boundaries still are, and what the near-term hardening direction should
look like after the first MVP release.

## Shipped Capabilities

### Core Engine

`0.1.0` ships a real shared engine for:

- canonical `ContextSource`, `ContextPacket`, and `ContextTrace` artifacts
- lexical retrieval over a shared source registry
- candidate ranking and deduplication
- budgeting and compression
- memory retention
- structured packet assembly with explicit trace metadata

The engine is no longer only an architecture skeleton. It now includes the
starter implementation needed to assemble and inspect real packets end to end.

### Source Families

`0.1.0` supports two source families through one canonical source model:

- governed filesystem documents
- structured records supplied as already-fetched payloads

Filesystem document ingestion is ontology-aware for the project's document
classes, and structured records now have a validated adapter surface rather than
living only as planning intent.

### Workflow Surfaces

`0.1.0` ships four supported user-facing workflow surfaces:

- starter workflow
- Codex repository workflow
- documents-plus-database workflow
- low-code workflow

Those workflows are intentionally different outer experiences over the same
shared engine path rather than four separate orchestration systems.

### Inspection And Proof

`0.1.0` ships packet and trace inspection as first-class derived surfaces and
includes a reproducible MVP proof harness with tracked review artifacts.

That means the release is not only feature-shaped; it is also evidence-shaped.
The current release includes:

- packet inspection rendering
- trace inspection rendering
- proof-capture tooling
- MVP evaluation rubric
- MVP readiness assessment

### Package Surface

`0.1.0` also establishes the first credible package-facing product surface:

- `context_atlas.api` as the curated starter namespace
- `context_atlas.rendering` for derived inspection views
- `context-atlas-starter` as the installable starter CLI
- aligned product-facing guidance under `docs/Guides/`

That package and documentation surface now tells a more coherent story than the
earlier repo-local example-first shape.

## Known Gaps

The `0.1.0` release is `MVP Ready`, but it is still intentionally narrow in
several important ways.

- The repository workflow is still governed-docs-first. It does not yet provide
  full source-code crawling, git-history awareness, or issue-system ingestion.
- The documents-plus-database workflow still assumes already-fetched records.
  Atlas governs and translates them, but does not yet own database, vector
  store, or API client integration.
- The low-code workflow is still a thin preset-driven wrapper over the shared
  engine, not a broader no-code platform.
- The env-backed configuration surface is intentionally narrower than the full
  set of internal runtime constants.
- Release and packaging discipline are now stronger than before, but publication
  and post-release automation are still relatively light.
- The current MVP proof set is solid, but still centered on tracked local
  workflows rather than broader external-service or production-style evaluation.

## Future State

The immediate post-`0.1.0` direction should build on the shipped engine rather
than replacing it.

Near-term hardening and expansion should focus on:

- broader repository-aware inputs while preserving the shared packet path
- richer external-data integrations that keep fetching outside Atlas and
  translation/governance inside Atlas
- a stronger low-code product surface without forking the engine into a second
  orchestration model
- continued improvement of release/versioning discipline and publication
  repeatability
- additional proof scenarios and broader evaluation coverage

Longer term, the runtime floor can rise again when future capabilities actually
need it. For example, if Atlas later leans on newer Python concurrency
capabilities in a real architectural way, that version requirement should be
raised explicitly as part of that work rather than preemptively.

## Related Artifacts

- [MVP Readiness Assessment](../Reviews/MVP/mvp_readiness_assessment.md)
- [MVP Evaluation Rubric](../Reviews/MVP/mvp_evaluation_rubric.md)
- [Guides Index](../Guides/README.md)
- [Repository README](../../README.md)
