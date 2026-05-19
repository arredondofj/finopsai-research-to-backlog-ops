Request Check Result: Appropriate for task-card generation

Information Check Result: Sufficient information to proceed

Additional Considerations Requiring Decision

- The staged-file routing expansion must stay deterministic and file-path-based rather than becoming a heuristic or model-driven selector.
- The change should expand focused coverage for high-risk modules without turning the pre-commit hook into a broad slow full-suite runner.
- The mapping logic and the documentation must stay aligned so developers can predict which focused test subset will run from staged paths.

Task Card Example

Title

`test: expand staged-file test routing for high-risk modules`

Requirement / Problem Statement

FinOpsAI's repo-managed pre-commit unit-test subset is currently narrower than the repository's documented verification expectations for accounting-sensitive changes. `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh` presently routes only a limited staged-file set to `tests/test_classification.py`, while repo guidance in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`, `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`, and `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` already implies a broader focused accounting-sensitive subset including normalization, classification, controller validation, and Wave-related behavior.

Expand deterministic staged-file test routing for additional high-risk FinOpsAI modules and rule files so the pre-commit harness runs the appropriate focused test subset when staged changes touch high-risk accounting and workflow areas.

Expected Outcome

The pre-commit unit-test routing becomes more complete, deterministic, and predictable for high-risk staged changes. When staged files affect the targeted high-risk modules and rule files, the hook runs the appropriate focused test subset instead of relying on the current classification-only mapping.

The resulting routing remains deterministic, scoped, and fast enough for pre-commit use.

Business Context

This is an internal engineering-quality improvement for a production-oriented bookkeeping repository. It improves local verification of accounting-sensitive changes without changing application runtime behavior, transaction semantics, or posting behavior.

Scope

In scope:
- expand staged-file-to-test mapping in the repo-managed pre-commit unit-test check for approved high-risk modules and rule files
- align the mapping with current repo guidance for focused accounting-sensitive verification
- document the updated routing behavior in the governing engineering documentation
- keep the routing deterministic and observable from the staged file set

Out of scope:
- replacing the pre-commit hook with a full-suite test runner
- changing accounting semantics, classification rules, posting behavior, or transaction validation logic
- introducing model-based or heuristic test selection
- bundling this work with the separate pre-commit or review-summary legibility card
- broad redesign of all pre-commit checks beyond the staged-file routing required for this card

Acceptance Criteria

1. `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh` routes staged changes in the approved high-risk module and rule-file set to the appropriate focused pytest subset rather than only to `tests/test_classification.py`.
2. The expanded mapping remains deterministic and based on explicit staged-path rules.
3. The expanded mapping covers the high-risk accounting and workflow areas identified by repo guidance where relevant, including the focused subset documented for normalization, classification, controller validation, and Wave-related behavior.
4. If no staged files match the approved mapping rules, the check still exits cleanly with an explicit no-op message.
5. The updated routing does not broaden into an uncontrolled full test run for unrelated staged changes.
6. `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` and aligned testing guidance are updated to reflect the implemented mapping behavior.
7. Focused verification is added or updated to verify the routing behavior itself without inventing unrelated new scope.

Constraints

- Keep the routing deterministic, local, and shell-script-compatible with the existing pre-commit harness.
- Do not add new dependencies, model calls, or external services.
- Preserve the repository's deterministic accounting, validation, approval, privacy, and posting constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep the work limited to one primary workflow/tooling improvement.
- Ensure the documentation and the implemented routing stay aligned so developers can rely on the documented behavior.

Dependencies / References

- Governing spec path: `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- Related repo guidance:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`
- Related implementation paths:
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
- Related focused tests named in repo guidance:
  - `/Users/Sites/Repo-FinOpsAI/tests/test_normalizer.py`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_classification.py`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_controller_validation.py`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_wave_service.py`
- Source artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_roadmap_fit_2026_04_25.md`

Subtasks

1. Generate Specification
   - Confirm and refine the governing specification in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` for staged-file routing across the approved high-risk module and rule-file set.
   - Define the exact staged-path mappings, the corresponding focused test subset, no-match behavior, and documentation alignment requirements.
   - Keep this as a narrow refinement of the existing governing spec path rather than creating a separate competing spec.

2. Generate Execution Prompt
   - After the specification update is approved, prepare an execution prompt on this card that instructs implementation against `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`.
   - The execution prompt must stay on the card and must not be stored in the repo.
   - The execution prompt should require focused script, test, and documentation updates only for this staged-file routing work item.

3. Implement deterministic staged-file routing expansion
   - Update the pre-commit unit-test routing logic for the approved high-risk module and rule-file set.

4. Add or update routing verification coverage
   - Add or update focused tests or harness validation to verify that the routing behavior matches the approved staged-path rules.

5. Update documentation
   - Align `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` and relevant testing guidance with the final implemented routing behavior.

Notes / Operational Rule

- This card is limited to one primary workflow/tooling improvement.
- The specification lives in the repo at `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`.
- The execution prompt stays on the ClickUp card and is generated only after the governing specification is approved.
- Human publication or creation of the ClickUp card remains outside this workspace artifact.
