Request Check Result: Appropriate for task-card generation

Information Check Result: Sufficient information to proceed

Additional Considerations Requiring Decision

- The summary must stay deterministic and derived from existing pre-commit and staged-review artifacts rather than from any model-generated interpretation.
- The summary must improve scanability without becoming a second source of truth that can drift from `artifacts/pre-commit/run_<timestamp>.json` or the staged-review artifact set.
- The implementation must preserve current fail-fast behavior and must not reduce the visibility of blocking detail already emitted by the underlying scripts.

Task Card Example

Title

`chore: improve pre-commit and staged-review summary legibility`

Requirement / Problem Statement

FinOpsAI's repo-managed pre-commit and staged-review workflow already writes detailed artifacts, but the operator-visible summaries remain less legible than they could be for quick human review. `scripts/git/pre_commit.sh` produces a JSON audit artifact and `scripts/git/review/run_staged_review.sh` produces summary and full review artifacts, yet the current workflow does not provide a tight, deterministic legibility layer that makes run status, check results, skip reasons, artifact paths, and blocked outcomes easy to scan without opening the full artifacts.

Improve deterministic pre-commit and staged-review summary legibility for operators while preserving the existing JSON audit artifact and review outputs as the authoritative detailed records.

Expected Outcome

The pre-commit and staged-review workflow presents a clearer deterministic summary of each run that shows:
- overall run result
- executed check names and statuses
- skipped checks and why they were skipped when applicable
- where the full audit and review artifacts were written
- and whether the commit was blocked or passed

The summary remains aligned with the underlying authoritative artifacts and does not invent, reinterpret, or soften results.

Business Context

This is an internal engineering workflow improvement for FinOpsAI's repo-managed quality-gate system. It supports faster local verification, clearer review handoff, and better usability of existing harness artifacts without changing accounting runtime behavior, posting behavior, or deterministic bookkeeping logic.

Scope

In scope:
- improve the operator-facing deterministic summary layer for the existing pre-commit and staged-review workflow
- define summary content and formatting rules
- keep the summary sourced from existing run and review results
- update the governing engineering documentation to describe the summary behavior
- preserve current audit-artifact generation, staged-review artifact generation, and fail-fast semantics

Out of scope:
- changing accounting behavior, validation rules, or posting eligibility
- replacing or removing the JSON audit artifact or staged-review artifacts
- adding model-generated summaries or LLM interpretation
- redesigning the full pre-commit pipeline order
- bundling this work with the separate staged-file test-routing card

Acceptance Criteria

1. Running the repo-managed pre-commit workflow produces a concise deterministic summary for each run in addition to the existing JSON audit artifact.
2. The summary includes the run result, executed check names, each check status, and the path to the generated audit artifact.
3. When a check is skipped, the summary indicates that it was skipped rather than silently omitting it.
4. When staged review artifacts are produced, the workflow exposes their artifact paths in a predictable operator-readable way.
5. When a check fails, the summary preserves clear blocked and failure visibility and does not hide the underlying failure outcome.
6. Summary content is derived from the same run and review data already used to build the authoritative artifacts and does not become an independent competing source of truth.
7. Existing pre-commit fail-fast behavior remains intact.
8. Existing audit artifact generation under `artifacts/pre-commit/` and staged-review artifact generation under `artifacts/reviews/` remain intact.
9. Documentation in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` is updated to describe the summary behavior and its relationship to the authoritative artifacts.
10. Focused verification is added or updated to cover the deterministic summary behavior without inventing unrelated workflow scope.

Constraints

- Keep the work deterministic and local-only.
- Do not add any model, LLM, network, RAG, MCP, or external-service dependency.
- Do not weaken or bypass existing review, validation, approval, privacy, or posting constraints.
- Keep the JSON audit artifact and staged-review artifacts as the authoritative detailed records.
- Keep implementation aligned with `/Users/Sites/Repo-FinOpsAI/AGENTS.md`, especially the repository's deterministic workflow, dependency, privacy, and tooling constraints.
- Do not combine this card with the separate staged-file test-routing card.

Dependencies / References

- Governing spec path: `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- Related repo guidance:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
- Related implementation paths:
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/review.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/review/run_staged_review.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/review/review_with_lmstudio.sh`
- Source artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_roadmap_fit_2026_04_25.md`

Subtasks

1. Generate Specification
   - Confirm and refine the governing specification in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` for deterministic pre-commit and staged-review summary behavior.
   - Define the exact summary contents, output rules, blocked and failure handling, skip visibility, and relationship to the authoritative artifacts.
   - Keep this as a narrow refinement of the existing governing spec path rather than creating a parallel source of truth.

2. Generate Execution Prompt
   - After the specification update is approved, prepare an execution prompt on this card that instructs implementation against `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`.
   - The execution prompt must remain on the card and must not be stored in the repo.
   - The execution prompt should require focused code, test, and documentation updates only within the pre-commit and staged-review harness scope for this one work item.

3. Implement deterministic summary legibility improvements
   - Update the pre-commit orchestration and summary surfacing flow so the run emits the approved deterministic summary without changing audit-artifact authority or fail-fast semantics.

4. Add or update verification coverage
   - Add or update focused tests or validation coverage for the summary behavior at the appropriate layer.

5. Update documentation
   - Align `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` with final implemented behavior and keep any maintained companion documentation in sync if required by the current doc workflow.

Notes / Operational Rule

- This card is limited to one primary workflow/tooling improvement.
- The specification lives in the repo at `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`.
- The execution prompt stays on the ClickUp card and is generated only after the governing specification is approved.
- Human publication or creation of the ClickUp card remains outside this workspace artifact.
