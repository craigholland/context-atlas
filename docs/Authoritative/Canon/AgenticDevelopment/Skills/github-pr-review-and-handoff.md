---
id: craig-skill-github-pr-review-and-handoff
title: GitHub PR Review And Handoff
summary: Defines the portable skill for preparing, interpreting, and responding to pull-request review surfaces in GitHub-style workflows.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, github, review, handoff]
related:
  - ./README.md
  - ./review-findings-analysis.md
  - ../RoleArchetypes/quality-assurance-engineer.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# GitHub PR Review And Handoff

## Purpose

Define the portable skill for using pull-request review surfaces as structured
handoff and findings channels.

## Knowledge Scope

This skill should cover:

- pull-request descriptions, draft vs ready states, and review visibility
- inline findings, summary reviews, reply patterns, and audit continuity
- status checks, approval state, requested changes, and discussion resolution
- how PR surfaces support implementation handoff, QA review, and delivery
  readiness
- the distinction between using the review surface and having authority to
  approve or merge through it

## Common Mode Affinity

- review
- rework
- operational_delivery

## Common Role Affinity

- Quality Assurance Engineer
- DevOps Engineer
- Backend Staff Engineer

## Common Inputs

- the active PR and its diff
- review findings, status checks, and branch target
- structured handoff or review contracts when present
- known authority boundaries for comment, review, approval, and merge

## Decision Heuristics

- use the PR surface to make handoffs and findings visible where the work is
- keep comments specific enough to be action-guiding rather than conversational
  noise
- separate observation, finding, rationale, and acceptance clearly
- do not imply approval or merge authority merely because commentary authority
  exists
- escalate when the review surface cannot express the needed decision or when
  provider permissions block the required action

## Execution Pattern

- inspect the PR, checks, and current review state
- prepare a structured review or handoff comment
- respond to findings or questions with explicit rationale or corrective action
- leave the PR in a clearer review state than it started

## Expected Outputs

- PR review summary
- inline findings or responses
- handoff commentary tied to the review surface
- explicit statement of what remains open or accepted

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- a review surface that clearly shows what was found, requested, or accepted
- replies that a later reviewer can follow without hidden context
- preserved distinction between commentary authority and merge authority

## Escalation Conditions

Escalate when:

- required review actions exceed the actor's provider permissions
- the PR contains unresolved conflicts between authority, readiness, and review
  state
- findings imply architectural or product decisions beyond the current review
  scope

## Guardrails

- does not replace provider-specific authority rules
- does not automatically imply approval or merge
- should remain structured and review-centered rather than conversationally vague

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
