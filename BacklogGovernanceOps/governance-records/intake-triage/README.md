# Intake Triage Records

## Purpose

This folder holds Codex-managed acknowledgment records for the intake inbox. These records answer one narrow operational question:

`Which draft artifacts in governance-states/01_intake/ have already been surfaced to the Product Owner for review?`

## Why this exists

Run notifications confirm that research deposited artifacts and sent a handoff notification. They do not tell Codex whether a later intake-check run has already presented those artifacts to the PO.

This folder closes that gap without turning acknowledgment into a business decision:

- `Run notification` = research-to-governance delivery acknowledgment.
- `Intake triage acknowledgment` = Codex surfaced specific intake artifacts to the PO.
- `Governance log entry` = the PO made a business decision.

## Operating rule

These records are append-only where practical. Codex writes one triage batch entry the first time it identifies intake artifacts as `new to PO review` during a given pass.

The implemented triage runner is:

- `scripts/run_intake_triage.py`

Default behavior is a dry run. Use `--write` only when you want Codex to persist the acknowledgment batch.

Do not use this folder to record:

- admission to review
- hold decisions
- rejection decisions
- ClickUp publication

Those remain governed by `../governance-log/GOVERNANCE_LOG.md`.
