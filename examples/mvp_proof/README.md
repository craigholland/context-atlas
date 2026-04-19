# MVP Proof Evidence Capture

This folder documents the current evidence-package shape for Story 6.

At this stage, Context Atlas does **not** yet have one command that generates
all proof artifacts for every workflow. Instead, the current proof flow is:

1. run a supported workflow and save its generated artifacts
2. prepare a naive baseline rendered-context artifact for the same scenario
3. package both sides into one reproducible JSON evidence file with
   [`scripts/mvp_proof/capture_evidence.py`](/context-atlas/scripts/mvp_proof/capture_evidence.py)

The capture script expects:

- a workflow name
- a scenario name
- the query or task text
- a short input summary
- a naive baseline rendered-context artifact
- an Atlas packet artifact
- an Atlas trace artifact
- an Atlas rendered-context artifact

Example:

```powershell
python scripts/mvp_proof/capture_evidence.py `
  --workflow codex_repository `
  --scenario repo_docs_refactor `
  --query "Refactor the settings loader to remove duplicated validation logic." `
  --input-summary "repo_root=sample_repo; docs_root=sample_repo/docs" `
  --baseline-rendered tmp\baseline.txt `
  --atlas-packet tmp\packet.json `
  --atlas-trace tmp\trace.json `
  --atlas-rendered tmp\atlas_rendered.txt `
  --note "Baseline included duplicate planning notes." `
  --output tmp\evidence\repo_docs_refactor.json
```

The resulting JSON package is meant to be review-friendly and reproducible. It
should become one of the primary inputs for later Story 6 workflow comparison
and MVP readiness assessment work.
