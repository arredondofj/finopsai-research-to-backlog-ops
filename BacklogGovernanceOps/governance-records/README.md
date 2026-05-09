# Governance Records

## Purpose

This folder groups the durable records that support auditability, reopening, and traceability in the Backlog Governance Workflow. These folders are record surfaces, not active item-state folders.

## Why this folder exists

The Product Owner uses one set of folders for active governance movement and a separate set for durable records. Grouping the records here keeps the operational history distinct from the live state flow and makes the workspace easier to reopen later.

## Record folders

- `card-activity/` — the canonical per-card lifecycle record for workflow 2.
- `governance-log/` — a workspace-level governance summary register for major outcomes and archival rollups.
- `intake-triage/` — Codex-managed acknowledgment records that mark which newly deposited intake artifacts have already been surfaced to the PO.
- `run-notifications/` — auto-acknowledgment receipts that confirm research-run deposit into `../governance-states/01_intake/` and PO notification timing.
- `duplicate-log/` — canonical governed exception log for duplicate handoff events routed away from active intake.

## Operating rule

These folders record what happened; they do not replace the active governance states. Use `card-activity/` as the first reopening point when verifying one card's lifecycle, and use `governance-log/` only when a workspace-level summary view is needed.

## PO guidance

- Record card-specific decisions in the matching file under `card-activity/`.
- Record publication results in the matching card-activity file first.
- Use intake triage records to distinguish `new to PO review` from `already surfaced by Codex`.
- Use run notifications to confirm that handoff occurred, not to infer PO action.
- Use the duplicate log to record duplicate handoff events, not a generic error log.
- Keep records durable and append-only where practical.
- Do not treat record folders as substitute workflow states.
