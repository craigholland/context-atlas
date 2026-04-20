---
id: context-atlas-github-binding-readme
title: Context Atlas GitHub Binding
summary: Defines GitHub as the chosen repository provider for Context Atlas and establishes the project-specific binding for principals, operations, branch-target policy, audit identity, and agentic integration.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, identity, bindings]
related:
  - ./Principal-Binding-Model.md
  - ./Operation-Matrix.md
  - ./Branch-Target-Policy.md
  - ./Audit-Identity-Model.md
  - ./Agentic-Integration-Model.md
  - ../../Context-Atlas-Agentic-Development-Profile.md
  - ../../Canon/AgenticDevelopment/Role-Authority-Matrix.md
  - ../../Canon/AgenticDevelopment/Gate-Review-Pass-Matrix.md
  - ../../../Canon/RepoManagement/README.md
  - ../../../Canon/RepoManagement/GitHub/README.md
supersedes: []
---

# Context Atlas GitHub Binding

## Purpose

Define GitHub as the chosen repository provider for Context Atlas and
establish the project-specific binding for principals, operations,
branch-target policy, audit identity, and agentic integration.

## Scope

This document governs the current Context Atlas GitHub policy surface.

It does not redefine the portable RepoManagement canon, and it does not
replace the project role or protocol model.

## Binding Decisions

### 1. Context Atlas Uses GitHub As Its Current Repository Provider

GitHub is the current repository provider bound by Context Atlas for branch
delivery, pull-request review, and merge execution.

That is a project binding, not a portable RepoManagement claim.

### 2. This Binding Is Downstream Of Both RepoManagement And AgenticDevelopment

The Context Atlas GitHub binding must inherit meaning from:

- the portable RepoManagement canon
- the reusable GitHub provider canon
- the Context Atlas role, protocol, and gate-review-pass bindings

GitHub-facing project policy should not be invented in runtime materialization
docs or informal PR habits.

### 3. GitHub Pull Requests Are The Current Review Surface

For Context Atlas, the active GitHub PR surface is the current materialized
surface where:

- implementation work becomes reviewable
- QA publishes findings and review outcomes
- merge readiness is discussed and recorded

### 4. GitHub Merge Authority Is Branch-Target Scoped

Context Atlas does not treat GitHub merge rights as one global permission.

Merge authority is split by branch-target class and bound explicitly through
project principals and branch-target policy.

### 5. GitHub Audit Identity Must Stay Human-Readable

Closed PRs and merged branches should make it easy for a human reader to see:

- which principal implemented
- which principal reviewed
- which principal merged

Runtime instance identity should remain separately structured.

### 6. Runtime Materialization Does Not Create GitHub Authority

Codex-facing runtime files may help exercise GitHub operations, but they do not
authorize those operations.

GitHub authority must remain defined in this binding layer.

## Reading Order

1. this README
2. [Principal-Binding-Model.md](./Principal-Binding-Model.md)
3. [Operation-Matrix.md](./Operation-Matrix.md)
4. [Branch-Target-Policy.md](./Branch-Target-Policy.md)
5. [Audit-Identity-Model.md](./Audit-Identity-Model.md)
6. [Agentic-Integration-Model.md](./Agentic-Integration-Model.md)

## Related Artifacts

- [Principal Binding Model](./Principal-Binding-Model.md)
- [Operation Matrix](./Operation-Matrix.md)
- [Branch-Target Policy](./Branch-Target-Policy.md)
- [Audit Identity Model](./Audit-Identity-Model.md)
- [Agentic Integration Model](./Agentic-Integration-Model.md)
- [Context Atlas Agentic Development Profile](../../Context-Atlas-Agentic-Development-Profile.md)
- [Role Authority Matrix](../../Canon/AgenticDevelopment/Role-Authority-Matrix.md)
- [Gate Review Pass Matrix](../../Canon/AgenticDevelopment/Gate-Review-Pass-Matrix.md)
- [RepoManagement README](../../../Canon/RepoManagement/README.md)
- [GitHub RepoManagement Canon](../../../Canon/RepoManagement/GitHub/README.md)

