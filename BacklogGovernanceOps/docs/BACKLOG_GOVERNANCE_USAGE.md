# FinOpsAI Backlog Governance — Usage Reference

This document is the controlling operating reference for the BacklogGovernanceOps workspace. It defines how the Product Owner and supporting automation should handle handoff, governance movement, publication, and traceability.

## Recommended operating approach

Use a folder-based handoff with event-backed records.

- Research approves the Phase 4 run summary and triggers handoff.
- Research copies valid draft artifact files into `governance-states/01_intake/`.
- Research routes duplicate candidates into `governance-states/01_intake_duplicates/` without overwrite.
- Research writes one run-level receipt into `governance-records/run-notifications/`.
- The Product Owner is notified once per run.
- The Product Owner records explicit per-artifact governance decisions in the matching file under `governance-records/card-activity/`.

This is the default operating model until a later API intake path is built.

## Required workflow sequence

1. Research approves the Phase 4 run summary.
2. Research copies valid draft artifact(s) into `governance-states/01_intake/`.
3. Research routes duplicate candidates into `governance-states/01_intake_duplicates/`.
4. Research writes the run notification receipt.
5. Product Owner reviews the intake batch.
6. Product Owner records a hold or admit decision for each valid artifact.
7. Admitted artifacts move to `governance-states/02_review/`.
8. Approved artifacts move to `governance-states/03_approved/`.
9. Product Owner publishes only from `governance-states/03_approved/`.
10. Product Owner records publication and later stewardship in the matching card-activity file.

## Handoff decision rule

Treat the handoff as complete when Phase 4 run-summary approval plus deposit plus receipt plus notification are all confirmed. Do not treat handoff completion as Product Owner review completion.

## Acknowledgment rule

Use three separate acknowledgments:

- `System acknowledgment`: the run receipt confirms delivery and PO notification.
- `Codex triage acknowledgment`: the intake triage log confirms that specific intake artifacts were surfaced to the PO.
- `PO acknowledgment`: the matching card-activity file confirms an explicit intake decision.

Do not merge these concepts. Keeping them separate prevents false visibility in the dashboard.

## Product Owner intake decision rule

Every artifact in `governance-states/01_intake/` must eventually have one explicit intake outcome:

- `Hold`
- `Admit to review`
- `Reject`

Passive aging is not a valid governance state.

For `Hold`, the canonical note location is the matching file under `governance-records/card-activity/`. A companion `_hold.md` file beside the draft artifact in `01_intake` is optional and only for local visibility.

## Duplicate handling rule

- Duplicate detection uses `run_id + task_card_identifier`.
- Never overwrite an existing artifact in `governance-states/01_intake/`.
- Route duplicate candidates to `governance-states/01_intake_duplicates/`.
- Record the event in `governance-records/duplicate-log/DUPLICATE_LOG.md`.
- Treat duplicates as governed exceptions, not generic system failures.

## Logging rules

### Run notification receipt

Each research run must create one receipt file in `governance-records/run-notifications/` with:

- Run ID
- Research run close timestamp
- Run summary approval timestamp
- Deposit timestamp
- Artifact count
- Artifact filenames
- Duplicate-routed artifact filenames, if any
- Source path(s)
- Intake destination path
- Product Owner notification timestamp
- Acknowledgment status
- Overall handoff status

### Card activity

Use the matching file under `governance-records/card-activity/` to record:

- Intake holds
- Admissions to review
- Rejections
- Approval decisions
- Publication records
- Significant stewardship updates

### Governance summary register

Use `governance-records/governance-log/GOVERNANCE_LOG.md` only when a
workspace-level summary entry is helpful in addition to the per-card record.

### Intake triage log

Use `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md` to record:

- The first time Codex identifies an intake artifact as new to PO review
- The receipt files and run IDs tied to that triage batch
- The exact artifact paths surfaced in that batch

The implemented runner is `scripts/run_intake_triage.py`. Use dry run first; use `--write` only when the triage result should be persisted.

### Duplicate log

Use `governance-records/duplicate-log/DUPLICATE_LOG.md` to record:

- Duplicate identity key
- Source run ID
- Incoming artifact path
- Matched intake artifact path
- Duplicate folder path
- Action taken
- Notification status

## Dashboard derivation rules

The dashboard should read workflow status from the file system and records using these rules:

- If an artifact is in `01_intake`, a receipt exists, and no triage record exists yet, show `New to PO review`.
- If an artifact is in `01_intake` and a triage record exists but no PO decision exists, show `Awaiting intake decision`.
- If an artifact is in `01_intake_duplicates` and a duplicate log entry exists, show `Duplicate detected`.
- If a hold is recorded in card activity, show `Held in intake`.
- If the artifact is in `02_review`, show `In review`.
- If the artifact is in `03_approved`, show `Approved for publication`.
- If a publication record exists with ClickUp ID or URL, show `Published`.
- If age or count thresholds are exceeded, show `Escalated`.

## Validation checklist

Use this checklist to validate the handoff approach in operation:

- A deposited artifact can be found in `01_intake` from the receipt alone.
- A newly deposited artifact can be distinguished from an already surfaced artifact using the intake triage log.
- A duplicate-routed artifact can be found in `01_intake_duplicates` from the duplicate log alone.
- A receipt can be traced to the run ID and artifact inventory.
- A Product Owner intake decision can be found in the matching card-activity file for each reviewed artifact.
- A published PBI can be traced to one approved source draft artifact.
- Overdue unreviewed items can be identified from timestamps and config thresholds.

## Fixed constraints

- Research ends with draft artifacts on the file system at `/output/<name>_YYYY_MM_DD/<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`.
- `governance-states/01_intake/` is the canonical shared state.
- `governance-states/01_intake_duplicates/` is the canonical duplicate quarantine surface.
- Only `governance-states/03_approved/` may be used for publication or MCP loading.
- One approved draft artifact maps to exactly one published PBI.
- `governance-records/card-activity/` remains the canonical per-card trace to the live ClickUp PBI.
