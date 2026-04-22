# Context Atlas Skill: Python Authoring

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to create or modify bounded Python implementation surfaces in a
way that preserves local conventions, architecture, and reviewability.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `specialist-python-implementation`
- This skill assumes working familiarity with Python `3.12-3.14` plus common
  framework and library families when they are already present locally. It
  does not settle architecture or acceptance on its own.

## Workflow

1. Inspect the local Python, framework, and architectural context before
   editing.
2. Choose the smallest coherent change that satisfies the requested behavior.
3. Preserve local typing, boundary, and framework idioms rather than imposing a
   generic style.
4. Return the focused diff, supporting test changes, and concise verification
   notes.

## Escalation Conditions

- Required framework or library semantics exceed the evidence available locally.
- The requested change crosses major architecture boundaries.
- Correctness depends on unavailable runtime, data, or infrastructure state.

## Return Contract

- focused Python code changes
- nearby test or evidence updates when behavior changes
- concise implementation rationale when needed
- verification notes tied to the changed behavior

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-authoring.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
