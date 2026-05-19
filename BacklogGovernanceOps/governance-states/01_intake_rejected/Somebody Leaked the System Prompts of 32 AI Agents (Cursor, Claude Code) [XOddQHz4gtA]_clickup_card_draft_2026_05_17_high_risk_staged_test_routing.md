Request Check Result: Appropriate for task-card generation

Information Check Result: Sufficient information to proceed

## Task Card Example

### Title

`chore: tighten high-risk staged test routing`

### Requirement / Problem Statement

FinOpsAI already uses repo-managed pre-commit controls, staged-scope review, and explicit engineering workflow guidance, but the current pre-commit unit-test routing for staged changes is intentionally narrow. `docs/engineering/standards/testing.md` states that the current hook maps only classification-related staged changes to `tests/test_classification.py`, and `scripts/git/checks/unit_tests.sh` currently routes only a small staged-file subset to that test.

This creates a workflow-control gap between:

- the repo's deterministic-accounting and workflow-control expectations in `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`
- the documented pre-commit implementation in `/Users/Dev/Apps/finopsai-desktop/docs/engineering/git/git_pre_commit_implementation.md`
- the testing guidance in `/Users/Dev/Apps/finopsai-desktop/docs/engineering/standards/testing.md`
- and the combined research conclusion from this run that workflow-critical control surfaces need stronger, explicit verification boundaries

The work item is to review the current staged test-routing behavior for high-risk workflow-critical engineering surfaces, define the intended tightened coverage policy, and align the corresponding repo-local spec, hook behavior, and affected docs in one governed task.

### Expected Outcome

FinOpsAI has one approved repo-local specification and one aligned implementation pass for tighter staged pre-commit unit-test routing on high-risk workflow-critical changes.

The resulting work should:

- define which staged changes must trigger focused tests for high-risk workflow-critical engineering surfaces
- preserve staged-scope and fail-fast behavior unless the approved specification explicitly narrows or broadens that rule
- align `scripts/git/checks/unit_tests.sh`, any directly affected pre-commit behavior, and the relevant engineering docs
- keep advisory-only LM Studio review boundaries intact
- avoid widening the task into full CI redesign, runtime-product changes, or general architecture work

### Business Context

FinOpsAI is production-oriented bookkeeping software. Its engineering workflow is part of the control surface protecting deterministic accounting behavior, validation, approval, and posting safety. If pre-commit test routing is too narrow for high-risk staged changes, the repo's documented workflow discipline and actual enforcement can drift apart, especially when AI-assisted implementation increases change throughput.

### Scope

#### Included

- review the current staged-change-to-test routing behavior for workflow-critical high-risk engineering surfaces
- define the intended tightened routing policy in one governing specification
- update `scripts/git/checks/unit_tests.sh` and any directly affected repo-managed hook behavior required by the approved specification
- update the relevant engineering docs so documented expectations match implemented behavior
- explicitly identify which high-risk change classes must trigger focused tests in this task

#### Excluded

- changing product-facing bookkeeping behavior
- changing transaction semantics, validation rules, posting rules, or accounting-state decisions
- redesigning the full pre-commit architecture
- implementing broad CI or integration-test strategy changes outside this one primary task
- introducing new dependencies, external services, model-serving, MCP, RAG, or runtime AI authority
- revising advisory-review scope beyond what is required to document or preserve current boundaries

### Acceptance Criteria

1. One governing specification path is selected for the high-risk staged test-routing work item.
2. The governing specification documents:
   - the current staged test-routing behavior
   - the workflow gap being addressed
   - the target high-risk staged-change routing policy
   - the exact workflow-critical surfaces covered by this task
   - explicit boundaries on what is not being broadened in this work item
3. The implementation updates repo-managed pre-commit behavior only where required by the approved governing specification.
4. `scripts/git/checks/unit_tests.sh` and any directly affected hook behavior are aligned with the approved routing policy.
5. `/Users/Dev/Apps/finopsai-desktop/docs/engineering/standards/testing.md` and `/Users/Dev/Apps/finopsai-desktop/docs/engineering/git/git_pre_commit_implementation.md` are updated if implemented behavior or documented expectations change.
6. The task preserves deterministic accounting, validation, approval, posting, privacy, dependency, and advisory-review constraints from `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`.
7. The task remains one primary workflow/tooling item and does not expand into general CI redesign, runtime architecture work, or product behavior change.
8. The resulting card supports later execution without inventing customer-facing or accounting-policy requirements.

### Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`.
- Keep advisory review advisory only.
- Keep the work scoped to one primary workflow/tooling task.
- Do not broaden into product-design or runtime-architecture work.
- Do not silently widen staged hook behavior beyond what the governing specification approves.
- Keep the execution prompt on the card and not in the repo.

### Dependencies / References

- Research workspace artifacts:
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_analysis_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_github_repo_assessment_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_workflow_analysis_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_repo_mapping_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_roadmap_fit_2026_05_17.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`
  - `/Users/Dev/Apps/finopsai-desktop/docs/engineering/standards/testing.md`
  - `/Users/Dev/Apps/finopsai-desktop/docs/engineering/git/git_pre_commit_implementation.md`
  - `/Users/Dev/Apps/finopsai-desktop/docs/engineering/standards/programming_guidance.md`
  - `/Users/Dev/Apps/finopsai-desktop/scripts/git/pre_commit.sh`
  - `/Users/Dev/Apps/finopsai-desktop/scripts/git/checks/unit_tests.sh`

### Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Dev/Apps/finopsai-desktop/docs/product_specifications/high_risk_precommit_test_routing_spec.md`
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
     `/Users/Dev/Apps/finopsai-desktop/docs/product_specifications/high_risk_precommit_test_routing_spec.md`
   - Do not store the execution prompt in the repo.

### Notes / Operational Rule

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- The execution prompt stays on the card and is not stored in the repo.
