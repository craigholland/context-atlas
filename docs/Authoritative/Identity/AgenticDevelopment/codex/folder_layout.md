---
id: context-atlas-codex-folder-layout
title: Context Atlas Codex Folder Layout
summary: Defines the Codex-specific discovery surfaces and folder layout used to materialize Context Atlas roles, agents, skills, modes, protocols, and supporting runtime guidance.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, folders]
related:
  - ./README.md
  - ../../Context-Atlas-Agentic-Development-Profile.md
  - ../../../AgenticDevelopment/Discovery-Model.md
  - ../../../AgenticDevelopment/Template-Model.md
supersedes: []
---

# Context Atlas Codex Folder Layout

## Purpose

Define the concrete discovery surfaces and folder layout that the Context Atlas
Codex binding uses to materialize upstream roles, agents, skills, modes,
protocols, and supporting guidance.

## Scope

This document governs the Context Atlas Codex layout and the mapping from
abstract concept families into concrete Codex-facing surfaces.

It does not redefine the portable concepts those surfaces express.

## Binding Decisions

### 1. Context Atlas Uses Two Top-Level Codex Runtime Roots

The Codex binding uses two project-local runtime roots:

- `.codex/` for project-scoped Codex runtime guidance, configuration,
  role/agent/mode/protocol surfaces, and related indexes
- `.agents/skills/` for reusable skill assets discoverable through Codex skill
  conventions

Those roots are downstream layout choices that satisfy the Story 7 discovery
model for Context Atlas.

### 2. `.codex/AGENTS.md` Is The Runtime Orientation Surface

`.codex/AGENTS.md` is the runtime-facing orientation surface for Codex.

It should provide:

- read order
- high-level runtime guidance
- references to the concrete role, agent, mode, and protocol surfaces that
  Codex should consult

It should not become the only place where all agentic concepts are defined.

### 3. Roles Materialize Into Dedicated Role Projection Surfaces

Project roles should materialize into:

- `.codex/roles/<role-id>.md`

Those files are the Codex-facing role projections for accountability and
authority expectations inherited from the Identity layer.

They remain distinct from parent-agent descriptors because a role is still an
accountability concept, not the same thing as the materialized actor that
embodies it.

### 4. Parent Agents And Specialists Materialize Into Agent Descriptor Surfaces

Parent agents and specialists should materialize into:

- `.codex/agents/<agent-id>.toml`

Those descriptors should carry enough information to tell whether the asset
represents:

- a parent agent
- a specialist

The shared file type is acceptable here because the descriptors still retain
the upstream parent-versus-specialist distinction explicitly.

### 5. Modes Materialize Into Dedicated Mode Surfaces

Project modes should materialize into:

- `.codex/modes/<mode-id>.md`

Those files are the Codex-facing execution-state surfaces derived from the
project mode model and its transition/mutation bindings.

### 6. Protocols Materialize Into Dedicated Protocol Surfaces

Project protocol guidance should materialize into:

- `.codex/protocols/<protocol-id>.md`

Those files are the Codex-facing workflow-path surfaces that bind the portable
protocol family to Context Atlas roles, modes, review gates, and handoff
expectations.

### 7. Skills Materialize Into Dedicated Skill Surfaces

Project skills should materialize into:

- `.agents/skills/<skill-id>/SKILL.md`

Those files remain the Codex-facing realization of the atomic skill model.

They should stay distinct from parent-agent or specialist descriptors even when
an agent later attaches to multiple skills.

### 8. Supporting Runtime Configuration Materializes Into `.codex/config.toml`

Codex-specific non-behavioral runtime configuration should materialize into:

- `.codex/config.toml`

That file is for runtime-facing configuration and coordination settings, not
for redefining project roles, protocols, or portable canon concepts.

### 9. Naming Conventions Should Preserve Upstream Distinctions

The Codex layout should use naming conventions that preserve the distinctions
already defined upstream.

The initial naming pattern is:

- roles:
  - `.codex/roles/<role-id>.md`
  - `<role-id>` should be kebab-case and align with the project role roster
- parent agents:
  - `.codex/agents/parent-<role-id>.toml`
  - the role-aligned suffix keeps the accountable actor tied back to the role
    it materializes
- specialists:
  - `.codex/agents/specialist-<specialist-id>.toml`
  - `<specialist-id>` should be kebab-case and scoped to the delegated domain
- modes:
  - `.codex/modes/<mode-id>.md`
  - `<mode-id>` should preserve the stable project mode vocabulary in kebab-case
- protocols:
  - `.codex/protocols/<protocol-id>.md`
  - `<protocol-id>` should preserve the stable protocol vocabulary in kebab-case
- skills:
  - `.agents/skills/context-atlas-<skill-id>/SKILL.md`
  - the `context-atlas-` namespace keeps project-local skills distinct from
    external or shared skill catalogs

### 10. Shared File Formats Must Still Carry Explicit Type Markers

Even when multiple concept families use the same file format, the files should
carry explicit type markers or identifying fields where appropriate.

For example:

- agent descriptors should still identify whether they are parent agents or
  specialists
- role, mode, and protocol surfaces should use titles and metadata that match
  their concept family explicitly

That keeps the shared format from collapsing the upstream distinctions.

## Surface Mapping Summary

| Concept family | Codex surface |
| --- | --- |
| Runtime orientation | `.codex/AGENTS.md` |
| Role projections | `.codex/roles/<role-id>.md` |
| Parent agents and specialists | `.codex/agents/<agent-id>.toml` |
| Modes | `.codex/modes/<mode-id>.md` |
| Protocols | `.codex/protocols/<protocol-id>.md` |
| Skills | `.agents/skills/<skill-id>/SKILL.md` |
| Runtime config | `.codex/config.toml` |

## Constraints

- The Codex layout must remain traceable to the Story 7 discovery and template
  model.
- Folder layout should remain a downstream binding choice, not a substitute
  source of truth.
- Role, parent-agent, specialist, mode, protocol, and skill distinctions must
  remain explicit even when multiple concept families share Markdown or TOML as
  a file format.
- Naming conventions should remain stable enough that later templates and
  governance hooks can validate them mechanically.

## Non-Goals

- Define the final naming conventions for each Codex asset.
- Define the exact template bodies for each Codex surface.
- Replace the later governance rules that keep these surfaces aligned.

## Related Artifacts

- [Context Atlas Codex Binding](./README.md)
- [Context Atlas Agentic Development Profile](../../Context-Atlas-Agentic-Development-Profile.md)
- [Discovery Model](../../../AgenticDevelopment/Discovery-Model.md)
- [Template Model](../../../AgenticDevelopment/Template-Model.md)
