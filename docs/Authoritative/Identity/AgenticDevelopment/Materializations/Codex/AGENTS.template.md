# `AGENTS.md` Template

Use this template when creating or refreshing `.codex/AGENTS.md`.

This file is the Codex-facing orientation surface. It should index and point
to the more specific role, agent, mode, protocol, skill, and config surfaces
rather than redefining them.

## Required Sections

### Purpose

- explain that the file is the runtime-facing orientation surface for Context
  Atlas Codex assets
- state that it is downstream of the portable canon and Identity-layer binding
  docs

### Read Order

- identify the order Codex should read the local role, agent, mode, protocol,
  and skill surfaces

### Runtime Surface Index

- link to:
  - `.codex/roles/`
  - `.codex/agents/`
  - `.codex/modes/`
  - `.codex/protocols/`
  - `.agents/skills/`
  - `.codex/config.toml`

### Boundary Notes

- remind readers that:
  - roles are accountability surfaces
  - agents are materialized actors
  - skills are atomic capabilities
  - modes are execution states
  - protocols are workflow paths

### Traceability Notes

- identify the upstream authoritative sources this runtime orientation surface
  depends on
- state the maintenance mode for the file
- briefly distinguish which sections are copied, adapted, or locally derived
  when that would help later refresh work

## Authoring Rules

- do not collapse all definitions into this file
- do not redefine portable canon or Identity-layer meaning here
- prefer links and short summaries over copied authoritative prose
