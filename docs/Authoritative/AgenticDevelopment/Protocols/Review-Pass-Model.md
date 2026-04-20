---
id: craig-review-pass-model
title: Review Pass Model
summary: Defines the portable review-pass taxonomy used inside governed review workflows so systems can apply different evaluation lenses without creating separate roles or modes for each one.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, review, review-pass, qa, canon]
related:
  - ./Review-Protocol.md
  - ./Protocol-Template.md
  - ../Mode-Model.md
supersedes: []
---

# Review Pass Model

## Purpose

Define the portable review-pass taxonomy used inside governed review workflows.

## Scope

This document defines evaluation lenses that may be applied within a review
protocol.

It does not define which passes a specific application requires at which gate.
That mapping belongs in a downstream binding layer.

## Binding Decisions

### 1. Review Passes Are Lenses Inside Review Work

A review pass is an evaluation lens used by a reviewer while executing review
work.

It is not:

- a separate role
- a separate mode
- a separate protocol family

### 2. More Than One Pass May Apply To The Same Review Intake

A single governed review may execute one or more passes over the same intake.

Those passes should be recorded distinctly when doing so improves clarity.

### 3. Code Pass

`code` focuses on local changed-surface correctness and implementation quality.

Typical concerns include:

- correctness of the changed logic
- obvious regressions
- test and validation sufficiency
- local readability and maintainability at the changed surface

### 4. Architecture Pass

`architecture` focuses on structural integrity across the changed scope.

Typical concerns include:

- boundary preservation
- layering and ownership integrity
- decomposition honesty
- cohesion and code-shape governance

### 5. Security Pass

`security` focuses on authority, trust, and unsafe-behavior concerns.

Typical concerns include:

- secrets and credential handling
- unsafe filesystem, shell, or network behavior
- permission and approval drift
- injection, exposure, or trust-boundary mistakes

### 6. Product Pass

`product` focuses on user-facing or operator-facing coherence.

Typical concerns include:

- setup and onboarding truthfulness
- guide, example, and README alignment
- delivered outcomes matching the claimed product surface
- evaluator-facing clarity

### 7. Pass Results Should Stay Structured

When passes are recorded explicitly, review outcomes should retain structured
pass state such as:

- pass name
- status
- findings emitted
- summary or rationale

## Constraints

- Review passes should stay small in number and semantically distinct.
- New passes should justify themselves through a durable evaluation difference,
  not one transient project habit.
- Pass taxonomy should remain portable and should not embed project-specific
  gate policies.

## Non-Goals

- Define a project-specific gate-to-pass matrix.
- Replace the review protocol itself.
- Turn review passes into worker names or approval roles.

## Related Artifacts

- [Review Protocol](./Review-Protocol.md)
- [Protocol Template](./Protocol-Template.md)
- [Mode Model](../Mode-Model.md)
