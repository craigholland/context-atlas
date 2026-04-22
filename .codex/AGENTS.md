# Context Atlas Codex Runtime Orientation

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

This is the runtime-facing orientation surface for the Context Atlas Codex materialization. It is downstream of the portable AgenticDevelopment canon, the Context Atlas Identity bindings, and the Codex materialization rules.

Use this file to orient to the local runtime surface, then move quickly into the more specific role, agent, mode, protocol, and skill files instead of treating this file as the only definition source.

## Read Order

1. Read this file for the current runtime surface and concept boundaries.
2. Read the relevant role projection under `.codex/roles/`.
3. Read the parent-agent descriptor in `.codex/agents/` for the accountable actor bound to that role.
4. If work is delegated, read the relevant specialist descriptor in `.codex/agents/`.
5. Read the active mode under `.codex/modes/` and the governing workflow under `.codex/protocols/`.
6. Read only the attached skills needed for the current bounded work under `.agents/skills/`.
7. Use `.codex/config.toml` for runtime roots, manifest traceability, and planning-capacity defaults.

## Runtime Surface Index

- Roles:
  - .codex/roles/planner-decomp.md
  - .codex/roles/backend.md
  - .codex/roles/documentation-uat.md
  - .codex/roles/qa.md
  - .codex/roles/devops.md
- Agents:
  - .codex/agents/parent-planner-decomp.toml
  - .codex/agents/parent-backend.toml
  - .codex/agents/parent-documentation-uat.toml
  - .codex/agents/parent-qa.toml
  - .codex/agents/parent-devops.toml
  - .codex/agents/specialist-planning-change.toml
  - .codex/agents/specialist-python-implementation.toml
  - .codex/agents/specialist-review-readiness.toml
  - .codex/agents/specialist-delivery-recovery.toml
- Modes:
  - .codex/modes/planning.md
  - .codex/modes/implementation.md
  - .codex/modes/review.md
  - .codex/modes/rework.md
  - .codex/modes/recovery.md
  - .codex/modes/operational-delivery.md
- Protocols:
  - .codex/protocols/planning.md
  - .codex/protocols/execution-slice.md
  - .codex/protocols/review.md
  - .codex/protocols/rework.md
  - .codex/protocols/recovery.md
  - .codex/protocols/delegation.md
  - .codex/protocols/handoff.md
  - .codex/protocols/escalation.md
- Skills:
  - `.agents/skills/context-atlas-*/SKILL.md`
- Runtime config:
  - `.codex/config.toml`

## Boundary Notes

- Roles are accountability surfaces.
- Parent agents are the materialized accountable actors for those roles.
- Specialists are bounded delegates beneath parent-owned accountability.
- Skills are atomic reusable capabilities attached to parents or specialists.
- Modes are execution states, not alternate roles.
- Protocols are workflow paths, not new role or mode families.
- GitHub authority remains downstream of RepoManagement bindings rather than
  being redefined by these runtime files.

## Traceability Notes

- Maintenance mode: `generated`
- Primary upstream sources:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
  - `docs/Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/`
  - `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/`
- Copied content:
  - stable role, mode, protocol, parent-agent, specialist, and skill ids
- Adapted content:
  - short Codex-facing summaries and read-order guidance
- Derived content:
  - file layout, runtime index, and local cross-surface links
