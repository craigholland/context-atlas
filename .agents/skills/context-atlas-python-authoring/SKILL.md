# Context Atlas Skill: Python Authoring

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for authoring and modifying Python implementation surfaces in a bounded, reviewable way.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `specialist-python-implementation`
- Does not replace debugging, testing, or review skills

## Workflow

1. Inspect the local code context before editing
2. Identify the relevant Python, framework, and architectural surfaces
3. Make the bounded implementation change
4. Update tests or supporting evidence surfaces as needed
5. Summarize what changed and how it was verified

## Escalation Conditions

- The work requires deep framework or library knowledge not evidenced locally
- The requested change crosses architecture boundaries rather than staying in
  a bounded Python surface
- Multiple incompatible implementation patterns already exist and no governing
  rule is clear
- Correctness depends on data, infrastructure, or runtime state not available
  to the current actor

## Return Contract

- focused Python diffs
- supporting test adjustments
- concise verification notes
- framework-aware implementation rationale when needed

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-authoring.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
