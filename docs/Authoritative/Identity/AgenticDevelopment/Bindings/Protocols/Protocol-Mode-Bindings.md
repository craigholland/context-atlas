---
id: context-atlas-protocol-mode-bindings
title: Context Atlas Protocol Mode Bindings
summary: Defines how the shared protocol family binds to the Context Atlas mode model so workflow paths and execution-state transitions remain related but non-collapsed.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, protocols, modes]
related:
  - ../Modes/Mode-Model.md
  - ../Modes/Mode-Transition-Graph.md
  - ./Protocol-Role-Bindings.md
  - ../../../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md
  - ../../../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md
  - ../../../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md
  - ../../../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md
  - ../../../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md
supersedes: []
---

# Context Atlas Protocol Mode Bindings

## Purpose

Define how the shared protocol family binds to the Context Atlas mode model.

## Scope

This document governs the relationship between protocols and modes.

It does not redefine the mode catalog or the protocol catalog. It binds them.

## Binding Decisions

### 1. Planning Protocol Primarily Uses `planning`

The [Planning Protocol](../../../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md)
normally executes inside `planning`.

### 2. Execution Slice Protocol Primarily Uses `implementation`

The [Execution Slice Protocol](../../../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
normally executes inside `implementation`.

### 3. Review Protocol Primarily Uses `review`

The [Review Protocol](../../../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md)
normally executes inside `review`.

Multiple review passes may occur inside the same review-mode span. Context
Atlas should not create a new mode transition for each pass.

### 4. Rework Protocol Primarily Uses `rework`

The [Rework Protocol](../../../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md)
normally executes inside `rework`.

### 5. Recovery Protocol Primarily Uses `recovery`

The [Recovery Protocol](../../../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md)
normally executes inside `recovery`.

### 6. Delegation, Handoff, And Escalation Are Mode-Spanning Contract Protocols

The delegation, handoff, and escalation protocols are cross-cutting structured
contract workflows.

They normally occur:

- within the current mode
- at the edge of leaving one mode
- or at the edge of entering the next protocol-owned mode

They should not be modeled as long-running dedicated modes of their own.

### 7. Operational Delivery Remains A Project Mode Without A Story 5 Protocol

`operational_delivery` is part of the Context Atlas mode model, but Story 5's
initial shared protocol family does not yet introduce a dedicated portable
operational-delivery protocol.

That absence is intentional and should remain explicit until a later story
binds operational delivery into its own governed protocol surface.

## Constraints

- Protocol-to-mode bindings should stay explicit enough that runtime
  materialization does not invent hidden mode semantics.
- Review passes should remain review lenses, not mode nodes.
- Cross-cutting contract protocols should not be mistaken for primary execution
  modes.

## Non-Goals

- Replace the mode model or transition graph.
- Define project-specific runtime event triggers.
- Define every future protocol family.

## Related Artifacts

- [Context Atlas Mode Model](../Modes/Mode-Model.md)
- [Mode Transition Graph](../Modes/Mode-Transition-Graph.md)
- [Protocol Role Bindings](./Protocol-Role-Bindings.md)
- [Planning Protocol](../../../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md)
- [Execution Slice Protocol](../../../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
- [Review Protocol](../../../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md)
- [Rework Protocol](../../../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md)
- [Recovery Protocol](../../../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md)


