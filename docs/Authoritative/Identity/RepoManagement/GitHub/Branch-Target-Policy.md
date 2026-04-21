---
id: context-atlas-github-branch-target-policy
title: Branch-Target Policy
summary: Defines the Context Atlas GitHub branch-target policy for task, story, and epic merges, including required review passes and merge principals.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, branch-policy, merges]
related:
  - ./Principal-Binding-Model.md
  - ./Operation-Matrix.md
  - ../../AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md
supersedes: []
---

# Branch-Target Policy

## Purpose

Define the Context Atlas GitHub branch-target policy.

## Policy Matrix

| Source Class | Target Class | Typical Structured Intake | Required Review Passes | Permitted Merge Principal |
| --- | --- | --- | --- | --- |
| `task` | `story` | `implementation_complete` with `scope_level: task` | `code` | `context-atlas-devops-task[bot]` |
| `story` | `epic` | `implementation_complete` with `scope_level: story` | `architecture`, `security` | `context-atlas-devops-story[bot]` |
| `epic` | `development` | `implementation_complete` with `scope_level: epic` | `product` | `context-atlas-devops-epic[bot]` |

## Binding Decisions

### 1. Task Merges Are Story-Bounded

Task feature branches should merge only into their intended Story branch, and
that merge should remain downstream of the required `code` review pass.

### 2. Story Merges Are Epic-Bounded

Story branches should merge only into the active Epic branch, and that merge
should remain downstream of the required `architecture` and `security` review
passes.

### 3. Epic Merges Are development-Bounded

The active Epic branch should merge into `development` only after the required
`product` pass indicates readiness.

### 4. Merge Rights Follow The Target Tier

The permitted merge principal changes with the target tier rather than staying
constant across all merge classes.

### 5. Release Branch Policy Is Not Yet Bound Here

This document governs the current task/story/epic delivery ladder only.

Release-path policy can be added later as a separate higher-tier binding when
the project is ready to automate that path.

## Constraints

- Human maintainers may still execute the merge manually during transition, but
  this document defines the target governed policy surface.
- Later automation should treat this matrix as the branch-target source of
  truth for the current ladder.


