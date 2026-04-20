---
id: context-atlas-role-accountability-matrix
title: Context Atlas Role Accountability Matrix
summary: Defines what each Context Atlas role is primarily accountable for and which repository artifacts and decisions each role owns directly.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, roles, accountability, ownership]
related:
  - ./Role-Model.md
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../../AgenticDevelopment/Agent-Composition-Model.md
  - ../../AgenticDevelopment/Delegation-Model.md
supersedes: []
---

# Context Atlas Role Accountability Matrix

## Purpose

Define what each Context Atlas role is primarily accountable for and which
artifact and decision surfaces it may own directly.

This document distinguishes accountability from mere participation in a
workflow. A role may participate in many protocols, but only some artifacts and
decisions are actually owned by that role.

## Scope

This matrix defines:

- primary accountability by role
- directly owned artifact surfaces
- directly owned decision surfaces
- where specialist participation stays subordinate to parent-owned
  accountability

It does not yet define approval authority, escalation triggers, or precise
protocol sequencing. Those are handled by later Story 3 and Story 5 artifacts.

## Accountability Matrix

### Planner/Decomp

#### Primary Accountability

Maintain decomposition quality, dependency-aware sequencing, and planning
coherence across Epics, Stories, Tasks, and PR slices.

#### Direct Artifact Ownership

- planning artifacts under `docs/Planning/`
- decomposition updates that keep Epic, Story, Task, and PR-plan layers aligned
- planning readmes or orientation notes that govern how decomposition should be
  consumed

#### Direct Decision Ownership

- how work is decomposed
- what work is base or blocking versus parallelizable
- whether planning layers remain aligned and sufficiently explicit

#### Specialist Participation Note

Specialists may help with bounded planning analysis, but the parent-owned
Planner/Decomp role remains accountable for the resulting decomposition shape.

### Backend

#### Primary Accountability

Own product-engine implementation and the repository surfaces that define how
Context Atlas behaves as a system.

#### Direct Artifact Ownership

- engine and package code under `src/context_atlas/`
- backend-oriented tests under `tests/`
- technical implementation docs when they need to move with code or product
  behavior
- implementation-facing scripts that support product behavior or verification

#### Direct Decision Ownership

- implementation direction for domain, service, infrastructure, adapter, and
  rendering changes
- technical tradeoffs needed to deliver backend slices within Craig
  Architecture
- code-shape and architectural-conformance decisions inside owned backend work

#### Specialist Participation Note

Backend specialists may own narrow delegated slices, but they do so under
parent-owned Backend accountability rather than as an alternate top-level role.

### Documentation/UAT

#### Primary Accountability

Own user-facing documentation, guided evaluation, and user-acceptance-oriented
product surfaces for the repository.

#### Direct Artifact Ownership

- user-facing guides and onboarding surfaces under `docs/Guides/`
- runnable example experience under `examples/`
- documentation or example flows that shape how a technical evaluator
  understands and validates the product
- CLI-facing experience when the concern is user-facing evaluation or clarity
  rather than backend execution logic

#### Direct Decision Ownership

- how evaluators and users encounter, understand, and exercise the current
  product surface
- documentation and example choices for guided setup, guided validation, and
  user-acceptance-style walkthroughs
- user-facing clarity when backend capabilities need outward explanation or
  demonstration

#### Specialist Participation Note

Documentation/UAT specialists may help with narrow presentation or evaluation
tasks, but the parent-owned Documentation/UAT role remains accountable for the
resulting user-facing surface.

### QA

#### Primary Accountability

Own governed validation, finding quality, acceptance analysis, and rework
feedback loops.

#### Direct Artifact Ownership

- review findings and acceptance artifacts
- test-oriented verification additions that exist to validate behavior rather
  than to own the primary implementation direction
- review or proof surfaces that summarize validation outcomes

#### Direct Decision Ownership

- whether delivered work appears validated, incomplete, risky, or ready for
  acceptance recommendation
- what findings must be resolved before work should be treated as ready
- how verification evidence should be framed for downstream handoff

#### Specialist Participation Note

QA specialists may execute narrow validation scopes, but the parent-owned QA
role remains accountable for the integrity of the review outcome.

### DevOps

#### Primary Accountability

Own repository operational delivery surfaces that should not drift into general
implementation work.

#### Direct Artifact Ownership

- CI/workflow definitions under `.github/workflows/`
- release-process documentation and release-summary surfaces
- versioning, tagging, merge, and operational delivery artifacts
- automation or operational scripts whose primary job is repository delivery
  rather than product behavior

#### Direct Decision Ownership

- merge readiness once required planning, implementation, and QA expectations
  are satisfied
- release preparation and release-cut decisions
- operational workflow changes that affect how the repository is validated,
  merged, or shipped

#### Specialist Participation Note

DevOps specialists may help with narrow operational or automation work, but the
parent-owned DevOps role remains accountable for the resulting operational
change.

## Cross-Role Clarifications

- Roles own accountabilities; protocols only describe how those roles perform
  and hand off work.
- Specialists may participate in owned work, but their participation does not
  change which role is accountable.
- A role may touch artifacts outside its most common surfaces when a protocol
  requires it, but that should not be used to redefine the ownership model
  implicitly.

## Constraints

- Accountability should remain grounded in real repository work.
- Artifact ownership should stay specific enough that handoffs can identify who
  owns the next move.
- The matrix should not drift into approval-authority rules that belong in the
  authority layer.

## Non-Goals

- Define which role may approve, merge, or release.
- Define the exact mode set each role may enter.
- Define protocol sequencing.

## Related Artifacts

- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Agent Composition Model](../../AgenticDevelopment/Agent-Composition-Model.md)
- [Delegation Model](../../AgenticDevelopment/Delegation-Model.md)
