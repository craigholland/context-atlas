---
id: context-atlas-github-principal-binding-model
title: Principal Binding Model
summary: Defines the Context Atlas GitHub principal roster and the split between implementation, review, and branch-target-scoped merge principals.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, principals, bots]
related:
  - ./README.md
  - ./Operation-Matrix.md
  - ./Branch-Target-Policy.md
  - ../../AgenticDevelopment/Role-Authority-Matrix.md
supersedes: []
---

# Principal Binding Model

## Purpose

Define the Context Atlas GitHub principal roster.

## Scope

This document names the GitHub-facing principal families Context Atlas intends
to use and explains why merge authority is split by target class.

## Binding Decisions

### 1. Context Atlas Uses Stable GitHub-Visible Machine Principals

The project should use stable GitHub-visible machine principals for governed
repository actions rather than one shared generic bot identity.

### 2. The Initial Principal Roster Is

- `context-atlas-planner[bot]`
- `context-atlas-backend[bot]`
- `context-atlas-documentation-uat[bot]`
- `context-atlas-qa[bot]`
- `context-atlas-devops-task[bot]`
- `context-atlas-devops-story[bot]`
- `context-atlas-devops-epic[bot]`

This roster reflects the current delivery model:

- planning publication
- implementation publication
- governed QA review
- branch-target-scoped merge execution

### 3. Merge Principals Stay Split By Branch-Target Tier

Context Atlas keeps merge execution split across three DevOps principals so
that merge authority can remain narrower than a single global "may merge"
permission.

### 4. Runtime Instances Remain Separate From GitHub Principals

The runtime instance that performed work should be recorded separately from the
stable GitHub-visible principal, not embedded into the principal name itself.

### 5. Human Operators May Still Perform Manual Actions During Transition

Until the full automation path exists, human maintainers may still perform
manual GitHub actions.

That transitional reality does not change the target principal model defined
here.

## Constraints

- Principal names should stay stable across runs.
- Principal names should remain role-oriented and readable in PR history.
- Future additions should justify themselves by real authority differences.

## Non-Goals

- Define GitHub App registration details.
- Define the full operation matrix by itself.
- Define release principals beyond the current task/story/epic merge tiers.
