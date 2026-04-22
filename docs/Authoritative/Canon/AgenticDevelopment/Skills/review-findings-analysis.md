---
id: craig-skill-review-findings-analysis
title: Review Findings Analysis
summary: Defines the portable skill for converting observed evidence into explicit findings, risk statements, and acceptance judgments.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, review, findings, qa]
related:
  - ./README.md
  - ./python-testing.md
  - ../Escalation-Model.md
  - ../RoleArchetypes/quality-assurance-engineer.md
supersedes: []
---

# Review Findings Analysis

## Purpose

Define the portable skill for turning evidence into explicit findings, risk
statements, and review outcomes.

## Knowledge Scope

This skill should cover:

- the difference between evidence, observation, finding, risk, and acceptance
  judgment
- how to frame findings with reproducibility, expected behavior, and impact
- how review lenses can differ across code, architecture, security, and product
  concerns
- how to distinguish blocker-level issues from questions, clarifications, and
  low-severity advice
- how to express confidence honestly when evidence is partial

## Common Mode Affinity

- review

## Common Role Affinity

- Quality Assurance Engineer
- User Acceptance Tester

## Common Inputs

- code diffs, tests, traces, docs, or review-surface evidence
- expected behavior or governing contracts
- prior findings or known risk context
- current gate or review-pass purpose

## Decision Heuristics

- state the evidence first, then the finding derived from it
- distinguish severity from confidence
- write findings that a rework actor can act on concretely
- do not promote vague discomfort to a blocker without supporting rationale
- keep “needs clarification” distinct from “changes required”

## Execution Pattern

- inspect the available evidence
- compare it to expected behavior or governing constraints
- classify the concern by kind, severity, and confidence
- state the outcome or follow-up path explicitly

## Expected Outputs

- findings summary
- acceptance or risk statement
- escalation or rework recommendation
- severity and confidence framing

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- findings that are specific enough to verify or remediate
- clear evidence for why the finding exists
- explicit separation between confirmed defects and open questions

## Escalation Conditions

Escalate when:

- available evidence is too weak to support a responsible judgment
- the concern crosses into unsettled architecture, security, or product policy
- the required remedy would exceed the current review pass or role authority

## Guardrails

- does not replace the underlying evidence-producing skills
- should not become implementation ownership by proxy
- must remain specific enough to support rework or follow-up

## Related Artifacts

- [Skills](./README.md)
- [Python Testing](./python-testing.md)
- [Escalation Model](../Escalation-Model.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
