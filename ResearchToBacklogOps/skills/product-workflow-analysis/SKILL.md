---
name: product-workflow-analysis
description: "Use this skill for written process and delivery material: product
  development workflows, operating model docs, SOPs/runbooks, QA/review gates,
  backlog or sprint workflow guidance, agent workflow/harness guidance, or
  ClickUp workflow ideas. Trigger on requests like 'analyze this process doc',
  'review our delivery practices', 'what should change in how we work', or
  'should this affect our agent workflow'. For YouTube URLs or VTT transcript
  sources (including workflow-topic videos), use youtube-transcript-pipeline
  first; then use this skill for workflow applicability or process mapping."
---

# Product Workflow Analysis

## Purpose
Use this skill when the user wants to:
1. analyze product-development or delivery workflow material as source input,
2. separate process improvements from product features,
3. classify impacts on human workflow, agent-assisted workflow, prompts, QA,
   docs, or harness tooling,
4. generate a workflow analysis artifact,
5. optionally assess workflow applicability to FinOpsAI,
6. and hand the run off to the shared research workflow for roadmap-fit or
   ClickUp-card decisions when later phases are requested.

## Inputs
Expected user-provided inputs:
- workflow source material
- optional FinOpsAI process/tooling context
- optional request for applicability assessment

## Source Disambiguation
Lane 5 handles workflow content delivered as written text: articles, process
guides, delivery docs, prompt engineering posts, QA writeups,
retrospectives, or agentic workflow reference material.

If the source is a **YouTube URL or `.vtt` file** whose content is about
workflow topics, use `youtube-transcript-pipeline` first to acquire, clean,
and analyze the transcript. Once that Phase 1 analysis exists, this skill
may be used to assess workflow applicability to FinOpsAI if requested.

Do not use this skill to acquire or clean transcripts.

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_workflow_analysis_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

Optional:
- `output/<name>_YYYY_MM_DD/<name>_workflow_applicability_YYYY_MM_DD.md`
- `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`

## Rules
- Use `skills/research-markdown-authoring/SKILL.md` when writing markdown
  artifacts for this lane or later shared workflow phases.
- Separate process changes from product features.
- Distinguish human workflow changes, agent-assisted workflow ideas, prompt
  updates, QA gates, harness tooling, and documentation changes.
- Treat AI/model ideas as advisory unless a later approved design introduces
  deterministic safeguards.
- Do not create roadmap-fit or ClickUp-ready draft artifacts directly from
  this lane skill alone.
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` when later workflow phases are
  requested.
- Ensure the workflow artifact exposes stable surfaces for later workflow
  phases: executive summary, process findings, candidate outputs, explicit
  exclusions, recommendation/disposition, and verification notes.

## Workflow
### Step 1: Workflow analysis
- Identify the workflow problem, target audience, and operational claims.
- Separate process improvements from product behavior changes.
- Record candidate outputs such as docs, process changes, harness tooling,
  prompt updates, QA gates, or deferred notes.
- Produce `output/<name>_YYYY_MM_DD/<name>_workflow_analysis_YYYY_MM_DD.md`.

### Step 2: Optional workflow applicability
Use this when the user wants a FinOpsAI-specific applicability assessment.
- Assess whether the idea should influence FinOpsAI human workflow,
  agent-assisted workflow, docs, prompts, QA gates, or tooling.
- Start the FinOpsAI evidence search progressively:
  - read the repo root `AGENTS.md` first and any closer nested `AGENTS.md`
    in workflow-relevant areas,
  - start with `docs/engineering/` and other obviously relevant workflow docs,
  - expand to CI, automation, prompts, harness tooling, templates, or tests
    only when the workflow claim needs enforcement evidence,
  - inspect representative source files only if the workflow claim cannot be
    grounded credibly from docs, tooling, and tests alone.
- Produce
  `output/<name>_YYYY_MM_DD/<name>_workflow_applicability_YYYY_MM_DD.md`.

### Step 3: Optional repo mapping
Use this only if the user explicitly asks for a FinOpsAI repo-grounded mapping
or the applicability assessment produces ideas that need repo evidence.
- For FinOpsAI mapping, read `/Users/Sites/Repo-FinOpsAI/AGENTS.md` first.
- If the mapping target is not FinOpsAI, read that target repo's `AGENTS.md` first.
- Use a progressive repo search:
  - start with `docs/engineering/` and other workflow/process docs,
  - then check enforcement surfaces such as CI workflows, automation scripts,
    prompt/agent/harness files, templates, and checklists,
  - then inspect representative tests or source modules only if needed to
    confirm whether the documented workflow is actually enforced or constrained.
- Inspect only the relevant FinOpsAI docs, specs, source files, tests, or
  tooling needed to answer the mapping question. Do not widen to broad
  whole-repo browsing once the workflow claim is grounded.
- Keep the assessment read-only unless implementation is explicitly requested.
- Save to `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.
- Update the same run entry in `notes/output_catalog.md`.

### Step 4: Output catalog
- Add or update one concise run entry in `notes/output_catalog.md`.

### Step 5: Optional workflow handoff
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` for later workflow phases.

## Safety / discipline
- Do not let workflow-source enthusiasm collapse product, process, and AI ideas
  into one backlog item.
- Prefer explicit routing over broad “implement the workflow” recommendations.
- Keep FinOpsAI applicability assessments read-only unless implementation is
  explicitly requested.
- State evidence gaps rather than speculating on how a workflow idea would
  integrate with FinOpsAI tooling or process.
