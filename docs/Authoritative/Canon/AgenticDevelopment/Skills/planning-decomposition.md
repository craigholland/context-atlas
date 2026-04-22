---
id: craig-skill-planning-decomposition
title: Planning Decomposition
summary: Defines the portable skill for breaking work into bounded, reviewable slices with explicit sequencing, architectural alignment, and level-of-work reasoning.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, planning, decomposition]
related:
  - ./README.md
  - ../Skill-Contract.md
  - ../Protocols/Planning-Protocol.md
  - ../RoleArchetypes/planning-decomposition-lead.md
supersedes: []
---

# Planning Decomposition

## Purpose

Define the portable skill for turning a larger objective into bounded,
sequenced, reviewable work slices that preserve architectural and workflow
clarity.

## Knowledge Scope

This skill should cover:

- how to read an objective in terms of outcome, scope, and affected surfaces
- how architectural boundaries constrain decomposition
- how role, mode, and protocol boundaries shape the work model
- how to distinguish `epic`, `story`, and `task` levels beyond simple size
- how to reason about sequencing, dependency, and handoff placement
- how to incorporate bounded runtime capacity into the plan

## Common Mode Affinity

- planning
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- Backend Staff Engineer
- DevOps Engineer

## Common Inputs

- the objective or requested outcome
- the governing architecture and canon
- known role, mode, protocol, and review-gate constraints
- any declared capacity, timing, or parallelism limits
- existing work already in progress that must not be duplicated

## Decision Heuristics

- treat something as an `epic` when it spans multiple coherent outcomes,
  multiple stories, or multiple review/integration stages
- treat something as a `story` when it defines one coherent bounded outcome
  that still requires multiple executable tasks
- treat something as a `task` when it is directly executable, reviewable, and
  attributable as one bounded unit of work
- do not mix unrelated architectural boundaries into a single task merely to
  reduce item count
- do not split work so finely that validation and ownership become noisy or
  meaningless
- prefer decomposition that preserves explicit handoffs instead of hiding them

## Execution Pattern

- restate the objective in concrete outcome terms
- identify affected boundaries, roles, and proof surfaces
- separate critical-path work from parallelizable work
- place epic, story, and task boundaries deliberately
- state sequencing, dependencies, and handoff points clearly

## Expected Outputs

- decomposition outline
- proposed epic/story/task breakdown
- dependency and sequencing notes
- handoff and proof-surface notes

## Verification And Evidence

A well-used instance of this skill should make it possible to answer:

- why each work item belongs at its chosen level
- which architectural or workflow boundaries each item respects
- where review and handoff are expected to occur
- why the plan is executable under the stated capacity assumptions

## Escalation Conditions

Escalate when:

- the objective is too ambiguous to decompose responsibly
- the governing architecture is missing, contradictory, or unstable
- ownership boundaries between roles or parent agents are unclear
- the work implies product decisions that have not been settled
- the requested scope cannot be made reviewable without revising expectations

## Guardrails

- does not, by itself, authorize protocol transitions or role ownership
- does not replace implementation or review evidence
- should not become an unbounded product-management or architecture document

## Related Artifacts

- [Skills](./README.md)
- [Skill Contract](../Skill-Contract.md)
- [Planning Protocol](../Protocols/Planning-Protocol.md)
- [Planning/Decomposition Lead](../RoleArchetypes/planning-decomposition-lead.md)
