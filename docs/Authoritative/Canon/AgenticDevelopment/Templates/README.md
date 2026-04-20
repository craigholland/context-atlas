---
id: craig-generic-template-contracts
title: Generic Template Contracts
summary: Defines the portable information contracts that each generic materialization template type should carry before any platform-specific file layout is chosen.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, templates, contracts, materialization, portability]
related:
  - ../Template-Model.md
  - ../Materialization-Boundary-Model.md
  - ../RoleArchetypes/README.md
  - ../Protocols/README.md
supersedes: []
---

# Generic Template Contracts

## Purpose

Define the portable information contract that each generic template type should
carry before a platform-specific layout is chosen.

## Scope

This document governs the information expected from generic template surfaces.

It does not define any specific runtime filename, extension, or folder path.

## Shared Template Contract

Every generic template surface should be able to answer:

- what concept family it projects
- which upstream authoritative sources it depends on
- whether it expresses portable canon, project binding, or both
- which runtime-facing asset class it is meant to support
- which semantics are required versus optional

## Template-Type Expectations

### Parent-Agent Template

Should carry:

- the parent-owned accountability being projected
- attached or referenced skill surfaces
- delegated specialist relationships when the runtime needs them
- upstream role, protocol, and mode references when applicable

### Specialist-Agent Template

Should carry:

- the bounded delegated scope being projected
- its parent relationship or owning boundary
- attached skills and escalation/return expectations when applicable

### Skill Template

Should carry:

- the atomic skill purpose
- the upstream semantic source for that skill
- any required attachment context or usage constraints

### Role-Projection Template

Should carry:

- the project-specific role being projected
- the authoritative role source it depends on
- enough context for a runtime-facing asset to distinguish role accountability
  from actor materialization

### Mode Template

Should carry:

- the execution state being projected
- its authoritative entry/exit semantics
- any mutation or transition constraints that a runtime-facing asset must
  preserve

### Protocol Template

Should carry:

- the workflow path being projected
- the required protocol sections or outcome semantics that must survive
  materialization
- any review-pass, handoff, or escalation semantics that the runtime-facing
  asset must not erase

### Runtime-Guidance Template

Should carry:

- non-semantic operational guidance needed around the runtime-facing asset
- references back to the authoritative sources that justify that guidance

### Configuration Template

Should carry:

- non-behavioral settings needed by the runtime-facing asset
- the authoritative source for those settings
- enough context to distinguish configuration from canon semantics

## Constraints

- Template contracts should preserve upstream traceability.
- Contracts should remain platform-agnostic.
- Contracts should not collapse unrelated concept families into one undifferentiated blob.

## Non-Goals

- Define platform-specific file headers or front matter.
- Define discovery folder conventions.
- Define regeneration or drift-control rules in full.

## Related Artifacts

- [Template Model](../Template-Model.md)
- [Materialization Boundary Model](../Materialization-Boundary-Model.md)
- [Role Archetypes README](../RoleArchetypes/README.md)
- [Protocols README](../Protocols/README.md)
