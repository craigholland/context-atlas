---
id: context-atlas-mvp-evaluation-rubric
title: Context Atlas MVP Evaluation Rubric
summary: Defines the evidence dimensions and review thresholds for deciding whether Context Atlas has reached MVP readiness.
doc_class: review
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, review, rubric, evidence, evaluation]
related:
  - ./mvp_readiness_assessment.md
  - ../../Planning/completed/MVP/mvp_product_defintiion.md
  - ../../Planning/completed/MVP/Stories/story_6_mvp_proof.md
  - ../../Planning/completed/MVP/Stories/Tasks/task_6_1_evidence_shape.md
supersedes: []
---

# Context Atlas MVP Evaluation Rubric

## Objective

Define the minimum evidence dimensions that must be reviewed before Context Atlas can make a grounded MVP readiness claim.

## Inputs

- [Context Atlas MVP Product Definition](../../Planning/completed/MVP/mvp_product_defintiion.md)
- [Story 6 - MVP Proof](../../Planning/completed/MVP/Stories/story_6_mvp_proof.md)
- completed workflow outputs from Stories 1 through 5

## Evaluation Dimensions

### 1. Packet Quality

Evidence should show that Atlas selects context that is materially more usable than a naive baseline.

Review questions:

- Does the packet contain sources that are clearly relevant to the task or query?
- Does the packet avoid obvious filler or duplicate content?
- Does the packet preserve enough structure to explain what was selected?

Minimum acceptable evidence:

- at least one packet artifact from a supported workflow
- one comparable naive baseline artifact for the same scenario
- short written notes explaining the most important differences

### 2. Trace Legibility

Evidence should show that packet decisions are inspectable by a human reviewer without reading internal implementation code.

Review questions:

- Can a reviewer tell why sources were included, excluded, compressed, or deferred?
- Is the ordering of decisions understandable?
- Is workflow metadata visible enough to explain which outer path produced the packet?

Minimum acceptable evidence:

- one trace artifact per reviewed workflow
- one human-readable inspection view, not only raw structured data

### 3. Authority Handling

Evidence should show that Atlas treats governed source meaning as a first-class concern rather than as a retrieval afterthought.

Review questions:

- Do authoritative sources remain visible and distinguishable in the evidence?
- Can a reviewer tell when lower-authority or exploratory material was included?
- Does the evidence show that source semantics survive adapter translation?

Minimum acceptable evidence:

- source summaries that preserve class or authority meaning
- notes that call out whether authority-aware behavior was visible in the packet and trace

Document-authority reference scenario:

- workflow id: `codex_repository`
- scenario id: `repo_document_authority_precedence`
- intent: run the flagship repository workflow over an authority-rich governed-doc tree so the packet and trace show authoritative architecture guidance being preferred over lower-authority planning or review material for the same query
- success signal: a reviewer can point to at least one authoritative document that remains visible or is ranked ahead of a lower-authority document candidate and can explain that difference through packet and trace evidence rather than path names alone
- current state: this Story 7 hardening scenario is now implemented and reviewed as part of the standing MVP proof set

### 4. Budget Behavior

Evidence should show that Atlas remains disciplined under constrained context budgets instead of simply stuffing everything into output.

Review questions:

- Is the packet budget state inspectable?
- Can a reviewer see when compression, trimming, or exclusion occurred?
- Does the evidence show what was lost or transformed under pressure?
- Does at least one proof run make the budget tradeoff strong enough that a reviewer can name the sacrificed content, not merely infer that pressure existed?

Minimum acceptable evidence:

- one scenario with explicit budget pressure
- packet and trace artifacts that make the tradeoffs visible
- one scenario definition that states which workflow is under pressure and why that workflow is a meaningful budget test rather than an arbitrary tiny-budget demo

Budget-pressure reference scenario:

- workflow id: `codex_repository`
- scenario id: `repo_budget_pressure_tradeoffs`
- intent: run the flagship repository workflow with a deliberately reduced total budget so packet inspection and trace review show which governed-doc candidates were compressed or excluded under pressure
- success signal: a reviewer can point to at least one concrete exclusion, compression, or deferred document-context tradeoff and relate it back to the visible budget state
- current state: this Story 7 hardening scenario is now implemented and reviewed as part of the standing MVP proof set

### 5. Workflow Reproducibility

Evidence should show that proof artifacts come from supported workflows, not one-off manual assembly.

Review questions:

- Can the evidence be regenerated from a documented workflow path?
- Are the input roots, presets, and task/query values captured clearly enough to repeat the run?
- Does the proof stay on the same shared engine path used by the product workflows?

Minimum acceptable evidence:

- a documented workflow identifier for each captured scenario
- reproducible input references
- a stable capture path rather than ad hoc screenshots or copied terminal fragments

## Required Evidence Package

Each proof scenario should eventually capture:

- workflow name
- scenario name
- query or task text
- input summary
- naive baseline rendered context
- Atlas packet artifact
- Atlas trace artifact
- Atlas rendered context artifact
- short reviewer notes

The current reference packaging path for that evidence is
`scripts/mvp_proof/capture_evidence.py`. It packages already-generated workflow
artifacts; it does not generate packet or trace outputs itself.

The canonical review record for those packages should live in
[mvp_readiness_assessment.md](./mvp_readiness_assessment.md).

## Evidence Review Path

Each captured evidence package should be reviewed in the same order:

1. read the naive baseline rendered-context artifact first
2. read the Atlas rendered-context artifact for the same scenario
3. inspect the Atlas packet artifact to verify what was actually selected
4. inspect the Atlas trace artifact to understand inclusion, exclusion, and transformation decisions
5. record notes against each rubric dimension before making a recommendation

That review order is also embedded directly into the evidence package produced by
`scripts/mvp_proof/capture_evidence.py` so the proof process stays repeatable
even when the artifacts are reviewed later by a different contributor.

## Recommendation Thresholds

### Not Ready

- evidence is incomplete, workflow-specific, or not reproducible
- packet and trace artifacts do not clearly outperform narrative-only explanation

### Conditionally Ready

- evidence is reproducible and legible
- at least two workflows show meaningful value
- one or more important gaps still need to be called out explicitly

### MVP Ready

- evidence is reproducible across the selected workflows
- packet, trace, authority, and budget behavior are all inspectable
- Atlas can be defended as a reusable pipeline component rather than a workflow-specific demo

## Current Recommendation State

The current assessment now records `MVP Ready` as of `2026-04-19` after the
Story 7 hardening pass closed the prior authority and budget caveats.

This rubric still exists to define the threshold for future reassessments; the
canonical decision record remains
[mvp_readiness_assessment.md](./mvp_readiness_assessment.md).

## Workflows Under Test For The Current Proof Pass

The current MVP proof pass will include all three supported MVP workflows.

### Inclusion Criteria

A workflow is included only if it currently has:

- a supported runnable path in `examples/`
- packet inspection and trace inspection on the shared engine path
- reproducible local inputs without hidden external services
- enough product-facing documentation that a later reviewer can understand what
  the workflow is proving

### Exclusion Criteria

A workflow should be excluded from the current proof pass if it:

- requires a live provider API or external database client that is not already
  modeled as tracked local input
- depends on unpublished setup steps or manual hand-editing of packet or trace
  artifacts
- bypasses the supported Atlas workflow path to generate proof artifacts more
  conveniently

### Selected Workflow Set

`1. Codex repository workflow`

- workflow id: `codex_repository`
- scenario id: `repo_governed_docs_update`
- query focus: how an engineer should update repository planning and
  architecture guidance
- why included: it is the flagship repository-facing workflow and already has a
  supported runnable path with packet and trace inspection

`2. Documents plus database workflow`

- workflow id: `docs_database_builder`
- scenario id: `builder_support_troubleshooting`
- query focus: how a technical builder should configure Atlas and troubleshoot
  environment or preflight issues in a chatbot pipeline
- why included: it proves the mixed-source component story over governed docs
  plus already-fetched record rows

`3. Low-code workflow`

- workflow id: `low_code_chatbot`
- scenario id: `low_code_validation`
- query focus: how a low-code builder should validate Atlas packet and trace
  behavior through the preset-driven path
- why included: it now has a supported preset-driven wrapper with shared packet
  and trace inspection plus reproducible tracked inputs
