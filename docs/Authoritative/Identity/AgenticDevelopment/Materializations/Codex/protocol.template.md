# Protocol Surface Template

Use this template when creating `.codex/protocols/<protocol-id>.md`.

## Required Sections

### Generated Surface Notice

- state that the file is generated or regenerated from authoritative Canon and
  Identity docs
- warn that local edits may be overwritten by later regeneration
- direct lasting meaning changes upstream to Canon or Identity depending on
  whether the change is portable or Context Atlas-specific

### Purpose

- identify the workflow path the protocol materializes

### Trigger / Enter Conditions

- state what starts the protocol in the Codex-facing runtime surface

### Participating Roles And Modes

- summarize the roles and modes the protocol binds together

### Structured Contract Expectations

- identify the handoff, delegation, escalation, or review contracts the
  protocol consumes or emits

### Exit Criteria

- summarize what counts as completion for the protocol

### Traceability

- list the upstream authoritative sources
- declare the maintenance mode

## Authoring Rules

- keep the protocol as a workflow-path surface
- keep the generated-surface warning visible enough that readers do not treat
  the file as the lasting source of truth
- do not redefine roles or modes inside the protocol file
