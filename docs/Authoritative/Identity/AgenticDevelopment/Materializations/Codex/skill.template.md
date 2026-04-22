# Skill Surface Template

Use this template when creating `.agents/skills/context-atlas-<skill-id>/SKILL.md`.

## Required Sections

### Generated Surface Notice

- state that the file is generated or regenerated from authoritative Canon and
  Identity docs
- warn that local edits may be overwritten by later regeneration
- direct lasting meaning changes upstream to Canon or Identity depending on
  whether the change is portable or Context Atlas-specific

### Purpose

- explain the bounded capability the skill provides

### Parent Boundary

- identify which parent role or parent-agent contexts should attach to this
  skill

### Workflow

- describe the repeatable steps the skill performs

### Escalation Conditions

- identify when the skill should return or escalate rather than continue

### Return Contract

- state what outputs or state the caller should receive back

### Traceability

- list the authoritative and binding sources the skill derives from
- declare the maintenance mode
- note any copied versus adapted wording that should stay stable across refresh
  work

## Authoring Rules

- keep the skill atomic
- keep the generated-surface warning visible enough that readers do not treat
  the file as the lasting source of truth
- do not smuggle role, mode, or protocol ownership into the skill
