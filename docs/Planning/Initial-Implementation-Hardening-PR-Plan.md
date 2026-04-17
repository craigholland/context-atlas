---
id: initial-implementation-hardening-pr-plan
title: Initial Implementation Hardening PR Plan
summary: Sequences the follow-up PRs needed to correct the first Context Atlas implementation's known shortcomings and normalize its modeling conventions.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-17
owners: [core]
tags: [planning, hardening, migration, pydantic, cleanup]
related:
  - ./Context-Engine-Conversion-PR-Plan.md
  - ../Authoritative/Identity/Context-Atlas-Charter.md
  - ../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../Authoritative/Architecture/Craig-Architecture.md
  - ../Authoritative/Architecture/Craig-Architecture-Python.md
  - ../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Initial Implementation Hardening PR Plan

## Objective

Address the known shortcomings in the first Context Atlas implementation after the initial `context-engine` conversion landing.

This follow-up plan is intended to harden correctness, remove planning and implementation drift, and normalize the project's structured-data modeling approach so future contributors are not left guessing between `dataclass` and Pydantic patterns.

This plan assumes the following hardening posture:

- Fix correctness issues before adding more capability.
- Align planning and local contracts to the implementation that actually exists.
- Standardize non-trivial structured data objects on Pydantic.
- Leave only small private helper structs on `dataclass` when they do not act as canonical artifacts, policy outputs, service-boundary DTOs, or persistence/serialization surfaces.

## Inputs

- [Context Engine Conversion PR Plan](./Context-Engine-Conversion-PR-Plan.md)
- [Context Atlas Charter](../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture Python](../Authoritative/Architecture/Craig-Architecture-Python.md)
- [Documentation Ontology](../Authoritative/Ontology/Documentation-Ontology.md)
- The current first implementation under `src/context_atlas/`
- The 2026-04-17 branch review findings, especially:
  - short-term memory entries can be evicted under memory-slot budget pressure
  - the planning surface still references a `domain/events` layer that is no longer part of the live design
  - non-trivial data objects are still split between `dataclass` and Pydantic patterns

## Proposed Work

### Cross-Cutting Rules For Every PR

- Do not add new capability until the targeted hardening scope is covered by tests.
- Any PR that changes a visible runtime default must update all of:
  - `src/context_atlas/infrastructure/config/settings.py`
  - `src/context_atlas/infrastructure/config/environment.py`
  - `.env.example`
  - the relevant local `__ai__.md` files
  - tests that prove parsing and default behavior
- Any PR that changes structured-data modeling must update the relevant local `__ai__.md` files so the package contracts continue to match the real code shape.
- Reusable errors and log messages should continue to route through `domain/errors`, `domain/messages`, and `infrastructure/logging`; this plan does not reopen the direct inline-string pattern.
- Prompt-ready strings remain derived outputs. Hardening work must preserve the canonical status of packets, traces, decisions, budgets, sources, and transformations.

### Pydantic Modeling Standard For This Follow-Up

This plan assumes the following working rule:

- Use Pydantic for non-trivial structured data objects.
- Treat the following kinds of objects as non-trivial by default:
  - canonical domain artifacts
  - policy input and output objects
  - service-boundary result objects
  - adapter-facing validated DTOs
  - configuration models
- A `dataclass` may remain only when all of the following are true:
  - it is private or tightly local to one module
  - it is not part of the package's intended public surface
  - it does not need validation beyond trivial construction
  - it is not used as a serialization, persistence, or transport shape

This means the follow-up should convert the current non-trivial `dataclass` objects to Pydantic rather than leaving a mixed modeling style in place.

### Initial Conversion Inventory For Non-Trivial Data Objects

The current high-priority conversion targets include:

- `src/context_atlas/domain/models/sources.py`
  - `ContextSourceProvenance`
  - `ContextSource`
  - `ContextCandidate`
- `src/context_atlas/domain/models/budget.py`
  - `ContextBudgetSlot`
  - `ContextBudget`
- `src/context_atlas/domain/models/assembly.py`
  - `ContextAssemblyDecision`
  - `ContextTrace`
  - `ContextPacket`
- `src/context_atlas/domain/models/memory.py`
  - `ContextMemoryEntry`
- `src/context_atlas/domain/models/transformations.py`
  - `CompressionResult`
- `src/context_atlas/domain/policies/budgeting.py`
  - `BudgetRequest`
  - `BudgetAllocation`
  - `BudgetAllocationOutcome`
- `src/context_atlas/domain/policies/ranking.py`
  - `CandidateRankingOutcome`
  - `StarterCandidateRankingPolicy`
- `src/context_atlas/domain/policies/compression.py`
  - exported policy result/value objects
- `src/context_atlas/domain/policies/memory.py`
  - `MemorySelectionOutcome`
  - `StarterMemoryRetentionPolicy`

Private helper structs such as `_RankableCandidate` or `_ScoredMemoryEntry` should be reviewed individually. They may remain dataclasses only if they stay private, lightweight, and validation-light.

### PR H1: Correct Memory Budget Semantics

**Goal**

Make the starter memory model behave consistently with its stated short-term retention semantics under budget pressure.

**Main scope**

- Ensure short-term retained entries are not evicted behind older long-term entries when the memory slot is tight.
- Decide whether the correct enforcement point is:
  - ordering in `StarterMemoryRetentionPolicy.select_memory()`
  - explicit prioritization in `ContextAssemblyService._select_memory_within_budget()`
  - or both, if both are needed for clarity
- Preserve decision-trace visibility for entries that are still dropped due to memory-slot pressure.

**Cross-cutting updates**

- Update `src/context_atlas/domain/__ai__.md` and `src/context_atlas/services/__ai__.md` if the retained-ordering contract becomes more explicit.
- Add or refine error and log messages only if the hardening work introduces new observable cases.

**Verification**

- Add a regression test proving that recent short-term entries survive ahead of long-term entries under a tight memory budget.
- Add a service-level test that exercises memory selection plus memory-slot trimming together.

### PR H2: Align Plans, Contracts, And Logging Surface

**Goal**

Remove the remaining drift between the implementation and the plan/contract language around logging events and message ownership.

**Main scope**

- Update planning and local-contract docs so they describe the actual live pattern:
  - direct `LogMessage.*` constants
  - stable event names carried by those log-message constants
  - no separate `domain/events` package as a required public surface
- Remove or clarify any references that imply contributors should recreate the old `domain/events` design.

**Cross-cutting updates**

- Update:
  - `docs/Planning/Context-Engine-Conversion-PR-Plan.md`
  - relevant `__ai__.md` files
  - any tests or comments that still describe `domain/events` as live surface area

**Verification**

- Structural validation of the touched `__ai__.md` files.
- Narrow doc-consistency checks plus full preflight before merge.

### PR H3: Convert Canonical Domain Artifacts To Pydantic

**Goal**

Normalize the project's first-class canonical artifacts onto one validated modeling system.

**Main scope**

- Convert the canonical domain artifacts from `dataclass` to Pydantic models.
- Preserve current invariants and immutability expectations where appropriate.
- Prefer explicit Pydantic configuration over ad hoc `__post_init__` validation patterns.
- Ensure canonical artifacts continue to expose stable, ergonomic read-only behavior for callers.

**Cross-cutting updates**

- Update `src/context_atlas/domain/__ai__.md` and `src/context_atlas/__ai__.md` with the Pydantic-first modeling rule.
- Update tests that currently assume dataclass-specific behavior.

**Verification**

- Domain tests for all current invariants still pass.
- Add coverage for `model_validate`, `model_dump`, and immutability expectations on the canonical public artifacts.

### PR H4: Convert Policy Inputs, Outputs, And Non-Trivial Policy Objects To Pydantic

**Goal**

Finish the modeling normalization by converting policy-surface objects that shape service orchestration and decision flow.

**Main scope**

- Convert non-trivial policy input/output objects to Pydantic.
- Convert starter policy configuration objects to Pydantic where they act as validated structured state rather than mere behavior holders.
- Keep only truly private helper structs as dataclasses if they still satisfy the lightweight-helper rule.

**Cross-cutting updates**

- Update local contracts in:
  - `src/context_atlas/domain/__ai__.md`
  - `src/context_atlas/services/__ai__.md`
  - `tests/__ai__.md`
- Revisit any serialization or copy behavior that should now use Pydantic idioms consistently.

**Verification**

- Tests for ranking, budgeting, compression, and memory outcomes still pass after conversion.
- Add focused tests around validated construction and rejected invalid inputs for the newly converted models.

### PR H5: Re-Harden Services, Adapters, And Rendering Against The New Model Surface

**Goal**

Make the assembly path and adapter path feel clean after the model conversion rather than merely still passing.

**Main scope**

- Update service orchestration, rendering, and adapters to use the Pydantic-based model surface consistently.
- Remove any leftover dataclass-era assumptions, helper conversions, or mutation workarounds.
- Recheck the filesystem adapter, retrieval adapter, and assembly service for any model friction introduced by the conversion.

**Cross-cutting updates**

- Update:
  - `src/context_atlas/adapters/__ai__.md`
  - `src/context_atlas/services/__ai__.md`
  - `src/context_atlas/rendering/__ai__.md`
  - `src/context_atlas/__ai__.md`
- Confirm the root `__ai__.md` still describes the repo-level preflight accurately after the hardening work.

**Verification**

- Full preflight.
- End-to-end tests covering assembly, rendering, retrieval, memory, and filesystem classification on the converted model surface.

## Sequencing

The intended order is:

1. PR H1 fixes the concrete memory correctness bug first.
2. PR H2 removes plan and contract drift so the hardening phase starts from accurate documentation.
3. PR H3 converts canonical domain artifacts to Pydantic.
4. PR H4 converts policy and service-boundary structured objects to Pydantic.
5. PR H5 hardens services, adapters, rendering, and tests against the normalized model surface.

This order is deliberate:

- correctness issues should be fixed before broad refactors
- documentation drift is cheapest to remove before more work stacks on top
- canonical public artifacts should be normalized before policy surfaces that depend on them
- services and adapters should be re-hardened only after the stable model surface is in place

## Risks And Unknowns

- The memory-priority fix can be implemented in more than one place, and the wrong split could leave the semantics implicit rather than explicit.
- Pydantic conversion may expose places where current tests accidentally depend on dataclass behavior such as tuple coercion, frozen semantics, or direct construction without explicit validation.
- Some starter policy objects may be better represented as ordinary behavioral classes with Pydantic config sub-models rather than full Pydantic behavior objects; this should be decided deliberately rather than by habit.
- The current package exports may need small cleanup after the model conversion to keep the public surface obvious.
- Local `__ai__.md` files may drift quickly during the conversion unless they are updated in the same PRs as the modeling changes.

## Exit Criteria

This plan is complete enough to supersede once the following are true:

- short-term memory retention semantics remain intact under memory-slot budget pressure
- the planning surface no longer refers contributors to a `domain/events` layer that is not part of the live implementation
- non-trivial structured data objects use Pydantic consistently across the domain and policy surfaces
- only small, private, validation-light helper structs remain as dataclasses
- services, adapters, and rendering work cleanly against the normalized model surface
- local `__ai__.md` contracts describe the actual modeling and logging conventions now in use
- the repo preflight and the focused test suites pass after the hardening work

## Related Artifacts

- [Context Engine Conversion PR Plan](./Context-Engine-Conversion-PR-Plan.md)
- [Context Atlas Charter](../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture Python](../Authoritative/Architecture/Craig-Architecture-Python.md)
- [Documentation Ontology](../Authoritative/Ontology/Documentation-Ontology.md)
