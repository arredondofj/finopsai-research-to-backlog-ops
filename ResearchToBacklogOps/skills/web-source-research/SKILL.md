---
name: web-source-research
description: Research a web article, documentation page, benchmark post, announcement, or other internet source by validating the URL, capturing durable source metadata, preserving citation-ready evidence, and producing a structured source-analysis artifact for later workflow phases.
---

# Web Source Research

## Purpose
Use this skill when the user wants to:
1. research an internet source that is not primarily a YouTube transcript or a
   GitHub repository,
2. assess a blog post, documentation page, article, benchmark writeup,
   announcement, RFC-style page, or other web-published material,
3. preserve citation-ready source metadata and access context,
4. produce a durable workspace artifact that later phases can map to FinOpsAI,
5. and avoid relying on ephemeral browser state or memory of a changing page.

Use this as the first-class lane for general web-source research.

## Inputs
Expected user-provided inputs:
- one or more web URLs
- research question or focus area
- optional FinOpsAI target area
- optional request for later mapping or roadmap-fit continuation

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates
  are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_web_capture_YYYY_MM_DD.md`
- `output/<name>_YYYY_MM_DD/<name>_source_analysis_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

Optional:
- `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`
- `output/<name>_YYYY_MM_DD/<name>_roadmap_fit_YYYY_MM_DD.md`

## Rules
- Use `skills/research-markdown-authoring/SKILL.md` when writing markdown
  artifacts for this lane or later shared workflow phases.
- Validate the URL before treating the page as usable source material.
- Use `scripts/capture_web_source.sh <url> <output.md>` for deterministic source
  capture when possible.
- Capture canonical URL, page title, publisher/site name when discoverable, and
  access date in the durable artifact.
- Record acquisition method explicitly:
  - browser/web view only,
  - browser + saved extracted text,
  - or other approved source-capture method.
- Distinguish page claims from your own interpretation.
- If the source is time-sensitive, record that freshness matters and note the
  access date in both the capture artifact and the analysis artifact.
- If key claims depend on multiple pages, record each source separately rather
  than blending unattributed evidence.
- Do not treat mutable web pages as stable evidence unless the artifact records
  when and how the content was accessed.
- Do not broaden into GitHub repo assessment when the main source is a repo;
  route that work through `skills/github-repo-assessment/SKILL.md`.
- Do not broaden into transcript acquisition when the main source is a YouTube
  URL; route that work through `skills/youtube-transcript/SKILL.md`.

## Workflow
### Step 1: Source capture
- Validate the URL shape and note any access constraints.
- Open the page and confirm it is the intended source.
- Prefer running
  `scripts/capture_web_source.sh <url> output/<name>_YYYY_MM_DD/<name>_web_capture_YYYY_MM_DD.md`
  so source metadata and extracted text are captured deterministically.
- Record:
  - original URL,
  - canonical URL if different,
  - page title,
  - publisher/site name when available,
  - access date,
  - acquisition method,
  - and research question.
- Create
  `output/<name>_YYYY_MM_DD/<name>_web_capture_YYYY_MM_DD.md`.

### Step 2: Source analysis
- Read the captured source material and answer the research question.
- Separate:
  - source summary,
  - evidence-backed claims,
  - unverified or weakly supported claims,
  - candidate ideas or recommendations,
  - caveats and exclusions,
  - and the current recommendation/disposition.
- Produce
  `output/<name>_YYYY_MM_DD/<name>_source_analysis_YYYY_MM_DD.md`.

### Step 3: Output catalog
- Add or update one concise run entry in `notes/output_catalog.md`.
- Keep the entry referential and high-level.
- Include source URL(s), capture artifact, analysis artifact, and important
  freshness/citation notes.

### Step 4: Optional repo mapping
Use this only if the user explicitly asks for FinOpsAI applicability or the
analysis clearly needs repo-grounded comparison.
- Read the capture artifact and source-analysis artifact first.
- If the same run folder includes other lane artifacts, treat them as part of
  the combined evidence base.
- Read only the relevant FinOpsAI docs, specs, source files, tests, and
  tooling needed for the mapping question.
- Save the mapping to
  `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.

## Evidence discipline
- Prefer primary sources over commentary when both are available.
- If a claim is high-stakes or likely to change, re-check the current page
  before finalizing later-phase recommendations.
- Quote minimally and record where the claim came from.
- If the page is inaccessible, stale, or obviously updated after the cited
  discussion, record that freshness gap instead of guessing.
- If scripted capture fails, record the failure mode and whether the fallback
  was browser-only/procedural capture.
