---
id: craig-skills-readme
title: Skills
summary: Introduces the portable skill catalog used by downstream bindings to assemble role-specific and specialist-specific capability sets without redefining atomic skills each time.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, canon, portability, catalog]
related:
  - ../Skill-Contract.md
  - ../Skill-Attachment-Model.md
  - ../RoleArchetypes/README.md
  - ../SpecialistArchetypes/README.md
supersedes: []
---

# Skills

## Purpose

This directory holds the portable skill catalog for agentic development.

These documents define reusable atomic capability units that downstream
application bindings may adopt, refine, and attach to parent agents or
specialists. They are portable skills, not one application's active skill map.

## Scope

The skill catalog describes things like:

- what capability a skill is meant to provide
- what knowledge and ecosystem surface the skill is expected to cover
- which modes the skill commonly supports
- which role families commonly use the skill
- what inputs and decision heuristics shape use of the skill
- what evidence a well-used skill should usually produce
- what bounded outputs the skill is expected to produce
- what constraints keep the skill from expanding into a specialist or role

It does not define:

- which skills a specific application adopts
- which parent agents or specialists a specific project attaches those skills to
- which runtime file layout materializes those skills
- which skills are mandatory for any particular implementation environment

Those choices belong in the downstream identity and materialization layers.

## Expected Shape Of A Skill Definition

Each skill document in this directory should be substantial enough to act as a
real reusable capability definition, not merely a label.

At minimum, a portable skill definition should make the following concerns
explicit:

- purpose
- knowledge scope and any relevant version or ecosystem assumptions
- common mode affinity
- common role affinity
- common inputs
- decision heuristics
- execution pattern
- expected outputs
- verification and evidence expectations
- escalation conditions
- guardrails

## Current Skill Families

- Planning and change:
  - [planning-decomposition.md](./planning-decomposition.md)
  - [composition-and-integration-planning.md](./composition-and-integration-planning.md)
  - [change-management.md](./change-management.md)
- Python engineering:
  - [python-authoring.md](./python-authoring.md)
  - [python-debugging.md](./python-debugging.md)
  - [python-testing.md](./python-testing.md)
- Architecture:
  - [backend-architecture-clean.md](./backend-architecture-clean.md)
  - [backend-architecture-solid.md](./backend-architecture-solid.md)
- Repo and delivery:
  - [git-branch-and-history.md](./git-branch-and-history.md)
  - [github-pr-review-and-handoff.md](./github-pr-review-and-handoff.md)
  - [ci-cd-pipeline-operations.md](./ci-cd-pipeline-operations.md)
  - [operational-delivery-readiness.md](./operational-delivery-readiness.md)
- Review, rework, and recovery:
  - [review-findings-analysis.md](./review-findings-analysis.md)
  - [rework-remediation.md](./rework-remediation.md)
  - [recovery-triage.md](./recovery-triage.md)

## Coverage by Initial Role Families

This portable catalog is intentionally broad enough to support the initial role
families already present in the canon and common downstream bindings.

- `Planning/Decomposition` style roles commonly draw from:
  - `planning-decomposition`
  - `composition-and-integration-planning`
  - `change-management`
- `Backend Engineer (Python)` style roles commonly draw from:
  - `python-authoring`
  - `python-debugging`
  - `python-testing`
  - `backend-architecture-clean`
  - `backend-architecture-solid`
  - `rework-remediation`
- `DevOps` style roles commonly draw from:
  - `git-branch-and-history`
  - `github-pr-review-and-handoff`
  - `ci-cd-pipeline-operations`
  - `operational-delivery-readiness`
  - `recovery-triage`
  - `change-management`
- `QA` style roles commonly draw from:
  - `python-testing`
  - `python-debugging`
  - `review-findings-analysis`
  - `backend-architecture-clean`
  - `backend-architecture-solid`
  - `github-pr-review-and-handoff`

These are affinity patterns, not binding-layer attachment decisions.

## Coverage by Mode

This catalog also intentionally covers the common mode set without turning
skills into disguised modes.

- `planning`:
  - `planning-decomposition`
  - `composition-and-integration-planning`
  - `change-management`
- `implementation`:
  - `python-authoring`
  - `backend-architecture-clean`
  - `backend-architecture-solid`
  - `git-branch-and-history`
- `review`:
  - `python-testing`
  - `review-findings-analysis`
  - `backend-architecture-clean`
  - `backend-architecture-solid`
  - `github-pr-review-and-handoff`
  - `operational-delivery-readiness`
- `rework`:
  - `python-debugging`
  - `rework-remediation`
  - `change-management`
- `recovery`:
  - `recovery-triage`
  - `change-management`
  - `composition-and-integration-planning`
- `operational_delivery`:
  - `ci-cd-pipeline-operations`
  - `operational-delivery-readiness`
  - `github-pr-review-and-handoff`

## How To Use This Set

The intended layering is:

1. read the portable skill contract
2. read the relevant skill documents in this directory
3. read portable specialist archetypes when a bounded delegated actor may be
   more appropriate than a direct skill attachment
4. move to downstream bindings only when a project needs to choose which skills
   and specialists it actually adopts

Applications should treat this catalog as reusable source material, not as a
required one-to-one skill roster.

## Related Artifacts

- [Skill Contract](../Skill-Contract.md)
- [Skill Attachment Model](../Skill-Attachment-Model.md)
- [Role Archetypes](../RoleArchetypes/README.md)
- [Specialist Archetypes](../SpecialistArchetypes/README.md)
