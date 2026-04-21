---
id: craig-skill-rework-remediation
title: Rework Remediation
summary: Defines the portable skill for turning accepted findings into bounded corrective changes with traceable intent.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, rework, remediation]
related:
  - ./README.md
  - ./review-findings-analysis.md
  - ../Protocols/Rework-Protocol.md
supersedes: []
---

# Rework Remediation

## Purpose

Define the portable skill for translating findings or clarified defects into
bounded corrective changes.

## Common Mode Affinity

- rework

## Common Role Affinity

- Backend Staff Engineer
- Technical Documentation Writer
- DevOps Engineer

## Bounded Capability

- identify the minimum responsible change that addresses the finding
- preserve traceability back to the triggering finding or defect
- communicate what changed and what remains intentionally unchanged

## Common Outputs

- targeted corrective diff
- response-to-finding notes
- bounded verification summary

## Guardrails

- does not dismiss findings on its own authority
- does not replace debugging or testing evidence
- should not become a stealth redesign unless explicitly escalated

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Rework Protocol](../Protocols/Rework-Protocol.md)
