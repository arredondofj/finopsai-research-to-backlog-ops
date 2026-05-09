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

### LL-2026-05-07-01 - Stop Recommendations Should End With An Actionable Closure Approval Prompt

- Date: 2026-05-07
- Run: `adversarial_dev`
- Lane: `GitHub Repo Assessment` with approved `Product Workflow Analysis`
- Phase / Step: `Phase 1 completion display stop path`
- Category: `instruction design`
- Severity: `medium`
- Status: `open`
- Issue: The stop recommendation wording could end with a passive phrase such as `Stop at catalog-only closure for this run`, which states the disposition but does not clearly tell the user how to accept the stop and trigger the required run-closure sequence.
- Impact: Users can reasonably think the run is already finished, even though the workflow still requires an explicit closure approval before the end-of-run summary is written and the run is formally closed.
- Likely Cause: The workflow already defines the stop-path mechanics and the later closure syntax, but the recommendation line itself does not consistently echo that next required action in user-facing language.
- Decision / Resolution: Record a wording rule that stop recommendations should be definitive and action-oriented. Prefer wording that both declares the stop decision and points immediately to the closure approval step instead of stopping at a passive status description.
- Instruction or Process Change: When the Phase 1 recommendation is to stop, prefer wording substantially like: `Stop at this step and hold at catalog-only closure for this run.` Then follow it with an explicit closure instruction that tells the user how to continue, using the existing approval syntax: `If you want to close the run here, reply: Approved — end-of-run summary`. This preserves the decision/next-step separation while making the stop path operationally clear.
- Impacted Files:
  - `notes/lessons_learned.md`
  - `RESEARCH_WORKFLOW_USAGE.md` (future wording refinement recommended)
- Verification: Confirmed that the workflow already contains the required closure-approval syntax `Approved — end-of-run summary`, and compared that existing requirement against the softer stop wording used in the recent Phase 1 response.
- Reuse Guidance: Any workflow stop state that still requires one more human approval should say both things explicitly: that work stops here for now, and the exact approval phrase needed to finish closure. Do not leave stop-path responses as passive state labels when the run is not yet formally closed.

### LL-2026-05-07-02 - Research Closure Needed An Explicit Automatic Intake Handoff Before Backlog Governance Step 1

- Date: 2026-05-07
- Run: `Don’t Use Boolean Flags in Python, Use Policies Instead [wYeDGkdMi3g]`
- Lane: `YouTube Transcript`
- Phase / Step: `run closure / bridge boundary`
- Category: `workflow boundary`
- Severity: `high`
- Status: `closed`
- Issue: Research workflow closure ended with approved ClickUp-ready draft artifacts and run summary, while Backlog Governance Step 1 expected those same draft artifacts to have already been deposited into the governance intake folder with receipt and duplicate handling completed.
- Impact: The user-facing workflow looked complete from the research side, but the next workflow could not begin cleanly without a manual, undocumented transfer step. That created an observability gap, made automation ambiguous, and weakened auditability across the boundary.
- Likely Cause: A previous refactor preserved the Backlog Publication bridge but dropped the earlier automatic intake-deposit bridge that should happen after run-summary approval and before Backlog Governance Step 1.
- Decision / Resolution: Reinsert an explicit `Backlog Governance Intake Handoff` as its own automatic post-run-summary bridge step. Keep it outside `Another approved recommendation to process?` and outside Phase 4 Step 3 so recommendation-cycle control, draft generation, and governance intake remain distinct.
- Instruction or Process Change: Updated the canonical workflow and the human-readable workflow companion so research closure now includes automatic deposit of approved draft artifacts into `governance-states/01_intake/`, duplicate quarantine into `governance-states/01_intake_duplicates/`, one run-level receipt, durable recording of the handoff result back into the run summary or roadmap-fit artifact, and a required workflow-tracker bridge row whenever approved drafts exist.
- Impacted Files:
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `docs/finopsai_research-to-backlog_workflow.md`
  - `notes/lessons_learned.md`
- Verification: Read back the standard-flow steps, the new bridge section, the updated research boundary wording, and the workflow progress tracker rows to confirm that automatic intake handoff now occurs after run-summary approval and before Backlog Governance Step 1.
- Reuse Guidance: When one workflow ends with approved draft artifacts and the next workflow starts from an operational inbox, model the inbox deposit and receipt as a distinct automatic bridge step. Do not hide that handoff inside a recommendation loop or inside a draft-generation step.

### LL-2026-05-07-03 - Final Approved Draft Cycles Still Need An Explicit End-Of-Run Summary Approval Prompt

- Date: 2026-05-07
- Run: `Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]`
- Lane: `YouTube Transcript` with approved `Product Workflow Analysis`, `FinOpsAI repo mapping`, and one approved Phase 4 draft cycle
- Phase / Step: `post-Phase-4 closure handoff`
- Category: `approval gate`
- Severity: `high`
- Status: `closed`
- Issue: After the final approved ClickUp-ready draft cycle completed, the response did not present the required explicit closure prompt telling the user that no additional eligible card candidates remained and asking for approval to write the end-of-run summary.
- Impact: The workflow advanced directly into run-summary generation and governance handoff without giving the human the deterministic final approval step defined by the harness. A user could not see the exact required next action in chat, and formal closure approval was skipped.
- Likely Cause: The workflow already encoded the closure prompt for both stop-path runs and post-Phase-4 runs, but the execution path over-focused on completing the approved draft cycle and bridge handoff instead of pausing at the mandatory end-of-run approval checkpoint.
- Decision / Resolution: Treat the missing closure prompt as an execution flaw, not a document-authority gap. The controlling workflow already defines the exact required wording and sequencing for this situation.
- Instruction or Process Change: After the last approved recommendation in a run is processed, always stop and emit the required closure prompt before writing the run summary or performing governance intake handoff. Use the documented wording substantially like: `No additional eligible ClickUp card candidates remain for this run.` followed by `Ready to write the end-of-run summary for: <run/source name>` and `Approved — end-of-run summary`.
- Impacted Files:
  - `notes/lessons_learned.md`
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `docs/finopsai_research-to-backlog_workflow.md`
- Verification: Re-read the controlling closure rules and patched both workflow docs so closure approval is now a distinct mandatory tracked gate in the controlling workflow and the companion narrative explicitly forbids writing the run summary or performing governance handoff before that approval.
- Reuse Guidance: When a run reaches "no additional eligible card candidates remain," do not treat artifact completion as permission to close the run. The human still needs one deterministic final approval step, and the exact approval syntax must be shown in chat before closure work begins.

### LL-2026-05-07-04 - FinOpsAI Repo Mapping Needed A Canonical Path Guardrail

- Date: 2026-05-07
- Run: `Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]`
- Lane: `Product Workflow Analysis` with approved `FinOpsAI repo mapping`
- Phase / Step: `Phase 2 repo-target selection`
- Category: `repo mapping`
- Severity: `high`
- Status: `closed`
- Issue: The run used `/Users/Dev/Prototypes/FinOpsAI` as the FinOpsAI target repo during mapping and drafting even though the intended active repo had been moved and renamed to `/Users/Dev/Apps/finopsai-desktop`.
- Impact: Repo-mapping and ClickUp-ready draft artifacts recorded the wrong target-repo path, understated the available engineering guidance surfaces, and propagated incorrect repo references into durable workflow artifacts.
- Likely Cause: Workflow and skill docs still pointed to an old canonical FinOpsAI path, and execution silently fell back to a different visible local checkout instead of stopping when the expected path was unavailable.
- Decision / Resolution: Establish `/Users/Dev/Apps/finopsai-desktop` as the canonical local FinOpsAI path in the research workspace and require a human confirmation stop whenever that canonical path is missing and another checkout is the only visible candidate.
- Instruction or Process Change: Updated the workspace `AGENTS.md`, the canonical workflow, the human-readable workflow companion, and the FinOpsAI-relevant lane skills to use `/Users/Dev/Apps/finopsai-desktop`, to point card-drafting guidance to `docs/engineering/workflows/`, and to forbid silent local-checkout substitution before Phase 2 mapping or Phase 4 drafting.
- Impacted Files:
  - `AGENTS.md`
  - `RESEARCH_WORKFLOW_USAGE.md`
  - `docs/finopsai_research-to-backlog_workflow.md`
  - `skills/product-workflow-analysis/SKILL.md`
  - `skills/accounting-domain-review/SKILL.md`
  - `skills/github-repo-assessment/SKILL.md`
  - run artifacts under `output/Why Senior Devs Keep Shipping Slow (And How to Stop) [bNKRiN86cho]_2026_05_07/`
- Verification: Confirmed that `/Users/Dev/Apps/finopsai-desktop` exists, contains `.git`, `AGENTS.md`, `docs/engineering/standards/programming_guidance.md`, and the expected workflow guidance files under `docs/engineering/workflows/`. Read back the patched workflow and skill files to verify the new canonical path and stop condition were present.
- Reuse Guidance: When a workflow depends on one target repo repeatedly, encode one canonical local path and add an explicit mismatch stop. Never let repo mapping or task-card drafting silently switch to another visible checkout just because it exists on disk.
