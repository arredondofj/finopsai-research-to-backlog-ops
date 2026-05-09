# Card Activity

## Purpose

This folder is the canonical per-card lifecycle record for workflow 2.

Use one activity file per draft task card to keep all card-specific governance
history in one place without mixing it with run-level handoff receipts or
duplicate exception logs.

## Why this exists

`run-notifications/` is run-level and may describe multiple cards at once.
`intake-triage/` is batch-level and confirms only that Codex surfaced cards to
the Product Owner. `duplicate-log/` is exception-only.

This folder exists so a reviewer can open one file and answer:

- where this card came from,
- when it was deposited,
- when it was surfaced to the PO,
- what decision was made,
- whether it moved to review or approval,
- whether it was published,
- and what later stewardship happened.

## File naming

Use one file per card:

`<draft-artifact-stem>__activity.md`

Keep the file name derived from the draft artifact so the relationship is easy
to scan and script.

## Entry guidance

Each card activity file should include:

- source draft artifact path
- research run ID when known
- links to the run receipt and intake-triage acknowledgment when present
- append-only activity entries in chronological order

Typical event types:

- `deposit`
- `triage_acknowledgment`
- `intake_decision`
- `review_decision`
- `approval`
- `publication`
- `stewardship_update`
- `rejection`

## Canonical rule

Record card-specific governance decisions here first.

Use `governance-log/GOVERNANCE_LOG.md` only as a workspace-level summary
register for major outcomes when needed. Do not use it as the primary place to
understand one specific card.

## Suggested structure

```md
# Card Activity - <draft artifact filename>

- **Source draft artifact:** <full path>
- **Research run ID:** <run identifier when known>

## Activity Entries

### YYYY-MM-DD HH:MM TZ - Deposited to intake
- **Event type:** deposit
- **Recorded by:** Research workflow
- **Run receipt:** <path>
- **State after event:** `governance-states/01_intake/`
- **Notes:** <optional>

### YYYY-MM-DD HH:MM TZ - Surfaced to PO
- **Event type:** triage_acknowledgment
- **Recorded by:** Codex
- **Triage record:** <path>
- **State after event:** `governance-states/01_intake/`

### YYYY-MM-DD HH:MM TZ - Intake decision
- **Event type:** intake_decision
- **Recorded by:** <PO identifier>
- **Decision:** Hold | Admit to review | Reject
- **Decision rationale:** <brief reason>
- **State after event:** `governance-states/01_intake/` | `governance-states/02_review/` | closed
```
