---
id: craig-composition-decision-model
title: Composition Decision Model
summary: Defines the portable decision rules for when new work should be handled by adding a skill, introducing a specialist, or keeping responsibility parent-owned.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, composition, decisions, specialists, canon]
related:
  - ./Agent-Composition-Model.md
  - ./Delegation-Model.md
  - ./Escalation-Model.md
  - ./Skill-Attachment-Model.md
supersedes: []
---

# Composition Decision Model

## Purpose

Define the portable decision rules for when a new need should be handled by
adding a skill, introducing a specialist, or keeping responsibility
parent-owned.

## Scope

This document governs structural composition decisions in an agentic system,
with the goal of preventing shallow specialist sprawl while preserving real
authority boundaries where they matter.

It does not define a project's actual role roster or protocol catalog.

## Binding Decisions

- The default bias should be toward the smallest structural change that keeps
  authority boundaries honest.
- Add a skill when the need is:
  - a reusable capability
  - bounded enough to stay atomic
  - attachable to an existing actor without creating a new authority boundary
- Introduce a specialist when the need is:
  - a recurring narrow subdomain
  - better served by a curated skill bundle than one extra skill attachment
  - structurally distinct enough to justify explicit scope and return
    constraints
- Keep work parent-owned when the need requires:
  - workflow continuity
  - cross-domain judgment
  - final authority decisions
  - repeated escalation that would make delegation mostly ceremonial

## Anti-Patterns

- Creating a new specialist for every new work slice.
- Creating a specialist when a single added skill would suffice.
- Treating temporary workload pressure as proof that a new specialist is needed.
- Delegating work that predictably returns to the parent for final judgment on
  nearly every run.

## Constraints

- Composition decisions should prefer explicit capability reuse over actor
  multiplication.
- New specialists should justify themselves by real structural difference, not
  by naming convenience.
- Parent-owned work should remain explicit where delegation would hide genuine
  accountability.

## Non-Goals

- Choose a specific application's initial specialist roster.
- Define protocol-level escalation steps in detail.
- Define environment-specific manifest templates for composed actors.

## Related Artifacts

- [Agent Composition Model](./Agent-Composition-Model.md)
- [Delegation Model](./Delegation-Model.md)
- [Escalation Model](./Escalation-Model.md)
- [Skill Attachment Model](./Skill-Attachment-Model.md)
