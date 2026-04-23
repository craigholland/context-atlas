---
id: context-atlas-013-cleanup-task-2-4-contributor-path-containment
title: Task 2.4 - Contributor-Path Containment PR Plan
summary: Defines the PR sequence for keeping contributor and governance instructions in the surfaces that actually own them instead of letting them bleed back into product-facing docs.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, contributors, governance, containment]
related:
  - ../story_2_product_path_separation_from_agentic_and_governance_surfaces.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../README.md
  - ../../../../../__ai__.md
  - ../../../../../docs/README.md
supersedes: []
---

# Task 2.4 - Contributor-Path Containment PR Plan

## Objective

Keep contributor and governance instructions in the surfaces that actually own
them, so the product route stays clean while contributor-facing expectations
remain explicit and discoverable.

## Task Status

PLANNED

## Inputs

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Root Owner File](../../../../../__ai__.md)
- contributor/governance-facing docs that are currently cross-linked from the
  repo edge

## Proposed Work

### PR - A: Contributor-Surface Audit And Containment Rules

- identify where contributor or governance instructions still bleed into
  product-facing docs
- define the smallest containment rule that routes those instructions back to
  the owning surfaces
- keep the audit bounded to repo-edge and routing surfaces

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`
- `docs/README.md`

#### Update AI files

- `.`

### PR - B: Contributor/Governance Surface Cleanup

- update the owning contributor or governance surfaces so they can safely
  receive the redirected detail
- keep cross-links explicit and purpose-labeled rather than removing them

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `__ai__.md`
- contributor-facing docs under `docs/Authoritative/Identity/AgenticDevelopment/`
- `docs/README.md`

#### Update AI files

- `.`

### PR - C: Story Closeout Reinforcement

- align Story 2 with the final containment rule
- document any follow-on questions reserved for the consumer packaging or AI
  governance Epics

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_2_product_path_separation_from_agentic_and_governance_surfaces.md`
- `docs/Planning/013_Cleanup/013_cleanup_product_definition.md`

#### Update AI files

- `.`

## Sequencing

- audit bleed-through first
- clean up the owning contributor/governance surfaces second
- reinforce Story and Epic language third

## Risks And Unknowns

- Containment work can hide useful contributor links if it is interpreted as
  removal rather than rerouting.
- It can also drift into governance redesign if the task starts changing the
  meaning of owner-file authority rather than only the routing.

## Exit Criteria

- contributor/governance detail no longer bleeds into product-facing docs by
  default
- owning surfaces are strong enough to receive the redirected detail
- Story 2 and the Epic state the containment boundary clearly

## Related Artifacts

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [013 Cleanup Product Definition](../../013_cleanup_product_definition.md)
- [Root Owner File](../../../../../__ai__.md)

