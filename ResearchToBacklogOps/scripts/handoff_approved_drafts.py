#!/usr/bin/env python3
"""Deposit approved research draft artifacts into BacklogGovernanceOps intake."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GOVERNANCE_ROOT = REPO_ROOT.parent / "BacklogGovernanceOps"


@dataclass
class DraftArtifact:
    path: Path
    identifier: str
    source_key: str
    draft_date: str

    @property
    def run_id(self) -> str:
        return f"{self.source_key}_{self.draft_date}"

    @property
    def identity_key(self) -> str:
        return f"{self.run_id}::{self.identifier}"


@dataclass
class HandoffResult:
    deposited: list[tuple[DraftArtifact, Path]]
    duplicates: list[tuple[DraftArtifact, Path, Path]]
    receipt_path: Path
    status: str
    deposit_timestamp: str
    approval_timestamp: str
    close_timestamp: str
    already_handed_off: bool = False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Absolute or relative research run directory.")
    parser.add_argument(
        "--governance-root",
        default=str(DEFAULT_GOVERNANCE_ROOT),
        help="BacklogGovernanceOps workspace root.",
    )
    parser.add_argument(
        "--approval-timestamp",
        help="Run-summary approval timestamp to record in the receipt. Defaults to now.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Persist the deposit, duplicate routing, and receipt. Default is dry-run.",
    )
    return parser.parse_args()


def now_stamp() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def parse_draft_artifact(path: Path) -> DraftArtifact:
    pattern = re.compile(
        r"^(?P<prefix>.+?)_clickup_card_draft_(?P<date>\d{4}_\d{2}_\d{2})_(?P<identifier>.+)\.md$"
    )
    match = pattern.match(path.name)
    if not match:
        raise ValueError(f"Unsupported draft filename format: {path.name}")

    prefix = match.group("prefix")
    source_key_match = re.search(r"\[(?P<source>[^\]]+)\]$", prefix)
    source_key = source_key_match.group("source") if source_key_match else prefix

    return DraftArtifact(
        path=path.resolve(),
        identifier=match.group("identifier"),
        source_key=source_key,
        draft_date=match.group("date"),
    )


def collect_drafts(run_dir: Path) -> list[DraftArtifact]:
    drafts = []
    for path in sorted(run_dir.glob("*_clickup_card_draft_*.md")):
        drafts.append(parse_draft_artifact(path))
    return drafts


def format_bullets(items: list[str]) -> str:
    if not items:
        return "None"
    return "\n".join(f"  - `{item}`" for item in items)


def receipt_filename(source_key: str, date_str: str) -> str:
    return f"run_notification_{source_key}_{date_str}.md"


def unique_duplicate_path(duplicate_dir: Path, filename: str) -> Path:
    candidate = duplicate_dir / filename
    if not candidate.exists():
        return candidate

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    timestamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S")
    return duplicate_dir / f"{stem}__duplicate_{timestamp}{suffix}"


def existing_artifact_match(governance_root: Path, identity_key: str) -> Path | None:
    state_dirs = [
        governance_root / "governance-states" / "01_intake",
        governance_root / "governance-states" / "01_intake_duplicates",
        governance_root / "governance-states" / "02_review",
        governance_root / "governance-states" / "03_approved",
    ]
    for state_dir in state_dirs:
        for path in sorted(state_dir.glob("*_clickup_card_draft_*.md")):
            try:
                artifact = parse_draft_artifact(path)
            except ValueError:
                continue
            if artifact.identity_key == identity_key:
                return path.resolve()
    return None


def build_receipt_text(
    *,
    run_id: str,
    run_summary_path: Path,
    close_timestamp: str,
    approval_timestamp: str,
    deposit_timestamp: str,
    deposited_paths: list[Path],
    duplicate_paths: list[Path],
    source_paths: list[Path],
    status: str,
) -> str:
    deposited_names = [path.name for path in deposited_paths]
    duplicate_names = [path.name for path in duplicate_paths]
    source_names = [str(path) for path in source_paths]
    return "\n".join(
        [
            "# Run Notification Receipt",
            "",
            f"- **Run ID:** `{run_id}`",
            "- **Receipt type:** Standard research handoff",
            f"- **Research run close timestamp:** `{close_timestamp}`",
            f"- **Run summary approval timestamp:** `{approval_timestamp}`",
            f"- **Run summary approval evidence:** `{run_summary_path}`",
            f"- **Deposit timestamp:** `{deposit_timestamp}`",
            f"- **Number of draft artifacts deposited:** `{len(deposited_paths)}`",
            "- **List of deposited artifact file names:**",
            format_bullets(deposited_names),
            "- **List of duplicate-routed artifact file names, if any:**",
            format_bullets(duplicate_names),
            "- **Source path(s):**",
            format_bullets(source_names),
            "- **Deposit destination:** `governance-states/01_intake/`",
            f"- **PO notification timestamp:** `{deposit_timestamp}`",
            "- **Auto-acknowledgment status:** confirmed",
            f"- **Overall handoff status:** {status}",
            "",
        ]
    )


def append_duplicate_log(
    duplicate_log_path: Path,
    *,
    artifact: DraftArtifact,
    matched_path: Path,
    duplicate_path: Path,
    timestamp: str,
) -> str:
    entry = "\n".join(
        [
            f"## DUPLICATE: {artifact.identifier}",
            "",
            f"- **Detected at:** {timestamp}",
            f"- **Source run ID:** {artifact.run_id}",
            f"- **Identity key:** {artifact.identity_key}",
            f"- **Incoming artifact filename:** {artifact.path.name}",
            f"- **Incoming source path:** {artifact.path}",
            f"- **Matched intake artifact:** {matched_path}",
            f"- **Duplicate folder path:** {duplicate_path}",
            "- **Action taken:** Routed to duplicate folder, no overwrite",
            "- **Notification status:** Included in run receipt",
            "- **Notes:** Automatic research-to-governance handoff detected an existing governed artifact.",
            "",
        ]
    )
    with duplicate_log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    return entry


def run_handoff(
    *,
    run_dir: Path,
    governance_root: Path,
    approval_timestamp: str,
    write: bool,
) -> HandoffResult:
    drafts = collect_drafts(run_dir)
    if not drafts:
        raise SystemExit(f"No ClickUp-ready draft artifacts found in {run_dir}")

    run_summary_candidates = sorted(run_dir.glob("*_run_summary_*.md"))
    if not run_summary_candidates:
        raise SystemExit(f"No run summary found in {run_dir}")
    run_summary_path = run_summary_candidates[0].resolve()

    run_ids = {artifact.run_id for artifact in drafts}
    if len(run_ids) != 1:
        raise SystemExit(f"Draft artifacts in {run_dir} map to multiple run IDs: {sorted(run_ids)}")
    run_id = next(iter(run_ids))

    intake_dir = governance_root / "governance-states" / "01_intake"
    duplicate_dir = governance_root / "governance-states" / "01_intake_duplicates"
    receipt_dir = governance_root / "governance-records" / "run-notifications"
    duplicate_log_path = governance_root / "governance-records" / "duplicate-log" / "DUPLICATE_LOG.md"

    for required in [intake_dir, duplicate_dir, receipt_dir, duplicate_log_path.parent]:
        if not required.exists():
            raise SystemExit(f"Required governance path not found: {required}")

    close_timestamp = datetime.fromtimestamp(
        run_summary_path.stat().st_mtime,
        tz=datetime.now().astimezone().tzinfo,
    ).strftime("%Y-%m-%d %H:%M:%S %Z")
    deposit_timestamp = now_stamp()
    date_str = datetime.now().astimezone().strftime("%Y_%m_%d")
    source_keys = {artifact.source_key for artifact in drafts}
    if len(source_keys) != 1:
        raise SystemExit(f"Draft artifacts in {run_dir} map to multiple source keys: {sorted(source_keys)}")
    source_key = next(iter(source_keys))

    receipt_path = receipt_dir / receipt_filename(source_key, date_str)

    deposited: list[tuple[DraftArtifact, Path]] = []
    duplicates: list[tuple[DraftArtifact, Path, Path]] = []

    for artifact in drafts:
        matched_path = existing_artifact_match(governance_root, artifact.identity_key)
        if matched_path is not None:
            duplicate_path = unique_duplicate_path(duplicate_dir, artifact.path.name)
            duplicates.append((artifact, matched_path, duplicate_path))
            continue
        destination = intake_dir / artifact.path.name
        deposited.append((artifact, destination))

    if receipt_path.exists():
        if write:
            raise SystemExit(f"Receipt already exists for run {run_id}: {receipt_path}")
        existing_deposited: list[tuple[DraftArtifact, Path]] = list(deposited)
        existing_duplicates: list[tuple[DraftArtifact, Path, Path]] = []
        for artifact, matched_path, duplicate_path in duplicates:
            if matched_path.parent.name == "01_intake_duplicates":
                existing_duplicates.append((artifact, matched_path, duplicate_path))
            else:
                existing_deposited.append((artifact, matched_path))
        return HandoffResult(
            deposited=existing_deposited,
            duplicates=existing_duplicates,
            receipt_path=receipt_path,
            status="already_completed",
            deposit_timestamp=deposit_timestamp,
            approval_timestamp=approval_timestamp,
            close_timestamp=close_timestamp,
            already_handed_off=True,
        )

    status = "completed_with_duplicates" if duplicates else "completed"

    if write:
        for artifact, destination in deposited:
            shutil.copy2(artifact.path, destination)
        for artifact, matched_path, duplicate_path in duplicates:
            shutil.copy2(artifact.path, duplicate_path)
            append_duplicate_log(
                duplicate_log_path,
                artifact=artifact,
                matched_path=matched_path,
                duplicate_path=duplicate_path,
                timestamp=deposit_timestamp,
            )

        receipt_text = build_receipt_text(
            run_id=run_id,
            run_summary_path=run_summary_path,
            close_timestamp=close_timestamp,
            approval_timestamp=approval_timestamp,
            deposit_timestamp=deposit_timestamp,
            deposited_paths=[path for _, path in deposited],
            duplicate_paths=[path for _, _, path in duplicates],
            source_paths=[artifact.path for artifact in drafts],
            status=status,
        )
        receipt_path.write_text(receipt_text, encoding="utf-8")

    return HandoffResult(
        deposited=deposited,
        duplicates=duplicates,
        receipt_path=receipt_path,
        status=status,
        deposit_timestamp=deposit_timestamp,
        approval_timestamp=approval_timestamp,
        close_timestamp=close_timestamp,
    )


def print_result(result: HandoffResult, write: bool) -> None:
    mode = "WRITE" if write else "DRY-RUN"
    print(f"[{mode}] Handoff status: {result.status}")
    print(f"[{mode}] Deposit timestamp: {result.deposit_timestamp}")
    print(f"[{mode}] Approval timestamp: {result.approval_timestamp}")
    print(f"[{mode}] Research run close timestamp: {result.close_timestamp}")
    print(f"[{mode}] Receipt path: {result.receipt_path}")
    print(f"[{mode}] Deposited artifact count: {len(result.deposited)}")
    for artifact, destination in result.deposited:
        print(f"  DEPOSIT {artifact.path.name} -> {destination}")
    print(f"[{mode}] Duplicate artifact count: {len(result.duplicates)}")
    for artifact, matched_path, duplicate_path in result.duplicates:
        print(f"  DUPLICATE {artifact.path.name} matches {matched_path} -> {duplicate_path}")
    if result.already_handed_off:
        print(f"[{mode}] Existing receipt preserved: {result.receipt_path}")


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).expanduser().resolve()
    governance_root = Path(args.governance_root).expanduser().resolve()

    if not run_dir.exists():
        raise SystemExit(f"Run directory not found: {run_dir}")
    if not governance_root.exists():
        raise SystemExit(f"Governance workspace not found: {governance_root}")

    approval_timestamp = args.approval_timestamp or now_stamp()
    result = run_handoff(
        run_dir=run_dir,
        governance_root=governance_root,
        approval_timestamp=approval_timestamp,
        write=args.write,
    )
    print_result(result, write=args.write)
    return 0


if __name__ == "__main__":
    sys.exit(main())
