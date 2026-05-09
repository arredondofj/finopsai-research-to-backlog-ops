# Duplicate Log

## Purpose

This folder holds the canonical duplicate-event record for the Backlog Governance Workflow. It exists so duplicate handoff attempts can be tracked as governed exceptions without polluting the active intake flow or being mixed into generic error handling.

## Operating rule

- Use `DUPLICATE_LOG.md` to record duplicate handoff events only.
- Do not use this folder for Product Owner review decisions or publication records.
- Do not treat duplicate events as system failures unless a technical error also occurred.

## Entry format

```md
## DUPLICATE: [task-card-identifier]

- **Detected at:** YYYY-MM-DD HH:MM TZ
- **Source run ID:** [run identifier]
- **Identity key:** [run_id + task_card_identifier]
- **Incoming artifact filename:** [filename]
- **Incoming source path:** [full path in ResearchToBacklogOps]
- **Matched intake artifact:** [full path in governance-states/01_intake/]
- **Duplicate folder path:** [full path in governance-states/01_intake_duplicates/]
- **Action taken:** Routed to duplicate folder, no overwrite
- **Notification status:** Included in run receipt / separately notified / both
- **Notes:** [optional context]
```
