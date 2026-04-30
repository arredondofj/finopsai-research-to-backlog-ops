# Duplicate Log

## Purpose

This folder holds the canonical duplicate-event record for the Backlog Governance Workflow. It exists so duplicate handoff attempts can be tracked as governed exceptions without polluting the active intake flow or being mixed into generic error handling.

## Operating rule

- Use `DUPLICATE_LOG.md` to record duplicate handoff events only.
- Do not use this folder for Product Owner review decisions or publication records.
- Do not treat duplicate events as system failures unless a technical error also occurred.
