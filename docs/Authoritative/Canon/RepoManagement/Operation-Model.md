---
id: repo-operation-model
title: Operation Model
summary: Defines the portable families of repository operations that later provider and project bindings should scope explicitly.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, operations, review, merge, release]
related:
  - ./README.md
  - ./Authorization-Model.md
  - ./Branch-Target-Policy-Model.md
supersedes: []
---

# Operation Model

## Purpose

Define the portable families of repository operations that later bindings
should scope explicitly.

## Scope

This document defines operation families, not provider API details.

## Operation Families

### 1. Ref And Branch Mutation

Operations that create, update, or push branch or ref state.

Typical later bindings may refine this into:

- branch creation
- commit push
- ref update

### 2. Work-Item Surface Mutation

Operations that create or update repository-visible work items such as pull
requests, merge requests, issues, or release drafts.

### 3. Comment Publication

Operations that publish conversational or explanatory comments onto a provider
surface.

### 4. Review Publication

Operations that publish governed review findings, inline comments, or
accept/reject judgments onto a formal review surface.

### 5. Metadata Mutation

Operations that mutate labels, assignments, statuses, titles, or other
non-content metadata on a repository work item.

### 6. Merge Execution

Operations that integrate one source branch class into a target branch class.

### 7. Release And Tag Execution

Operations that create, edit, or publish tags, releases, or equivalent
provider release artifacts.

### 8. Workflow Or Automation Mutation

Operations that change repository automation, CI/CD behavior, provider hooks,
or policy surfaces.

## Binding Decisions

### 1. Operation Families Should Be Scoped Before Provider Mapping

Projects should decide which operation families matter before binding those
families to one provider's API or one runtime's tool surface.

### 2. Merge Execution Is Distinct From Ref Mutation

Pushing a branch and merging a branch are not the same authority surface.

### 3. Review Publication Is Distinct From Comment Publication

Freeform comments and governed review findings should remain separate
operation families even if one provider exposes both through a similar UI.

### 4. Workflow Mutation Should Remain Highly Scoped

Workflow or automation mutation typically deserves narrower authority than
ordinary implementation or review work.

## Constraints

- Project bindings should map these families explicitly.
- Providers may expose additional sub-operations, but those should remain
  downstream refinements.
- The portable model should stay small enough to remain legible.

## Non-Goals

- Enumerate every provider API endpoint.
- Choose one project's allowed operation matrix.
