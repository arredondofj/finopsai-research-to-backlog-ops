# Governance Records

## Purpose

This folder groups the durable records that support auditability, reopening, and traceability in the Backlog Governance Workflow. These folders are record surfaces, not active item-state folders.

## Why this folder exists

The Product Owner uses one set of folders for active governance movement and a separate set for durable records. Grouping the records here keeps the operational history distinct from the live state flow and makes the workspace easier to reopen later.

## Record folders

- `governance-log/` — the single canonical record connecting research draft artifacts to published ClickUp PBIs and later stewardship decisions.
- `intake-triage/` — Codex-managed acknowledgment records that mark which newly deposited intake artifacts have already been surfaced to the PO.
- `run-notifications/` — auto-acknowledgment receipts that confirm research-run deposit into `../governance-states/01_intake/` and PO notification timing.
- `duplicate-log/` — canonical governed exception log for duplicate handoff events routed away from active intake.

## Operating rule

These folders record what happened; they do not replace the active governance states. Use the governance log as the first reopening point when verifying publication status, stewardship history, or the source-to-PBI chain of custody.

## PO guidance

- Record publication results immediately in the governance log.
- Use intake triage records to distinguish `new to PO review` from `already surfaced by Codex`.
- Use run notifications to confirm that handoff occurred, not to infer PO action.
- Use the duplicate log to record duplicate handoff events, not a generic error log.
- Keep records durable and append-only where practical.
- Do not treat record folders as substitute workflow states.
