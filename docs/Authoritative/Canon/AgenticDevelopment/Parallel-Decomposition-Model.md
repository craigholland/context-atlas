---
id: craig-parallel-decomposition-model
title: Parallel Decomposition Model
summary: Defines the portable planning rules for separating base work from independent parallel lanes while keeping decomposition bounded by real runtime capacity and architectural independence.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, decomposition, parallelism, planning, runtime-capacity]
related:
  - ./Runtime-Capacity-Model.md
  - ../Architecture/Craig-Architecture-Planning-And-Decomposition.md
supersedes: []
---

# Parallel Decomposition Model

## Purpose

Define the portable planning rules for separating base work from independent
parallel lanes.

## Scope

This document governs how planners should shape work when runtime capacity
allows bounded parallelism.

It does not define project-specific role bindings, protocol ownership, or live
runtime scheduling behavior.

## Binding Decisions

### 1. Base Work Must Be Identified Before Parallel Fan-Out

Planners should first identify any base or blocking work that must exist before
downstream work can proceed safely.

Typical examples include:

- foundational canon or terminology work
- shared boundary or contract decisions
- common infrastructure or schema work
- workflow or artifact definitions that later lanes depend on

If that work is genuinely blocking, it should not be parallelized just because
capacity exists.

### 2. Parallel Lanes Must Represent Real Independence

A parallel lane is a bounded workstream that can move forward without
reconstructing state from another not-yet-finished lane.

Lanes are only valid when they are independent enough that:

- architectural boundaries remain legible
- ownership stays clear
- later merge and review surfaces do not collapse into one hotspot

### 3. Runtime Capacity Bounds Lane Count

Planners should not propose more simultaneous independent lanes than the
governed planning-capacity input supports.

Capacity therefore acts as a ceiling on parallel fan-out, not as proof that
parallel fan-out is wise.

### 4. Under-Utilizing Capacity Is Sometimes Correct

It is valid to plan fewer parallel lanes than the available capacity when:

- the remaining work is not truly independent
- the resulting review or merge burden would be too concentrated
- architectural clarity would be harmed by forced concurrency

Good decomposition should prefer coherence over capacity saturation.

### 5. Lane Independence Must Be Re-Evaluated At Each Level

Parallel decomposition should be reconsidered at:

- Epic to Story
- Story to Task
- Task to PR

Work that is independent at one level may still need deliberate sequencing at
another level.

### 6. Parallel Planning Must Preserve Reviewability

Parallel lanes should remain bounded enough that later review gates still have
coherent surfaces to assess.

If planning many small lanes causes later Story, Epic, or release review to
collapse into one tangled surface, the decomposition was not actually healthy.

### 7. Capacity Should Inform Sequencing, Not Replace Judgment

The planner should use runtime capacity to shape the plan, but architectural
judgment still decides:

- what is base work
- what is safe to run in parallel
- what should remain sequential
- when a lane split would create more merge risk than delivery value

### 8. The Planner Should Read Capacity Before Proposing Parallel Lanes

When a project maintains a governed planning-capacity artifact, the planner
should read that input before proposing parallel lane counts.

That read should happen before the planner finalizes:

- Story fan-out from an Epic
- Task fan-out from a Story
- parallel PR fan-out from a Task

### 9. Capacity Consumption Should Be Narrow And Explicit

The planner should use the capacity input to answer a narrow question:

`How many independent lanes may be planned safely at this level?`

The capacity input should not be treated as if it answers:

- who is currently free right now
- which queue should run next
- which exact runtime instance must receive a lane

Those are operational questions, not decomposition questions.

## Constraints

- Base work should be identified before parallel fan-out is proposed.
- Parallel lanes should stay bounded by both capacity and architectural
  independence.
- The model should remain portable and should not assume one runtime vendor or
  scheduler.

## Non-Goals

- Define project-specific branch names or role assignments.
- Define live dispatcher or queueing behavior.
- Require planners to use every available runtime lane.

## Related Artifacts

- [Runtime Capacity Model](./Runtime-Capacity-Model.md)
- [Craig Architecture - Planning And Decomposition](../Architecture/Craig-Architecture-Planning-And-Decomposition.md)
