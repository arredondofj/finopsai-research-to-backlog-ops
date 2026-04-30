# Intake Duplicates

## Purpose

This folder quarantines duplicate draft artifact handoff candidates detected during Research-to-Backlog closeout. Items placed here must not enter the active governance intake path until the duplicate condition is reviewed and resolved through the duplicate record process.

## What belongs here

- Draft artifact copies blocked from `../01_intake/` because the same identity key already exists in the governed intake path.
- Files routed here during the Phase 4 run-summary approval handoff event.

## Identity rule

Duplicate detection uses the identity key:

- `run_id + task_card_identifier`

This keeps the current model simple and avoids introducing draft-version management unless it becomes operationally necessary later.

## What does not belong here

- Valid first-time handoff artifacts; those belong in `../01_intake/`.
- Product Owner review candidates; those belong in `../02_review/`.
- Error or technical failure records; those belong in the appropriate operational record surface, not here.

## Operating rule

- Never overwrite the existing governed intake artifact when a duplicate is detected.
- Keep the original artifact in `../01_intake/` as the authoritative governed copy.
- Route the duplicate candidate here and record the event in `../../governance-records/duplicate-log/DUPLICATE_LOG.md`.

## Dashboard rule

Artifacts here should appear in the dashboard as `Duplicate detected`, not as `Awaiting intake decision`.
