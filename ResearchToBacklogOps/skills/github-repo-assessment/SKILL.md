---
name: github-repo-assessment
description: Assess an external GitHub repository or local clone as source material, then optionally map compatible ideas to FinOpsAI.
---

# GitHub Repo Assessment

## Purpose
Use this skill when the user wants to:
1. assess an external GitHub repository or local clone as source material,
2. identify architecture, patterns, tooling, tests, docs, and compatibility signals,
3. generate a GitHub repo assessment artifact,
4. update the output catalog with concise run metadata,
5. optionally map the repo's ideas to FinOpsAI,
6. and hand the run off to the shared research workflow for roadmap-fit or
   ClickUp-card decisions when later phases are requested.

## Inputs
Expected user-provided inputs:
- GitHub URL or path to a local clone
- assessment question or area of focus
- optional request to map the repo ideas to FinOpsAI

Typical files:
- local repo clone path
- optional notes file: `notes/<name>_notes.md`

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_github_repo_assessment_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

Optional:
- `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`

## Rules
- Use `skills/research-markdown-authoring/SKILL.md` when writing markdown
  artifacts for this lane or later shared workflow phases.
- Treat the source repo as assessment input, not implementation scope, unless
  the user explicitly asks for code changes in that repo.
- When the source is a remote GitHub URL and no local clone is provided,
  establish and record the acquisition method first:
  - use GitHub web and raw-file views first for lightweight assessment,
  - use a local clone only when the assessment question cannot be answered
    credibly from web-visible docs, representative source, tests, and CI
    surfaces, or when the user explicitly provides/approves a clone path.
- Inspect only the files needed to answer the assessment question.
- Record evidence for repo purpose, architecture, reusable patterns,
  dependencies, tests, docs, and license/security concerns when available.
- Record repo URL, owner/repo name, default branch when visible, commit or
  snapshot identifier when visible, and access method in the durable artifact.
- Distinguish reusable ideas from code reuse; do not copy code or recommend
  code reuse without explicit review.
- If the assessment continues into FinOpsAI mapping, use
  `/Users/Dev/Apps/finopsai-desktop` as the canonical local repo path, read
  `/Users/Dev/Apps/finopsai-desktop/AGENTS.md` first, stop for human
  confirmation if that path is missing and another checkout is the only visible
  candidate, and keep the mapping read-only unless implementation is explicitly
  requested.
- If the run needs roadmap-fit, approval gating, or ClickUp-ready drafting,
  hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` after lane outputs are complete.
- After generating outputs, update `notes/output_catalog.md` with concise
  source metadata, generated file paths, file purposes, practical relevance,
  caveats, and verification notes.
- If the assessment is based on web-visible repo surfaces only, say so
  explicitly and record what was not inspected because no clone or local test
  environment was used.
- After the repo assessment, run a lane-local cross-lane applicability check
  for Lane 6 Product Workflow Analysis and surface the result in the Phase 1
  completion display before any FinOpsAI mapping work begins.
- Ensure the assessment artifact exposes stable surfaces for later workflow
  phases: executive summary, repo evidence, caveats, candidate recommendations,
  applicability recommendation, explicit exclusions, and verification notes.

## Workflow
### Step 1: Repo assessment
- Record repo source, branch or commit if known, and access needs.
- When using a remote GitHub URL, capture:
  - canonical repo URL,
  - access method (`web-only`, `web + raw file views`, or `local clone`),
  - default branch when visible,
  - and any visible commit/SHA or release tag used as evidence anchor.
- Inspect only the files needed to answer the assessment question.
- Write the artifact so later phases can extract one or more bounded candidate
  recommendations rather than only a narrative assessment.
- Produce `output/<name>_YYYY_MM_DD/<name>_github_repo_assessment_YYYY_MM_DD.md`.

### Step 2: Output catalog
- Add or update one concise run entry in `notes/output_catalog.md`.
- Keep the entry referential and high-level.

### Step 3: Cross-lane applicability check
- Evaluate whether the repo assessment shows a Lane 6 Product Workflow Analysis
  signal.
- Flag Lane 6 when the repo's main value is in process, orchestration,
  approval flow, agent workflow, review/QA workflow, harness design, or other
  operating-model patterns beyond narrow implementation detail.
- Record either:
  - `Strong signal` with rationale,
  - `Weak signal` with rationale,
  - or no Lane 6 signal detected.
- Ask the human whether to run Lane 6 before proceeding to any Phase 2 mapping.

### Step 4: Optional repo mapping
Use this only if the user explicitly asks for FinOpsAI applicability or the
assessment clearly needs a FinOpsAI comparison.
- Read the assessment artifact.
- If the same run folder also contains transcript-lane artifacts, read the
  cleaned transcript and transcript analysis artifact too.
- When both transcript-lane artifacts and a repo assessment artifact exist in
  the same run, treat them as a combined evidence base for FinOpsAI mapping
  rather than choosing only one lane's evidence.
- Distinguish transcript-derived ideas, repo-validated or repo-challenged
  findings, and FinOpsAI compatibility evidence in the mapping.
- Read only the relevant FinOpsAI docs, specs, source files, tests, and
  tooling needed for the mapping question.
- Save the mapping to
  `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.
- Update the same run entry in `notes/output_catalog.md`.

### Step 5: Optional workflow handoff
- Do not create roadmap-fit or ClickUp-ready draft artifacts directly from
  this lane skill alone.
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` for later workflow phases.

## Safety / discipline
- Do not edit unrelated files.
- Do not modify the target repo unless the user explicitly asks for
  implementation changes.
- Prefer evidence-backed assessment over broad architectural speculation.
