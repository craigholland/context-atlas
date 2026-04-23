---
id: context-atlas-013-cleanup-task-3-1-leak-inventory-and-classification
title: Task 3.1 - Leak Inventory And Classification PR Plan
summary: Defines the PR sequence for inventorying the current Canon leaks and classifying which ones should be generalized, rerouted downstream, or left in place intentionally.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-23
owners: [core]
tags: [cleanup, task, pr-plan, canon, inventory, portability]
related:
  - ../story_3_portable_canon_leak_cleanup.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../docs/Authoritative/Canon/AgenticDevelopment/README.md
  - ../../../../../docs/Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../../../../../docs/Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
supersedes: []
---

# Task 3.1 - Leak Inventory And Classification PR Plan

## Objective

Inventory the current portable-Canon leaks and classify them clearly enough
that later cleanup tasks can act intentionally instead of debating each example
from scratch.

## Task Status

IMPLEMENTED

## Inputs

- [Story 3 - Portable Canon Leak Cleanup](../story_3_portable_canon_leak_cleanup.md)
- current touched Canon entry surfaces in AgenticDevelopment, Architecture, and
  Ontology

## Proposed Work

### PR - A: Leak Inventory Pass

- inspect the current candidate leak surfaces and capture the examples that are
  clearly local rather than portable
- keep the inventory bounded to obvious high-value examples already surfaced by
  the reviews

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_3_portable_canon_leak_cleanup.md`

#### Update AI files

- `.`

### PR - B: Classification Rules And Story Reinforcement

- classify findings as generalize, reroute downstream, or keep intentionally
- reinforce Story 3 with the classification model so later tasks can move
  mechanically
- avoid turning this task into actual document cleanup

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_3_portable_canon_leak_cleanup.md`
- `docs/Planning/013_Cleanup/013_cleanup_product_definition.md`

#### Update AI files

- `.`

## Sequencing

- inventory first
- classify and reinforce the Story second

## Completed Outcome

Task 3.1 now settles the bounded leak inventory and classification model for
Story 3.

The Story now names a concrete leak set across AgenticDevelopment,
Architecture, and Ontology canon surfaces, and it classifies each finding into
one of three dispositions:

- `generalize in Canon`
- `reroute to downstream Identity/materialization`
- `keep intentionally as a case-study-derived example`

That gives later Story 3 tasks a shared operating model for cleanup without
re-litigating whether every project-local noun in the broader canon is in scope
for this Epic.

## Risks And Unknowns

- The task can become a second cleanup task if contributors start fixing every
  leak while inventorying.
- Classification can become too theoretical if it is not kept tied to the
  concrete leak set already in scope.

## Exit Criteria

- Story 3 has a clear inventory and classification model for its target leaks
- later cleanup tasks can operate from that shared map rather than re-litigate
  scope

## Related Artifacts

- [Story 3 - Portable Canon Leak Cleanup](../story_3_portable_canon_leak_cleanup.md)
- [013 Cleanup Product Definition](../../013_cleanup_product_definition.md)

