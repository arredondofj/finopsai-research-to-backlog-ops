# FinOpsAI Agent Guidance

## Scope

Place this file at the FinOpsAI repository root as `AGENTS.md`.

This guidance applies to the entire FinOpsAI repo unless a more specific nested `AGENTS.md` exists in a subdirectory. For nested files, the closest applicable `AGENTS.md` takes precedence for files in that subtree.

## Domain Invariants

- Preserve deterministic accounting, allocation, reconciliation, billing, reporting, and bookkeeping logic.
- Treat financial correctness, auditability, reproducibility, and traceability as higher priority than speed, novelty, or broad automation.
- Do not weaken validation, approval, reconciliation, authorization, audit, or review gates.
- Treat rounding, currency handling, date boundaries, period close behavior, duplicate inputs, missing data, idempotency, and reconciliation behavior as high-risk areas.
- Do not change financial outputs without focused tests or a clear explanation of the expected output change.

## Dependency And Integration Rules

- Do not add hidden external dependencies, background jobs, network calls, model calls, or third-party services without explicit approval.
- Prefer existing repo patterns, data models, service boundaries, and libraries before introducing new abstractions.
- Do not introduce non-deterministic behavior into accounting or financial decision paths unless explicitly approved and isolated from bookkeeping correctness.
- Do not move sensitive data to external services unless the user explicitly approves the data flow and security model.

## Review Gates

- Do not bypass or weaken tests, linting, type checks, approval checks, security checks, or existing CI expectations.
- If a check cannot be run, state that clearly and explain the residual risk.
- Keep patches narrow and task-scoped.
- Do not refactor unrelated code.
- Do not modify migrations, schemas, generated files, or lockfiles unless required by the task.

## Verification Discipline

- Use staged verification:
  1. run focused tests for touched code,
  2. run broader tests for shared or financial logic,
  3. run linting and type checks when relevant.
- For financial logic changes, include edge cases for rounding, currency precision, period boundaries, duplicate inputs, missing data, idempotency, and reconciliation behavior.
- Prefer deterministic assertions over snapshot-only or visual-only checks for financial behavior.

## AI / Transcript Application Assessments

When assessing transcript ideas against this repo:

- Read the transcript analysis first, then inspect the repo only as needed.
- Do not implement code changes unless explicitly asked.
- Be skeptical of applying practices from AI demos, large labs, or unusually mature teams without checking fit against this repo.
- Distinguish clearly between:
  - immediately applicable ideas,
  - ideas requiring moderate process or tooling changes,
  - ideas requiring deeper architecture changes,
  - ideas that are speculative, hype-prone, immature, or poor fits.
- Evaluate ideas against:
  - financial correctness,
  - determinism,
  - data privacy,
  - security,
  - auditability,
  - maintainability,
  - test coverage,
  - operational complexity,
  - review burden.
- Reference concrete files, modules, workflows, or tests when making repo-specific claims.
- If repo evidence is insufficient, say so rather than guessing.

## Change Discipline

- Explain any proposed change that affects financial outputs, permissions, audit trails, data retention, or external integrations.
- Prefer reversible, incremental improvements over sweeping architecture changes.
- Protect bookkeeping correctness over speed.
