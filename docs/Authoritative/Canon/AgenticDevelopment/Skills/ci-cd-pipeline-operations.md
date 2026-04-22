---
id: craig-skill-ci-cd-pipeline-operations
title: CI/CD Pipeline Operations
summary: Defines the portable skill for working with build, validation, and delivery pipelines as bounded operational surfaces.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, ci-cd, delivery, operations]
related:
  - ./README.md
  - ./operational-delivery-readiness.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# CI/CD Pipeline Operations

## Purpose

Define the portable skill for reasoning about build, validation, and delivery
pipelines as bounded operational systems.

## Knowledge Scope

This skill should cover:

- common pipeline stages such as build, test, package, publish, and deploy
- job logs, artifacts, caches, matrices, status checks, and retry behavior
- common failure categories such as flaky tests, environment drift, secret or
  permission issues, and packaging or deployment mismatches
- the difference between interpreting pipeline state and owning the authority to
  change production systems
- how pipelines interact with review gates and delivery readiness

## Common Mode Affinity

- operational_delivery
- recovery

## Common Role Affinity

- DevOps Engineer
- Quality Assurance Engineer

## Common Inputs

- current pipeline and job status
- workflow configuration or job definition context
- logs, artifacts, and associated PR or branch state
- known release or readiness gates

## Decision Heuristics

- identify the earliest stage where the failure becomes visible
- separate deterministic failures from likely flaky or environment-driven
  failures
- prefer bounded remediation or rerun logic over wide speculative changes
- escalate when the failure implies missing operational authority or unsafe
  infrastructure action
- keep reviewability intact by leaving an explainable audit trail

## Execution Pattern

- inspect failing or blocked pipeline state
- classify the failure type
- identify the smallest responsible operational response
- state whether the next step is rerun, fix, hold, rollback, or escalate

## Expected Outputs

- pipeline status summary
- failure interpretation notes
- bounded remediation or escalation recommendation
- readiness impact statement

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- a clear statement of what failed and where
- explicit reasoning about why the proposed next step is appropriate
- enough audit context that another operator can follow the decision

## Escalation Conditions

Escalate when:

- remediation requires privileged infrastructure or production access
- the failure cannot be classified from available logs and artifacts
- the pipeline is signaling a broader release or environment problem
- retrying would create unacceptable uncertainty or risk

## Guardrails

- does not automatically grant infrastructure-administration authority
- does not replace application-level debugging
- should remain centered on bounded pipeline behavior

## Related Artifacts

- [Skills](./README.md)
- [Operational Delivery Readiness](./operational-delivery-readiness.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
