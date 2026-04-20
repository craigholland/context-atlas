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
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, creation-guidance]
related:
  - ./README.md
  - ./folder_layout.md
  - ./AGENTS.template.md
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

## Creation Workflow

### 1. Start From Upstream Sources, Not Existing Runtime Files

When creating or refreshing a Codex asset, begin with:

- the portable AgenticDevelopment canon
- the Context Atlas Identity bindings
- the Codex binding docs under `docs/Authoritative/Identity/AgenticDevelopment/codex/`

Existing runtime-facing assets may help confirm current layout or wording, but
they should not become the primary source of truth.

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
- `role.template.md`
- `agent.template.toml`
- `mode.template.md`
- `protocol.template.md`
- `skill.template.md`

If a surface has no dedicated file template yet, derive it from the
folder-layout and binding docs rather than improvising a new concept shape.

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
- check that the maintenance mode is explicit
- check that Codex wording does not silently redefine portable or Identity-layer
  semantics

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
