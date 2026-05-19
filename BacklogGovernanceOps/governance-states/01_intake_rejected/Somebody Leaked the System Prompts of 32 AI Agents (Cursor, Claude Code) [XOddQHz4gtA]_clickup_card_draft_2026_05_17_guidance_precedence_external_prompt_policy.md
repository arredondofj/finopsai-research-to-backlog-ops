Request Check Result: Appropriate for task-card generation

Information Check Result: Sufficient information to proceed

## Additional Considerations Requiring Decision

- The work should define one authoritative policy surface first, then add only minimal cross-references in related workflow and repo-local guidance. It should not create parallel policy sources.
- The task should stay documentation/process only. If implementation pressure appears for enforcement tooling, prompt injection changes, or broader harness restructuring, that work must be deferred into a separate later decision.

## Task Card Example

### Title

`docs: clarify AI guidance precedence and external prompt-source policy`

### Requirement / Problem Statement

FinOpsAI and the surrounding workflow harness already have multiple durable authority surfaces that shape AI-assisted engineering behavior, including workspace `AGENTS.md` files, canonical OpsControl workflow docs, workflow-ops control documents, FinOpsAI repo-local guidance, and task-specific approved artifacts. The bounded follow-on assessment for this source concluded that the harness can already support a clear policy without structural re-engineering, but that the precedence model and the external prompt-source boundary remain implied across several surfaces instead of being stated plainly in one short durable policy path.

This creates a governance and comprehension gap:

- operators and agents may not be able to quickly tell which instruction surface wins when guidance overlaps
- external prompt corpora or leaked prompt research could influence local workflow behavior informally without an explicit research-versus-adoption boundary
- authority notes may be duplicated or interpreted inconsistently across canonical workflow docs and repo-local engineering guidance

The work item is to define one bounded documentation/process clarification that makes AI-assisted engineering guidance precedence explicit and formalizes the default handling rule for external prompt sources.

### Expected Outcome

FinOpsAI has one approved governing specification that defines:

- the precedence order for AI-assisted engineering guidance across canonical workflow and repo-local guidance surfaces
- the default rule that external prompt corpora are research input only unless separately translated, reviewed, and adopted through local policy
- the minimum set of workflow and repo-local doc updates required so the policy is discoverable without creating competing authorities

The resulting work should:

- create one governing specification path for this policy clarification
- state which surfaces are authoritative, supporting, transitional, or task-local for this context
- preserve the existing research-versus-implementation, advisory-versus-deterministic, and publication-versus-intake boundaries already present in the harness
- avoid turning this docs/process clarification into tooling, runtime, governance-state, or accounting behavior change

### Business Context

FinOpsAI operates in a workflow environment where AI-assisted engineering guidance matters, but deterministic accounting, validation, review, and posting constraints still remain non-negotiable. If precedence across guidance surfaces stays implicit, teams can misread which rules govern AI-assisted work, and external prompt research can accumulate soft authority without explicit review. The clarification work is intended to reduce that ambiguity before it turns into a larger workflow-control or maintenance problem.

### Scope

#### Included

- define the precedence order for AI-assisted engineering guidance across the relevant durable surfaces
- define the default handling rule for external prompt corpora and other comparative prompt-source material
- define the research-versus-adoption boundary for external prompt-derived ideas
- select and use one governing specification path for this policy clarification
- update only the directly affected workflow and repo-local guidance surfaces needed to make the policy discoverable and non-conflicting

#### Excluded

- workflow harness re-engineering
- new enforcement tooling, linting, or runtime policy validation
- prompt injection architecture changes
- changes to Backlog Governance mechanics or ClickUp publication behavior
- changes to deterministic accounting, validation, approval, posting, or product-runtime AI behavior
- broad cleanup or rewrite of unrelated workflow docs

### Acceptance Criteria

1. One governing specification path is selected for the policy clarification work item.
2. The governing specification documents:
   - the current authority surfaces relevant to AI-assisted engineering guidance
   - the precedence order among those surfaces
   - the default handling rule for external prompt corpora and similar external prompt-source material
   - the research-versus-adoption boundary
   - the minimum direct cross-reference updates required in adjacent durable guidance surfaces
   - explicit exclusions preventing the task from widening into tooling or harness redesign
3. The implementation updates only documentation/process surfaces required by the approved specification.
4. The resulting documentation makes clear that external prompt-derived ideas do not become local workflow authority without translation into repo-local policy language and normal review.
5. The task preserves existing deterministic-accounting, review, approval, posting, privacy, and advisory-tooling constraints from `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`.
6. The task remains one primary `docs` item and does not widen into architecture design, tooling enforcement, or multiple competing policy documents.
7. The resulting card supports later execution without inventing code-level behavior, runtime AI authority, or process changes outside the approved scope.

### Constraints

- Keep the work documentation/process only.
- Keep one primary work item only.
- Use one governing specification path and avoid parallel sources of truth.
- Preserve the canonical operator-doc authority model already defined in OpsControl.
- Preserve FinOpsAI repo-local deterministic accounting and advisory-tooling constraints.
- Do not let external prompt research become implied implementation authority.
- Keep the execution prompt on the card and not in the repo.

### Dependencies / References

- Research workspace artifacts:
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_workflow_analysis_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_repo_mapping_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_workflow_applicability_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_process_decision_note_2026_05_17.md`
  - `/Users/Dev/Ops/finopsai-research-to-backlog-ops/ResearchToBacklogOps/output/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_2026_05_17/Somebody Leaked the System Prompts of 32 AI Agents (Cursor, Claude Code) [XOddQHz4gtA]_roadmap_fit_2026_05_17.md`
- OpsControl authority surfaces:
  - `/Users/Dev/Apps/finopsai-opscontrol/AGENTS.md`
  - `/Users/Dev/Apps/finopsai-opscontrol/docs/workflows/README.md`
  - `/Users/Dev/Apps/finopsai-opscontrol/docs/workflows/research-to-backlog.html`
- FinOpsAI repo guidance surfaces:
  - `/Users/Dev/Apps/finopsai-desktop/AGENTS.md`
  - `/Users/Dev/Apps/finopsai-desktop/docs/engineering/standards/programming_guidance.md`
  - `/Users/Dev/Apps/finopsai-desktop/docs/engineering/git/git_pre_commit_implementation.md`

### Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Dev/Apps/finopsai-desktop/docs/product_specifications/ai_guidance_precedence_external_prompt_policy_spec.md`
   - Define:
     - the relevant authority surfaces
     - the precedence order among them
     - the default external prompt-source handling rule
     - the research-versus-adoption boundary
     - the minimum direct cross-reference surfaces to update
     - explicit exclusions preventing tooling or architecture scope creep

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update only the approved documentation/process surfaces exactly against:
     `/Users/Dev/Apps/finopsai-desktop/docs/product_specifications/ai_guidance_precedence_external_prompt_policy_spec.md`
   - Do not store the execution prompt in the repo.

### Notes / Operational Rule

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- The execution prompt stays on the card and is not stored in the repo.
