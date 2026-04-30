---
name: research-markdown-authoring
description: Standardize ResearchToBacklogOps markdown artifacts so lane analysis, applicability mapping, roadmap-fit decisions, and run summaries expose consistent evidence, recommendation, scope, and next-step surfaces for later workflow phases.
---

# Research Markdown Authoring

## Purpose
Use this skill when a `ResearchToBacklogOps` workflow needs to write or revise a
durable markdown artifact such as:
1. a Phase 1 lane-analysis artifact,
2. a Phase 2 applicability or repo-mapping artifact,
3. a roadmap-fit decision artifact,
4. a run summary,
5. or another research markdown file whose content will later be consumed by
   Phase 1 completion, Phase 2 classification, Phase 3 approval, or Phase 4
   ClickUp-card drafting.

This is a shared authoring skill. It does not replace the lane skills. It gives
them a stable markdown contract so later workflow phases do less inference and
more evidence-backed extraction.

## When to use
Apply this skill whenever a lane or later workflow phase writes a markdown
artifact under `output/` in this workspace.

Do not use it for:
- transcript cleanup text outputs such as `_cleaned_YYYY_MM_DD.txt`,
- direct repo implementation work,
- ClickUp publishing,
- or non-durable chat-only responses.

## Core rules
- Preserve lane-specific analysis depth and domain nuance.
- Keep artifact structure consistent enough that later phases can extract:
  summary, decision takeaways, candidate recommendations, exclusions, risks,
  confidence, and next-step guidance without guessing.
- Distinguish source evidence from FinOpsAI evidence.
- Distinguish recommendation candidates from final approvals.
- Do not collapse multiple recommendation candidates into one blended item.
- Make scope boundaries explicit before anything could later become a card.
- If evidence is weak or missing, say so directly instead of smoothing over the
  gap.

## Required artifact surfaces
Every research markdown artifact written for this workflow should expose these
surfaces in clearly labeled sections, even if the exact section names vary by
lane:

1. Source and scope
- What source was reviewed.
- What question or lane the artifact answers.
- What inputs or sibling artifacts were used.

2. Executive summary
- A concise summary suitable for Phase 1 completion or later review.

3. Evidence and caveats
- What evidence supports the claims.
- What could not be verified.
- What caveats constrain interpretation.

4. Candidate ideas or findings
- Separate findings or recommendation candidates instead of merging them into a
  narrative blob.

5. Risks and exclusions
- Record operational, compliance, workflow, architecture, or scope risks.
- Record what should not be translated directly into product or task work.

6. Recommendation surface
- State the current recommendation or disposition for this artifact.
- Make clear whether it supports Phase 2, another workflow, or catalog-only
  closure.

7. Verification notes
- Record artifact-local checks, source validation state, and any important
  workflow boundary checks.

## Recommendation-candidate contract
When an artifact contains one or more actionable candidates, each candidate
should include these fields in substance:
- candidate name,
- problem or opportunity,
- source evidence,
- confidence,
- likely fit type or change type,
- major risks or blockers,
- explicit exclusions / out-of-scope,
- recommended next step,
- and, when the candidate is concrete enough, a concise identifier seed.

This can be rendered as headings, short subsections, or a compact repeated
pattern. Do not force tables when prose is clearer.

## Lane-specific expectations
### Phase 1 lane artifacts
Each lane artifact should make it easy to extract:
- a Phase 1 summary,
- Phase 2 decision takeaways,
- cross-lane or no-go rationale when relevant,
- recommendation candidates or explicit non-candidates,
- and a recommended next action.

### Phase 2 mapping artifacts
Make category separation explicit. For each applicable idea, include:
- source artifact attribution,
- FinOpsAI evidence,
- applicability level,
- change type,
- risks,
- and next artifact recommendation.

### Roadmap-fit artifacts
For each recommendation, make explicit:
- status,
- why that status fits,
- what evidence supports it,
- what risk remains,
- whether card drafting is blocked,
- and what exact next artifact or approval path applies.

### Run summaries
Summaries should preserve the reopening point of the run:
- lanes completed,
- final disposition,
- recommendation outcomes,
- durable artifacts produced,
- ClickUp draft status when applicable,
- and remaining follow-up outside the run.

## Writing discipline
- Prefer concrete headings over ornamental prose.
- Keep section names stable when the workflow already expects them.
- Avoid long narrative sections that hide the actual recommendation surface.
- Do not invent implementation detail just to make a candidate look card-ready.
- If an artifact is source-only and should stop at catalog-only closure, make
  that explicit and topic-specific.

## Handoff objective
The artifact should be strong enough that a later workflow phase can answer:
- what happened,
- what evidence exists,
- what is promising,
- what is excluded,
- why to proceed or stop,
- and what exact next step is justified.
