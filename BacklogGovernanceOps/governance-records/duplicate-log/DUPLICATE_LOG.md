# FinOpsAI Duplicate Log

This file is the canonical record of duplicate handoff events detected when Research-to-Backlog attempts to deposit draft artifacts into `governance-states/01_intake/`.

## How to use

- Add one entry for each duplicate candidate routed to `../../governance-states/01_intake_duplicates/`.
- Record duplicate events as governed exceptions, not as publication decisions or system failures.
- Keep entries append-only where practical.

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
