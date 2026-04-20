---
id: context-atlas-repo-management-bindings-readme
title: Context Atlas RepoManagement Bindings
summary: Defines the project-specific RepoManagement binding surface for Context Atlas and points readers to the chosen provider binding.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, identity, github]
related:
  - ./GitHub/README.md
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../../RepoManagement/README.md
supersedes: []
---

# Context Atlas RepoManagement Bindings

## Purpose

Define the project-specific RepoManagement binding surface for Context Atlas.

## Scope

This directory is where Context Atlas binds the portable RepoManagement canon
and reusable provider guidance into one project-specific policy surface.

It does not replace the portable RepoManagement canon, and it does not replace
the agentic role or protocol canon.

## Current Binding

Context Atlas currently binds RepoManagement through:

- [GitHub/README.md](./GitHub/README.md)

That GitHub binding is the project-specific home for:

- chosen principals
- operation scopes
- branch-target merge policy
- GitHub-facing audit identity
- role/protocol integration hooks for repository work

## Reading Order

For most readers:

1. [../../RepoManagement/README.md](../../RepoManagement/README.md)
2. [../../RepoManagement/GitHub/README.md](../../RepoManagement/GitHub/README.md)
3. [GitHub/README.md](./GitHub/README.md)

## Boundary Rules

- portable repo-management meaning belongs in `docs/Authoritative/RepoManagement/`
- provider-specific reusable GitHub meaning belongs in
  `docs/Authoritative/RepoManagement/GitHub/`
- Context Atlas-specific GitHub policy belongs here
