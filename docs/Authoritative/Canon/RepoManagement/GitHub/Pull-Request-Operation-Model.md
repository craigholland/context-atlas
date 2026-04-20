---
id: github-pull-request-operation-model
title: Pull Request Operation Model
summary: Defines how the portable operation families map onto GitHub pull request surfaces such as comments, review threads, review submissions, and merge execution.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, github, pull-requests, reviews, comments]
related:
  - ./README.md
  - ../Operation-Model.md
  - ../Audit-Identity-Model.md
supersedes: []
---

# Pull Request Operation Model

## Purpose

Define how portable repository operation families map onto GitHub pull request
surfaces.

## Scope

This document governs reusable GitHub semantics for PR comments, review
submissions, inline findings, metadata updates, and merge execution.

It does not define one project's final PR workflow or role bindings.

## Binding Decisions

### 1. Pull Requests Are A First-Class GitHub Review Surface

On GitHub, pull requests are not only integration requests. They are also the
primary provider-native review surface for:

- conversational comments
- inline review findings
- review summaries
- merge readiness discussion

### 2. Comment Publication And Review Publication Stay Distinct

GitHub exposes both ordinary issue-style PR comments and formal review
surfaces. Reusable guidance should preserve that distinction:

- comments are conversational or explanatory
- review publication expresses governed findings or judgments

### 3. Inline Findings And Review Summaries Are Complementary

GitHub review work may use:

- inline review comments for location-specific findings
- overall review summaries for gate-level outcome and next-step guidance

### 4. Merge Execution Is Downstream Of Review State

The GitHub PR surface is where review evidence and merge readiness typically
converge, but merge rights remain a separate operation family and should not be
implied by review participation alone.

### 5. PR Metadata Mutation Is A Separate Operation Family

Updating titles, labels, assignees, or target branches should remain a
separate scoped operation rather than being treated as part of ordinary review
or merge rights.

## Constraints

- Provider bindings should keep review publication and comment publication
  distinct on GitHub.
- Project bindings should make merge authority explicit rather than assuming it
  from PR authorship or review authorship.
- GitHub-specific PR semantics should remain reusable across projects.

## Non-Goals

- Define a project's exact review gate policy.
- Define one project's branch-target merge rules.
