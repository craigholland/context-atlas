---
id: craig-materialization-traceability-model
title: Materialization Traceability Model
summary: Defines the portable traceability expectations that keep runtime-facing assets linked to the canon, application bindings, and template surfaces that authorize them.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, traceability, materialization, portability]
related:
  - ./Platform-Materialization-Model.md
  - ./Template-Model.md
  - ./Discovery-Model.md
  - ./Drift-Model.md
  - ./Validation-Model.md
supersedes: []
---

# Materialization Traceability Model

## Purpose

Define the portable traceability expectations that keep runtime-facing assets
linked to the canon, application bindings, and template surfaces that
authorize them.

## Scope

This document governs what a reviewer or downstream validation step should be
able to learn when checking whether a materialized asset still matches its
authoritative sources.

It does not require one environment-specific metadata syntax or tool.

## Binding Decisions

### 1. Materialized Assets Should Point Back To Their Authoritative Sources

A materialized asset should remain traceable back to the upstream sources that
authorize its meaning, such as:

- portable canon
- application-specific bindings
- template contracts
- discovery bindings when relevant

Traceability should make it possible to answer "which upstream artifacts does
this asset express?"

### 2. Traceability May Be Embedded Or Adjacent

Traceability information may be expressed in different downstream ways, such
as:

- embedded metadata
- adjacent manifest entries
- maintained mapping docs
- generated trace indexes

The portable requirement is traceability itself, not one concrete encoding.

### 3. Traceability Should Make Drift Review Concrete

When drift is suspected, a reviewer should be able to compare at least:

- the materialized asset being reviewed
- the upstream authoritative sources it claims to express
- the template surface or template contract that shaped it
- the downstream discovery surface, if discovery mechanics are relevant

Traceability should reduce guesswork during review rather than merely record
provenance for its own sake.

### 4. Traceability Should Distinguish Semantic Sources From Runtime Mechanics

Traceability should make it clear which upstream artifacts govern meaning and
which downstream artifacts govern storage or discovery mechanics.

That distinction matters because runtime-facing assets may move between
folders, manifests, or registries without changing the underlying semantics.

### 5. Traceability Should Support Later Regeneration And Validation Work

The traceability model should be explicit enough that later validation,
regeneration, or drift-control work can rely on it without first inventing a
new provenance scheme.

### 6. Materialized Assets Should Declare Their Maintenance Mode

Each materialized asset surface should make it possible to tell whether it is:

- hand-maintained
- generated
- mixed, where some portions are regenerated and others remain human-owned

That declaration does not need one portable encoding, but the maintenance mode
itself should not stay implicit.

### 7. Regeneration Should Preserve Upstream Authority And Traceability

When an asset is regenerated, that process should preserve or refresh the
traceability needed to connect the regenerated output back to its upstream
authoritative sources.

Regeneration should not become a reason to discard provenance or silently
replace the semantic source of truth.

### 8. Mixed Maintenance Should Keep Human-Owned And Generated Surfaces Distinct

If a materialization uses a mixed maintenance model, reviewers should still be
able to tell:

- which portions are expected to regenerate
- which portions remain manually curated
- which upstream sources govern each portion

Mixed maintenance should not become an excuse for blurry ownership.

### 9. Traceability Should Support Drift Detection

Traceability declarations should make it possible for later validators and
reviewers to detect:

- missing authoritative-source lineage
- stale provenance after a binding changes
- runtime assets whose stated maintenance mode no longer matches reality
- discovery surfaces that still claim authority they no longer satisfy

Traceability should therefore support drift review directly, not only historic
provenance.

## Constraints

- Traceability rules must remain portable across multiple environments.
- Portable traceability guidance must not require one metadata field layout,
  one manifest schema, or one code generator.
- Traceability should stay subordinate to upstream canon and application
  bindings rather than becoming a new source of truth.
- Regeneration expectations should remain portable and should not assume one
  code generator, workflow engine, or environment hook.

## Non-Goals

- Define a platform-specific manifest format.
- Define platform-specific regeneration commands or automation hooks.
- Replace downstream validation or review policy.

## Related Artifacts

- [Platform Materialization Model](./Platform-Materialization-Model.md)
- [Template Model](./Template-Model.md)
- [Discovery Model](./Discovery-Model.md)
- [Drift Model](./Drift-Model.md)
- [Validation Model](./Validation-Model.md)
