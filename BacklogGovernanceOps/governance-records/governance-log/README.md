# Governance Summary Register

## Purpose

This folder holds the workspace-level governance summary register.

Use it for major outcome summaries, publication rollups, and archive snapshots.
Do not use it as the primary per-card lifecycle record.

## Relationship to other record surfaces

- `../card-activity/` is the canonical per-card activity surface.
- `../run-notifications/` is the run-level handoff receipt surface.
- `../intake-triage/` is the Codex intake acknowledgment surface.
- `../duplicate-log/` is the duplicate-exception surface.

## When to write here

Write here when a major governance milestone should also appear in one
workspace-level summary register, for example:

- publication completed
- large-scale archive note
- notable stewardship rollup

## Suggested entry structure

```md
## YYYY-MM-DD - <short summary title>

- **Event type:** publication | stewardship_rollup | archive_note
- **Source card activity:** <path in ../card-activity/>
- **Related draft artifact:** <path>
- **Related ClickUp URL/ID:** <when applicable>
- **Summary:** <brief note>
```
