---
id: context-atlas-agentic-story-5-protocol-model
title: Story 5 - Protocol Model
summary: Defines the workflow protocols that govern execution, handoff, delegation, escalation, review, and recovery across Context Atlas agentic development.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, protocols, handoff, delegation]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ./story_3_context_atlas_role_model.md
  - ./story_4_context_atlas_mode_model.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/README.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Protocol-Template.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Planning-Protocol.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Review-Pass-Model.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Review-Protocol.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Rework-Protocol.md
  - ../../../Authoritative/AgenticDevelopment/Protocols/Recovery-Protocol.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Accountability-Matrix.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md
  - ../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md
  - ../../../Authoritative/AgenticDevelopment/Delegation-Model.md
  - ../../../Authoritative/AgenticDevelopment/Escalation-Model.md
  - ../../../Authoritative/AgenticDevelopment/Mode-Model.md
supersedes: []
---

# Story 5 - Protocol Model

## Objective

Define the shared workflow protocols that govern how work is performed and
handed off across Context Atlas agentic development so execution logic lives in
first-class protocols rather than fragmented role notes or runtime prompts, and
so it is explicit that agents follow protocols while embodying roles and
entering modes during protocol execution, and so QA review is modeled as one
review workflow with explicit review passes that vary by gate instead of as an
ad hoc tool-trigger convention.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Story 4 - Context Atlas Mode Model](./story_4_context_atlas_mode_model.md)
- [Context Atlas Role Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Accountability Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Accountability-Matrix.md)
- [Context Atlas Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Context Atlas Mode Model](../../../Authoritative/Identity/AgenticDevelopment/Mode-Model.md)
- [Mode Transition Rules](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Rules.md)
- [Mode Mutation Matrix](../../../Authoritative/Identity/AgenticDevelopment/Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Mode-Matrix.md)
- [Mode Transition Graph](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Graph.md)
- [Agentic Development Glossary](../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md)
- [Mode Model](../../../Authoritative/AgenticDevelopment/Mode-Model.md)
- [Protocols README](../../../Authoritative/AgenticDevelopment/Protocols/README.md)
- [Protocol Template](../../../Authoritative/AgenticDevelopment/Protocols/Protocol-Template.md)
- [Planning Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Planning-Protocol.md)
- [Execution Slice Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
- [Review Pass Model](../../../Authoritative/AgenticDevelopment/Protocols/Review-Pass-Model.md)
- [Review Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Review-Protocol.md)
- [Rework Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Rework-Protocol.md)
- [Recovery Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Recovery-Protocol.md)
- Current repo experience with planning, slice execution, review gating, rework, and recovery

## Proposed Tasks

### Task 1: Protocol Template And Common Shape

- define the canonical structure every protocol document should follow
- make protocol docs consistent in how they express actors, triggers,
  preconditions, allowed mutations, required outputs, exit criteria, and
  handoff targets
- make the shared shape explicit about gate context, required review passes,
  review outcomes, and the structured contracts that carry those values
- keep protocol docs consuming already-defined skill attachments rather than
  redefining skills inline as protocol-local behavior
- keep protocols discoverable and reviewable as first-class workflow surfaces

### Task 2: Core Workflow Protocol Set

- define the initial shared protocols for:
  - planning
  - execution
  - review
  - rework
  - recovery
- define a reusable review-pass model for QA that distinguishes Code,
  Architecture, Security, and Product passes without turning those passes into
  separate roles, modes, or protocols
- treat protocols as workflow definitions that parent agents follow while
  embodying their roles, with specialists participating only through bounded
  delegation
- keep protocol ownership aligned with the parent-versus-specialist delegation
  boundary rather than letting specialists grow into parallel workflow owners
- make it explicit that protocols define gates, transitions, handoffs, and exit
  criteria rather than replacing the role or mode model

### Task 3: Delegation, Handoff, And Escalation Contracts

- define how work is delegated to specialists or other roles
- define what a valid handoff must communicate and require that it be expressed
  as a structured machine-readable contract rather than prose
- require completion and review contracts to carry the requested review passes
  and the resulting review outcome state explicitly
- define when escalation is required and what information must accompany it
- keep escalation inheriting the structural return-contract model rather than
  treating it as protocol-only improvisation
- make QA review enter from a structured `implementation_complete` handoff
  rather than from an ad hoc tool-invocation comment

### Task 4: Role And Mode Bindings

- bind the shared protocols to the project role and mode model
- bind the default review-pass requirements to the project gates:
  - `Task -> Story`: Code Pass
  - `Story -> Epic`: Architecture Pass and Security Pass
  - `Epic -> development`: Product Pass
- allow additional earlier passes only by risk or escalation rather than by
  duplicating the review model at each gate
- prevent protocol documents from becoming free-floating abstractions with no
  operational meaning in Context Atlas
- preserve the distinction between:
  - a protocol as workflow path
  - a role as accountability
  - a mode as execution state entered during protocol execution
- make it explicit that protocol steps and mode transitions are related but not
  one-to-one

## Sequencing

- define the shared protocol template and common structure
- define the initial workflow protocol set
- define delegation, handoff, and escalation contracts
- bind protocols back to the role and mode model

## Risks And Unknowns

- Protocol docs could duplicate role docs if they are written as actor-specific
  narratives instead of shared workflow definitions.
- Handoffs could remain too implicit if the required output contract is not
  precise enough.
- If handoff state is left conversational instead of structured, later
  automation and runtime materialization will be brittle.
- If escalation rules are vague, later runtime materialization will be hard to
  enforce consistently.
- Review passes could drift into pseudo-roles or pseudo-modes if the review
  model is not kept explicit.
- Gate-to-pass mapping could become inconsistent if the protocol docs do not
  state the default pass expectations clearly.

## Exit Criteria

- Context Atlas has a documented protocol model and a reusable protocol shape
- the initial shared workflow protocols are defined
- delegation, handoff, and escalation have explicit structured contract
  expectations
- the review protocol, review-pass model, and gate-to-pass bindings are
  explicit and internally coherent
- protocols are clearly bound to project roles and modes without collapsing the
  distinction between those layers
- the relationship between protocol execution and mode entry/transition is
  explicit enough to prevent later task-level drift
- the protocol layer has a reusable authoritative template and entrypoint
  instead of relying on planning docs to describe protocol shape ad hoc

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- protocol docs stay workflow-centered and do not become role-specific
  replacements or runtime prompt dumps
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge
- handoff and escalation expectations are explicit enough to support later
  runtime materialization and validation work
- inter-agent state transitions are defined as structured contracts so later QA
  automation does not depend on prose-only triggers
- the Story captures a stable distinction between review workflow, review
  passes, and gate-specific pass requirements so later Tasks do not reinvent
  review semantics ad hoc

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Story 4 - Context Atlas Mode Model](./story_4_context_atlas_mode_model.md)
- [Context Atlas Role Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Accountability Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Accountability-Matrix.md)
- [Context Atlas Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Context Atlas Mode Model](../../../Authoritative/Identity/AgenticDevelopment/Mode-Model.md)
- [Mode Transition Rules](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Rules.md)
- [Mode Mutation Matrix](../../../Authoritative/Identity/AgenticDevelopment/Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Mode-Matrix.md)
- [Mode Transition Graph](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Graph.md)
- [Delegation Model](../../../Authoritative/AgenticDevelopment/Delegation-Model.md)
- [Skill Attachment Model](../../../Authoritative/AgenticDevelopment/Skill-Attachment-Model.md)
- [Escalation Model](../../../Authoritative/AgenticDevelopment/Escalation-Model.md)
- [Protocols README](../../../Authoritative/AgenticDevelopment/Protocols/README.md)
- [Protocol Template](../../../Authoritative/AgenticDevelopment/Protocols/Protocol-Template.md)
- [Planning Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Planning-Protocol.md)
- [Execution Slice Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
- [Review Pass Model](../../../Authoritative/AgenticDevelopment/Protocols/Review-Pass-Model.md)
- [Review Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Review-Protocol.md)
- [Rework Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Rework-Protocol.md)
- [Recovery Protocol](../../../Authoritative/AgenticDevelopment/Protocols/Recovery-Protocol.md)
