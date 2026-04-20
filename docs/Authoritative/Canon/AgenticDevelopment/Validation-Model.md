---
id: craig-agentic-validation-model
title: Validation Model
summary: Defines how governed validation should reason about the agentic-development and repo-management surfaces without confusing structural checks with workflow-state review.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, validation, preflight, governance]
related:
  - ./Drift-Model.md
  - ./Change-Management-Model.md
  - ./Protocols/Protocol-Template.md
  - ../RepoManagement/README.md
supersedes: []
---

# Validation Model

## Purpose

Define how governed validation should reason about the agentic-development and
repo-management surfaces over time.

## Scope

This model governs structural validation expectations for:

- portable canon docs
- project-specific bindings
- machine-readable planning inputs
- runtime-facing materialization surfaces
- repo-management provider and project-binding surfaces
- local owner files and metadata when they are part of the same governed stack

It does not replace workflow-state review, QA judgment, or live operational
monitoring.

## Validation Layers

### 1. Canon Integrity Validation

Validation should be able to check whether the portable canon remains
internally coherent.

Typical checks include:

- required canon entrypoints are present and linked
- key supplements still exist where the canon README says they do
- downstream docs do not quietly become the only place a canon concept exists

### 2. Binding Integrity Validation

Validation should be able to check whether project-specific bindings still
declare the required bounded relationships to the canon they refine.

Typical checks include:

- required binding docs are present
- role, mode, protocol, and repo-management binding surfaces still exist
- required gate or scope fields remain present where the protocol model says
  they belong

### 3. Planning-Input Validation

Validation should be able to check whether governed machine-readable planning
inputs remain structurally trustworthy.

Typical checks include:

- YAML or JSON parses successfully
- required keys are present
- numeric or bounded fields remain internally coherent
- the file stays within the structural trust model defined by its guidance doc

Validation should not claim to prove live availability, queue state, or actual
runtime allocation.

### 4. Materialization Validation

Validation should be able to check whether runtime-facing assets still satisfy
the bound discovery, naming, traceability, and maintenance-mode rules that
authorize them.

Typical checks include:

- assets still live at bound paths
- required manifests, indexes, or companion files still exist
- cited authoritative sources and maintenance-mode declarations are still
  present
- copied, adapted, and derived assets still follow the bound creation guidance

### 5. Governance Validation

Validation should be able to check whether owner files and metadata remain
structurally present and aligned enough to support review.

Typical checks include:

- required `__ai__.md` files exist where the governance model expects them
- front matter parses cleanly
- key metadata fields remain present and non-empty
- planning and authoritative indexes still surface the relevant canon

## Structural Validation Versus Workflow Review

Structural validation answers questions like:

- is the required surface present?
- is the file shape coherent?
- does the binding still expose the required fields?
- does the runtime asset still declare its authoritative source?

Workflow review answers questions like:

- is this implementation ready for the next gate?
- are the findings acceptable?
- should this change merge now?

Those are related, but they are not the same.

## Preflight Integration Guidance

### 1. Preflight Should Start With Structural Trustworthiness

The first job of preflight is to confirm that governed artifacts are present,
parseable, and bounded correctly.

### 2. Preflight Should Grow By Stable Models, Not Ad Hoc Rules

Later checks should derive from:

- the drift model
- the protocol template
- the traceability model
- the runtime-capacity trust model
- the repo-management binding surface

Preflight should not grow by one-off heuristics that bypass those upstream
models.

### 3. Manual Review Can Remain Explicit

Some checks should remain manual until the repo has a trustworthy automated
path.

Examples include:

- whether a planning-capacity snapshot still matches real-world availability
- whether a role binding still reflects the right operating model
- whether a repo-management authority split is still the right policy choice

## Initial Validation Expectations

The repo should eventually be able to validate at least:

- presence of the core protocol set and its README linkage
- presence of required gate, scope, and review-pass fields in bound protocol
  surfaces
- structural coherence of runtime-capacity artifacts
- presence of discovery and traceability declarations for runtime assets
- presence of project-specific repo-management binding docs once a provider is
  chosen
- continued alignment of Codex runtime assets with their authoritative Codex
  binding entrypoint

## Constraints

- Validation must stay downstream of the authoritative canon and bindings.
- Validation must not become a shadow scheduler or shadow repository operator.
- Provider-specific checks should remain discoverable through the relevant
  binding entrypoints, not buried only in planning prose.

## Non-Goals

- Automatically assign work to runtimes.
- Prove live GitHub permissions or runtime availability.
- Replace QA review outcomes with structural checks alone.

## Related Artifacts

- [Drift Model](./Drift-Model.md)
- [Change-Management Model](./Change-Management-Model.md)
- [Protocol Template](./Protocols/Protocol-Template.md)
- [Repo Management](../RepoManagement/README.md)
