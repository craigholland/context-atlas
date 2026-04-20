# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 0ae3b5caff02ecd8ce0477f10d00a0058bc7cf72
- timestamp_utc: 2026-04-20T22:22:38Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: docs/Authoritative/Canon/RepoManagement
- included:
  - "*.md"
  - "**/*.md"
- excluded:
  - "__pycache__/**"

## Purpose
- Governs the portable repo-management canon and reusable provider-specific supplements.
- Keeps repository-principal, authorization, operation, branch-target, and audit-identity concepts out of runtime-specific prompts and role folklore.
- Defines the portable governance expectations that project-specific repo bindings should inherit.

## Architectural Rules
- This folder may define provider-agnostic repo-management meaning and reusable provider-specific supplements, but it must not define one project's chosen principal roster or branch policy.
- Provider-specific subfolders such as `GitHub/` remain downstream of the portable repo-management canon but upstream of project-specific bindings.
- Project-specific GitHub bot names, merge rights, and review-trigger policies belong under `docs/Authoritative/Identity/RepoManagement/`, not here.
- Repo-management docs should remain compatible with the neighboring AgenticDevelopment canon instead of duplicating role, mode, or protocol definitions.
- Meaningful changes to this folder should also review metadata, planning indexes, and neighboring bindings so the repo-management surface remains discoverable and bounded.

## Allowed Dependencies
- may depend on:
  - docs/Authoritative/Canon/AgenticDevelopment/**
  - docs/Authoritative/Canon/Architecture/**
  - docs/Authoritative/Canon/Ontology/**
- must not depend on:
  - docs/Authoritative/Identity/RepoManagement/**
  - docs/Planning/**
  - runtime-specific folders such as `.codex/**` or `.agents/**`

## Public API / Key Exports
- README.md:
  - entrypoint: defines the portable repo-management scope and reading order.
- RepoManagement-Glossary.md:
  - glossary: defines the reusable repo-management vocabulary.
- GitHub/README.md:
  - provider-readme: defines the reusable GitHub provider supplement.
- Authorization-Model.md:
  - authorization-model: defines portable authorization-scope semantics.
- Branch-Target-Policy-Model.md:
  - branch-target-policy-model: defines portable merge-scope semantics.

## File Index
- README.md:
  - responsibility: defines the portable repo-management boundary and reading order.
  - invariants:
    - must keep RepoManagement as a sibling canon to AgenticDevelopment
- RepoManagement-Glossary.md:
  - responsibility: defines the reusable repo-management vocabulary.
  - invariants:
    - terms should remain provider-agnostic unless moved into a provider subfolder
- GitHub/README.md:
  - responsibility: indexes the reusable GitHub provider surface.
  - invariants:
    - provider guidance remains reusable across projects and does not become a project binding
- Authorization-Model.md:
  - responsibility: defines portable authorization semantics.
  - invariants:
    - prompt-level instructions should not be treated as equivalent to credential scope
- Branch-Target-Policy-Model.md:
  - responsibility: defines how merge authority should be constrained by target branch class.
  - invariants:
    - merge authority should not collapse into one global permission concept

## Known Gaps / Future-State Notes
- The portable and GitHub-specific canon now exists, but the project-specific operational setup for real GitHub Apps and credentials still lives outside this repo documentation set.
- GitHub is the only provider-specific supplement currently defined here; future provider surfaces will need to prove that the portable model generalizes cleanly.
- Validation and drift-control expectations are now documented in the neighboring AgenticDevelopment canon, but dedicated repo-management validators have not yet been implemented.

## Cross-Folder Contracts
- docs/Authoritative/Canon/AgenticDevelopment: sibling canon for roles, protocols, modes, and handoffs that repo-management bindings must align with but not absorb.
- docs/Authoritative/Identity/RepoManagement: project-specific provider bindings that refine this folder's canon into one application's concrete policy.
- docs/Planning/Agentic: planning surfaces should reference this folder for repo principals and permissions rather than recreating repo-management policy in planning prose.
- docs/Authoritative/Identity/AgenticDevelopment: role and gate bindings that repo-management policy must respect when defining principals, review surfaces, and merge scope.

## Verification Contract
```yaml
steps:
  - name: validate_owner_file
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/RepoManagement/__ai__.md __ai__.md

  - name: validate_related_owner_files
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files docs/Authoritative/Canon/RepoManagement/__ai__.md docs/Authoritative/Canon/AgenticDevelopment/__ai__.md __ai__.md

  - name: freshness
    run: |
      py -3 scripts/check_ai_docs.py --repo-root . --base HEAD^ --head HEAD --governed-root docs/Authoritative/Canon/AgenticDevelopment --governed-root docs/Authoritative/Canon/RepoManagement --suffix .md
```

