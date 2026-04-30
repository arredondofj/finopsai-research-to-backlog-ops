# FinOpsAI Backlog Governance Log

This file is the single canonical record of all publication and significant stewardship activity in the BacklogGovernanceOps workspace. It is the authoritative place to verify publication status, trace a live ClickUp PBI back to its source research draft, and review stewardship decisions.

## How to use

- Add intake decision entries when the PO explicitly holds, admits, or rejects an intake artifact.
- Add one entry per published PBI immediately after publication.
- Add stewardship update entries for significant decisions such as scope changes, dependency discoveries, acceptance criteria changes, and deferral decisions.
- Do not record routine review or minor edits; record decisions that affect the PBI's identity, scope, or status.
- When the log grows large, archive older entries to `log-archive/` and note the archive date.

## Entry format — intake decision record

```md
## INTAKE: [Draft artifact identifier]

- **Source draft artifact:** [full file path]
- **Research run ID:** [run identifier from ../run-notifications/]
- **Decision date:** YYYY-MM-DD
- **Decided by:** [PO name or identifier]
- **Decision:** Hold | Admit to review | Reject
- **Decision rationale:** [brief reason]
- **Next state:** `governance-states/01_intake/` | `governance-states/02_review/` | closed
```

## Entry format — publication record

```md
## PBI: [ClickUp PBI Title]

- **ClickUp URL/ID:** [URL or ID]
- **Destination list/status:** [ClickUp list name and initial status]
- **Source draft artifact:** [full file path to source .md file]
- **Research run ID:** [run identifier from ../run-notifications/]
- **Publication date:** YYYY-MM-DD
- **Published by:** [PO name or identifier]
- **Sprint candidate:** Yes / No / Undecided
- **Refinement notes:** [any pre-publication refinement decisions]
- **Decision rationale:** [why this was published now vs. deferred]

### Stewardship updates
<!-- Add dated entries below as stewardship activity occurs -->
- YYYY-MM-DD: [update note]
```

## Entry format — rejection record

```md
## REJECTED: [Draft artifact identifier]

- **Source draft artifact:** [full file path]
- **Rejection date:** YYYY-MM-DD
- **Rejected by:** [PO name or identifier]
- **Reason:** [brief reason — duplicate, out of scope, deferred indefinitely, etc.]
```
