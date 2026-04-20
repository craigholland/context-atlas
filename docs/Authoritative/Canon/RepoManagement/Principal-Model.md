---
id: repo-principal-model
title: Principal Model
summary: Defines the portable model for repository principals and the stable distinction between visible principals, runtime instances, and authorization scope.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, principals, authorization, identities]
related:
  - ./README.md
  - ./RepoManagement-Glossary.md
  - ./Authorization-Model.md
  - ./Audit-Identity-Model.md
supersedes: []
---

# Principal Model

## Purpose

Define the portable model for repository principals.

## Scope

This document defines what a repository principal is, how principal families
should be separated, and how visible principals differ from runtime instances.

It does not choose provider-specific credential mechanisms or project-specific
principal names.

## Binding Decisions

### 1. Repo Operations Should Flow Through Explicit Principals

Repository actions should be performed through explicit principals rather than
through anonymous shared credentials or hidden runtime access.

### 2. Visible Principals And Runtime Instances Must Remain Distinct

The stable principal that appears in provider history should remain separate
from the transient runtime instance that happened to execute the work.

This keeps audit history readable while still allowing deeper traceability.

### 3. Automated Flows Should Prefer Machine Principals

When automation performs repository operations, the preferred model is a
machine principal with explicit provider-level authorization rather than a
human account with repurposed long-lived credentials.

### 4. Principal Families Should Mirror Real Authority Boundaries

Repository principals should be separated when they represent meaningfully
different authority surfaces, such as:

- implementation mutation
- governed review
- merge execution
- release execution

### 5. Principal Separation Should Be Stronger Than Prompt Separation

If two roles must not perform the same repository action, that boundary should
ideally be enforced by separate principals or separate provider permissions,
not only by instructions in a prompt.

### 6. Project Bindings May Refine One Portable Model Into Several Principals

The portable model does not require one principal per role, or one role per
principal.

Project bindings may split or group principals as needed, but they should
justify that choice against real authorization boundaries rather than
convenience alone.

## Constraints

- Principals should be stable enough for audit history.
- Principal families should stay narrower than "everything the automation can
  do."
- Runtime instance identity should never replace stable principal identity.

## Non-Goals

- Define provider-specific setup steps.
- Choose one project's bot names.
- Define one mandatory principal topology for every system.
