# Intake

## Purpose

This folder is the designated intake inbox for valid draft artifacts produced by the FinOpsAI Research-to-Backlog workflow. It is the canonical shared state for both the human Product Owner path (Phase 1) and the future agentic path (Phase 2). Everything from research lands here first after Phase 4 run-summary approval, and research ends here with governed file-system draft artifacts rather than published PBIs.

## What belongs here

- Draft artifact `.md` files copied here at Phase 4 run-summary approval closeout.
- Files named with the pattern `<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`.
- Artifacts sourced from `/output/<name>_YYYY_MM_DD/` in `ResearchToBacklogOps`.
- Only first-time valid handoff artifacts that do not collide with an existing intake identity key.

## What does not belong here

- Files already admitted to review; move those to `../02_review/`.
- Duplicate handoff candidates; those belong in `../01_intake_duplicates/`.
- Governance log entries; those belong in `../../governance-records/governance-log/`.
- Research run notification receipts; those belong in `../../governance-records/run-notifications/`.

## How items arrive (Phase 1 — current)

- The research workflow approves the Phase 4 run summary and then attempts handoff.
- Valid draft artifact(s) are copied here from the research workspace.
- Duplicate candidates are routed to `../01_intake_duplicates/` instead of being placed here.
- A single notification is sent to the PO referencing the run ID and artifact count, not one notification per artifact.
- An auto-acknowledgment receipt is written to `../../governance-records/run-notifications/` confirming deposit timestamp, run ID, and any duplicate exceptions.

## How items will arrive (Phase 2 — future)

- Draft artifacts will be posted to a defined API endpoint.
- The endpoint deposits to this same folder and returns a structured acknowledgment.
- Both human and agentic paths converge here; the intake folder is path-agnostic.

## PO intake action

- Run `../../scripts/run_intake_triage.py` in dry-run mode to identify items that are new to PO review.
- Use `../../scripts/run_intake_triage.py --write` only when the surfaced batch should be acknowledged in `../../governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`.
- Review intake contents at the next available governance session.
- Admit selected artifacts to `../02_review/` as a deliberate batch decision.
- For `Hold`, record the hold decision and rationale in `../../governance-records/governance-log/GOVERNANCE_LOG.md` and leave the draft artifact in place.
- Optional: add a companion `_hold.md` note beside the draft artifact for local visibility, but do not use filename edits as the canonical record.
- Do not delete items from intake without a recorded reason.

## Identity and freeze rule

- Handoff identity uses `run_id + task_card_identifier`.
- Once a draft artifact has been handed off here, treat it as frozen for governance purposes.
- Any later research-side change requires a new approved run summary and a new handoff event, not a silent overwrite.

## Escalation rules

- Any draft artifact remaining unreviewed beyond the configured sprint-cycle threshold triggers a Scrum Master notification.
- The threshold is defined in `config/governance_config.md`.
- The default threshold is one full sprint cycle from deposit timestamp.
- If total unreviewed item count exceeds the configured ceiling, the Scrum Master is notified independently of age.
- Escalation exists to assist the PO or remove roadblocks, not to bypass PO governance.
