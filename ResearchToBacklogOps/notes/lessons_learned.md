# Lessons Learned

This file stores durable workflow-harness lessons learned from real runs.

Purpose:
- preserve a concise memory of failures, friction points, and essential fixes,
- record what changed and why,
- make future harness design and workflow updates more evidence-based,
- and avoid rediscovering the same process problems in later runs.

Use this file for essential lessons only. Do not log every minor preference,
style tweak, or one-off annoyance.

## Format Choice

This register uses Markdown instead of JSON.

Reason:
- the entries are meant for human review, synthesis, and future workflow design,
- lessons often include narrative context, judgment, and cross-file reasoning,
- and the workspace already uses Markdown for durable notes and reports.

If machine querying becomes important later, a JSON export can be derived from
this file. The source of truth should remain the human-readable register unless
automation needs clearly justify a structured data store.

## Entry Structure

Each lesson should use this structure:

### `<lesson_id>` - `<short title>`

- Date:
- Run:
- Lane:
- Phase / Step:
- Category:
- Severity:
- Status:
- Issue:
- Impact:
- Likely Cause:
- Decision / Resolution:
- Instruction or Process Change:
- Impacted Files:
- Verification:
- Reuse Guidance:

### Field Guidance

- `lesson_id`:
  Use a stable identifier such as `LL-2026-04-24-01`.
- `Date`:
  Date the lesson was recorded, not necessarily the source-run date.
- `Run`:
  The run identifier or source name, ideally with video ID or unique suffix.
- `Lane`:
  Example: `YouTube Transcript`, `Accounting Domain Review`, `GitHub Repo Assessment`.
- `Phase / Step`:
  The workflow location where the issue appeared.
- `Category`:
  Use a short controlled label when possible, such as:
  `verification`, `catalog`, `routing`, `artifact naming`, `approval gate`,
  `repo mapping`, `evidence discipline`, `tooling`, `instruction design`.
- `Severity`:
  Use `low`, `medium`, or `high` based on workflow risk, not annoyance.
- `Status`:
  Use `open`, `mitigated`, `closed`, or `superseded`.
- `Issue`:
  One clear statement of the problem.
- `Impact`:
  What went wrong or what risk was introduced.
- `Likely Cause`:
  Best root-cause assessment, not blame.
- `Decision / Resolution`:
  What was decided or fixed in response.
- `Instruction or Process Change`:
  The concrete change to guidance, sequence, or behavior.
- `Impacted Files`:
  List the markdown instructions, notes, or artifacts affected.
- `Verification`:
  How the fix or lesson was confirmed.
- `Reuse Guidance`:
  What future harnesses should copy, preserve, or avoid.

## Logging Rules

- Record only essential lessons with clear reuse value.
- Prefer one entry per distinct issue.
- Update an existing entry when the same issue recurs, unless the recurrence
  reveals a materially different root cause.
- Keep entries concise but specific enough to drive instruction updates.
- Prefer process-level lessons over run-specific storytelling.
- When a lesson results in a doc patch, name the patched files explicitly.
- If a lesson is later replaced by a better control, mark the old entry
  `superseded` rather than deleting it.

## Review Heuristic

Add a lesson when at least one of these is true:
- the same class of issue occurred more than once,
- the issue caused durable artifact inaccuracies,
- the issue required a workflow-doc patch,
- the issue could misroute later phases or approvals,
- or the lesson has clear value for future workflow harness design.

---

### LL-2026-04-24-01 - Verification Metadata Was Entered Before Measurement

- Date: 2026-04-24
- Run: `STOP Using Your Credit Card Without Knowing About This IRS Rule [KrwXZY1GvZk]`
- Lane: `YouTube Transcript` and approved `Accounting Domain Review`
- Phase / Step: `Phase 1 artifact generation and catalog update`
- Category: `verification`
- Severity: `medium`
- Status: `closed`
- Issue: Catalog verification metadata recorded incorrect line counts for newly generated artifacts.
- Impact: `notes/output_catalog.md` contained inaccurate verification details for the analysis artifact and later for the domain analysis artifact.
- Likely Cause: Verification metadata was effectively estimated during catalog drafting instead of measured from disk after artifact write.
- Decision / Resolution: Treat verification metadata as measurement-based only; prohibit estimation and require measurement before finalizing catalog notes.
- Instruction or Process Change: Updated shared workflow guidance so the required sequence is write artifact, measure from disk, update catalog, then generate chat-visible completion output. Extended the same rule to approved secondary-lane runs and later-phase artifact steps. Made line counts optional unless measured and useful.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `PIPELINE_USAGE.md`
  - `skills/accounting-domain-review/SKILL.md`
  - `notes/output_catalog.md`
- Verification: Confirmed the final measured values with `wc -l` and patched the incorrect catalog entries. Read back the updated workflow instructions to verify the new sequencing language.
- Reuse Guidance: Future workflow harnesses should treat verification metadata as optional and measurement-derived. Do not let catalog updates or completion displays rely on manual counts or visual estimation.

### LL-2026-04-24-02 - Repo Lane Needed A Cross-Lane Workflow Check

- Date: 2026-04-24
- Run: `oh_my_codex`
- Lane: `GitHub Repo Assessment`
- Phase / Step: `Phase 1 completion and routing`
- Category: `routing`
- Severity: `medium`
- Status: `closed`
- Issue: The GitHub repo lane could finish with a Phase 1 assessment artifact but had no explicit end-of-run check for whether Lane 5 Product Workflow Analysis should run next.
- Impact: Workflow-oriented repositories could be treated as completed repo assessments even when their strongest value was process and operating-model guidance, creating avoidable under-routing and inconsistent Phase 1 behavior across lanes.
- Likely Cause: Cross-lane detection was originally designed around transcript secondary-lane handling and was not extended to the GitHub repo lane.
- Decision / Resolution: Add a lane-local cross-lane applicability check for GitHub repo assessments so Lane 2 explicitly evaluates whether Lane 5 should run before any Phase 2 mapping decision.
- Instruction or Process Change: Updated the canonical workflow, the human-readable workflow companion, and the GitHub repo assessment skill so Phase 1 now supports lane-specific cross-lane checks and the repo lane surfaces a Lane 5 `Strong signal`, `Weak signal`, or no-signal result in the completion display.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
  - `skills/github-repo-assessment/SKILL.md`
- Verification: Read back the patched sections to confirm the standard research flow, Phase 1 completion display, tracker guidance, and Lane 2 prompt instructions all now mention the repo-to-Lane-5 cross-lane check.
- Reuse Guidance: When one lane commonly yields another lane's stronger analysis frame, encode that as an explicit end-of-phase routing check rather than leaving it to ad hoc operator judgment.

### LL-2026-04-24-03 - Lane 5 Needed Progressive Repo Scope Guidance

- Date: 2026-04-24
- Run: `oh_my_codex`
- Lane: `Product Workflow Analysis`
- Phase / Step: `Phase 2 repo-evidence scoping`
- Category: `evidence discipline`
- Severity: `medium`
- Status: `closed`
- Issue: Lane 5 Phase 2 guidance said to inspect only relevant FinOpsAI evidence, but it did not define a default search order, leaving too much room for broad whole-repo review or inconsistent evidence gathering.
- Impact: Workflow applicability assessments could become slower, less focused, and less reproducible, or overread source files before checking the workflow docs and enforcement surfaces that should anchor the decision.
- Likely Cause: The workflow lane had a general scoping rule but lacked an explicit progressive repo-search pattern tailored to process and operating-model questions.
- Decision / Resolution: Establish a default progressive search order for Lane 5 Phase 2: repo guidance first, then `docs/engineering/`, then enforcement surfaces, then representative tests/source only if needed.
- Instruction or Process Change: Updated the canonical workflow, the human-readable workflow companion, and the Lane 5 skill so workflow mapping starts from `AGENTS.md` and `docs/engineering/`, widens only when stronger enforcement evidence is needed, and explicitly stops once the claim is grounded.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
  - `skills/product-workflow-analysis/SKILL.md`
- Verification: Read back the patched sections to confirm the progressive repo search rule appears in the Phase 2 scope guidance, the Lane 5 prompt example, and the product-workflow skill instructions.
- Reuse Guidance: For process-analysis lanes, define a default evidence ladder that starts with policy and workflow docs, then moves to enforcement evidence, then only to representative code when needed. This reduces repo sprawl and keeps workflow claims grounded in the right order.

### LL-2026-04-24-04 - Process-Approval Handoff Needed Approval-Ready Specificity

- Date: 2026-04-24
- Run: `oh_my_codex`
- Lane: `Product Workflow Analysis` to `Phase 3 Human Gate`
- Phase / Step: `Phase 3 route-selection handoff`
- Category: `approval gate`
- Severity: `medium`
- Status: `closed`
- Issue: The Phase 3 process-approval close-out could stop with a generic instruction to choose a recommendation later, without proposing a recommended identifier or repeating the exact approval syntax needed for deterministic continuation into Phase 4.
- Impact: Users could easily respond ambiguously, forcing extra turns and weakening the one-recommendation/one-identifier approval protocol.
- Likely Cause: The approval-capture template was encoded for immediate-candidate card drafting, but not for the process-approval handoff case where a recommendation is concrete enough to continue later.
- Decision / Resolution: Require the Phase 3 process-approval handoff to name one exact recommendation, propose one suggested identifier, and repeat the exact `Approved — identifier: <identifier>` format in the same response.
- Instruction or Process Change: Updated the canonical workflow and the human-readable workflow companion so process-approval route outputs now include an approval-ready handoff template instead of a generic next-step message.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
- Verification: Read back the patched sections to confirm both workflow docs now require a suggested identifier and exact approval format when a process-approval recommendation is ready to continue.
- Reuse Guidance: When a workflow stops at a human approval gate, the response should include the exact next-turn syntax the user needs, not just a description of the decision still required.

### LL-2026-04-24-05 - Every Run Needs One Canonical Reopening Summary

- Date: 2026-04-24
- Run: `oh_my_codex`
- Lane: `Cross-lane run through Phase 4`
- Phase / Step: `Run closure`
- Category: `artifact naming`
- Severity: `medium`
- Status: `closed`
- Issue: The run’s final state could be spread across different durable artifacts depending on where the workflow stopped, forcing returning users to remember whether the best recap lived in a lane artifact, roadmap-fit artifact, catalog note, or chat history.
- Impact: Reopening an old run became needlessly fragile because the location of the final summary depended on phase progression rather than one predictable file path.
- Likely Cause: The workflow emphasized phase-specific durable artifacts and concise catalog entries, but it did not reserve one stable run-closure artifact as the canonical reopening point.
- Decision / Resolution: Require every completed run to produce `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md` and update the catalog to reference that file as the canonical reopening point.
- Instruction or Process Change: Updated the canonical workflow and the human-readable workflow companion to add `run_summary` artifact naming, run-closure sequencing, tracker coverage, and catalog guidance.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
- Verification: Read back the patched sections to confirm both workflow docs now define the `run_summary` artifact and require catalog reference updates during run closure.
- Reuse Guidance: If users may return to completed runs after time has passed, give every run one canonical summary file in the run folder instead of making summary location conditional on phase or lane.

### LL-2026-04-24-06 - Backlog Publication Needed Its Own Workflow Boundary

- Date: 2026-04-24
- Run: `oh_my_codex`
- Lane: `Research to backlog handoff`
- Phase / Step: `Post-Phase-4 boundary definition`
- Category: `routing`
- Severity: `medium`

### LL-2026-04-25-01 - Phase 1 Stop Decisions Must Still Enter Run Closure

- Date: 2026-04-25
- Run: `What Do Models Still Suck At？ - Peter Gostev, Arena.ai, BullshitBench [R7A8rX-09Zw]`
- Lane: `YouTube Transcript` with approved `Product Workflow Analysis`
- Phase / Step: `Phase 1 stop-at-catalog-only closure to run closure`
- Category: `approval gate`
- Severity: `high`
- Status: `closed`
- Issue: The run stopped after the user accepted `no further action yet`, but the required per-run summary artifact and retrospective check were not performed before the run was treated as closed.
- Impact: The run lacked its canonical reopening summary, the catalog did not reference a run-summary artifact, and the retrospective lesson would have been missed without later remediation.
- Likely Cause: The workflow makes run closure mandatory for every completed run, but the explicit summary-approval prompt is written mainly in a late-phase closure branch, making the Phase 1 terminal stop path too easy to misread as already closed.
- Decision / Resolution: Remediate the run by writing the missing run summary, updating the catalog, performing the retrospective check, and patching the workflow docs so a Phase 1 stop recommendation cannot be treated as equivalent to completed run closure.
- Instruction or Process Change: Updated the canonical workflow and the human-readable companion so that when a Phase 1 decision is `stop at catalog-only closure` and the human accepts it, the agent must immediately present the run-closure prompt, obtain approval for the end-of-run summary, write the run summary artifact, update the catalog, and then run the retrospective check.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
  - `notes/output_catalog.md`
  - `output/What Do Models Still Suck At？ - Peter Gostev, Arena.ai, BullshitBench [R7A8rX-09Zw]_2026_04_25/What Do Models Still Suck At？ - Peter Gostev, Arena.ai, BullshitBench [R7A8rX-09Zw]_run_summary_2026_04_25.md`
- Verification: Confirmed the missing run summary was written, measured from disk, referenced in the catalog, and that both workflow docs now state the Phase 1 stop-to-closure transition explicitly.
- Reuse Guidance: Never treat agreement with a stop recommendation as the same thing as completed run closure. Terminal Phase 1 stops still need the same canonical summary and retrospective sequence as later-phase runs.
- Status: `closed`
- Issue: The workflow modeled research-to-draft generation and Product Development sprint intake, but it did not explicitly model the bridge where a Product Owner publishes an approved draft into ClickUp as a real PBI.
- Impact: Draft generation, backlog publication, and Sprint Backlog selection could blur together, making ownership and automation boundaries unclear.
- Likely Cause: The workflow treated ClickUp-ready drafts as the end of research and assumed manual Product Owner publication outside the modeled process.
- Decision / Resolution: Add a separate Backlog Publication bridge between research completion and Product Development Step 1.
- Instruction or Process Change: Updated the canonical workflow and the human-readable workflow companion to define publication as a separate bridge workflow with Product Owner ownership by default, optional future MCP assistance, and explicit separation from Sprint Backlog selection.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
- Verification: Read back the patched sections to confirm both workflow docs now distinguish approved draft creation from published PBI creation and from Product Development Step 1 Sprint intake.
- Reuse Guidance: When a workflow produces publishable backlog artifacts, model publication/admin as its own governed bridge rather than hiding it inside draft generation or sprint selection.

### LL-2026-04-25-01 - Multi-Candidate Runs Need Explicit Next-Step And Closure Prompts

- Date: 2026-04-25
- Run: `AI Agents Ignore Your Skills： Vercel Found the Fix (For Claude Code, Codex, and more) [yEg-7sp9GLU]`
- Lane: `YouTube Transcript` with approved `Product Workflow Analysis`, `FinOpsAI repo mapping`, and Phase 3/4 approval cycles
- Phase / Step: `Phase 4 approval loops and run closure`
- Category: `instruction design`
- Severity: `medium`
- Status: `closed`
- Issue: After completing one approved ClickUp-ready draft in a multi-candidate run, the workflow did not explicitly require the next candidate prompt, and when no more eligible candidates remained, it did not require an actionable closure prompt for end-of-run summary approval.
- Impact: Runs could stall in a descriptively correct but operationally incomplete state, leaving the next candidate unprompted or the run perpetually open without a clear user action.
- Likely Cause: The workflow modeled Phase 4 card cycles and run closure internally, but it did not force a user-facing prompt at the two key continuation boundaries: next eligible candidate and no-more-candidates closure.
- Decision / Resolution: Add explicit instruction that after each completed approved draft, the next eligible candidate must be presented using the structured approval prompt, and if no additional eligible candidate remains, the workflow must prompt for approval to write the end-of-run summary.
- Instruction or Process Change: Updated the canonical workflow and the human-readable workflow companion to require the `Ready to draft the next ClickUp card for:` handoff for remaining candidates and the `Approved — end-of-run summary` closure prompt when no more eligible candidates remain.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
- Verification: Read back the patched workflow sections, then used the new closure prompt path in this run to approve end-of-run summary generation and proceed into run closure correctly.
- Reuse Guidance: For any multi-candidate approval workflow, every loop exit must be user-actionable. After a successful draft cycle, either present the next exact candidate in approval-ready form or present an explicit closure approval prompt. Never end with a passive state description when the run still needs human confirmation to continue or close.

### LL-2026-04-25-02 - Refreshed Cycles In Reused Run Folders Need Full State Re-Verification

- Date: 2026-04-25
- Run: `It Ain't Broke： Why Software Fundamentals Matter More Than Ever [v4F1gFy-hqg]`
- Lane: `YouTube Transcript` with approved `GitHub Repo Assessment`, `Product Workflow Analysis`, refreshed `FinOpsAI repo mapping`, and refreshed Phase 3/4 approval cycles
- Phase / Step: `Phase 2 through run closure`
- Category: `verification`
- Severity: `medium`
- Status: `closed`
- Issue: When a later workflow cycle reuses an older run folder with existing downstream artifacts, newly written refreshed artifacts can leave stale line counts, outdated catalog notes, or now-incorrect progress-state text unless every affected durable record is re-measured and re-synchronized.
- Impact: The run briefly contained inconsistent metadata and workflow-state statements across the refreshed roadmap-fit artifact and `notes/output_catalog.md`, which could have misled later reopening or approval work.
- Likely Cause: The run reused an older folder with existing mapping, roadmap-fit, and card-draft history, so refreshed artifacts changed the run state without automatically invalidating older derived notes and counts.
- Decision / Resolution: Treat refreshed cycles in reused run folders as full state-refresh operations: after each new artifact write, re-measure from disk, re-check the refreshed artifact's internal state language, and then update catalog notes that summarize the run's current status.
- Instruction or Process Change: No workflow-doc patch was required in this run; the lesson was applied operationally by re-verifying the refreshed mapping, roadmap-fit, card-draft, and closure artifacts before final run summary generation.
- Impacted Files:
  - `notes/output_catalog.md`
  - `notes/lessons_learned.md`
  - `output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_roadmap_fit_2026_04_25.md`
  - `output/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_2026_04_23/It Ain't Broke： Why Software Fundamentals Matter More Than Ever — Matt Pocock, AI Hero @mattpocockuk [v4F1gFy-hqg]_run_summary_2026_04_25.md`
- Verification: Re-measured the refreshed artifacts with `wc -l`, corrected stale catalog counts and notes, corrected stale roadmap-fit state text, and then wrote the run summary only after the refreshed state was consistent.
- Reuse Guidance: When a run folder already contains older downstream artifacts, do not treat a refreshed cycle as a narrow append-only step. Re-verify every stateful summary artifact and catalog note that could be invalidated by the refreshed outputs before declaring the run closed.

### LL-2026-04-25-03 - Phase 1 Needed Explicit Separation Between Signals, Decisions, And Approval-Ready Actions

- Date: 2026-04-25
- Run: `[FULL WORKSHOP] AI Coding For Real Engineers - Matt Pocock, AI Hero [-QFHIoCo-Ko]`
- Lane: `YouTube Transcript`
- Phase / Step: `Phase 1 completion display`
- Category: `instruction design`
- Severity: `high`
- Status: `closed`
- Issue: The Phase 1 response blurred together a strong cross-lane signal, a stop-at-catalog-only recommendation within the user's constrained option set, and an approval-ready next action.
- Impact: The output appeared self-contradictory and it surfaced Lane 2 GitHub repo assessment too loosely even though no concretely named target repo had been confirmed in the response.
- Likely Cause: The workflow required the display sections but did not explicitly force decision-surface separation or define when a Lane 2 assessment is approval-ready.
- Decision / Resolution: Add explicit separation rules for cross-lane routing, Proceed/Stop decisions, constrained option-set recommendations, and approval-ready next actions. Also require a concretely named repo target before surfacing Lane 2 as approval-ready.
- Instruction or Process Change: Updated the canonical workflow, transcript-lane guidance, and human-readable workflow companion so Phase 1 outputs must distinguish these surfaces explicitly, must state when the user's option set is narrower than the full workflow, and must not offer `Approved — Lane 2 GitHub repo assessment` without a concrete target repo named in the same response.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `PIPELINE_USAGE.md`
  - `finopsai_research-to-backlog_workflow.md`
- Verification: Read back the patched sections to confirm the new decision-surface separation rule, constrained-option wording guidance, and Lane 2 approval-readiness rule are present.
- Reuse Guidance: When a workflow has multiple decision layers, require the response format to separate them explicitly; otherwise valid routing signals can be mistaken for immediate recommendations or approvals.

### LL-2026-04-25-04 - Stop Recommendations Needed A Dedicated No-Go Rationale Section

- Date: 2026-04-25
- Run: `You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]`
- Lane: `YouTube Transcript`
- Phase / Step: `Phase 1 completion display`
- Category: `instruction design`
- Severity: `medium`
- Status: `closed`
- Issue: When the workflow recommended not proceeding, the explanation could be compressed into the recommendation line or next-action line instead of appearing as its own clearly scannable reason.
- Impact: Users could see the stop decision without getting a distinct explanation for why Phase 2 or later work was not justified, which reduced the clarity of stop-path outcomes.
- Likely Cause: The completion-display format had separate sections for recommendation and next action but no dedicated surface for no-go reasoning.
- Decision / Resolution: Add a required `No-Go Rationale` section between `Proceed / Stop Recommendation` and `Recommended Next Action` whenever the recommendation is not to proceed.
- Instruction or Process Change: Updated the canonical workflow and transcript-lane guide so Phase 1 completion displays are conditionally 7 sections when proceeding and 8 sections when stopping, with an explicit no-go explanation that cannot be collapsed into the next-action field.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `PIPELINE_USAGE.md`
- Verification: Read back the patched completion-display rules and confirmed the conditional section-count rule and dedicated no-go wording are present in both the controlling workflow and the lane reference.
- Reuse Guidance: If a workflow can end in a stop/no-go state, reserve one explicit output surface for the reason the run should not advance. Do not hide no-go reasoning inside the recommendation label or the next-step text.

### LL-2026-04-25-05 - Technical-Education Transcripts Needed A Validation-Driven Phase 2 Path

- Date: 2026-04-25
- Run: `You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]`
- Lane: `YouTube Transcript`
- Phase / Step: `Phase 2 entry decision`
- Category: `routing`
- Severity: `medium`
- Status: `closed`
- Issue: Technical-education transcripts could contain useful engineering patterns for bounded refactor or technical-debt work, but the workflow had no explicit rule for advancing to Phase 2 when validation created a concrete repo-facing hypothesis.
- Impact: Useful transcript runs risked stopping too early at catalog-only closure even when later validation could justify a narrow repo mapping and card-candidate path.
- Likely Cause: Phase 2 entry rules assumed either direct implementation-level applicability from the source or no-go closure, without an intermediate validation-driven escalation path for educational material.
- Decision / Resolution: Allow transcript validation to strengthen a weak Phase 1 source into a valid Phase 2 candidate only when the validation produces bounded, non-speculative repo-facing refactor, technical-debt, `docs`, `test`, `chore`, or workflow-improvement hypotheses.
- Instruction or Process Change: Updated the canonical workflow and transcript-lane guide to define optional transcript validation, clarify that generic technical correctness is not enough, and require the decision to say explicitly when progression is based on validation-derived hypotheses rather than transcript interest alone.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `PIPELINE_USAGE.md`
- Verification: Read back the Phase 2 entry-decision rules and transcript-lane validation section to confirm the new proceed criteria, stop criteria, and validation-specific explanation requirements were present.
- Reuse Guidance: For research lanes that often start as general education, add an explicit validation-driven escalation rule so strong bounded implementation hypotheses can continue into repo mapping without lowering the evidence standard.
