# Collision Decisions

## Purpose

This folder stores bounded Product Owner collision-resolution notes for Phase 1.
Use one note when:

- multiple active artifacts from the same research run remain in play, or
- a candidate overlaps an existing backlog item or PBI strongly enough that an explicit PO resolution is required.

Do not create a collision decision note for ordinary single-artifact intake with no overlap concern.

## Naming convention

Use one markdown note per collision group:

- `<research_run_id>__collision_decision.md`

Example:

- `v4F1gFy-hqg_refreshed_2026_04_25__collision_decision.md`

## Required fields

Each note should include:

- `decision_id`
- `research_run_id`
- `decision_status`
- `decision_outcome`
- `po_decided_at`
- `decided_by`
- `related_artifacts`
- `evidence_summary`
- `next_action`

Optional fields:

- `canonical_target`
- `notes`

## Allowed values

### `decision_status`

- `unresolved`
- `resolved`

### `decision_outcome`

- `keep_separate`
- `merge_into_existing_pbi`
- `merge_candidate_artifacts`
- `reject_as_overlap`
- `hold_pending_clarification`

## Phase 1 template

```md
# Collision Decision Note

- decision_id: <unique-id>
- research_run_id: <run-id>
- decision_status: <unresolved|resolved>
- decision_outcome: <keep_separate|merge_into_existing_pbi|merge_candidate_artifacts|reject_as_overlap|hold_pending_clarification>
- po_decided_at: <timestamp>
- decided_by: <name-or-role>

## Related Artifacts

- <artifact-path-1>
- <artifact-path-2>

## Evidence Summary

<brief reason for why this is a collision or overlap case and what the Product Owner considered>

## Canonical Target

<optional target PBI or surviving canonical artifact>

## Next Action

<brief explicit next action>

## Notes

<optional supporting notes>
```

## Operating rule

A collision decision note is a durable record surface. It does not replace the
active governance state folders. Record the decision here, then move or hold the
related artifacts consistently in the live workflow.
