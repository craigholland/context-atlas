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
  - ../../Planning/MVP/mvp_product_defintiion.md
  - ../../Planning/MVP/Stories/story_6_mvp_proof.md
  - ../../Planning/MVP/Stories/Tasks/task_6_1_evidence_shape.md
supersedes: []
---

# Context Atlas MVP Evaluation Rubric

## Objective

Define the minimum evidence dimensions that must be reviewed before Context Atlas can make a grounded MVP readiness claim.

## Inputs

- [Context Atlas MVP Product Definition](../../Planning/MVP/mvp_product_defintiion.md)
- [Story 6 - MVP Proof](../../Planning/MVP/Stories/story_6_mvp_proof.md)
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

### 4. Budget Behavior

Evidence should show that Atlas remains disciplined under constrained context budgets instead of simply stuffing everything into output.

Review questions:

- Is the packet budget state inspectable?
- Can a reviewer see when compression, trimming, or exclusion occurred?
- Does the evidence show what was lost or transformed under pressure?

Minimum acceptable evidence:

- one scenario with explicit budget pressure
- packet and trace artifacts that make the tradeoffs visible

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

No recommendation yet. This rubric exists to define what later Story 6 tasks must capture before a recommendation is written.
