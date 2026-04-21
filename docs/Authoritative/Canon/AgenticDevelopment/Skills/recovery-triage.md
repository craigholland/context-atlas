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

## Common Mode Affinity

- recovery

## Common Role Affinity

- DevOps Engineer
- Planning/Decomposition Lead
- Backend Staff Engineer

## Bounded Capability

- assess what is broken, blocked, or drifted
- separate reversible issues from deeper structural failures
- propose bounded next steps for stabilization or escalation

## Common Outputs

- recovery-state summary
- likely cause categories
- immediate next-step recommendation

## Guardrails

- does not replace full incident-command or operational-governance structures
- should not hide the need for escalation when authority is insufficient
- does not imply permanent design decisions

## Related Artifacts

- [Skills](./README.md)
- [Recovery Protocol](../Protocols/Recovery-Protocol.md)
- [Escalation Model](../Escalation-Model.md)
