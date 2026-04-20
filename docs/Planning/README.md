# Planning

This directory holds forward-looking execution intent for Context Atlas.

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

The current MVP planning stack lives under [MVP](./MVP/):

- [MVP Product Definition](./MVP/mvp_product_defintiion.md)
- [Story docs](./MVP/Stories/)
- [Task PR plans](./MVP/Stories/Tasks/)

The current agentic-development planning surface lives under [Agentic](./Agentic/):

- [Agentic Development Product Definition](./Agentic/agentic_development_product_definition.md)
- [Story docs](./Agentic/Stories/)
- [Task PR plans](./Agentic/Stories/Tasks/)

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
[docs/Authoritative/Identity/AgenticDevelopment/codex/](../Authoritative/Identity/AgenticDevelopment/codex/).
Planning docs should treat that directory as the downstream Codex entrypoint
rather than restating Codex runtime conventions in planning prose.

When planning depends on machine-readable governance input, that input should
live in the authoritative layers rather than inside planning docs themselves.
For the agentic-development stack, runtime-capacity planning input belongs in
the Identity layer artifact at
[runtime_capacity.yaml](../Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml),
with its human update/trust model defined in
[runtime_capacity.md](../Authoritative/Identity/AgenticDevelopment/runtime_capacity.md).

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

