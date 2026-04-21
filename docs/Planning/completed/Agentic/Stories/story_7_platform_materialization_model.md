---
id: context-atlas-agentic-story-7-platform-materialization-model
title: Story 7 - Platform Materialization Model
summary: Defines how portable and project-specific agentic concepts are translated into concrete runtime assets without making platform files the source of truth.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, materialization, portability, templates]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ./story_5_protocol_model.md
  - ./story_6_runtime_capacity_and_parallel_decomposition.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Template-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Discovery-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Materialization-Traceability-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Drift-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Validation-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Boundary-Model.md
supersedes: []
---

# Story 7 - Platform Materialization Model

## Objective

Define the generic materialization model that explains how portable canon and
project-specific agentic bindings should become concrete runtime assets for a
given AI environment without making those runtime assets authoritative.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Materialization Boundary Model](../../../Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md)
- [Template Model](../../../Authoritative/Canon/AgenticDevelopment/Template-Model.md)
- [Discovery Model](../../../Authoritative/Canon/AgenticDevelopment/Discovery-Model.md)
- [Materialization Traceability Model](../../../Authoritative/Canon/AgenticDevelopment/Materialization-Traceability-Model.md)
- [Drift Model](../../../Authoritative/Canon/AgenticDevelopment/Drift-Model.md)
- [Validation Model](../../../Authoritative/Canon/AgenticDevelopment/Validation-Model.md)
- [Boundary Model](../../../Authoritative/Canon/AgenticDevelopment/Boundary-Model.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Story 6 - Runtime Capacity And Parallel Decomposition](./story_6_runtime_capacity_and_parallel_decomposition.md)
- Current repository experience with authoritative docs, project bindings, and executable operational artifacts

## Proposed Tasks

### Task 1: Materialization Concepts And Boundaries

- bind Story 7 to one explicit materialization-boundary model instead of
  letting later platform stories restate the source-of-truth rules ad hoc
- define what it means to materialize an abstract agentic concept into a
  platform-specific runtime artifact
- keep the source-of-truth boundary explicit so generated or maintained runtime
  files remain downstream of canon and project bindings
- define the inputs and outputs of a materialization step in a portable way
- treat Story 1 and the authoritative boundary model as upstream definitions
  rather than re-describing those layers in materialization language

### Task 2: Generic Template Model

- define the generic template surfaces needed for agents, skills, modes,
  protocols, and related runtime guidance
- define those template surfaces as portable materialization contracts before
  any platform story maps them into concrete file layouts
- keep the template model platform-agnostic so later platform bindings can map
  it into vendor-specific file shapes
- make the template model traceable back to the portable canon and project
  profile

### Task 3: Discovery And Folder-Convention Abstractions

- define the abstract discovery requirements that a runtime materialization
  must satisfy
- bind those discovery requirements to one portable discovery model before any
  environment story chooses concrete folders or file names
- separate those abstract discovery needs from platform-specific folder naming
  conventions
- position later platform stories to bind discovery rules without redefining
  materialization itself

### Task 4: Traceability And Regeneration Expectations

- define how a human operator or later validation step should tell whether
  runtime artifacts still match the authoritative docs
- bind those reviewer expectations to one portable traceability model before
  any platform story chooses a concrete metadata or manifest strategy
- clarify whether materialized assets are hand-maintained, generated, or
  partially generated
- make regeneration and update expectations explicit before the first concrete
  platform binding lands

## Sequencing

- define the materialization boundary and source-of-truth rules
- define the generic template model
- define abstract discovery expectations
- define traceability and regeneration expectations for later platform work

## Risks And Unknowns

- Materialization docs could drift into Codex-specific instructions too early.
- The Story could over-engineer generation before the repository even needs
  full automation.
- If traceability rules are weak, runtime artifacts may drift quickly from the
  canon and project bindings.

## Exit Criteria

- Context Atlas has a documented generic materialization model
- the boundary between authoritative docs and runtime artifacts is explicit
- the template/discovery model is defined without assuming one vendor
- the generic template model is explicit enough that Story 8 can bind to it
  instead of inventing a runtime-shaped substitute
- the abstract discovery model is explicit enough that Story 8 can choose
  folders, manifests, or indexes without inventing alternate discovery
  semantics
- the traceability and regeneration model is explicit enough that Story 8 can
  declare provenance and maintenance mode without inventing a platform-local
  provenance scheme
- Story 8 binds through one explicit Identity-layer Codex entrypoint before it
  defines downstream folder layouts, templates, or governance hooks
- Story 8's concrete Codex folder and file conventions remain explicitly
  downstream of the portable discovery and template model rather than becoming
  alternate discovery canon
- later platform-specific stories can bind to the model instead of inventing
  their own materialization rules
- Story 8 and later validation work inherit one clear upstream-versus-downstream
  change model instead of reconstructing it from planning prose
- later drift and validation work can reason about materialized assets through
  one stable vocabulary instead of inventing Codex-only terminology

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the materialization model stays platform-agnostic and does not leak Codex-only
  assumptions into the generic layer
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge
- traceability between canon, project bindings, and runtime artifacts is
  explicit enough to support later validation and drift-control work
- the Story continues to read as downstream materialization guidance rather
  than a second portable canon

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Materialization Boundary Model](../../../Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md)
- [Template Model](../../../Authoritative/Canon/AgenticDevelopment/Template-Model.md)
- [Discovery Model](../../../Authoritative/Canon/AgenticDevelopment/Discovery-Model.md)
- [Materialization Traceability Model](../../../Authoritative/Canon/AgenticDevelopment/Materialization-Traceability-Model.md)
- [Drift Model](../../../Authoritative/Canon/AgenticDevelopment/Drift-Model.md)
- [Validation Model](../../../Authoritative/Canon/AgenticDevelopment/Validation-Model.md)
- [Boundary Model](../../../Authoritative/Canon/AgenticDevelopment/Boundary-Model.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Story 6 - Runtime Capacity And Parallel Decomposition](./story_6_runtime_capacity_and_parallel_decomposition.md)

