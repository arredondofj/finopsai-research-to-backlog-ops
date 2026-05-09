# Approved

## Purpose

This folder holds draft artifacts that the Product Owner has approved for publication. Items here have passed review and are ready to be published as real PBIs in ClickUp for the first time.

> Only items in this folder may be published manually or loaded by a future MCP agent. No draft artifact may be published from `../01_intake/` or `../02_review/` directly. This folder is the enforcement point for publication governance.

## What belongs here

- Draft artifacts moved from `../02_review/` following explicit PO approval.
- Items that have passed the publication readiness check.

## PO publication actions

- Complete the publication readiness checklist before publishing each item; see `docs/BACKLOG_GOVERNANCE_USAGE.md`.
- Publish or create the PBI in ClickUp; the manual path is the default.
- Record the publication result in the matching file under `../../governance-records/card-activity/` immediately after publishing.
- After recording, archive or mark the source draft artifact as published; do not delete it without a card-activity entry confirming publication.

## One draft to one PBI rule

Each approved draft artifact maps to exactly one published PBI. Multiple approved drafts must never be silently collapsed into a single PBI. If consolidation appears warranted, record the decision explicitly in the matching card-activity file before acting.

## Future MCP path

When Phase 2 agentic publication is enabled, the MCP agent will read only from this folder. The PO confirms before the agent commits any publication action. The folder remains the sole publication source in both Phase 1 and Phase 2.
