---
id: context-atlas-agentic-task-10-3-owner-file-and-metadata-governance
title: Task 10.3 - Owner File And Metadata Governance PR Plan
summary: Defines the PR sequence for extending owner-file and front-matter governance to the new agentic-development and repo-management surfaces.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, __ai__, metadata]
related:
  - ../story_10_validation_governance_and_drift_control.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Ontology/base_metadata.md
supersedes: []
---

# Task 10.3 - Owner File And Metadata Governance PR Plan

## Objective

Define how owner-file governance and front matter metadata expectations extend
to the new agentic-development and repo-management surfaces.

## Task Status

PLANNED

## Inputs

- [Story 10 - Validation, Governance, And Drift Control](../story_10_validation_governance_and_drift_control.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [base_metadata](../../../../Authoritative/Ontology/base_metadata.md)
- current repo `__ai__.md` and metadata-governance patterns

## Proposed Work

### PR - A: Owner-File Scope Decision

- define which agentic-development and repo-management areas need direct
  `__ai__.md` coverage and which can remain governed by the root contract
- avoid both over-fragmenting and under-governing the new surfaces
- keep the owner-file model aligned with repo-wide contract practices

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/__ai__.md`
- `docs/Authoritative/RepoManagement/__ai__.md`

#### Expected Existing Files Updated
- `__ai__.md`
- `docs/Planning/Agentic/Stories/story_10_validation_governance_and_drift_control.md`

#### Update AI files
- `.`

### PR - B: Metadata Governance Expectations

- define what front-matter fields on the new agentic and repo-management docs
  must be reviewed and kept aligned
- extend the existing metadata-governance expectations to the new canon and
  planning surfaces
- keep metadata guidance focused on discoverability and governance rather than
  changelog use

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Authoritative/AgenticDevelopment/__ai__.md`
- `docs/Authoritative/RepoManagement/__ai__.md`
- `docs/Authoritative/Ontology/base_metadata.md`
- `__ai__.template.md`

#### Update AI files
- `.`

### PR - C: Planning And Canon Reinforcement

- align the planning stack and authoritative agentic/repo-management docs with
  the owner-file and metadata expectations
- reduce the chance that later Tasks bypass governance because the surface
  feels "just docs"
- document any additional local owner files that should wait until concrete
  runtime assets exist

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/README.md`
- `docs/Planning/Agentic/agentic_development_product_definition.md`
- `docs/Planning/Agentic/Stories/story_10_validation_governance_and_drift_control.md`
- `docs/Authoritative/AgenticDevelopment/README.md`
- `docs/Authoritative/RepoManagement/README.md`

#### Update AI files
- `.`

## Sequencing

- define owner-file scope first
- define metadata expectations second
- reinforce the planning and canonical surfaces third

## Risks And Unknowns

- The agentic-development and repo-management surfaces may become
  under-governed if owner-file scope stays too thin.
- Too many local owner files may create maintenance overhead if added too
  early.
- Metadata may drift if the new surfaces are not brought into the same
  discipline as the rest of the repo.

## Exit Criteria

- owner-file scope for the agentic-development and repo-management surfaces is
  explicit
- metadata-governance expectations are explicit
- later Tasks know how the new surfaces fit into repo-wide documentation
  governance

## Related Artifacts

- [Story 10 - Validation, Governance, And Drift Control](../story_10_validation_governance_and_drift_control.md)
- [base_metadata](../../../../Authoritative/Ontology/base_metadata.md)
