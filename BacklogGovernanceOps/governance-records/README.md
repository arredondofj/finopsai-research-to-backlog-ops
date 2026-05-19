# Governance Records

## Purpose

This folder groups the durable records that support auditability, reopening, and traceability in the Backlog Governance Workflow. These folders are record surfaces, not active item-state folders.

## Why this folder exists

The Product Owner uses one set of folders for active governance movement and a separate set for durable records. Grouping the records here keeps the operational history distinct from the live state flow and makes the workspace easier to reopen later.

## Record folders

- `card-activity/` — the canonical per-card lifecycle record for workflow 2.
- `collision-decisions/` — bounded collision-resolution notes for unresolved multi-artifact groups or real overlap cases that need explicit PO resolution.
- `governance-log/` — a workspace-level governance summary register for major outcomes and archival rollups.
- `intake-triage/` — Codex-managed acknowledgment records that mark which newly deposited intake artifacts have already been surfaced to the PO.
- `run-notifications/` — auto-acknowledgment receipts that confirm research-run deposit into `../governance-states/01_intake/` and PO notification timing.
- `duplicate-log/` — canonical governed exception log for duplicate handoff events routed away from active intake.

## Operating rule

These folders record what happened; they do not replace the active governance states. Use `card-activity/` as the first reopening point when verifying one card's lifecycle, use `collision-decisions/` when overlap or multi-artifact collision handling is in scope, and use `governance-log/` only when a workspace-level summary view is needed.

## PO guidance

- Record card-specific decisions in the matching file under `card-activity/`.
- Record publication results in the matching card-activity file first.
- Use collision decision notes only when multiple active artifacts remain in play or a real overlap with an existing backlog/PBI needs explicit PO resolution.
- Use intake triage records to distinguish `new to PO review` from `already surfaced by Codex`.
- Use run notifications to confirm that handoff occurred, not to infer PO action.
- Use the duplicate log to record duplicate handoff events, not a generic error log.
- Keep records durable and append-only where practical.
- Do not treat record folders as substitute workflow states.

## Required records before state movement

The active governance folders show where an item currently sits. They do not
replace the durable decision record that must justify that movement.

Use the following rule set for Phase 1:

### 1. Intake -> Review

Before moving an artifact from `governance-states/01_intake/` into
`governance-states/02_review/`, record the Product Owner intake decision in the
matching file under:

- `governance-records/card-activity/`

Minimum expectation:

- the event type is an intake decision
- the decision explicitly supports the movement
- the recorded next state reflects review admission

Without that record, movement into `02_review/` is invalid.

### 2. Review -> Approved

Before moving an artifact from `governance-states/02_review/` into
`governance-states/03_approved/`, record the Product Owner review or approval
decision in the matching file under:

- `governance-records/card-activity/`

Minimum expectation:

- the event type is a review decision or approval
- the decision explicitly supports approval
- the recorded next state reflects approved/publication-ready status

Without that record, movement into `03_approved/` is invalid.

### 3. Approved -> Published / Backlog-Active

Before an approved item is treated as truly published, record the publication
result in:

- `governance-records/governance-log/GOVERNANCE_LOG.md`

Minimum expectation:

- the source draft artifact is identified
- the published ClickUp target is identified
- the destination list/status is recorded
- the publication timestamp is recorded
- the publication owner is recorded

Without that record, publication/backlog-active treatment is invalid even if
the item was already approved.

### 4. Backlog-Active -> Sprint-Eligible

Before a published item is treated as sprint-eligible, record the readiness
confirmation in:

- `governance-records/governance-log/GOVERNANCE_LOG.md`

Minimum expectation:

- the live PBI is identified
- the readiness confirmation is explicit
- the timestamp is recorded
- the confirming owner is recorded

Without that record, sprint-eligible treatment is invalid even if the item
already exists in ClickUp.

## How OpsControl enforces this

OpsControl now checks for durable backing before it accepts certain state
movements as valid.

It will flag explicit issues when it finds:

- an artifact in review without a durable intake decision record
- an artifact in approved without a durable review/approval record
- a published/backlog-active item without a durable publication record
- a sprint-readiness confirmation without durable publication backing

OpsControl will also treat unsupported movement as anomalous mirrored state
rather than as normal workflow progression.

## Practical operator rule

Before moving a governance artifact forward, ask:

1. Did I record the decision in the correct durable surface first?
2. Does the record explicitly support this exact next state?
3. If I rebuild OpsControl now, will the mirror show this movement as valid?

If the answer to any of those is no, record the durable decision first and only
then move the artifact.
