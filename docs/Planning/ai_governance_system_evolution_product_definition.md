---
id: context-atlas-ai-governance-system-evolution-product-definition
title: Context Atlas AI Governance System Evolution Product Definition
summary: Defines a rough-draft Epic for strengthening the __ai__.md governance system around prose correctness, governed dirt, verification ergonomics, and durable owner-file authoring.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, ai-governance, owner-files, freshness, verification, ergonomics]
related:
  - ../Reviews/context-atlas-ai-governance-review.md
  - ../Reviews/context-atlas-agentic-review.md
  - ../../__ai__.md
  - ../../__ai__.template.md
  - ../../scripts/check_ai_docs.py
  - ../../scripts/ai_verify_contracts.py
  - ../../scripts/validate_ai_docs.py
  - ../../scripts/check_import_boundaries.py
  - ../../scripts/preflight.py
  - ../../scripts/import_boundary_rules.toml
  - ../../.github/workflows/ai-verify-folder-contracts.yml
  - ../../.github/workflows/ai-last-verified.yml
  - ./completed/task_ai_owner_file_compaction_and_hygiene.md
supersedes: []
---

# Context Atlas AI Governance System Evolution Product Definition

## Objective

Define the next Epic for the `__ai__.md` governance system so that Context
Atlas keeps the strengths of the current owner-file model while addressing the
main weaknesses surfaced by the recent review:

- prose correctness is still only weakly proven
- the system has no sanctioned path for intentional temporary boundary dirt
- enforcement can create avoidable friction against productive architectural
  exploration
- owner-file authoring and verification should stay rigorous without turning
  into a second source of cognitive drag

This Epic is successful only if the governance system becomes stronger in two
directions together:

- more trustworthy, by proving the most important claims better and making the
  limits of CI verification clearer
- more usable, by giving contributors a governed path for intentional dirt and
  a cleaner authoring model for owner files

The goal is not to replace the `__ai__.md` system. The goal is to make the
system more truthful, more ergonomic, and more aligned with the Craig
Architecture idea that codebases sometimes need to be dirty in a good way
before the right boundary is fully understood.

## Inputs

- [AI Governance Review](../Reviews/context-atlas-ai-governance-review.md)
- [Context Atlas Agentic Review](../Reviews/context-atlas-agentic-review.md)
- [Root __ai__.md](../../__ai__.md)
- [__ai__.template.md](../../__ai__.template.md)
- [check_ai_docs.py](../../scripts/check_ai_docs.py)
- [ai_verify_contracts.py](../../scripts/ai_verify_contracts.py)
- [validate_ai_docs.py](../../scripts/validate_ai_docs.py)
- [check_import_boundaries.py](../../scripts/check_import_boundaries.py)
- [preflight.py](../../scripts/preflight.py)
- [import_boundary_rules.toml](../../scripts/import_boundary_rules.toml)
- [ai-verify-folder-contracts.yml](../../.github/workflows/ai-verify-folder-contracts.yml)
- [ai-last-verified.yml](../../.github/workflows/ai-last-verified.yml)
- [Task - __ai__ Owner-File Compaction And Hygiene PR Plan](./completed/task_ai_owner_file_compaction_and_hygiene.md)

The review and follow-up discussion currently point at these high-value gaps:

- freshness and contract execution are useful, but they do not prove prose
  correctness
- the visual language around `Last Verified (CI)` can imply more confidence
  than the system actually proves
- `Allowed Dependencies` and related checks are strong at blocking violations
  but weak at managing intentional temporary exceptions
- there is no sanctioned `dirty in a good way` mechanism comparable to a
  governed waiver path
- the system is still too implicit about its authority relationship to the
  generated agent runtime layer
- scope globs are useful declarations, but the repo still lacks stronger
  confidence that owner-file coverage assertions stay complete as surfaces grow
- freshness detection and contract execution are complementary, but their
  trigger semantics are not yet as tightly aligned as they could be
- owner files risk drifting toward long-form explanation or append-only history
  unless their authoring shape stays disciplined
- CI writeback and owner-file refresh behavior are effective but can add
  friction as the repo evolves

## Proposed Work

### Thesis

Context Atlas should keep the current owner-file system, not retreat from it.

The nearest-owner model, diff-based freshness checks, executable verification
contracts, and folder-local contract surfaces are all real strengths. The next
step is not to remove governance. It is to evolve governance so it better
matches reality:

- some claims can be mechanically checked
- some claims are durable human-judgment contracts
- some current violations are intentional and temporary rather than accidental

This Epic should make those distinctions clearer and more governable instead of
pretending the current system already proves more than it does.

### Product Shape

This Epic should preserve the current shape of the governance system:

- nearest owner file wins
- freshness is diff-scoped and owner-file-aware
- verification contracts are executable
- CI and local preflight remain the primary enforcement paths

It should also make one authority rule explicit:

- `__ai__.md` governance is authoritative for repo-local contribution behavior
- generated agent runtime assets may specialize role/mode/protocol behavior for
  that repo context
- but generated runtime assets must never weaken, bypass, or reinterpret
  nearest owner-file governance as optional

But the next version of that system should add or strengthen:

- clearer truth-status signaling for owner-file claims
- a governed-dirt path for temporary intentional violations
- stronger ergonomics around how owner files are written, refreshed, and read
- better distinction between what CI proved and what humans still need to
  reason about

### Core Capability Areas

This Epic should establish or strengthen these capability areas:

- a clearer claim discipline for owner files so prose stays closer to
  structured contract and farther from essay-like summary
- a clearer boundary statement between owner-file governance and the generated
  runtime layer so contributors and future agent bindings know which layer has
  repo-local authority
- lightweight prose-correctness support for the highest-value claim types:
  paths, scripts, exports, environment keys, public API names, and other
  assertions that can actually be checked
- stronger scope-confidence support so owner-file coverage is less dependent on
  human memory alone when folder structure evolves
- clearer visual and textual language around `Last Verified (CI)` so it
  remains obvious that command success is not the same thing as human review
- a governed dirt model built around lightweight code annotations such as
  `# ai-dirt: <reason>` and richer owner-file-side rationale
- a queryable register or equivalent governed surface for intentional
  violations so dirt can be managed rather than hidden
- clearer contract-trigger semantics so contributors can tell what contract
  execution a changed governed file will actually cause
- verification and refresh ergonomics that keep the system useful without
  making exploratory boundary work disproportionately expensive
- continued owner-file compaction so repo-level and layer-level owner files
  remain curated contracts rather than append-only changelogs

### Epic Structure

This document should be treated as a rough-draft AI-governance Epic.

The current draft Story shape is:

- Story 1: Prose Correctness And Claim Discipline
- Story 2: Governed Dirt And Intentional Violations
- Story 3: Freshness, Scope Confidence, And Truth Signaling
- Story 4: Verification And CI Ergonomics
- Story 5: Owner-File Authoring Shape And Long-Term Hygiene

This Story set is intentionally governance-system-specific. It should not be
absorbed by the deeper architectural Epic just because import boundaries are
one of the enforcement surfaces, and it should not be folded into product docs
cleanup just because some owner-file prose is documentation.

### Target Users

`1. Core maintainer`

- Primary job: keep the governance system useful, truthful, and proportionate
- Value from this Epic: gets a more trustworthy and less brittle operating
  model for AI-assisted contribution governance

`2. Contributor doing exploratory architecture work`

- Primary job: test or temporarily bend a boundary without hiding the fact that
  it is a controlled violation
- Value from this Epic: gets a sanctioned governed-dirt path instead of a
  binary choice between silent violation and hard revert

`3. Reviewer auditing owner files`

- Primary job: understand what the repo proved versus what it merely asserts
- Value from this Epic: sees cleaner owner files, stronger claim discipline,
  and clearer truth-status signaling

`4. Future governance-system adopter`

- Primary job: decide whether the `__ai__.md` model is credible and reusable
- Value from this Epic: sees a system that acknowledges its limits while still
  proving meaningful things mechanically

## Deliverables

This Epic should ultimately produce:

- a clearer owner-file claim model with better distinction between checked
  facts, durable human contracts, and future-state notes
- an explicit repo-local authority rule that keeps owner-file governance above
  generated runtime specialization for contribution behavior
- stronger support for checking the highest-value prose claims rather than only
  detecting freshness
- better scope-confidence and contract-trigger clarity so governance behavior
  is easier to predict and trust
- a governed-dirt mechanism with lightweight code annotation and richer
  owner-file-side rationale
- clearer semantics around what `Last Verified (CI)` means and does not mean
- continued compaction and hygiene improvements so owner files stay readable as
  the repo grows

## Non-Goals For This Epic

- replacing the `__ai__.md` system with a different governance model
- trying to make AI or CI automatically determine whether freeform prose is
  globally true
- weakening import-boundary or freshness enforcement into mere suggestion
- solving the deeper code-level Craig Architecture tensions inside
  `src/context_atlas/`
- turning every owner file into a database-backed policy registry

## Open Questions

- Should governed dirt be recorded directly inside owner files, in a generated
  report, or in both with one as the authoritative source?
- Should `# ai-dirt: <reason>` support only import-boundary exceptions first,
  or should it be designed from day one for broader governance violations?
- How should scope-confidence checks balance stronger coverage assertions
  against the cost of keeping those assertions current as the repo grows?
- How much owner-file prose should be converted into more structured claim
  shapes before the system becomes harder to author than it is worth?
- Is the current `Last Verified (CI)` auto-stamping workflow the right trust
  signal long term, or should it evolve into a different visual language as the
  contributor base grows?
