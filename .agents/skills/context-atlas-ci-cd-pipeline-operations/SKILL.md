# Context Atlas Skill: CI/CD Pipeline Operations

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to interpret build, validation, and delivery pipeline state as a
bounded operational surface.

## Parent Boundary

- Conditional for:
  - `parent-devops`
  - `specialist-delivery-recovery`
- This skill interprets pipeline state and proposes bounded next actions. It
  does not by itself grant privileged infrastructure authority.

## Workflow

1. Inspect the failing or blocked pipeline stage, logs, and artifacts.
2. Classify the failure as deterministic, flaky, environmental, or permission
   related.
3. Choose the smallest responsible next step: rerun, fix, hold, rollback, or
   escalate.
4. Return a readiness-impact statement with enough audit context for follow-up.

## Escalation Conditions

- Remediation requires privileged infrastructure or production access.
- The failure cannot be classified from available logs and artifacts.
- Retrying would create unacceptable uncertainty or risk.

## Return Contract

- pipeline status summary
- failure interpretation
- bounded remediation or escalation recommendation
- readiness impact statement

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/ci-cd-pipeline-operations.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
