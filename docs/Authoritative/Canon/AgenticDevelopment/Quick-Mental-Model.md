---
id: craig-agentic-development-quick-mental-model
title: Quick Mental Model
summary: Provides a short human-readable primer on the main agentic-development entities and how they fit together before readers dive into the full canon.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, canon, primer, mental-model, orientation]
related:
  - ./README.md
  - ./Agentic-Development-Glossary.md
  - ./Agent-Authority-Model.md
  - ./Agent-Composition-Model.md
  - ./Mode-Model.md
  - ./Protocols/README.md
  - ./Skill-Contract.md
  - ./Skill-Attachment-Model.md
supersedes: []
---

# Quick Mental Model

## Purpose

Give a short human-readable explanation of the main agentic-development
entities before a reader dives into the full canon.

This is the "for dummies" entrypoint for the portable model, not the detailed
source of truth for every edge case.

## The Short Version

The easiest way to think about the system is:

- a `role` says who is accountable
- a `parent agent` is the accountable actor that carries that role in runtime
- a `skill` is an atomic capability the actor can use directly
- a `specialist` is a narrower delegated actor with a bounded scope
- a `mode` says what state the work is currently in
- a `protocol` says what workflow path is being followed

In one sentence:

> A parent agent carries a role, uses skills directly, delegates bounded work
> to specialists, operates in modes, and moves work through protocols.

## The Core Entities

### Role

A `role` is an accountability concept.

It answers questions like:

- who owns this kind of work
- who is responsible for its outcome
- who should absorb findings, escalation, or return work

A role is not yet the runtime actor. It is the responsibility boundary.

### Parent Agent

A `parent agent` is the accountable actor that embodies a role.

It is the broad coordinating boundary that:

- owns the role-aligned outcome
- may use some skills directly
- may delegate bounded work to specialists
- remains accountable even when delegation happens

If you want one "main actor" for a role, that is usually the parent agent.

### Skill

A `skill` is an atomic reusable capability.

It is not a role, not a protocol, and not a whole agent by itself.

Examples:

- Python authoring
- Python debugging
- planning decomposition
- PR review and handoff

Skills are the smallest reusable units in the model.

### Specialist

A `specialist` is a narrower delegated actor.

It exists when a parent agent needs a repeatable bounded helper rather than
just "another skill."

A specialist should have:

- a focused scope
- curated attached skills
- clear constraints
- a return path back to its parent

A specialist helps with narrow execution or analysis. It does not replace the
parent agent as the top-level accountable boundary.

### Mode

A `mode` is the current execution state of the work.

Examples:

- `planning`
- `implementation`
- `review`
- `rework`
- `recovery`

Modes answer "what state are we in right now?" not "who owns the work?"

### Protocol

A `protocol` is the workflow path being followed.

Examples:

- `planning`
- `execution-slice`
- `review`
- `rework`
- `recovery`

Protocols answer "what governed workflow are we performing?" not "what actor
are we?" and not "what state label do we show?"

## How The Pieces Fit Together

The normal relationship chain is:

`Role -> Parent Agent -> Skills / Specialists -> Modes -> Protocols`

Read that as:

1. a `role` defines the accountability boundary
2. a `parent agent` embodies that role
3. the parent agent either uses direct `skills` or delegates to `specialists`
4. the work is happening in a `mode`
5. the work is moving through a `protocol`

## A Small Example

Here is a simple mental picture:

- `Backend` is the `role`
- `parent-backend` is the `parent agent`
- `python-authoring` is a direct `skill`
- `specialist-python-implementation` is a delegated `specialist`
- `implementation` is the current `mode`
- `execution-slice` is the active `protocol`

That means:

- Backend is accountable
- the backend parent agent is carrying that accountability
- it may code directly with its own skills
- or delegate a bounded slice to a Python specialist
- while the work is in implementation
- and the workflow path is execution-slice

## Common Confusions To Avoid

### Role vs Parent Agent

- `role` = accountability
- `parent agent` = accountable actor

These are related, but they are not the same thing.

### Skill vs Specialist

- `skill` = atomic capability
- `specialist` = bounded actor composed from curated skills

A specialist is not just "a skill with a fancy name."

### Mode vs Protocol

- `mode` = current state
- `protocol` = workflow path

The work may stay in one mode while still following a governed protocol.

### Parent Agent vs Specialist

- `parent agent` = broader accountable boundary
- `specialist` = narrower delegate

The specialist helps. The parent agent still owns the outcome unless a later
explicit handoff says otherwise.

## What This Primer Is Not

This file does not define:

- a project's actual role roster
- a project's actual parent-agent roster
- concrete runtime file layouts
- provider-specific platform rules
- every detailed authority, delegation, or review rule

Use the deeper canon documents for that.

## Where To Read Next

- [Agentic Development README](./README.md)
- [Agentic Development Glossary](./Agentic-Development-Glossary.md)
- [Agent Authority Model](./Agent-Authority-Model.md)
- [Agent Composition Model](./Agent-Composition-Model.md)
- [Mode Model](./Mode-Model.md)
- [Protocols README](./Protocols/README.md)

