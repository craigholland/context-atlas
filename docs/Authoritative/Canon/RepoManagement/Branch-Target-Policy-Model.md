---
id: repo-branch-target-policy-model
title: Branch-Target Policy Model
summary: Defines the portable model for scoping merge authority by source and target branch classes instead of treating merge rights as one global permission.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, branch-policy, merges, governance]
related:
  - ./README.md
  - ./Authorization-Model.md
  - ./Operation-Model.md
supersedes: []
---

# Branch-Target Policy Model

## Purpose

Define the portable model for scoping merge authority by source and target
branch classes.

## Scope

This document defines how branch-target policy should be reasoned about before
one project or provider chooses exact branch names or protection settings.

## Binding Decisions

### 1. Merge Authority Should Be Target-Scoped

Merge authority should not be modeled as one generic "may merge" permission.

It should be scoped by target branch class and, where helpful, by source
branch class as well.

### 2. Branch Classes Should Reflect Workflow Meaning

Portable branch classes may include categories such as:

- task
- story
- epic
- integration
- release

Projects may refine or rename these, but the portable idea is that branch
policy should follow workflow meaning rather than arbitrary branch names alone.

### 3. Branch-Target Policy Should Bind Gate State To Merge Rights

A branch-target policy should state:

- which source class is permitted
- which target class is permitted
- which review or gate state must exist first
- which principal or principal family may execute the merge

### 4. Higher-Tier Targets Should Usually Have Narrower Authority

As target branches become more integrative or release-oriented, merge
authority should usually narrow rather than widen.

### 5. Direct Push And Merge Policy Should Remain Distinct

Branch-target policy should distinguish:

- direct push rights
- merge execution rights
- emergency or explicit human override paths

## Constraints

- Project bindings should expose branch-target policy explicitly.
- Provider enforcement should remain downstream of this model.
- Branch-target policy should remain readable without knowing one provider's
  rule syntax.

## Non-Goals

- Define exact branch names for one repository.
- Define one mandatory branch taxonomy for all projects.
