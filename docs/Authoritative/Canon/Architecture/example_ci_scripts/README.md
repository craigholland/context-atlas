---
id: architecture-example-ci-scripts
title: Architecture Example CI Scripts
summary: Defines the purpose and intended contents of the example CI scripts folder for Craig Architecture supplementary artifacts.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-17
owners: [core]
tags: [architecture, ci, examples, ai-guidance]
related:
  - ../Craig-Architecture-AI-Guidance.md
  - ../Craig-Architecture-Python.md
  - ../Craig-Architecture-__ai__-Template.md
  - ../../Ontology/README.md
supersedes: []
---

# Architecture Example CI Scripts

## Purpose

This folder holds example CI scripts referenced by the Craig Architecture supplementary documents.

Its purpose is to provide practical, reusable examples for enforcing architecture-adjacent repository contracts such as `__ai__.md` validation, verification-contract checks, and similar automation patterns.

These examples operationalize the AI contract system described in the Craig Architecture supplements. They are part of the enforcement layer around the philosophy, not a replacement for the philosophy itself.

## Scope

This folder is for example CI scripts and related supporting files.

It is not intended to be a production automation package or a mandatory runtime dependency for every Craig-style repository.

## Binding Decisions

### 1. This Folder Holds Examples, Not Canonical Runtime Tooling

Files in this folder are examples meant to illustrate how repositories may operationalize Craig Architecture guidance.

They may be adapted, copied, or refined by downstream repositories.

### 2. Examples Should Stay Aligned With The Architecture Supplements

Scripts in this folder should remain consistent with:

- [Craig Architecture - AI Guidance](../Craig-Architecture-AI-Guidance.md)
- [Craig Architecture - Python](../Craig-Architecture-Python.md)
- [Craig Architecture - __ai__.md Template](../Craig-Architecture-__ai__-Template.md)

### 3. Examples Should Be Honest About Their Limits

Example scripts should distinguish between hard structural checks and softer staleness heuristics.

They should not overclaim what automation can prove about architectural correctness.

### 4. Examples Are Intended To Be Copied And Adapted

These examples are reference implementations.

Downstream repositories should normally copy the workflow files into `.github/workflows/` and copy the helper scripts into a repository-owned scripts directory before adapting paths, commands, and policy details.

## Example Pack Layout

This folder currently contains:

- `github_workflows/`: commented example GitHub Actions workflows
- `python/`: generic Python helper scripts used by those workflows

The current example pack focuses on:

- updating `Last Verified (CI)` blocks for changed `__ai__.md` owners
- validating `__ai__.md` structure
- executing `Verification Contract` steps from local guidance files
- detecting likely stale `__ai__.md` files
- enforcing import-boundary rules through a small AST-based checker

## Adaptation Guidance

When copying these examples into a real repository, you will usually need to adapt:

- the default branch name or fallback merge-base references
- the app root paths and governed code roots
- the location where helper scripts live after copying
- package-management commands such as `poetry install`, `pip install`, or `npm ci`
- the import-boundary rules for your actual package names and layer boundaries

Most examples include inline comments calling out these expected changes directly in the file.

## Constraints

- Files in this folder should favor readability and adaptation over framework-specific cleverness.
- Example scripts should be small enough for future contributors and agents to understand quickly.
- Example scripts should state clearly whether they are intended to fail hard, warn, or provide heuristics only.
- Example files may contain placeholder paths such as `apps/example_app` and should not be mistaken for drop-in production configuration.

## Non-Goals

- This folder does not define mandatory CI for all Craig-style repositories.
- This folder does not replace repository-specific CI workflows.
- This folder does not imply that passing example automation is equivalent to architectural correctness.

## Related Artifacts

- [Craig Architecture - AI Guidance](../Craig-Architecture-AI-Guidance.md)
- [Craig Architecture - Python](../Craig-Architecture-Python.md)
- [Craig Architecture - __ai__.md Template](../Craig-Architecture-__ai__-Template.md)
- [Ontology Templates](../../Ontology/README.md)
