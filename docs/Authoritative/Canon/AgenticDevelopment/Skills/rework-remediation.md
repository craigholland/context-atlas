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

## Knowledge Scope

This skill should cover:

- how to read findings as actionable correction inputs
- how to choose the narrowest responsible fix that addresses the actual issue
- how to preserve traceability between the finding, the change, and the
  verification evidence
- how to decide between code change, test change, documentation change, or
  explicit rationale
- how rework differs from greenfield implementation

## Common Mode Affinity

- rework

## Common Role Affinity

- Backend Staff Engineer
- Technical Documentation Writer
- DevOps Engineer

## Common Inputs

- accepted findings or defect statements
- the relevant code, docs, config, or workflow surface
- expected behavior or acceptance criteria
- any reviewer guidance or requested evidence

## Decision Heuristics

- fix the finding actually raised, not every adjacent annoyance
- preserve surrounding behavior unless broader change is explicitly required
- prefer a rationale response when the implementation is correct and the finding
  stems from misunderstanding, but only when evidence supports that response
- keep rework traceable to the original finding

## Execution Pattern

- restate the finding in corrective terms
- identify the minimum responsible change
- implement or document the correction
- gather bounded verification evidence
- respond back through the relevant handoff or review surface

## Expected Outputs

- targeted corrective diff
- response-to-finding notes
- bounded verification summary
- explicit statement of what was corrected or defended

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- a clear mapping from finding to correction
- evidence that the stated issue is actually addressed
- a response surface that makes re-review straightforward

## Escalation Conditions

Escalate when:

- the finding implies broader redesign than the current actor may perform
- the evidence needed to defend or fix the finding is unavailable
- multiple findings conflict and cannot be satisfied within one bounded change

## Guardrails

- does not dismiss findings on its own authority
- does not replace debugging or testing evidence
- should not become a stealth redesign unless explicitly escalated

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Rework Protocol](../Protocols/Rework-Protocol.md)
