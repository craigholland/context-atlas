# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: d9a5ec4b8b2185a942d580648fc571b1f381b5b8
- timestamp_utc: 2026-04-20T23:33:24Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: docs/Authoritative/Canon/AgenticDevelopment
- included:
  - "*.md"
  - "**/*.md"
- excluded:
  - "__pycache__/**"

## Purpose
- Governs the portable, environment-agnostic canon for agentic-development concepts and invariants.
- Keeps the canon readable from its own README before downstream bindings or runtime materializations are consulted.
- Defines how drift, validation, and change-management should be reasoned about for this canon and the neighboring repo-management surface.
- Keeps the README strong enough to explain why this canon exists in a context-governance engine, not only how to traverse the file set.
- Keeps the portable skill catalog and specialist-archetype catalog distinct from both role archetypes and downstream project bindings.

## Architectural Rules
- This folder must stay portable: do not define project-specific role rosters, provider choices, or runtime folder layouts here unless the relevant portable boundary model explicitly authorizes them.
- Portable docs here may reference project bindings or runtime assets only as downstream categories, not as named source-of-truth implementations.
- Drift, validation, and change-management docs in this folder should define stable models and expectations, not platform-specific scripts or operator folklore.
- Protocol, role-archetype, materialization, and governance supplements should remain separate enough that later validators and reviewers can reason about one concern without reconstructing the whole system.
- Skill docs should stay atomic reusable capability units, while specialist-archetype docs should stay delegated composition patterns built from curated skills rather than project-specific runtime actors.
- Skill docs in this folder should be materially rich enough to define real capability expectations, including knowledge scope, common inputs, decision heuristics, outputs, evidence, and escalation conditions.
- Meaningful updates to this folder should also review root governance, metadata, and neighboring planning indexes so the canon remains discoverable and trustworthy.
- The README should explain why the agentic canon matters to Context Atlas's broader governance model, not only provide a reading order over the documents.
- When hardening or other planning closeout docs summarize evidence paths, they should point back to this canon for shared governance vocabulary rather than recreating a second portable validation or change-management model in planning prose.

## Allowed Dependencies
- may depend on:
  - docs/Authoritative/Canon/Architecture/**
  - docs/Authoritative/Canon/Ontology/**
  - docs/Authoritative/Canon/RepoManagement/**
- must not depend on:
  - docs/Authoritative/Identity/**
  - docs/Planning/**
  - runtime-specific folders such as `.codex/**` or `.agents/**`

## Public API / Key Exports
- README.md:
  - entrypoint: defines the portable reading order and boundary of the canon.
  - invariants:
    - should explain why the canon exists in a context-governance engine, not only list documents
- Agentic-Development-Glossary.md:
  - glossary: defines the portable vocabulary for the agentic model.
- Skills/README.md:
  - skill-index: defines the reusable portable skill catalog and its role/mode coverage.
- SpecialistArchetypes/README.md:
  - specialist-index: defines the reusable portable specialist-archetype catalog.
- Protocols/README.md:
  - protocol-index: defines the shared protocol set and template lineage.
- Drift-Model.md:
  - drift-model: defines the stable drift categories for validation and recovery.
- Validation-Model.md:
  - validation-model: defines structural validation expectations for canon, bindings, planning inputs, and materializations.
- Change-Management-Model.md:
  - change-management-model: defines the governed path for evolving the system.

## File Index
- README.md:
  - responsibility: anchors the portable reading order and scope boundary.
  - invariants:
    - must remain readable without consulting project-specific bindings first
- RoleArchetypes/README.md:
  - responsibility: indexes the reusable role-archetype catalog.
  - invariants:
    - archetypes stay reusable and do not become one project's active roster
- Skills/README.md:
  - responsibility: indexes the reusable portable skill catalog and its role/mode coverage.
  - invariants:
    - skills stay atomic and do not turn into disguised roles, modes, or specialists
- SpecialistArchetypes/README.md:
  - responsibility: indexes the reusable portable specialist-archetype catalog.
  - invariants:
    - specialist archetypes stay delegated composition patterns rather than project-specific runtime actors
- Protocols/README.md:
  - responsibility: indexes the portable protocol family and shared template.
  - invariants:
    - protocol docs remain workflow-centered rather than role-specific prompt bundles
- Drift-Model.md:
  - responsibility: defines meaningful drift categories and machine-vs-review boundaries.
  - invariants:
    - cosmetic wording changes should not automatically become high-severity drift
- Validation-Model.md:
  - responsibility: defines structural validation boundaries and preflight integration expectations.
  - invariants:
    - validation must not become a hidden scheduler or hidden workflow reviewer
- Change-Management-Model.md:
  - responsibility: defines the governed path for introducing and recovering changes.
  - invariants:
    - semantic changes should originate at the authoritative layer that owns them

## Known Gaps / Future-State Notes
- The canon now defines drift, validation, and change-management models, but the repo still relies mostly on broader preflight and owner-file checks rather than dedicated validators for every agentic surface.
- The portable canon supports multiple runtime environments in theory, but only the Codex binding is currently defined downstream in this repo.
- The portable skill catalog is now broad enough for an initial multi-role materialization pass, but downstream bindings still have to choose which skills and specialist archetypes Context Atlas actually adopts.
- The repo-management sibling canon is now present, but the provisioned GitHub-principal reality still depends on future operational setup outside this doc set.

## Cross-Folder Contracts
- docs/Authoritative/Canon/RepoManagement: sibling canon for repository-provider concepts that agentic-development may rely on but must not absorb.
- docs/Authoritative/Identity/AgenticDevelopment: project-specific binding layer that refines, but must not redefine, the portable canon.
- docs/Authoritative/Identity/RepoManagement: project-specific repo-provider bindings that must stay downstream of this canon and the RepoManagement canon.
- docs/Planning/completed/Agentic: planning surfaces should inherit vocabulary and governance from this folder rather than creating a second source of truth.

## Verification Contract
```yaml
steps:
  - name: validate_owner_file
    run: |
      # Linux/macOS analog: python3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/AgenticDevelopment/__ai__.md __ai__.md
      py -3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/AgenticDevelopment/__ai__.md __ai__.md

  - name: validate_related_owner_files
    run: |
      # Linux/macOS analog: python3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/AgenticDevelopment/__ai__.md docs/Authoritative/Canon/RepoManagement/__ai__.md __ai__.md
      py -3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/AgenticDevelopment/__ai__.md docs/Authoritative/Canon/RepoManagement/__ai__.md __ai__.md

  - name: freshness
    run: |
      # Linux/macOS analog: python3 scripts/check_ai_docs.py --repo-root . --base HEAD^ --head HEAD --governed-root docs/Authoritative/Canon/AgenticDevelopment --governed-root docs/Authoritative/Canon/RepoManagement --suffix .md
      py -3 scripts/check_ai_docs.py --repo-root . --base HEAD^ --head HEAD --governed-root docs/Authoritative/Canon/AgenticDevelopment --governed-root docs/Authoritative/Canon/RepoManagement --suffix .md
```

