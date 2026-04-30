---
name: accounting-domain-review
description: Review accounting, bookkeeping, finance operations, tax, reconciliation, reporting, compliance, or advisory source material, then optionally map product-relevant ideas to FinOpsAI.
---

# Accounting Domain Review

## Purpose
Use this skill when the user wants to:
1. review accounting, bookkeeping, finance operations, tax, reconciliation,
   reporting, compliance, or advisory source material,
2. separate domain education from product or workflow recommendations,
3. identify compliance, review, auditability, and roadmap risks,
4. generate a domain analysis artifact,
5. optionally assess domain applicability to FinOpsAI,
6. and hand the run off to the shared research workflow for roadmap-fit or
   ClickUp-card decisions when later phases are requested.

## Inputs
Expected user-provided inputs:
- source text, transcript, notes, article, or other domain material
- optional jurisdiction, user profile, or FinOpsAI context
- optional request for FinOpsAI applicability

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_domain_analysis_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

Optional:
- `output/<name>_YYYY_MM_DD/<name>_domain_applicability_YYYY_MM_DD.md`
- `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`

## Rules
- Separate domain education from product-feature recommendations.
- Preserve deterministic accounting, review, approval, posting, credential,
  dependency, privacy, and testing constraints.
- Do not turn tax, compliance, or accounting advice into implementation tasks
  without explicit human approval and appropriate professional review.
- If the run continues into FinOpsAI applicability or repo mapping, keep the
  assessment read-only unless implementation is explicitly requested.
- If the run needs roadmap-fit, approval gating, or ClickUp-ready drafting,
  hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` after lane outputs are complete.

## Workflow
### Step 1: Domain analysis
- Identify domain area, user profile, and jurisdiction when relevant.
- Distinguish product-relevant ideas from general education or advisory
  material.
- Record compliance, review, auditability, and roadmap risks.
- Produce `output/<name>_YYYY_MM_DD/<name>_domain_analysis_YYYY_MM_DD.md`.

### Step 2: Optional domain applicability
Use this when the user wants FinOpsAI-oriented applicability rather than
source-only review.
- Assess which ideas are product-relevant, workflow-relevant, or unsuitable.
- Produce
  `output/<name>_YYYY_MM_DD/<name>_domain_applicability_YYYY_MM_DD.md`.

### Step 3: Optional repo mapping
Use this only if the user explicitly asks for a FinOpsAI repo-grounded mapping
or the applicability assessment produces ideas that need repo evidence.
- For FinOpsAI mapping, read `/Users/Sites/Repo-FinOpsAI/AGENTS.md` first.
- If the mapping target is not FinOpsAI, read that target repo's `AGENTS.md` first.
- Inspect only the relevant FinOpsAI docs, specs, source files, tests, or
  tooling needed to answer the mapping question.
- Keep the assessment read-only unless implementation is explicitly requested.
- Save to `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.
- Update the same run entry in `notes/output_catalog.md`.

### Step 4: Output catalog
- Add or update one concise run entry in `notes/output_catalog.md`.
- If verification metadata such as line counts is recorded, measure it from the
  saved artifact after write before finalizing the catalog entry.

### Step 5: Optional workflow handoff
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` for later workflow phases.

## Safety / discipline
- Be conservative with domain-to-product translation.
- State evidence gaps rather than guessing on regulated or professional-review
  issues.
