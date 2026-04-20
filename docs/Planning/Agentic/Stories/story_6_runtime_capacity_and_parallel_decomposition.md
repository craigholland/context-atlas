---
id: context-atlas-agentic-story-6-runtime-capacity-and-parallel-decomposition
title: Story 6 - Runtime Capacity And Parallel Decomposition
summary: Defines how Context Atlas models available AI runtimes for planning and how decomposition should react to that capacity when shaping Stories, Tasks, and parallel work lanes.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [agentic-development, story, runtime-capacity, planning, decomposition]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ./story_5_protocol_model.md
  - ../../../Authoritative/AgenticDevelopment/Runtime-Capacity-Model.md
  - ../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md
supersedes: []
---

# Story 6 - Runtime Capacity And Parallel Decomposition

## Objective

Define the runtime-capacity model and the planning rules that should let
Context Atlas decompose work according to how many independent AI runtimes are
actually available for an Epic, Story, or Task.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Runtime Capacity Model](../../../Authoritative/AgenticDevelopment/Runtime-Capacity-Model.md)
- [Craig Architecture - Planning And Decomposition](../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- Current repository planning patterns around feature branches, task gating, and bounded parallel work

## Proposed Tasks

### Task 1: Runtime Capacity Model

- define what runtime capacity means at planning time
- distinguish planning capacity from live operational availability so the model
  does not confuse stable planning input with ephemeral runtime state
- define the portable fields that a planner should need before shaping parallel
  work

### Task 2: Machine-Readable Project Capacity Artifact

- define the project-specific machine-readable artifact that stores current
  planning capacity
- keep the artifact simple enough for a human operator to edit safely
- ensure the file can drive decomposition without becoming a hidden runtime
  scheduler

### Task 3: Parallel Decomposition Rules

- define how planners should identify:
  - base or blocking work that must happen first
  - independent work lanes that may happen in parallel
- ensure the number of planned parallel lanes does not exceed usable runtime
  capacity
- preserve Craig Architecture decomposition quality even when parallelism is
  available

### Task 4: Update And Validation Guidance

- define how runtime-capacity inputs should be reviewed, updated, and trusted
- make it explicit when the planning artifact should be read during Epic, Story,
  or Task decomposition
- position later validation work to catch stale or malformed capacity inputs

## Sequencing

- define the runtime-capacity model and boundary with live state
- introduce the machine-readable project artifact
- define the decomposition rules that consume that artifact
- define update and validation expectations for keeping the input trustworthy

## Risks And Unknowns

- Capacity could be mistaken for live orchestration if the model is too
  operational.
- Planners could over-parallelize work if the rules do not distinguish blocking
  work from independent lanes clearly enough.
- A machine-readable artifact could become stale quickly if update expectations
  are not explicit.

## Exit Criteria

- Context Atlas has a documented runtime-capacity model
- the project has a planned machine-readable capacity artifact shape
- decomposition guidance explains how capacity affects parallel Story and Task
  planning
- update and validation expectations are explicit enough to trust the artifact

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the Story preserves the distinction between planning capacity, live runtime
  availability, and workflow protocol state
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge
- any machine-readable capacity artifact introduced by the Story is documented
  well enough for later validation and human editing

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Runtime Capacity Model](../../../Authoritative/AgenticDevelopment/Runtime-Capacity-Model.md)
- [Craig Architecture - Planning And Decomposition](../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
