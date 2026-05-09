# BacklogGovernanceOps Agent Guidance

## Scope

This file applies to the entire `BacklogGovernanceOps` workspace.

Use this workspace for Product Owner governed backlog intake, review,
approval, publication tracking, duplicate handling, intake-triage
acknowledgment, and governance records. Do not treat this workspace as the
upstream research workspace or the downstream implementation workspace.

## Document Authority

- `docs/BACKLOG_GOVERNANCE_USAGE.md` is the controlling operating reference
  for handoff, governance movement, publication boundaries, and traceability.
- `docs/finopsai_backlog_governance_workflow.md` is the human-readable
  workflow companion and Codex usage guide.
- `README.md` is the landing page and quick-start for workspace navigation.
- If these documents appear to conflict on operating rules, follow
  `docs/BACKLOG_GOVERNANCE_USAGE.md`.

## Workspace Boundaries

- Research ends upstream with durable draft artifacts and governed handoff.
- This workspace begins when valid draft artifacts are copied into
  `governance-states/01_intake/` and corresponding run receipts are written to
  `governance-records/run-notifications/`.
- This workspace does not own research source files stored in
  `ResearchToBacklogOps/output/`.
- This workspace does not own implementation delivery, sprint commitment, or
  product-development execution.

## State Model

- `governance-states/01_intake/` is the canonical shared intake state.
- `governance-states/01_intake_duplicates/` is the duplicate quarantine
  surface.
- `governance-states/02_review/` is the active review state.
- `governance-states/03_approved/` is the only publishable state.
- Never invent additional active workflow states unless the user explicitly
  asks to change the workflow design.

## Operating Rules

- Use `scripts/run_intake_triage.py` for deterministic intake triage.
- Run intake triage in dry-run mode first; use `--write` only when the
  acknowledgment batch should be persisted.
- Record Product Owner card decisions in the matching file under
  `governance-records/card-activity/`.
- Use `governance-records/governance-log/GOVERNANCE_LOG.md` only for
  workspace-level summary entries when needed.
- Record duplicate events in
  `governance-records/duplicate-log/DUPLICATE_LOG.md`.
- Treat receipts, triage acknowledgments, governance decisions, and duplicate
  records as distinct record surfaces. Do not collapse them into one log.
- Preserve one approved draft artifact to one published PBI.
- Never publish or simulate publication from `01_intake/` or `02_review/`.
- Never overwrite an intake artifact to handle a duplicate. Route duplicates
  to `01_intake_duplicates/` and record the event.

## Editing Discipline

- Keep changes narrow and workflow-specific.
- Preserve the existing folder-based handoff model unless the user explicitly
  asks for a redesign.
- Prefer updating the authoritative docs over scattering rules across many
  files.
- Do not remove durable governance records unless the user explicitly asks.
- Do not rewrite historical logs for style or consistency alone.
- If a workflow change affects state transitions, receipt fields, or logging
  rules, update both the controlling usage doc and the human-readable workflow
  companion.

## Automation Discipline

- Treat `api/` as future-state design unless the user explicitly asks to build
  Phase 2.
- Treat `config/governance_config.md` as the place for adjustable operating
  parameters, not the operating docs.
- If automation behavior depends on file naming or record formats, validate the
  current docs before changing code.
- Keep scripts deterministic and file-system grounded. Do not add hidden
  services, background jobs, or network calls without explicit approval.

## Skills

- The `skills/` folder in this workspace is reserved for future
  governance-specific Codex skills.
- Add a workflow-local skill only when a repeated governance task needs a
  stable reusable instruction surface that is distinct from the shared docs.
- Until then, rely on `README.md`,
  `docs/BACKLOG_GOVERNANCE_USAGE.md`, and
  `docs/finopsai_backlog_governance_workflow.md`.
