---
id: context-atlas-mvp-story-4-documents-plus-database-workflow
title: Story 4 - Documents Plus Database Workflow
summary: Defines the technical-builder workflow that uses Context Atlas to govern context from both documents and database-backed records.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, story, chatbot, docs, database]
related:
  - ../mvp_product_defintiion.md
  - ../../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 4 - Documents Plus Database Workflow

## Objective

Show that Context Atlas can act as a reusable context-governance component for a technical builder who wants to assemble chatbot context from both documents and database-backed information.

## Inputs

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- Story 2 source-coverage outcomes

## Proposed Tasks

### Task 1: Workflow Shape

- ingest filesystem documents through the docs adapter
- ingest structured records through a record adapter or adapter-ready record feed
- assemble a single packet from both source families
- render and inspect the resulting packet and trace for a chatbot query

### Task 2: Product Deliverables

- one technical integration guide
- one mixed-source example
- one clear explanation of where Atlas stops and application-specific database access begins

### Task 3: Architectural Shape

- database and vector-store clients remain outward concerns
- adapters translate rows, records, or retrieved chunks into canonical sources
- services, policies, packets, and traces remain shared with the Codex workflow
- no provider-specific database semantics should leak into the canonical domain model

## Sequencing

- define the technical-builder example scenario
- finalize the record-ingestion contract or adapter
- assemble mixed-source packets through the shared engine
- write the integration guide and validate the example

## Risks And Unknowns

- It may be tempting to over-generalize the database adapter before the first example is stable.
- Vector-backed results and relational rows may create pressure for multiple adapter shapes.
- Without good examples, the workflow may seem more abstract than the Codex repository path.

## Exit Criteria

- a technical builder can see how Atlas fits into a docs-plus-db chatbot pipeline
- the example mixes documents and structured records through one packet path
- the guide makes the Atlas boundary versus application boundary explicit
- the implementation still respects Craig Architecture layer ownership

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md` files in the same slice
- the supported docs, examples, and runtime knobs stay aligned with the implemented surface
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives `@codex review`, and any review findings are resolved on that same feature branch before human merge
- any deviations from Craig Architecture boundaries are documented explicitly rather than left implicit

## Related Artifacts

- [Context Atlas MVP Product Definition](../mvp_product_defintiion.md)
- [Context Atlas System Model](../../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)

