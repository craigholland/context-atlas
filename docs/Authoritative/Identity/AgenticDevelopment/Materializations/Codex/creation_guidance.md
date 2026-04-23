---
id: context-atlas-codex-creation-guidance
title: Context Atlas Codex Creation Guidance
summary: Defines how contributors should create or refresh Context Atlas Codex assets from the authoritative canon, project bindings, and Codex template surfaces.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-22
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, creation-guidance]
related:
  - ./README.md
  - ./folder_layout.md
  - ./AGENTS.template.md
  - ./config.template.toml
  - ./agent.template.toml
  - ./role.template.md
  - ./mode.template.md
  - ./protocol.template.md
  - ./skill.template.md
supersedes: []
---

# Context Atlas Codex Creation Guidance

## Purpose

Define the repeatable process for creating or refreshing Context Atlas Codex
assets from the authoritative canon, project bindings, and Codex-specific
templates.

## Scope

This document governs how contributors should derive runtime-facing Codex
assets from upstream sources.

It does not replace the upstream canon or the Codex template surfaces.

If you were routed here from a repo-edge contributor path, use this document
for the derivation workflow and use
[governance.md](./governance.md) for the matching refresh and drift-check
expectations.

## Creation Workflow

### 1. Start From Upstream Sources, Not Existing Runtime Files

When creating or refreshing a Codex asset, begin with:

- the portable AgenticDevelopment canon
- the Context Atlas Identity bindings
- the Codex binding docs under `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/`

Existing runtime-facing assets may help confirm current layout or wording, but
they should not become the primary source of truth.

### 1a. Prefer The Repo-Owned Generator When The Surface Is Declared Generated

For the current Codex binding, contributors should prefer the repo-owned
generator at `scripts/materialize_codex_runtime.py` whenever the upstream
manifest declares that a runtime surface is `generated`.

Manual refresh is still a useful review aid, but it should not become a shadow
generation path once the repo owns a deterministic materialization script.

### 2. Choose The Correct Codex Surface First

Select the runtime-facing surface that matches the concept being materialized:

- role projection -> `.codex/roles/<role-id>.md`
- parent agent or specialist -> `.codex/agents/<agent-id>.toml`
- mode -> `.codex/modes/<mode-id>.md`
- protocol -> `.codex/protocols/<protocol-id>.md`
- skill -> `.agents/skills/context-atlas-<skill-id>/SKILL.md`
- runtime orientation -> `.codex/AGENTS.md`
- runtime config -> `.codex/config.toml`

Do not choose a surface based only on convenience.

### 3. Apply The Matching Template Or Template Guidance

Use the matching Codex template surface when it exists:

- `AGENTS.template.md`
- `config.template.toml`
- `role.template.md`
- `agent.template.toml`
- `mode.template.md`
- `protocol.template.md`
- `skill.template.md`

If a surface has no dedicated file template yet, derive it from the
folder-layout and binding docs rather than improvising a new concept shape.

### 4. Treat Runtime Assets As Regenerable Outputs

When creating or refreshing `.codex/` or `.agents/skills/` assets, treat those
files as derived runtime outputs rather than as the lasting source of truth.

That means:

- local edits to generated runtime assets may be useful temporarily
- those edits may be overwritten by later regeneration
- durable semantic changes should be made upstream in authoritative docs first

Use `docs/Authoritative/Canon/` when the change is meant to be portable or
reusable.

Use `docs/Authoritative/Identity/` when the change is Context Atlas-specific.

### 4a. Maintenance Mode Comes From The Manifest, Not The Runtime File

The authoritative `maintenance_mode` for a Codex runtime surface lives in
`docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`.

The generator may echo that value into the runtime file, but the runtime file
must not become the place that decides whether it may be overwritten.

The current maintenance semantics are:

- `generated`: the generator fully owns and rewrites the surface
- `human`: the generator does not rewrite the surface, but the surface remains
  declared and reviewable
- `mixed`: reserved for future explicit manual-block preservation; do not
  assume ambiguous freeform preservation behavior

## Copied, Adapted, And Derived Content

### Copied

The following should normally be copied from upstream sources with minimal
change:

- stable ids and vocabulary for roles, modes, and protocols
- parent-versus-specialist distinctions
- review-pass and structured-contract terminology
- upstream authoritative file references used for traceability

### Adapted

The following are expected to be adapted for Codex readability:

- concise summaries
- runtime-oriented read order
- Codex-facing guidance phrasing
- file-specific notes about how one surface points to another

Adaptation should improve usability without changing meaning.

### Derived

The following are derived at the Codex layer:

- concrete file paths and names
- traceability metadata that points to the upstream sources used
- maintenance-mode declarations
- cross-surface indexes inside `.codex/AGENTS.md`

Derived data should clarify provenance, not invent new semantics.

## Per-Surface Source Expectations

### `AGENTS.md`

- derive from:
  - Codex binding README
  - Codex folder layout
  - role, mode, protocol, and skill indexes
- use:
  - `AGENTS.template.md`

### Role Projections

- derive from:
  - `Role-Model.md`
  - `Role-Accountability-Matrix.md`
  - `Role-Authority-Matrix.md`
  - `Role-Agent-Binding-Model.md`
- use:
  - `role.template.md`

### Agent Descriptors

- derive from:
  - `materialization_manifest.yaml`
  - `Context-Atlas-Agentic-Development-Profile.md`
  - `Role-Agent-Binding-Model.md`
  - attached skill, mode, and protocol bindings
- use:
  - `agent.template.toml`

### Mode Surfaces

- derive from:
  - `Mode-Model.md`
  - `Mode-Transition-Rules.md`
  - `Mode-Mutation-Matrix.md`
  - `Role-Mode-Matrix.md`
- use:
  - `mode.template.md`

### Protocol Surfaces

- derive from:
  - portable protocol canon
  - `Protocol-Role-Bindings.md`
  - `Protocol-Mode-Bindings.md`
  - `Gate-Review-Pass-Matrix.md`
- use:
  - `protocol.template.md`

### Skills

- derive from:
  - the upstream skill contract and skill-attachment model
  - the parent role or parent-agent context that needs the skill
- use:
  - `skill.template.md`

## Review Rules

- check that ids and filenames follow the Codex folder layout naming rules
- check that the runtime surface still points back to upstream authoritative
  sources
- check that the generated-surface notice remains accurate
- check that the maintenance mode is explicit
- check that `maintenance_mode` still matches the upstream manifest rather than
  a local runtime edit
- check that Codex wording does not silently redefine portable or Identity-layer
  semantics

## Refresh Triggers

Refresh or re-review an affected Codex asset when:

- one of its cited upstream authoritative sources changes meaning
- the repo-owned generator changes the derived output shape
- the upstream manifest changes `maintenance_mode`, roster membership, or
  runtime-surface participation
- the Codex folder layout or naming rules change
- the Codex templates change in a way that invalidates the current asset
- the creation guidance changes how copied, adapted, or derived content should
  be expressed

## Contributor Refresh Path

When a contributor intentionally changes Canon, Identity, or manifest inputs
that feed the generated Codex runtime surface, the normal refresh path is:

1. make the durable semantic change upstream first
2. regenerate generator-owned Codex assets:
   `py -3 scripts/materialize_codex_runtime.py --write`
3. verify drift and declared-human surfaces:
   `py -3 scripts/check_codex_materialization.py`
4. run full repo preflight before push:
   `py -3 scripts/preflight.py`

Those commands belong here and in the companion governance doc, not in the
repo's product-facing onboarding path.

## Non-Goals

- Define one automation mechanism for generating every Codex asset.
- Replace future validation or governance hooks.
- Author the runtime-facing Codex assets themselves inside this guidance doc.

## Related Artifacts

- [Context Atlas Codex Binding](./README.md)
- [Context Atlas Codex Folder Layout](./folder_layout.md)
- [AGENTS Template](./AGENTS.template.md)
- [Agent Template](./agent.template.toml)
- [Role Template](./role.template.md)
- [Mode Template](./mode.template.md)
- [Protocol Template](./protocol.template.md)
- [Skill Template](./skill.template.md)
