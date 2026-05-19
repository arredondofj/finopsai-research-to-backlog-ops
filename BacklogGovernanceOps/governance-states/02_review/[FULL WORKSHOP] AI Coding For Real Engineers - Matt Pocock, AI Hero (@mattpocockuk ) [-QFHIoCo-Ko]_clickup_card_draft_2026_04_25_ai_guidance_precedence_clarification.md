# Task Card Example

## Title

`docs: define AI engineering guidance precedence`

## Requirement / Problem Statement

FinOpsAI already uses several durable control surfaces for AI-assisted engineering work, including the root `AGENTS.md`, engineering workflow documents, task-card generation guidance, and repo-managed hook and review scripts. The transcript analysis, workflow analysis, repo mapping, and roadmap-fit review for this run identified a workflow risk: when multiple guidance surfaces exist, the repo needs a clearer rule for where AI-engineering instructions belong, how they interact, and which source takes precedence when those surfaces overlap.

This creates a workflow ambiguity between:

- the root AI-engineering constraints in `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
- the phase and artifact controls in `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-development-workflow.html`
- the task-card and prompt-gate controls in `/Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md`
- the engineering and testing guidance in `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md` and `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
- and the repo-managed hook and review behavior in `scripts/git/`

The work item is to define one explicit repo-local guidance-precedence rule for AI-assisted engineering work so humans and agent-assisted workflows can tell which instruction surface governs which kind of behavior, and how to avoid overlapping or contradictory guidance.

## Expected Outcome

FinOpsAI has one explicit, repo-local specification and documentation pass that defines guidance precedence for AI-assisted engineering work.

The resulting work should:

- define the intended responsibility of each major guidance surface
- define which surface governs when overlap exists
- reduce ambiguity between repo-level AI instructions, workflow docs, and review/tooling surfaces
- preserve deterministic accounting, staged review, and human-approval boundaries
- avoid broadening the task into runtime AI behavior, product behavior, or workflow-architecture redesign

## Business Context

FinOpsAI is production-oriented bookkeeping software, and its development workflow is part of the safety boundary. If guidance precedence is unclear, AI-assisted work can follow the wrong instruction source or combine sources inconsistently. That weakens the repo’s control model even if the individual guidance documents are good.

## Scope

### Included

- define a repo-local precedence model for AI-assisted engineering guidance
- identify the key instruction surfaces that currently affect AI-assisted development behavior
- document the intended responsibility and boundary of each relevant surface
- define how conflicts or overlaps should be resolved
- update the affected guidance docs if required so the documented precedence is explicit and consistent

### Excluded

- changing runtime bookkeeping behavior
- changing accounting rules, validation rules, posting logic, or transaction semantics
- redesigning the entire engineering workflow
- creating a new autonomous-agent runtime or review architecture
- introducing new dependencies, external services, model-serving, MCP, or runtime AI authority
- broad prompt-library design beyond the one primary work item of repo-guidance precedence

## Acceptance Criteria

1. One governing specification path is selected for the AI-engineering guidance-precedence work item.
2. The governing specification documents:
   - the current instruction surfaces relevant to AI-assisted engineering work
   - the intended role of each surface
   - the precedence or conflict-resolution rule when surfaces overlap
   - explicit examples of which surface should govern which class of instruction
   - clear boundaries on what this task does not change
3. The resulting documentation clarifies how `AGENTS.md`, workflow docs, task-card guidance, and review/tooling guidance should interact.
4. Any directly affected repo-local guidance docs are updated so they do not contradict the approved precedence model.
5. The task preserves deterministic accounting, validation, approval, posting, privacy, dependency, and advisory-review constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
6. The task remains one documentation/process work item and does not expand into runtime-product, architecture, or CI redesign work.
7. The resulting card supports later execution without inventing customer-facing or accounting-policy requirements.

## Constraints

- Preserve deterministic accounting, validation, approval, posting, credential, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep advisory review advisory only.
- Keep the work scoped to one primary documentation/process task.
- Do not broaden into runtime architecture or product-design work.
- Do not invent new AI operating modes beyond clarifying current guidance precedence.
- Keep the execution prompt on the card and not in the repo.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_workflow_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_2026_04_25/[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero (@mattpocockuk ) [-QFHIoCo-Ko]_roadmap_fit_2026_04_25.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-development-workflow.html`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/programming_guidance.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/engineering/testing.md`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/pre_commit.sh`
  - `/Users/Sites/Repo-FinOpsAI/scripts/git/review/run_staged_review.sh`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/ai_engineering_guidance_precedence_spec.md`
   - Define:
     - current instruction surfaces
     - intended role of each surface
     - precedence and conflict-resolution rules
     - examples of which surface governs which class of instruction
     - affected docs to align
     - explicit exclusions to prevent scope creep

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update the approved guidance and docs behavior exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/engineering_workflow/ai_engineering_guidance_precedence_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
