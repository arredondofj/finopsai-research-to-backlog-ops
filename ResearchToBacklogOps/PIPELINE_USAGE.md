# YouTube Transcript Pipeline Usage Guide

<!-- MAINTENANCE NOTE: This file covers YouTube transcript lane mechanics only.
Shared harness governance — phase completion display format, catalog update
sequencing, Phase 2 entry decision, roadmap-fit rules, and the ClickUp
card-candidate gate — is defined in RESEARCH_WORKFLOW_USAGE.md and takes
precedence over this file on those topics. After any update to
RESEARCH_WORKFLOW_USAGE.md, review this file for accuracy. -->

## Purpose

This file covers the YouTube transcript lane of the shared research harness.
It defines lane-specific mechanics: transcript acquisition, VTT cleanup
scripts, analysis focus, run-folder naming, and chat-title hook behavior.

It does not redefine shared harness governance. The following topics are
controlled by `RESEARCH_WORKFLOW_USAGE.md` and must not be restated or
overridden here:

- Phase 0–4 structure and phase entry conditions.
- Phase 1 completion display format and catalog update sequencing.
- Phase 2 entry decision criteria.
- Roadmap-fit statuses and the consolidation rule.
- The ClickUp card-candidate gate and Approval Capture Protocol.
- Chat-visible gate output requirements for Phases 2, 3, and 4.
- Boundary rules.

Use this file for transcript lane mechanics. Use `RESEARCH_WORKFLOW_USAGE.md`
for everything that governs the run after the lane analysis is complete.

## Lane Position in the Shared Harness

The YouTube transcript lane maps to the shared harness as follows:

| This file | Shared harness |
| --- | --- |
| Acquisition (URL validation, yt-dlp) | Phase 0: Register source and select lane |
| Cleanup and analysis | Phase 1: Produce lane-specific source analysis |
| Cross-lane signal detection | Phase 1 post-analysis step — output feeds completion display item 4 |
| Phase 1 completion display and catalog update | Governed by `RESEARCH_WORKFLOW_USAGE.md` |
| Approved cross-lane runs | Phase 1 extension — produces additional evidence before Phase 2 |
| Repo application / FinOpsAI mapping | Phase 2: Map to FinOpsAI applicability |
| Human gate, roadmap-fit, card drafting | Phases 3 and 4: Governed by `RESEARCH_WORKFLOW_USAGE.md` |

When this file and `RESEARCH_WORKFLOW_USAGE.md` appear to conflict on a shared
harness step, `RESEARCH_WORKFLOW_USAGE.md` governs.

## Lane Mechanics

### Phase 0: Acquisition (Optional)

Use this step when the user provides a YouTube URL instead of a local
transcript file.

YouTube subtitle acquisition requires network access. In sandboxed runs,
expect `yt-dlp` to need network escalation. If DNS or connection errors occur
after local validation passes, rerun the same acquisition command with approved
network access before treating the URL or transcript as unavailable.

Validate the URL before any download attempt:
- the URL must use `http://` or `https://`
- the host must be `youtube.com`, `www.youtube.com`, `m.youtube.com`,
  `music.youtube.com`, or `youtu.be`
- the URL must contain a valid 11-character YouTube video ID

If URL validation fails, stop and inform the user. Do not continue to cleanup,
analysis, catalog updates, or repo mapping.

Download subtitles only through the acquisition script:

    skills/youtube-transcript-pipeline/scripts/acquire_transcript.sh <URL>

The script uses `yt-dlp` with `--skip-download`, `--write-sub`, and
`--write-auto-sub`.

If local validation passes but `yt-dlp` reports DNS, connection, TLS, timeout,
or network-unreachable errors, classify the failure as a network-access problem
and request/retry with approved network access.

If `yt-dlp` cannot use the URL or no `.vtt` transcript artifact is created,
stop and inform the user.

Preserve the downloaded subtitle file in `input/`. Use this naming pattern:

    input/<title> [<video_id>]_YYYY_MM_DD.<lang>.vtt

### Phase 1: Cleanup and Analysis

**Cleanup**

Convert the raw transcript into a clean, analysis-ready form.

For `.vtt` sources, run the mechanical cleanup utility first:

    python3 skills/youtube-transcript-pipeline/scripts/clean_vtt_transcript.py <input.vtt> <output.txt>

The utility removes VTT scaffolding, inline timing tags, HTML escapes, and
rolling-caption duplication while preserving timestamps. Apply the cleanup
prompt afterward for high-confidence transcript-specific corrections only.

Do not summarize or analyze during cleanup. Preserve timestamps unless the
user explicitly asks to remove them. Correct only high-confidence
transcription defects. If uncertain, preserve the original wording.

**Analysis**

Review the cleaned transcript and generate a structured analysis report. Focus
on software engineering, AI, coding workflows, systems design, and technical
relevance to FinOpsAI.

**Optional transcript validation**

For transcript types that are primarily technical education or pattern
demonstration, an optional validation step may be used before the Phase 2
entry decision.

Use this only when needed to determine whether the source has enough
engineering substance to justify repo mapping.

Validation in this lane means checking whether the transcript's technical
patterns or claims hold up well enough to produce bounded improvement
hypotheses. It does not mean generic fact confidence alone.

If validation is performed:
- distinguish validated patterns from merely interesting examples,
- extract only bounded, non-speculative hypotheses,
- identify whether those hypotheses look like likely `refactor`,
  technical-debt, `docs`, `test`, `chore`, or workflow-improvement candidates,
- and carry those hypotheses forward into the Phase 2 decision.

Do not treat validation as an automatic Phase 2 trigger.
- If validation only confirms that the speaker is broadly correct about Python,
  tooling, or general engineering practice, that is still weak Phase 2
  evidence.
- Use validation to justify Phase 2 only when it creates concrete repo-facing
  hypotheses that can be assessed against FinOpsAI or another explicitly named
  target repo.

**Artifact paths**

Save artifacts to the run folder using these paths:
- `output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt`
- `output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md`

**Repo reference check**

After producing the analysis report, check whether the source or cleaned
transcript includes a concrete repository reference.
- If a repo reference is detected, record it as cited context in the analysis
  or catalog notes and notify the user in the response.
- Do not inspect the referenced repo during Phase 1 unless the user explicitly
  requests repo assessment or repo mapping.
- A detected repo reference does not by itself make Lane 2 GitHub repo
  assessment approval-ready in the Phase 1 display. Only surface Lane 2 as an
  approval-ready next action when the target repo can be named concretely in
  the response and the response distinguishes that optional repo assessment
  from any stronger cross-lane workflow signal.

**Phase 1 completion**

After saving the analysis artifact, follow the catalog update sequencing and
Phase 1 completion display format defined in `RESEARCH_WORKFLOW_USAGE.md`:

1. Run the verification pass for all newly written durable artifacts first.
   Measure any verification metadata from disk after the files are saved. For
   transcript runs, this includes any recorded line counts or similar metrics.
2. Update `notes/output_catalog.md` next, before generating the completion
   display. For transcript runs, the catalog entry must include the source
   transcript path, title, and video ID or URL when known. Populate any
   verification metadata values (such as line counts) using values measured
   in step 1 — do not estimate or derive them from visual inspection.
3. Generate the Phase 1 completion display in the chat following the
   conditional 7-or-8-item format in `RESEARCH_WORKFLOW_USAGE.md`:
   `Summary`, `Phase 2 Decision Takeaways`, `Generated Artifacts`,
   `Cross-Lane Signals`, `Proceed / Stop Recommendation`, optional
   `No-Go Rationale` when not proceeding, `Recommended Next Action`, and
   `Verification Notes`.
4. Apply the Phase 2 Entry Decision criteria from `RESEARCH_WORKFLOW_USAGE.md`
   to make the proceed-or-stop recommendation explicit before any Phase 2 work
   begins.

If optional transcript validation was performed, the completion display must
state whether the proceed-or-stop recommendation is based on
validation-derived refactor or technical-debt hypotheses or whether validation
still left the run at catalog-only closure.

For transcript analysis reports, use these sections as the default source for
the GUI display:
- Summary: `Executive Summary`
- Phase 2 Decision Takeaways: `What Seems Practically Useful`,
  `What Seems Aspirational, Fragile, or Hype-Prone`, and
  `Practical Takeaways for a Software / AI Product Leader`

If the analysis report uses different section names, extract the closest
equivalent summary, applicability, practical-use, caveat, and next-step
content.

### Phase 2: FinOpsAI Repo Mapping (Optional)

Enter this phase only after:
- the Phase 1 completion display has been shown in the chat,
- the human has responded to the Cross-Lane Signals prompt,
- any approved cross-lane runs are complete and their artifacts are saved,
- and the Phase 2 entry decision is explicitly yes.

Run this phase from the FinOpsAI repo, or provide its absolute path.

Before assessing applicability, read the FinOpsAI repo-local guidance:
- Prefer `AGENTS.md` at the FinOpsAI repo root.
- If nested `AGENTS.md` files exist in relevant FinOpsAI subdirectories,
  apply the closest applicable guidance for those areas.
- Use `AGENTS.md` to identify repo-specific constraints such as deterministic
  accounting logic, review gates, dependency policy, verification
  expectations, privacy/security rules, and high-risk modules.
- If no FinOpsAI `AGENTS.md` exists, state that explicitly in the assessment
  and proceed using evidence from the repo itself.

Transcript workspace:
`/Users/Admin/Documents/CodeX/ResearchToBacklogOps`

Read all available run-folder artifacts before beginning the assessment:
- Cleaned transcript: `output/<n>_YYYY_MM_DD/<n>_cleaned_YYYY_MM_DD.txt`
- Analysis report: `output/<n>_YYYY_MM_DD/<n>_analysis_YYYY_MM_DD.md`
- GitHub repo assessment (if present):
  `output/<n>_YYYY_MM_DD/<n>_github_repo_assessment_YYYY_MM_DD.md`
- Domain analysis (if present):
  `output/<n>_YYYY_MM_DD/<n>_domain_analysis_YYYY_MM_DD.md`
- Workflow analysis (if present):
  `output/<n>_YYYY_MM_DD/<n>_workflow_analysis_YYYY_MM_DD.md`
- Requirement triage (if present):
  `output/<n>_YYYY_MM_DD/<n>_requirement_triage_YYYY_MM_DD.md`

Apply the multi-source evidence rule from `RESEARCH_WORKFLOW_USAGE.md` when
more than one artifact type is present. The repo mapping must cite all
available evidence sources, distinguish their contributions by source, and not
allow any single artifact to silently override the others.

Apply:
`skills/youtube-transcript-pipeline/references/repo_application_prompt.md`

Assess what ideas are realistically applicable to the FinOpsAI repo. Ground
the assessment in all available run-folder artifacts, the FinOpsAI codebase,
and the FinOpsAI `AGENTS.md` guidance when present.

Follow the repo-mapping categories, applicability classification structure,
and multi-source evidence rule defined in `RESEARCH_WORKFLOW_USAGE.md`.

In the report, include a short note on how the FinOpsAI `AGENTS.md` guidance
affected the assessment, or state that no repo-local guidance was found.

Save the repo mapping artifact to:
`output/<n>_YYYY_MM_DD/<n>_repo_mapping_YYYY_MM_DD.md`

Update `notes/output_catalog.md` with the repo mapping artifact and a
high-level mapping note in the same run entry.

Do not modify the FinOpsAI codebase unless explicitly asked.

**After Phase 2:** The repo mapping output feeds the Phase 3 human gate and
Phase 4 card-candidate gate defined in `RESEARCH_WORKFLOW_USAGE.md`. Those
steps govern roadmap-fit assignment, human approval, and ClickUp card draft
generation. Do not skip to card drafting from Phase 2 output alone.

## Run-Folder Rule

- Create one run folder per processed source as `output/<n>_YYYY_MM_DD/`.
- Use the date of the first durable artifact for that source run as the folder
  date.
- Save all artifacts for that run inside the folder, keeping the same `<n>`
  prefix on each file.
- If later phases happen on a later day, keep their files in the same folder
  and preserve each file's own date suffix.
- The flat `output/` root should contain run subfolders, not mixed transcript
  artifacts from multiple runs.

## Chat-Title Hook Rule

- If the run is launched through a CodeX UI or automation layer that supports
  thread-title updates, pass chat-title metadata at run start and let that
  layer set the chat title immediately.
- Use the transcript lane default template:
  `Transcript | <source_title> | <run_date_pacific>`
- Resolve `<source_title>` from YouTube metadata first, then the acquired
  subtitle filename, then a user-supplied label.
- Use `America/Los_Angeles` for `<run_date_pacific>` unless the user
  explicitly requests another timezone.
- Chat-title metadata is advisory to the UI or automation layer and does not
  change transcript artifact naming.

## Folder Structure

Expected structure for the full workspace. Transcript lane artifacts for a
given run appear under `output/<n>_YYYY_MM_DD/`. Other lane artifact types are
defined in `RESEARCH_WORKFLOW_USAGE.md`.

```text
ResearchToBacklogOps/
├─ AGENTS.md
├─ PIPELINE_USAGE.md
├─ RESEARCH_WORKFLOW_USAGE.md
├─ finopsai_research-to-backlog_workflow.md
├─ finopsai_research-to-backlog_workflow.html
├─ .codex/
│  └─ config.toml
├─ skills/
│  ├─ accounting-domain-review/
│  │  └─ SKILL.md
│  ├─ business-requirement-triage/
│  │  └─ SKILL.md
│  ├─ github-repo-assessment/
│  │  └─ SKILL.md
│  ├─ product-workflow-analysis/
│  │  └─ SKILL.md
│  └─ youtube-transcript-pipeline/
│     ├─ SKILL.md
│     ├─ references/
│     │  ├─ cleanup_prompt.md
│     │  ├─ analysis_prompt.md
│     │  └─ repo_application_prompt.md
│     └─ scripts/
├─ input/
├─ output/
│  └─ <n>_YYYY_MM_DD/
│     ├─ <n>_cleaned_YYYY_MM_DD.txt
│     ├─ <n>_analysis_YYYY_MM_DD.md
│     ├─ <n>_github_repo_assessment_YYYY_MM_DD.md    (optional — Lane 2 cross-lane)
│     ├─ <n>_domain_analysis_YYYY_MM_DD.md           (optional — Lane 4 cross-lane)
│     ├─ <n>_workflow_analysis_YYYY_MM_DD.md         (optional — Lane 5 cross-lane)
│     ├─ <n>_requirement_triage_YYYY_MM_DD.md        (optional — Lane 3 cross-lane)
│     ├─ <n>_repo_mapping_YYYY_MM_DD.md              (optional — Phase 2)
│     ├─ <n>_roadmap_fit_YYYY_MM_DD.md               (optional — Phase 2/3)
│     ├─ <n>_clickup_card_draft_YYYY_MM_DD_<identifier>.md  (optional — Phase 4)
│     └─ <n>_run_summary_YYYY_MM_DD.md               (required at run closure)
├─ templates/
│  └─ FinOpsAI_AGENTS.md
└─ notes/
   ├─ output_catalog.md
   └─ lessons_learned.md
```

## Output Catalog

Catalog discipline is governed by `RESEARCH_WORKFLOW_USAGE.md`. The rules
below are transcript-lane-specific addenda to those shared requirements.

For transcript runs, each catalog entry must include:
- source transcript path, title, and video ID or URL when known
- generated output files and their purpose
- high-level topic, thesis, technical areas, practical relevance, and main
  caveat
- cross-lane signals detected, which were approved, and which were declined,
  with a brief rationale for any declined lanes
- verification notes such as line counts measured from disk and whether the
  source transcript was left unchanged in `input/`

Update the catalog before generating the Phase 1 completion display, not
after. Update it again after each approved cross-lane artifact is saved.
If Phase 2 repo mapping is generated, add the mapping artifact and a
high-level mapping note to the same run entry.

At run closure, add the run summary artifact
(`output/<n>_YYYY_MM_DD/<n>_run_summary_YYYY_MM_DD.md`) to the catalog entry
as the canonical reopening point for the run, per `RESEARCH_WORKFLOW_USAGE.md`.
If a reusable workflow lesson was recorded in `notes/lessons_learned.md`,
note that in the catalog entry as well.

Keep entries concise and referential. Do not paste full transcript text, long
report excerpts, or detailed analysis sections.
