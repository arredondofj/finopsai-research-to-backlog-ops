#!/usr/bin/env python3
"""Backfill per-card activity files from existing governance records."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import run_intake_triage as triage


REPO_ROOT = Path(__file__).resolve().parent.parent
CARD_ACTIVITY_DIR = REPO_ROOT / "governance-records" / "card-activity"


def activity_path_for_artifact(artifact: Path) -> Path:
    return CARD_ACTIVITY_DIR / f"{artifact.stem}__activity.md"


def render_activity_file(
    artifact: Path,
    receipt_records: list[triage.ReceiptRecord],
    triage_batches: list[triage.TriageBatch],
) -> str:
    run_ids = sorted({record.run_id for record in receipt_records if record.run_id})
    lines = [
        f"# Card Activity - {artifact.name}",
        "",
        f"- **Source draft artifact:** `{artifact}`",
        f"- **Research run ID:** `{', '.join(run_ids) if run_ids else 'Unknown'}`",
        "",
        "## Activity Entries",
        "",
    ]

    for record in receipt_records:
        timestamp = record.deposit_timestamp or "Unknown timestamp"
        lines.extend(
            [
                f"### {timestamp} - Deposited to intake",
                "- **Event type:** deposit",
                "- **Recorded by:** Research workflow",
                f"- **Run receipt:** `{record.file_path}`",
                "- **State after event:** `governance-states/01_intake/`",
                f"- **Notes:** Handoff status `{record.handoff_status or 'unknown'}`.",
                "",
            ]
        )

    for batch in triage_batches:
        timestamp = batch.timestamp or batch.heading.removeprefix("## Intake triage batch: ").strip()
        lines.extend(
            [
                f"### {timestamp} - Surfaced to PO",
                "- **Event type:** triage_acknowledgment",
                "- **Recorded by:** Codex",
                f"- **Triage record:** `{triage.TRIAGE_LOG}`",
                "- **State after event:** `governance-states/01_intake/`",
                "- **Notes:** Item was surfaced in the intake triage batch.",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    CARD_ACTIVITY_DIR.mkdir(parents=True, exist_ok=True)
    artifacts = triage.list_intake_artifacts()
    receipt_index = triage.build_receipt_index(triage.parse_receipts())
    triage_index = triage.build_triage_index(triage.parse_triage_batches())

    created = 0
    for artifact in artifacts:
        target = activity_path_for_artifact(artifact)
        if target.exists():
            continue
        receipt_records = receipt_index.get(artifact.name, [])
        triage_batches = triage_index.get(artifact.name, [])
        target.write_text(
            render_activity_file(artifact, receipt_records, triage_batches),
            encoding="utf-8",
        )
        created += 1

    print(f"Created {created} card activity file(s) at {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
