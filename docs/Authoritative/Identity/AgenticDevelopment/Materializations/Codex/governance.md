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
last_reviewed: 2026-04-22
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, governance]
related:
  - ./README.md
  - ./folder_layout.md
  - ./creation_guidance.md
  - ../../../Context-Atlas-Agentic-Development-Profile.md
  - ../../Bindings/Roles/Role-Model.md
  - ../../Bindings/Modes/Mode-Model.md
  - ../../Bindings/Protocols/Protocol-Role-Bindings.md
  - ../../Bindings/Protocols/Protocol-Mode-Bindings.md
  - ../../Bindings/Protocols/Gate-Review-Pass-Matrix.md
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

It does not replace the generic drift-control model from Story 10 or the
portable [Drift Model](../../../../Canon/AgenticDevelopment/Drift-Model.md).

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
- the maintenance mode that governs whether they are human-managed,
  generated, or mixed

Review should treat missing or contradictory provenance as a governance issue,
not as a cosmetic omission.

That maintenance mode should come from
`docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`,
not from a local runtime edit inside `.codex/` or `.agents/skills/`.

### 5. Codex Assets Should Refresh After Meaningful Upstream Changes

Codex assets should be reviewed for refresh when upstream changes affect:

- role ownership or authority
- parent-agent versus specialist structure
- mode vocabulary or transition/mutation rules
- protocol bindings or review-pass expectations
- Codex folder layout or naming conventions
- Codex templates or creation-guidance rules

The refresh trigger is the upstream semantic or binding change, not just a
desire to keep runtime files cosmetically recent.

### 6. Codex Drift Should Be Defined Explicitly

For the Codex surface, drift includes at least:

- an asset living at the wrong bound path
- names or ids that no longer follow the Codex naming conventions
- copied content that no longer matches its upstream source
- adapted content that now changes meaning instead of presentation
- missing or stale traceability declarations
- missing or stale maintenance-mode declarations
- maintenance-mode declarations that contradict the upstream manifest
- generated-surface notices that no longer match the real upstream
  source-of-truth model
- Codex assets that no longer follow the creation guidance or folder-layout
  rules

### 7. Local Runtime Edits Must Not Be Mistaken For Durable Upstream Change

Contributors may edit generated `.codex/` or `.agents/skills/` assets locally
while exploring or testing, but those files should still be treated as derived
surfaces that may be overwritten by regeneration.

If a reviewer sees a desired lasting change expressed only in a runtime asset,
that should be treated as incomplete governance. The durable source update
belongs upstream in:

- the portable canon for reusable or global meaning
- the Identity layer for Context Atlas-specific meaning

If a surface truly needs to stop being generator-owned, the lasting change is
to update the manifest-level `maintenance_mode`, not to flip a local toggle in
the generated runtime file.

### 8. `mixed` Must Not Be Treated As Magic Preservation

Until the Codex binding defines an explicit manual-block format and the
generator validates it, `mixed` should be treated as a declared future mode,
not as permission for ambiguous freeform preservation behavior.

## Review Checklist

When Codex-binding assets change, reviewers should check:

- the file still lives at the correct Codex-bound path
- ids and names follow the Codex naming conventions
- the concept family is still clear from the file and its metadata
- the file still tells readers that it is a generated or regenerated derived
  surface when that notice is expected
- upstream sources are still cited accurately
- copied/adapted/derived content still follows the creation guidance
- the asset does not redefine portable or Identity-layer semantics locally

## Refresh Expectations

- refresh the affected Codex assets when upstream binding meaning changes
- refresh the affected Codex assets when the Codex folder layout, templates, or
  creation guidance changes in a way that invalidates current files
- do not refresh unrelated Codex assets only to create artificial churn

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
- [Context Atlas Agentic Development Profile](../../../Context-Atlas-Agentic-Development-Profile.md)
- [Role Model](../../Bindings/Roles/Role-Model.md)
- [Mode Model](../../Bindings/Modes/Mode-Model.md)
- [Protocol Role Bindings](../../Bindings/Protocols/Protocol-Role-Bindings.md)
- [Protocol Mode Bindings](../../Bindings/Protocols/Protocol-Mode-Bindings.md)
- [Gate Review Pass Matrix](../../Bindings/Protocols/Gate-Review-Pass-Matrix.md)

