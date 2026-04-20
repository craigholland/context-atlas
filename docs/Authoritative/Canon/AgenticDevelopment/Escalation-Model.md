---
id: craig-escalation-model
title: Escalation Model
summary: Defines the portable escalation and return-contract rules that keep delegated work bounded and prevent specialists from quietly acquiring broader authority.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, escalation, delegation, return-contract, canon]
related:
  - ./Delegation-Model.md
  - ./Composition-Decision-Model.md
  - ./Agent-Authority-Model.md
  - ./Agent-Composition-Model.md
  - ./Protocols/Escalation-Protocol.md
supersedes: []
---

# Escalation Model

## Purpose

Define the portable escalation and return-contract rules that keep delegated
work bounded and structurally honest.

## Scope

This document governs when a delegate should return control, findings, or a
blocked state to a broader authority boundary instead of widening its own
scope.

It does not define protocol-specific escalation steps or a project's concrete
review workflow.

The protocol-specific workflow and contract shape for escalation live
downstream in [Protocols/Escalation-Protocol.md](./Protocols/Escalation-Protocol.md).

## Binding Decisions

- Escalation is the explicit return of a decision, blocked state, or risk to a
  broader authority boundary.
- Escalation is not failure; it is evidence that the delegate stayed within its
  structural contract.
- A delegate should escalate when:
  - the requested work exceeds its stated scope
  - conflicting signals require broader judgment
  - a higher-authority decision is needed
  - the next required mutation lies outside the delegate's allowed boundary
- A valid return contract should communicate:
  - what bounded work was completed
  - what remains unresolved
  - why escalation was necessary
  - what next action appears to be required
- Return contracts should be structured and machine-readable, typically in a
  form representable as YAML or JSON, so the receiving authority boundary does
  not have to reconstruct the state from prose.

## Constraints

- Delegates must not resolve scope overflow by silently widening their own
  authority.
- Return contracts should be explicit enough that the parent boundary can
  resume work without reconstructing the delegated context from scratch.
- Escalation should not silently transfer approval or ownership authority;
  those boundaries must remain explicit in the downstream binding layer.
- Frequent predictable escalation may indicate that the work should remain
  parent-owned or be restructured.

## Non-Goals

- Define a project-specific or runtime-specific handoff artifact schema.
- Define protocol-specific rework loops.
- Replace broader workflow protocols with escalation rules alone.

## Related Artifacts

- [Delegation Model](./Delegation-Model.md)
- [Composition Decision Model](./Composition-Decision-Model.md)
- [Agent Authority Model](./Agent-Authority-Model.md)
- [Agent Composition Model](./Agent-Composition-Model.md)
- [Escalation Protocol](./Protocols/Escalation-Protocol.md)
