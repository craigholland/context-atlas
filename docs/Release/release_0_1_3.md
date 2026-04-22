---
id: release-0-1-3
title: Release 0.1.3
summary: Records the entry-surface refinement and Codex runtime-governance release of Context Atlas, covering the layered README/guides split, richer agentic canon bindings, and manifest-driven Codex runtime materialization with drift enforcement.
doc_class: releases
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [releases, patch, version-0-1-3, documentation, codex, governance]
related:
  - ./release_0_1_2.md
  - ../Guides/README.md
  - ../Guides/context_atlas_tour.md
  - ../Authoritative/Canon/AgenticDevelopment/Skills/README.md
  - ../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md
  - ../../README.md
supersedes:
  - ./release_0_1_2.md
---

# Release 0.1.3

## Context

This document records the entry-surface refinement and Codex
runtime-governance release of Context Atlas.

`0.1.3` does not reopen the core shared-engine semantics that were hardened in
`0.1.2`. Instead, it packages the next layer of polish around that hardened
engine:

- a cleaner, more layered public entry surface for the repository
- a richer portable skill and specialist-archetype canon for the agentic model
- a concrete project-side materialization manifest for Codex runtime assets
- deterministic generation and drift enforcement for the generated Codex
  runtime surface

This release is intentionally a micro release. It improves how the repo is
understood, reviewed, and operationalized without changing the core packet,
trace, retrieval, budgeting, or compression contract that `0.1.2` established.

## Shipped Capabilities

### Layered README And Guide Entry Surface

`0.1.3` turns the repository root into a clearer map rather than letting the
README carry both the map and the full tour.

The root [README](../../README.md) now:

- keeps the product framing and problem statement near the top
- adds a short explicit mental model
- keeps the multi-audience `Start Here` surface
- keeps the AI-assisted review prompts
- routes deeper walkthrough readers into the guide layer instead of asking
  first-time readers to absorb every workflow shape from the root

The deeper walkthrough now lives under
[docs/Guides/context_atlas_tour.md](../Guides/context_atlas_tour.md), which
gives the product-facing system tour a stable home without crowding the entry
surface.

### Richer Portable Agentic Skill And Specialist Catalog

`0.1.3` also deepens the portable AgenticDevelopment canon.

This release ships:

- a richer portable skill catalog under
  `docs/Authoritative/Canon/AgenticDevelopment/Skills/`
- reusable specialist archetypes under
  `docs/Authoritative/Canon/AgenticDevelopment/SpecialistArchetypes/`
- a short human-readable quick mental model for the core agentic entities

The skill definitions are now materially stronger than the earlier scaffold.
They carry real capability expectations, knowledge scope, heuristics, output
shape, evidence expectations, and escalation boundaries instead of acting as
light labels only.

### Materialization Manifest For Context Atlas Codex Runtime

`0.1.3` turns the Context Atlas Codex runtime projection into a clearer
project-side binding.

The release upgrades
[materialization_manifest.yaml](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
into the machine-readable source of truth for:

- parent agents
- specialists
- direct skills
- delegated specialists
- mode participation
- protocol participation
- runtime-root declarations
- `maintenance_mode`

That means the repo now has an explicit upstream surface that can answer not
just *what* Codex runtime files exist, but *why* they exist and which agentic
entities they represent.

### Generated Codex Runtime Surface

`0.1.3` also ships the first real manifest-driven Codex runtime surface under:

- `.codex/`
- `.agents/skills/`

This release makes those runtime assets part of the governed repository
surface, rather than leaving them as still-theoretical materialization targets.

The generated runtime files now explicitly inherit guidance that they are
derived from Canon and Identity inputs. Durable semantic changes should happen
upstream first, then the runtime surface should be regenerated.

### Deterministic Generation And Drift Enforcement

The biggest operational change in `0.1.3` is that Codex runtime materialization
is now enforceable rather than only described.

This release ships:

- `scripts/materialize_codex_runtime.py`
- `scripts/check_codex_materialization.py`
- preflight enforcement for the generated runtime surface
- CI enforcement for Codex materialization drift

The current implementation supports:

- `maintenance_mode: generated`
- `maintenance_mode: human`

It intentionally refuses to pretend that `mixed` is solved before explicit
manual-block semantics exist.

That makes the Codex runtime story materially stronger. The repository no
longer only explains how runtime assets *should* be projected; it now has a
real deterministic generation path and a real drift check.

### Owner-File And Planning Surface Hygiene

`0.1.3` also includes a few supporting repo-hygiene improvements:

- completed planning stacks now live under `docs/Planning/completed/`
- large owner files were compacted so they read more like current-state
  contracts than append-only changelogs
- an exploratory pickup note now captures the remaining Codex materialization
  gaps so they are visible without being mistaken for current authority

These changes do not alter product behavior directly, but they make the repo
more maintainable and easier to navigate.

## Known Gaps

`0.1.3` strengthens the runtime-governance loop for Codex, but several gaps
remain intentionally open:

- `maintenance_mode: mixed` is still not supported because the manual-block
  format has not been fully defined
- `maintenance_mode: human` is supported in policy, but it is not yet exercised
  as a fully proven real runtime surface in the current manifest
- Codex is still the only runtime materialization binding; Claude and other
  future environments are not yet implemented
- the repo-level entry surface is now layered, but the broader release/process
  automation path is still relatively manual
- the core product still keeps its intentionally narrow workflow boundaries; it
  does not yet own broader connector, database, vector-store, or repository
  integrations

## Future State

The next phase after `0.1.3` should build on the clearer layered repo surface
and the now-enforced Codex runtime path.

Near-term follow-on work should emphasize:

- broader scenario and integration coverage over the already-hardened engine
- fuller exercise of `human` and eventual `mixed` runtime maintenance modes
- future runtime bindings such as Claude using the same manifest-driven
  generator/checker pattern
- continued improvement of the product-facing entry surface without letting the
  root README collapse back into a second walkthrough layer

The core principle should remain the same: keep the hardened shared-engine
truths stable, then improve explanation, governance, and operationalization
around them deliberately.

## Related Artifacts

- [Release 0.1.2](./release_0_1_2.md)
- [Guides Index](../Guides/README.md)
- [Context Atlas Tour](../Guides/context_atlas_tour.md)
- [Materialization Manifest](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Codex Governance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md)
- [Repository README](../../README.md)
