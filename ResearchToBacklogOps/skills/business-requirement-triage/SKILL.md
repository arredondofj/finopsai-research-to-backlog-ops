---
name: business-requirement-triage
description: Normalize a raw Product Owner or stakeholder request into a scoped requirement-triage artifact, then hand off to the shared research workflow when later phases are needed.
---

# Business Requirement Triage

## Purpose
Use this skill when the user wants to:
1. turn a raw Product Owner or stakeholder request into a structured triage
   artifact,
2. identify expected outcome, affected area, and scope boundaries,
3. decide whether the request is one primary work item or must be split,
4. decide whether Product Design Workflow is required before Product
   Development,
5. update the output catalog with concise run metadata,
6. and hand the run off to the shared research workflow for roadmap-fit or
   ClickUp-card decisions when later phases are requested.

## Inputs
Expected user-provided inputs:
- raw requirement text
- optional affected FinOpsAI area
- optional request for roadmap-fit or card-candidate continuation

## Outputs
Create one run folder per source run:
- `output/<name>_YYYY_MM_DD/`
- use the date of the first durable artifact for the run as the folder date
- keep later-phase files in the same folder even if their individual file dates are later

Generate:
- `output/<name>_YYYY_MM_DD/<name>_requirement_triage_YYYY_MM_DD.md`
- update `notes/output_catalog.md`

## Rules
- Normalize the request into one primary work item where possible.
- If multiple independent work items are present, split or explicitly record
  the need to split.
- Do not invent product behavior to make the request look implementation-ready.
- Route to Product Design when product intent, UX behavior, acceptance
  outcomes, or scope boundaries are materially incomplete.
- Do not create roadmap-fit or ClickUp-ready draft artifacts directly from
  this lane skill alone.
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` when later workflow phases are
  requested.

## Workflow
### Step 1: Requirement triage
- Identify the core requirement, expected outcome, user/business context, and
  affected FinOpsAI area.
- Determine whether this is one primary work item or must be split.
- Identify known in-scope and out-of-scope boundaries.
- Decide whether Product Design Workflow is required before Product
  Development.
- Produce `output/<name>_YYYY_MM_DD/<name>_requirement_triage_YYYY_MM_DD.md`.

### Step 2: Output catalog
- Add or update one concise run entry in `notes/output_catalog.md`.

### Step 3: Optional workflow handoff
- Hand off to `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md` for roadmap-fit assignment,
  approval gating, and any later ClickUp-card work.

## Safety / discipline
- Do not broaden scope just to make the request fit a card.
- Prefer explicit uncertainty over guessed requirements.
