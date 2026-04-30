# FinOpsAI BacklogGovernanceOps — Governance Configuration

## Purpose

This file defines the configurable parameters that govern escalation thresholds, sprint cycle definitions, and inbox ceilings. Changing a parameter here affects workflow behavior without requiring edits to process authority documents.

## Parameters

```txt
## Escalation configuration

# Age-based escalation threshold
# Any draft artifact remaining unreviewed in governance-states/01_intake/ beyond this threshold
# triggers a Scrum Master notification.
# Unit: sprint cycles (1 sprint cycle = [define sprint length in days])
INTAKE_AGE_THRESHOLD_SPRINTS = 1

# Sprint length in business days (used to calculate age threshold)
SPRINT_LENGTH_BUSINESS_DAYS = 10

# Count-based escalation ceiling
# If total unreviewed items in governance-states/01_intake/ exceeds this count,
# Scrum Master is notified independently of age.
INTAKE_COUNT_CEILING = 10

## Notification configuration

# Product Owner contact / notification target
PO_NOTIFICATION_TARGET = [define — email, ClickUp user, Slack handle, etc.]

# Scrum Master contact / escalation target
SM_ESCALATION_TARGET = [define — email, ClickUp user, Slack handle, etc.]

## Handoff phase configuration

# Current active handoff phase
# Phase 1: folder-based intake with auto-acknowledgment
# Phase 2: API endpoint intake (future)
ACTIVE_HANDOFF_PHASE = 1

## Sprint candidacy

# Default sprint candidacy flag for newly published PBIs
# Options: backlog-only | sprint-candidate | undecided
DEFAULT_SPRINT_CANDIDACY = undecided
```

## Change log

| Date | Parameter changed | Changed by | Reason |
|---|---|---|---|
| YYYY-MM-DD | [parameter name] | [name or identifier] | [reason] |
