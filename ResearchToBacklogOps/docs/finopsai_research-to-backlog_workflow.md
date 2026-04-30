# Research-to-Backlog Human Workflow

<!-- MAINTENANCE NOTE: This markdown is the textual reference companion to
finopsai_research-to-backlog_workflow.html. RESEARCH_WORKFLOW_USAGE.md is the
canonical control document. When this file and the HTML diverge from
RESEARCH_WORKFLOW_USAGE.md, RESEARCH_WORKFLOW_USAGE.md governs. After any
update to RESEARCH_WORKFLOW_USAGE.md or this file, review the HTML for
accuracy. -->

Visual companion source:
- `finopsai_research-to-backlog_workflow.html`

Controlling workspace guides:
- `RESEARCH_WORKFLOW_USAGE.md` — canonical authority for source routing,
  artifact naming, repo-mapping categories, roadmap-fit statuses, chat-visible
  gate outputs, and the ClickUp card-candidate gate.
- `PIPELINE_USAGE.md` — YouTube transcript lane mechanics, secondary lane
  signal detection, acquisition scripts, and run-folder naming.
- `AGENTS.md` — workspace-scoped behavior and lane skill selection. Defers to
  `RESEARCH_WORKFLOW_USAGE.md` on all shared harness decisions.

Both the HTML and this markdown are controlled by `RESEARCH_WORKFLOW_USAGE.md`.

---

## Workflow Usage

CodeX is the primary interface for registering sources, selecting lanes,
producing research artifacts, mapping ideas to FinOpsAI, assigning roadmap-fit
status, and drafting ClickUp-ready card candidates.

Use another tool only when that tool owns the action:
- ClickUp for publishing cards.
- A browser or Git tooling for approved external repo or source access.
- FinOpsAI workflow docs for Product Design and Product Development handoff.

Implemented guide: `RESEARCH_WORKFLOW_USAGE.md` is the controlling workspace
guide for source taxonomy, routing, artifact names, repo-mapping categories,
roadmap-fit statuses, and the ClickUp card-candidate gate.

Separate lanes: each source type keeps its own intake rules and risk checks so
transcripts, GitHub repos, domain content, requirements, and workflow material
are not forced through the same analysis path.

If the source is only a transcript cleanup request, use the transcript pipeline
directly through `PIPELINE_USAGE.md`.

---

## Decision Summary

Avoid one generalized pipeline because it hides source-specific risk and can
turn weak research into premature backlog items.

Implemented: a research usage guide centered on `RESEARCH_WORKFLOW_USAGE.md`.
The shared standards live there; the HTML workflow is the visual operational
view of those rules.

---

## Harness Map

Common harness responsibilities:
- source taxonomy
- routing table
- artifact naming
- catalog discipline
- repo-mapping categories
- roadmap-fit statuses
- ClickUp card-candidate gate
- standard research flow
- boundary rules

Lanes:

1. **Lane 1: YouTube transcript intake**
   - Acquire, clean, analyze, detect secondary lane signals, then optionally
     run approved secondary lanes and map to FinOpsAI.
   - Output: cleaned transcript + analysis report; optional secondary lane
     artifacts; optional mapping.

2. **Lane 2: GitHub repo intake**
   - Assess external architecture, patterns, tooling, tests, and compatibility.
   - Then check whether Lane 5 workflow analysis should run before any mapping.
   - Output: repo assessment; optional workflow-analysis follow-on; optional mapping.

3. **Lane 3: Business requirement intake**
   - Turn raw Product Owner intent into scoped triage or design workflow routing.
   - Output: requirement triage.

4. **Lane 4: Accounting domain intake**
   - Review bookkeeping, tax, reconciliation, reporting, and compliance material.
   - Output: domain analysis/applicability; optional mapping.

5. **Lane 5: Workflow content intake**
   - Separate process improvements from product features and harness tooling.
   - Output: workflow analysis/applicability; optional mapping.

---

## Phase Navigation

| Phase | Label |
| --- | --- |
| Phase 1 | Intake And Analyze |
| Phase 2 | Map To FinOpsAI Applicability |
| Phase 3 | Human Roadmap And Workflow Gate |
| Phase 4 | Card Candidate |

Bridge after research completion:
- Backlog Publication / PBI Administration
  - owner: Product Owner by default
  - system of record: ClickUp
  - purpose: turn an approved ClickUp-ready draft into a real backlog item
  - boundary: separate from research drafting and separate from Sprint Backlog
    selection in Product Development Step 1

---

## Standard Research Flow

1. Register source and select lane.
2. Produce lane-specific source analysis.
3. Run cross-lane applicability detection when the active lane defines one.
   - For Lane 1 transcripts, use the transcript secondary-lane rules.
   - For Lane 2 GitHub repos, check whether Lane 5 workflow analysis is
     relevant based on workflow, orchestration, or operating-model evidence in
     the repo assessment.
4. Update `notes/output_catalog.md` with the Phase 1 artifact and any
   cross-lane detection results before generating the Phase 1 completion display.
5. Show the Phase 1 completion display in the chat, including Cross-Lane
   Signals and the explicit Phase 2 entry decision. Wait for the human to
   respond to the cross-lane prompt before proceeding.
6. If the human approves one or more cross-lane runs: execute each approved
   lane in sequence, save artifacts to the same run folder, complete the
   verification pass for each new durable artifact and measure verification
   metadata from disk before updating the catalog, then update
   `notes/output_catalog.md` using the measured values after each artifact
   step. Do not proceed to Phase 2 until all approved cross-lane runs are
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
    complete the verification pass first, measure verification metadata from
    disk, and then update `notes/output_catalog.md` using the measured values.
13. If another recommendation is approved, loop back to the human gate for the
    next one-recommendation cycle.
14. Before declaring the run complete, write
    `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md` as the canonical
    reopening summary for the run, then update `notes/output_catalog.md`.
15. Perform the End-of-Run Retrospective Check and record any reusable lesson
    in `notes/lessons_learned.md` when needed.

If a run stops earlier at Phase 1 with a `catalog-only closure` decision and
the human accepts that recommendation, do not treat the recommendation
acceptance as completed closure. The workflow must still transition through the
same run-closure sequence: ask for approval to write the end-of-run summary,
write the run summary artifact, update the catalog, and then perform the
retrospective check.

Research workflow boundary:
- Research ends with approved ClickUp-ready draft artifacts, not published PBIs.
- A separate Backlog Publication bridge may later publish those drafts into
  ClickUp manually or via MCP.
- FinOpsAI Product Development Step 1 starts from already published PBIs that
  the Product Owner selects into Sprint Backlog.

---

## Workflow Phases

---

## Bridge: Backlog Publication

Purpose and scope:
- This bridge turns an approved ClickUp-ready draft into a real Product Backlog
  Item in ClickUp.
- It is not part of research analysis and not part of Product Development
  Sprint intake.
- It preserves Product Owner control over backlog administration while allowing
  future MCP-assisted publication when explicitly authorized.

Core actions:
1. confirm the exact approved draft artifact and identifier
2. confirm destination backlog/list/status
3. publish or create the ClickUp item
4. record the created ClickUp URL/ID
5. note whether the item is backlog-only or later selected into Sprint Backlog

Rules:
- do not auto-publish simply because a Phase 4 draft exists
- do not combine multiple approved drafts into one PBI
- if MCP publication is used later, require duplicate checks and destination
  confirmation before create/update
- keep publication/admin ownership distinct from Product Development Step 1,
  which selects existing PBIs into Sprint Backlog rather than creating them

Recommended durable record:
- store the publication result in the run’s canonical summary or roadmap-fit
  artifact, including the ClickUp URL/ID and backlog destination

---

## Phase 1: Intake And Analyze

Purpose and scope:
- Phase 1 begins with intake and routing, then continues into lane-specific
  source analysis.
- Intake and routing establish the operating boundary for the run. They include
  source capture, lane selection, expected artifact naming, and workflow
  boundary confirmation before durable analysis begins.
- Lane analysis includes transcript cleanup plus analysis when applicable, repo
  or source assessment, requirement triage, domain review, or workflow analysis.
- For the YouTube transcript lane, Phase 1 also includes secondary lane signal
  detection and any approved secondary lane runs before the Phase 2 decision.
- It does not assess FinOpsAI applicability, assign roadmap-fit status, or
  generate ClickUp-ready drafts.

Implemented rule: start from the source taxonomy in `RESEARCH_WORKFLOW_USAGE.md`.
The first decision is source type and lane, not the final output.

---

### Step 1: Intake And Routing

Required intake substeps:
- Capture source metadata.
- Select lane.
- Set expected artifact.
- Confirm boundary rules.

#### Step 1A: Capture source metadata

Record:
- source path or URL
- source type
- date
- intended question
- target FinOpsAI area
- whether network access or repo cloning is needed
- chat title metadata when the run uses a CodeX UI or automation hook

Required fields:
- **Source:** URL, local file path, local repo path, or raw requirement text.
- **Source type:** YouTube transcript, GitHub repository, business requirement,
  accounting/bookkeeping content, or product workflow content.
- **Purpose:** source analysis, FinOpsAI mapping, roadmap fit, or card-candidate
  readiness.
- **Target area:** relevant FinOpsAI product, codebase, workflow, docs,
  accounting domain, or ClickUp area if known.
- **Access needs:** whether CodeX needs network access, an external repo clone,
  a local file, or a target repo read.
- **Chat Title Mode:** `auto`, `manual`, or `none` when UI or automation naming
  is in use.
- **Chat Title Template:** the thread-title template the CodeX UI or automation
  layer should apply.
- **Chat Timezone:** use `America/Los_Angeles` unless the user explicitly
  overrides it.

Rule: if any required source detail is missing, record the gap and ask for it
before producing durable artifacts.

Chat-title implementation rule:
- Chat-title metadata is for the CodeX UI or automation layer, not for artifact
  naming.
- When `Chat Title Mode` is `auto`, the UI or automation layer should set the
  chat title at thread creation or the earliest available run-start hook.
- The workflow agent may derive title inputs, but the UI or automation layer
  owns the actual chat-title update.
- If no UI or automation rename hook exists, continue the workflow without
  treating chat naming as a blocker.

Recommended metadata block:
```text
Chat Title Mode: auto
Chat Title Template: <lane> | <source_title> | <run_date_pacific>
Chat Title Source Priority: source_title -> local_filename -> user_supplied_label
Chat Timezone: America/Los_Angeles
Chat Title Max Length: 120
```

Lane defaults:
- YouTube transcript: `Transcript | <source_title> | <run_date_pacific>`
- GitHub repo assessment: `Repo Assessment | <repo_name> | <run_date_pacific>`
- Business requirement: `Requirement | <short_requirement_topic> | <run_date_pacific>`
- Accounting or domain review: `Domain Review | <topic> | <run_date_pacific>`
- Product workflow analysis: `Workflow Analysis | <topic> | <run_date_pacific>`

#### Step 1B: Select lane

Route as follows:

| Source | Lane | First Artifact |
| --- | --- | --- |
| YouTube URL, VTT file, or raw transcript | YouTube transcript lane | Cleaned transcript + analysis report |
| External GitHub repo or local clone | GitHub repository lane | GitHub repo assessment |
| Raw Product Owner or stakeholder request | Business requirement lane | Requirement triage report |
| Accounting, bookkeeping, finance, tax, reconciliation, reporting, compliance, or advisory content | Accounting/bookkeeping domain lane | Domain analysis report |
| Product development, human-in-the-loop, agentic workflow, backlog refinement, QA, review, or delivery material | Product development workflow lane | Workflow analysis report |

Routing guardrail:
- Do not use transcript cleanup for non-transcript sources.
- If one source contains multiple independent work items, split or triage before
  mapping to ClickUp candidates.

#### Step 1C: Set expected artifact

Create one run folder per source run: `output/<n>_YYYY_MM_DD/`

Use the date of the first durable artifact for the run as the folder date. Keep
later-phase files in the same folder even if their file date is later.

| Artifact need | Naming pattern |
| --- | --- |
| Transcript cleanup | `output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt` |
| Transcript analysis | `output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md` |
| General source analysis | `output/<n>_YYYY_MM_DD/<n>_source_analysis_YYYY_MM_DD.md` |
| GitHub repo assessment | `output/<n>_YYYY_MM_DD/<n>_github_repo_assessment_YYYY_MM_DD.md` |
| Domain analysis | `output/<n>_YYYY_MM_DD/<n>_domain_analysis_YYYY_MM_DD.md` |
| Domain applicability | `output/<n>_YYYY_MM_DD/<n>_domain_applicability_YYYY_MM_DD.md` |
| Workflow analysis | `output/<n>_YYYY_MM_DD/<n>_workflow_analysis_YYYY_MM_DD.md` |
| Workflow applicability | `output/<n>_YYYY_MM_DD/<n>_workflow_applicability_YYYY_MM_DD.md` |
| Requirement triage | `output/<n>_YYYY_MM_DD/<n>_requirement_triage_YYYY_MM_DD.md` |
| Repo mapping | `output/<n>_YYYY_MM_DD/<n>_repo_mapping_YYYY_MM_DD.md` |
| Roadmap fit | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` |
| Run summary | `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md` |
| Deferred and rejected outcomes | Record in `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` by default; split into exception artifacts only when volume or separate review justifies it. |
| ClickUp-ready draft | `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md` |

ClickUp-ready draft suffix rule: every draft must append a concise descriptive
identifier before `.md`. The identifier must distinguish the work item clearly
enough to avoid overwriting an earlier approved draft.

Catalog rule: update `notes/output_catalog.md` after generated research runs
that produce durable artifacts. Keep entries concise and referential.

#### Step 1D: Confirm boundary rules

| Boundary | Instruction |
| --- | --- |
| Assessment only | Research and mapping do not modify FinOpsAI unless the user explicitly asks for implementation. |
| Target repo guidance | When FinOpsAI mapping is needed, read `/Users/Sites/Repo-FinOpsAI/AGENTS.md` first. |
| Accounting controls | Preserve deterministic validation, review, approval, posting, credential, dependency, privacy, and testing constraints. |
| External access | Use CodeX by default. Use network, browser, Git tooling, or ClickUp only when that tool owns the action and access is approved. |
| Evidence gaps | If source or repo evidence is insufficient, state the gap instead of guessing. |
| Card drafting | Research output creates card candidates only. Generate ClickUp-ready drafts only after the card-candidate gate passes. |

Phase 1 Step 1 pass gate:
- The source is registered.
- The lane is selected.
- The expected artifact is known.
- Boundary rules are clear.
- If any are missing, pause and clarify before moving to Phase 1 Step 2.

---

### Step 2: Run Lane-Specific Source Analysis

Purpose and scope:
- Step 2 produces the source-facing analysis artifact for the selected lane.
  It includes transcript cleanup plus analysis when applicable, repo or source
  assessment, requirement triage, domain review, or workflow analysis.
- It does not decide FinOpsAI mapping by default, assign roadmap-fit status, or
  generate backlog or task-card artifacts unless a later phase explicitly runs.

Implemented rule: produce lane-specific source analysis before deciding whether
FinOpsAI mapping is needed.

---

### Lane 1: YouTube Transcript

Rule: clean first, then analyze. Preserve source files and timestamps unless
explicitly changed.

Prompt example:
```text
Use CodeX as the interface and follow RESEARCH_WORKFLOW_USAGE.md and PIPELINE_USAGE.md.

Phase 0: Register this source and confirm lane selection before proceeding.
Lane: YouTube Transcript

Chat Title Mode: auto
Chat Title Template: Transcript | <source_title> | <run_date_pacific>
Chat Timezone: America/Los_Angeles

Source:
<YouTube URL, .vtt file, or raw transcript path>

Instructions:
1. If this is a YouTube URL, validate it before acquisition.
2. If acquisition is needed, use the transcript pipeline and preserve source
   files in input/.
3. Clean the transcript without summarizing or analyzing during cleanup.
4. Preserve timestamps unless I explicitly ask to remove them.
5. Correct only high-confidence transcription defects. If uncertain, preserve
   the original wording.
6. Create the run folder as output/<n>_YYYY_MM_DD/.
7. Save the cleaned transcript to output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt.
8. Generate the transcript analysis report to output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md.
9. Run secondary lane signal detection: evaluate the analysis report and cleaned
   transcript for content signals indicating any of the other four lanes are
   relevant. For each lane evaluated, record a confidence level of Strong signal
   or Weak signal, or confirm no signal detected. Do not run any secondary lane
   during this step.
10. Update notes/output_catalog.md with the Phase 1 artifact and secondary lane
    detection results before generating the Phase 1 completion display.
11. Present the Phase 1 completion display in the chat using the 7-item format
    in RESEARCH_WORKFLOW_USAGE.md. Include Secondary Lane Signals as item 4.
    For each flagged lane, ask whether to run that lane before Phase 2 begins.
    Wait for my response before proceeding.
12. After I confirm which secondary lanes to run (if any), run each approved
    lane in sequence, save artifacts to the same run folder, and update
    notes/output_catalog.md after each.
13. Then apply the Phase 2 entry decision from RESEARCH_WORKFLOW_USAGE.md.
    Ask before running FinOpsAI repo mapping or ClickUp card-candidate drafting.
```

---

### Lane 2: GitHub Repo Assessment

Rule: assess architecture, patterns, dependencies, tests, docs, and
license/security concerns before mapping. Include a final applicability
recommendation with cited rationale before any repo mapping decision.

Prompt example:
```text
Use CodeX as the interface and follow RESEARCH_WORKFLOW_USAGE.md.

Phase 0: Register this source and confirm lane selection before proceeding.
Lane: GitHub Repository

Source repo:
<GitHub URL or local clone path>

Assessment question:
<patterns, architecture, tooling, workflow, tests, AI integration, or other focus>

Instructions:
1. Record repo source, branch or commit if known, and access needs.
2. Inspect only the files needed to answer the assessment question.
3. Identify repo purpose, architecture, reusable patterns, dependencies, tests,
   docs, and license/security concerns when evidence is available.
4. Distinguish reusable ideas from code reuse; do not copy code or recommend
   reuse without explicit review.
5. Include an Applicability Recommendation section in the artifact that states:
   - applicability level: High applicability, Moderate applicability,
     Low applicability, or Reference only
   - next-step recommendation: Proceed to FinOpsAI repo mapping, Do not proceed
     yet, or No further action
   - cited rationale grounded in concrete repo evidence and caveats
6. Save a GitHub repo assessment artifact to
   output/<n>_YYYY_MM_DD/<n>_github_repo_assessment_YYYY_MM_DD.md.
7. After the repo assessment, check whether Lane 5 Product Workflow Analysis
   should run before any Phase 2 mapping. Record `Strong signal`,
   `Weak signal`, or no Lane 5 signal detected, with rationale grounded in the
   repo evidence.
8. Surface the recommendation, rationale, and Lane 5 check explicitly in the
   user-facing response after the assessment.
9. Do not start FinOpsAI repo mapping unless I explicitly approve.
```

---

### Lane 3: Product Requirement Triage

Rule: normalize raw Product Owner intent into one work item, or route to design
if product definition is incomplete.

Prompt example:
```text
Use CodeX as the interface and follow RESEARCH_WORKFLOW_USAGE.md.

Phase 0: Register this source and confirm lane selection before proceeding.
Lane: Business Requirement

Raw requirement:
<Product Owner request, stakeholder request, feature idea, or workflow pain point>

Instructions:
1. Identify the core requirement, expected outcome, user/business context, and
   affected FinOpsAI area.
2. Determine whether this is one primary work item or must be split.
3. Identify known in-scope and out-of-scope boundaries.
4. Decide whether Product Design Workflow is required before Product Development.
5. Produce a requirement triage artifact to
   output/<n>_YYYY_MM_DD/<n>_requirement_triage_YYYY_MM_DD.md.
6. Do not draft a ClickUp-ready card unless the card-candidate gate and
   FinOpsAI task-card gates can pass.
```

---

### Lane 4: Accounting Domain Review

Rule: capture jurisdiction, user profile, domain reliability, compliance
caveats, and product relevance.

Prompt example:
```text
Use CodeX as the interface and follow RESEARCH_WORKFLOW_USAGE.md.

Phase 0: Register this source and confirm lane selection before proceeding.
Lane: Accounting Domain Review

Domain source:
<article, transcript, guidance, SOP, notes, or documentation>

Domain focus:
<accounting, bookkeeping, tax, reconciliation, reporting, compliance, advisory,
or finance operations>

Instructions:
1. Identify source type, domain area, jurisdiction if relevant, intended user
   profile, and reliability caveats.
2. Separate domain education from product feature ideas.
3. Identify compliance, auditability, review, and roadmap risks.
4. Map only high-confidence product-relevant ideas to FinOpsAI.
5. Do not convert tax, compliance, or accounting advice into implementation
   tasks without human approval and appropriate professional review.
6. Save a domain analysis or domain applicability artifact to
   output/<n>_YYYY_MM_DD/<n>_domain_analysis_YYYY_MM_DD.md or
   output/<n>_YYYY_MM_DD/<n>_domain_applicability_YYYY_MM_DD.md.
```

---

### Lane 5: Product Workflow Analysis

Rule: separate process changes from product features and identify whether the
idea affects human workflow, agent-assisted workflow, or both.

Prompt example:
```text
Use CodeX as the interface and follow RESEARCH_WORKFLOW_USAGE.md.

Phase 0: Register this source and confirm lane selection before proceeding.
Lane: Product Workflow Analysis

Workflow source:
<process article, transcript, prompt, delivery practice, QA practice, backlog
refinement material, or agentic workflow source>

Instructions:
1. Identify whether the idea affects the current human workflow, future
   agent-assisted workflow, or both.
2. Separate process improvements from product features.
3. Classify possible outputs as docs, process, harness tooling, prompt updates,
   QA gates, or deferred notes.
4. Compare against FinOpsAI Product Design and Product Development workflow docs
   when relevant.
5. For any FinOpsAI repo-grounded follow-on, search progressively:
   start with root `AGENTS.md`, nested `AGENTS.md` in relevant areas, and
   `docs/engineering/`; widen to CI, automation, prompt/harness files,
   templates, tests, or representative source only when needed.
6. Do not change ClickUp workflow, prompts, QA gates, or operating model without
   process owner approval.
7. Save a workflow analysis or workflow applicability artifact to
   output/<n>_YYYY_MM_DD/<n>_workflow_analysis_YYYY_MM_DD.md or
   output/<n>_YYYY_MM_DD/<n>_workflow_applicability_YYYY_MM_DD.md.
```

---

Shared standard: every lane records source evidence, caveats, risks, candidate
ideas, and confidence before repo mapping or card drafting.

---

### Secondary Lane Signal Detection (YouTube Transcript Lane Only)

After producing the analysis report, evaluate the transcript content against
the characteristics of all five harness lanes. This is a content assessment,
not a structural link scan. See `PIPELINE_USAGE.md` for full detection criteria.

Evaluate each lane in turn:

- **Lane 2 — GitHub repository:** Does the transcript discuss a specific
  external repository, its architecture, patterns, tooling, tests, or workflows
  in enough depth to warrant a repo assessment? Also check for a concrete
  repository URL or name. Flag Lane 2 if either a content signal or a
  structural reference is present.

- **Lane 3 — Business requirement:** Does the transcript contain a raw product
  requirement, feature idea, stakeholder request, or workflow pain point stated
  as a concrete ask? Flag Lane 3 when the speaker articulates something that
  could be triaged as a product requirement.

- **Lane 4 — Accounting and bookkeeping domain:** Does the transcript discuss
  accounting, bookkeeping, finance operations, tax, reconciliation, reporting,
  compliance, or advisory content in a way that may be product-relevant to
  FinOpsAI? Flag Lane 4 only when domain content could influence FinOpsAI
  product behavior, compliance posture, or feature design.

- **Lane 5 — Product development workflow:** Does the transcript discuss
  product development process, human-in-the-loop workflow, agentic delivery
  practices, backlog refinement, specification, QA, review processes, or
  ClickUp workflow ideas in a way that could affect the current or future
  FinOpsAI operating model? Flag Lane 5 when the content goes beyond general
  process discussion and touches practices applicable to this team.

For each flagged lane, record:
- lane number and name
- one-sentence rationale grounded in specific transcript content
- confidence level: `Strong signal` or `Weak signal`

Only flag lanes where there is genuine content evidence. If no secondary lane
signals are detected, state that explicitly. Do not run any secondary lane
analysis during this step — detection only. The human decides whether to
proceed with any flagged lane before the Phase 2 entry decision is made.

---

### Phase 1 Completion Display

After secondary lane signal detection is complete, complete the verification
pass for all durable artifacts written in Phase 1, then update
`notes/output_catalog.md`, then generate the Phase 1 completion display in
the chat. The catalog update must happen before the completion display is
shown so that Verification Notes can confirm the update is complete, not
pending.

Verification metadata discipline:
- Do not estimate or manually count line counts, file sizes, artifact paths,
  or similar verification metadata.
- Derive verification metadata from the saved artifact after the file has been
  written to disk.
- Populate any catalog line counts or similar metrics only from measured
  command output.
- If a verification value has not yet been measured, omit it until the
  verification pass is complete.
- Do not draft or finalize catalog verification metadata from visual inspection
  of the markdown content alone.
- Full authority for verification metadata discipline is in
  `RESEARCH_WORKFLOW_USAGE.md` Phase 1 Completion Display.

Print the Phase 1 completion content in this order:

**1. Summary**
A concise extract of the report's executive summary or source analysis summary.
For transcript analysis reports, draw from the `Executive Summary` section.

**2. Phase 2 Decision Takeaways**
The assessment content needed to decide whether to proceed to FinOpsAI mapping
or another Phase 2 workflow. For transcript reports, draw from:
- `What Seems Practically Useful`
- `What Seems Aspirational, Fragile, or Hype-Prone`
- `Practical Takeaways for a Software / AI Product Leader`

**3. Generated Artifacts**
Links to the durable files that were created or updated.

**4. Cross-Lane Signals** (when the active lane defines a cross-lane check)
List each flagged lane with its one-sentence rationale and confidence level.
For the GitHub repo lane, this currently means whether Lane 5 Product Workflow
Analysis should run before Phase 2 begins. For each flagged lane, ask the
human whether to run that lane before Phase 2 begins. Wait for the human's
response before continuing. If no cross-lane signals were detected, state that
explicitly to confirm the check was performed.

**5. Proceed / Stop Recommendation**
An explicit recommendation to proceed to Phase 2 or stop at catalog-only
closure. Apply the Phase 2 Entry Decision criteria from
`RESEARCH_WORKFLOW_USAGE.md`. This recommendation reflects all available
evidence including any approved secondary lane runs that have been completed.

**6. Recommended Next Action**
The specific next step: FinOpsAI repo mapping, a cross-lane run, another
approved workflow, or no further action yet.

**7. Verification Notes**
Brief checks: source validation, line counts, catalog update status (must
confirm updated, not pending), cross-lane detection confirmation, and
whether optional Phase 2 or card-drafting work was not run.

Decision-surface separation rule:
- Keep `Cross-Lane Signals`, `Proceed / Stop Recommendation`, and
  `Recommended Next Action` distinct in the chat-visible output.
- If the user gave a constrained option set, state the recommendation within
  that set separately from the strongest workflow next step outside that set.
- Do not let a cross-lane signal read like it is already a Phase 2
  recommendation or an approval-ready next action.
- Do not offer a GitHub repo assessment as approval-ready unless the target
  repo is concretely identified in the same response.

Phase 1 completion chat template:
```text
Phase 1 Completion
- Summary: <concise source-analysis summary>
- Phase 2 Decision Takeaways: <why to proceed or stop>
- Generated Artifacts: <durable artifact path(s)>
- Cross-Lane Signals: <flagged lanes with rationale and confidence, or
  "No cross-lane signals detected — check performed">
  <For each flagged lane: "Proceed with Lane N [name]? Yes / No">
- Proceed / Stop Recommendation: <proceed to Phase 2 OR stop at catalog-only,
  with reason>
- Recommended Next Action: <Phase 2 mapping, cross-lane run, another
  workflow, or stop>
- Verification Notes: <source validation, catalog status, cross-lane check,
  and other brief checks>
```

Recommendation clarity rule: when the recommendation is `no further action
yet`, name the specific source topic and explain why that topic should stop at
catalog-only closure. The explanation must be topic-specific, not generic.

If the recommendation is `stop at catalog-only closure` and the human accepts
that recommendation, the next chat-visible step must be the explicit
run-closure prompt for end-of-run summary approval. Do not end the run from
the Phase 1 completion display alone.

Do not advance into any secondary lane run or Phase 2 until the completion
display has been shown and the human has responded to each flagged lane prompt.

---

### Phase 1 Step 2 Pass Gate

- Lane artifact saved with the expected naming pattern.
- Source summary, caveats, and confidence captured in the lane artifact and
  Phase 1 completion display.
- Secondary lane signal detection completed and result recorded.
- Human has responded to the secondary lane prompt (YouTube transcript lane only).
- Any approved secondary lane runs are complete and artifacts are saved.
- `notes/output_catalog.md` updated before the completion display was generated.
- FinOpsAI mapping decision recorded: proceed to Phase 2 or stop at
  catalog-only.

---

## Decision: FinOpsAI Mapping Needed?

After Phase 1 source analysis and any approved secondary lane runs are complete,
and the completion display has been shown in the chat, decide explicitly whether
to proceed to Phase 2 FinOpsAI mapping or stop at catalog-only closure.

The Phase 2 entry decision must account for all available run-folder artifacts —
primary lane and any secondary lane artifacts — not just the initial Phase 1
analysis. A secondary lane run may strengthen or create the case for Phase 2
even when the primary lane analysis alone would not have justified it.

**Yes → Proceed to Phase 2 when:**
- Lane output contains candidate ideas affecting FinOpsAI product behavior, repo
  architecture, engineering workflow, prompts, testing, or documentation.
- The user has requested FinOpsAI mapping.
- The source contains at least one pattern, idea, or finding grounded in
  implementation-level evidence with plausible FinOpsAI relevance.

**No → Stop at catalog-only closure when:**
- The request was transcript cleanup, source-only analysis, general education
  capture, or a non-FinOpsAI comparison.
- The source is speculative, hype-dense, or lacks concrete implementation
  patterns with FinOpsAI applicability.
- The user has not requested mapping and no strong mapping case exists from lane
  output.
- The Lane To Phase Map marks Phase 2 as not applicable for the selected lane.

When stopping, the Phase 1 completion display must name the specific source
topic and explain why Phase 2 is not currently justified. The explanation must
be topic-specific, not generic.

If the human accepts the stop recommendation, transition immediately into run
closure: ask for approval to write the end-of-run summary, write the run
summary artifact, update `notes/output_catalog.md`, and then perform the
retrospective check.

---

## Phase 2: Map To FinOpsAI Applicability

Purpose and scope:
- Phase 2 evaluates whether lane output should influence FinOpsAI product,
  workflow, tooling, testing, documentation, or architecture decisions. It
  includes targeted repo evidence review, applicability classification, and
  roadmap-fit assignment.
- If the same run contains outputs from more than one Phase 1 lane artifact,
  Phase 2 must use the combined evidence base. Apply the multi-source evidence
  rule: read all available run-folder artifacts, attribute findings by lane,
  distinguish primary vs. secondary contributions, and state relationships
  explicitly. Do not allow any single source to silently override another.
- It does not approve work for implementation, request task-card generation, or
  bypass evidence gaps with speculation.

Conditional phase: enter only after the mapping decision is `Yes`. Some source
runs stop after lane-specific analysis, requirement triage, domain review,
workflow review, or catalog update.

Repo rule: read FinOpsAI `AGENTS.md` first. Treat mapping as read-only unless
implementation is explicitly requested.

---

### Step 1: Inspect Only Relevant Repo Evidence

Run phase-step verification first:

| Order | Verification | Fail action |
| --- | --- | --- |
| 1 | Confirm current phase and step match this section. | If mismatched, stop and return to the correct phase/step. |
| 2 | Confirm required prior gates or decisions are completed. | If any prerequisite is missing, stop and complete it before continuing. |
| 3 | Confirm progress-tracker state before this step. | If tracker state is missing or stale, stop and update the tracker before continuing. |
| 4 | Confirm target artifact path and identifier when applicable. | If target is unclear or conflicts, stop and clarify before running prompts. |

Run combined phase-step verification prompt:
```text
Before Phase 2 Step 1 repo-evidence work, verify all four checks and return a
structured gate result:
1. Current phase and step match Phase 2 Step 1.
2. Required prior gates or decisions are complete.
3. Progress-tracker state is present and current for this step.
4. Target artifact path and identifier are confirmed when applicable.

Return exactly one line per check in this format:
- Check 1: PASS|FAIL - <concise reason>
- Check 2: PASS|FAIL - <concise reason>
- Check 3: PASS|FAIL - <concise reason>
- Check 4: PASS|FAIL - <concise reason or "N/A - no target artifact required yet">

Then return:
- Overall: PASS|FAIL
- Next action: <proceed to repo-evidence actions OR stop with the blocking item(s)>

If any check fails, stop and report only the blocking item(s). Do not start
repo-evidence actions.
```

Chat output template:
```text
Phase 2 Step 1 Gate Result
- Check 1: PASS|FAIL - <concise reason>
- Check 2: PASS|FAIL - <concise reason>
- Check 3: PASS|FAIL - <concise reason>
- Check 4: PASS|FAIL - <concise reason or "N/A - no target artifact required yet">
- Overall: PASS|FAIL
- Next action: <proceed to repo-evidence actions OR stop with the blocking item(s)>
```

Run repo-evidence actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run repo-guidance read prompt | If repo guidance cannot be established, stop and record the evidence gap. |
| 2 | Run scoped repo-evidence prompt | If relevant evidence is missing, stop and report what evidence is needed. |
| 3 | Run mapping-boundary confirmation prompt | If read-only boundary or constraints are violated, stop and correct before continuing. |

Run repo-guidance read prompt:
```text
Read /Users/Sites/Repo-FinOpsAI/AGENTS.md first and apply nested AGENTS.md
files if relevant to the mapped idea. Confirm the applicable repo constraints
before any mapping claim is made.
```

Run scoped repo-evidence prompt:
```text
Inspect only the relevant FinOpsAI docs, specs, source files, tests, and
tooling needed for the mapping question. Read all available run-folder artifacts
(transcript analysis, secondary lane artifacts if present) before beginning.
Attribute findings to their source artifact. If evidence is insufficient, stop
and state the gap instead of guessing.
```

Progressive repo search rule:
- Do not treat Phase 2 as whole-repo review by default.
- Start with `/Users/Sites/Repo-FinOpsAI/AGENTS.md` and any closer nested
  `AGENTS.md` files in the workflow-relevant area.
- For Lane 5 Product Workflow Analysis, start repo evidence review with
  `/Users/Sites/Repo-FinOpsAI/docs/engineering/` and other obviously relevant
  workflow/process documentation.
- Expand next to enforcement surfaces only when needed: CI workflows,
  automation scripts, prompt/agent/harness files, templates, checklists, and
  related tooling.
- Inspect representative tests or source files only when the workflow claim
  cannot be grounded credibly from guidance and enforcement surfaces alone.
- Stop widening the search once the applicability claim is evidence-backed.

Run mapping-boundary confirmation prompt:
```text
Keep this assessment read-only unless implementation is explicitly requested.
Preserve deterministic accounting, review, approval, posting, credential,
dependency, privacy, and testing constraints.
```

Repo-evidence checklist:

| Check | Required condition |
| --- | --- |
| Repo guidance | `/Users/Sites/Repo-FinOpsAI/AGENTS.md` read first; nested `AGENTS.md` applied where relevant. |
| Progressive scope | Lane 5 starts with `docs/engineering/` and widens only when more enforcement evidence is needed. |
| All run-folder artifacts read | Primary lane artifact and all secondary lane artifacts present in the run folder have been read before classification begins. |
| Scope | Only relevant docs, specs, source files, tests, and tooling inspected. |
| Record outcome | Assessment outcome is written to `output/` using the defined naming format. |
| Boundary | Mapping kept read-only unless implementation explicitly requested. |
| Evidence quality | Claims grounded in source evidence and FinOpsAI evidence, attributed by artifact source. |
| Gaps | Any missing evidence explicitly recorded instead of guessed. |

---

### Step 2: Classify Applicability

Run phase-step verification first (same four checks as Step 1).

Run classification actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run category-classification prompt | If category cannot be assigned from evidence, stop and record uncertainty/evidence gaps. |
| 2 | Run evidence-capture prompt | If source or FinOpsAI evidence is weak, stop and mark as non-applicable or deferred. |
| 3 | Run category-boundary prompt | If categories are collapsed, split streams before continuing. |

Run category-classification prompt:
```text
Classify each mapped idea using these categories: Product feature, Harness or
workflow tooling, AI integration, Prompting or agent workflow, Engineering
process, Architecture or infrastructure, Testing/QA/evaluation,
Docs/spec/product-vault, or Non-applicable.
```

Run evidence-capture prompt:
```text
For each applicable category, record source idea, source evidence (attributed
to the artifact it came from), FinOpsAI evidence, applicability level, required
change type, risk, and recommended next artifact.
```

Run category-boundary prompt:
```text
Do not collapse categories. Keep product features, workflow/process changes,
harness/tooling updates, AI integration ideas, architecture changes,
testing/QA work, docs/spec updates, and non-applicable items as separate
streams.
```

Chat output template:
```text
Phase 2 Classification Summary
- Immediate fits: <concise list or "none">
- Process-change fits: <concise list or "none">
- Architecture/design-dependent fits: <concise list or "none">
- Rejected or poor-fit ideas: <concise list or "none">
```

Applicability category reference:

| Category | Meaning |
| --- | --- |
| Product feature | End-user capabilities, product behavior, UI, or functional requirements. |
| Harness or workflow tooling | Research harness, local tools, scripts, runbooks, catalogs, or operational workflow mechanics. |
| AI integration | Model-assisted product behavior, LLM signals, local model tooling, or AI review support. |
| Prompting or agent workflow | Reusable prompts, agent operating instructions, CodeX usage patterns, or review-agent behavior. |
| Engineering process | Coding practice, review policy, dependency discipline, documentation discipline, or development workflow. |
| Architecture or infrastructure | Layering, persistence, external services, ingestion architecture, packaging, or major dependency changes. |
| Testing, QA, or evaluation | Regression tests, validation gates, QA plans, evaluation harnesses, or source-code checks. |
| Docs/spec/product-vault | Product specs, engineering docs, product-vault notes, decision logs, or durable guidance. |
| Non-applicable | Poor fit, premature, unsafe, speculative, unsupported, or outside FinOpsAI scope. |

---

### Step 3: Assign Roadmap-Fit Status

Run phase-step verification first (same four checks as Step 1).

Run roadmap-status actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run status-assignment prompt | If status cannot be assigned from evidence, stop and record uncertainty/evidence gaps. |
| 2 | Run status-justification prompt | If rationale, risk, or next artifact is unclear, stop and refine before continuing. |
| 3 | Run status-boundary prompt | If status implies unauthorized drafting or implementation, stop and route through the proper gate. |

Run status-assignment prompt:
```text
Assign one roadmap-fit status to each recommendation using
RESEARCH_WORKFLOW_USAGE.md statuses: Immediate candidate, Needs roadmap
approval, Needs product design, Needs architecture design, Needs process
approval, Research backlog, Deferred, or Rejected.
```

Run status-justification prompt:
```text
For each assigned status, explain why it fits, what evidence supports it, what
risk remains, and what the next artifact should be. Save or update
output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md when roadmap-fit is needed.
```

Run status-boundary prompt:
```text
For AI/model recommendations, require a design or approval path when ideas
could affect accounting authority, validation, approval, posting eligibility,
or review gates. Do not permit ClickUp-ready drafting unless status and human
approval path explicitly allow it.
```

Roadmap-status reference:

| Status | Use when | Next step |
| --- | --- | --- |
| Immediate candidate | Clear fit, strong evidence, low ambiguity, and compatible with current architecture and roadmap. | Ask for human approval for card drafting. |
| Needs roadmap approval | Product-relevant but not already established as current priority. | Product Owner decision. |
| Needs product design | Product intent, UX behavior, acceptance outcomes, or scope boundaries are incomplete. | Product Design Workflow. |
| Needs architecture design | Requires structural change, persistence change, external service, major dependency, or new integration pattern. | Architecture/design assessment. |
| Needs process approval | Affects human workflow, ClickUp workflow, prompts, QA gates, or operating model. | Process owner approval. |
| Research backlog | Interesting but not ready for implementation or product commitment. | Future review item. |
| Deferred | Plausible but blocked by timing, missing evidence, roadmap mismatch, or dependency. | Record in roadmap-fit by default; separate deferred note only by exception. |
| Rejected | Poor fit, unsafe, speculative, contradictory, or outside FinOpsAI scope. | Record in roadmap-fit by default; separate rejected note or catalog-only mention only by exception. |

Phase 2 pass gate:
- All available run-folder artifacts read and cited in the mapping.
- Repo evidence reviewed and mapping remained read-only.
- Applicable ideas classified with source and FinOpsAI evidence, attributed by
  artifact source.
- Roadmap-fit status assigned and saved to expected artifact.
- Next path recorded: proceed to Phase 3 human gate, or stop with catalog-only
  closure if no actionable recommendation remains.

---

## Phase 3: Human Roadmap And Workflow Gate

Purpose and scope:
- Phase 3 converts mapped recommendations into a governed human decision. It
  includes route selection, design-readiness review, next-artifact selection,
  and explicit approval recording when one recommendation is authorized for
  ClickUp-ready drafting.
- It does not generate the draft itself, merge multiple recommendations into one
  approval, or replace human routing with automatic backlog creation.

Conditional phase: run only when lane output may influence roadmap, product,
domain, workflow, process, or backlog decisions. Not required for source-only
analysis with no FinOpsAI recommendation.

Implemented gate: research output creates card candidates, not automatic task
cards.

---

### Step 1: Approve, Route, Defer, or Reject

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run human-decision actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run route-selection prompt | If route cannot be determined from evidence, stop and record uncertainty or missing context. |
| 2 | Run route-justification prompt | If rationale or risk is unclear, stop and refine before continuing. |
| 3 | Run route-boundary prompt | If route implies unauthorized drafting, stop and return to proper gate/approval step. |

Run route-selection prompt:
```text
Using lane output, repo mapping, and roadmap-fit status, select one route:
Product Design, Product Development, process approval, research backlog,
deferred in roadmap-fit, rejected in roadmap-fit/catalog-only, or catalog-only
when no FinOpsAI recommendation is warranted.
```

Run route-justification prompt:
```text
Explain why the selected route is correct, including source/repo evidence,
residual risk, and next artifact. Record deferred and rejected outcomes in
output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md by default; use exception
artifacts only when justified.
```

Run route-boundary prompt:
```text
Confirm this step does not draft a ClickUp-ready card. If the route is
immediate candidate, require explicit human approval before any Phase 4 card
drafting.
```

Chat output template:
```text
Route Result
- Selected route: <Product Design | Product Development | Process approval |
  Research backlog | Deferred | Rejected | Catalog-only>
- Recommendation set covered: <exact recommendation(s) or "none">
- Why this route is correct: <one concise rationale>
- Card drafting status: <blocked pending approval OR not applicable OR may
  continue toward Phase 4>
```

Process-approval handoff rule:
- If the selected route is `Process approval` and one recommendation is
  concrete enough to continue later as a single ClickUp-ready draft candidate,
  do not stop at a generic "choose one of these recommendations" message.
- Present one exact recommendation at a time, propose one exact identifier, and
  repeat the approval syntax in the same response.

Use this handoff template:
```text
Ready to draft a ClickUp card for: <recommendation name>
Suggested identifier: <identifier>

Please confirm using this format:
  Approved — identifier: <identifier>
```

If more than one process recommendation survives, present them sequentially one
at a time rather than asking for an unstructured choice.
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

Route-decision reference:

| Decision | Use when |
| --- | --- |
| Product Design | Product intent, UX behavior, acceptance outcomes, scope, or user value needs definition. |
| Product Development | Recommendation is implementation-ready enough to become a governed work item after card gates. |
| Process approval | Idea affects ClickUp workflow, CodeX workflow, prompts, QA gates, or operating model. |
| Research backlog | Idea is useful but not ready for product, process, or implementation commitment. |
| Deferred in roadmap-fit | Idea is plausible but blocked by timing, evidence, roadmap, dependency, or professional-review concerns. |
| Rejected in roadmap-fit or catalog-only | Idea is poor fit, unsafe, speculative, outside scope, or source-only. |

---

### Step 2: Decide Design Readiness

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run design-readiness actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run design-readiness check prompt | If readiness is unclear, stop and record missing product-definition requirements. |
| 2 | Run design-route decision prompt | If Product Design route is required, stop downstream drafting and record design route. |
| 3 | Run design-boundary prompt | If route/boundary is inconsistent, stop and correct before continuing. |

Run design-readiness check prompt:
```text
Evaluate design readiness for this recommendation using the FinOpsAI Product
Design Workflow. Check product intent, UX behavior, acceptance outcomes, scope
boundaries, dependencies, and governing artifact path.
```

Run design-route decision prompt:
```text
If any material product definition is missing, route to Product Design Workflow
before task-card drafting and record the route in
output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md or current mapping artifact.
```

Run design-boundary prompt:
```text
Confirm design-readiness outcome is consistent with the approved route and does
not bypass Phase 3/Phase 4 gating.
```

Chat output template:
```text
Design Readiness Result
- Product Design required: Yes|No
- Rationale: <one concise sentence>
- Next artifact implication: <design referral, roadmap-fit update, or continue>
```

Design-readiness reference:

| Check | Design needed when |
| --- | --- |
| Product intent | The user outcome, business value, or product behavior is unclear. |
| UX behavior | Interaction, review state, screen behavior, or user decision flow is undefined. |
| Acceptance outcomes | Success cannot be tested without inventing requirements. |
| Scope boundary | In-scope and out-of-scope limits are missing or competing ideas are bundled. |
| Governing artifact | No suitable spec path or design candidate exists for the work item. |

---

### Step 3: Choose Next Artifact

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run next-artifact actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run next-artifact selection prompt | If next artifact is unclear, stop and map the decision to one explicit target. |
| 2 | Run immediate-candidate approval prompt (conditional) | If route is immediate candidate and approval details are missing, stop and return to Step 1. |
| 3 | Run artifact-boundary prompt | If one-to-one recommendation/card rule is violated, stop and split before continuing. |

Run next-artifact selection prompt:
```text
Based on the approved route, choose the next artifact and explain why it is the
correct destination. If the approved route is an immediate candidate, record
that Phase 4 should run using target draft path
output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md.
Otherwise, produce the appropriate design referral, process note, roadmap-fit
update, or catalog-only update.
```

Run immediate-candidate approval prompt (only when immediate candidate route is
selected). This is the Approval Capture Protocol required by
`RESEARCH_WORKFLOW_USAGE.md`:
```text
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

```text
Ready to draft the next ClickUp card for: <recommendation name>
Suggested identifier: <identifier>

Please confirm using this format:
  Approved — identifier: <identifier>

If you want a different identifier, send the same format with your preferred identifier.
```

Do not accept an approval that does not confirm both the recommendation name and
the identifier. If the user message is ambiguous — for example, "yes go ahead"
or "looks good" without naming the recommendation or identifier — stop and ask
for the missing confirmation before writing any file.

Run artifact-boundary prompt:
```text
Confirm one approved recommendation maps to one draft artifact, with one exact
identifier. Do not combine multiple recommendations into one card and do not
infer "next" from ordering when multiple immediate candidates exist.
```

Next-artifact reference:

| Decision | Next artifact |
| --- | --- |
| Immediate candidate with approval | Phase 4 card-candidate gate using `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md` |
| Needs product design | Design referral or Design Specification Candidate path |
| Needs architecture design | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` with architecture/design next step |
| Needs process approval | Workflow applicability artifact or process decision note |
| Research backlog | Research note or catalog entry with future review marker |
| Deferred | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` by default; separate deferred note only by exception |
| Rejected | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` by default; separate rejected note or catalog-only mention only by exception |
| Source-only | Catalog-only mention when no FinOpsAI recommendation exists |

Phase 3 pass gate:
- One next artifact path selected.
- Decision route explicitly recorded.
- Approval Capture Protocol completed with confirmed recommendation name and
  identifier before Phase 4 begins for any selected immediate candidate.

---

## Decision: ClickUp Card Needed And Approved?

**Yes → Proceed to Phase 4 when:**
- One recommendation is explicitly approved for ClickUp-ready drafting with one
  exact identifier confirmed by the human using the Approval Capture Protocol.

**No → Stop when:**
- No Phase 4 is required.
- Roadmap-fit, design, process routing, or catalog-only outcome remains final.

---

## Phase 4: Run ClickUp Card-Candidate Gate

Purpose and scope:
- Phase 4 executes the post-approval card-candidate workflow for one approved
  recommendation. It includes readiness verification, approval verification,
  FinOpsAI task-card gates, collision checks, and generation of one
  ClickUp-ready draft artifact when all gates pass.
- It does not request initial approval, broaden scope beyond the approved
  recommendation, or publish/create the ClickUp card automatically.

Optional phase: run only after human approval to draft ClickUp-ready card
content. This phase produces draft content only. Publishing or creating the
ClickUp card remains a human/tool-owned action.

Implemented rule: use the ClickUp card-candidate gate in
`RESEARCH_WORKFLOW_USAGE.md`, then apply FinOpsAI task-card and title guides.
The card is the control record. The spec lives in the repo. The execution
prompt stays on the card.

---

### Step 1: Check Candidate Readiness

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run check prompts in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run approval prompt | If approval is missing, ambiguous, or mismatched, stop and return to Phase 3 Step 3. |
| 2 | Run readiness-check prompt | If readiness issues are raised, stop, refer to the readiness checklist table, and fix issues before continuing. |

Run approval prompt:
```text
Confirm that approval already exists for "<exact recommendation name>" with
identifier "<identifier>". If the approval is missing, ambiguous, or does not
match the current target draft, stop and return to Phase 3 Step 3 instead of
drafting.
```

Run readiness-check prompt:
```text
Check whether this recommendation is ready to become a ClickUp-ready card
draft. Use the card-candidate gate in RESEARCH_WORKFLOW_USAGE.md. Confirm that
Phase 3 approval already exists for one exact recommendation and one exact
identifier. If any readiness item is missing, or if that approval record is
missing or ambiguous, stop and report what must be fixed before drafting
output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md.
Before writing the file, verify that the target path does not already exist;
if it does, stop and inform the user and recommend reviewing the existing draft
or choosing a different identifier.
```

Chat output template:
```text
Phase 4 Readiness Result
- Recommendation verified: <exact approved recommendation>
- Identifier verified: <exact identifier>
- One-primary-task scope confirmed: Yes|No
- Collision check passed: Yes|No
- Next action: <continue to task-card gates OR stop with blocker>
```

Operator rule: print `Phase 4 Readiness Result` in the chat before drafting
begins. Do not rely on the draft artifact to communicate readiness verification
after the file is written.

Readiness checklist:

| Readiness item | Required condition |
| --- | --- |
| Source artifact | Durable source analysis, mapping, triage, or applicability artifact exists. |
| Evidence / caveats / risks | Source evidence, caveats, and risks are recorded; FinOpsAI applicability is grounded in repo/product evidence. |
| Card-candidate status | Roadmap-fit status is `Immediate candidate` or otherwise eligible for card consideration. |
| Task shape | Work is one primary task with clear scope and out-of-scope boundaries. |
| Design readiness | Product Design is not needed, or work is routed there before card finalization. |
| Acceptance criteria | Acceptance criteria are writable without inventing missing requirements. |
| Task type and governing path | Task type is known and one governing spec path or design route is selected. |
| Draft authorization | Human approval is already recorded before Phase 4 begins and names one exact recommendation and one exact draft filename identifier. |
| Draft path collision check | Intended draft path does not already exist; if it does, stop and inform the user instead of overwriting it. |

---

### Step 2: Run FinOpsAI Task-Card Gates

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run task-card gate checks in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run Request Appropriateness | If it fails, stop. Do not draft. |
| 2 | Run Information Sufficiency | If it fails, stop. Do not draft. |
| 3 | Confirm both passed | If either failed, return missing details instead of drafting. |

Run Request Appropriateness prompt:
```text
Evaluate whether this request is appropriate for ClickUp-ready task-card
drafting under /Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md.
If the request is not a valid task-card candidate, stop and explain the correct
next action. Do not generate
output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md.
```

Run Information Sufficiency prompt:
```text
Evaluate whether requirement, outcome, one-primary-task boundary, scope, and
behavioral intent are sufficiently defined without inventing requirements. If
information is insufficient, stop and list exactly what is missing before
drafting.
```

Run confirm both-pass gate prompt:
```text
Confirm that Request Appropriateness and Information Sufficiency both passed.
Enforce delivery boundaries: one primary work item, specification in repo,
execution prompt on the card. Only then continue toward drafting
output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md.
```

Chat output template:
```text
Request Check Result
- PASS|FAIL - <concise reason>

Information Check Result
- PASS|FAIL - <concise reason>
```

Operator rule: print both gate results in the chat before generating the
ClickUp-ready draft. Do not rely on the generated draft artifact to carry the
gate outcomes after drafting.

Task-card gate checklist:

| Gate | Pass condition | Fail action |
| --- | --- | --- |
| Request Appropriateness | User is asking for a ClickUp-style task card, task-card example, structured development work item, card refinement, or requirement-to-card conversion. | Do not generate a card. Explain why and recommend the correct next action. |
| Information Sufficiency | Core requirement, intended outcome, one-primary-task boundary, scope, and behavioral intent are sufficient without inventing requirements. | Do not generate a card. List what information is still needed. |
| Both must pass | Request Appropriateness and Information Sufficiency are both passed. | If either fails, stop and return failure reason(s) and required fixes. |
| Delivery boundary | Card keeps one primary work item; specification stays in repo; execution prompt stays on the card. | Do not draft until boundaries are corrected. |

---

### Step 3: Draft One Primary Card Only

Run phase-step verification first (same four checks as Phase 2 Step 1).

Run drafting actions in order:

| Order | Action | Fail action |
| --- | --- | --- |
| 1 | Run card-draft generation prompt | If generation cannot satisfy required sections or one-primary-task rule, stop and return required fixes. |
| 2 | Run draft quality-check prompt | If required section coverage is incomplete, revise before finalizing the artifact. |
| 3 | Run final draft-record prompt | If collision/no-overwrite or publish boundary is violated, stop and correct before completion. |

Run card-draft generation prompt:
```text
Both Step 1 and Step 2 passed. Generate one ClickUp-ready task-card draft using
FinOpsAI's task-card generation guide and title guide. Keep it to one primary
work item and do not invent requirements. Use the approved identifier and target
path output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md.
Do not publish or create the ClickUp card.
```

Run draft quality-check prompt:
```text
Review the generated draft against required sections: title, requirement/problem
statement, expected outcome, scope, acceptance criteria, constraints,
dependencies/references, and subtasks. Confirm one governing spec path or design
route is present. Confirm Generate Specification and Generate Execution Prompt
subtasks are included when applicable.
```

Run final draft-record prompt:
```text
Before finalizing, verify collision/no-overwrite behavior and ensure the
artifact remains workspace markdown only. If target path already exists, stop
and inform the user; recommend reviewing existing draft or approving a different
identifier. Record that human publishes/creates the ClickUp card.
```

Card content checklist:

| Card section | Requirement |
| --- | --- |
| Title | Use `<type>: <short task summary>` with `feat`, `fix`, `refactor`, `docs`, `test`, or `chore`. |
| Requirement / Problem Statement | State the work item without inventing unclear requirements. |
| Expected Outcome | Describe desired result and user/business value. |
| Scope | Define in-scope and out-of-scope boundaries. |
| Acceptance Criteria | Use observable criteria strong enough to constrain later specification work. |
| Constraints | Include deterministic accounting, validation, privacy, dependency, review, and workflow constraints where relevant. |
| Dependencies / References | Reference source artifacts, repo evidence, specs, docs, and governing paths. |
| Subtasks | Include `Generate Specification` and `Generate Execution Prompt` when applicable, both tied to one governing artifact. |

Phase 4 exit check:
- Artifact path used:
  `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md`
- Collision check passed before write; no overwrite performed.
- Draft content stays workspace markdown; human publishes/creates ClickUp card.
- `Generate Specification` and `Generate Execution Prompt` subtasks included
  when applicable.
- Roadmap-fit artifact re-opened after the Phase 4 cycle to confirm tracker
  rows and narrative still agree.
- `notes/output_catalog.md` reflects the final durable artifact set for the
  completed card cycle.

---

## Workflow Loop Decision

Another approved recommendation to process?

- Before re-entry, update workflow progress-tracker state for the completed card
  cycle.
- Before re-entry, re-open the roadmap-fit artifact and verify that tracker
  rows, route/design status, and surrounding narrative are synchronized.
- If any roadmap-fit narrative text became stale after drafting, correct it
  before re-entry.
- Before re-entry, record changed artifacts and verification notes, including
  `notes/output_catalog.md` updates when applicable.
- If tracker or record updates are missing, stop and complete them before
  returning to Phase 3.
- **Yes →** return to Phase 3 Step 1 for the next one-recommendation cycle with
  a new identifier, then rerun Phases 3 and 4.
- **No →** do not stop at a descriptive state update. Present an explicit
  closure prompt that tells the user no additional eligible ClickUp card
  candidates remain and that the next step is approval to write the end-of-run
  summary. Use wording substantially like:

  `No additional eligible ClickUp card candidates remain for this run.`

  `Ready to write the end-of-run summary for: <run/source name>`

  `Please confirm using this format:`

  `  Approved — end-of-run summary`

  If the user does not approve end-of-run summary generation, do not treat the
  run as closed. After approval, write the run summary, update
  `notes/output_catalog.md`, then perform the End-of-Run Retrospective Check.
  Add or update `notes/lessons_learned.md` only if the run exposed a reusable
  workflow lesson. Ordinary bad input, unavailable sources, or user
  cancellation do not require a lessons-learned entry unless they reveal a
  reusable harness issue.

---

## Artifact Model

### Artifact Map

| Artifact | Purpose | Primary phase | System of record | Location |
| --- | --- | --- | --- | --- |
| Cleaned transcript | Transcript-only artifact that preserves source content for later analysis. | Phase 1 | Workspace text artifact | `output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt` |
| Transcript analysis | Structured transcript analysis after cleanup. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md` |
| Source analysis | Summarize source claims, caveats, risks, and candidate ideas. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_source_analysis_YYYY_MM_DD.md` |
| GitHub repo assessment | Assess external repository patterns, tooling, compatibility, and risks, then record an applicability recommendation and next-step recommendation with cited rationale. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_github_repo_assessment_YYYY_MM_DD.md` |
| Domain analysis | Review accounting, bookkeeping, finance operations, tax, reconciliation, reporting, compliance, or advisory content. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_domain_analysis_YYYY_MM_DD.md` |
| Domain applicability | Assess domain content against FinOpsAI user profile, scope, roadmap, and compliance boundaries. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_domain_applicability_YYYY_MM_DD.md` |
| Workflow analysis | Separate process changes, agentic workflow ideas, prompts, QA gates, and harness tooling from product features. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_workflow_analysis_YYYY_MM_DD.md` |
| Workflow applicability | Assess whether workflow content should influence FinOpsAI human workflow, agent-assisted workflow, docs, prompts, or process gates. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_workflow_applicability_YYYY_MM_DD.md` |
| Requirement triage | Normalize raw Product Owner intent and decide whether design, mapping, or card drafting is appropriate. | Phase 1 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_requirement_triage_YYYY_MM_DD.md` |
| Repo mapping | Map source ideas to FinOpsAI evidence and applicability categories. | Phase 2 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_repo_mapping_YYYY_MM_DD.md` |
| Roadmap fit | Assign roadmap-fit status and next step. Start with the required workflow progress tracker. | Phase 2 / Phase 3 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` |
| Run summary | Canonical reopening summary for the completed run. | Run closure | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md` |
| ClickUp-ready draft | Human-approved card draft after candidate and task-card gates pass. | Phase 4 | Workspace markdown artifact | `output/<n>_YYYY_MM_DD/<n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md` |
| Deferred outcomes | Plausible ideas blocked by timing, missing evidence, roadmap mismatch, or dependency. | Phase 2 / Phase 3 | Roadmap-fit artifact by default | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` |
| Rejected outcomes | Poor-fit, unsafe, speculative, contradictory, or out-of-scope ideas. | Phase 2 / Phase 3 | Roadmap-fit artifact by default | `output/<n>_YYYY_MM_DD/<n>_roadmap_fit_YYYY_MM_DD.md` or catalog-only mention |
| Catalog entry | Concise run index without long report excerpts. | Catalog update | Workspace catalog | `notes/output_catalog.md` |
| Lessons learned register | Durable record of reusable workflow lessons from completed runs or terminal stop conditions. | Run closure / retrospective | Workspace notes | `notes/lessons_learned.md` |

---

## Implemented Routing Table

| Source Type | First Artifact | Optional Next Artifact | ClickUp Candidate |
| --- | --- | --- | --- |
| YouTube transcript | Cleaned transcript + analysis report | Secondary lane artifacts (if approved) + repo mapping report | Only after mapping and approval |
| GitHub repo | GitHub repo assessment with applicability recommendation | Repo mapping report | Only for high-confidence compatible ideas and only after the recommendation supports moving forward |
| Business requirement | Requirement triage report | Roadmap fit or design referral | Yes, if task-card gates pass |
| Accounting/bookkeeping content | Domain analysis report | Domain applicability or repo mapping report | Only after domain and roadmap approval |
| Product workflow content | Workflow analysis report | Workflow applicability or repo mapping report | Usually `docs` or `chore`, only after approval |

---

## Roadmap-Fit Statuses

| Status | Meaning | Typical Next Step |
| --- | --- | --- |
| Immediate candidate | Clear fit, strong evidence, low ambiguity, compatible with current architecture and roadmap. | Human approval for card drafting |
| Needs roadmap approval | Product-relevant but not already established as current priority. | Product Owner decision |
| Needs product design | Product intent, UX behavior, acceptance outcomes, or scope boundaries are incomplete. | Product Design Workflow |
| Needs architecture design | Requires structural change, new integration pattern, persistence change, external service, or significant dependency. | Architecture/design assessment |
| Needs process approval | Affects human workflow, ClickUp workflow, prompts, QA gates, or operating model. | Process owner approval |
| Research backlog | Interesting but not ready for implementation or product commitment. | Future review item |
| Deferred | Plausible but blocked by timing, missing evidence, roadmap mismatch, or dependency. | Record in roadmap-fit by default; separate deferred note only by exception |
| Rejected | Poor fit, unsafe, speculative, contradictory, or outside FinOpsAI scope. | Record in roadmap-fit by default; separate rejected note or catalog-only mention only by exception |

---

## Lane To Phase Map

Required front door: Phase 1 Step 1 and Phase 1 Step 2 are mandatory for every
lane. Phases 2 through 4 are lane-dependent.

| Lane | Phase 2: FinOpsAI Mapping | Phase 3: Human Gate | Phase 4: Card Candidate |
| --- | --- | --- | --- |
| YouTube transcript | Choice: run only when transcript ideas need FinOpsAI applicability assessment. | Choice: run only if mapping produces recommendations or card candidates. | Choice: run only after mapping, roadmap fit, and human approval. |
| GitHub repository | Choice: run when external repo patterns need FinOpsAI compatibility assessment. | Choice: run if compatible ideas may affect roadmap, workflow, tooling, or architecture. | Choice: run only for high-confidence compatible ideas after approval. |
| Business requirement | Choice: run only if request needs repo/product applicability evidence. | Must if actionable: required when triage produces a roadmap, design, defer, reject, or card-candidate decision. | Choice: run only if request is one primary task and task-card gates can pass. |
| Accounting/bookkeeping domain | Choice: run only when domain content is product-relevant to FinOpsAI. | Must if actionable: required when domain findings may influence roadmap, compliance, product behavior, or backlog. | Choice: run only after domain, roadmap, and any professional-review concerns are resolved. |
| Product workflow content | Choice: run only if workflow idea affects FinOpsAI docs, tooling, prompts, QA, or process. | Must if actionable: required when workflow findings may change docs, prompts, QA gates, ClickUp flow, or operating model. | Choice: usually a `docs` or `chore` candidate, only after approval. |
| Source-only analysis | Not applicable. | Not applicable. | Not applicable. |

Verification result:
- Phase 2 is conditional for every lane.
- Phase 3 is mandatory only when lane output may influence roadmap, product,
  domain, or workflow decisions.
- Phase 4 is always optional and only runs after the ClickUp card-candidate gate
  can pass.

---

## Guardrails

| Risk | Control | Implemented In |
| --- | --- | --- |
| Premature backlog creation | Research output creates card candidates, not automatic task cards. | `RESEARCH_WORKFLOW_USAGE.md` ClickUp Card-Candidate Gate; Phase 3 and Phase 4 notices and prompts. |
| Overgeneralized source handling | Route sources using the implemented taxonomy in `RESEARCH_WORKFLOW_USAGE.md`. | `RESEARCH_WORKFLOW_USAGE.md` Source Taxonomy and Routing Table; Phase 1 Step 1 and Phase 1 Step 2 rules. |
| Accounting correctness drift | Preserve deterministic validation, review, and posting gates. | `/Users/Sites/Repo-FinOpsAI/AGENTS.md`; `RESEARCH_WORKFLOW_USAGE.md` repo-mapping rules; Phase 1 Step 1, Phase 2, and Phase 4 prompts. |
| Speculative AI integration | Treat model outputs as advisory unless a separate approved design adds safeguards. | `/Users/Sites/Repo-FinOpsAI/AGENTS.md`; `RESEARCH_WORKFLOW_USAGE.md` ClickUp exclusions; Phase 2 prompt examples. |
| ClickUp card bloat | One primary task per card, with Product Design routing when scope is unclear. | `/Users/Sites/Repo-FinOpsAI/docs/engineering/task_card_generation_guide.md`; `RESEARCH_WORKFLOW_USAGE.md` card-candidate gate; Phase 3 and Phase 4 rules. |
