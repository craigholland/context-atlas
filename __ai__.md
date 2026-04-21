# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: c9ee71f1d304f7d3ef5bac728a6c32f1fe47a7dc
- timestamp_utc: 2026-04-21T20:02:32Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: .
- included:
  - "README.md"
  - "CONTRIBUTING.md"
  - "pyproject.toml"
  - ".gitignore"
  - ".env.example"
  - "__ai__.md"
  - "__ai__.template.md"
  - ".githooks/**"
- excluded:
  - "docs/**"
  - "src/**"
  - "tests/**"
  - "scripts/**"
  - ".github/workflows/**"
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Defines repo-level operational rules that apply before recommending a push or merge.
- Connects the local `__ai__.md` contract system to a single repo-wide preflight entrypoint.
- Establishes hook and packaging expectations for the standalone Context Atlas library repo.
- Keeps the tracked example environment surface aligned with supported runtime settings.
- Makes the visible runtime knob surface reviewable at the repo root as ranking, compression, memory, and observability defaults begin to grow.
- Treats runtime config dependencies as part of the visible package contract when infrastructure moves from ad hoc parsing to validated libraries like Pydantic.
- Treats canonical domain artifacts as part of the visible package contract when the domain model standard shifts from starter dataclasses to frozen Pydantic models.
- Treats public policy request/result/configuration objects as part of the same modeling contract so the repo does not drift back to mixed boundary styles.
- Provides the contributor on-ramp for using the ontology system correctly when adding new project documents.

## Architectural Rules
- Before recommending a push or merge, contributors should run `py -3 scripts/preflight.py`.
- The tracked pre-push hook under `.githooks/pre-push` is the preferred enforcement mechanism for local pushes.
- Repo-root policy should stay thin: package/runtime behavior belongs in `src/`, enforcement logic in `scripts/`, and reusable architecture canon in `docs/`.
- The root owner file should express repo-wide operational rules and delegate folder-specific rules to nearer `__ai__.md` files rather than duplicating them.
- When hardening slices materially change governed package or test contracts, this root owner file should still be updated alongside the nearer owner files so repo-level freshness checks remain honest.
- The repo's logging/message surface is the direct `LogMessage` pattern with stable event-name fields; contributors should not reintroduce a separate `domain/events` layer unless the authoritative docs change first.
- The repo's canonical domain-artifact standard is now frozen Pydantic models with explicit domain validation; contributors should not introduce new non-trivial dataclass artifacts without first updating the hardening plan and local owner files.
- The repo's public policy-surface standard is now also validated Pydantic models; the remaining dataclasses should be explicitly justified as private helpers or script-local records.
- The authoritative Craig Architecture docs now explicitly treat decomposition depth, folder flatness, file size, and helper-sprawl as real architectural governance concerns, not just style preferences.
- The top-tier authoritative split is now explicit: `docs/Authoritative/Canon/` is the home of portable cross-project canon, and `docs/Authoritative/Identity/` is the sibling home of Context Atlas-specific bindings.
- The authoritative architecture canon now includes `docs/Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md` as the detailed supplement for planning mechanics, decomposition sanity checks, and code-shape governance.
- The planning/decomposition canon now also treats branch naming as part of the delivery model: task-level feature branches should reflect the Task, and Codex PR-slice branches should reflect the Story, Task, and PR slice.
- The planning/decomposition canon now also treats the task-level feature PR as the main review gate: contributors should finish the Task's planned slice branches, run preflight on the feature branch, request `@codex review`, resolve findings there, and only then hand the feature PR to a human reviewer.
- Contributors should not start the next Task until the current task-level feature PR has been reviewed, fixed if needed, and merged, unless an explicit parallelization decision has been made.
- MVP planning work should now be expected to decompose from Epic to Stories to Tasks to PR plans, and those PR plans should identify expected new files, expected updated files, and relevant `__ai__.md` updates.
- Agentic-development planning should follow that same decomposition model, with product intent centered at the Epic layer, architectural bindings and boundaries centered at the Story layer, implementation-ready sequencing centered at the Task layer, and concrete file-touch guidance centered at the PR-plan layer.
- The current agentic-development planning surface now includes an Epic doc, Story docs, and Task PR plans under `docs/Planning/Agentic/`; contributors should keep those layers aligned rather than treating the Task docs as a separate planning system.
- The current post-MVP hardening planning surface now begins under `docs/Planning/Hardening/`; contributors should use that area for core assembly-engine performance, duplicate-handling, token-estimation, and budget/compression hardening rather than burying those increments inside MVP-ready status docs or release notes.
- The current hardening Epic is now specifically the context-assembly hardening surface under `docs/Planning/Hardening/context_assembly_hardening_product_definition.md`; later Story and Task decomposition there should keep retrieval-index reuse, duplicate-detection quality, token-estimation decisions, and budget/compression truthfulness grouped as one shared engine-hardening program rather than scattering them across unrelated docs.
- The current hardening planning surface now also includes Story docs under `docs/Planning/Hardening/Stories/`; contributors should use those Story docs to carry architectural hardening boundaries and task-shaping guidance before opening Task-level decomposition.
- The current hardening planning surface now also includes Task PR plans under `docs/Planning/Hardening/Stories/Tasks/`; those Task docs should carry implementation sequencing, expected file-touch guidance, and PR-slice shape without reopening Story-level scope ceilings or decision gates.
- Hardening Task feature branches should mark the task PR-plan document `IMPLEMENTED` when the integrated Task branch is ready for its review gate, and that closeout should refresh this root owner file so repo-level freshness checks stay honest.
- Hardening Story 5 should keep its regression closeout explicit: the named `test_story_5_hardening_baseline_*` tests in `tests/` are the intended anchor set for hardened engine semantics, and later closeout work should extend that named set before inventing a second proof-only regression layer.
- Hardening Task 5.2 should keep human-readable proof bounded to the canonical packet/trace bundle story under `examples/mvp_proof/`; retrieval reuse and duplicate acceptance should remain primarily test-anchored, while budget/compression and document-authority proof may use reviewable packet/trace bundles where that adds real reviewer value.
- Hardening Task 5.2 should also keep the proof-facing example docs under `examples/mvp_proof/inputs/README.md` and `examples/mvp_proof/evidence/README.md` aligned with that same boundary: they may name the budget-pressure and document-authority bundle targets explicitly, but they should not imply a second retrieval-demo, duplicate-demo, or hardening-summary artifact family.
- Hardening Task 5.2 closes with one explicit proof split: `examples/mvp_proof/` carries the bounded human-readable packet/trace bundle story for budget/compression and document-authority review, while retrieval reuse and duplicate acceptance remain intentionally anchored by the named Story 5 baseline tests until broader guide refresh work in Task 5.3.
- Hardening Task 5.3 should keep the outward-facing product story explicit across `README.md`, `docs/Guides/`, and example READMEs: the shared engine now uses a shape-aware starter estimator by default, packet/trace inspection should prefer truthful budget and compression vocabulary, and those truths should be explained in user-facing docs without leaking internal planning-story jargon into the primary workflow guides.
- Hardening Task 5.3 should keep the example layer aligned with the guide layer rather than treating `examples/README.md` and workflow-specific example READMEs as looser secondary notes; if guides now name truthful budget/compression fields or the shape-aware estimator story, the runnable example docs should echo that same user-facing language.
- Hardening Task 5.3 should also distinguish packet and trace budget labels accurately: packet inspection uses `fixed_reserved_tokens`, `unreserved_tokens`, and `unallocated_tokens`, while trace rendering currently uses `budget_fixed_reserved_tokens`, `budget_unreserved_tokens`, and `budget_unallocated_tokens`; user-facing docs should not blur those two surfaces together.
- Hardening Task 5.3 should keep `docs/Release/README.md` honest about shipped history versus current development-branch guidance; release-history docs should not imply that unreleased hardening work is already part of the current shipped tag.
- Release-prep slices that move the shipped package version forward should keep `README.md`, `pyproject.toml`, `context_atlas.__version__`, `tests/test_cli.py`, and the current note under `docs/Release/` aligned to the same version rather than advancing only one surface.
- Hardening Task 5.4 should close the Epic with one explicit evidence map from the original six findings to the named Story 5 baseline tests and bounded proof surfaces; closeout docs should not force later reviewers to reconstruct that lineage from merged PR history alone.
- Hardening Task 5.4 should also keep `docs/Planning/README.md` aligned with that final evidence path so contributors can discover the integrated Epic summary, the Story 5 proof split, the named `test_story_5_hardening_baseline_*` anchors, and the bounded `examples/mvp_proof/` surface from the planning index itself.
- Hardening Task 5.4 should leave Story 5 execution-complete but review-pending on its Story branch: final closeout edits should mark the Task plan `IMPLEMENTED`, make the Story-level handoff explicit, and direct any later follow-on work to start from the integrated evidence path rather than from the original six findings as if they were still open defects.
- The current hardening execution model now uses one Epic branch off `development`, one Story branch per Story off that Epic branch, one Task feature branch per Task off its Story branch, and PR-slice branches off the Task feature branch; review is expected at the Task feature PR rather than waiting for the full Story PR.
- Hardening Task 2.1 now treats `src/context_atlas/domain/policies/deduplication.py` as the intended inward home for the shared duplicate-detection surface; later Story 2 work should extend that helper instead of re-forking normalization and comparison rules inside ranking or memory.
- Hardening Task 2.1 also locks the initial duplicate baseline to normalized exact-key matching, normalized containment, and token overlap; later Story 2 work may refine normalization and policy integration, but it should not silently widen the comparison family without updating the Story boundary first.
- Hardening Task 2.2 now bounds boilerplate handling to top-of-file front matter and bounded shared leading prefixes; later Story 2 work should refine integration around that rule instead of inventing format-specific stripping paths or mid-document boilerplate removal.
- Hardening Story 2 review fixes should keep that front-matter boundary precise: only column-zero fences should terminate bounded top-of-file front matter, and metadata-only front-matter documents should remain distinct unless their normalized keys match exactly.
- Hardening Task 2.3 now treats ranking and memory as sharing one bounded duplicate semantics surface: ranking remains source-family-aware while memory duplicate decisions expose the shared match kind directly, and later Story 2 work should tighten coverage rather than re-forking policy-local duplicate gates.
- Hardening Task 2.4 closes Story 2 with one explicit duplicate-handling acceptance bar: case/whitespace variants, bounded front-matter variants, normalized containment, and reordered-token near duplicates may collapse, while shared-header distinct bodies, metadata-only front matter, and cross-source-family ranking inputs must stay distinct.
- Story 2 should now also treat exact full-text equality and the historical prefix-equality shortcut as rejected duplicate baselines, not as acceptable fallback strategies waiting to reappear in later hardening work.
- Story 5 validation and documentation work should inherit Story 2's explicit duplicate-handling acceptance bar and proof cases instead of renegotiating duplicate success criteria during later closeout work.
- Hardening Task 4.1 should establish explicit budget vocabulary before wider caller-contract cleanup: fixed-slot reservation, pre-allocation unreserved capacity, and post-allocation unallocated remainder should each have truthful canonical names instead of sharing one generic "remaining" label.
- Hardening Task 4.2 should preserve allocator behavior while moving caller-facing budget contracts onto the truthful vocabulary from Task 4.1; legacy `reserved_tokens` and `remaining_tokens` surfaces may remain temporarily, but packet/trace/service-facing metadata should prefer `fixed_reserved_tokens`, `unreserved_tokens`, and `unallocated_tokens`.
- Hardening Task 4.3 should make compression truth primary: effective runtime strategy belongs on the canonical result surface, while configured strategy should appear separately only when fallback or service-owned truncation would otherwise be hidden.
- Hardening Task 4.4 should keep service metadata and renderers aligned with that truth: top-level packet/trace compression strategy fields should be truthful, and packet/trace inspection should surface `unallocated_tokens` plus effective-versus-configured compression strategy without relying on stale alias names or duplicated prefixed metadata.
- Hardening Task PR plans should keep front-matter `related` links navigable from the Task directory itself; repo-root targets like `src/`, `examples/`, and sibling docs surfaces should use the full repo-root-relative path depth instead of assuming the Story directory level.
- Hardening Task PR plans should also make upstream conditionality explicit when a prior Task can change downstream file expectations or activation state; do not let "none expected" or parallel-looking Task wording hide a real decision gate or extraction-dependent file path.
- Hardening Story docs should make file-placement expectations, kickoff decision-record locations, and known ripple surfaces explicit at the Story layer whenever later Tasks would otherwise have to infer them from the existing codebase.
- Hardening Story 3 now records an explicit `heuristic-first` kickoff decision; Task 3.2 is the lead path for improving starter token estimation, while Task 3.3 remains bounded complementary seam work unless the Story boundary is reopened deliberately.
- Hardening Task 3.2 and Task 3.3 should now say that same thing at the Task layer: 3.2 is the active implementation track, and 3.3 is complementary seam work that must not masquerade as a second primary Story 3 path.
- Hardening Task 3.2 should keep starter token-estimation improvement bounded to provider-agnostic content-shape distinctions such as prose baseline, code/markup tightening, and non-Latin-heavy tightening; it should not introduce hidden tokenizer tables or provider-specific counting rules.
- Hardening Task 3.2 is now the delivered lead-path baseline for Story 3: starter estimation is content-shape-aware for prose, structured code/markup, and non-Latin-heavy text, while tokenizer-specific integration remains intentionally deferred to the bounded seam work.
- Hardening Task 3.3 should now keep the complementary tokenizer seam narrow: a generic callable token-estimation contract may be bound outward through infrastructure composition, but provider-specific tokenizer selection, SDK ownership, and broader provider integration must remain out of scope.
- Hardening Task 3.4 should keep the Story 3 runtime surface truthful: `CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN` remains the baseline control for the shape-aware starter heuristic, while any custom token estimator remains an outward callable seam rather than an env-backed tokenizer selector.
- Story 3 review fixes should keep compression-prefix budgeting correctness-first: once token estimation becomes shape-aware or outward-callable, longest-fitting-prefix helpers must not rely on binary-search monotonicity assumptions.
- Hardening Story 4 should now inherit that Story 3 lead-path decision explicitly: budget and compression truthfulness work should assume the starter heuristic correction lands before any tokenizer seam grows into more than bounded outward support work.
- The new `docs/Authoritative/Canon/AgenticDevelopment/` surface is the portable, environment-agnostic canon for agentic-development concepts; application-specific bindings and environment-specific materialization details should not be authored there unless the authoritative boundary model changes first.
- The `docs/Authoritative/Canon/AgenticDevelopment/` canon should remain readable from its directory-level README so contributors do not have to reverse-engineer later project bindings or runtime assets just to understand the portable layer.
- The `docs/Authoritative/Canon/AgenticDevelopment/` canon now also carries the portable drift, validation, and change-management models; later planning, binding, and runtime surfaces should inherit those models instead of inventing parallel governance vocabularies.
- The portable agentic canon should keep authority, mode, skill, and materialization concerns in separate authoritative docs rather than collapsing them back into one general narrative.
- The new `docs/Authoritative/Canon/RepoManagement/` surface is the portable canon for repository principals, authorization, operation families, branch-target policy, and audit identity; provider- or project-specific GitHub policy should not be authored there unless the portable boundary changes first.
- The project-specific repository-provider binding for Context Atlas should now live under `docs/Authoritative/Identity/RepoManagement/`; GitHub principal rosters, operation matrices, branch-target merge policy, and audit identity should not be treated as Codex-binding details or runtime folklore.
- GitHub-facing review and merge behavior for agentic roles should inherit from the RepoManagement binding layer; Codex materialization docs may explain how a runtime discovers assets, but they should not become the source of repository authority.
- The `docs/Authoritative/Canon/RepoManagement/` surface is now also governed by its own local owner file; contributors should treat provider supplements there as reusable canon, not as project-specific GitHub policy.
- The portable agentic canon should keep workflow protocol guidance under `docs/Authoritative/Canon/AgenticDevelopment/Protocols/`; those docs should stay workflow-centered, share the common protocol template, and reserve explicit space for gate context, review-pass expectations, and structured contract state where relevant.
- The portable protocol canon should keep the initial workflow family explicit: planning, execution, review, rework, and recovery should remain first-class protocol docs, while review passes stay defined as lenses inside review work rather than separate roles, modes, or protocol families.
- The portable agentic canon should now also keep runtime-capacity and parallel-decomposition guidance explicit through `docs/Authoritative/Canon/AgenticDevelopment/Runtime-Capacity-Model.md` and `docs/Authoritative/Canon/AgenticDevelopment/Parallel-Decomposition-Model.md`; later project bindings should inherit those models instead of restating them ad hoc in planning docs or runtime assets.
- Structured delegation, handoff, and escalation movement in the portable protocol canon should bind to explicit protocol docs and should keep contract state machine-readable, including requested review-pass and review-outcome fields when work is moving into or out of review.
- Project-specific protocol bindings should now live under `docs/Authoritative/Identity/AgenticDevelopment/`; contributors should keep role participation, mode participation, and gate-to-review-pass mapping in separate binding docs instead of burying them inside runtime materialization files or flattening them into one matrix.
- The portable agentic canon should also keep delegation and agent-composition rules explicit so later role, protocol, and environment work inherit a stable parent-versus-specialist boundary instead of redefining it ad hoc.
- The portable agentic canon should keep skills explicitly atomic and should define skill attachment separately from skill content, so later role, protocol, and environment work do not smuggle workflow or authority semantics into skill definitions.
- The portable agentic canon should also keep the composition decision tree explicit: contributors should prefer adding a skill first, introduce a specialist only when a real bounded authority difference exists, and keep work parent-owned when delegation would mostly escalate back upward.
- The project-specific structural binding for agentic development should live under `docs/Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md`; contributors should not bypass that profile by jumping directly from portable canon to role, mode, protocol, or environment-materialization assumptions.
- The project-specific runtime-capacity planning input should now live at `docs/Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml`, with the human update and trust model documented in `docs/Authoritative/Identity/AgenticDevelopment/runtime_capacity.md`; contributors should not create alternate planning-capacity sources in Story docs, prompts, or runtime-specific folders.
- The project-specific role roster for agentic development should live under `docs/Authoritative/Identity/AgenticDevelopment/Role-Model.md`; contributors should not let specialist labels, runtime worker names, or tool-specific naming conventions become a shadow role model, and they should not imply a dedicated frontend/UI role until the repository actually owns that kind of product surface.
- The portable role-archetype catalog for agentic development should live under `docs/Authoritative/Canon/AgenticDevelopment/RoleArchetypes/`; project-specific role docs under Identity should refine those archetypes rather than acting as the first place reusable role patterns are defined.
- The project-specific accountability and ownership surface for agentic-development roles should live under `docs/Authoritative/Identity/AgenticDevelopment/Role-Accountability-Matrix.md`; contributors should keep specialist participation subordinate to parent-owned role accountability instead of creating a second ownership layer.
- The project-specific authority surface for agentic-development roles should live under `docs/Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md`; contributors should keep approval, merge, release, and workflow authority explicit instead of letting it drift out of ownership or implementation participation.
- The project-specific role-to-parent binding for agentic development should live under `docs/Authoritative/Identity/AgenticDevelopment/Role-Agent-Binding-Model.md`; contributors should not let specialists, runtime files, or worker labels become substitute expressions of top-level project accountability.
- The project-specific mode model for agentic development should live under `docs/Authoritative/Identity/AgenticDevelopment/Mode-Model.md`; contributors should keep modes as execution states rather than letting them collapse into role aliases, protocol names, or runtime prompt habits.
- Entry/exit rules, mutation scopes, role-to-mode applicability, and transition graphs for the project-specific mode model should remain explicit companion docs under `docs/Authoritative/Identity/AgenticDevelopment/` rather than being scattered across role notes or runtime materialization files.
- The project-specific mode-transition graph should preserve the normal planning-to-implementation path when structured planning output hands work to a deliverable-producing role; contributors should not force that baseline flow through recovery or restart semantics.
- Inter-agent handoff, escalation, and review-intake state for the agentic-development model should be defined as structured machine-readable contracts, typically representable as YAML or JSON, rather than prose-only status updates.
- The target review model for agentic development is role-owned QA intake from a structured completion handoff, not long-term dependence on tool-specific trigger comments as the canonical review mechanism.
- The portable agentic layer should preserve an explicit three-layer split between portable canon, application-specific bindings, and environment-specific materialization; contributors should not let concrete role rosters, workflow gates, or environment folder conventions leak upward into the canon.
- When editing the portable agentic canon, contributors should treat named applications, named environment vendors, concrete mode selections, concrete workflow gates, current capacity values, and implementation layouts as downstream binding-layer content rather than portable definitions.
- The agentic planning stack for Stories 7 and 8 should continue to treat the portable boundary model as upstream authoritative guidance; materialization planning should bind to Story 1 rather than restating or replacing it.
- The portable materialization layer should keep the generic template model and template-contract surface explicit so later environment bindings inherit one upstream template vocabulary instead of inventing runtime-shaped substitute taxonomies.
- The portable materialization layer should define abstract discovery requirements separately from environment-specific folder conventions so later bindings can choose concrete layouts without rewriting the discovery model.
- When later environment bindings introduce folder conventions, manifests, or indexes, they should document those mechanics as downstream mappings of the portable discovery model rather than treating them as new portable canon.
- The portable materialization layer should keep traceability expectations explicit so later runtime assets can point back to canon, bindings, and template surfaces without inventing a platform-local provenance model first.
- The portable materialization layer should also keep maintenance-mode and regeneration expectations explicit so downstream bindings do not hide whether assets are hand-maintained, generated, or mixed.
- The portable drift model should stay shared across AgenticDevelopment and RepoManagement surfaces so later validators and reviewers do not invent separate drift taxonomies for neighboring governed layers.
- The portable agentic validation model should remain focused on structural trustworthiness of canon, bindings, planning inputs, and runtime assets; it should not drift into hidden workflow-state review or live scheduler claims.
- The portable change-management model should keep semantic changes flowing through the highest authoritative layer that owns them before downstream bindings, planning docs, or runtime assets are updated.
- The Context Atlas Codex binding should express its concrete runtime layout through the Identity-layer docs under `docs/Authoritative/Identity/AgenticDevelopment/codex/`; later `.codex/` and `.agents/skills/` assets should inherit that layout instead of inventing ad hoc folder conventions from memory.
- The Context Atlas Codex binding should also keep a repeatable creation path through its template set and `creation_guidance.md`; later Codex runtime assets should not be authored from memory when the binding docs already define what is copied, adapted, and derived.
- The Context Atlas Codex governance surface should anchor drift and refresh expectations to the portable `Drift Model` and the Story 10 validation/governance closeout, not to stale earlier Story numbers that can change as the planning stack evolves.
- Broader doc indexes such as `docs/README.md`, `docs/Authoritative/Canon/Architecture/README.md`, and `docs/Planning/README.md` should surface the AgenticDevelopment canon explicitly so contributors can discover it before writing application-specific bindings or materialized assets.
- Broader doc indexes should now also surface the RepoManagement canon explicitly so contributors working on repository principals, review surfaces, or branch policy can start from the portable layer before writing project-specific GitHub bindings.
- The `docs/Authoritative/Canon/AgenticDevelopment/README.md` file should remain the portable entrypoint for human readers; later Story docs should inherit that orientation instead of compensating for a weak canon index.
- Cross-links between `docs/README.md`, `docs/Authoritative/Canon/Architecture/README.md`, `docs/Authoritative/Canon/AgenticDevelopment/README.md`, and `docs/Planning/README.md` should preserve the reading order from portable canon to project binding to planning rather than flattening those layers together.
- Downstream Agentic Story docs should point back to the relevant portable AgenticDevelopment canon docs in their inputs or related artifacts instead of expecting Task plans to reconstruct that lineage.
- The docs under `docs/Authoritative/Canon/AgenticDevelopment/` should not point downward into planning Stories or other project-actualization artifacts; that canon should reference peer authoritative docs and describe downstream layers only in generic terms.
- The planning stack under `docs/Planning/` should include an orienting README, and Story docs should carry a lightweight Definition Of Done so review expectations stay visible before implementation starts.
- MVP Task PR-plan docs should carry a basic `Task Status` field using `PLANNED`, `WORKING`, or `IMPLEMENTED` so task-level progress remains visible before contributors open individual PR-plan slices.
- There is no currently active MVP task; Story 7 is complete and the current baseline is the merged `MVP Ready` recommendation plus its standing proof scenarios.
- The Task 7.3 configuration-surface decision is now part of the active proof baseline: the supported env-backed surface includes `CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION`, while ranking authority tables, memory-scoring semantics, and canonical slot identifiers remain internal by design.
- The architecture canon under `docs/Authoritative/Canon/Architecture/` should include a directory-level README so contributors can orient to the full Craig Architecture set before jumping into individual supplements.
- The current MVP-supported package surface is now centered on `context_atlas.api`; repo-level docs and examples should prefer that curated starter namespace over deep internal module paths unless they are deliberately teaching architectural seams.
- Product-facing repo guidance should stay aligned around one visible golden path from install to configure to assemble to inspect; contributors should not let root docs, examples, and runtime-knob docs drift into separate onboarding stories.
- The getting-started guide and starter context-flow example are now part of that visible onboarding path; contributors should keep them aligned with the supported starter imports, runtime knobs, and inspection surfaces.
- The starter context-flow example is now the recommended first-run path, while the smoke script is secondary; root guidance should preserve that distinction instead of presenting both as equal onboarding surfaces.
- The recommended first-run story should prefer the editable-install path and the quieter starter example output; repo-local `PYTHONPATH` usage and smoke scripts should stay secondary and clearly labeled.
- Product-facing docs should not imply that `.env.example` or a copied `.env` file is loaded automatically; the current runtime settings loader reads the live process environment only.
- Product-facing docs should keep the supported env-backed surface intentionally narrow and should not imply that every starter constant in `domain/policies/` or `services/` is automatically a public runtime knob.
- Product-facing setup guidance should point users to `docs/Guides/` first; runnable artifacts under `examples/` are companion material and should not become the primary setup surface.
- Product-facing guides and runnable example READMEs should avoid Windows-only operator assumptions; if PowerShell-specific activation or environment syntax is shown, the same surface should also give at least one bash/Linux/macOS analog.
- Shipped release summaries should now live in `docs/Release/` as in-repo `releases`-class artifacts instead of existing only as GitHub release text or ad hoc status notes.
- The release-history surface should stay discoverable through `docs/Release/README.md`, and the current shipped release note should move forward deliberately rather than leaving the root README pinned to an older release forever.
- The root `CONTRIBUTING.md` file should stay aligned with the ontology and directory model so a new contributor can get from "I want to add a document" to the correct class, template, and destination without reverse-engineering the doc system.
- The guides under `docs/Guides/` should stay aligned with the actual runnable example boundaries, including which workflows support one-shot budget overrides or proof-artifact emission and which ones do not.
- The technical-builder documents-plus-database workflow is now a first-class product-facing guide path alongside the starter and repository workflows; repo-facing docs should keep its already-fetched-record boundary and shared runtime-knob story aligned across README, examples, and guide docs.
- The starter inspection story should surface packet and trace views as derived renderers under `context_atlas.rendering`, not as alternate canonical models or prompt-first strings.
- The first product-facing packet inspection surface should emphasize selected sources, retained memory, budget state, and compression without requiring direct model dumps.
- The first trace inspection surface should emphasize ordered decisions, exclusions, transformations, and trace metadata rather than raw `model_dump()` output.

## Allowed Dependencies
- may depend on:
  - repository metadata files
  - repo-owned scripts and hooks
- must not depend on:
  - folder-specific rules being restated here when a nearer owner file already governs them
  - hidden local-only push behavior that is not represented by tracked scripts or hooks

## Public API / Key Exports
- `pyproject.toml`:
  - project metadata, author info, Python floor, dev-tool declarations, and installable starter script
- `CONTRIBUTING.md`:
  - root contributor on-ramp for choosing the right document class, template, and destination
- `__ai__.template.md`:
  - baseline authoring template for local contract files
- `.env.example`:
  - tracked example environment surface for supported runtime knobs
- `__ai__.md`:
  - repo-level operational contract for preflight and push readiness
- `.githooks/pre-push`:
  - tracked pre-push hook that runs repo preflight

## File Index
- `pyproject.toml`:
  - responsibility: defines package metadata and repo-local developer tool dependencies
  - invariants:
    - Python floor here should match active CI and local preflight assumptions
    - runtime validation libraries added here should correspond to real package behavior, not speculative future plans
- `CONTRIBUTING.md`:
  - responsibility: gives contributors one clear path into the ontology/template system before they author new repo documents
  - invariants:
    - should point to the current ontology canon rather than restating a parallel document-class system
    - should keep Canon versus Identity placement guidance explicit for contributors adding authoritative docs
- `__ai__.template.md`:
  - responsibility: provides the reusable authoring shape for local owner files
  - footguns:
    - changes here should be reflected intentionally in validator expectations and local owner files
- `.env.example`:
  - responsibility: makes the supported environment-backed runtime settings visible at the repo root
  - invariants:
    - keys here should reflect the actual environment surface supported by infrastructure config loaders
    - assembly and memory default knobs should stay intentionally small and clearly operator-facing
- `src/context_atlas/domain/models/*.py`:
  - responsibility: define the canonical Pydantic-backed artifacts consumed across the package
  - invariants:
    - non-trivial canonical artifacts should remain frozen Pydantic models rather than drifting back to mixed constructor styles
    - inner metadata maps should stay immutable so packet/source state remains trustworthy once assembled
- `__ai__.md`:
  - responsibility: states repo-wide operational rules before push or merge
  - invariants:
    - must call out the canonical preflight entrypoint
- `.githooks/pre-push`:
  - responsibility: executes repo preflight before local pushes when hooks are installed
  - footguns:
    - tracked hook file is inert until `core.hooksPath` points at `.githooks`

## Known Gaps / Future-State Notes
- The current root contract is strong on push readiness and repo governance, but it is still thinner on release/versioning policy, packaging/publication workflow, and post-merge operational automation.
- The tracked Git hook remains opt-in per clone until local setup tooling configures `core.hooksPath` automatically.
- The supported runtime-knob surface is intentionally narrow; many ranking, memory, and slot-level constants remain internal implementation details rather than env-backed settings.
- The flagship repository workflow is still governed-docs-first. It does not yet represent full code crawling, git/history awareness, issue-system ingestion, or broader repository connector coverage.
- The mixed-source technical-builder workflow still assumes already-fetched record payloads. Atlas shapes and governs those payloads, but it does not yet own database, vector-store, or API client integration.
- The low-code workflow is still a small preset-driven wrapper over the shared engine, not a broader no-code product surface with connector management or hidden config loading.
- The current MVP proof set is evidence-backed and sufficient for the `MVP Ready` recommendation, but it is still limited to the tracked local scenarios under the three supported workflows rather than a broader external-service or production-style evaluation matrix.
- Product-facing docs must continue to stay synchronized across the root README, `docs/Guides/`, `examples/README.md`, and `.env.example`; drift between those surfaces remains an ongoing maintainability risk.
- Release-history documentation now has an in-repo home, but the repo still does not have a fuller release-process canon for branching, cutover, publication cadence, or post-release follow-up.

## Cross-Folder Contracts
- `scripts/`: root policy delegates actual enforcement logic to repo-owned scripts; changing script entrypoints should update this contract.
- `docs/Authoritative/Canon/AgenticDevelopment/`: roles, protocols, runtime-capacity semantics, materialization rules, drift vocabulary, validation expectations, and governed change paths should stay portable here and flow downward into project bindings rather than being restated in planning or runtime docs.
- `docs/Authoritative/Canon/RepoManagement/`: repository-principal, authorization, operation-family, branch-target, and audit-identity semantics should stay portable here and flow downward into project bindings rather than being restated in runtime docs.
- `docs/Authoritative/Canon/AgenticDevelopment/__ai__.md` and `docs/Authoritative/Canon/RepoManagement/__ai__.md`: the nearest owner files for those canon surfaces should stay aligned when Story-level governance or validation expectations change.
- `docs/Planning/Hardening/`: core assembly-engine hardening work should decompose here once it moves beyond one-off review notes, and later Story/Task docs in that surface should stay aligned with the same Craig-style planning depth used by the MVP and Agentic stacks.
- `src/context_atlas/`: preflight should prove repo readiness without redefining package-layer rules that belong to nearer owner files.
- `src/context_atlas/infrastructure/`: supported environment variable keys in config loaders should stay mirrored in `.env.example`.
- `src/context_atlas/infrastructure/`: assembly and memory default settings plus structured observability helpers should not grow new env knobs without updating the repo root surface.
- `.github/workflows/`: CI should mirror the local preflight closely enough that GitHub failures are usually reproducible before push.

## Verification Contract
```yaml
steps:
  - name: validate_root_owner
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md

  - name: import_boundaries
    run: |
      py -3 scripts/check_import_boundaries.py --repo-root . --config scripts/import_boundary_rules.toml

  - name: test_and_typecheck
    run: |
      py -3 -m ruff check .
      py -3 -m ruff format --check .
      py -3 -m mypy src
      py -3 -m pytest
```

