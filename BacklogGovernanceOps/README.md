# FinOpsAI BacklogGovernanceOps Workspace

This workspace supports the Product Owner governed bridge between the FinOpsAI Research-to-Backlog workflow and the FinOpsAI Product Development workflow. It covers PBI intake, review, approval, publication, backlog stewardship, duplicate exception handling, and sprint-readiness confirmation in a lean operating model for a part-time Product Owner.

This workspace is a sibling to `ResearchToBacklogOps`. Research ends with markdown draft artifacts at `/output/<name>_YYYY_MM_DD/<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`; at Phase 4 run-summary approval, research attempts a governed handoff by copying valid draft artifacts into `governance-states/01_intake/` and routing duplicates to `governance-states/01_intake_duplicates/`. This workspace governs what happens from that point through Sprint Kanban selection, while Product Development begins only after PBIs are already published and sprint-eligible.

## PO quick-start — regular working path

1. Run `python3 scripts/run_intake_triage.py` to check `governance-states/01_intake/` for new valid draft artifacts from completed research runs.
2. Check `governance-states/01_intake_duplicates/` and `governance-records/duplicate-log/` for any duplicate exceptions raised at handoff.
3. Record each card decision in the matching file under `governance-records/card-activity/`; move admitted artifacts to `governance-states/02_review/` and leave held artifacts in `governance-states/01_intake/`.
4. Review admitted candidates in `governance-states/02_review/` and move items that pass review into `governance-states/03_approved/`; record explicit rejection reasons rather than leaving outcomes implied.
5. Complete the publication readiness check before publishing.
6. Publish or create the PBI in ClickUp from `governance-states/03_approved/`.
7. Record the publication result in the matching card-activity file and optionally add a workspace-level summary entry in `governance-records/governance-log/GOVERNANCE_LOG.md`.
8. Perform ongoing backlog stewardship until the PBI reaches sprint-eligible status.
9. Confirm sprint-readiness by updating the live ClickUp PBI referenced from the matching card-activity file to `Sprint-Eligible`.

## Folder map

| Folder | Purpose | PO touches regularly |
|---|---|---|
| `README.md` | Primary quick-start and workspace map for the PO | Yes |
| `docs/` | Process authority documents, workflow HTML, terminology companion | Reference only |
| `governance-states/` | Parent folder for active workflow states used for intake, review, and approval flow | Yes |
| `governance-records/` | Parent folder for durable records, receipts, and governance audit history | Yes |
| `config/` | Configurable operating parameters — escalation threshold, sprint cycle, inbox ceiling | As needed |
| `api/` | Phase 2 reserved — API endpoint specs and agentic path definitions | No — future state |
| `notes/` | Durable lessons learned as the workflow matures | As needed |

> Sprint planning artifacts, delivery records, and velocity data belong in the Product Development workspace. Research run source files and original draft artifacts belong in `ResearchToBacklogOps/output/`. This workspace receives governed copies for `governance-states/01_intake/`, quarantined duplicate copies for `governance-states/01_intake_duplicates/`, and governed movement through `governance-states/02_review/` and `governance-states/03_approved/`; it does not own the upstream research run source.

## Workspace family

- `ResearchToBacklogOps` (upstream)
- `BacklogGovernanceOps` (this workspace)
- `ProductDevelopmentOps` (downstream — future)

## Guardrails

- The `governance-states/01_intake/` folder is the canonical shared state for both the human PO path and the future agentic path.
- Intake triage should be run through `scripts/run_intake_triage.py`; dry run first, then `--write` when the PO-facing triage batch should be recorded.
- Research ends with draft artifacts on the file system, not published PBIs.
- Nothing may be published or MCP-loaded unless it originated from `governance-states/03_approved/`.
- One approved draft artifact maps to one published PBI; never silently collapse multiple drafts into one PBI.
- `governance-records/card-activity/` is the canonical per-card lifecycle record for workflow 2.
- PBI publication creates the real PBI in ClickUp for the first time.
- Product Development begins from already-published, sprint-eligible PBIs; it does not create them.

Last updated: 2026-04-26
