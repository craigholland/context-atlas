---
id: context-atlas-github-operation-matrix
title: Operation Matrix
summary: Defines which Context Atlas GitHub principals may push, open PRs, comment, review, merge, and mutate workflow or release surfaces.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, operations, permissions]
related:
  - ./Principal-Binding-Model.md
  - ./Branch-Target-Policy.md
  - ../../Canon/AgenticDevelopment/Role-Authority-Matrix.md
supersedes: []
---

# Operation Matrix

## Purpose

Define which Context Atlas GitHub principals may perform which operation
families.

## Operation Matrix

| Principal | Push Scoped Branches | Open/Update PRs | Comment On PRs | Submit Review | Merge Task -> Story | Merge Story -> Epic | Merge Epic -> development | Mutate Workflows | Create Release/Tag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `context-atlas-planner[bot]` | yes | yes | yes | no | no | no | no | no | no |
| `context-atlas-backend[bot]` | yes | yes | yes | no | no | no | no | no | no |
| `context-atlas-documentation-uat[bot]` | yes | yes | yes | no | no | no | no | no | no |
| `context-atlas-qa[bot]` | no | no | yes | yes | no | no | no | no | no |
| `context-atlas-devops-task[bot]` | no | no | yes | no | yes | no | no | no | no |
| `context-atlas-devops-story[bot]` | no | no | yes | no | no | yes | no | no | no |
| `context-atlas-devops-epic[bot]` | no | no | yes | no | no | no | yes | no | no |

## Binding Decisions

### 1. Implementation Principals Publish Work But Do Not Merge

Planner, Backend, and Documentation/UAT principals may publish scoped branch
work and update PR state for their owned work, but they do not merge those PRs
by default.

### 2. QA Publishes Review But Does Not Merge

The QA principal may comment and submit governed review on the GitHub PR
surface, but it does not merge work by default.

### 3. Merge Execution Is Split Across DevOps Principals

Merge execution is split across target tiers:

- task into story
- story into epic
- epic into `development`

### 4. Workflow And Release Mutation Remain Unbound Here

This initial binding does not yet assign routine workflow mutation or release
tag execution to an active GitHub machine principal.

Those surfaces remain future work unless a later binding makes them explicit.

## Constraints

- This matrix should stay aligned with the role-authority model.
- Branch-target merge rights should remain narrower than broad implementation
  publication rights.
- Later automation should consume this matrix rather than inventing a second
  permission table.

