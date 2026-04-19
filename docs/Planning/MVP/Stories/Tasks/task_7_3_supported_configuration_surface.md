---
id: context-atlas-mvp-task-7-3-supported-configuration-surface
title: Task 7.3 - Supported Configuration Surface PR Plan
summary: Defines the PR sequence for deciding which hidden starter defaults should remain internal and which should become supported env-backed runtime knobs.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-19
owners: [core]
tags: [mvp, task, pr-plan, configuration, env, defaults]
related:
  - ../story_7_mvp_readiness_hardening.md
  - ../../../Reviews/MVP/mvp_readiness_assessment.md
  - ../../mvp_product_defintiion.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 7.3 - Supported Configuration Surface PR Plan

## Objective

Audit the hidden starter-policy and service defaults so Atlas has a clearer boundary between internal implementation constants and supported runtime knobs.

## Task Status

IMPLEMENTED

## Inputs

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
- current runtime settings surface in `.env.example`
- current settings models under `src/context_atlas/infrastructure/config/`

## Current Assessment

- `src/context_atlas/domain/policies/ranking.py`
  - `_DEFAULT_MINIMUM_SCORE` already maps to `CONTEXT_ATLAS_RANKING_MINIMUM_SCORE`; it does not need a new env key, though the default ownership could be consolidated later.
  - `_AUTHORITY_BONUS_BY_LEVEL` and `_AUTHORITY_ORDER` should stay in code because they define starter ranking semantics, not a simple operator-facing scalar knob.
  - `_RANKED_SIGNAL` should stay in code because it is an internal trace/signal marker rather than a supported product setting.
- `src/context_atlas/domain/policies/memory.py`
  - `_DEFAULT_MINIMUM_EFFECTIVE_SCORE` already maps to `CONTEXT_ATLAS_MEMORY_MIN_EFFECTIVE_SCORE`; it does not need a new env key.
  - `_DEFAULT_QUERY_BOOST_WEIGHT` already maps to `CONTEXT_ATLAS_MEMORY_QUERY_BOOST_WEIGHT`; it does not need a new env key.
  - The memory module would benefit more from one clear default authority than from adding more env surface.
- `src/context_atlas/services/assembly.py`
  - `_DOCUMENT_SLOT_NAME` and `_MEMORY_SLOT_NAME` should stay in code because they are canonical slot identifiers, not operator-level configuration.
  - `_DEFAULT_MEMORY_BUDGET_FRACTION` is the strongest candidate for promotion into validated settings and `.env.example`, because it changes the visible default budget behavior for callers who rely on the starter budget profile.

## Proposed Work

### PR - A: Configuration-Surface Inventory And Decision Record

- turn the constant audit into one explicit decision record
- align planning, review, and product docs around which defaults are intentionally supported
- avoid adding env knobs before the supported-surface decision is written down

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Reviews/MVP/mvp_readiness_assessment.md`
- `README.md`
- `docs/Guides/getting_started.md`

#### Update AI files
- `.`

### PR - B: Promote Approved Runtime Knobs

- if the audit confirms promotion, add the chosen knob or knobs to the validated settings surface
- keep unsupported semantic mappings and internal identifiers in code
- update tests so the env-backed defaults and starter wiring stay aligned

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `.env.example`
- `src/context_atlas/infrastructure/config/settings.py`
- `src/context_atlas/infrastructure/config/environment.py`
- `src/context_atlas/infrastructure/assembly.py`
- `src/context_atlas/services/assembly.py`
- `tests/test_config_observability.py`
- `tests/test_context_assembly_service.py`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`
- `src/context_atlas/services/`
- `tests/`

### PR - C: Supported-Surface Reinforcement

- update docs and owner files so the supported knob surface is explicit
- call out which hidden constants remain internal on purpose
- make sure `.env.example` remains a truthful contract rather than a speculative wishlist

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `README.md`
- `.env.example`
- `__ai__.md`
- `src/context_atlas/infrastructure/__ai__.md`

#### Update AI files
- `.`
- `src/context_atlas/infrastructure/`

## Sequencing

- document the supported-surface decision first
- promote only the approved knob surface second
- reinforce docs and owner files last

## Risks And Unknowns

- Exposing too many knobs can make the MVP surface harder to govern.
- Hidden defaults that remain in code may still need better naming or placement even if they should not become env keys.
- Configuration work can accidentally drift into refactoring-for-refactoring's-sake if the supported-surface goal is not kept explicit.

## Exit Criteria

- the hidden defaults under review are classified as internal or env-backed
- `.env.example` and validated settings reflect only the supported runtime knobs
- the product docs explain the supported starter configuration surface clearly

## Implementation Notes

- The supported env-backed starter budget-allocation knob is now
  `CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION`.
- Ranking authority tables, ranking signal names, memory-scoring semantics, and
  canonical slot identifiers remain internal by design.
- That supported-surface decision is now part of the standing MVP boundary and
  the Story 7 proof baseline.

## Related Artifacts

- [Story 7 - MVP Readiness Hardening](../story_7_mvp_readiness_hardening.md)
- [Context Atlas MVP Readiness Assessment](../../../Reviews/MVP/mvp_readiness_assessment.md)
