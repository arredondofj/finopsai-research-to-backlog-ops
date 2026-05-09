#!/usr/bin/env python3
"""Produce a read-only daily intake review with context-quality assessment."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import run_intake_triage as triage


CRITICAL_SECTIONS = [
    "Title",
    "Requirement / Problem Statement",
    "Expected Outcome",
    "Scope",
    "Acceptance Criteria",
    "Constraints",
    "Dependencies / References",
]

SUPPORTING_SECTIONS = [
    "Business Context",
    "Subtasks",
    "Notes / Operational Rule",
]


@dataclass
class ContextAssessment:
    level: str
    recommendation: str
    strengths: list[str]
    gaps: list[str]
    rationale: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-status",
        action="append",
        dest="include_statuses",
        help=(
            "Restrict assessment to one or more triage statuses. "
            "Example: --include-status 'New to PO review'"
        ),
    )
    return parser.parse_args()


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^## (.+)$", text, flags=re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[name] = text[start:end].strip()
    return sections


def count_list_items(section_text: str) -> int:
    return len(
        re.findall(r"^\s*(?:- |\d+\. )", section_text, flags=re.MULTILINE)
    )


def has_concrete_reference_paths(section_text: str) -> bool:
    return any(token in section_text for token in ["/Users/", "ResearchToBacklogOps/", "Repo-FinOpsAI/"])


def assess_context(artifact: triage.ArtifactResult) -> ContextAssessment:
    text = artifact.full_path.read_text(encoding="utf-8")
    sections = parse_sections(text)

    missing_critical = [name for name in CRITICAL_SECTIONS if not sections.get(name)]
    missing_supporting = [name for name in SUPPORTING_SECTIONS if not sections.get(name)]

    strengths: list[str] = []
    gaps: list[str] = []

    if not missing_critical:
        strengths.append("all critical task-card sections are present")
    else:
        gaps.append(f"missing critical sections: {', '.join(missing_critical)}")

    acceptance_items = count_list_items(sections.get("Acceptance Criteria", ""))
    if acceptance_items >= 3:
        strengths.append("acceptance criteria are explicit enough to guide PO review")
    elif sections.get("Acceptance Criteria"):
        gaps.append("acceptance criteria exist but are thin for governance review")

    if has_concrete_reference_paths(sections.get("Dependencies / References", "")):
        strengths.append("references include concrete research or repo evidence paths")
    elif sections.get("Dependencies / References"):
        gaps.append("references exist but do not clearly ground the task in specific evidence")

    excluded_scope = sections.get("Scope", "")
    if "Excluded" in excluded_scope or "### Excluded" in text:
        strengths.append("scope boundaries include explicit exclusions")
    else:
        gaps.append("scope boundaries do not clearly state exclusions")

    if artifact.anomalies:
        gaps.append(f"intake-state anomalies present: {', '.join(artifact.anomalies)}")

    if missing_supporting and len(missing_supporting) < len(SUPPORTING_SECTIONS):
        gaps.append(f"missing supporting sections: {', '.join(missing_supporting)}")

    if len(missing_critical) >= 2 or not sections.get("Requirement / Problem Statement"):
        return ContextAssessment(
            level="Weak",
            recommendation="Reject",
            strengths=strengths,
            gaps=gaps or ["card is too incomplete for governed intake"],
            rationale="Critical task-card structure is missing, so the item is not governable enough to enter review responsibly.",
        )

    if artifact.anomalies or missing_critical or gaps:
        return ContextAssessment(
            level="Partial",
            recommendation="Hold",
            strengths=strengths,
            gaps=gaps,
            rationale="The card looks directionally useful but still needs clarification or record cleanup before review admission is advisable.",
        )

    return ContextAssessment(
        level="Strong",
        recommendation="Admit to review",
        strengths=strengths,
        gaps=gaps,
        rationale="The card is bounded, evidenced, and structured well enough for the Product Owner to move it into formal review.",
    )


def select_results(
    results: list[triage.ArtifactResult],
    include_statuses: list[str] | None,
) -> list[triage.ArtifactResult]:
    if include_statuses:
        allowed = set(include_statuses)
        return [result for result in results if result.status in allowed]
    default_statuses = {"New to PO review", "Awaiting intake decision", "Held in intake"}
    return [result for result in results if result.status in default_statuses]


def render_report(
    results: list[triage.ArtifactResult],
    assessments: list[tuple[triage.ArtifactResult, ContextAssessment]],
) -> str:
    lines = [
        "# Backlog Governance Daily Intake Review",
        "",
        "## Intake Summary",
        f"- Intake artifacts assessed: {len(assessments)}",
        f"- Total artifacts currently in intake: {len(results)}",
        "",
        "## Artifact Status",
    ]

    if not assessments:
        lines.append("- No intake artifacts matched the requested review scope.")
    else:
        for artifact, assessment in assessments:
            lines.append(
                f"- `{artifact.filename}`: status `{artifact.status}`, context `{assessment.level}`, recommendation `{assessment.recommendation}`"
            )

    lines.extend(["", "## Context Assessment"])
    if not assessments:
        lines.append("- None")
    else:
        for artifact, assessment in assessments:
            lines.append(f"### {artifact.filename}")
            if assessment.strengths:
                lines.append("- Strengths:")
                for strength in assessment.strengths:
                    lines.append(f"  - {strength}")
            if assessment.gaps:
                lines.append("- Gaps:")
                for gap in assessment.gaps:
                    lines.append(f"  - {gap}")
            if not assessment.strengths and not assessment.gaps:
                lines.append("- No additional context signals were detected.")

    lines.extend(["", "## Recommendation"])
    if not assessments:
        lines.append("- No recommendations generated.")
    else:
        for artifact, assessment in assessments:
            lines.append(f"- `{artifact.filename}` -> `{assessment.recommendation}`")

    lines.extend(["", "## Rationale"])
    if not assessments:
        lines.append("- None")
    else:
        for artifact, assessment in assessments:
            lines.append(f"- `{artifact.filename}`: {assessment.rationale}")

    lines.extend(["", "## PO Next Step"])
    if not assessments:
        lines.append("- No PO intake action is required from this daily review pass.")
    else:
        lines.append("- Review the recommendations artifact by artifact before recording any governance decision.")
        lines.append("- Record accepted decisions in the matching file under `governance-records/card-activity/`.")
        lines.append("- Move only PO-admitted artifacts into `governance-states/02_review/` after the decision is logged.")

    lines.extend(["", "## Record Update Guidance"])
    lines.append("- This report is read-only and does not write triage acknowledgments or PO decisions.")
    lines.append("- If new intake items have not yet been acknowledged, run `python3 BacklogGovernanceOps/scripts/run_intake_triage.py --write` only after confirming the dry-run result.")
    lines.append("- Use the recommendation here as decision support, not as an automatic state transition.")

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    missing_paths = triage.validate_paths()
    if missing_paths:
        for path in missing_paths:
            print(f"Missing required path: {path}", file=sys.stderr)
        return 1

    artifacts = triage.list_intake_artifacts()
    receipt_index = triage.build_receipt_index(triage.parse_receipts())
    triage_index = triage.build_triage_index(triage.parse_triage_batches())
    governance_index = triage.build_governance_index(triage.parse_governance_decisions())
    results, _ = triage.classify_artifacts(
        artifacts,
        receipt_index,
        triage_index,
        governance_index,
    )

    selected = select_results(results, args.include_statuses)
    assessments = [(artifact, assess_context(artifact)) for artifact in selected]
    sys.stdout.write(render_report(results, assessments))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
