# Task Card Example

## Title

`chore: tighten high-risk pre-commit test routing`

## Requirement / Problem Statement

FinOpsAI already uses repo-managed pre-commit controls, staged-scope LM Studio review, and explicit engineering workflow guidance, but the current workflow-critical unit-test routing enforced from pre-commit is intentionally narrow. `docs/engineering/testing.md` states that the current pre-commit unit-test hook maps only a small classification-related subset, and `scripts/git/checks/unit_tests.sh` currently routes only limited staged changes to `tests/test_classification.py`.

This creates a workflow gap between:
- the repo's deterministic accounting and workflow-control expectations in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
- the documented pre-commit implementation in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- the testing guidance in `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
- and the desired workflow-critical gate discipline identified in the transcript analysis, workflow analysis, FinOpsAI repo mapping, and roadmap-fit record for this run

The work item is to review the current staged test-routing behavior for high-risk engineering surfaces, define the intended tightened coverage policy, and implement the corresponding repo-local specification, hook-script, and documentation updates in one governed task.

## Expected Outcome

FinOpsAI has one explicit, repo-local specification and implementation pass for tighter staged pre-commit test routing on high-risk workflow-critical changes.

The resulting work should:
- define which staged changes must trigger focused tests for high-risk workflow-critical engineering surfaces
- preserve staged-scope and fail-fast behavior unless the governing specification explicitly approves a narrower or broader rule
- align `scripts/git/checks/unit_tests.sh`, related hook behavior, and the affected engineering docs
- keep advisory-only AI review boundaries intact
- avoid widening the task into full CI redesign or runtime-product changes

## Business Context

FinOpsAI is production-oriented bookkeeping software. Its engineering workflow is part of the control surface for deterministic accounting behavior, validation, approval, and posting safety. If pre-commit test routing is too narrow for high-risk staged changes, the repo's documented workflow discipline and its actual enforcement can drift apart.

## Scope

### In scope

- review the current staged-change-to-test routing behavior for workflow-critical high-risk engineering surfaces
- define the intended tightened routing policy in one governing specification
- update `scripts/git/checks/unit_tests.sh` and any directly affected repo-managed hook behavior required by the approved specification
- update the relevant engineering docs so documented expectations match implemented behavior
- explicitly identify which high-risk change classes must trigger focused tests in this task

### Out of scope

- changing product-facing bookkeeping behavior
- changing transaction semantics, validation rules, posting rules, or accounting-state decisions
- redesigning the full pre-commit architecture
- implementing broad CI or integration-test strategy changes outside this one primary task
- introducing new dependencies, external services, model-serving, MCP, RAG, or runtime AI authority
- revising LM Studio review scope beyond what is required to document or preserve current advisory boundaries

## Acceptance Criteria

1. One governing specification path is selected for the high-risk staged test-routing work item.
2. The governing specification documents:
   - the current staged test-routing behavior
   - the workflow gap or inadequacy being addressed
   - the target high-risk staged-change routing policy
   - the exact workflow-critical surfaces covered by this task
   - explicit boundaries on what is not being broadened in this work item
3. The implementation updates repo-managed pre-commit behavior only where required by the approved governing specification.
4. `scripts/git/checks/unit_tests.sh` and any directly affected hook behavior are aligned with the approved routing policy.
5. `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md` and `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md` are updated if implemented behavior or documented expectations change.
6. The task preserves deterministic accounting, validation, approval, posting, privacy, and advisory-review constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
7. The task remains one primary workflow/tooling item and does not expand into general CI redesign, runtime architecture work, or product behavior change.
8. The resulting card supports later execution without inventing customer-facing or accounting-policy requirements.

## Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep LM Studio review advisory only.
- Keep the work scoped to one primary workflow/tooling task.
- Do not broaden into product-design or runtime-architecture work.
- Do not silently widen staged hook behavior beyond what the governing specification approves.
- Keep the execution prompt on the card and not in the repo.
- Subtask 2 is blocked until the specification is approved.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_2026_04_25/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_2026_04_25/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_workflow_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_2026_04_25/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_2026_04_25/AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]_roadmap_fit_2026_04_25.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/review/run_staged_review.sh`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/high_risk_precommit_test_routing_spec.md`
   - Define:
     - current staged test-routing behavior
     - target tightened routing policy
     - the high-risk change classes covered in this task
     - staged-scope and fail-fast boundaries
     - affected hook/docs surfaces to align
     - explicit exclusions to prevent scope creep

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update the approved hook/docs behavior exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/high_risk_precommit_test_routing_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes/creates the ClickUp card.
