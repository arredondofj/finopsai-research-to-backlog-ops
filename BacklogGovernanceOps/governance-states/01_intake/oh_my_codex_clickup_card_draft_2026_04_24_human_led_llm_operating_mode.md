# Task Card Example

## Title

`docs: define human-led llm operating mode`

## Requirement / Problem Statement

FinOpsAI already has a strongly governed human-led development workflow, repo guidance, task-card/specification discipline, and advisory LM Studio review tooling, but it does not yet define one explicit operating-mode note for the current human-led with LLM support workflow.

This leaves a clarity gap between:
- the repo’s human-led workflow and front-door gates in `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-development-workflow.html`
- the accounting, approval, and advisory-AI boundaries in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
- the documented pre-commit and review behavior in `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
- and the process recommendation derived from the `oh_my_codex` repo assessment, workflow analysis, and FinOpsAI repo mapping

The work item is to define one explicit FinOpsAI operating-mode note for the current human-led with LLM support workflow so AI assistance fits the existing process without ambiguity about authority, approvals, or controlling artifacts.

## Expected Outcome

FinOpsAI has one documented operating-mode note that explains how human-led development with LLM support works in the current repo.

The note should make clear:
- where LLM assistance can be used in each existing workflow phase
- what remains human-authoritative
- which artifacts remain controlling
- how advisory review tooling fits the workflow
- what is out of scope for the current operating mode

## Business Context

FinOpsAI is production-oriented bookkeeping software with deterministic accounting, approval, and posting constraints. As AI assistance becomes more common in engineering work, the repo needs an explicit operating-mode note so human-led use of LLMs is consistent, auditable, and aligned with the existing engineering workflow.

## Scope

### In scope

- define one repo-local operating-mode note for the current human-led with LLM support workflow
- identify where the operating-mode note should live as the governing documentation artifact
- align the note with existing FinOpsAI workflow and repo guidance
- clarify how advisory AI assistance maps onto current development phases and approval checkpoints
- clarify what remains human-authoritative in the current operating mode
- explicitly exclude future overnight Agentic Dev policy from this task

### Out of scope

- defining the future overnight Agentic Dev operating mode
- changing customer-facing product behavior
- changing accounting rules, validation logic, posting logic, or transaction semantics
- redesigning the full product-development workflow
- changing pre-commit/test-mapping behavior directly in this card
- introducing OMX-style runtime orchestration, tmux coordination, MCP services, or persistent agent-state tooling into FinOpsAI

## Acceptance Criteria

1. One governing specification path is selected for the human-led with LLM support operating-mode note.
2. The governing specification defines:
   - purpose and intended audience
   - where LLM assistance fits within the current FinOpsAI development workflow
   - what remains human-authoritative
   - how specs, approvals, and execution prompts remain controlling artifacts
   - how advisory review tooling relates to deterministic and approval-based controls
   - explicit exclusions for future Agentic Dev policy
3. The note aligns with `/Users/Sites/Repo-FinOpsAI/AGENTS.md` and does not imply model authority over accounting state, validation, approval, posting eligibility, or review decisions.
4. The task remains documentation/process scoped and does not require Product Design work for user-facing behavior.
5. The resulting card supports a later execution prompt without inventing runtime-product requirements or future-agent autonomy rules.

## Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep the work documentation/process scoped.
- Do not merge the current human-led operating-mode note with the future Agentic Dev operating mode.
- Do not invent user-facing product behavior.
- Keep the execution prompt on the card and not in the repo.
- Subtask 2 is blocked until Subtask 1 specification is approved.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_github_repo_assessment_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_workflow_analysis_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_repo_mapping_2026_04_24.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/oh_my_codex_2026_04_24/oh_my_codex_roadmap_fit_2026_04_24.md`
- FinOpsAI repo guidance and workflow docs:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-development-workflow.html`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/git_pre_commit_implementation.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/human_led_llm_operating_mode_spec.md`
   - Define:
     - purpose and audience
     - workflow-phase mapping for LLM assistance
     - human authority boundaries
     - controlling artifacts and approvals
     - advisory-tooling boundaries
     - explicit exclusions for future Agentic Dev policy

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to produce or update the documented operating-mode note exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/human_led_llm_operating_mode_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes/creates the ClickUp card.
