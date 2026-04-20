---
id: repo-management-glossary
title: RepoManagement Glossary
summary: Defines the core portable vocabulary used by the RepoManagement canon before provider or project bindings refine it.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, glossary, vocabulary, principals, audit]
related:
  - ./README.md
  - ./Principal-Model.md
  - ./Authorization-Model.md
  - ./Operation-Model.md
  - ./Branch-Target-Policy-Model.md
  - ./Audit-Identity-Model.md
supersedes: []
---

# RepoManagement Glossary

## Purpose

Define the portable vocabulary used throughout the RepoManagement canon.

## Terms

### Repo Principal

A stable identity that performs repository operations on behalf of a human,
system, or governed automation flow.

### Principal Family

A bounded group of principals that share a common functional purpose, such as
implementation, review, or merge execution, while still remaining separately
scoped.

### Authorization Scope

The bounded set of repository operations, targets, and provider permissions
granted to a principal.

### Repo Operation

A repository-facing action such as pushing a branch, opening or updating a PR,
commenting, reviewing, merging, tagging a release, or modifying repository
automation.

### Review Surface

The provider-visible place where review work is materialized, such as a pull
request conversation, inline review thread, or provider-native review
submission.

### Branch Class

A policy-oriented grouping of branches by workflow role, such as task,
story, epic, integration, or release.

### Branch-Target Policy

The governed rule set that binds source branch class, target branch class,
required gate state, and permitted merge authority together.

### Provider Binding

A reusable binding layer that refines the portable RepoManagement canon into
one provider's specific mechanics without making project-specific decisions.

### Project Binding

A project-specific refinement that declares which provider is used and how
principals, operations, branch-target policy, and audit identity are applied
within that project.

### Audit Identity

The readable identity trail that lets humans understand which principal acted,
which runtime instance participated, and which workflow state authorized the
action.

### Runtime Instance Identity

A transient execution identity for one runtime session or worker instance.
This is not the same thing as the stable provider-visible principal.

### Visible Principal Name

The provider-facing name that appears in repository history, pull requests,
reviews, comments, checks, or merge records.

### Ambient Runtime Power

Repository access that exists only because a runtime happens to hold a broad
credential, rather than because a governed principal and policy explicitly
authorize the operation.

## Constraints

- Terms in this glossary should remain provider-agnostic.
- Provider-specific meanings belong in provider supplements, not here.
- Project-specific role rosters, branch names, and bot names belong in project
  bindings, not here.
