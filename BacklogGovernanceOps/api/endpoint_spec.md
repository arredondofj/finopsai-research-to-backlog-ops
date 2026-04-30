# FinOpsAI BacklogGovernanceOps — API Endpoint Specification (Draft)

Status: Placeholder — to be completed when Phase 2 is built.

The endpoint defined here will support intake only. It must preserve `governance-states/01_intake/` as the canonical shared state, write receipts to `governance-records/run-notifications/`, and must never bypass `governance-states/03_approved/` for publication or MCP loading.

## Intended endpoint

`POST /intake/deposit`

## Intended request payload fields

- `run_id` — research run identifier
- `artifact_filename` — draft artifact file name following `<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`
- `artifact_content` — full markdown content of the draft artifact
- `deposit_timestamp` — ISO 8601 timestamp
- `source_path` — original file path in `ResearchToBacklogOps/output/`, following `/output/<name>_YYYY_MM_DD/`

## Intended response fields

- `acknowledgment_status` — confirmed / failed
- `intake_path` — path where artifact was deposited in `governance-states/01_intake/`
- `receipt_id` — run notification receipt identifier
- `po_notification_sent` — boolean
- `escalation_triggered` — boolean

## Notes

To be expanded when Phase 2 design is formalized. See `api/README.md` for architectural context.
