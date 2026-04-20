---
id: craig-agentic-change-management-model
title: Change-Management Model
summary: Defines the governed path for introducing, reviewing, recovering, and evolving agentic-development and repo-management changes over time.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, change-management, review, recovery, governance]
related:
  - ./Drift-Model.md
  - ./Validation-Model.md
  - ../Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../RepoManagement/README.md
supersedes: []
---

# Change-Management Model

## Purpose

Define the governed path for introducing, reviewing, recovering, and evolving
changes across the agentic-development and repo-management system.

## Scope

This model governs changes to:

- portable canon
- project-specific bindings
- machine-readable planning inputs
- runtime-facing materializations
- repo-management provider and project-binding surfaces
- local governance artifacts when they anchor those surfaces

It does not define one repository-provider workflow or one runtime-specific
automation pipeline.

## Core Rule

Changes should originate at the highest authoritative layer that actually owns
the semantics being changed.

That means:

- change the portable canon when portable meaning changes
- change the project binding when the application-specific choice changes
- change the materialization layer when only the runtime projection changes
- change repo-management bindings when repository-provider policy changes

Runtime-facing assets should not become the first place a semantic change is
introduced.

## Change Classes

### 1. Canon Change

Use this path when changing:

- definitions
- invariant authority rules
- protocol template shape
- drift, validation, or traceability meaning

### 2. Binding Change

Use this path when changing:

- the active role roster
- role authority or role-to-agent bindings
- mode participation
- gate-to-review-pass mapping
- chosen repository provider policy

### 3. Planning-Input Change

Use this path when changing:

- governed capacity values
- bounded decomposition policy inputs
- other machine-readable planning snapshots

### 4. Materialization Change

Use this path when changing:

- runtime folder conventions
- templates
- discovery manifests
- runtime-facing copied, adapted, or derived assets

These changes should remain traceable back to the canon and bindings that
authorize them.

## Required Change Path

When a meaningful semantic change is proposed, the governed path is:

1. update the authoritative source that owns the meaning
2. update project bindings if they are affected
3. update planning artifacts if decomposition or execution guidance changes
4. update runtime-facing assets only after upstream authority is clear
5. refresh owner files and metadata where the change alters governance scope
6. run the relevant validation and review gates

## Review Expectations

- semantic and authority changes should receive architectural review
- repo-management authority changes should receive security-oriented review
- user-facing workflow consequences should receive product-oriented review at
  the appropriate gate
- structural validation should support review, not replace it

## Recovery Expectations

When drift or bad changes are discovered, recovery should proceed by:

1. identifying which authoritative layer owns the mismatch
2. deciding whether the upstream source or downstream artifact is wrong
3. repairing the source-of-truth path first
4. regenerating or refreshing downstream assets as needed
5. documenting the recovery outcome in the governed surface rather than in
   runtime-only notes

Recovery should not normalize manual hotfixes directly inside runtime-facing
assets when those hotfixes bypass the canon or project bindings.

## Constraints

- The governed path must remain usable for small changes.
- Review and recovery rules must not require a new ceremony for trivial wording
  edits that do not affect meaning.
- Change-management guidance must remain portable enough to support multiple
  runtime environments and repository providers.

## Non-Goals

- Replace project planning and decomposition.
- Define provider-specific click-by-click setup instructions.
- Force every doc-only correction through the heaviest review path.

## Related Artifacts

- [Drift Model](./Drift-Model.md)
- [Validation Model](./Validation-Model.md)
- [Craig Architecture - Planning And Decomposition](../Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Repo Management](../RepoManagement/README.md)
