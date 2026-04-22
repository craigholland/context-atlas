---
id: context-atlas-exploratory-agentic-runtime-materialization-shortcomings
title: Current Shortcomings In Automated Agent Runtime Materialization
summary: Captures the main non-blocking gaps that remain in the current Codex-focused runtime materialization and enforcement loop.
doc_class: exploratory
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [exploratory, agentic, codex, materialization, drift, automation]
related:
  - ./README.md
  - ../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md
  - ../../.codex/AGENTS.md
  - ../../scripts/materialize_codex_runtime.py
  - ../../scripts/check_codex_materialization.py
  - ../Planning/completed/task_codex_runtime_materialization_enforcement.md
supersedes: []
---

# Current Shortcomings In Automated Agent Runtime Materialization

## Context

Context Atlas now has a real Codex runtime materialization loop:

- a machine-readable roster and attachment map in
  `materialization_manifest.yaml`
- deterministic generation through `scripts/materialize_codex_runtime.py`
- drift checking through `scripts/check_codex_materialization.py`
- preflight and CI enforcement when generated runtime assets drift

That is a meaningful step forward. This note exists to capture what is still
incomplete so later work does not mistake the current state for a fully solved,
platform-complete materialization system.

This document is exploratory on purpose. It is a pickup point for future work,
not binding project truth.

## Content

### 1. Maintenance-Mode Coverage Is Still Partial

The current implementation supports:

- `generated`
- `human`

But it does not yet support:

- `mixed`

That missing `mixed` path matters because it is the obvious future answer when
a generated file needs bounded manual sections without giving the file
authority over its own regeneration behavior.

Until explicit manual-block semantics exist, the system can only choose between
full generator ownership and full human ownership.

### 2. `human` Exists Mechanically, But Not Yet Operationally

The manifest and checker already understand `maintenance_mode: human`, but the
current runtime surface is still entirely generated.

That means the repo has not yet proven:

- what a healthy human-managed runtime surface looks like in practice
- how reviewers should judge intentional human edits against upstream Canon or
  Identity changes
- how often a human-managed file can drift semantically before it should be
  pulled back into generated ownership

So `human` is available, but not yet socially or operationally exercised.

### 3. Automation Is Enforced, But Still Contributor-Initiated

The generator and checker are real, and drift now breaks preflight and CI.
That is good.

But the current loop still depends on contributors to:

- edit Canon or Identity
- run `materialize_codex_runtime.py --write`
- commit the refreshed runtime assets

The system does not yet auto-regenerate on authoritative change, and it does
not yet emit a review-friendly materialization report that explains what was
rewritten and why.

So the process is enforced, but not fully self-driving.

### 4. Codex Is The Only Materialized Runtime Target

The current automation is intentionally Codex-specific:

- `.codex/`
- `.agents/skills/`
- Codex template set
- Codex governance path

That is appropriate for the current repository state, but it also means the
shared-vs-platform-specific split has only been proven once.

Future Claude or other runtime materializations will still need to prove:

- which generator logic stays shared
- which template or folder-layout rules are platform-specific
- whether one manifest can cleanly drive multiple runtime projections without
  awkward platform leakage

### 5. Provenance And Reviewer Ergonomics Are Still Lightweight

The current system proves sync through regeneration and drift checks, but it
does not yet provide a richer reviewer-facing provenance layer such as:

- per-surface source fingerprints
- a compact materialization report
- a dedicated audit summary showing which Canon and Identity inputs shaped each
  generated runtime file

That is not required for correctness today, but it may matter later if the
runtime surface grows or multiple runtimes are materialized from the same
upstream bindings.

### 6. The Current Roster Is Still A First Operational Pass

The current parent-agent, specialist, mode, protocol, and skill roster is good
enough to generate a first real Codex runtime surface.

It is not yet proven to be the long-term stable roster.

Runtime use may still reveal:

- skills that are too broad
- skills that should be split
- specialist archetypes that need different boundaries
- missing protocol participation or mode participation detail
- parent agents that need narrower or broader direct-skill ownership

So the runtime surface is now materially real, but still early enough that some
roster refinement should be expected.

## Notes Or Findings

- The current system is strong enough for deterministic Codex generation plus
  mechanical drift enforcement.
- The most important unresolved design question is still how to support
  bounded manual edits safely through `maintenance_mode: mixed`.
- The next most important proof gap is likely a real `human`-managed runtime
  surface, because that will test whether the manifest semantics are actually
  useful beyond purely generated assets.
- Multi-runtime materialization should probably wait until the Codex path has
  either proved or rejected the `human` and `mixed` ownership models.

## Related Artifacts

- [Exploratory README](./README.md)
- [Materialization Manifest](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Codex Materialization README](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- [Codex Governance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md)
- [Generated AGENTS Surface](../../.codex/AGENTS.md)
- [Codex Runtime Generator](../../scripts/materialize_codex_runtime.py)
- [Codex Drift Checker](../../scripts/check_codex_materialization.py)
- [Completed Materialization Enforcement Task](../Planning/completed/task_codex_runtime_materialization_enforcement.md)
