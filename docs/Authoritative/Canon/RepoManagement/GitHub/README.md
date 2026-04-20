---
id: repo-management-github-readme
title: GitHub RepoManagement Canon
summary: Defines the reusable GitHub-specific RepoManagement guidance that remains downstream of the portable canon and upstream of project-specific GitHub bindings.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, github, authoritative, provider-binding]
related:
  - ../README.md
  - ../Principal-Model.md
  - ../Authorization-Model.md
  - ../Operation-Model.md
  - ../Branch-Target-Policy-Model.md
  - ../Audit-Identity-Model.md
  - ./GitHub-App-Model.md
  - ./Pull-Request-Operation-Model.md
  - ./Branch-Protection-Model.md
  - ./Audit-Identity-Guidance.md
supersedes: []
---

# GitHub RepoManagement Canon

## Purpose

Define reusable GitHub-specific RepoManagement guidance without turning GitHub
mechanics into portable canon or into one project's binding.

## Scope

This directory refines the portable RepoManagement surface into GitHub's
specific mechanics for:

- GitHub Apps and bot principals
- pull request review and comment surfaces
- branch protection and merge enforcement
- GitHub-facing audit identity guidance

It does not define:

- a project's chosen GitHub App names
- a project's branch-specific merge policy
- a project's role-to-principal mapping

## Reading Order

1. this README
2. [GitHub-App-Model.md](./GitHub-App-Model.md)
3. [Pull-Request-Operation-Model.md](./Pull-Request-Operation-Model.md)
4. [Branch-Protection-Model.md](./Branch-Protection-Model.md)
5. [Audit-Identity-Guidance.md](./Audit-Identity-Guidance.md)

## Boundary Rules

- Stay in this directory when the guidance depends on GitHub concepts such as
  Apps, pull requests, rulesets, branch protection, or GitHub-visible bot
  identity.
- Move to `docs/Authoritative/Identity/RepoManagement/GitHub/` only when
  choosing which GitHub principals, branch-target rules, or audit names one
  project uses.
- Do not let reusable GitHub guidance become click-by-click setup folklore
  that will age faster than the policy itself.

## Related Artifacts

- [RepoManagement README](../README.md)
- [GitHub App Model](./GitHub-App-Model.md)
- [Pull Request Operation Model](./Pull-Request-Operation-Model.md)
- [Branch Protection Model](./Branch-Protection-Model.md)
- [Audit Identity Guidance](./Audit-Identity-Guidance.md)
