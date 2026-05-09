# FinOpsAI ResearchToBacklogOps Workspace

This workspace supports the research side of the FinOpsAI research-to-backlog flow. It is used to intake source material, route it to the correct research lane, generate durable analysis artifacts, optionally map findings to FinOpsAI, and produce approval-ready backlog-draft artifacts when the workflow reaches that point.

This workspace is not the FinOpsAI implementation repo. It is a research and assessment workspace with controlled outputs under `output/`, preserved source material under `input/`, and workflow notes under `notes/`.

## Start here

If you are new to this workspace, read these files in this order:

1. `README.md` for workspace purpose, folder map, and document routing.
2. `RESEARCH_WORKFLOW_USAGE.md` for the canonical shared workflow, lane taxonomy, artifact naming, gates, and approval rules.
3. `PIPELINE_USAGE.md` if the source is a YouTube transcript or `.vtt` subtitle file.
4. `docs/finopsai_research-to-backlog_workflow.md` if you want the human-readable workflow companion to the canonical guide.
5. `AGENTS.md` for workspace-scoped operating guidance and lane-skill rules used by Codex.

## Quick document map

| File | Purpose | Use first? |
| --- | --- | --- |
| `README.md` | Workspace landing page and navigation | Yes |
| `RESEARCH_WORKFLOW_USAGE.md` | Canonical authority for routing, phases, artifact naming, roadmap-fit, and card-candidate gates | Yes |
| `PIPELINE_USAGE.md` | YouTube transcript lane mechanics, acquisition, cleanup, and transcript-specific analysis flow | Only for transcript work |
| `docs/finopsai_research-to-backlog_workflow.md` | Human-readable workflow companion | Reference |
| `AGENTS.md` | Workspace behavior, lane selection, and editing discipline for Codex | Reference |
| `notes/output_catalog.md` | Durable catalog of completed runs and generated artifacts | Ongoing reference |
| `notes/lessons_learned.md` | Durable workflow lessons with reuse value | As needed |

## Folder map

| Folder | Purpose |
| --- | --- |
| `input/` | Preserved raw source material such as transcripts and subtitle files |
| `output/` | Per-run durable artifacts written as `output/<name>_YYYY_MM_DD/` |
| `docs/` | Human-readable workflow companion materials |
| `notes/` | Catalog and lessons learned |
| `skills/` | Lane-specific and shared authoring skills used by Codex |
| `templates/` | Reusable template content |
| `.codex/` | Workspace-local Codex configuration |

## Workflow summary

1. Register the source and select the correct lane.
2. Produce the lane-specific analysis artifact.
3. Detect any cross-lane follow-on work when the workflow requires it.
4. Update `notes/output_catalog.md`.
5. Decide whether FinOpsAI applicability mapping should proceed.
6. If approved and justified, produce roadmap-fit and ClickUp-ready draft artifacts.
7. Close the run with a canonical run summary in the same run folder.

## Guardrails

- Keep source-specific workflows separate; do not force every source through the same analysis path.
- Preserve original source files in `input/`.
- Write durable run artifacts only under `output/<name>_YYYY_MM_DD/`.
- Treat `RESEARCH_WORKFLOW_USAGE.md` as the controlling authority when documents overlap.
- Do not treat this workspace as the target implementation repo unless explicitly asked.
- Research ends with durable research artifacts and approved draft backlog items, not with ClickUp publication.

## Workspace family

- `ResearchToBacklogOps` (this workspace)
- `BacklogGovernanceOps` (downstream backlog governance bridge)
- `ProductDevelopmentOps` (downstream implementation workflow, when present)

Last updated: 2026-05-04
