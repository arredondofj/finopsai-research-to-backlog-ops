# ResearchToBacklogOps Agent Guidance

## Scope

This file applies to the entire `ResearchToBacklogOps` workspace.

Use this workspace for transcript ingestion, cleanup, technical analysis, repo-application reports, reusable prompts, notes, and run catalogs. Do not treat this workspace as the target software repo for implementation unless the user explicitly asks to modify this workspace.

## Transcript Pipeline Rules

- Use the `youtube-transcript-pipeline` skill for transcript cleanup, transcript analysis, and repo-application assessments.
- Preserve source transcript files in `input/`.
- Write generated transcript artifacts to per-run folders under `output/`.
- Create the run folder as `output/<name>_YYYY_MM_DD/`.
- Use the date of the first durable artifact for the run as the folder date.
- Save all artifacts for that run inside the run folder using the same `<name>` prefix.
- Update `notes/output_catalog.md` after each transcript run.
- Keep catalog entries concise and referential. Do not paste full transcript text or long analysis excerpts into the catalog.
- Do not summarize or analyze during cleanup.
- Preserve timestamps during cleanup unless the user explicitly asks to remove them.
- Correct only high-confidence transcription defects. If uncertain, preserve the original wording.

## Research Lane Skills

- Use `skills/research-markdown-authoring/SKILL.md` whenever a durable
  research markdown artifact is written or revised under `output/`.
- Use `skills/youtube-transcript/SKILL.md` for the YouTube transcript lane.
- Use `skills/github-repo-assessment/SKILL.md` for the GitHub repository lane.
- Use `skills/web-source-research/SKILL.md` for general web articles,
  documentation pages, benchmark posts, announcements, and other internet
  sources that are not primarily YouTube transcripts or GitHub repositories.
- Use `skills/business-requirement-triage/SKILL.md` for the business requirement lane.
- Use `skills/accounting-domain-review/SKILL.md` for the accounting/bookkeeping domain lane.
- Use `skills/product-workflow-analysis/SKILL.md` for the product workflow lane.
- Treat the six lane skills as source-routing skills and
  `research-markdown-authoring` as the shared artifact-writing skill. Shared
  roadmap-fit, approval, and ClickUp-card behavior still comes from
  `RESEARCH_WORKFLOW_USAGE.md` and
  `finopsai_research-to-backlog_workflow.md`.

## Phase A: Transcript-Only Workflow

- Read the raw transcript from `input/`.
- Save the cleaned transcript to `output/<name>_YYYY_MM_DD/<name>_cleaned_YYYY_MM_DD.txt`.
- Save the analysis report to `output/<name>_YYYY_MM_DD/<name>_analysis_YYYY_MM_DD.md`.
- Update `notes/output_catalog.md` with the generated files, high-level topic, practical relevance, caveats, and verification notes.
- Do not modify unrelated files.

## Phase B: Repo-Application Workflow

- Treat Phase B as an assessment workflow, not an implementation workflow.
- Read the cleaned transcript and analysis report from this workspace.
- When FinOpsAI is the target repo, use `/Users/Dev/Apps/finopsai-desktop` as the
  canonical local repo path unless the user explicitly names a different target.
- Read the target repo only as needed.
- If the target repo has an `AGENTS.md`, read it before assessing applicability.
- If the target repo has nested `AGENTS.md` files in relevant areas, apply the closest applicable guidance for those areas.
- If the canonical FinOpsAI path is missing or a different local checkout is the
  only visible candidate, stop and ask the user to confirm the intended repo
  path before continuing Phase B.
- If no target-repo `AGENTS.md` exists, state that explicitly in the assessment.
- Save repo-application reports back to this workspace under `output/<name>_YYYY_MM_DD/<name>_repo_mapping_YYYY_MM_DD.md`.
- Update `notes/output_catalog.md` with the repo-mapping artifact and a high-level mapping note.
- Do not modify the target repo unless the user explicitly asks for implementation changes.

## Assessment Discipline

- Distinguish immediately applicable ideas from ideas requiring process changes, tooling changes, or architecture changes.
- Separate practical engineering practices from hype, speculation, or ideas that depend on unusual team maturity.
- Ground claims in the cleaned transcript, the analysis report, and concrete evidence from the target repo.
- If repo evidence is insufficient, say so rather than guessing.

## Editing Discipline

- Keep changes narrow and task-scoped.
- Prefer existing file naming conventions and folder structure.
- Do not modify generated outputs unless the user asks to regenerate or revise them.
- Do not add hidden dependencies, network calls, automation, or external services to this workspace.
