# Run Notifications

## Purpose

This folder holds auto-acknowledgment receipts generated at research run close. Each receipt confirms that a research run deposited draft artifacts to `../../governance-states/01_intake/` and that the handoff notification was sent to the PO.

## Important distinction

These receipts record that a handoff was initiated and received, not that the PO reviewed or acted on the intake. Card-specific lifecycle decisions belong in `../card-activity/`. Workspace-level summaries, when needed, belong in `../governance-log/GOVERNANCE_LOG.md`.

## Receipt naming convention

`run_notification_<run-ID>_YYYY_MM_DD.md`

## Required receipt content

- Run ID
- Research run close timestamp
- Number of draft artifacts deposited
- List of deposited artifact file names
- List of duplicate-routed artifact file names, if any
- Deposit destination: `governance-states/01_intake/`
- PO notification timestamp
- Auto-acknowledgment status: confirmed / failed
- Overall handoff status: completed / completed_with_duplicates / partial_notification_failure / failed

## Escalation reference

If a receipt shows artifacts deposited but the matching card-activity file shows no corresponding intake decision after the configured threshold, escalation to the Scrum Master should be triggered. See `config/governance_config.md` for threshold values.
