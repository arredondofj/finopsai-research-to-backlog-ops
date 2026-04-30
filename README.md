# FinOpsAI Research-to-Backlog Operations

This repository contains two sibling workspaces for FinOpsAI research and backlog governance operations.

## Overview

- `ResearchToBacklogOps`: Upstream research workspace for ingesting source content, performing transcript cleanup and analysis, and generating backlog candidates.
- `BacklogGovernanceOps`: Downstream governance workspace for intake triage, duplicate handling, review, approval, and publication readiness.

These workspaces are designed to work together:
- `ResearchToBacklogOps` produces draft artifacts and research outputs.
- `BacklogGovernanceOps` receives governed copies of approved draft artifacts and manages Product Owner backlog governance.

## Workspace roles

### ResearchToBacklogOps

This workspace is focused on the research pipeline:
- Source ingestion and transcript cleanup
- Technical analysis and artifact generation
- Repo applicability and backlog candidate assessment
- Cataloging research outputs in `notes/output_catalog.md`

Key files:
- `AGENTS.md`
- `RESEARCH_WORKFLOW_USAGE.md`
- `PIPELINE_USAGE.md`
- `notes/output_catalog.md`
- `skills/`

### BacklogGovernanceOps

This workspace is focused on governance and handoff:
- Intake triage for artifacts arriving from research
- Duplicate detection and exception handling
- Review and approval workflow
- Publication readiness and backlog stewardship

Key files:
- `README.md`
- `scripts/run_intake_triage.py`
- `governance-states/`
- `governance-records/`

## Getting started

1. Review `ResearchToBacklogOps/AGENTS.md` and `ResearchToBacklogOps/RESEARCH_WORKFLOW_USAGE.md` for the upstream research process.
2. Review `BacklogGovernanceOps/README.md` for the governance workflow and PO quick-start path.
3. Run the intake triage script from `BacklogGovernanceOps` when moving completed research artifacts into governance.

## Root structure

- `BacklogGovernanceOps/` — Product Owner governance and review workflow
- `ResearchToBacklogOps/` — Research pipeline and backlog candidate workflow

## Notes

- No additional root-level markdown files are required at this time.
- The repo should track the existing workspace folders, docs, and output artifacts.
- Local git is initialized in the root, with a `.gitignore` for editor and runtime artifacts.
