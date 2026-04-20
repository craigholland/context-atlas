---
id: github-app-model
title: GitHub App Model
summary: Defines the reusable GitHub-specific principal model centered on GitHub Apps, installation scoping, and short-lived provider-issued credentials.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, github, github-apps, principals, credentials]
related:
  - ./README.md
  - ../Principal-Model.md
  - ../Authorization-Model.md
supersedes: []
---

# GitHub App Model

## Purpose

Define the reusable GitHub-specific principal model centered on GitHub Apps.

## Scope

This document governs the preferred GitHub-side principal mechanism for
automation and governed repository actions.

It does not choose one project's actual App roster or permission set.

## Binding Decisions

### 1. GitHub Apps Are The Preferred Machine-Principal Model

When governed automation needs to perform GitHub actions, the preferred
mechanism is a GitHub App or an equivalent provider-managed machine principal
surface, not a reused human account.

### 2. Installation Scope Should Stay Explicit

GitHub principal reach should be bounded through explicit installation scope,
repository selection, and permission scope rather than one broad credential
with ambient access.

### 3. Short-Lived Provider-Issued Credentials Are Preferred

The GitHub-side credential flow should prefer short-lived, revocable
installation or app-issued tokens instead of long-lived manually copied
secrets wherever practical.

### 4. App Identity And Project Binding Must Stay Separate

This GitHub App model describes the provider mechanism.

It does not choose:

- which project uses which App names
- which role maps to which GitHub principal
- which branch targets one principal may merge

Those are project-binding decisions.

### 5. One Provider Mechanism May Support Several Project Principal Families

Project bindings may choose:

- one GitHub App per principal family
- several principals beneath one App family
- a simpler topology for smaller systems

The important rule is that provider-level scoping must still reflect real
authorization boundaries.

## Constraints

- GitHub App usage should remain auditable and revocable.
- Reusable guidance should stay policy-oriented rather than click-by-click.
- Project bindings should make the final principal split explicit.

## Non-Goals

- Define a project's bot names.
- Define a project's GitHub installation steps.
- Define one universal GitHub App topology for all projects.
