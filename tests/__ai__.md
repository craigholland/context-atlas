# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

## Scope
- folder: tests
- included:
  - "test_*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds automated tests for the standalone Context Atlas package.
- Verifies bootstrap contracts and guards early architectural seams from silent drift.
- Provides the first executable safety net for domain and infrastructure bootstrap behavior.

## Architectural Rules
- Tests may import internal project modules to verify behavior, but they must not become an alternate runtime API or hide bad package boundaries.
- Keep fast unit tests here; broader integration or environment-specific test suites should be introduced deliberately rather than mixed in by accident.
- Test helpers should not reimplement production semantics when assertions can exercise the real code directly.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - `context_atlas`
- must not depend on:
  - ad hoc `PYTHONPATH` tricks outside declared verification commands
  - hidden environment assumptions not documented in local owner files

## Public API / Key Exports
- `test_bootstrap_layers.py`:
  - `BootstrapLayerTests`: verifies error/message centralization, config loading, and structured log events

## File Index
- `test_bootstrap_layers.py`:
  - responsibility: verifies the current package bootstrap and shared semantic/runtime contracts
  - defines:
    - `BootstrapLayerTests`: bootstrap test suite
  - depends_on:
    - `context_atlas.domain`
    - `context_atlas.infrastructure`
  - invariants:
    - tests should stay fast and deterministic
    - assertions should track centralized contracts rather than ad hoc inline strings

## Known Gaps / Future-State Notes
- The current suite is intentionally small and bootstrap-focused.
- As services, adapters, and richer domain models arrive, this folder will likely need more granular owner files or sub-suites.

## Cross-Folder Contracts
- `src/context_atlas/`: tests exercise internal modules directly, but the package layout should remain understandable without depending on tests to explain it.
- `scripts/`: verification scripts invoke this suite and should keep the invocation contract stable or update it deliberately.

## Verification Contract
```yaml
steps:
  - name: compile_tests
    run: |
      py -3 -m compileall tests

  - name: unit_tests
    run: |
      py -3 -m pytest

  - name: import_sanity
    run: |
      $env:PYTHONPATH='src'
      py -3 -c "import tests.test_bootstrap_layers"
```
