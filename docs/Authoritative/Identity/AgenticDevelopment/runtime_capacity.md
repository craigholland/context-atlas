---
id: context-atlas-runtime-capacity-guidance
title: Context Atlas Runtime Capacity Guidance
summary: Defines how the Context Atlas runtime-capacity artifact should be updated and interpreted so decomposition uses one trustworthy planning-capacity source.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, runtime-capacity, planning]
related:
  - ./runtime_capacity.yaml
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../../AgenticDevelopment/Runtime-Capacity-Model.md
  - ../../AgenticDevelopment/Parallel-Decomposition-Model.md
supersedes: []
---

# Context Atlas Runtime Capacity Guidance

## Purpose

Define how Context Atlas should update and interpret the runtime-capacity
artifact.

## Scope

This document governs the human-facing update and trust model for:

- [runtime_capacity.yaml](./runtime_capacity.yaml)

It does not define live worker scheduling or runtime-materialization behavior.

## Update Guidance

### 1. The Artifact Should Be Updated Intentionally

`runtime_capacity.yaml` should be updated only when the planning assumptions for
Context Atlas actually change.

Typical triggers include:

- the total number of available runtimes changes
- one or more runtimes become reserved for other work
- specialization or platform differences materially affect planning
- the decomposition policy for safe parallel work changes

### 2. Normal Ownership Lives With Planning Leadership Or A Human Operator

The normal maintainers of the artifact are:

- the `Planner/Decomp` role when preparing or refreshing decomposition
- a human operator when the available planning capacity changes outside a
  planning session

Implementation roles should not quietly edit the artifact as a side effect of
ordinary code work.

### 3. The Artifact Should Be Read Before Parallel Planning

Planners should read the artifact before finalizing:

- Epic-to-Story parallel fan-out
- Story-to-Task fan-out
- Task-to-PR parallel slice decisions

If no bounded parallelism is being considered, the planner does not need to
force artifact usage into the flow.

### 4. The Artifact Is Trusted As Planning Input, Not As Live State

The YAML file is a governed planning snapshot.

It should be trusted for decomposition even though real-world runtime
availability may fluctuate afterward.

If live conditions change materially, the correct response is usually to update
the planning artifact intentionally rather than letting ad hoc runtime state
become the new hidden source of truth.

## Constraints

- The guidance should remain simple enough for a human to follow without extra
  tooling.
- Artifact updates should be rare, intentional, and reviewable.
- The artifact should remain a planning aid, not a scheduler.

## Non-Goals

- Replace live operational monitoring.
- Encode queue state, workload state, or PR state.
- Automatically assign work to specific runtimes.

## Related Artifacts

- [Context Atlas Runtime Capacity Artifact](./runtime_capacity.yaml)
- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Runtime Capacity Model](../../AgenticDevelopment/Runtime-Capacity-Model.md)
- [Parallel Decomposition Model](../../AgenticDevelopment/Parallel-Decomposition-Model.md)
