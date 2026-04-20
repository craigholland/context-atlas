---
id: craig-runtime-capacity-model
title: Runtime Capacity Model
summary: Defines the portable planning-time concept of runtime capacity and keeps it distinct from live operational availability, workflow state, and scheduler behavior.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, runtime-capacity, planning, decomposition, parallelism]
related:
  - ./Boundary-Model.md
  - ../Architecture/Craig-Architecture-Planning-And-Decomposition.md
supersedes: []
---

# Runtime Capacity Model

## Purpose

Define the portable planning-time concept of runtime capacity.

## Scope

This document governs how agentic-development systems should describe available
execution capacity for planning and decomposition.

It does not define project-specific capacity values, live runtime state, or
environment-specific worker discovery.

## Binding Decisions

### 1. Runtime Capacity Is A Planning Input

Runtime capacity is a planning-time statement of how much independent execution
capacity may be assigned safely during decomposition.

It exists so planners can shape work into realistic parallel lanes before
implementation begins.

### 2. Runtime Capacity Is Distinct From Live Operational Availability

Runtime capacity describes the stable planning input a planner should use when
decomposing work.

It is not the same thing as:

- moment-by-moment runtime availability
- current queue depth or scheduler state
- protocol state such as who currently owns a handoff

Those concerns may matter operationally, but they should not replace the
planning-capacity model.

### 3. Runtime Capacity Is An Upper Bound, Not A Throughput Mandate

Capacity defines the maximum number of independent work lanes that may be
planned confidently.

It does not require planners to saturate all available capacity on every Epic,
Story, or Task.

Planners should still prefer deliberate sequencing when:

- base or blocking work must happen first
- available work is not truly independent
- forcing parallelism would damage architectural quality

### 4. The Model Must Stay Small Enough For Human Reasoning

The portable concept model should remain small enough that a human planner can
reason about it quickly.

At minimum, a planner should be able to answer:

- how much total planning capacity exists
- how much of that capacity is reserved or unavailable for general planning
- how much usable capacity remains for parallel work lanes
- whether any capacity profiles or specialization constraints materially affect
  planning

### 5. Heterogeneous Capacity Should Remain A Planning Constraint

Some systems may have runtimes with different capabilities or specialization.

When that matters, the capacity model should treat those differences as
planning constraints on eligible work lanes rather than as a hidden scheduler.

### 6. Capacity Should Be Read At Decomposition Boundaries

Runtime capacity is relevant when planners shape:

- Epic-to-Story decomposition
- Story-to-Task decomposition
- Task-to-PR fan-out when parallel PR slices are being considered

That does not mean every planning step must parallelize aggressively.

It means the planner should have one stable capacity input before deciding how
much parallel structure is safe.

The normal consumption rule is:

- identify base or blocking work first
- read the governed capacity input
- bound any proposed parallel fan-out by usable planning capacity
- choose less than the available ceiling when architectural independence is weak

### 7. The Portable Model Must Stay Vendor-Agnostic

The portable runtime-capacity concept must remain valid regardless of whether
the downstream environment uses Codex, Claude, or another execution system.

Project bindings may later map the model onto concrete runtime platforms, but
the concept itself should not assume one vendor or discovery convention.

### 8. Runtime Capacity Should Be Governed Like Other Planning Inputs

When a project chooses to maintain explicit runtime-capacity input, that input
should be treated as governed planning data rather than as ad hoc
conversational context.

That means:

- planners should read one authoritative capacity source
- later bindings should make update expectations explicit
- live queue state or transient availability should not silently override the
  governed planning input during decomposition

### 9. Downstream Bindings Should Choose One Machine-Readable Source

When a project decides to materialize runtime-capacity input, it should expose
that planning input through one authoritative machine-readable artifact.

That artifact should be:

- easy for a human operator to inspect
- simple enough to edit intentionally
- explicit enough that later validation can reason about its structure

Projects should avoid scattering planning-capacity truth across multiple
uncoordinated notes, prompts, or runtime-specific state files.

### 10. Validation Should Focus On Structural Trustworthiness

When projects validate a runtime-capacity artifact, the first validation target
should be structural trustworthiness.

Typical checks include:

- required fields are present
- values are well-formed
- numeric relationships remain internally coherent
- declared policy fields stay within the expected schema

Those checks should not claim to prove real-time runtime availability.

## Constraints

- Runtime capacity should remain a planning concept rather than an operational
  scheduler model.
- The model should stay compact enough that later project-specific artifacts
  remain editable by humans.
- Capacity semantics should stay separate from role, mode, protocol, or live
  workflow ownership state.

## Non-Goals

- Define current capacity values for a particular project.
- Define live runtime scheduling or queueing behavior.
- Require planners to maximize parallelism mechanically.
- Define environment-specific config files or folder layouts.

## Related Artifacts

- [Boundary Model](./Boundary-Model.md)
- [Craig Architecture - Planning And Decomposition](../Architecture/Craig-Architecture-Planning-And-Decomposition.md)
