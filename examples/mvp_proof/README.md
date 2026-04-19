# MVP Proof Evidence Capture

This folder documents the current evidence-package shape for Story 6.

At this stage, Context Atlas does **not** yet have one command that generates
all proof artifacts for every workflow. Instead, the current proof flow is:

1. run a supported workflow and save its generated artifacts
2. prepare a naive baseline rendered-context artifact for the same scenario
3. package both sides into one reproducible JSON evidence file with
   [`scripts/mvp_proof/capture_evidence.py`](/context-atlas/scripts/mvp_proof/capture_evidence.py)

That capture step is intentionally a packaging boundary, not a second workflow
runner. It should package the canonical packet, trace, and rendered-context
artifacts emitted by one supported workflow path. It should not be treated as a
place to hand-author replacement packet JSON or proof-only trace shapes.

The capture script expects:

- a workflow name
- a scenario name
- the query or task text
- a short input summary
- a naive baseline rendered-context artifact
- an Atlas packet artifact
- an Atlas trace artifact
- an Atlas rendered-context artifact

For constrained proof scenarios, the capture script can also assert that the
Atlas packet and trace really do show budget pressure rather than merely using a
smaller number in narration:

- pass `--expect-budget-pressure` for scenarios that are supposed to show
  compression or budget-driven exclusion
- the script will then require visible budget metadata plus at least one
  budget-pressure signal in the packet or trace artifacts

The first constrained hardening target now uses the supported repository
workflow with `--total-budget 64`; see
[`inputs/README.md`](/context-atlas/examples/mvp_proof/inputs/README.md) for the
exact run and packaging commands.

Before packaging those artifacts, the script now also verifies that the Atlas
packet and Atlas trace still look like one canonical workflow run:

- the packet includes a canonical embedded trace
- the standalone trace includes workflow metadata
- the trace metadata `request_workflow` matches the declared `--workflow`
- the packet trace identifier matches the standalone trace identifier

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

Recommended review order for each captured package:

1. read `artifacts.baseline_rendered_context`
2. read `artifacts.atlas_rendered_context`
3. inspect `artifacts.atlas_packet`
4. inspect `artifacts.atlas_trace`
5. record notes against the `review_path.rubric_dimensions` list

That order is deliberate. The proof story should answer whether Atlas improved
over a naive baseline, not simply whether the Atlas output looks reasonable in
isolation.
