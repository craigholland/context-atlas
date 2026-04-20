# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: <FILL_IN_SHA>
- timestamp_utc: <FILL_IN_UTC_ISO8601>
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).

## Scope
- folder: <RELATIVE/POSIX/PATH/TO/FOLDER>
- included:
  - <glob patterns, e.g. "*.py", "**/*.py">
- excluded:
  - <glob patterns, e.g. "__pycache__/**", "**/*.pyc">

## Purpose
- <1-3 bullets describing what this folder provides and why it exists>

## Architectural Rules
- <what this folder is allowed to do>
- <what this folder must not do>
- <important runtime / import-safety / layering rules>
- <for documentation/governance surfaces, how metadata review and authoritative-source lineage should stay explicit>

## Allowed Dependencies
- may depend on:
  - <important allowed upstream modules/packages>
- must not depend on:
  - <important forbidden modules/packages>

## Public API / Key Exports
- <module>:
  - <symbol>: <what it is + why it matters>

## File Index
- <file>:
  - responsibility: <short>
  - defines:
    - <class/function>: <inputs/outputs + notes>
  - depends_on:
    - <important imports / upstream modules>
  - used_by:
    - <known downstream modules (optional)>
  - invariants:
    - <rules that should always hold>
  - footguns:
    - <common pitfalls / gotchas>

## Known Gaps / Future-State Notes
- <intentional simplification in current implementation>
- <future direction that is relevant to reading current code>
- <areas where current scope is still narrower than the long-term architecture>
- <do not use this section as a changelog of completed work>

## Cross-Folder Contracts
- <folder or module>: <assumption this folder relies on>
- <folder or module>: <boundary or behavioral expectation>
- <folder or module>: <which upstream authoritative sources or machine-readable artifacts this folder must stay traceable to>

## Verification Contract
```yaml
steps:
  - name: compile
    run: |
      <REPO_LOCAL_COMPILE_COMMAND>

  - name: verify
    run: |
      <REPO_LOCAL_VERIFICATION_COMMAND>

  - name: import_sanity
    run: |
      <REPO_LOCAL_IMPORT_SANITY_COMMAND>
```
