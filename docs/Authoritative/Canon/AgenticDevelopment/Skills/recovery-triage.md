---
id: craig-skill-recovery-triage
title: Recovery Triage
summary: Defines the portable skill for diagnosing unstable or blocked states and choosing bounded recovery directions without absorbing full incident command.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, recovery, triage]
related:
  - ./README.md
  - ../Protocols/Recovery-Protocol.md
  - ../Escalation-Model.md
supersedes: []
---

# Recovery Triage

## Purpose

Define the portable skill for diagnosing blocked, unstable, or drifted states
and choosing a bounded recovery direction.

## Knowledge Scope

This skill should cover:

- common recovery scenarios such as branch drift, failed rollout, blocked
  pipeline, broken validation surface, and incomplete handoff state
- how to separate recoverable local failures from broader systemic issues
- how to identify a last-known-good or safer fallback position
- how rollback, retry, hold, and escalation differ
- how to preserve reviewability while recovering

## Common Mode Affinity

- recovery

## Common Role Affinity

- DevOps Engineer
- Planning/Decomposition Lead
- Backend Staff Engineer

## Common Inputs

- the current failure or blocked state
- recent change history and evidence surfaces
- pipeline, branch, review, or runtime signals
- known recovery constraints and authority limits

## Decision Heuristics

- stabilize before optimizing
- prefer reversible recovery steps when uncertainty remains
- identify whether the failure is local, workflow-level, or systemic
- separate symptom suppression from real recovery
- escalate when recovery would require authority or system knowledge not
  currently available

## Execution Pattern

- summarize the current unstable or blocked state
- classify likely cause categories
- identify the smallest safe next action
- state whether the path is retry, rollback, hold, repair, or escalate

## Expected Outputs

- recovery-state summary
- likely cause categories
- immediate next-step recommendation
- recovery-risk note

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- a clear statement of what recovery is trying to restore
- explicit rationale for the chosen next step
- an understandable path for follow-up if the first recovery action fails

## Escalation Conditions

Escalate when:

- no bounded safe recovery action is visible
- the issue appears systemic rather than local
- recovery would require destructive or high-authority operations
- the known-good state is uncertain or disputed

## Guardrails

- does not replace full incident-command or operational-governance structures
- should not hide the need for escalation when authority is insufficient
- does not imply permanent design decisions

## Related Artifacts

- [Skills](./README.md)
- [Recovery Protocol](../Protocols/Recovery-Protocol.md)
- [Escalation Model](../Escalation-Model.md)
