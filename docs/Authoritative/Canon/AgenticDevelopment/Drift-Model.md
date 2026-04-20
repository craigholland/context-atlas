---
id: craig-agentic-drift-model
title: Drift Model
summary: Defines the portable drift categories that matter across canon, bindings, planning inputs, and runtime materializations.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, drift, validation, governance]
related:
  - ./Materialization-Traceability-Model.md
  - ./Validation-Model.md
  - ./Change-Management-Model.md
  - ../RepoManagement/README.md
supersedes: []
---

# Drift Model

## Purpose

Define the portable drift vocabulary that later validation, review, and
recovery work should use when checking whether agentic-development and
neighboring repo-management surfaces still align.

## Scope

This model governs meaningful drift across:

- portable canon
- project-specific bindings
- machine-readable planning inputs
- runtime-facing materializations
- neighboring repo-management bindings when those bindings are part of the same
  governed execution system

It does not define one platform-specific validator or one review workflow.

## Drift Categories

### 1. Semantic Drift

Semantic drift occurs when a downstream artifact changes meaning relative to
the upstream canon or binding it claims to express.

Examples include:

- a runtime asset that redefines a role, mode, protocol, or skill
- a project binding that contradicts the portable canon
- a repo-management binding that assigns authority inconsistent with the role
  or gate model it cites

### 2. Structural Drift

Structural drift occurs when a governed artifact no longer satisfies the shape
or required sections that its upstream model expects.

Examples include:

- a protocol doc missing required protocol-template sections
- a machine-readable planning input missing required keys
- a materialized asset no longer living at a bound path or no longer matching
  a required discovery class

### 3. Traceability Drift

Traceability drift occurs when a downstream artifact can no longer be reviewed
against the upstream sources that authorize it.

Examples include:

- missing or stale source references
- missing maintenance-mode declarations
- contradictory provenance declarations across related surfaces

### 4. Discovery Drift

Discovery drift occurs when a runtime-facing asset no longer satisfies the
discovery mechanics that its binding claims to implement.

Examples include:

- a required manifest, index, or folder path going missing
- a skill, mode, or agent asset moving to a path that is no longer bound by the
  active environment layout
- a runtime folder convention diverging from the discovery model it cites

### 5. Planning-Input Drift

Planning-input drift occurs when a governed machine-readable planning artifact
is malformed, stale, or used outside the trust model that authorizes it.

Examples include:

- runtime-capacity values that are internally inconsistent
- decomposition logic treating planning capacity as live scheduler state
- parallel-planning claims that exceed the governed planning artifact

### 6. Governance Drift

Governance drift occurs when owner files, metadata, or review expectations no
longer match the surface they are supposed to govern.

Examples include:

- local `__ai__.md` files that no longer describe the docs in scope
- front matter that no longer reflects current discoverability or boundaries
- validation docs that point at obsolete authoritative sources

## Machine-Checked Versus Review-Surfaced Drift

### Drift That Should Often Be Machine-Checked

These categories often support structural validation:

- missing required files
- malformed machine-readable artifacts
- missing required protocol sections
- missing traceability declarations
- bound paths or names that no longer match the active binding

### Drift That Often Requires Human Review

These categories often require interpretation:

- whether a downstream paraphrase changed meaning
- whether a specialization claim still reflects reality
- whether a role or policy refinement remains faithful to the upstream canon
- whether a repo-management authority decision is still appropriate

The drift model should support both machine checks and human review without
collapsing them into one claim of certainty.

## Drift Severity Guidance

Not every mismatch is equally important.

Reviewers and later validators should prioritize:

- semantic contradictions over wording differences
- missing authority or traceability declarations over cosmetic layout changes
- bound discovery/path mismatches over harmless prose reordering
- machine-readable artifact incoherence over incidental formatting variance

## Constraints

- Drift categories must remain portable.
- The model must stay broad enough to cover multiple runtime environments and
  repository providers.
- Cosmetic text changes should not automatically be treated as meaningful drift.
- Drift vocabulary should remain stable enough that later validation docs do
  not invent a parallel taxonomy.

## Non-Goals

- Define a provider-specific enforcement script.
- Replace QA review or human architectural judgment.
- Treat live operational availability as equivalent to structural planning
  validation.

## Related Artifacts

- [Materialization Traceability Model](./Materialization-Traceability-Model.md)
- [Validation Model](./Validation-Model.md)
- [Change-Management Model](./Change-Management-Model.md)
- [Repo Management](../RepoManagement/README.md)
