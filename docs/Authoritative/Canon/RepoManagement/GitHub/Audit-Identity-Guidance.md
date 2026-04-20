---
id: github-audit-identity-guidance
title: Audit Identity Guidance
summary: Defines reusable GitHub guidance for stable visible bot names, readable PR history, and structured runtime traceability that stays separate from provider-visible identities.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, github, audit, bot-identities, traceability]
related:
  - ./README.md
  - ../Audit-Identity-Model.md
  - ./Pull-Request-Operation-Model.md
supersedes: []
---

# Audit Identity Guidance

## Purpose

Define reusable GitHub guidance for visible bot names and deeper structured
traceability.

## Scope

This document governs readable GitHub-side identity behavior without choosing
one project's final names.

## Binding Decisions

### 1. GitHub-Visible Principal Names Should Stay Stable And Human-Readable

A GitHub-visible principal name should help a human scanning a closed pull
request understand which governed actor family performed the action.

### 2. Runtime Instance Detail Should Stay In Structured Metadata

Runtime instance IDs, worker numbers, or temporary execution identifiers should
not be embedded directly in the visible GitHub actor name.

Those details belong in structured event metadata, check output, or governed
comment payloads.

### 3. Visible Names Should Prefer Role-Oriented Clarity Over Tool Jargon

Names should make sense to a reviewer looking at repository history, for
example by signaling planning, implementation, QA, or merge execution
authority, rather than exposing one runtime's internal naming habits.

### 4. Pull Request History Should Reveal Who Implemented, Reviewed, And Merged

GitHub history should make it easy to answer:

- which principal published the implementation work
- which principal published the governed review
- which principal executed the merge

### 5. Deeper Context Should Be Machine-Readable

When projects need richer audit context, they should carry it through
structured payloads rather than through increasingly noisy visible actor names.

## Constraints

- GitHub-visible names should remain stable across runs.
- Provider bindings should keep naming guidance reusable across projects.
- Project bindings should refine this guidance into concrete names.

## Non-Goals

- Choose one project's final principal names.
- Define one mandatory payload schema for every project.
