# FinOpsAI BacklogGovernanceOps — API Intake (Phase 2 — Not yet built)

## Status

This folder is reserved for Phase 2 of the BacklogGovernanceOps handoff architecture. Phase 2 is not yet built. This README documents the intended design so future builders have full context while preserving the current low-friction PO workflow.

## Why this folder exists now

The intake folder, `governance-states/01_intake/`, is designed as a path-agnostic shared state. In Phase 1, the research workflow deposits draft artifacts directly to that folder using the research output pattern `/output/<name>_YYYY_MM_DD/<name>_clickup_card_draft_YYYY_MM_DD_<task-card-identifier>.md`. In Phase 2, draft artifacts will be posted to an API endpoint that deposits to the same folder and returns a structured acknowledgment. Reserving this folder now gives Phase 2 a clean home without retrofitting.

## Intended Phase 2 design

- A defined API endpoint receives draft artifact payloads from the research workflow run-close event.
- The endpoint validates the payload, deposits the artifact to `../governance-states/01_intake/`, writes an acknowledgment receipt to `../governance-records/run-notifications/`, and returns a structured response to the caller.
- Both the human PO path and the agentic path converge at `governance-states/01_intake/`; the endpoint is a delivery mechanism, not a separate workflow state.
- A future MCP agent may call this endpoint to deposit artifacts or may read from `../governance-states/03_approved/` for publication. Both use cases remain governed by the same non-negotiable rules as the human path.

## Key design constraint

The API endpoint must never bypass the `03_approved/` gate. No agent may publish a PBI from `governance-states/01_intake/` or `governance-states/02_review/` directly. PO confirmation is required before any agent commits a publication action, and one approved draft artifact still maps to exactly one published PBI.

## Files in this folder

- `endpoint_spec.md` — API contract to be defined when Phase 2 is built.
