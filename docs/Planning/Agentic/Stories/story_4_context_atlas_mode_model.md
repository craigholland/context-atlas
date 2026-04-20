---
id: context-atlas-agentic-story-4-context-atlas-mode-model
title: Story 4 - Context Atlas Mode Model
summary: Defines the project-specific execution modes that Context Atlas uses and the entry, exit, and mutation constraints attached to those modes.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, modes, workflow-state, governance]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ./story_3_context_atlas_role_model.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Agent-Binding-Model.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Mode-Model.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Rules.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Mode-Mutation-Matrix.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Mode-Matrix.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Graph.md
  - ../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 4 - Context Atlas Mode Model

## Objective

Define the project-specific mode model for Context Atlas so execution state is
governed explicitly instead of being hidden inside ad hoc prompt wording or
role-specific habits, and so it is clear that modes are execution states
entered while an agent participates in a workflow protocol rather than
alternate role definitions.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Context Atlas Role Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Context Atlas Role-Agent Binding Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Agent-Binding-Model.md)
- [Context Atlas Mode Model](../../../Authoritative/Identity/AgenticDevelopment/Mode-Model.md)
- [Mode Transition Rules](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Rules.md)
- [Mode Mutation Matrix](../../../Authoritative/Identity/AgenticDevelopment/Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Mode-Matrix.md)
- [Mode Transition Graph](../../../Authoritative/Identity/AgenticDevelopment/Mode-Transition-Graph.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
- Current repository workflow expectations around planning, implementation, review, rework, recovery, and release-oriented work

## Proposed Tasks

### Task 1: Canonical Mode Set

- define the initial project mode set for Context Atlas
- distinguish execution state from role accountability so modes do not become
  alternate role names
- define modes in a way that allows the same mode to appear inside multiple
  protocols rather than treating each protocol step as a unique mode
- keep the initial mode set bounded enough to govern clearly

### Task 2: Entry, Exit, And Allowed Mutations

- define when a mode may be entered or exited
- define which classes of artifacts may be mutated in each mode
- make mode boundaries precise enough to guide later protocol and runtime
  materialization work

### Task 3: Role Applicability And Constraints

- define which roles may operate in which modes
- identify where a role may enter multiple modes but with different mutation or
  authority constraints
- prevent mode rules from being copied redundantly into each role definition

### Task 4: Transition Model

- define the allowed transitions between modes
- make rework, review, recovery, and release-oriented movement explicit rather
  than implied
- make it explicit that a protocol may contain several steps in the same mode
  and that not every protocol step implies a mode transition
- position the protocol story to build on a stable mode state model

## Sequencing

- define the initial mode set
- define entry, exit, and mutation rules for each mode
- bind roles to the mode model
- lock the allowed transitions before workflow protocols are written

## Risks And Unknowns

- Modes could become too numerous if every workflow nuance becomes its own mode.
- The Story could duplicate role definitions if role applicability is not kept
  separate from role accountability.
- If allowed mutations are vague, later runtime materialization will be hard to
  validate or enforce consistently.

## Exit Criteria

- Context Atlas has an explicit project mode set
- each mode has entry, exit, and mutation rules
- role-to-mode applicability is documented without collapsing the distinction
  between role and mode
- the relationship between protocol execution and mode entry/transition is
  explicit
- later protocol docs can reference the mode model as a stable workflow-state
  layer

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the mode model stays project-specific and workflow-oriented rather than
  drifting into runtime-specific file conventions
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives `@codex review`, and any review findings are
  resolved on that same feature branch before human merge
- mode definitions include enough transition detail to support later protocol
  and validation work without prematurely becoming task-level implementation

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Context Atlas Role Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Context Atlas Role-Agent Binding Model](../../../Authoritative/Identity/AgenticDevelopment/Role-Agent-Binding-Model.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
