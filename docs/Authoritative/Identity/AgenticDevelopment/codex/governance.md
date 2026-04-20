---
id: context-atlas-codex-governance
title: Context Atlas Codex Governance
summary: Defines the review hooks, refresh expectations, and drift checks that keep the Codex materialized surface aligned with the authoritative canon, project bindings, and Codex creation guidance.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, governance]
related:
  - ./README.md
  - ./folder_layout.md
  - ./creation_guidance.md
  - ../../Context-Atlas-Agentic-Development-Profile.md
  - ../Role-Model.md
  - ../Mode-Model.md
  - ../Protocol-Role-Bindings.md
  - ../Protocol-Mode-Bindings.md
  - ../Gate-Review-Pass-Matrix.md
supersedes: []
---

# Context Atlas Codex Governance

## Purpose

Define the review hooks and governance expectations that keep the Codex
materialized surface aligned with the authoritative canon, project bindings,
and Codex creation guidance.

## Scope

This document governs how Codex binding artifacts should be reviewed and what
they must stay aligned with over time.

It does not replace the generic drift-control model from Story 9.

## Binding Decisions

### 1. Codex Asset Review Must Check Upstream Alignment Explicitly

When Codex assets or Codex-binding docs change, review should verify alignment
with:

- the project role model and role-accountability/authority bindings
- the project mode model and transition/mutation bindings
- the project protocol-role and protocol-mode bindings
- the gate-review-pass model where review-facing behavior is affected
- the Story 7 materialization, discovery, template, and traceability model
- the Codex creation guidance and folder-layout rules

### 2. Review Should Check The Runtime Surface By Concept Family

Codex review should not treat the runtime surface as one flat bundle.

Review should check the affected concept families explicitly, such as:

- role projections
- parent-agent or specialist descriptors
- mode surfaces
- protocol surfaces
- skills
- runtime orientation/config surfaces

That keeps localized changes from silently affecting unrelated concept
families.

### 3. Review Should Check Copied, Adapted, And Derived Content Separately

For Codex assets that follow the creation guidance, review should distinguish:

- copied content that should stay semantically identical to upstream sources
- adapted content that should remain faithful while becoming Codex-facing
- derived content such as filenames, traceability metadata, and maintenance
  declarations

That separation helps reviewers find the real source of drift.

### 4. Review Should Check Traceability And Maintenance Mode

Codex assets should continue to declare:

- the upstream sources they depend on
- the maintenance mode that governs whether they are hand-maintained,
  generated, or mixed

Review should treat missing or contradictory provenance as a governance issue,
not as a cosmetic omission.

## Review Checklist

When Codex-binding assets change, reviewers should check:

- the file still lives at the correct Codex-bound path
- ids and names follow the Codex naming conventions
- the concept family is still clear from the file and its metadata
- upstream sources are still cited accurately
- copied/adapted/derived content still follows the creation guidance
- the asset does not redefine portable or Identity-layer semantics locally

## Constraints

- Codex governance should stay downstream of the generic drift-control model.
- Review hooks should remain concrete enough to use in normal Story work.
- Codex governance should not imply that Codex-specific practices are generic
  requirements for all future runtime bindings.

## Non-Goals

- Replace the project-wide review-pass model.
- Define automated validation logic in full.
- Define a non-Codex governance model.

## Related Artifacts

- [Context Atlas Codex Binding](./README.md)
- [Context Atlas Codex Folder Layout](./folder_layout.md)
- [Context Atlas Codex Creation Guidance](./creation_guidance.md)
- [Context Atlas Agentic Development Profile](../../Context-Atlas-Agentic-Development-Profile.md)
- [Role Model](../Role-Model.md)
- [Mode Model](../Mode-Model.md)
- [Protocol Role Bindings](../Protocol-Role-Bindings.md)
- [Protocol Mode Bindings](../Protocol-Mode-Bindings.md)
- [Gate Review Pass Matrix](../Gate-Review-Pass-Matrix.md)
