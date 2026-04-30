# Task Card Example

## Title

`chore: tighten high-risk staged test routing`

## Requirement / Problem Statement

FinOpsAI already uses repo-managed pre-commit controls, staged-scope advisory review, and explicit engineering workflow guidance, but the current workflow-critical unit-test routing enforced from pre-commit is intentionally narrow. `docs/engineering/testing.md` states that the current pre-commit unit-test hook maps only classification-related staged changes to `tests/test_classification.py`, and `scripts/git/checks/unit_tests.sh` currently routes only a small staged-file subset to that test.

This creates a workflow gap between:

- the repo's deterministic-accounting and workflow-control expectations in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
- the documented pre-commit implementation in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- the testing guidance in `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
- and the workflow conclusion from this research run that feedback loops are the ceiling on safe AI-assisted implementation quality

The work item is to review the current staged test-routing behavior for high-risk workflow-critical engineering surfaces, define the intended tightened coverage policy, and implement the corresponding repo-local specification, hook-script, and documentation updates in one governed task.

## Expected Outcome

FinOpsAI has one explicit, repo-local specification and implementation pass for tighter staged pre-commit unit-test routing on high-risk workflow-critical changes.

The resulting work should:

- define which staged changes must trigger focused tests for high-risk workflow-critical engineering surfaces
- preserve staged-scope and fail-fast behavior unless the governing specification explicitly approves a narrower or broader rule
- align `scripts/git/checks/unit_tests.sh`, related hook behavior, and affected engineering docs
- keep advisory-only AI review boundaries intact
- avoid widening the task into full CI redesign, runtime-product changes, or broad architecture work

## Business Context

FinOpsAI is production-oriented bookkeeping software. Its engineering workflow is part of the control surface protecting deterministic accounting behavior, validation, approval, and posting safety. If pre-commit test routing is too narrow for high-risk staged changes, the repo's documented workflow discipline and actual enforcement can drift apart, especially when AI-assisted implementation increases change throughput.

## Scope

### Included

- review the current staged-change-to-test routing behavior for workflow-critical high-risk engineering surfaces
- define the intended tightened routing policy in one governing specification
- update `scripts/git/checks/unit_tests.sh` and any directly affected repo-managed hook behavior required by the approved specification
- update the relevant engineering docs so documented expectations match implemented behavior
- explicitly identify which high-risk change classes must trigger focused tests in this task

### Excluded

- changing product-facing bookkeeping behavior
- changing transaction semantics, validation rules, posting rules, or accounting-state decisions
- redesigning the full pre-commit architecture
- implementing broad CI or integration-test strategy changes outside this one primary task
- introducing new dependencies, external services, model-serving, MCP, RAG, or runtime AI authority
- revising advisory review scope beyond what is required to document or preserve current boundaries

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
6. The task preserves deterministic accounting, validation, approval, posting, privacy, dependency, and advisory-review constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
7. The task remains one primary workflow/tooling item and does not expand into general CI redesign, runtime architecture work, or product behavior change.
8. The resulting card supports later execution without inventing customer-facing or accounting-policy requirements.

## Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep advisory review advisory only.
- Keep the work scoped to one primary workflow/tooling task.
- Do not broaden into product-design or runtime-architecture work.
- Do not silently widen staged hook behavior beyond what the governing specification approves.
- Keep the execution prompt on the card and not in the repo.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_workflow_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_roadmap_fit_2026_04_25.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/checks/unit_tests.sh`

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

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
