# Task Card Example

## Title

`refactor: validate transaction source definitions before use`

## Requirement / Problem Statement

FinOpsAI already relies on behavior-bearing transaction source definitions in `/Users/Sites/Repo-FinOpsAI/src/resources/transaction_source_rules.json`, but the current controller startup flow in `/Users/Sites/Repo-FinOpsAI/src/controller/app.py` only verifies file existence and JSON parseability. It does not validate whether a source definition is semantically compatible with the current ingestion implementation.

This creates a concrete maintainability and correctness gap that the repo’s own ingestion specs already call out. `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/ingestion_source_extensibility_spec.md` explicitly says source-definition integrity is not strongly validated and names `validate_csv_source_definition(...)` as desired work. `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/csv_transaction_ingestion_matrix.md` documents a real mismatch today: `Wells Fargo` declares `row_format: "headerless"` while `/Users/Sites/Repo-FinOpsAI/src/services/ingestion.py` still requires a detected header row.

The work item is to add deterministic validation for transaction source definitions before they are used, so invalid or incompatible configuration fails fast with explicit errors instead of silently drifting into runtime ingestion behavior.

## Expected Outcome

FinOpsAI has one explicit, repo-local validation pass for transaction source definitions that runs before ingestion depends on those definitions.

The resulting work should:

- validate source-definition structure and required sections
- reject known invalid or currently unsupported combinations deterministically
- make config/implementation mismatches visible before runtime ingestion work proceeds
- add focused regression coverage for invalid definitions
- remain scoped to validation-only refactor work without turning into a broader ingestion redesign

## Business Context

FinOpsAI is production-oriented bookkeeping software. Even though this task does not change accounting semantics directly, transaction source definitions influence ingestion behavior and therefore affect the reliability of the staged transaction pipeline. Weak validation on behavior-bearing config increases the risk of brittle onboarding, confusing runtime failures, and silent divergence between documented source capabilities and implemented ingestion support.

## Scope

### Included

- define and implement deterministic validation for transaction source definitions before use
- validate required top-level structure for currently supported source-definition shape
- validate known compatibility constraints between declared source metadata and current ingestion behavior
- fail fast with explicit, actionable errors when definitions are invalid or unsupported
- add focused tests covering invalid definitions and at least one known incompatibility case
- update the relevant repo docs/spec references if implemented validation behavior changes documented expectations

### Excluded

- implementing generic headerless CSV parsing
- parser-strategy refactor or canonical-mapping redesign
- transaction-source CRUD UI/controller/persistence work
- changing transaction semantics, posting behavior, classification logic, or accounting-state decisions
- adding new dependencies, external services, model-serving, MCP, RAG, or runtime AI behavior
- broad ingestion architecture redesign beyond this one validation-focused refactor

## Acceptance Criteria

1. One governing specification path is selected for the source-definition validation work item.
2. The governing specification documents:
   - the current validation gap
   - the currently supported source-definition contract for this task
   - the exact invalid or unsupported combinations that must fail fast
   - explicit exclusions preventing scope creep into headerless parsing, parser strategies, or CRUD
3. FinOpsAI adds deterministic validation for transaction source definitions before those definitions are relied on by ingestion workflows.
4. Invalid or incompatible source definitions fail with clear, actionable error behavior rather than silent acceptance.
5. The current mismatch where a source declares unsupported behavior, such as `row_format: "headerless"` under the current ingestor constraints, is covered by validation behavior and regression tests.
6. Focused tests are added or updated to cover invalid definitions and supported-definition pass cases relevant to this task.
7. The work preserves deterministic accounting, validation, approval, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
8. The task remains one primary `refactor` item and does not expand into a broader ingestion implementation program.

## Constraints

- Preserve deterministic accounting and staged-pipeline expectations from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep the work dependency-light; prefer handwritten or minimal standard-library validation unless the governing specification explicitly justifies something else.
- Do not broaden this task into headerless parsing, parser dispatch, source CRUD, or product-facing behavior change.
- Keep the execution prompt on the card and not in the repo.
- Keep the card scoped to one primary task.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_2026_04_25/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_2026_04_25/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_2026_04_25/You’ve Been Underusing Dataclasses (These Tricks Are Wild) [Y9_h7ehjhO4]_roadmap_fit_2026_04_25.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/src/controller/app.py`
  - `/Users/Sites/Repo-FinOpsAI/src/services/ingestion.py`
  - `/Users/Sites/Repo-FinOpsAI/src/resources/transaction_source_rules.json`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_ingestion.py`
  - `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/ingestion_source_extensibility_spec.md`
  - `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/csv_transaction_ingestion_matrix.md`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/source_definition_validation_spec.md`
   - Define:
     - current transaction-source definition loading behavior
     - current validation gaps and known incompatibility examples
     - the supported validation contract for this task
     - exact fail-fast conditions and error expectations
     - focused test surfaces to align
     - explicit exclusions preventing headerless parsing, parser strategy, and CRUD expansion

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update validation behavior and focused tests exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/ingestion/source_definition_validation_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
