---
id: context-atlas-deeper-architectural-tensions-product-definition
title: Context Atlas Deeper Architectural Tensions Product Definition
summary: Defines a deeper, decision-driven Epic for the code-level Craig Architecture tensions inside src/context_atlas that are currently documented, tolerated, or only partially resolved.
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
are real, documented, and currently tolerated inside `src/context_atlas/`, but
not yet cleanly resolved.

This Epic is successful only if each major tension ends in one of three
explicit outcomes:

- refactored away
- intentionally ratified as a project-specific deviation
- or left in place with sharper documentation, tests, and validation so the
  tradeoff is owned rather than accidental

The goal is not to chase abstract architectural purity, and it is not to
re-open already-separate planning horizons around product onboarding, agentic
runtime modeling, consumer packaging, or `__ai__.md` governance. The goal is
to decide which code-level tensions are worth paying down and which ones
Context Atlas should formally own as part of its working design.

Every Story in this Epic should therefore answer a deeper question than
"should we clean this up?" It should answer:

- what the actual current code truth is
- what Craig Architecture guidance says the ideal shape would be
- whether the gap is harmful enough to justify refactor cost now
- and what proof is required if Context Atlas decides the current deviation is
  acceptable on purpose

## Inputs

- [Context Atlas Architecture Review](../Reviews/context-atlas-architecture-review.md)
- [Context Atlas Agentic Review](../Reviews/context-atlas-agentic-review.md)
- [Craig Architecture](../Authoritative/Canon/Architecture/Craig-Architecture.md)
- [Craig Architecture - Python](../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- current import-boundary enforcement in [scripts/import_boundary_rules.toml](../../scripts/import_boundary_rules.toml)
- current service orchestration in [src/context_atlas/services/assembly.py](../../src/context_atlas/services/assembly.py)
- current domain model base in [src/context_atlas/domain/models/base.py](../../src/context_atlas/domain/models/base.py)
- current infrastructure composition helpers in [src/context_atlas/infrastructure/assembly.py](../../src/context_atlas/infrastructure/assembly.py)
- current runtime-capacity input in [docs/Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml](../Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml)

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

This Epic should not behave like a grab-bag for every review finding that
sounds architectural. It is specifically about the code-level shape and
ownership model of the shared engine under `src/context_atlas/`.

### Scope Boundary

This Epic is in scope for:

- engine-layer package and dependency shape
- inward versus outward ownership of contracts and utilities
- modeling standards inside the domain and policy layers
- ownership and validation of machine-readable inputs that affect runtime or
  decomposition behavior in a code-meaningful way
- explicit ratification of local deviations from Craig Architecture when those
  deviations are chosen, stable, and worth keeping

This Epic is not in scope for:

- product-facing docs cleanup that is already carried by the low-hanging Epic
- Codex/Claude platform-binding placement, protocol/runtime-surface design, or
  generated-asset fidelity work that belongs in the agentic-runtime Epic
- `__ai__.md` authority, prose correctness, governed dirt, or CI ergonomics as
  a governance-system problem
- consumer packaging, publication, or install-path questions

The most important architectural discipline in this Epic is therefore not
"purity." It is scope control.

### Decision Standard

Each Story in this Epic should end with an explicit decision record in one of
these forms:

- `refactor`: the current shape is materially wrong enough to change now
- `ratify`: the current shape is a conscious local tradeoff and should stop
  pretending to be temporary
- `defer with guardrails`: the current shape is still unresolved, but the repo
  should add enough tests, owner-file language, or validation to keep the
  ambiguity from spreading

For any of those outcomes, the Story should be considered incomplete unless it
also names:

- the concrete code boundary under discussion
- the canonical guidance being weighed against
- the chosen rationale
- the practical enforcement or documentation change that makes the decision
  durable

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
That is acceptable as long as the outcome is explicit and durable.

#### Story 1: Infrastructure Composition Boundary And Outer-Layer Responsibilities

This Story should answer whether `infrastructure/` is one coherent outer-layer
boundary or whether it is currently carrying two responsibilities that should
be split:

- runtime mechanics such as config, logging, and environment-facing helpers
- concrete assembly/composition wiring for the starter surface

The key decision is not simply "is this folder too big?" The key decision is:

- does the current shape make outward composition clearer
- or does it hide an implicit composition layer inside a general
  infrastructure package

Likely acceptable outcomes:

- ratify `infrastructure/` as the chosen outer composition boundary and state
  that clearly in the authoritative docs and owner files
- or subdivide it so runtime mechanics and concrete composition are no longer
  bundled together by convenience alone

Evidence to look for:

- whether concrete adapter choices are proliferating there
- whether startup/composition concerns are beginning to diverge from pure
  runtime-mechanics concerns
- whether import-boundary rules should explicitly represent the chosen shape

#### Story 2: Inward Port Ownership And Service/Adapter Contract Placement

This Story should decide whether service-owned `Protocol` definitions are a
pragmatic local standard or an architectural smell that should be corrected.

The current tension is not merely stylistic. It affects:

- where adapter authors look for the contract they satisfy
- whether ports are inward-owned in the Craig Architecture sense
- whether import-boundary enforcement is catching the right kinds of outward
  dependency leaks

Likely acceptable outcomes:

- move selected ports inward into a more explicit domain-owned contract
  surface
- or ratify service-owned structural Protocols as the local standard and stop
  implying that a more inward placement is still the assumed future state

Evidence to look for:

- whether adapters need to know too much about `services/`
- whether moving ports inward would materially simplify the architecture or
  merely create churn
- whether import-boundary rules need strengthening to match the chosen answer

#### Story 3: Domain Modeling Standard And Pydantic Deviation Decision

This Story should make the repo stop speaking with two voices about domain
modeling.

Right now the codebase has effectively chosen:

- frozen Pydantic-backed canonical artifacts
- and at least some Pydantic-backed policy/config surfaces

while parts of the Canon still frame Pydantic as boundary-first technology.

The decision here is not "Pydantic good or bad." The decision is:

- is Context Atlas intentionally a project that uses validated Pydantic models
  as its domain standard
- or is the current state a tolerated deviation on the way to a different
  long-term model

Likely acceptable outcomes:

- ratify Pydantic-backed domain artifacts and policy objects as local project
  standard, with sharper Canon-versus-project guidance
- define a more explicit split between canonical artifacts, behavior-carrying
  policies, and boundary settings objects
- or deliberately migrate a meaningful subset away from Pydantic if the repo
  concludes the current coupling cost is too high

Evidence to look for:

- inconsistency between artifact classes and policy classes
- mismatch between Canon guidance and actual code policy
- whether the current model is creating real change friction or just
  theoretical discomfort

#### Story 4: Policy Encapsulation And Token-Estimation Boundary Cleanup

This Story should examine the narrower but more concrete coupling where the
service reaches directly for `estimate_tokens` from the compression policy
module.

This is likely the cleanest pure refactor candidate in the Epic because it is:

- small
- specific
- and easier to improve without reopening the larger architecture

The decision should be:

- should token estimation be fully encapsulated behind a policy surface
- or is the current utility export an intentional shared domain helper that
  the service is allowed to depend on directly

Likely acceptable outcomes:

- refactor the service so it no longer imports the utility directly
- or ratify the helper as a real shared domain export and make that policy
  explicit in authoritative docs and owner files

Evidence to look for:

- how tightly the service is coupled to compression implementation detail
- whether alternate token-estimation strategies would force awkward service
  changes
- whether a small seam would materially reduce leakage without needless
  indirection

#### Story 5: Planning/Governance Input Validation For Runtime Capacity And Related Artifacts

This Story should determine which machine-readable planning artifacts are
architecture-relevant enough to deserve stronger enforcement as part of the
engine's truth model.

The immediate anchor is `runtime_capacity.yaml`, but the deeper question is:

- when a machine-readable artifact shapes decomposition or runtime behavior,
  who owns its validation contract
- architecture
- agentic runtime
- governance
- or some shared boundary between them

This Story should stay focused on the code-level side of that question:

- schema truth
- validation entrypoints
- ownership boundaries
- and what the engine is allowed to assume from those artifacts

Likely acceptable outcomes:

- architecture-owned schema validation with agentic/governance reuse
- a shared validation seam with clearer ownership boundaries
- or a ratified statement that the artifact remains advisory until a later
  implementation milestone, with that limitation made explicit

Evidence to look for:

- whether the current engine already depends on the artifact semantically
- whether reviewers and docs are over-claiming validation that does not exist
- whether validation belongs in preflight, specialized tooling, or both

### Expected Outcome Profile

Based on the current review set, the most likely outcome profile is:

- Story 1: either a modest structural refactor or a strong explicit
  ratification of `infrastructure/` as the outer composition boundary
- Story 2: possibly ratification with stronger wording and enforcement, unless
  moving ports inward proves simpler than expected
- Story 3: more likely a deliberate deviation decision than a sweeping code
  migration
- Story 4: the strongest near-term refactor candidate
- Story 5: likely a shared validation-and-ownership clarification rather than
  a purely code-only refactor

That profile is not binding, but it should help keep this Epic realistic.

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

- a clearer composition-boundary story around `infrastructure/`, whether that
  means subdivision or explicit ratification
- a decided position on domain-layer Pydantic use and policy-model
  consistency, including how that choice relates to Craig Architecture canon
- a cleaner or more explicitly justified placement of inward-owned ports
- tighter policy encapsulation where direct service-to-utility coupling is no
  longer desirable
- stronger validation and ownership guidance around planning inputs that claim
  to be architecture-relevant
- explicit decision records in authoritative docs and owner files so accepted
  deviations stop reading like temporary accidents

## Non-Goals For This Epic

- redesigning the whole shared engine into a different architecture
- undoing working hardening or runtime-materialization work just to satisfy
  abstract purity concerns
- broad product-facing documentation cleanup already captured in the
  low-hanging-fruit Epic
- protocol, skill, or platform-binding work that belongs in the agentic
  runtime-model Epic
- `__ai__.md` authority, prose-correctness, governed dirt, or CI ergonomics
  work that belongs in the AI governance Epic
- namespacing policy, specialist-roster completeness policy, or Canon runtime
  placement questions that belong in the agentic-runtime Epic
- consumer packaging, publication, or install-surface decisions that belong in
  the consumer-packaging Epic

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
- When this Epic ratifies a local deviation, where should that decision live
  so future contributors see it as a stable rule instead of an undocumented
  compromise?
