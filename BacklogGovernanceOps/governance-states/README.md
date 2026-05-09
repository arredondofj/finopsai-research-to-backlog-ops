# Governance States

## Purpose

This folder groups the active workflow-state folders used by the Product Owner governance path. These are the working states where draft artifacts move as they progress from intake through review to publication readiness. For additional usage details, reference `docs/finopsai_backlog_governance_workflow.html`, `Workflow Usage` → `See Workflow Usage Details` → `Folder And State Flow Map`.

## Why this folder exists

The Backlog Governance Workflow depends on explicit, reopenable state transitions. Grouping the state folders here makes the active flow easier to scan and keeps it separate from governance records such as logs and run receipts.

## State folders

- `01_intake/` — canonical intake inbox for newly deposited research draft artifacts.
- `01_intake_duplicates/` — quarantine folder for duplicate handoff candidates that must not enter active intake.
- `02_review/` — Product Owner admitted candidates under active review.
- `03_approved/` — Product Owner approved items that are eligible for publication.

## Operating rule

Only items that originated in this state flow may move forward through governance. The intake state remains the canonical shared state for both the human Product Owner path and the future agentic path. The duplicates folder is an exception surface, not a working review state. Nothing may be published or MCP-loaded unless it has reached the approved state.

## PO guidance

- Work left to right: `01_intake`, `02_review`, `03_approved`.
- Treat `01_intake_duplicates/` as an exception surface, not as a review state.
- Do not skip a state.
- Do not silently collapse multiple approved drafts into one PBI.
- Reopen status from the matching card-activity file when needed, but treat these folders as the live working states.
