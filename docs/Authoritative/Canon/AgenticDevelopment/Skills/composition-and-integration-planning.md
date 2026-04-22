---
id: craig-skill-composition-and-integration-planning
title: Composition And Integration Planning
summary: Defines the portable skill for reasoning about how bounded work slices fit back together without violating ownership, architecture, or workflow boundaries.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, planning, composition, integration]
related:
  - ./README.md
  - ../Agent-Composition-Model.md
  - ../Protocols/Planning-Protocol.md
supersedes: []
---

# Composition And Integration Planning

## Purpose

Define the portable skill for planning how separately bounded work can be
recombined safely, coherently, and in the correct order.

## Knowledge Scope

This skill should cover:

- how bounded work slices compose back into a coherent outcome
- how parent ownership persists across delegated or parallel work
- how branch, review, and merge structure can affect integration risk
- how cross-cutting concerns can invalidate naive parallel decomposition
- how architectural seams should influence reintegration order

## Common Mode Affinity

- planning
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- Backend Staff Engineer
- DevOps Engineer

## Common Inputs

- the existing decomposition or work breakdown
- branch and review model constraints
- known dependency graph and integration points
- architecture and binding-layer boundaries
- runtime capacity and coordination limits

## Decision Heuristics

- identify where composition must happen before splitting work further
- prefer reintegration points that preserve one accountable parent actor
- pull integration earlier when hidden coupling is likely
- keep independently reviewable work independent unless recomposition requires
  tighter sequencing
- treat shared infrastructure, shared contracts, and shared public interfaces as
  higher-risk composition seams

## Execution Pattern

- inspect the work breakdown for recomposition surfaces
- identify merge, handoff, and contract-touching seams
- state which work may proceed in parallel and which must converge first
- define the order in which partial outputs should be integrated

## Expected Outputs

- integration plan
- ownership-aware recomposition notes
- merge and handoff sequencing guidance
- integration risk summary

## Verification And Evidence

A well-used instance of this skill should make it possible to explain:

- where composition will occur
- why the chosen order reduces risk
- who remains accountable when delegated or parallel work returns
- which seams deserve explicit review before wider rollout

## Escalation Conditions

Escalate when:

- multiple slices appear to compete for the same write scope or authority
- integration risks cannot be bounded without revisiting the decomposition
- architecture or interface contracts are unstable
- no responsible parent actor is clearly accountable for recomposition

## Guardrails

- does not replace architecture conformance review
- does not grant merge or release authority
- should not silently absorb change-management or operational-delivery work

## Related Artifacts

- [Skills](./README.md)
- [Agent Composition Model](../Agent-Composition-Model.md)
- [Planning Protocol](../Protocols/Planning-Protocol.md)
