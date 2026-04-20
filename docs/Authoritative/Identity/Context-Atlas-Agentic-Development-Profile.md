---
id: context-atlas-agentic-development-profile
title: Context Atlas Agentic Development Profile
summary: Defines the project-specific structural binding that applies the portable parent-agent, specialist, and skill canon to Context Atlas.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, structural-binding, profile]
related:
  - ./Context-Atlas-Charter.md
  - ./Context-Atlas-System-Model.md
  - ./AgenticDevelopment/runtime_capacity.yaml
  - ./AgenticDevelopment/Role-Model.md
  - ./AgenticDevelopment/Role-Accountability-Matrix.md
  - ./AgenticDevelopment/Role-Authority-Matrix.md
  - ./AgenticDevelopment/Role-Agent-Binding-Model.md
  - ./AgenticDevelopment/Protocol-Role-Bindings.md
  - ./AgenticDevelopment/Protocol-Mode-Bindings.md
  - ./AgenticDevelopment/Gate-Review-Pass-Matrix.md
  - ./AgenticDevelopment/Mode-Model.md
  - ./AgenticDevelopment/Mode-Transition-Rules.md
  - ./AgenticDevelopment/Mode-Mutation-Matrix.md
  - ./AgenticDevelopment/Role-Mode-Matrix.md
  - ./AgenticDevelopment/Mode-Transition-Graph.md
  - ./AgenticDevelopment/codex/README.md
  - ../AgenticDevelopment/Agent-Composition-Model.md
  - ../AgenticDevelopment/Composition-Decision-Model.md
  - ../AgenticDevelopment/Boundary-Model.md
supersedes: []
---

# Context Atlas Agentic Development Profile

## Purpose

Define the project-specific structural binding that applies the portable
parent-agent, specialist, and skill canon to Context Atlas.

## Scope

This document governs the structural shape that Context Atlas intends to use
for agentic development beneath the later role, mode, protocol, and
environment-specific materialization layers.

It does not replace the later role roster, mode model, protocol catalog, or
any environment-specific file layout.

## Binding Decisions

### 1. Context Atlas Uses A Parent-Agent Plus Specialist Structure

Context Atlas will not model its governed agentic-development surface as a flat
set of peer workers.

Instead, it will treat top-level accountable actors as parent agents and treat
delegated narrow-scope actors as specialists.

### 2. Top-Level Project Accountability Lives In The Parent Layer

The parent layer is where Context Atlas will bind future project-facing
accountabilities.

That means the later role model must name project accountabilities at the
parent layer rather than introducing a parallel specialist-owned accountability
system.

### 3. Specialists Are Bounded Delegates, Not A Second Role Layer

Specialists exist to execute narrow recurring scopes with curated skills and
explicit return contracts.

They are not the place where Context Atlas defines top-level project
responsibilities, workflow ownership, or final authority boundaries.

### 4. Skills Remain Atomic Reusable Units Across The Structure

Context Atlas adopts the portable skill model directly:

- skills are atomic reusable capabilities
- skills may attach to parent agents or specialists
- skills do not become alternate role, protocol, or mode definitions

### 5. The Initial Structural Bias Is Conservative

Context Atlas should prefer:

- adding a skill before introducing a new specialist
- introducing a specialist only when a real bounded authority difference exists
- keeping work parent-owned when delegation would mostly escalate back upward

This keeps the initial project structure governable and discourages specialist
sprawl.

### 6. Later Stories Must Bind Through This Profile

Later role, mode, protocol, capacity, and materialization stories should treat
this profile as the project-specific structural source of truth.

They should not bypass it by binding directly from the portable canon to
environment-facing assets.

### 7. Named Roles Must Bind At The Parent Layer

When Context Atlas defines named project roles, those roles should bind at the
parent-agent layer described by this profile.

That means the project role roster should be interpreted as top-level
accountability carried by parent agents, while specialists remain subordinate
delegates beneath those parent-owned roles.

### 8. Specialist Participation Does Not Change Role Ownership

When specialists contribute to a workstream, they do so beneath a
parent-owned role.

That means planning artifacts remain Planner/Decomp-owned, engine
implementation remains Backend-owned, user-facing documentation and evaluation
surfaces remain Documentation/UAT-owned, governed validation remains QA-owned,
and operational delivery remains DevOps-owned unless a later authority or
protocol artifact explicitly changes the handoff state.

### 9. Authority Must Stay Bound To Parent-Owned Roles Until Explicit Handoff

Context Atlas should treat approval, merge, release, and operational workflow
authority as role-bound parent-agent authority rather than as an ambient
capability available to any participant in the work.

That means delegation and escalation may route work or decisions, but they
should not implicitly reassign authority without an explicit downstream
contract.

### 10. Handoff State Changes Must Be Structured, Not Conversational

Context Atlas should treat inter-agent handoff, review, escalation, and return
state as changed only when a valid structured contract artifact exists.

That means:

- role transitions should not depend on prose-only status updates
- review intake should not depend on ad hoc tool-invocation comments
- YAML or JSON should be the expected contract shape, even when a later
  runtime materialization projects that contract onto a PR review or comment
  surface

### 11. Mode Bindings Must Stay Downstream Of The Structural Profile

Context Atlas should define project-specific modes, transition rules, mutation
rules, and role-to-mode bindings as downstream bindings on top of this
structural profile rather than mixing those concerns back into the parent
versus specialist model itself.

### 12. Role Bindings Must Remain Separate From Runtime Materialization

Context Atlas should define role-to-parent bindings at the project-identity
layer before any environment-specific files attempt to materialize those
bindings.

That keeps the project's accountability model readable even when later runtime
assets use different naming conventions or file layouts.

### 13. Protocol Bindings Must Remain Separate From Portable Protocol Definitions

Context Atlas should bind the portable protocol family to project roles, modes,
and review gates in the Identity layer rather than pushing those project
choices back into the portable protocol canon.

### 14. Planning Capacity Must Bind Through One Authoritative Artifact

Context Atlas should bind planning-time runtime capacity through one
machine-readable artifact at:

`docs/Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml`

That artifact is the authoritative planning-capacity input for decomposition.

It should remain:

- human-editable
- project-specific
- separate from live runtime availability or runtime-materialization state

### 15. Runtime Capacity Updates Must Be Intentional, Not Ambient

Context Atlas should treat changes to the runtime-capacity artifact as an
intentional planning update rather than as a side effect of transient runtime
conditions.

That means later tooling may validate or consume the file, but it should not
silently overwrite the planning input based on queue state, PR state, or
momentary worker availability.

### 16. Environment Bindings Must Consume This Profile Explicitly

When Context Atlas binds its agentic-development model into a concrete runtime
environment, that environment-specific binding should cite this profile as one
of its upstream authoritative inputs.

That keeps the project-specific structural choices readable before any
environment translates them into runtime-facing folders, templates, or helper
assets.

## Constraints

- Context Atlas should keep the parent layer small enough that top-level
  accountability remains legible.
- Specialists should justify themselves by repeated bounded value, not by
  one-off task convenience.
- Project-specific structural bindings must remain distinct from later
  environment-specific materialization choices.
- Environment-specific binding docs should inherit from this profile rather
  than restating the structural model ad hoc.

## Non-Goals

- Define the final named parent-agent role roster.
- Define the detailed project mode set, transitions, or mutation rules.
- Define the project's workflow protocol set.
- Define concrete environment-discovery files or folder layouts.
- Replace the later environment-binding docs that consume this profile.

## Related Artifacts

- [Context Atlas Charter](./Context-Atlas-Charter.md)
- [Context Atlas System Model](./Context-Atlas-System-Model.md)
- [Context Atlas Runtime Capacity Artifact](./AgenticDevelopment/runtime_capacity.yaml)
- [Context Atlas Role Model](./AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Accountability Matrix](./AgenticDevelopment/Role-Accountability-Matrix.md)
- [Context Atlas Role Authority Matrix](./AgenticDevelopment/Role-Authority-Matrix.md)
- [Context Atlas Role-Agent Binding Model](./AgenticDevelopment/Role-Agent-Binding-Model.md)
- [Protocol Role Bindings](./AgenticDevelopment/Protocol-Role-Bindings.md)
- [Protocol Mode Bindings](./AgenticDevelopment/Protocol-Mode-Bindings.md)
- [Gate Review Pass Matrix](./AgenticDevelopment/Gate-Review-Pass-Matrix.md)
- [Context Atlas Mode Model](./AgenticDevelopment/Mode-Model.md)
- [Mode Transition Rules](./AgenticDevelopment/Mode-Transition-Rules.md)
- [Mode Mutation Matrix](./AgenticDevelopment/Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](./AgenticDevelopment/Role-Mode-Matrix.md)
- [Mode Transition Graph](./AgenticDevelopment/Mode-Transition-Graph.md)
- [Context Atlas Codex Binding](./AgenticDevelopment/codex/README.md)
- [Agent Composition Model](../AgenticDevelopment/Agent-Composition-Model.md)
- [Composition Decision Model](../AgenticDevelopment/Composition-Decision-Model.md)
- [Boundary Model](../AgenticDevelopment/Boundary-Model.md)
