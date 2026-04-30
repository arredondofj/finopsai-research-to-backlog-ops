# FinOpsAI Backlog Governance Workflow — Terminology and Structure Companion

This document is the text companion to [`finopsai_backlog_governance_workflow.html`](./finopsai_backlog_governance_workflow.html). It defines the recommended handoff contract between `ResearchToBacklogOps` and `BacklogGovernanceOps`, the records that make the handoff auditable, and the terms the dashboard should use when presenting status across the workflow.

## Recommended handoff model

The best fit for the current working stage is an event-backed folder handoff:

1. Research approves the Phase 4 run summary and triggers handoff.
2. Valid draft artifact files are copied into `governance-states/01_intake/`.
3. Duplicate candidates are routed to `governance-states/01_intake_duplicates/` without overwriting the existing intake artifact.
4. The same run writes one run-level receipt into `governance-records/run-notifications/`.
5. The Product Owner is notified once per run with run ID, artifact count, and any duplicate exceptions.
6. The Product Owner later records a per-artifact intake decision in `governance-records/governance-log/GOVERNANCE_LOG.md`.

This keeps the current low-friction folder model, avoids introducing a second active workflow surface, and still produces the event trail needed for auditability and dashboard visibility.

Current implemented Codex support for the Step 1 and Step 2 intake pass lives in `scripts/run_intake_triage.py`. That runner validates the inbox in dry-run mode by default and appends a triage acknowledgment batch only when run with `--write`.

## Step 1 and Step 2 through Codex

Use this exact sequence when running the intake pass through Codex:

1. Run the dry pass first:
   - Command: `python3 scripts/run_intake_triage.py`
   - Purpose: validate current intake state without writing any acknowledgment record
2. If the dry pass is correct, persist the triage acknowledgment:
   - Command: `python3 scripts/run_intake_triage.py --write`
   - Purpose: append one batch entry to `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`
3. Re-run the dry pass:
   - Command: `python3 scripts/run_intake_triage.py`
   - Purpose: confirm the same artifacts are no longer `New to PO review`

Use this prompt in Codex to start the dry pass:

```md
Run the Backlog Governance intake triage workflow for this workspace in dry-run mode.

Inspect `governance-states/01_intake/` and reconcile intake artifacts against:
- `governance-records/run-notifications/`
- `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`
- `governance-records/governance-log/GOVERNANCE_LOG.md`

Do not write any records yet. Report:
1. Count of new artifacts
2. Artifact status table
3. PO review queue summary
4. Any anomalies
5. Next Step for the Product Owner
```

Use this prompt in Codex after the dry pass is reviewed and approved for persistence:

```md
Persist the Backlog Governance intake triage acknowledgment for the newly identified items.

Use the existing dry-run result as the source of truth.
Append one triage batch entry to:
`governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`

Then present:
1. The exact triage acknowledgment recorded
2. The PO-facing list of surfaced artifacts
3. Any anomalies
4. Next Step for the Product Owner
5. Verification rerun result
```

## Step 1 intake triage handling

### Procedural steps

1. Open the governance workspace and confirm that new draft artifacts are expected in `governance-states/01_intake/`.
2. Run the Step 1 Codex dry pass with `python3 scripts/run_intake_triage.py`.
3. Review the dry-run output and confirm the reported intake batch matches what you expect to see.
4. Check whether any anomalies were reported. If anomalies exist, resolve them before continuing to Step 2.
5. Confirm that the artifact filenames, receipt matches, and deposit timestamps look correct for this intake batch.
6. If the dry-run result is correct, continue to Step 2 and persist the intake-triage acknowledgment.

### Required confirmations

- Draft file matches `/output/<name>_YYYY_MM_DD/<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`.
- Deposit timestamp and artifact count are captured.
- Unreviewed-threshold escalation rule is armed.

### Output

Artifact enters Intake state with receipt, timer, and canonical run-level acknowledgment in place. If threshold is breached later, Scrum Master notification is triggered.

## Step 2 decision handling

Step 2 is explicit and physical:

### Procedural steps

1. Run the Step 2 Codex acknowledgment pass after the Step 1 dry-run result has been reviewed and accepted.
2. Confirm that the triage acknowledgment was appended to `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`.
3. Re-run `python3 scripts/run_intake_triage.py` and confirm the surfaced artifacts are now reported as `Awaiting intake decision` rather than `New to PO review`.
4. Open one draft artifact from `governance-states/01_intake/`.
5. Decide exactly one outcome for that artifact: `Hold`, `Admit to review`, or `Reject`.
6. Record that decision in `governance-records/governance-log/GOVERNANCE_LOG.md`.
7. If the decision is `Admit to review`, move the artifact file from `governance-states/01_intake/` to `governance-states/02_review/`.
8. If the decision is `Hold`, leave the artifact file in `governance-states/01_intake/` and optionally add a companion `<draft-artifact-filename>_hold.md` note beside it.
9. If the decision is `Reject`, record the rejection in `governance-records/governance-log/GOVERNANCE_LOG.md` and do not leave the outcome implied or undocumented.
10. Repeat the same sequence for each remaining artifact in the intake batch until every surfaced item has an explicit decision recorded.

- `Admit to review`
  - Record an intake decision entry in `governance-records/governance-log/GOVERNANCE_LOG.md` with:
    - `Decision: Admit to review`
    - `Next state: governance-states/02_review/`
  - After the log entry is recorded, move the draft artifact file from `governance-states/01_intake/` into `governance-states/02_review/`.
- `Hold`
  - Record an intake decision entry in `governance-records/governance-log/GOVERNANCE_LOG.md` with:
    - `Decision: Hold`
    - `Decision rationale: [reason for hold]`
    - `Next state: governance-states/01_intake/`
  - Leave the draft artifact file in `governance-states/01_intake/`.
  - Optional: add a companion note beside the draft artifact named `<draft-artifact-filename>_hold.md` for quick local visibility.
- `Reject`
  - Record the rejection in `governance-records/governance-log/GOVERNANCE_LOG.md`.
  - Do not leave rejection as an implied folder state with no record.

The governance log is the canonical hold note location. The optional companion `_hold.md` file is only a local convenience reminder, not the system of record.

## Step 3 review and staging handling

### Procedural steps

1. Open one artifact from `governance-states/02_review/`.
2. Review the candidate for publication timing, backlog fit, and duplication risk against existing PBIs.
3. Decide whether the item should move forward now, remain under review, or be explicitly rejected.
4. If the item is not ready to move forward, keep it in review with an explicit recorded reason rather than leaving the status implied.
5. If the item is rejected, record the reason explicitly in the governance log.
6. If the item passes review and should move forward, move it into `governance-states/03_approved/`.
7. Repeat the same sequence for each remaining artifact in `governance-states/02_review/`.

### Checks performed

- Publish now or defer.
- Backlog fit and ordering relevance.
- Collision or duplication risk with existing PBIs.

### State rule

Only items in Approved state are eligible for publication or any future MCP-assisted loading path. Intake and Review states are not publishable.

## Step 4 publication readiness handling

### Procedural steps

1. Open one artifact that is already in `governance-states/03_approved/`.
2. Decide whether the item should be published now or deferred.
3. Check that the item does not duplicate or collide with an existing ClickUp PBI.
4. Identify the exact ClickUp destination backlog, list, and starting status before any publication action is taken.
5. Decide whether the item should be marked backlog-only or as a later sprint candidate at publication time.
6. Confirm the draft is clear enough to publish without heavier pre-publication elaboration.
7. If any readiness check fails, stop publication and continue to Step 5 for pre-publication refinement.
8. If every readiness check passes, continue to Step 6 for publication.

### What must be confirmed before publication

- The item should be published now.
- It is not a duplicate or collision with an existing PBI.
- The correct ClickUp destination backlog, list, and status are identified.
- The item is backlog-only or a candidate for later sprint selection.
- The draft is clear enough for Product Owner publication without heavier pre-publication elaboration.

## Step 7 publication logging handling

### Procedural steps

1. Complete the publication or creation action in ClickUp.
2. Capture the ClickUp URL or ID before moving on to another task.
3. Open `governance-records/governance-log/GOVERNANCE_LOG.md`.
4. Add a publication record for the newly created PBI.
5. Record the source draft artifact path, destination list and status, publication date, publication owner, and sprint candidacy.
6. Include any refinement notes or decision rationale that should remain part of the durable audit trail.
7. Save the governance log entry before leaving the publication workflow.

### What must be recorded after publication

- ClickUp URL or ID.
- Destination list and status used at publication time.
- Linked source draft artifact file path.
- Publication timestamp and publication owner.
- Backlog-only or sprint-candidate flag.
- Any refinement note or decision rationale worth preserving.

## Step 9 sprint-readiness confirmation and handoff

### Procedural steps

1. Review the published PBI and confirm it is ready for Sprint Kanban consideration.
2. Decide explicitly whether the item is sprint-ready now or should remain under backlog stewardship.
3. If it is sprint-ready, update the ClickUp status to `Sprint-Eligible` on the live PBI referenced by the publication record in `governance-records/governance-log/GOVERNANCE_LOG.md`.
4. Leave sprint commitment and actual selection to the downstream Sprint Kanban process.
5. When Sprint Kanban later selects the item, update the same ClickUp PBI status to `Sprint-Selected` and record the selection timestamp and sprint reference in `governance-records/governance-log/GOVERNANCE_LOG.md` so governance can close cleanly.

### Boundary rule

This workflow does not perform sprint commitment, velocity planning, or delivery scheduling. It stops at the prioritized Product Backlog. The PO works with the Sprint team to decide on a Sprint goal to pull PBIs, not push them in from the Product Governance Workflow side.

## Why this is the best fit

- It simplifies the handoff by keeping `governance-states/01_intake/` as the only shared operational inbox.
- It separates delivery acknowledgment from Product Owner business acknowledgment.
- It preserves reopenability because the folder state and record surfaces can be inspected independently.
- It gives the future dashboard two clean data sources: run receipts and governance decisions.
- It isolates duplicates as governed exceptions instead of contaminating active intake.
- It stays compatible with a later API intake path because the endpoint can write to the same folder and receipt model.

## Non-negotiable rules

- Research ends with draft artifacts on the file system.
- `governance-states/01_intake/` is the canonical shared state.
- `governance-states/01_intake_duplicates/` is a quarantine exception surface, not an active governance state.
- Nothing may be published or MCP-loaded unless it originated from `governance-states/03_approved/`.
- One approved draft artifact maps to exactly one published PBI.
- The governance log is the canonical chain of custody from source draft to live ClickUp PBI.

## Handoff event contract

Each research run close creates one handoff event. The event is considered successful only when all of the following are true:

- The Phase 4 run summary has been approved.
- Valid draft artifact file(s) exist in `governance-states/01_intake/`.
- A run receipt exists in `governance-records/run-notifications/`.
- The receipt includes the run ID, deposit timestamp, artifact inventory, duplicate exceptions if any, and notification status.

The handoff event does not mean the Product Owner has reviewed the work. It means delivery into governance succeeded and can be reopened later.

## Acknowledgment model

Use three acknowledgments, not one:

- `Delivery acknowledgment`: automatic, generated at research run close, proves the deposit and notification happened.
- `Codex triage acknowledgment`: recorded when Codex first surfaces deposited intake artifacts to the PO.
- `Governance acknowledgment`: manual, recorded when the Product Owner explicitly admits, holds, rejects, or approves an artifact.

This distinction matters because a dashboard should never infer Product Owner action from a deposit receipt alone.

## Canonical record surfaces

| Surface | Scope | Owner | Purpose |
|---|---|---|---|
| `governance-states/01_intake/` | Live shared state | Research workflow / PO | Current inventory of newly handed-off draft artifacts |
| `governance-states/01_intake_duplicates/` | Governed exception surface | Research workflow / PO | Quarantine for duplicate handoff candidates blocked from active intake |
| `governance-records/run-notifications/` | Run-level event record | Research workflow | Delivery receipt and notification proof |
| `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md` | Intake-triage record | Codex / PO support | Proof that specific intake artifacts were already surfaced to the PO |
| `governance-records/duplicate-log/DUPLICATE_LOG.md` | Duplicate-event record | Research workflow / PO | Canonical trace for duplicate handoff exceptions |
| `governance-records/governance-log/GOVERNANCE_LOG.md` | Artifact-level governance record | Product Owner | Intake, review, publication, and stewardship decisions |

## Dashboard-facing statuses

The dashboard should derive status from records, not manual interpretation:

| Dashboard status | Derived from |
|---|---|
| `Deposited` | Artifact exists in `01_intake` and run receipt exists |
| `PO notified` | Run receipt shows notification sent |
| `New to PO review` | Receipt exists, no triage acknowledgment exists yet, and no PO decision exists |
| `Awaiting intake decision` | Triage acknowledgment exists but no intake decision is logged yet |
| `Held in intake` | Governance log records explicit hold |
| `Admitted to review` | Artifact moved to `02_review` and intake decision logged |
| `Approved for publication` | Artifact moved to `03_approved` and approval logged |
| `Published` | Governance log has publication record with ClickUp ID/URL |
| `Duplicate detected` | Artifact routed to `01_intake_duplicates` and duplicate event logged |
| `Escalated` | Threshold breach recorded from config rules |

## Notification recommendation

The recommended current-state pattern is one Product Owner notification per research run, not one per artifact. That message should include:

- Run ID
- Deposit timestamp
- Artifact count
- Artifact file names
- Duplicate-routed artifact file names, if any
- Intake destination
- Receipt path

This keeps notification volume low while preserving enough detail for reopening.

## Validation approach

The agreed handoff approach should be validated against four checks:

1. `Simplicity`: a run can be handed off without adding a second active state or manual reconciliation step.
2. `Auditability`: a reviewer can trace any published PBI back to its source draft and originating run.
3. `Trackability`: the dashboard can determine whether an item is merely delivered, explicitly held, admitted, approved, or published.
4. `Escalation readiness`: overdue intake items and inbox accumulation can be detected from existing timestamps and config thresholds.

## Implementation note for Phase 2

When API intake is introduced, preserve the same contract:

- Endpoint writes to `governance-states/01_intake/`.
- Endpoint routes duplicates to `governance-states/01_intake_duplicates/` without overwrite.
- Endpoint writes or returns the same receipt data.
- Dashboard logic stays the same because the canonical shared state and record surfaces do not change.
