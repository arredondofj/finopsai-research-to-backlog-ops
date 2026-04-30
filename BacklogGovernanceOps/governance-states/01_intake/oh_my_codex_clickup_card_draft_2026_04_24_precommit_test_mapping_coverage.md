# Task Card Example

## Title

`chore: tighten workflow-critical pre-commit test mapping coverage`

## Requirement / Problem Statement

FinOpsAI already uses repo-managed pre-commit controls and advisory LM Studio review, but the current workflow-critical test coverage enforced from pre-commit is intentionally narrow. The current `scripts/git/checks/unit_tests.sh` maps only a limited staged-change set to `tests/test_classification.py`, and the integration test hook remains unimplemented.

This creates a workflow gap between:
- the repo's strong engineering/process guidance in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
- the documented pre-commit implementation in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- the testing guidance in `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
- and the desired workflow-critical gate discipline identified in the `oh_my_codex` repo assessment, workflow analysis, and FinOpsAI repo mapping

The work item is to review the current workflow-critical pre-commit and staged test-mapping coverage, define the intended tightened coverage policy, and implement the corresponding repo-local documentation and hook-script updates in one governed task.

## Expected Outcome

FinOpsAI has one explicit, repo-local specification and implementation pass for tighter workflow-critical pre-commit test mapping coverage.

The resulting work should:
- define which staged changes must trigger focused tests for workflow-critical engineering surfaces
- keep the staged-scope, fail-fast philosophy of the current hook system unless the governing spec explicitly approves a broader rule
- align the documented pre-commit behavior, testing guidance, and hook implementation
- preserve advisory-only AI review boundaries and deterministic accounting safeguards

## Business Context

FinOpsAI is production-oriented bookkeeping software. Engineering workflow controls matter because the repo depends on deterministic accounting behavior, approval gates, and trustworthy developer workflow automation. If pre-commit coverage is too narrow for workflow-critical surfaces, repo guidance and actual enforcement can drift apart.

## Scope

### In scope

- review the current pre-commit check and staged test-mapping behavior for workflow-critical engineering surfaces
- define the target tightened coverage policy in one governing specification
- update the relevant hook/test-mapping implementation to match the approved specification
- align affected engineering documentation with the implemented behavior
- preserve the existing staged-scope orientation unless the governing specification explicitly chooses a different rule

### Out of scope

- changing product-facing bookkeeping behavior
- changing accounting rules, validation logic, posting logic, or transaction semantics
- redesigning the full pre-commit architecture
- introducing OMX-style multi-agent runtime architecture, tmux orchestration, MCP services, or persistent agent-state tooling into FinOpsAI
- broad repo-wide CI redesign beyond the one primary work item of workflow-critical pre-commit test-mapping coverage

## Acceptance Criteria

1. One governing specification path is selected for the pre-commit test-mapping coverage work item.
2. The governing specification documents:
   - the current behavior that is considered too narrow or incomplete
   - the target staged-change-to-test/check mapping policy
   - the workflow-critical surfaces covered by the change
   - explicit boundaries on what is not being broadened in this task
3. The implementation updates repo-managed pre-commit behavior only where required by the approved governing specification.
4. `scripts/git/checks/unit_tests.sh` and any other directly affected hook scripts are aligned with the approved coverage policy.
5. `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` and `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md` are updated if implementation behavior or documented expectations change.
6. The task preserves staged-scope, fail-fast hook behavior unless the approved governing specification explicitly authorizes a different rule.
7. The task does not introduce model-based authority over accounting state, validation, approval, posting eligibility, or review decisions.
8. The task remains one primary workflow/tooling item and does not expand into general CI redesign or product-development changes.

## Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep LM Studio review advisory only.
- Keep the card scoped to one primary workflow/tooling task.
- Do not broaden into product-design or runtime-architecture work.
- Do not silently widen hook behavior beyond what the governing specification approves.
- Keep the execution prompt on the card and not in the repo.
- Subtask 2 is blocked until the specification is approved.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_github_repo_assessment_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_workflow_analysis_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_repo_mapping_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_roadmap_fit_2026_04_24.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/review/run_staged_review.sh`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/precommit_test_mapping_coverage_spec.md`
   - Define:
     - current hook/test-mapping behavior
     - target tightened coverage policy
     - covered workflow-critical surfaces
     - staged-scope and fail-fast boundaries
     - affected docs/scripts to align
     - explicit exclusions to prevent scope creep

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update the approved hook/docs behavior exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/precommit_test_mapping_coverage_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes/creates the ClickUp card.
