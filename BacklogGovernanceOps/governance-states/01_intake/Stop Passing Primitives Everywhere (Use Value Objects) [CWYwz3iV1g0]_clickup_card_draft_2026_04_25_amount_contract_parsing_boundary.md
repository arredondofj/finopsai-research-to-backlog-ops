# Task Card Example

## Title

`refactor: define one internal amount contract boundary`

## Requirement / Problem Statement

FinOpsAI currently relies on repeated amount parsing and coercion across multiple layers instead of one deterministic internal contract for transaction and journal-line amounts.

`/Users/Sites/Repo-FinOpsAI/src/services/normalizer.py` computes a numeric amount from debit and credit fields but then stores it into normalized records as a formatted string such as `"$1,234.56"`. `/Users/Sites/Repo-FinOpsAI/src/controller/app.py` reparses transaction-level amounts with its own `_parse_amount_value(...)` helper and separately coerces journal-line amounts again during validation. `/Users/Sites/Repo-FinOpsAI/src/services/wave_service.py` duplicates amount parsing with slightly different semantics and also directly coerces journal-line amounts during payload construction. `/Users/Sites/Repo-FinOpsAI/src/persistence/models.py` still types `Transaction.amount` as `float`, which does not line up cleanly with the normalizer’s formatted-string output.

This creates a concrete maintainability and safety seam in a production-oriented bookkeeping repository whose root guidance requires deterministic, explainable, and testable accounting behavior. The work item is to define and enforce one explicit internal amount contract boundary so accepted amount shapes are handled consistently and malformed or ambiguous values fail more clearly, without broadening into a larger accounting-model redesign.

## Expected Outcome

FinOpsAI has one explicit, repo-local contract for internal transaction and journal-line amount handling across normalization, validation, and Wave-posting preparation.

The resulting work should:

- define one authoritative internal amount parsing and validation boundary
- reduce duplicated parsing and coercion behavior across the current code paths
- preserve current accepted behavior unless the governing specification explicitly narrows malformed-input handling
- make malformed or incompatible amount values fail with clearer deterministic behavior
- add focused regression coverage for the preserved accepted cases and the clarified failure cases
- remain scoped to contract-boundary refactor work without turning into a broader money-type or accounting-architecture redesign

## Business Context

FinOpsAI is production-oriented bookkeeping software. Even though this task is a refactor rather than a product feature, amount interpretation directly affects validation, journal balancing, and posting behavior. Weak or duplicated amount handling increases the risk of silent drift between normalization, controller checks, persistence assumptions, and Wave payload construction.

## Scope

### Included

- define the currently supported internal amount contract for transaction-level and journal-line handling
- implement one authoritative parsing and validation boundary for that contract
- align the affected normalization, controller-validation, and Wave-posting preparation code paths to that boundary
- clarify and preserve the intended invariants for valid numeric shape and positive journal-line amounts where required
- add focused regression tests for preserved supported inputs and deterministic malformed-input failures
- update the relevant repo docs/spec references if the clarified contract changes documented expectations

### Excluded

- broad value-object rollout across unrelated repo surfaces
- `Decimal` migration or a broader money-type redesign
- UI redesign or user-facing accounting workflow changes
- ingestion architecture redesign unrelated to the amount contract boundary
- changes to transaction semantics, approval rules, posting policy, or classification behavior beyond the amount-contract seam itself
- new dependencies, external services, model-serving, MCP, RAG, or runtime AI behavior

## Acceptance Criteria

1. One governing specification path is selected for the internal amount-contract work item.
2. The governing specification documents:
   - the current split amount-handling behavior across normalization, controller validation, persistence assumptions, and Wave posting
   - the intended internal amount contract for this task
   - which accepted behaviors must remain stable
   - which malformed or ambiguous inputs must fail deterministically
   - explicit exclusions preventing scope creep into a broader money-type migration or accounting redesign
3. FinOpsAI adds one authoritative internal amount parsing and validation boundary used by the relevant transaction-level and journal-line flows in scope.
4. The affected code paths no longer rely on duplicated ad hoc parsing rules with materially inconsistent behavior for the same internal amount concepts.
5. Journal-line positivity and related amount invariants remain explicit and deterministic where current posting and validation behavior requires them.
6. Focused tests are added or updated to cover preserved supported inputs and clarified malformed-input failures relevant to this task.
7. The work preserves deterministic accounting, validation, approval, privacy, dependency, and testing constraints from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
8. The task remains one primary `refactor` item and does not expand into a full internal money-type migration, broad wrapper conversion, or accounting-domain redesign.

## Constraints

- Preserve deterministic accounting and staged-pipeline expectations from `/Users/Sites/Repo-FinOpsAI/AGENTS.md`.
- Keep the first pass narrowly scoped to contract-boundary cleanup rather than a larger domain-model rewrite.
- Do not broaden this task into `Decimal` migration, UI work, classification redesign, or posting-policy changes.
- Keep the execution prompt on the card and not in the repo.
- Keep the card scoped to one primary task.

## Dependencies / References

- Research workspace artifacts:
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_2026_04_25/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_analysis_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_2026_04_25/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_repo_mapping_2026_04_25.md`
  - `/Users/Admin/Documents/CodeX/ResearchToBacklogOps/output/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_2026_04_25/Stop Passing Primitives Everywhere (Use Value Objects) [CWYwz3iV1g0]_roadmap_fit_2026_04_25.md`
- FinOpsAI repo guidance and evidence:
  - `/Users/Sites/Repo-FinOpsAI/AGENTS.md`
  - `/Users/Sites/Repo-FinOpsAI/src/services/normalizer.py`
  - `/Users/Sites/Repo-FinOpsAI/src/controller/app.py`
  - `/Users/Sites/Repo-FinOpsAI/src/services/wave_service.py`
  - `/Users/Sites/Repo-FinOpsAI/src/persistence/models.py`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_controller_validation.py`
  - `/Users/Sites/Repo-FinOpsAI/tests/test_wave_service.py`
  - `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/transaction_semantics_spec.md`

## Subtasks

1. Generate Specification
   - Create the governing specification at:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/transaction_amount_contract_spec.md`
   - Define:
     - the current amount-handling split across normalization, validation, persistence, and posting
     - the supported internal amount contract for this task
     - preserved accepted behavior versus deterministic malformed-input failures
     - exact invariants for transaction-level and journal-line amounts in scope
     - focused test surfaces to align
     - explicit exclusions preventing `Decimal` migration, broad wrapper conversion, and accounting redesign

2. Generate Execution Prompt
   - Blocked until Subtask 1 specification is approved.
   - Create the execution prompt on the task card only.
   - The execution prompt must instruct the implementation chat to update the scoped amount-handling code and focused tests exactly against:
     `/Users/Sites/Repo-FinOpsAI/docs/product_specifications/transaction_amount_contract_spec.md`
   - Do not store the execution prompt in the repo.

## Notes / Operational Rule

- Subtask 2 is blocked until Subtask 1 is approved.
- This card represents one primary work item only.
- The card is the control record.
- The repo stores the specification only.
- Human publishes or creates the ClickUp card.
