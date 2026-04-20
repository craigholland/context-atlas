---
id: craig-agent-authority-model
title: Agent Authority Model
summary: Defines the portable relationship chain and authority invariants that govern parent agents, specialists, roles, protocols, modes, skills, delegation, handoff, and escalation.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, authority, canon, delegation, handoff]
related:
  - ./Agentic-Development-Glossary.md
  - ../Architecture/Craig-Architecture.md
  - ../../Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md
supersedes: []
---

# Agent Authority Model

## Purpose

Define the invariant relationship model for agentic development so later
project-specific bindings and runtime materializations preserve the same
authority chain across AI environments.

## Scope

This document governs the portable relationship between parent agents,
specialists, roles, protocols, modes, skills, delegation, handoff, and
escalation.

It does not choose which roles, specialists, skills, or protocols a specific
project uses.

## Binding Decisions

- The fundamental relationship chain is:
  - a parent agent embodies a role
  - a parent agent follows protocols
  - a parent agent enters modes while executing a protocol
  - a parent agent or specialist uses skills to perform bounded work
  - a parent agent may delegate bounded work to specialists
- A `role` is an accountability concept, not a runtime artifact.
- A `parent agent` is the accountable actor that carries a role through
  protocol execution.
- A `specialist` is a bounded delegate, not a parallel top-level owner of the
  same workflow.
- A `mode` is an execution state, not a role or protocol.
- A `protocol` defines workflow structure, gates, required artifacts, handoffs,
  and exit criteria, but does not replace role or mode semantics.
- A `skill` is a reusable capability unit, not an owning actor, role, or
  workflow path.
- Delegation transfers bounded execution responsibility, but does not
  automatically transfer the parent agent's overall accountability.
- Handoff is the explicit protocol-governed transfer of workflow ownership
  between eligible actors.
- Escalation returns decisions or blocked states to a broader authority
  boundary rather than silently widening a delegate's authority.

## Constraints

- Parent agents should not be modeled as mere containers of skills; their
  defining property is accountable workflow ownership.
- Specialists should not silently acquire broader authority than the parent
  agent granted them.
- Protocol participation must not blur the distinction between actor
  accountability and workflow structure.
- Mode transitions must not be treated as implicit substitutes for handoff,
  escalation, or delegation.
- The authority model must remain portable and must not assume one vendor's
  runtime layout or discovery semantics.

## Non-Goals

- Define the project-specific role roster for Context Atlas.
- Define the concrete workflow protocols a project chooses to adopt.
- Select current mode names or current skill libraries.
- Bind these rules to any specific AI runtime.

## Related Artifacts

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Craig-Architecture.md](../Architecture/Craig-Architecture.md)
- [Story 1 - Portable Agentic Development Canon](../../Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md)
