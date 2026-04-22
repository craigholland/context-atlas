# Context Atlas Skill: CI/CD Pipeline Operations

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for reasoning about build, validation, and delivery pipelines as bounded operational systems.

## Parent Boundary

- Conditional for:
  - `parent-devops`
  - `specialist-delivery-recovery`
- Does not automatically grant infrastructure-administration authority

## Workflow

1. Inspect failing or blocked pipeline state
2. Classify the failure type
3. Identify the smallest responsible operational response
4. State whether the next step is rerun, fix, hold, rollback, or escalate

## Escalation Conditions

- Remediation requires privileged infrastructure or production access
- The failure cannot be classified from available logs and artifacts
- The pipeline is signaling a broader release or environment problem
- Retrying would create unacceptable uncertainty or risk

## Return Contract

- pipeline status summary
- failure interpretation notes
- bounded remediation or escalation recommendation
- readiness impact statement

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/ci-cd-pipeline-operations.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
