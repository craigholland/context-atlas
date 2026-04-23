# Planning

This directory holds forward-looking execution intent for Context Atlas.

Active planning work should live directly under `docs/Planning/` until it is
completed. Once an Epic and its downstream Story/Task decomposition are no
longer the active future-planning surface, move that stack under
`docs/Planning/completed/` so contributors can distinguish upcoming work from
historical execution intent at a glance.

There is currently one active planning surface in this directory:

- [013 Cleanup Product Definition](./013_Cleanup/013_cleanup_product_definition.md)

This numbered Epic now holds the active cleanup horizon for fast-ROI
review-response work around:

- product-evaluator onboarding clarity
- product-path separation from contributor and governance surfaces
- portable Canon leak cleanup
- immediate generated-surface defect cleanup
- Linux-first CI and executable contract-command alignment

The most recent small follow-up tasks have moved under
[completed](./completed/):

- [Task - Codex Runtime Materialization Enforcement PR Plan](./completed/task_codex_runtime_materialization_enforcement.md)
- [Task - __ai__ Owner-File Compaction And Hygiene PR Plan](./completed/task_ai_owner_file_compaction_and_hygiene.md)
- [Task - README Map And Tour Separation PR Plan](./completed/task_readme_map_and_tour_split.md)

Planning artifacts here should derive their decomposition model from [Craig Architecture - Planning And Decomposition](../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md).

The expected planning stack is:

- `Epic` documents for major product or delivery surfaces
- `Story` documents for architectural increments inside an Epic
- `Task` documents for implementation-ready decomposition of a Story, including a basic `Task Status` field (`PLANNED`, `WORKING`, or `IMPLEMENTED`)
- task-level PR-plan documents for bounded reviewable slices

The expected execution loop for a Task is:

- open the task-level feature branch and feature PR early
- mark the Task `WORKING`
- implement bounded PR slices on short-lived slice branches and merge them back into the task feature branch
- when the Task's planned slices are complete, mark it `IMPLEMENTED`
- run local preflight on the feature branch, request `@codex review`, and resolve findings there
- hand the clean feature PR to a human reviewer before starting the next Task unless an explicit parallelization decision has been made

Completed planning stacks now live under [completed](./completed/):

- [MVP](./completed/MVP/)
  This archive contains the shipped MVP product definition, Story docs, and
  Task PR plans.
- [Agentic](./completed/Agentic/)
  This archive contains the completed agentic-development planning stack.
- [Hardening](./completed/Hardening/)
  This archive contains the completed context-assembly hardening planning
  stack.

The completed MVP planning stack lives under [MVP](./completed/MVP/):

- [MVP Product Definition](./completed/MVP/mvp_product_defintiion.md)
- [Story docs](./completed/MVP/Stories/)
- [Task PR plans](./completed/MVP/Stories/Tasks/)

The completed agentic-development planning surface lives under
[Agentic](./completed/Agentic/):

- [Agentic Development Product Definition](./completed/Agentic/agentic_development_product_definition.md)
- [Story docs](./completed/Agentic/Stories/)
- [Task PR plans](./completed/Agentic/Stories/Tasks/)

The completed post-MVP hardening planning surface begins under
[Hardening](./completed/Hardening/):

- [Context Assembly Hardening Product Definition](./completed/Hardening/context_assembly_hardening_product_definition.md)
- [Story docs](./completed/Hardening/Stories/)
- [Task PR plans](./completed/Hardening/Stories/Tasks/)

The Hardening stack now also has an explicit closeout evidence path:

- the integrated Epic-level resolution map lives in
  [Context Assembly Hardening Product Definition](./completed/Hardening/context_assembly_hardening_product_definition.md)
- the Story-level review path and proof split live in
  [Story 5 - Validation, Documentation, And Hardening Proof](./completed/Hardening/Stories/story_5_validation_documentation_and_hardening_proof.md)
- the named `test_story_5_hardening_baseline_*` regressions in `tests/` are
  the primary executable review anchors
- bounded human-readable proof remains under `examples/mvp_proof/` rather than
  expanding into a second artifact family for every hardened concern

Those planning artifacts should derive their portable vocabulary and boundary
rules from [docs/Authoritative/Canon/AgenticDevelopment/README.md](../Authoritative/Canon/AgenticDevelopment/README.md)
and its neighboring canon docs instead of redefining those concepts at the
planning layer.

When planning depends on repository principals, permissions, review surfaces,
branch-target policy, or audit identity, those semantics should derive from
[docs/Authoritative/Canon/RepoManagement/README.md](../Authoritative/Canon/RepoManagement/README.md)
and the downstream project binding under
[docs/Authoritative/Identity/RepoManagement/](../Authoritative/Identity/RepoManagement/)
rather than being invented in Story prose or runtime-materialization docs.

For the Codex materialization Story in the agentic-development stack, the
project-specific runtime binding, layout, template, creation, and governance
surfaces live under
[docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/).
Planning docs should treat that directory as the downstream Codex entrypoint
rather than restating Codex runtime conventions in planning prose.

When planning depends on machine-readable governance input, that input should
live in the authoritative layers rather than inside planning docs themselves.
For the agentic-development stack, runtime-capacity planning input belongs in
the Identity layer artifact at
[runtime_capacity.yaml](../Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml),
with its human update/trust model defined in
[runtime_capacity.md](../Authoritative/Identity/AgenticDevelopment/Bindings/runtime_capacity.md).

If a planning artifact needs to explain what a role, mode, skill, protocol, or
materialization layer means, the first fix should usually be to improve the
AgenticDevelopment canon rather than expanding the planning doc into a second
source of truth.

If planning depends on drift detection, validation boundaries, or governed
change paths for the agentic stack, those expectations should derive from:

- [docs/Authoritative/Canon/AgenticDevelopment/Drift-Model.md](../Authoritative/Canon/AgenticDevelopment/Drift-Model.md)
- [docs/Authoritative/Canon/AgenticDevelopment/Validation-Model.md](../Authoritative/Canon/AgenticDevelopment/Validation-Model.md)
- [docs/Authoritative/Canon/AgenticDevelopment/Change-Management-Model.md](../Authoritative/Canon/AgenticDevelopment/Change-Management-Model.md)

Planning docs should reference those models rather than introducing a second
validation or drift vocabulary in story/task prose.

Contributors should prefer planning artifacts that move from:

- product-level intent at the Epic layer
- architectural shape at the Story layer
- implementation sequencing at the Task layer
- concrete code-touch expectations at the PR-plan layer

Planning documents are not authoritative project truth in the same sense as the `Authoritative` docs. They describe intended work, sequencing, and decomposition, and they must yield to the authoritative canon when conflicts appear.

