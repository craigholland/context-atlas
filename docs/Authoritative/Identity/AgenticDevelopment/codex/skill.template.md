# Skill Surface Template

Use this template when creating `.agents/skills/context-atlas-<skill-id>/SKILL.md`.

## Required Sections

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

## Authoring Rules

- keep the skill atomic
- do not smuggle role, mode, or protocol ownership into the skill
