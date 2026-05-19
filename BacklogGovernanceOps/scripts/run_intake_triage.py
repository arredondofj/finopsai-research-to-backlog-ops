#!/usr/bin/env python3
"""Run deterministic intake triage for BacklogGovernanceOps.

Default mode is a dry run that reports what would be surfaced to the Product
Owner. Use --write to append a triage acknowledgment batch for newly surfaced
artifacts.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
INTAKE_DIR = REPO_ROOT / "governance-states" / "01_intake"
REJECTED_DIR = REPO_ROOT / "governance-states" / "01_intake_rejected"
RECEIPTS_DIR = REPO_ROOT / "governance-records" / "run-notifications"
TRIAGE_LOG = REPO_ROOT / "governance-records" / "intake-triage" / "INTAKE_TRIAGE_LOG.md"
CARD_ACTIVITY_DIR = REPO_ROOT / "governance-records" / "card-activity"
REVIEW_DIR = REPO_ROOT / "governance-states" / "02_review"
APPROVED_DIR = REPO_ROOT / "governance-states" / "03_approved"


@dataclass
class ReceiptRecord:
    file_path: Path
    run_id: str | None = None
    deposit_timestamp: str | None = None
    handoff_status: str | None = None
    artifact_filenames: list[str] = field(default_factory=list)


@dataclass
class TriageBatch:
    heading: str
    timestamp: str | None = None
    artifact_paths: list[str] = field(default_factory=list)


@dataclass
class GovernanceDecision:
    heading: str
    artifact_path: str | None = None
    decision: str | None = None
    next_state: str | None = None


@dataclass
class ArtifactResult:
    filename: str
    full_path: Path
    status: str
    run_ids: list[str] = field(default_factory=list)
    receipt_files: list[Path] = field(default_factory=list)
    deposit_dates: list[str] = field(default_factory=list)
    po_decision: str | None = None
    anomalies: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Append a triage acknowledgment batch for newly surfaced artifacts.",
    )
    return parser.parse_args()


def list_intake_artifacts() -> list[Path]:
    artifacts = []
    for path in sorted(INTAKE_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        artifacts.append(path.resolve())
    return artifacts


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_receipts() -> list[ReceiptRecord]:
    records: list[ReceiptRecord] = []
    for path in sorted(RECEIPTS_DIR.glob("*.md")):
        text = read_text(path)
        record = ReceiptRecord(file_path=path.resolve())
        record.run_id = match_field(text, "Run ID")
        record.deposit_timestamp = (
            match_field(text, "Deposit timestamp")
            or match_field(text, "Catchup deposit timestamp")
        )
        record.handoff_status = match_field(text, "Overall handoff status")
        record.artifact_filenames = parse_bullet_section(
            text,
            "List of deposited artifact file names",
        )
        records.append(record)
    return records


def parse_triage_batches() -> list[TriageBatch]:
    if not TRIAGE_LOG.exists():
        return []
    text = read_text(TRIAGE_LOG)
    sections = re.split(r"(?=^## Intake triage batch: )", text, flags=re.MULTILINE)
    batches: list[TriageBatch] = []
    for section in sections:
        if not section.startswith("## Intake triage batch: "):
            continue
        heading = section.splitlines()[0].strip()
        batch = TriageBatch(heading=heading)
        batch.timestamp = match_field(section, "Triage run timestamp")
        artifact_paths = parse_bullet_section(section, "Artifacts surfaced to PO")
        if not artifact_paths:
            artifact_paths = parse_bullet_section(section, "Artifact paths surfaced to PO")
        batch.artifact_paths = artifact_paths
        batches.append(batch)
    return batches


def parse_governance_decisions() -> list[GovernanceDecision]:
    if not CARD_ACTIVITY_DIR.exists():
        return []
    decisions: list[GovernanceDecision] = []
    for path in sorted(CARD_ACTIVITY_DIR.glob("*__activity.md")):
        text = read_text(path)
        artifact_path = match_field(text, "Source draft artifact")
        sections = re.split(r"(?=^### )", text, flags=re.MULTILINE)
        for section in sections:
            decision_value = match_field(section, "Decision")
            if not decision_value:
                continue
            decision = GovernanceDecision(
                heading=section.splitlines()[0].strip(),
                artifact_path=artifact_path,
                decision=decision_value,
                next_state=match_field(section, "State after event"),
            )
            decisions.append(decision)
    return decisions


def match_field(text: str, label: str) -> str | None:
    pattern = rf"^- \*\*{re.escape(label)}:\*\* (.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    return strip_backticks(value)


def parse_bullet_section(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    target = f"- **{heading}:**"
    results: list[str] = []
    capture = False
    for line in lines:
        if line.startswith(target):
            capture = True
            continue
        if capture:
            if line.startswith("- **"):
                break
            match = re.match(r"^\s*-\s+(.+?)\s*$", line)
            if match:
                value = strip_backticks(match.group(1).strip())
                if value and value.lower() != "none":
                    results.append(value)
            elif line.strip() and not line.startswith("  "):
                break
    return results


def strip_backticks(value: str) -> str:
    if value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def basename_key(value: str | Path | None) -> str | None:
    if value is None:
        return None
    return Path(str(value)).name


def build_receipt_index(records: Iterable[ReceiptRecord]) -> dict[str, list[ReceiptRecord]]:
    index: dict[str, list[ReceiptRecord]] = {}
    for record in records:
        for filename in record.artifact_filenames:
            index.setdefault(filename, []).append(record)
    return index


def build_triage_index(batches: Iterable[TriageBatch]) -> dict[str, list[TriageBatch]]:
    index: dict[str, list[TriageBatch]] = {}
    for batch in batches:
        for artifact_path in batch.artifact_paths:
            key = basename_key(artifact_path)
            if key:
                index.setdefault(key, []).append(batch)
    return index


def build_governance_index(
    decisions: Iterable[GovernanceDecision],
) -> dict[str, list[GovernanceDecision]]:
    index: dict[str, list[GovernanceDecision]] = {}
    for decision in decisions:
        key = basename_key(decision.artifact_path)
        if key:
            index.setdefault(key, []).append(decision)
    return index


def state_presence(filename: str) -> tuple[bool, bool, bool]:
    return (
        (REJECTED_DIR / filename).exists(),
        (REVIEW_DIR / filename).exists(),
        (APPROVED_DIR / filename).exists(),
    )


def classify_artifacts(
    artifacts: list[Path],
    receipt_index: dict[str, list[ReceiptRecord]],
    triage_index: dict[str, list[TriageBatch]],
    governance_index: dict[str, list[GovernanceDecision]],
) -> tuple[list[ArtifactResult], list[ArtifactResult]]:
    results: list[ArtifactResult] = []
    new_items: list[ArtifactResult] = []

    for artifact in artifacts:
        filename = artifact.name
        receipts = receipt_index.get(filename, [])
        triage_batches = triage_index.get(filename, [])
        decisions = governance_index.get(filename, [])
        in_rejected, in_review, in_approved = state_presence(filename)

        anomalies: list[str] = []
        status = "New to PO review"
        decision_value = None

        if not receipts:
            status = "Anomalous"
            anomalies.append("missing matching receipt")
        elif len(receipts) > 1:
            status = "Anomalous"
            anomalies.append("multiple matching receipts")

        if len(triage_batches) > 1:
            anomalies.append("multiple prior triage acknowledgments")
        if len(decisions) > 1:
            anomalies.append("multiple governance decisions")

        if decisions:
            decision_value = decisions[-1].decision
            if decision_value == "Hold":
                status = "Held in intake"
            elif decision_value == "Admit to review":
                status = "Admitted to review"
            elif decision_value == "Reject":
                status = "Rejected"

        if in_rejected:
            anomalies.append("artifact still present in intake and rejected")
            status = "Rejected"

        if in_review:
            if status in {"New to PO review", "Awaiting intake decision", "Held in intake"}:
                anomalies.append("artifact still present in intake and review")
            if not decisions:
                anomalies.append("artifact exists in review without intake decision")
            status = "Admitted to review"

        if in_approved:
            if status in {"New to PO review", "Awaiting intake decision", "Held in intake"}:
                anomalies.append("artifact still present in intake and approved")
            status = "Approved for publication"

        if status == "New to PO review" and triage_batches:
            status = "Awaiting intake decision"

        if decisions and status in {"Held in intake", "Admitted to review", "Rejected"}:
            if status not in {"Held in intake", "Rejected"}:
                anomalies.append("artifact remains in intake after PO decision")

        if anomalies and status != "Anomalous":
            if status == "New to PO review":
                status = "New to PO review"

        result = ArtifactResult(
            filename=filename,
            full_path=artifact,
            status=status,
            run_ids=sorted({record.run_id for record in receipts if record.run_id}),
            receipt_files=sorted({record.file_path for record in receipts}),
            deposit_dates=sorted(
                {
                    record.deposit_timestamp for record in receipts if record.deposit_timestamp
                }
            ),
            po_decision=decision_value,
            anomalies=anomalies,
        )
        results.append(result)
        if result.status == "New to PO review":
            new_items.append(result)

    return results, new_items


def make_triage_batch(new_items: list[ArtifactResult]) -> str:
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    receipt_paths = sorted(
        {str(receipt) for item in new_items for receipt in item.receipt_files}
    )
    run_ids = sorted({run_id for item in new_items for run_id in item.run_ids})
    artifact_paths = [str(item.full_path) for item in new_items]

    lines = [
        f"## Intake triage batch: {timestamp}",
        "",
        f"- **Triage run timestamp:** {timestamp}",
        "- **Triaged by:** Codex",
        f"- **Receipt file count:** {len(receipt_paths)}",
        "- **Receipt files:**",
    ]
    lines.extend([f"  - `{path}`" for path in receipt_paths])
    lines.append(f"- **Research run ID count:** {len(run_ids)}")
    lines.append("- **Research run IDs:**")
    lines.extend([f"  - `{run_id}`" for run_id in run_ids])
    lines.append(f"- **Artifact count surfaced:** {len(artifact_paths)}")
    lines.append("- **Artifact paths surfaced to PO:**")
    lines.extend([f"  - `{path}`" for path in artifact_paths])
    lines.append("- **Outcome:** surfaced_to_po")
    lines.append("- **Notes:** Deterministic Step 1 and Step 2 intake triage pass.")
    lines.append("")
    return "\n".join(lines)


def append_triage_batch(batch_text: str) -> None:
    existing = read_text(TRIAGE_LOG) if TRIAGE_LOG.exists() else ""
    separator = "\n" if existing.endswith("\n") else "\n\n"
    TRIAGE_LOG.write_text(existing + separator + batch_text, encoding="utf-8")


def render_next_step(
    counts: dict[str, int],
    new_items: list[ArtifactResult],
    anomalies: list[ArtifactResult],
    batch_text: str | None,
) -> list[str]:
    if anomalies:
        return [
            "## Next Step",
            "",
            "### PO Action Required",
            "- Resolve the anomalies before treating the intake state as clean governance input.",
            "",
            "### Records To Update",
            "- Correct the inconsistent receipt, triage, card-activity, or folder-state records identified in the anomaly section.",
            "",
            "### Re-Run",
            "- Re-run `python3 scripts/run_intake_triage.py` after the corrections are complete.",
        ]

    if new_items and batch_text is None:
        return [
            "## Next Step",
            "",
            "### PO Action Required",
            "- Review the `PO review queue summary` and confirm the newly surfaced artifacts should be acknowledged for PO review.",
            "",
            "### Records To Update",
            "- If the dry-run result is correct, run `python3 scripts/run_intake_triage.py --write` to record the intake-triage batch acknowledgment in `governance-records/intake-triage/INTAKE_TRIAGE_LOG.md`.",
            "",
            "### Re-Run",
            "- After writing the acknowledgment, re-run `python3 scripts/run_intake_triage.py` and then proceed with explicit PO intake decisions.",
        ]

    if new_items and batch_text is not None:
        return [
            "## Next Step",
            "",
            "### PO Action Required",
            "- The intake-triage acknowledgment is now recorded. Review each surfaced artifact and make one explicit intake decision per item: `Hold`, `Admit to review`, or `Reject`.",
            "",
            "### Records To Update",
            "- Record each decision in the matching `governance-records/card-activity/<draft-artifact-stem>__activity.md` file.",
            "",
            "### State Move To Perform",
            "- Move each admitted artifact into `governance-states/02_review/` after its decision is recorded.",
            "- Move each rejected artifact into `governance-states/01_intake_rejected/` after its decision is recorded.",
        ]

    awaiting_count = counts.get("Awaiting intake decision", 0)
    if awaiting_count:
        return [
            "## Next Step",
            "",
            "### PO Action Required",
            "- Work the intake queue now.",
            f"- Review the {awaiting_count} artifact(s) currently in `Awaiting intake decision` status and decide `Hold`, `Admit to review`, or `Reject` for each one.",
            "",
            "### Records To Update",
            "- Record each intake decision in the matching `governance-records/card-activity/<draft-artifact-stem>__activity.md` file.",
            "",
            "### State Move To Perform",
            "- Move each admitted artifact into `governance-states/02_review/` after its decision is recorded.",
            "- Move each rejected artifact into `governance-states/01_intake_rejected/` after its decision is recorded.",
        ]

    return [
        "## Next Step",
        "",
        "### PO Action Required",
        "- No immediate intake-triage action is required.",
        "",
        "### Continue From",
        "- If governance work continues, proceed from the current recorded state in `02_review`, `03_approved`, and the matching `card-activity/` file.",
    ]


def render_report(results: list[ArtifactResult], new_items: list[ArtifactResult], batch_text: str | None) -> str:
    counts: dict[str, int] = {}
    anomalies = []
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
        if result.anomalies:
            anomalies.append(result)

    lines = [
        "# Backlog Governance Intake Triage Report",
        "",
        "## Intake summary",
        f"- Total intake draft count: {len(results)}",
        f"- New to PO review: {counts.get('New to PO review', 0)}",
        f"- Awaiting intake decision: {counts.get('Awaiting intake decision', 0)}",
        f"- Held in intake: {counts.get('Held in intake', 0)}",
        f"- Admitted to review: {counts.get('Admitted to review', 0)}",
        f"- Approved for publication: {counts.get('Approved for publication', 0)}",
        f"- Rejected: {counts.get('Rejected', 0)}",
        f"- Anomalous: {counts.get('Anomalous', 0)}",
        "",
        "## Intake artifact status table",
        "",
        "| Artifact filename | Run ID(s) | Receipt file(s) | Deposit date(s) | Status |",
        "|---|---|---|---|---|",
    ]

    for result in results:
        run_ids = "<br>".join(result.run_ids) if result.run_ids else "None"
        receipt_files = "<br>".join(path.name for path in result.receipt_files) if result.receipt_files else "None"
        deposit_dates = "<br>".join(result.deposit_dates) if result.deposit_dates else "None"
        lines.append(
            f"| {escape_table(result.filename)} | {escape_table(run_ids)} | "
            f"{escape_table(receipt_files)} | {escape_table(deposit_dates)} | {escape_table(result.status)} |"
        )

    lines.extend(["", "## PO review queue summary"])
    if not new_items:
        lines.append("- No new intake artifacts were identified.")
    else:
        for item in new_items:
            lines.append(f"- {item.filename}")

    lines.extend(["", "## Triage acknowledgment"])
    if batch_text is None:
        lines.append("- Dry run only. No triage acknowledgment was written.")
    else:
        lines.append("```md")
        lines.append(batch_text.rstrip())
        lines.append("```")

    lines.extend(["", "## Anomalies"])
    if not anomalies:
        lines.append("- None")
    else:
        for result in anomalies:
            lines.append(f"- {result.filename}: {', '.join(result.anomalies)}")

    lines.extend([""])
    lines.extend(render_next_step(counts, new_items, anomalies, batch_text))

    return "\n".join(lines) + "\n"


def escape_table(value: str) -> str:
    return value.replace("|", "\\|")


def validate_paths() -> list[str]:
    missing = []
    for path in [INTAKE_DIR, RECEIPTS_DIR, CARD_ACTIVITY_DIR]:
        if not path.exists():
            missing.append(str(path))
    return missing


def main() -> int:
    args = parse_args()
    missing_paths = validate_paths()
    if missing_paths:
        for path in missing_paths:
            print(f"Missing required path: {path}", file=sys.stderr)
        return 1

    artifacts = list_intake_artifacts()
    receipt_index = build_receipt_index(parse_receipts())
    triage_index = build_triage_index(parse_triage_batches())
    governance_index = build_governance_index(parse_governance_decisions())

    results, new_items = classify_artifacts(
        artifacts,
        receipt_index,
        triage_index,
        governance_index,
    )

    batch_text = None
    if args.write and new_items:
        batch_text = make_triage_batch(new_items)
        append_triage_batch(batch_text)

    report = render_report(results, new_items, batch_text)
    sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
