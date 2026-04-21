---
id: release-0-1-1
title: Release 0.1.1
summary: Records the first post-MVP hardening release of Context Atlas, covering the new portable canon, project bindings, repo-management model, and current operational boundaries.
doc_class: releases
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: superseded
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [releases, post-mvp, version-0-1-1, agentic-development, repo-management]
related:
  - ./release_0_1_2.md
  - ./release_0_1_0.md
  - ../Reviews/MVP/mvp_readiness_assessment.md
  - ../Guides/README.md
  - ../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ../Authoritative/Identity/RepoManagement/GitHub/README.md
  - ../../README.md
supersedes:
  - ./release_0_1_0.md
---

# Release 0.1.1

## Context

This document records the first post-MVP hardening release of Context Atlas.

`0.1.1` does not replace the `MVP Ready` engine established in `0.1.0`. It
packages the next layer of operational and governance work around that engine
so the repository has a clearer portable canon, a cleaner project-binding
surface, and a more explicit model for agentic development and repository
operations.

This release is intentionally more about governed structure than about adding a
new end-user workflow. It captures how Context Atlas now explains:

- portable canon versus project-specific identity
- agentic roles, skills, modes, protocols, and runtime capacity
- repository principals, permissions, review surfaces, and merge policy
- drift control and change-management expectations for those new surfaces

## Shipped Capabilities

### Canon And Identity Split

`0.1.1` introduces a clearer top-tier authoritative structure:

- `docs/Authoritative/Canon/` for portable cross-project canon
- `docs/Authoritative/Identity/` for Context Atlas-specific bindings

That split makes it easier to reuse the Craig Architecture, Agentic
Development, RepoManagement, and Ontology surfaces without mixing them together
with Context Atlas-specific operational choices.

### Portable Agentic Development Canon

`0.1.1` ships a real portable canon for agentic development under
`docs/Authoritative/Canon/AgenticDevelopment/`, including:

- glossary and boundary definitions
- parent-agent, specialist, and skill-composition rules
- role archetypes
- mode model
- review-pass-aware protocol canon
- runtime-capacity and parallel-decomposition guidance
- platform-materialization and template models
- drift, validation, and change-management models

That canon is intentionally runtime-agnostic. It defines the concepts and
constraints without tying them to a single AI environment.

### Context Atlas Agentic Bindings

`0.1.1` also adds the Context Atlas-specific binding layer for those concepts
under `docs/Authoritative/Identity/AgenticDevelopment/`.

That binding now makes explicit:

- the project role model
- role accountabilities and authorities
- role-to-parent binding
- mode transitions and mutation rules
- gate-to-review-pass mapping
- protocol-to-role and protocol-to-mode bindings
- project runtime-capacity inputs
- Codex-specific materialization guidance for this repository

This means the project now has a governed place to say not only what the
portable concepts are, but how Context Atlas chooses to instantiate them.

### Portable Repo Management Canon

`0.1.1` adds a new reusable `RepoManagement` canon under
`docs/Authoritative/Canon/RepoManagement/`.

That surface establishes portable models for:

- repository principals
- authorization scopes
- operation families
- branch-target policy
- audit identity

It also includes a reusable GitHub supplement so repository-facing automation
can be discussed in one authoritative place instead of being buried inside
agent/runtime notes.

### Context Atlas GitHub Binding

`0.1.1` binds that repo-management canon to the actual Context Atlas GitHub
usage model under `docs/Authoritative/Identity/RepoManagement/GitHub/`.

That binding now makes explicit:

- which kinds of GitHub principals the project expects
- what each principal may do
- how merge authority should vary by target branch class
- how audit identity should remain readable in PR history
- how agentic roles connect to GitHub review and merge actions

### Versioned Package Surface

`0.1.1` also updates the package-facing version surfaces so release metadata is
consistent across:

- `pyproject.toml`
- `context_atlas.__version__`
- the installable CLI version test
- in-repo release history under `docs/Release/`

## Known Gaps

`0.1.1` strengthens the repository's operating model, but several important
gaps remain intentionally open.

- The new agentic and repo-management surfaces are authoritative and
  reviewable, but they are still more defined than fully materialized in live
  automation.
- The repository still operationally relies on the current manual PR review
  pattern; the future QA-owned review handoff model is now defined, but not yet
  fully enacted end to end.
- The project-specific Codex binding is documented, but the full runtime asset
  set and drift enforcement loops are still a follow-on step rather than a
  complete day-to-day operational system.
- GitHub principal strategy is now modeled, but bootstrap and provisioning of
  scoped GitHub Apps or equivalent machine principals are still external follow-
  up work.
- Release history is now cleaner, but the repository still does not have a
  fuller release-process canon for branching, cutover, publication cadence, or
  post-release automation.

## Future State

The next phase after `0.1.1` should focus on turning the newly governed
structures into a more complete operational system.

Near-term work should emphasize:

- materializing the agentic bindings into real runtime assets and workflows
- replacing manual review invocation with structured QA-owned review intake
- provisioning scoped repository principals that match the documented
  RepoManagement model
- strengthening release-process canon and publication automation
- continuing to widen scenario coverage without weakening the Canon versus
  Identity boundary

The key principle should remain the same: extend the governed model through
clear authoritative layers first, then materialize it into runtime behavior
without collapsing portable canon, project bindings, and operational assets
back together.

## Related Artifacts

- [Release 0.1.0](./release_0_1_0.md)
- [MVP Readiness Assessment](../Reviews/MVP/mvp_readiness_assessment.md)
- [Guides Index](../Guides/README.md)
- [Context Atlas Agentic Development Profile](../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas GitHub Binding](../Authoritative/Identity/RepoManagement/GitHub/README.md)
- [Repository README](../../README.md)
