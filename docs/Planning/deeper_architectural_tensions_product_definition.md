---
id: context-atlas-deeper-architectural-tensions-product-definition
title: Context Atlas Deeper Architectural Tensions Product Definition
summary: Defines a deeper architectural epic for the code-level Craig Architecture tensions that are currently documented, tolerated, or only partially resolved.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, architecture, craig-architecture, domain, services, infrastructure, ports]
related:
  - ../Reviews/context-atlas-architecture-review.md
  - ../Authoritative/Canon/Architecture/Craig-Architecture.md
  - ../Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
  - ../../scripts/import_boundary_rules.toml
  - ../../src/context_atlas/services/assembly.py
  - ../../src/context_atlas/domain/models/base.py
  - ../../src/context_atlas/infrastructure/assembly.py
  - ../Authoritative/Identity/Context-Atlas-System-Model.md
supersedes: []
---

# Context Atlas Deeper Architectural Tensions Product Definition

## Objective

Define the deeper architectural Epic for the Craig Architecture tensions that
are real, documented, and currently tolerated in the codebase, but not yet
cleanly resolved.

This Epic is successful only if each major tension ends in one of three
explicit outcomes:

- refactored away
- intentionally ratified as a project-specific deviation
- or left in place with sharper documentation, tests, and validation so the
  tradeoff is owned rather than accidental

The goal is not to chase abstract architectural purity. The goal is to decide
which tensions are worth paying down and which ones Context Atlas should
formally own as part of its working design.

## Inputs

- [Context Atlas Architecture Review](../Reviews/context-atlas-architecture-review.md)
- [Craig Architecture](../Authoritative/Canon/Architecture/Craig-Architecture.md)
- [Craig Architecture - Python](../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- current import-boundary enforcement in [scripts/import_boundary_rules.toml](../../scripts/import_boundary_rules.toml)
- current service orchestration in [src/context_atlas/services/assembly.py](../../src/context_atlas/services/assembly.py)
- current domain model base in [src/context_atlas/domain/models/base.py](../../src/context_atlas/domain/models/base.py)
- current infrastructure composition helpers in [src/context_atlas/infrastructure/assembly.py](../../src/context_atlas/infrastructure/assembly.py)

The highest-signal tensions currently called out are:

- infrastructure currently acts as both config/logging layer and concrete
  wiring layer
- Pydantic is intentionally baked into the domain core despite Canon guidance
  that treats it as better suited to boundaries
- service-facing ports such as `CandidateRetriever` live in `services/` rather
  than further inward
- the service imports and uses `estimate_tokens` directly from a domain policy
  implementation utility
- runtime-capacity and related planning/governance inputs still need clearer
  validation and ratified ownership boundaries

## Proposed Work

### Thesis

Context Atlas has already done the most important architectural thing
correctly: dependency direction is mostly preserved and mechanically checked.

The remaining tensions are not proof that the architecture failed. They are the
secondary and tertiary decisions that become visible only after the primary
layering is working. That is why this Epic should be deeper, slower, and more
decision-driven than the quick-wins or runtime-model Epics.

### Product Shape

This Epic should preserve the current working engine while making its
architectural deviations explicit.

Where possible, the work should prefer:

- clear formalization of composition boundaries
- clearer placement of inward-owned contracts
- consistency in how domain artifacts and policy objects are modeled
- explicit validation of planning/governance inputs that are meant to be
  architecture-relevant rather than merely documentary

But this Epic should also be willing to conclude that a current deviation is
acceptable if the tradeoff is justified and the repo stops pretending otherwise.

### Core Capability Areas

This Epic should establish or strengthen these capability areas:

- a cleaner distinction between infrastructure-as-runtime-mechanics and
  infrastructure-as-composition boundary
- a decision about whether Pydantic in the domain is a temporary compromise, a
  long-term project standard, or a split model that needs a clearer rule
- inward ownership of ports/contracts where Craig Architecture expects those
  contracts to live, or an explicit ratification that structural typing plus
  service-owned Protocols is the chosen local tradeoff
- better encapsulation of token-estimation behavior so the service is not
  coupled to domain policy utilities more than necessary
- stronger validation and ownership of machine-readable planning/governance
  inputs such as runtime capacity when those inputs are meant to influence real
  decomposition behavior

### Epic Structure

This document should be treated as a rough-draft deeper-architecture Epic.

The current draft Story shape is:

- Story 1: Infrastructure Composition Boundary And Outer-Layer Responsibilities
- Story 2: Inward Port Ownership And Service/Adapter Contract Placement
- Story 3: Domain Modeling Standard And Pydantic Deviation Decision
- Story 4: Policy Encapsulation And Token-Estimation Boundary Cleanup
- Story 5: Planning/Governance Input Validation For Runtime Capacity And Related Artifacts

This Story set is deliberately decision-heavy. Some Stories may end in code
refactors; others may end in ratified documentation plus targeted guardrails.

### Target Users

`1. Core maintainer`

- Primary job: keep the architecture truthful as the engine grows
- Value from this Epic: gets explicit resolution of tensions that are currently
  understood informally but not fully settled

`2. Architecture reviewer`

- Primary job: evaluate whether Craig Architecture is real in the code or only
  decorative in the docs
- Value from this Epic: sees which tensions were intentionally accepted versus
  simply left ambiguous

`3. Future contributor touching core seams`

- Primary job: change services, domain policies, adapters, or infrastructure
  without accidentally deepening known boundary leaks
- Value from this Epic: gets more explicit rules about where ports,
  composition, and domain validation belong

## Deliverables

This Epic should ultimately produce:

- a clearer composition-boundary story around `infrastructure/`
- a decided position on domain-layer Pydantic use and policy-model consistency
- a cleaner or more explicitly justified placement of inward-owned ports
- tighter policy encapsulation where direct service-to-utility coupling is no
  longer desirable
- stronger validation and governance around planning inputs that claim to be
  architecture-relevant

## Non-Goals For This Epic

- redesigning the whole shared engine into a different architecture
- undoing working hardening or runtime-materialization work just to satisfy
  abstract purity concerns
- broad product-facing documentation cleanup already captured in the
  low-hanging-fruit Epic
- protocol, skill, or platform-binding work that belongs in the agentic
  runtime-model Epic

## Open Questions

- Should the infrastructure/composition tension be solved by subdivision inside
  `infrastructure/`, by a new outward composition package, or by explicit
  ratification of the current shape?
- Is Pydantic in the domain a deviation that should remain project policy, or
  is the Canon guidance itself ready to change?
- Would moving ports inward materially improve the architecture, or would it
  mostly create churn around Protocol definitions that already work
  structurally?
- Is runtime-capacity validation best treated as architecture enforcement,
  agentic/governance enforcement, or both?
