# Task Card Example

## Title

`docs: define architecture review guidance surface`

## Requirement / Problem Statement

This research run established one narrow, defensible use for the transcript `Why Senior Devs Keep Shipping Slow (And How to Stop)`: create a durable FinOpsAI documentation/workflow surface where architecture-restraint guardrails can live and be reused during engineering review.

The repo-mapping result matters here because it found a concrete evidence gap in the currently available target checkout at `/Users/Dev/Prototypes/FinOpsAI`:

- no visible repo-local `AGENTS.md`
- no visible programming-guidance document
- no visible architecture-review workflow document
- only one visible engineering workflow doc:
  `/Users/Dev/Prototypes/FinOpsAI/docs/engineering/clickup_sprint_kanban_title_guide.md`

That existing guide is about ClickUp title formatting and one-card task scope. It is not an appropriate surface for architecture-review guardrails. The work item is therefore to define one dedicated architecture-review guidance surface for FinOpsAI and specify how it should relate to existing workflow docs without mixing unrelated concerns.

## Expected Outcome

FinOpsAI has one defined documentation surface for architecture-review guidance that can later hold:

- simplicity-first architecture guardrails
- prompts for reviewing complexity-bearing changes
- scope boundaries distinguishing architecture review from task-card naming or other engineering workflow docs
- reuse guidance for both human-led and AI-assisted planning/review work

The resulting work should make clear where this guidance belongs, what it is for, and what it does not replace.

## Business Context

The user interest in this run is improving durable engineering guidance and workflow control so solid code is developed under clearer expectations. The transcript is useful only at that level. It supports architectural restraint and explicit review prompts, but it does not justify code refactors, hard automation, or broad architecture changes by itself.

The Phase 2 mapping sharpened that conclusion: the immediate gap is not product behavior or implementation detail. The immediate gap is the absence of a visible architecture-review guidance surface in the available repo snapshot. Defining that surface is the smallest reusable workflow step that preserves the assessment findings instead of losing them in chat.

## Scope

### In scope

- define one dedicated FinOpsAI architecture-review guidance surface
- select the governing specification path for that surface
- define the intended audience and operational purpose of the guidance surface
- define how the new surface should relate to the existing ClickUp title guide and any future engineering/programming guidance docs
- define the categories of guardrails and review prompts the surface is expected to hold
- keep the work documentation/process scoped

### Out of scope

- writing product code in this task
- claiming current code violations in FinOpsAI
- adding automated enforcement, linting, or pre-commit checks in this task
- mixing the architecture-review guidance into `clickup_sprint_kanban_title_guide.md`
- user-facing product behavior changes
- new dependencies, external services, or runtime architecture changes

## Acceptance Criteria

1. One governing specification path is selected for the architecture-review guidance surface.
2. The governing specification defines:
   - the purpose of the guidance surface
   - the intended audience
   - how it differs from task-card naming guidance and other workflow docs
   - what categories of architecture guardrails and review prompts belong there
   - how the surface should be reused during engineering review or planning
   - explicit exclusions so the work does not expand into code changes or automation
3. The specification records the evidence constraint that the available repo snapshot contained no visible `AGENTS.md`, programming-guidance doc, or architecture-review workflow doc.
4. The resulting work remains one documentation/process item and does not invent code-level fixes or repo violations.
5. The resulting card supports later execution against the approved specification without requiring Product Design work.

## Constraints

- Keep the work strictly documentation/process scoped.
- Preserve the assessment finding that the current visible repo snapshot is evidence-limited.
- Do not treat the transcript as sufficient evidence for code-level enforcement or implementation work.
- Do not place the new guardrails inside `docs/engineering/clickup_sprint_kanban_title_guide.md`.
- Keep the execution prompt on the card and not in the repo.
- Subtask 2 is blocked until Subtask 1 specification is approved.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_2026_05_07/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_analysis_2026_05_07.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_2026_05_07/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_workflow_analysis_2026_05_07.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_2026_05_07/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_repo_mapping_2026_05_07.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_2026_05_07/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_roadmap_fit_2026_05_07.md`
- FinOpsAI evidence available in this environment:
  - `/Users/Dev/Prototypes/FinOpsAI/docs/engineering/clickup_sprint_kanban_title_guide.md`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Dev/Prototypes/FinOpsAI/docs/product_specifications/engineering_workflow/architecture_review_guidance_surface_spec.md`
   - Define:
     - purpose and audience
     - intended workflow role
     - relationship to existing ClickUp workflow guidance
     - categories of architecture guardrails and review prompts
     - explicit exclusions and evidence limits

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to create or update the approved guidance surface exactly against:
     `/Users/Dev/Prototypes/FinOpsAI/docs/product_specifications/engineering_workflow/architecture_review_guidance_surface_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
