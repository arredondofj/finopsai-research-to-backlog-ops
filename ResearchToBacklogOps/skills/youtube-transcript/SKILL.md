---
name: youtube-transcript-pipeline
description: Clean raw YouTube transcripts into analysis-ready text, then generate a structured technical analysis report. Optionally map transcript ideas to a software repo such as FinOpsAI.
---

# YouTube Transcript Pipeline

## Purpose
Use this skill when the user wants to:
1. optionally acquire a YouTube transcript from a URL,
2. clean a raw YouTube transcript,
3. generate a structured analysis report from the cleaned transcript,
4. update the output catalog with concise run metadata,
5. optionally produce a transcript-lane repo mapping artifact,
6. and hand the run off to the shared research workflow for roadmap-fit or
   ClickUp-card decisions when later phases are requested.

This skill is designed for software engineering, AI, coding-agent, systems-design, product-engineering, and developer-workflow transcripts.

## Inputs
Expected user-provided inputs:
- path to raw transcript file, or a YouTube URL to acquire the transcript first
- optional path to notes file
- optional YouTube URL
- optional request to map the transcript ideas to a repo

Typical files:
- acquired source transcript: `input/<title> [<video_id>]_YYYY_MM_DD.<lang>.vtt`
- manually supplied raw transcript: `input/<name>_raw_YYYY_MM_DD.txt`
- `notes/<name>_notes.md`

Optional CodeX UI or automation metadata:
- `Chat Title Mode: auto`
- `Chat Title Template: Transcript | <source_title> | <run_date_pacific>`
- `Chat Timezone: America/Los_Angeles`
- `Chat Title Source Priority: source_title -> local_filename -> user_supplied_label`

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_cleaned_YYYY_MM_DD.txt`
- `output/<name>_YYYY_MM_DD/<name>_analysis_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

Optional:
- `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`

## Rules
- Use `skills/research-markdown-authoring/SKILL.md` when writing markdown
  artifacts for this lane or later shared workflow phases.
- If the user provides a YouTube URL instead of a local transcript file, run transcript acquisition before cleanup.
- If the run is started through a CodeX UI or automation layer with a
  thread-title hook, provide chat-title metadata at run start so the UI layer
  can name the chat immediately.
- Validate the YouTube URL before attempting download. If validation fails, stop and inform the user; do not continue to cleanup, analysis, catalog updates, or repo mapping.
- Use `scripts/acquire_transcript.sh` for transcript acquisition when possible.
- YouTube subtitle acquisition requires network access. In restricted or sandboxed environments, if local validation passes but `yt-dlp` fails with DNS, connection, TLS, timeout, or network-unreachable errors, retry the same acquisition command with approved network access before treating the URL or subtitles as unavailable.
- Transcript acquisition must download subtitles/transcript only. Do not download video or audio.
- Preserve acquired source subtitle files in `input/`.
- Do not summarize during cleanup.
- Do not analyze during cleanup.
- Preserve timestamps unless the user explicitly asks to remove them.
- Remove duplicate duration-description lines such as “15 seconds” or “1 minute, 25 seconds”.
- Remove blank lines caused by cleanup.
- Correct only obvious transcription defects where intent is reasonably clear.
- If uncertain, preserve original wording rather than guessing.
- Keep the original order of the transcript.
- Use the cleanup prompt from `references/cleanup_prompt.md`.
- Use the analysis prompt from `references/analysis_prompt.md`.
- Use the repo application prompt from `references/repo_application_prompt.md` only when the user asks for repo relevance or codebase application.
- If the run needs roadmap-fit, approval gating, or ClickUp-ready drafting,
  hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` after transcript-lane outputs are
  complete.
- After generating outputs, update `notes/output_catalog.md` with concise source metadata, generated file paths, file purposes, high-level analysis reference tags, practical relevance, caveats, and verification notes.
- Do not duplicate transcript or report content in the catalog.
- In the user-facing completion response, recommend the next step explicitly.
- If the recommendation is `no further action yet`, name the specific transcript
  topic and explain why that topic does not warrant repo mapping, GitHub repo
  assessment, or ClickUp card-candidate drafting yet.
- Ensure the analysis report exposes stable surfaces for later workflow phases:
  summary, evidence/caveats, candidate ideas, recommendation/disposition, and
  verification notes.

## Workflow
### Step 0: Optional transcript acquisition
Use this only when the user provides a YouTube URL instead of a local transcript file.
- Validate the URL locally before making a network request.
- Stop and inform the user if the URL is malformed, is not a YouTube URL, or does not contain a valid video ID.
- Run `scripts/acquire_transcript.sh <URL>` from the workspace or with an absolute script path.
- If the script reports a network-access failure after local URL validation, request approved network access and rerun the same command once.
- If `yt-dlp` cannot reach the URL, cannot use the URL, or cannot create a `.vtt` subtitle artifact, stop and inform the user.
- Use the generated `input/<title> [<video_id>]_YYYY_MM_DD.<lang>.vtt` file as the raw source transcript for cleanup.

### Step 1: Cleanup
- Read the raw transcript file.
- For `.vtt` sources, use `scripts/clean_vtt_transcript.py <input.vtt> <output.txt>` for the mechanical cleanup pass when possible. This removes VTT scaffolding, inline timing tags, HTML escapes, and rolling-caption duplication while preserving timestamps.
- Apply the cleanup instructions from `references/cleanup_prompt.md`.
- Create the run folder `output/<name>_YYYY_MM_DD/` if it does not exist.
- Save the result to `output/<name>_YYYY_MM_DD/<name>_cleaned_YYYY_MM_DD.txt`.

### Step 2: Analysis
- Read the cleaned transcript.
- Apply the structured software-engineering / AI transcript analysis instructions from `references/analysis_prompt.md`.
- Structure the markdown so later phases can reliably extract:
  - `Executive Summary`,
  - decision takeaways / practical-use and caveat sections,
  - candidate ideas or explicit non-candidates,
  - recommendation or disposition,
  - and verification-oriented notes when relevant.
- Save the result to `output/<name>_YYYY_MM_DD/<name>_analysis_YYYY_MM_DD.md`.

### Step 3: Output catalog
- Create `notes/output_catalog.md` if it does not already exist.
- Add or update one concise entry for the run.
- Include:
  - source transcript path, source title if known, video ID or URL if known,
  - generated output file paths,
  - the purpose of each output file,
  - high-level topic, thesis, key technical areas, practical relevance, and main caveats,
  - verification notes such as line counts or artifact checks.
- Keep the catalog entry referential and high-level; do not paste transcript excerpts or analysis sections.

### Step 4: Optional repo mapping
Use this only if the user explicitly asks how the transcript relates to a repo or codebase.
- Read the cleaned transcript and the analysis output.
- If the same run folder also contains a GitHub repo assessment artifact, read
  that artifact too and treat it as part of the mapping evidence base.
- When both transcript artifacts and a GitHub repo assessment artifact exist in
  the same run, distinguish transcript-derived ideas, repo-validated or
  repo-challenged findings, and FinOpsAI compatibility evidence in the mapping.
- Read the local repo only as needed.
- Apply `references/repo_application_prompt.md`.
- Distinguish:
  - immediately applicable ideas,
  - ideas requiring architectural change,
  - ideas that are speculative or not suitable,
  - and ideas that conflict with the repo’s constraints.
- Save the result to `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.
- Update the same run entry in `notes/output_catalog.md` with the repo mapping file and a high-level mapping note.

### Step 5: Optional workflow handoff
Use this only when the user wants the transcript run to continue into the
shared research workflow.
- Do not create roadmap-fit or ClickUp-ready draft artifacts directly from this
  lane skill alone.
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` for:
  - roadmap-fit assignment,
  - workflow progress tracking,
  - human approval recording,
  - ClickUp card-candidate gating,
  - and ClickUp-ready draft generation.

## Safety / discipline
- Do not edit unrelated files.
- Do not modify the target software repo unless the user explicitly asks for implementation changes.
- Prefer writing reports over making code changes when the task is analytical.
- Be conservative when inferring names, terms, or technical intent from noisy transcripts.

## Suggested invocation examples
Example 1:
“Use youtube-transcript-pipeline on `input/harness_engineering_raw_YYYY_MM_DD.txt` and produce cleaned and analysis outputs.”

Example 2:
“Use youtube-transcript-pipeline on `input/harness_engineering_raw_YYYY_MM_DD.txt`, then assess what is realistically applicable to this FinOpsAI repo without making code changes.”

Example 3:
“Use youtube-transcript-pipeline for this YouTube URL: `<URL>`. First acquire the transcript, then produce cleaned and analysis outputs and update the catalog.”
