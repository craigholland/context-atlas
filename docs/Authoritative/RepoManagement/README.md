---
id: repo-management-readme
title: Repo Management
summary: Defines the portable, provider-agnostic repo-management canon for principals, authorization, operations, branch-target policy, and audit identity.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, authoritative, principals, authorization, operations]
related:
  - ./RepoManagement-Glossary.md
  - ./Principal-Model.md
  - ./Authorization-Model.md
  - ./Operation-Model.md
  - ./Branch-Target-Policy-Model.md
  - ./Audit-Identity-Model.md
  - ./GitHub/README.md
  - ../AgenticDevelopment/README.md
  - ../Architecture/README.md
supersedes: []
---

# Repo Management

## Purpose

Define the portable repo-management canon for how governed systems interact
with external repository providers.

This surface exists so concepts like principals, permissions, review actions,
merge authority, branch-target policy, and audit identity have one portable
home instead of being buried inside project bindings or runtime prompts.

## Scope

This directory defines:

- portable repo-management vocabulary
- portable models for principals, authorization, operations, branch-target
  policy, and audit identity
- reusable provider-specific supplements that remain downstream of the
  portable canon but upstream of any one project binding

It does not define:

- an application's chosen provider
- an application's chosen principal roster
- an application's branch-specific merge policy
- runtime-specific prompt or tool behavior

## Start Here

If you are new to this canon, read in this order:

1. this README
2. [RepoManagement-Glossary.md](./RepoManagement-Glossary.md)
3. [Principal-Model.md](./Principal-Model.md)
4. [Authorization-Model.md](./Authorization-Model.md)
5. [Operation-Model.md](./Operation-Model.md)
6. [Branch-Target-Policy-Model.md](./Branch-Target-Policy-Model.md)
7. [Audit-Identity-Model.md](./Audit-Identity-Model.md)
8. a provider-specific surface such as [GitHub/README.md](./GitHub/README.md)

## What Lives Here

The portable RepoManagement canon should define:

- what a repository principal is
- what authorization scope means
- what operation families matter
- how branch-target policy should constrain merge authority
- how audit identity should stay readable across humans, runtimes, and bot
  principals

The initial canon surface is centered on:

- [RepoManagement-Glossary.md](./RepoManagement-Glossary.md)
- [Principal-Model.md](./Principal-Model.md)
- [Authorization-Model.md](./Authorization-Model.md)
- [Operation-Model.md](./Operation-Model.md)
- [Branch-Target-Policy-Model.md](./Branch-Target-Policy-Model.md)
- [Audit-Identity-Model.md](./Audit-Identity-Model.md)
- [GitHub/README.md](./GitHub/README.md)

## Boundary Rules

- Stay in this directory when defining provider-agnostic repo-management
  meaning.
- Move into a provider subdirectory when a concept depends on one provider's
  mechanics or terminology.
- Move into `docs/Authoritative/Identity/RepoManagement/` only when binding
  these concepts to one project's chosen provider, principal roster, branch
  policy, or audit names.
- Do not define project-specific GitHub bot names, merge rights, or review
  triggers here.

## Neighboring Canon

The most relevant adjacent surfaces are:

- [../AgenticDevelopment/README.md](../AgenticDevelopment/README.md): portable
  agentic-development canon for roles, protocols, modes, skills, and
  handoffs
- [../Architecture/README.md](../Architecture/README.md): reusable Craig
  Architecture philosophy and planning/decomposition guidance

RepoManagement is a sibling canon to AgenticDevelopment, not a child of it.
AgenticDevelopment defines the actor and workflow model. RepoManagement
defines how those actors interact with external repository systems.
