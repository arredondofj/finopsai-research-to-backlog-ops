---
name: backlog-intake-triage
description: Review BacklogGovernanceOps intake draft artifacts, reconcile them against receipts and governance records, assess task-card context quality, and recommend whether the Product Owner should hold, admit to review, or reject an intake item. Use when working the 01_intake backlog-governance inbox or preparing daily intake review summaries.
---

# Backlog Intake Triage

## Purpose

Use this skill to interrogate intake draft artifacts in
`BacklogGovernanceOps/governance-states/01_intake/` before the Product Owner
makes an explicit governance decision.

This skill adds one assessment layer at the start of the current governance
workflow:

1. validate intake state and record alignment,
2. assess the task card's context quality and decision-readiness,
3. recommend `Hold`, `Admit to review`, or `Reject`,
4. then let the Product Owner decide whether to record that outcome in the
   matching file under `governance-records/card-activity/`.

This skill supports governance decisions. It does not make them automatically.

## Read first

Read these files before using the skill:

- `BacklogGovernanceOps/AGENTS.md`
- `BacklogGovernanceOps/docs/BACKLOG_GOVERNANCE_USAGE.md`
- `BacklogGovernanceOps/docs/finopsai_backlog_governance_workflow.md`

Use `BacklogGovernanceOps/scripts/run_intake_triage.py` as the source of truth
for receipt/triage/governance-state reconciliation.

Use `BacklogGovernanceOps/scripts/run_daily_intake_review.py` when you need the
added context assessment pass for new or waiting intake items.

## When to use

Use this skill when the user asks to:

- review new intake cards,
- assess whether intake artifacts are ready for Product Owner review,
- produce a PO-facing intake queue summary,
- run a daily or batch intake assessment,
- or recommend `Hold`, `Admit to review`, or `Reject` without yet moving files.

Do not use it for:

- research-lane analysis in `ResearchToBacklogOps`,
- publication from `03_approved/`,
- duplicate logging by itself,
- or downstream product-development work.

## Inputs to inspect

For each intake run, inspect:

- `governance-states/01_intake/`
- `governance-records/run-notifications/`
- `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`
- `governance-records/card-activity/`
- `governance-records/duplicate-log/DUPLICATE_LOG.md` when duplicate context is relevant

## Assessment workflow

### Step 1: Reconcile intake state

Run the deterministic intake triage runner first:

```bash
python3 BacklogGovernanceOps/scripts/run_intake_triage.py
```

If the dry-run output shows anomalies, treat the intake state as not clean
enough for confident recommendation. Recommend `Hold` unless the artifact is so
malformed that `Reject` is clearly justified.

Use `--write` only when the user explicitly wants the triage acknowledgment
persisted.

### Step 2: Assess context quality

For each intake card being assessed, check whether the card contains enough
context for the Product Owner to make a bounded governance decision.

At minimum, inspect whether the card has:

- a clear title
- a concrete problem statement
- an expected outcome
- business context
- scoped inclusions and exclusions
- acceptance criteria
- constraints
- dependencies or references
- explicit subtasks or next-step structure when the workflow expects them

Also assess whether the content is:

- specific rather than generic
- traceable to research or repo evidence
- scoped to one primary work item
- bounded enough to avoid hidden implementation sprawl
- aligned with repo or workflow constraints already cited in the card

### Step 3: Classify decision-readiness

Use this heuristic:

- `Strong context`
  - core sections are present
  - the task is bounded
  - references are concrete
  - acceptance criteria are decision-useful
  - no major ambiguity blocks PO intake review
- `Partial context`
  - the card is directionally useful
  - but one or more important sections are weak, vague, or under-evidenced
  - the PO may need clarification before admitting it to review
- `Weak context`
  - critical sections are missing
  - the task boundary is unclear
  - or the card is too malformed to govern reliably

### Step 4: Recommend an intake outcome

Map the assessment to a recommendation:

- `Admit to review`
  - use when context is strong and the item looks governable
- `Hold`
  - use when the item is promising but needs clarification, anomaly cleanup, or
    queue timing delay before moving into `02_review/`
- `Reject`
  - use when the card is too weak, malformed, duplicated in substance, or too
    poorly bounded to govern responsibly

Keep the recommendation separate from the Product Owner decision.

## Required output

When using this skill, present a PO-facing report with these sections:

1. `Intake Summary`
2. `Artifact Status`
3. `Context Assessment`
4. `Recommendation`
5. `Rationale`
6. `PO Next Step`
7. `Record Update Guidance`

For each card, include:

- artifact filename
- current intake status
- context level: `Strong`, `Partial`, or `Weak`
- recommended decision: `Admit to review`, `Hold`, or `Reject`
- the specific reasons behind that recommendation

## Daily review mode

For a daily intake sweep, prefer:

```bash
python3 BacklogGovernanceOps/scripts/run_daily_intake_review.py
```

This should be treated as a read-only assessment pass. It helps the Product
Owner see:

- newly deposited artifacts,
- items still awaiting intake decision,
- context-quality gaps,
- and which items look ready for review versus clarification or rejection.

Scheduling is external to the skill. Use the script as the execution surface
for a future `launchd`, cron, CI, or workflow-triggered daily review.

## Guardrails

- Do not move artifacts between governance states unless the user explicitly
  asks you to carry out the PO decision.
- Do not write card-activity decisions automatically from your recommendation.
- Do not collapse system acknowledgment, triage acknowledgment, and PO
  decision into one action.
- Do not recommend `Admit to review` when the card is materially under-scoped
  or when intake-state anomalies make the record chain unreliable.
- Do not publish or simulate publication from this skill.

## Handoff objective

The goal is to give the Product Owner a cleaner decision surface at intake:
not just whether an artifact exists, but whether it contains enough bounded,
evidence-backed context to enter formal review.
