# Research Workflow Usage Guide

<!-- MAINTENANCE NOTE: This file is the canonical control document for the
shared research harness. The HTML workflow (finopsai_research-to-backlog_workflow.html)
is a human-readable companion only. When the two diverge, this file governs.
After any update to this file, review the HTML for accuracy. -->

## Document Authority

This file is the controlling authority for source routing, artifact naming,
repo-mapping categories, roadmap-fit statuses, chat-visible gate outputs, and
the ClickUp card-candidate gate.

`AGENTS.md` governs workspace-scoped behavior and lane skill selection. For
any conflict between `AGENTS.md` and this file on shared harness decisions —
routing, gates, approval handling, artifact naming, or catalog discipline —
this file takes precedence.

`PIPELINE_USAGE.md` governs YouTube transcript lane mechanics (acquisition,
cleanup, scripts, secondary lane signal detection, and run-folder naming).
For Phase 1 completion display format and catalog update sequencing, this file
governs. Do not use `PIPELINE_USAGE.md` step-level completion guidance as a
substitute for the `Phase 1 Completion Display` section below.

## Purpose

Use this guide when source material should be researched, assessed, mapped to FinOpsAI, or converted into a Product Owner backlog candidate.

This guide defines the shared research harness. It does not replace the YouTube transcript lane. Use `PIPELINE_USAGE.md` for transcript cleanup and transcript-only analysis details.

The shared harness should:
- route each source to the correct workflow lane,
- use consistent artifact names,
- expose consistent chat-title metadata for CodeX UI or automation hooks,
- keep catalog entries concise,
- separate research findings from roadmap decisions,
- map ideas to FinOpsAI only when requested or needed,
- and generate ClickUp task-card drafts only after approval gates pass.

The shared harness does not, by default, publish approved draft cards into
ClickUp. Publication and Product Owner backlog administration are modeled as a
separate bridge workflow between research completion and Product Development
Sprint intake.

## Core Rule

Do not treat all research as the same pipeline.

Use one shared harness with separate workflow lanes:
- YouTube Transcript.
- GitHub repo assessment.
- Web source research.
- Product requirement triage.
- Accounting domain review.
- Product workflow analysis.

The harness standardizes outputs and gates. The lanes preserve source-specific analysis rules.

## Source Taxonomy

### YouTube Transcript

Use for:
- YouTube URLs,
- `.vtt` subtitle files,
- raw transcript text files.

Typical work:
- acquire transcript when needed,
- clean transcript,
- analyze source content,
- optionally map to FinOpsAI.

Use:
- `PIPELINE_USAGE.md`
- `skills/research-markdown-authoring/SKILL.md`
- `skills/youtube-transcript-pipeline/SKILL.md`

### GitHub Repository

Use for:
- external GitHub repositories,
- local clones of external repositories,
- repo patterns, architecture, tooling, prompts, tests, or workflows offered as source material.

Typical work:
- identify repo purpose and maturity,
- inspect relevant architecture and docs,
- assess reusable ideas,
- identify license, dependency, security, or compatibility concerns when evidence is available,
- assign an applicability level and next-step recommendation with cited rationale,
- surface that recommendation clearly to the user after the assessment,
- map patterns to FinOpsAI only when useful.

Do not copy code or recommend code reuse without explicit review.

Use:
- `skills/research-markdown-authoring/SKILL.md`
- `skills/github-repo-assessment/SKILL.md`

### Web Source

Use for:
- web articles,
- documentation pages,
- benchmark or eval posts,
- announcements,
- standards/RFC-style pages,
- and other internet-published material that is not primarily a YouTube
  transcript or GitHub repository.

Typical work:
- validate and normalize the URL,
- capture canonical source metadata and access date,
- prefer deterministic scripted capture when possible,
- preserve citation-ready evidence context,
- analyze the source content,
- and optionally map the result to FinOpsAI.

Use:
- `skills/research-markdown-authoring/SKILL.md`
- `skills/web-source-research/SKILL.md`

### Business Requirement

Use for:
- raw Product Owner requests,
- stakeholder requests,
- feature ideas,
- workflow pain points,
- initial business requirements needing vetting.

Typical work:
- clarify the core requirement,
- identify expected outcome,
- determine whether it is one primary work item,
- decide whether Product Design Workflow is required,
- decide whether ClickUp card drafting is appropriate.

Use:
- `skills/research-markdown-authoring/SKILL.md`
- `skills/business-requirement-triage/SKILL.md`

### Accounting And Bookkeeping Domain Content

Use for:
- accounting, bookkeeping, finance operations, tax, reconciliation, reporting, compliance, or advisory content.

Typical work:
- identify domain area,
- identify user profile and jurisdiction when relevant,
- separate domain education from product feature ideas,
- identify compliance, review, auditability, and roadmap risks,
- map only high-confidence, product-relevant ideas to FinOpsAI.

Do not turn tax, compliance, or accounting advice into implementation tasks without human approval and appropriate professional review.

Use:
- `skills/research-markdown-authoring/SKILL.md`
- `skills/accounting-domain-review/SKILL.md`

### Product Development Workflow Content

Use for:
- product development process material,
- human-in-the-loop workflow material,
- agentic delivery practices,
- backlog refinement practices,
- specification, QA, review, or ClickUp workflow ideas.

Typical work:
- separate process improvements from product features,
- decide whether the idea affects the current human workflow, future agent-assisted workflow, or both,
- classify possible outputs as docs, process, harness tooling, prompt updates, QA gates, or deferred notes,
- map workflow/tooling ideas to FinOpsAI when repo-grounded evidence is requested or needed.

Use:
- `skills/research-markdown-authoring/SKILL.md`
- `skills/product-workflow-analysis/SKILL.md`

### Shared Research Markdown Authoring

Use for:
- any durable markdown artifact under `output/`,
- lane analysis artifacts,
- applicability or repo-mapping artifacts,
- roadmap-fit artifacts,
- run summaries,
- and revisions needed to make those artifacts easier for later phases to
  consume.

Typical work:
- expose summary, evidence, caveats, candidate ideas, exclusions, disposition,
  and verification surfaces consistently,
- keep recommendation candidates distinct instead of blending them into one
  narrative,
- make scope and next-step guidance explicit before roadmap-fit or card work,
- and reduce interpretation loss between Phase 1, Phase 2, Phase 3, and
  Phase 4.

Use:
- `skills/research-markdown-authoring/SKILL.md`

## Routing Table

| Source Type | First Artifact | Optional Next Artifact | FinOpsAI Mapping? | ClickUp Candidate? |
| --- | --- | --- | --- | --- |
| YouTube transcript | Cleaned transcript + analysis report | Repo mapping report | Optional | Only after mapping and approval |
| GitHub repo | GitHub repo assessment with applicability recommendation | Repo mapping report | Usually yes if FinOpsAI relevance is requested and the assessment recommends moving forward | Only for high-confidence compatible ideas |
| Web article / documentation / internet source | Web capture + source analysis report | Repo mapping report | Optional when the source produces concrete FinOpsAI-relevant ideas | Only after mapping and approval |
| Business requirement | Requirement triage report | Roadmap fit or design referral | As needed | Yes, if task-card gates pass |
| Accounting/bookkeeping content | Domain analysis report | Domain applicability or repo mapping report | Only when product-relevant | Only after domain and roadmap approval |
| Product workflow content | Workflow analysis report | Workflow applicability or repo mapping report | Only if it affects FinOpsAI docs/tooling/process | Usually `docs` or `chore`, only after approval |

## Artifact Naming Conventions

Use lowercase descriptive suffixes and the run date.

Create one run folder per source run:
- `output/<n>_YYYY_MM_DD/`

Store all durable artifacts for that run inside the run folder. Keep the same
`<n>` prefix on each file inside the folder. Use the date of the first
durable artifact for the run as the folder date. If later phases happen on a
later day, keep their files in the same folder and preserve each file's own
date suffix.

Transcript artifacts:
- `output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt`
- `output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_repo_mapping_YYYY_MM_DD.md`

Shared research artifacts:
- `output/<n>_YYYY_MM_DD/<n>_web_capture_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_source_analysis_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_github_repo_assessment_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_domain_analysis_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_domain_applicability_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_workflow_analysis_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_workflow_applicability_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_requirement_triage_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md`
- `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md`

ClickUp-ready draft naming:
- Use `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md`
  for every approved card draft in a run.
- The suffix identifier is required and must distinguish the work item clearly
  enough that later drafts do not overwrite earlier approved card artifacts.

Catalog:
- Update `notes/output_catalog.md` after generated research runs that produce durable artifacts.
- Keep entries concise and referential.
- Do not paste full transcript text, long source excerpts, or long analysis sections.
- Treat the per-run summary artifact as the canonical reopening point for a
  completed run when one exists.
- Verification metadata such as line counts is optional. If recorded, it must
  be measured from the saved artifact after write and before the catalog entry
  is finalized.

## External Source Evidence Discipline

For internet-derived sources, record enough metadata that a later reviewer can
understand what was accessed and when.

Required for web-source and remote-GitHub research artifacts:
- original URL,
- canonical URL when different,
- source title / page title when available,
- publisher or site name when available,
- access date,
- acquisition method,
- and whether the evidence came from web-visible pages only or from a local
  clone / local file as well.

Preferred capture rule for general web sources:
- When possible, use
  `skills/web-source-research/scripts/capture_web_source.sh <url> <output.md>`
  to create the `_web_capture_YYYY_MM_DD.md` artifact deterministically.
- If scripted capture fails or is unsuitable for the source, record the failure
  mode and the fallback acquisition method explicitly in the artifact.

Freshness rule:
- If a source claim is time-sensitive, product-changing, benchmark-sensitive,
  or likely to drift, re-check it before finalizing Phase 2 or later-phase
  recommendations.
- If the source could not be re-checked, record the freshness gap explicitly.

Citation rule:
- Prefer primary sources over commentary when both are available.
- Keep quotes minimal.
- Attribute important claims to the specific source artifact or web page used.
- If a critical claim rests on weak or secondary evidence, mark that caveat in
  the analysis artifact instead of smoothing it over.

## Repo-Mapping Categories

Use these categories when mapping source ideas to FinOpsAI:
- Product feature applicability.
- Harness or workflow tooling applicability.
- AI integration applicability.
- Prompting or agent workflow applicability.
- Coding practice or engineering process applicability.
- Architecture or infrastructure applicability.
- Testing, QA, or evaluation applicability.
- Documentation, specification, or product-vault applicability.
- Non-applicable, premature, or rejected ideas.

For each relevant category, record:
- source idea,
- source evidence,
- FinOpsAI evidence,
- applicability level,
- required change type,
- risk,
- recommended next artifact.

Multi-source evidence rule:
- Before making any applicability judgment in Phase 2, read every durable
  artifact present in the run folder. This includes the primary lane artifact
  and any secondary lane artifacts produced by approved secondary lane runs
  during Phase 1 (GitHub repo assessment, domain analysis, workflow analysis,
  requirement triage).
- The repo mapping must cite all available evidence sources and distinguish
  their individual contributions:
  - primary lane artifact findings (e.g. transcript-derived ideas),
  - secondary lane artifact findings (e.g. repo-validated or domain-reviewed
    ideas), clearly attributed to the lane that produced them,
  - and FinOpsAI codebase compatibility evidence.
- Do not allow any single source to silently override another. If a secondary
  lane artifact validates, challenges, or reframes a primary lane finding,
  state that explicitly in the mapping.
- If only one artifact type is present (primary lane only, no secondary lane
  artifacts), state that explicitly so the scope of the evidence base is clear.
- Do not substitute transcript impressions for concrete repo evidence, and do
  not let a later secondary lane artifact silently replace earlier primary lane
  analysis without stating the relationship.

When FinOpsAI is the target repo:
- read `/Users/Sites/Repo-FinOpsAI/AGENTS.md` first,
- apply nested `AGENTS.md` files if present in relevant areas,
- treat the task as read-only unless implementation is explicitly requested,
- preserve deterministic accounting, review, approval, posting, credential, dependency, privacy, and testing constraints.

## Roadmap-Fit Statuses

Use one of these statuses for each recommendation:

| Status | Meaning | Typical Next Step |
| --- | --- | --- |
| `Immediate candidate` | Clear fit, strong evidence, low ambiguity, compatible with current architecture and roadmap. | Human approval for card drafting. |
| `Needs roadmap approval` | Product-relevant but not already established as current priority. | Product Owner decision. |
| `Needs product design` | Product intent, UX behavior, acceptance outcomes, or scope boundaries are incomplete. | Product Design Workflow. |
| `Needs architecture design` | Requires structural change, new integration pattern, persistence change, external service, or significant dependency. | Architecture/design assessment before card drafting. |
| `Needs process approval` | Affects human workflow, ClickUp workflow, prompts, QA gates, or team operating model. | Process owner approval. |
| `Research backlog` | Interesting but not ready for implementation or product commitment. | Store as research note or future review item. |
| `Deferred` | Plausible but blocked by timing, missing evidence, roadmap mismatch, or dependency. | Record in the roadmap-fit artifact by default; use a separate deferred note only if volume or review needs justify it. |
| `Rejected` | Poor fit, unsafe, speculative, contradictory, or outside FinOpsAI scope. | Record in the roadmap-fit artifact by default; use a separate rejected note only if volume or review needs justify it. |

## Consolidation Rule

Use `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` as the default
durable decision record for all recommendation statuses, including:
- `Immediate candidate`
- `Needs roadmap approval`
- `Needs product design`
- `Needs architecture design`
- `Needs process approval`
- `Research backlog`
- `Deferred`
- `Rejected`

Do not create separate deferred or rejected artifacts by default.

Create `output/<n>_YYYY_MM_DD/<n>_deferred_ideas_YYYY_MM_DD.md` or
`output/<n>_YYYY_MM_DD/<n>_rejected_ideas_YYYY_MM_DD.md` only when one
of these is true:
- the deferred or rejected set is large enough to swamp the roadmap-fit file,
- the decision needs a separate audience, review cycle, or approval path,
- the deferred or rejected items require substantial supporting evidence beyond
  status-level reasoning,
- or the deferred or rejected content becomes its own reusable research note.

When a separate deferred or rejected artifact is created as an exception, the
roadmap-fit artifact must still retain the status row, concise rationale, and
linking reference to that exception artifact.

## ClickUp Card-Candidate Gate

Research output should create card candidates, not automatic task cards.

Use the card-candidate gate in two stages:

1. `Readiness check`
   - Determine whether the approved recommendation is ready to proceed to
     ClickUp-ready drafting.
   - This check verifies the approved recommendation against the card-candidate
     conditions before any file is written.

2. `Draft authorization`
   - Generate a ClickUp-ready task-card draft only after the readiness check
     passes and previously recorded human approval exists for that exact
     recommendation and identifier.

Readiness check conditions:
- the source artifact exists,
- source evidence is summarized,
- caveats and risks are recorded,
- FinOpsAI applicability is grounded in repo or product evidence,
- roadmap-fit status is `Immediate candidate` or otherwise eligible for card consideration,
- the work is one primary task,
- product-design readiness has been decided,
- scope and out-of-scope boundaries are clear,
- acceptance criteria can be written without inventing requirements,
- the expected task type is known: `feat`, `fix`, `refactor`, `docs`, `test`, or `chore`,
- a governing spec path can be selected or the work is routed to Product Design first.

Draft authorization condition:
- the human explicitly approves card drafting for one specific recommendation.
- the approval must identify the exact recommendation being authorized.
- the approval must identify the intended draft filename identifier.
- if the recommendation target or identifier is ambiguous, stop and ask for
  clarification before drafting.

### Approval Capture Protocol

When requesting approval for card drafting, present the following in the chat
before writing any file:

1. The exact recommendation name being authorized.
2. The proposed full draft file path including the identifier.
3. An explicit confirmation prompt asking the user to approve both.

Use this template:

```
Ready to draft a ClickUp card for: <recommendation name>
Proposed file: output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md

Please confirm approval using this format:
  Approved — identifier: <identifier>

Or provide a different identifier if the proposed one is not suitable.
```

If a ClickUp-ready draft has just been generated for one approved
recommendation and additional eligible recommendations still remain in the same
run, immediately present the next candidate using a follow-on prompt rather
than a generic summary. Use this follow-on template:

```
Ready to draft the next ClickUp card for: <recommendation name>
Suggested identifier: <identifier>

Please confirm using this format:
  Approved — identifier: <identifier>

If you want a different identifier, send the same format with your preferred identifier.
```

Do not accept an approval that does not confirm both the recommendation name
and the identifier. If the user message is ambiguous — for example, "yes go
ahead" or "looks good" without naming the recommendation or identifier — stop
and ask for the missing confirmation before writing any file.

One-to-one recommendation-to-card rule:
- one approved recommendation authorizes one ClickUp-ready task-card draft.
- do not combine multiple recommendations into one card draft.
- do not generate multiple card drafts from one approval message unless the
  human explicitly approves each recommendation separately.
- when asking for approval or recording approval, name the exact
  recommendation and the exact identifier to be used in
  `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md`.

ClickUp draft collision rule:
- Before writing any ClickUp-ready draft file, verify whether the target file
  path already exists.
- If the target file already exists, stop and inform the user instead of
  overwriting it.
- Recommend the fix: either review the existing artifact and confirm reuse, or
  approve a new uniquely suffixed filename for the next card draft.
- Do not overwrite an existing ClickUp-ready draft artifact silently.

Use FinOpsAI's card guidance as the source of truth:
- `/Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md`
- `/Users/Sites/Repo-FinOpsAI/docs/engineering/clickup_sprint_kanban_title_guide.md`
- `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-development-workflow.html`
- `/Users/Sites/Repo-FinOpsAI/docs/engineering/finopsai-product-design-workflow.html`

The task-card guide requires:
- Request Appropriateness gate first,
- Information Sufficiency gate second,
- no card generation if either gate fails,
- no invented requirements,
- one primary work item,
- one governing specification path,
- `Generate Specification` and `Generate Execution Prompt` subtasks when applicable,
- specification stored in the repo,
- execution prompt kept on the ClickUp card, not in the repo.

Never automatically convert these into ClickUp cards:
- speculative ideas,
- weakly supported source claims,
- roadmap-misaligned ideas,
- multi-work-item bundles,
- unclear product behavior,
- tax or compliance-sensitive recommendations without review,
- AI/model behavior that would replace deterministic accounting controls,
- architecture rewrites inspired by external repositories,
- new dependencies, external services, RAG, MCP, model-serving, or automation without explicit approval.

## Phase 2 Entry Decision

After Phase 1 source analysis and any approved secondary lane runs are complete,
and the completion display has been shown in the chat, decide explicitly whether
to proceed to Phase 2 FinOpsAI mapping or stop at catalog-only closure.

The Phase 2 entry decision must account for all available run-folder artifacts —
primary lane and any secondary lane artifacts — not just the initial Phase 1
analysis. A secondary lane run may strengthen or create the case for Phase 2
even when the primary lane analysis alone would not have justified it.

This decision must be stated in the Phase 1 completion display before any
Phase 2 work begins. Do not enter Phase 2 without making the decision
explicit.

Proceed to Phase 2 when:
- The lane output contains candidate ideas that may affect FinOpsAI product
  behavior, repo architecture, engineering workflow, prompts, testing, or
  documentation.
- The user has requested FinOpsAI mapping.
- The source contains at least one pattern, idea, or finding grounded in
  implementation-level evidence with plausible FinOpsAI relevance.
- A transcript-lane validation step has produced one or more bounded,
  non-speculative refactor, technical-debt, `docs`, `test`, `chore`, or
  workflow-improvement hypotheses that are plausible candidates for repo
  assessment in Phase 2.

Validation-driven Phase 2 rule:
- Transcript validation may strengthen a weak Phase 1 source into a valid
  Phase 2 candidate, but only when the validation output does more than
  confirm that the speaker is technically correct.
- Validation must produce concrete engineering hypotheses that can be checked
  against the target repo, such as duplicated boilerplate, ad hoc validation,
  weak typing/tooling support, repetitive parser/config patterns, brittle test
  structure, or similar maintainability issues.
- Validation alone is not enough if it yields only general education value,
  generic best practices, or language-level correctness with no plausible repo
  mapping surface.
- When this rule is used, the Phase 1 completion display must say explicitly
  that the recommendation to proceed is based on validation-derived refactor or
  technical-debt hypotheses rather than on transcript interest alone.

Stop at catalog-only closure when:
- The request was transcript cleanup, source-only analysis, general education
  capture, or a non-FinOpsAI comparison.
- The source is speculative, hype-dense, or lacks concrete implementation
  patterns with FinOpsAI applicability.
- The user has not requested mapping and no strong mapping case exists from
  the lane output.
- The Lane To Phase Map table for the selected lane marks Phase 2 as not
  applicable.
- A transcript validation step, if performed, confirmed only general technical
  correctness and did not produce bounded repo-relevant refactor or
  technical-debt hypotheses.

When stopping at catalog-only closure, the Phase 1 completion display must
name the specific source topic and explain why that topic does not currently
justify Phase 2 work. The explanation must be topic-specific, not generic.

If the human accepts a `stop at catalog-only closure` recommendation, do not
treat that acceptance as completed run closure by itself. Immediately
transition into the run-closure sequence:
- present the explicit closure prompt asking for approval to write the
  end-of-run summary,
- write `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md` after approval,
- update `notes/output_catalog.md` to reference that summary,
- and then perform the End-of-Run Retrospective Check before declaring the run
  closed.

## Standard Research Flow

1. Register source and select lane.
2. Produce lane-specific source analysis.
3. Run cross-lane applicability detection when the active lane defines one:
   - For the YouTube transcript lane: evaluate the analysis report and cleaned
     transcript for content signals that indicate any of the other five lanes
     are relevant. Record flagged lanes with rationale and confidence level. If
     no signals are detected, record that explicitly. See `PIPELINE_USAGE.md`
     for detection criteria.
   - For the GitHub repo lane: evaluate the repo assessment for workflow and
     operating-model signals that indicate Lane 6 Product Workflow Analysis is
     relevant. Record the Lane 6 result with rationale and confidence level. If
     no Lane 6 signal is detected, record that explicitly.
4. Update `notes/output_catalog.md` with the Phase 1 artifact and any
   cross-lane detection results before generating the Phase 1 completion
   display.
5. Show the Phase 1 completion display in the chat, including Cross-Lane
   Signals and the explicit Phase 2 entry decision. Wait for the human to
   respond to any cross-lane prompt before proceeding.
6. If the human approves one or more cross-lane runs: execute each approved
   lane in sequence, save artifacts to the same run folder, complete the
   verification pass for each new durable artifact, and then update
   `notes/output_catalog.md` using measured metadata after each artifact step.
   Do not proceed to Phase 2 until all approved cross-lane runs are
   complete.
7. If the Phase 2 decision is yes: read target repo guidance first and classify
   applicability using all available run-folder artifacts. Apply the
   multi-source evidence rule.
8. Assign roadmap-fit status.
9. Ask for human approval for one specific recommendation and identifier before
   card drafting. Use the Approval Capture Protocol.
10. If approved with confirmed recommendation name and identifier, run the
    ClickUp card-candidate gate for that one approved recommendation only.
11. Generate a ClickUp-ready draft only if task-card gates pass.
12. For any additional durable artifacts generated in Phases 2 through 4,
    complete the verification pass first and then update
    `notes/output_catalog.md` using measured metadata.
13. If another recommendation is approved, loop back to the human gate for the
    next one-recommendation cycle.
14. If no additional eligible card candidate remains, do not stop at a
    descriptive state update. Present an explicit user-facing closure prompt
    that states the run is ready for closure and asks for approval to write the
    end-of-run summary. Use wording substantially like:

    `No additional eligible ClickUp card candidates remain for this run.`

    `Ready to write the end-of-run summary for: <run/source name>`

    `Please confirm using this format:`

    `  Approved — end-of-run summary`

    If the user does not approve end-of-run summary generation, do not treat
    the run as closed.
    The same closure-prompt requirement also applies when a run ends earlier at
    Phase 1 `stop at catalog-only closure`; do not skip run closure merely
    because later phases were not entered.
15. Before declaring the run complete, write a per-run summary artifact to
    `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md`, measure any
    recorded verification metadata from disk, and update
    `notes/output_catalog.md` so the run summary is referenced as the canonical
    reopening point for the run.
16. Perform the End-of-Run Retrospective Check. If a reusable workflow lesson
    is detected, add or update `notes/lessons_learned.md` before closing the
    run.

## Backlog Publication Bridge

Backlog publication is a separate workflow boundary between:
- completed research runs that produced approved ClickUp-ready draft artifacts
- the FinOpsAI Product Development Workflow, which starts from already
  published backlog items selected into Sprint Backlog

Use this bridge when a ClickUp-ready draft should become a real Product Backlog
Item (PBI).

Purpose:
- publish or create the approved ClickUp card in the correct backlog location
- capture the real ClickUp URL/ID
- preserve Product Owner control over backlog administration
- distinguish "draft candidate created" from "PBI exists in the system of
  record"

Rules:
- Do not treat Phase 4 draft generation as equivalent to publication.
- Do not treat Product Development Sprint intake as the place where a draft is
  first created or normalized.
- Backlog publication may be manual or MCP-assisted, but it remains a governed
  step with explicit owner approval.
- Publication must preserve one approved recommendation to one published PBI.
- If publication is automated later, require destination confirmation,
  duplicate/collision checks, and return of the created ClickUp ID/URL.

Recommended publication record:
- store a concise publication note in the run folder or roadmap-fit artifact
  that records:
  - approved recommendation name
  - approved identifier
  - ClickUp URL/ID when published
  - backlog/list/status destination
  - whether the item is backlog-only or selected for later sprint intake

Boundary:
- Research workflow ends with approved draft candidates and run closure.
- Backlog Publication creates or updates the real PBI.
- Product Development begins when the Product Owner selects existing PBIs into
  Sprint Backlog.

## Chat-Visible Gate Outputs

Durable artifacts remain the system of record, but later workflow gates,
decisions, and approval checks must also be reported in the chat so the run is
auditable without opening every file.

When a later phase or step includes a gate, decision, route selection, or card
authorization check, present the gate result in the chat before or alongside
artifact generation. Keep these outputs concise and decision-oriented.

This chat-visible requirement applies to:
- Phase 1 completion and the secondary lane signal detection result,
- Phase 1 secondary lane prompt and the human's response for each flagged lane,
- Phase 1 completion and the recommendation for whether to continue to Phase 2,
- Phase 2 Step 1 repo-evidence verification,
- Phase 2 Step 2 applicability classification summary,
- Phase 3 Step 1 route selection,
- Phase 3 Step 2 design readiness,
- Phase 4 Step 1 readiness and approval verification,
- Phase 4 Step 2 task-card gate outcomes.

Do not treat artifact creation alone as sufficient evidence that a later gate
was checked.

## Roadmap-Fit Progress Tracking

Every `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` file must start with a
workflow progress tracker before the roadmap-fit status register or any
classification content.

The tracker records which phase and step produced or updated the roadmap-fit
file, which later steps have been run, and which approval-gated steps remain
blocked or not started. Before performing any subsequent workflow step that
touches a roadmap-fit artifact, check the tracker first. After the step is
performed, update the tracker in the same artifact and then update
`notes/output_catalog.md` if the artifact changed.

After each Phase 4 cycle, re-open the roadmap-fit artifact and verify that the
workflow tracker rows and surrounding narrative still agree. If any narrative
section has become stale after card-draft generation or route changes, correct
that artifact before considering the cycle complete, then confirm the catalog
entry reflects the final durable artifact set.

Use these status values:
- `Completed`
- `In progress`
- `Not started`
- `Blocked`
- `Skipped`

Required tracker rows:

| Phase | Step | Status | Completed On | Evidence / Artifact | Notes |
| --- | --- | --- | --- | --- | --- |
| Phase 0 | Step 1: Register source and select lane |  |  |  |  |
| Phase 1 | Step 1: Produce lane-specific source analysis |  |  |  |  |
| Phase 1 | Step 2: Run cross-lane applicability detection (lane-specific) |  |  |  |  |
| Phase 1 | Step 3: Present cross-lane signals in completion display and await human response |  |  |  |  |
| Phase 1 | Step 4: Run Lane 2 GitHub repo assessment (if approved) |  |  |  |  |
| Phase 1 | Step 5: Run Lane 3 business requirement triage (if approved) |  |  |  |  |
| Phase 1 | Step 6: Run Lane 4 accounting domain review (if approved) |  |  |  |  |
| Phase 1 | Step 7: Run Lane 5 product workflow analysis (if approved) |  |  |  |  |
| Catalog | Update `notes/output_catalog.md` before Phase 1 completion display |  |  |  |  |
| Decision | FinOpsAI mapping needed? (yes/no with rationale, reflecting all available artifacts) |  |  |  |  |
| Phase 2 | Step 1: Generate or update FinOpsAI repo mapping from scoped repo evidence |  |  |  |  |
| Phase 2 | Step 2: Classify applicability categories with source and FinOpsAI evidence |  |  |  |  |
| Phase 2 | Step 3: Generate or update roadmap-fit status record |  |  |  |  |
| Phase 3 | Step 1: Ask for and record route decision (approve/route/defer/reject) |  |  |  |  |
| Phase 3 | Step 2: Decide design readiness and route if needed |  |  |  |  |
| Phase 3 | Step 3: Select next artifact and record single-card approval details when applicable |  |  |  |  |
| Decision | ClickUp card needed and approved? (yes/no with exact identifier if yes) |  |  |  |  |
| Phase 4 | Step 1: Run candidate readiness check and approval verification |  |  |  |  |
| Phase 4 | Step 2: Run task-card gates (Request Appropriateness, Information Sufficiency, both-pass) |  |  |  |  |
| Phase 4 | Step 3: Generate one ClickUp-ready draft only if all gates pass |  |  |  |  |
| Loop Decision | Another approved recommendation to process? (yes -> return to Phase 3 Step 1; no -> end run) |  |  |  |  |
| Catalog | Update `notes/output_catalog.md` for durable artifacts from Phases 2–4 |  |  |  |  |
| Run Closure | Write per-run summary artifact and update catalog reference |  |  |  |  |
| Retrospective | End-of-run retrospective check completed; lessons-learned entry added or explicitly not needed |  |  |  |  |

Phase 1 cross-lane rows use lane-specific applicability rules:
- For the YouTube transcript lane, Steps 2–7 apply to any flagged secondary
  lane.
- For the GitHub repo lane, Step 2 and Step 3 apply to the Lane 6 Product
  Workflow Analysis check. Mark Step 4 through Step 6 as `Skipped` unless one
  of those lanes is separately introduced by another source in the same run.
  Use Step 7 when Lane 6 workflow analysis is approved and run.
- For other lanes, mark Steps 2–7 as `Skipped` with a note identifying the
  active lane unless a lane-local rule later defines a cross-lane check.

Phase 2 Step 1 through Step 3 are mandatory rows whenever mapping is run
because they generate and qualify repo-mapping and roadmap-fit outcomes.
Phase 3 rows are mandatory whenever actionable recommendations exist because
they record the governed human decision path before any card candidate work.
Phase 4 rows are mandatory whenever a ClickUp-ready draft is attempted.
The `Run Closure` row is mandatory for every completed run regardless of which
phase the run reaches, because it records the canonical reopening summary.

If a workflow lane uses more detailed local steps, keep these required rows and
add lane-specific rows underneath them. Do not remove blocked Phase 3 or Phase
4 rows just because drafting has not been approved; blocked or not-started
status is part of the durable decision record.

General verification rule:
- The verification metadata discipline in this file applies to every
  artifact-producing step in every phase, including approved secondary-lane
  runs, Phase 2 mapping artifacts, roadmap-fit artifacts, and Phase 4 card
  drafts.
- Line counts and similar metrics are optional unless a lane explicitly
  requires them. When recorded, they must be measured from disk after write and
  before the catalog entry or chat-visible verification note is finalized.

## End-of-Run Retrospective Check

Before the retrospective check, every completed run must first produce one
canonical per-run summary artifact:

- `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md`

This summary is the durable reopening point for the run. Do not make users
infer whether the final disposition lives in a lane artifact, roadmap-fit
artifact, or only in the chat.

Required contents:
- source and lane(s)
- final disposition
- accepted / rejected / deferred recommendations when applicable
- durable artifacts produced
- whether ClickUp-ready drafts were created
- explicit next steps, if any
- concise verification note

Catalog rule:
- update `notes/output_catalog.md` after the run summary is written
- reference the run summary as the canonical reopening point for the run
- keep the catalog entry concise; the run summary holds the fuller recap

Before declaring a run complete, perform a short retrospective check. This
check also applies to terminal stop conditions where the workflow instructs the
agent to stop and inform the user because the run cannot proceed.

Question:
- Did this run expose a reusable workflow lesson?

A reusable workflow lesson exists when at least one of the following is true:
- a durable artifact had to be corrected after initial generation,
- instructions were patched to prevent recurrence,
- the same class of issue occurred more than once,
- a process weakness affected routing, verification, approvals, or artifact
  quality,
- or the lesson has clear reuse value for future workflow harness design.

If no reusable workflow lesson exists:
- close the run normally,
- do not create a lessons-learned entry,
- and state in the final response that no lessons-learned update was needed
  only when that clarification is useful.
- For terminal stop conditions before durable artifact creation, ordinary bad
  input, unavailable sources, or user cancellation do not require a
  lessons-learned entry unless they expose a reusable workflow lesson.

If a reusable workflow lesson exists:
- add or update an entry in `notes/lessons_learned.md`,
- keep the entry concise and reusable,
- reference any impacted instruction files,
- and mention in the final response that a lesson was recorded.

## Phase 1 Completion Display

When Phase 1 source analysis is complete, first complete the verification pass
for every durable artifact written in the phase, then update
`notes/output_catalog.md`, then generate the Phase 1 completion display in the
chat. The catalog update must happen before the completion display is shown so
that the Verification Notes field can confirm the catalog was updated, not mark
it as pending.

Verification metadata discipline:
- Do not estimate or manually count line counts, file sizes, artifact paths, or
  similar verification metadata.
- Derive verification metadata from the saved artifact after the file has been
  written to disk.
- If `notes/output_catalog.md` includes line counts or similar metrics, populate
  them only from measured command output.
- If a verification value has not yet been measured, omit it until the
  verification pass is complete.
- Do not draft or finalize catalog verification metadata from visual inspection
  of the markdown content alone.

Required sequencing:
1. Write or update the durable artifact.
2. Measure verification metadata from disk.
3. Update `notes/output_catalog.md` using the measured values.
4. Generate the Phase 1 completion display in the chat.

The CodeX GUI response must include the decision material directly, before or
alongside the generated file links. This lets the human decide whether to
continue to Phase 2 without opening the full report.

Print the Phase 1 completion content in this order:

1. **Summary**: a concise extract of the report's executive summary or source
   analysis summary.
2. **Phase 2 Decision Takeaways**: the assessment content needed to decide
   whether to proceed to FinOpsAI mapping or another Phase 2 workflow.
3. **Generated Artifacts**: links to the durable files that were created or
   updated.
4. **Cross-Lane Signals** (when the active lane defines a cross-lane check):
   list each flagged lane with its one-sentence rationale and confidence level
   (`Strong signal` or `Weak signal`). If no signals were detected, state that
   explicitly so the human can confirm the check was performed.
   - For the YouTube transcript lane, this may include any of the other four
     lanes.
   - For the GitHub repo lane, this currently means whether Lane 5 Product
     Workflow Analysis should run before Phase 2.
   For each flagged lane, ask the human whether to run that lane before
   proceeding to Phase 2. Wait for the human's response before continuing. If
   no cross-lane signals were detected, this item confirms the check and no
   prompt is needed.
5. **Proceed / Stop Recommendation**: an explicit recommendation to proceed to
   the next Phase 2 workflow or stop at catalog-only closure. Apply the Phase
   2 Entry Decision criteria above to make this decision. This recommendation
   reflects the full set of available evidence including any approved
   secondary lane runs that have been completed.
6. **No-Go Rationale** (required when the Proceed / Stop Recommendation is to
   stop or otherwise not proceed): a topic-specific explanation of why the
   source does not currently justify advancing into the next Phase 2 workflow.
   This section must explain the no-go decision directly rather than hiding the
   reason inside the recommendation line or the next-action line.
7. **Recommended Next Action**: the specific next step to take, such as
   FinOpsAI repo mapping, GitHub repo assessment, another approved workflow, or
   no further action yet.
8. **Verification Notes**: brief checks such as source validation, measured
   line counts when recorded, catalog update status (must confirm updated, not
   pending), cross-lane detection confirmation, and whether optional Phase 2 or
   card-drafting work was not run.

Conditional section-count rule:
- When the Proceed / Stop Recommendation is to proceed, `No-Go Rationale` is
  omitted and the display contains 7 sections.
- When the Proceed / Stop Recommendation is not to proceed, `No-Go Rationale`
  is required between `Proceed / Stop Recommendation` and
  `Recommended Next Action`, and the display contains 8 sections.

Decision-surface separation rule:
- Keep these three surfaces distinct in the chat output:
  - `Cross-Lane Signals` answers whether another lane is relevant.
  - `Proceed / Stop Recommendation` answers whether to enter Phase 2 now or
    stop at catalog-only closure.
  - `No-Go Rationale` answers why the recommendation is not to proceed when
    the recommendation is a stop/no-go.
  - `Recommended Next Action` answers what the human should do next, which may
    be a cross-lane approval rather than a Phase 2 action.
- Do not let a cross-lane signal be restated as though it were already the
  same thing as a Phase 2 recommendation or an approval-ready next step.
- Do not collapse the no-go explanation into `Recommended Next Action` when
  the workflow is stopping. Use the dedicated `No-Go Rationale` section.
- If the user constrained the available choices to a narrower set than the full
  workflow, say so explicitly. Prefer wording such as:
  - `Among the requested options (...) the recommendation is: ...`
  - `Outside that constrained option set, the strongest workflow next step is:
    ...`
- If a cross-lane workflow is the strongest next step, and the constrained
  option set excludes it, the response must explicitly state both facts rather
  than collapsing them into one recommendation.

Approval-readiness rule:
- Only offer `Approved — <lane/action>` prompts for actions that are actually
  valid and sufficiently specified to run next.
- Do not offer `Approved — Lane 2 GitHub repo assessment` unless there is a
  concrete target repo that can be named in the same response:
  - a user-supplied GitHub URL,
  - a local repo path supplied by the user,
  - or a clearly identified cited repo that the response explicitly proposes as
    the assessment target.
- A vague spoken repo mention, an inferred repo identity, or a transcript-only
  reference without a confirmed target is not enough to surface Lane 2 as an
  approval-ready next action.

Recommendation clarity rule:
- When the recommendation is `no further action yet`, the GUI response must
  name the specific source topic explicitly and explain why that topic should
  stop at catalog-only closure for now.
- The explanation must be topic-specific rather than generic. It should state
  why the topic does not currently justify FinOpsAI repo mapping, GitHub repo
  assessment, or ClickUp card-candidate drafting.
- Prefer wording such as: "`<topic>` is not recommended for further action yet
  because ..." followed by the concrete evidence gap, weak applicability, or
  insufficient implementation value.

Do not advance into Phase 2 until this completion display has been shown in the
chat and the proceed-or-stop recommendation is explicit.

If the recommendation is `stop at catalog-only closure` and the human accepts
that recommendation, the next chat-visible step must be the explicit
run-closure prompt for end-of-run summary approval. Do not end the run from
the Phase 1 completion display alone.

For transcript analysis reports, use these sections as the default source for
the GUI display:

- Summary: `Executive Summary`.
- Phase 2 Decision Takeaways: `What Seems Practically Useful`,
  `What Seems Aspirational, Fragile, or Hype-Prone`, and
  `Practical Takeaways for a Software / AI Product Leader`.

Keep the GUI display concise and referential. Do not paste the full report,
full transcript, or long excerpts. If the relevant source report uses different
section names, extract the closest equivalent summary, applicability,
practical-use, caveat, and next-step content.

## Phase 2 Chat Output Requirements

Before starting Phase 2 Step 1 repo-evidence review, print a concise
`Phase 2 Step 1 Gate Result` in the chat that confirms:
- the current phase and step,
- the prerequisite source analysis is complete,
- the roadmap-fit tracker is present and current when applicable,
- the target artifact path for the mapping or update is confirmed.

Repo scope rule for Phase 2:
- Do not review the entire FinOpsAI repo by default.
- Start with repo guidance first.
- For Lane 6 Product Workflow Analysis, begin with
  `/Users/Sites/Repo-FinOpsAI/docs/engineering/` and other obviously relevant
  workflow/process docs.
- Expand only when needed to enforcement surfaces such as CI workflows,
  automation scripts, prompt/agent/harness files, templates, checklists, and
  then representative tests or source modules.
- Stop widening the search once the applicability claim is grounded.

After Phase 2 Step 2 classification work, print a concise
`Phase 2 Classification Summary` in the chat that covers:
- immediate fits,
- process-change fits,
- architecture or design-dependent fits,
- rejected or poor-fit ideas.

These summaries are not a replacement for the durable artifacts. They are the
operator-visible checkpoint that shows classification happened before route or
approval handling.

## Phase 3 Chat Output Requirements

Before continuing past Phase 3 Step 1, print a concise `Route Result` in the
chat that states:
- the selected route,
- the recommendation set covered by that route decision,
- why the route is correct,
- whether ClickUp card drafting remains blocked or can continue toward Phase 4.

Before continuing past Phase 3 Step 2, print a concise `Design Readiness
Result` in the chat that states:
- `Product Design required: Yes` or `Product Design required: No`,
- a one-sentence rationale,
- the next artifact implication if design work is still required.

When a Phase 3 outcome leaves the run at a process-approval gate but one
recommendation is concrete enough to continue later as a single ClickUp-ready
draft candidate, the chat output must not stop at a generic "choose one"
instruction. Instead:
- name the exact recommendation that is eligible to continue,
- provide one recommended draft filename identifier,
- and repeat the exact approval format the user should use.

Use this handoff template:

```text
Ready to draft a ClickUp card for: <recommendation name>
Suggested identifier: <identifier>

Please confirm using this format:
  Approved — identifier: <identifier>
```

If more than one recommendation is eligible, present one recommendation at a
time with its own suggested identifier. Do not leave the next action implicit.
After one approved candidate completes Phase 4 draft generation, if additional
eligible recommendations remain in the same run, immediately present the next
candidate using the same structured handoff format instead of falling back to a
generic follow-up. The next-candidate handoff must read substantially like:

```text
Ready to draft the next ClickUp card for: <recommendation name>
Suggested identifier: <identifier>

Please confirm using this format:
  Approved — identifier: <identifier>

If you want a different identifier, send the same format with your preferred identifier.
```

When more than one candidate remains, still present only one next candidate at
a time. Do not batch multiple recommendations into one approval prompt.

## Phase 4 Chat Output Requirements

Before Phase 4 Step 1 writes any ClickUp-ready draft artifact, print a concise
`Phase 4 Readiness Result` in the chat that confirms:
- the exact approved recommendation,
- the exact approved identifier,
- one-primary-task scope,
- the ClickUp draft collision check passed.

Before or alongside Phase 4 Step 2 drafting decisions, print both of these
labels in the chat:
- `Request Check Result`
- `Information Check Result`

Do not rely on the generated ClickUp draft file alone to communicate these gate
results. The chat transcript must show them explicitly before or alongside
draft generation.

## Boundary Rules

- Research and assessment are not implementation.
- Do not modify FinOpsAI during repo mapping unless explicitly asked.
- Do not modify generated outputs unless regenerating or revising them by request.
- Do not create external service calls, hidden dependencies, or automations as part of this workflow.
- If evidence is insufficient, state the gap rather than guessing.
- Preserve the difference between product features, process changes, AI integration ideas, architecture changes, engineering practices, and deferred research.
