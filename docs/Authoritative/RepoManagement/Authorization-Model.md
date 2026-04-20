---
id: repo-authorization-model
title: Authorization Model
summary: Defines the portable authorization model for repository principals, including least privilege, target scoping, and provider-enforced boundaries.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, authorization, least-privilege, permissions]
related:
  - ./README.md
  - ./Principal-Model.md
  - ./Operation-Model.md
  - ./Branch-Target-Policy-Model.md
supersedes: []
---

# Authorization Model

## Purpose

Define the portable authorization model for repository principals.

## Scope

This document governs how principal permissions should be scoped and enforced.

It does not define provider-specific permission names or one project's
principal roster.

## Binding Decisions

### 1. Authorization Should Be Provider-Enforced, Not Prompt-Only

Meaningful repository boundaries should be enforced through provider-level
permissions, scoped credentials, or provider policy wherever possible.

Prompt instructions alone are not a sufficient long-term authorization model.

### 2. Least Privilege Should Be The Default

Each principal should receive only the operations and targets required for its
governed purpose.

### 3. Authorization Should Bind Operations And Targets Together

Repository authorization is not just "may merge" or "may comment."

The model should bind:

- which operation may occur
- against which target class
- under which workflow or gate conditions

### 4. Review, Merge, Release, And Workflow Mutation Should Stay Distinct

These operation families should remain separately scoped:

- review and findings publication
- merge execution
- release/tag execution
- repository workflow or automation mutation

### 5. Revocable And Short-Lived Access Is Preferred

Project or provider bindings should prefer credential mechanisms that can be
revoked cleanly and that avoid unnecessary long-lived secrets.

### 6. Human Override Should Be Explicit

When a human operator acts outside the normal machine-principal path, that
override should remain explicit rather than being mistaken for the normal
automation policy.

## Constraints

- Authorization models should remain auditable.
- Target scoping should be visible at the project-binding layer.
- Provider permissions should remain downstream of this portable model.

## Non-Goals

- Define provider-specific permission names.
- Define a project's exact merge gates.
- Choose one credential technology.
