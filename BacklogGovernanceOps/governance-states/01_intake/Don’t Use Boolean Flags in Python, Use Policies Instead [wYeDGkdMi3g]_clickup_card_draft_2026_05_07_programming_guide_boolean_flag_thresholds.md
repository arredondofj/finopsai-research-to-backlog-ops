# Task Card Example

## Title

`docs: clarify boolean-flag refactor thresholds`

## Requirement / Problem Statement

This research run found one bounded, defensible use for the transcript `Don’t Use Boolean Flags in Python, Use Policies Instead`: clarify repo-local programming guidance for when boolean control parameters, growing condition trees, and rule-heavy functions should trigger refactor review instead of accumulating more branching logic.

The current FinOpsAI evidence available in this environment is intentionally limited. The target checkout exposed only:

- `/Users/Dev/Prototypes/FinOpsAI/docs/engineering/clickup_sprint_kanban_title_guide.md`

No repo-local `AGENTS.md`, code, tests, or pre-commit hook scripts were available in the target checkout used for this assessment. Because of that evidence constraint, this work item must stay documentation- and process-scoped. It should define review thresholds and guidance language, not invent code-level fixes or automation requirements that the available repo evidence cannot support.

The work item is to define one explicit programming-guide addition or revision that explains:

- when boolean flags are acceptable
- when they become a maintainability smell
- when branch growth should trigger rule extraction or refactor review
- and how to document exceptions so simple code is not over-engineered

## Expected Outcome

FinOpsAI has one explicit, repo-local programming-guidance update for boolean flags, rule extraction thresholds, and branch-growth review expectations.

The resulting work should:

- define a threshold-based guidance rule rather than an absolute ban
- explain when a boolean parameter or growing conditional tree should trigger refactor consideration
- clarify that explicit rule units or extracted logic are options, not mandatory patterns in every case
- provide exception guidance for small, simple, or clearly bounded code
- preserve the scope as an internal documentation/process task only

## Business Context

The user interest for this run is improving programming-guide markdown so it better supports solid code development and pre-commit-quality review behavior. The transcript is useful for that because it gives a concrete maintainability heuristic: repeated branching and boolean controls often indicate missing abstraction boundaries.

For FinOpsAI, the strongest safe application of that idea is documentation and reviewer guidance. The available repo evidence in this environment is not strong enough to justify code refactor claims or automation-heavy enforcement, so the value here is a clearer internal standard that can later guide implementation and review decisions.

## Scope

### In scope

- define repo-local programming guidance for boolean flags and branch-growth thresholds
- explain what kinds of boolean controls are acceptable versus suspicious
- define when reviewers should ask for rule extraction, clearer naming, or refactor consideration
- define how exceptions should be documented so the guidance does not become a blanket anti-pattern rule
- update directly affected guidance docs if needed so the new rule is explicit and self-consistent

### Out of scope

- refactoring product code in this task
- introducing lint rules, static analysis, or pre-commit automation in this task
- proving specific code violations in the FinOpsAI codebase
- broad repo-wide migration to policy pipelines or registries
- user-facing product behavior changes
- new dependencies, external services, runtime AI behavior, or workflow-architecture redesign

## Acceptance Criteria

1. One governing specification path is selected for this programming-guidance work item.
2. The governing specification documents:
   - what boolean flags or boolean control parameters mean in scope for this guidance
   - when they are acceptable
   - when they should trigger maintainability review or refactor consideration
   - how branch-heavy rule growth should be evaluated
   - examples of acceptable exceptions and explicit exclusions
3. The resulting documentation stays threshold-based and does not impose an absolute "never use booleans" rule.
4. Any directly affected repo-local guidance docs are updated so the new rule does not conflict with existing engineering-writing conventions.
5. The task remains one documentation/process work item and does not expand into code refactors, automated checks, or product behavior change.
6. The resulting card supports later execution without inventing code-level violations that were not evidenced in this run.

## Constraints

- Keep the work strictly documentation/process-scoped.
- Do not claim that specific FinOpsAI code currently violates the guidance unless later execution has stronger repo evidence.
- Do not convert the transcript into a blanket policy-pattern mandate.
- Keep the guidance threshold-based, exception-aware, and maintainability-focused.
- Keep the execution prompt on the card and not in the repo.
- Subtask 2 is blocked until the specification is approved.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_2026_05_07/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_analysis_2026_05_07.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_2026_05_07/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_repo_mapping_2026_05_07.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_2026_05_07/Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]_roadmap_fit_2026_05_07.md`
- FinOpsAI evidence available in this environment:
  - `/Users/Dev/Prototypes/FinOpsAI/docs/engineering/clickup_sprint_kanban_title_guide.md`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Dev/Prototypes/FinOpsAI/docs/product_specifications/engineering_workflow/programming_guidance_boolean_flag_thresholds_spec.md`
   - Define:
     - acceptable uses of boolean control parameters
     - review thresholds for branch growth and rule concentration
     - when refactor consideration should be triggered
     - examples and exception patterns
     - explicit exclusions to prevent scope creep
     - which guidance docs should be aligned

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update the approved documentation exactly against:
     `/Users/Dev/Prototypes/FinOpsAI/docs/product_specifications/engineering_workflow/programming_guidance_boolean_flag_thresholds_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
