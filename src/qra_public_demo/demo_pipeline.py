from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RELEVANCE_KEYWORDS: dict[str, int] = {
    "quantum foundations": 4,
    "operational theories": 3,
    "relational quantum mechanics": 3,
    "reconstruction": 3,
    "hidden variables": 2,
    "contextuality": 2,
    "generalized probabilistic theories": 2,
    "foundations": 1,
}


def load_sample_papers(path: str | Path) -> list[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("sample paper input must be a JSON list")
    return data


def score_paper(record: dict[str, Any]) -> dict[str, Any]:
    topics = [str(topic).lower() for topic in record.get("topics", [])]
    title = str(record.get("title", "")).lower()
    abstract = str(record.get("abstract", "")).lower()
    searchable = " ".join([title, abstract, *topics])

    matched: list[str] = []
    score = 0
    for keyword, points in RELEVANCE_KEYWORDS.items():
        if keyword in searchable:
            matched.append(keyword)
            score += points

    return {
        "paper_id": record.get("paper_id", ""),
        "title": record.get("title", ""),
        "authors": record.get("authors", []),
        "year": record.get("year"),
        "source": record.get("source", ""),
        "url": record.get("url", ""),
        "topics": record.get("topics", []),
        "artifact_status": "demo",
        "score": score,
        "matched_keywords": matched,
        "priority": "low",
        "rationale": _rationale(matched),
    }


def triage_papers(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    scored = [score_paper(record) for record in records]
    scored.sort(key=lambda item: (-int(item["score"]), str(item["title"])))

    for index, item in enumerate(scored):
        score = int(item["score"])
        if index == 0 and score > 0:
            item["priority"] = "high"
        elif score >= 4:
            item["priority"] = "medium"
        else:
            item["priority"] = "low"
    return scored


def generate_daily_report(
    triage: list[dict[str, Any]],
    run_id: str = "generated-demo",
    artifact_status: str = "demo",
) -> str:
    rows = [
        "| Priority | Paper | Reason |",
        "| --- | --- | --- |",
    ]
    for item in triage:
        rows.append(
            f"| {item['priority'].title()} | {item['title']} | {item['rationale']} |"
        )

    return "\n".join(
        [
            "# Daily Research Report",
            "",
            f"Run ID: `{run_id}`  ",
            f"Artifact status: `{artifact_status}`  ",
            "Pipeline mode: `public_demo`  ",
            "Human review status: `not_reviewed`",
            "",
            "## Summary",
            "",
            "This demo report shows the shape of a daily autonomous research-agent artifact. It is not a production run.",
            "",
            "## Top Items",
            "",
            *rows,
            "",
            "## Candidate Connections",
            "",
            "- Compare operational reconstruction themes against relational fact assumptions.",
            "- Check whether hidden-variable constraints are structural or only terminological.",
            "- Identify which contextuality claims require mathematical follow-up.",
            "",
            "## Follow-Up Tasks",
            "",
            "- Human review of the high-priority item.",
            "- Verify source claims before adding any item to private research memory.",
            "- Keep speculative candidates separate from accepted notes.",
            "",
        ]
    )


def generate_paper_triage(
    triage: list[dict[str, Any]],
    run_id: str = "generated-demo",
    artifact_status: str = "demo",
) -> str:
    rows = [
        "| Priority | Paper ID | Title | Score | Rationale |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in triage:
        rows.append(
            f"| {item['priority'].title()} | {item['paper_id']} | {item['title']} | {item['score']} | {item['rationale']} |"
        )

    return "\n".join(
        [
            "# Paper Triage",
            "",
            f"Run ID: `{run_id}`  ",
            f"Artifact status: `{artifact_status}`  ",
            "Pipeline mode: `public_demo`",
            "",
            *rows,
            "",
            "This demo triage uses transparent toy scoring. It is not the private production scoring logic.",
            "",
        ]
    )


def generate_idea_candidates(
    triage: list[dict[str, Any]],
    run_id: str = "generated-demo",
    artifact_status: str = "demo",
) -> str:
    top = triage[0] if triage else {"title": "No paper", "matched_keywords": []}
    matched = ", ".join(top.get("matched_keywords", [])) or "no matched keyword"

    return "\n".join(
        [
            "# Idea Candidates",
            "",
            f"Run ID: `{run_id}`  ",
            f"Artifact status: `{artifact_status}`  ",
            "Pipeline mode: `public_demo`",
            "",
            "These candidates are speculative demo outputs. They are not reviewed research claims.",
            "",
            "## Candidate 1",
            "",
            f"Use `{top['title']}` as a starting point for comparing {matched} themes against the current research agenda.",
            "",
            "Status: `speculative`",
            "",
            "## Candidate 2",
            "",
            "Separate structural claims from terminology matches before treating any connection as substantive.",
            "",
            "Status: `speculative`",
            "",
            "## Candidate 3",
            "",
            "Record rejected leads explicitly so future runs do not repeatedly surface the same weak connection.",
            "",
            "Status: `speculative`",
            "",
        ]
    )


def generate_provenance(
    run_id: str,
    records: list[dict[str, Any]],
    outputs: list[str],
    artifact_status: str = "demo",
) -> dict[str, Any]:
    return {
        "artifact_status": artifact_status,
        "run_id": run_id,
        "source_type": "sample_public_input",
        "sources": [
            {
                "paper_id": record.get("paper_id", ""),
                "title": record.get("title", ""),
                "source": record.get("source", ""),
                "url": record.get("url", ""),
                "artifact_status": artifact_status,
            }
            for record in records
        ],
        "outputs": [
            {
                "path": output,
                "artifact_status": artifact_status,
                "description": "Generated public demo artifact.",
            }
            for output in outputs
        ],
    }


def write_demo_run(
    output_dir: str | Path = "examples/runs/generated-demo",
    input_path: str | Path = "examples/sample_public_papers.json",
) -> None:
    output_path = Path(output_dir)
    records = load_sample_papers(input_path)
    triage = triage_papers(records)
    run_id = output_path.name
    outputs = [
        "daily_report.md",
        "paper_triage.md",
        "idea_candidates.md",
        "provenance.json",
        "validation_report.json",
    ]

    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True)

    manifest = {
        "run_id": run_id,
        "artifact_status": "demo",
        "source_type": "sample_public_input",
        "created_at": _now_iso(),
        "pipeline_mode": "public_demo",
        "input_files": [str(input_path)],
        "outputs": outputs,
        "human_review_status": "not_reviewed",
        "notes": "Generated by public demo mode. Not a production run.",
    }
    provenance = generate_provenance(run_id, records, outputs, "demo")
    validation_report = {
        "artifact_status": "demo",
        "validation_passed": True,
        "checks": {
            "required_files_present": True,
            "schemas_valid": True,
            "secret_scan_passed": True,
            "artifact_status_present": True,
        },
        "notes": "Generated demo validation report. Run validate_public_repo.py for repository-level checks.",
    }

    _write_json(output_path / "run_manifest.json", manifest)
    (output_path / "daily_report.md").write_text(
        generate_daily_report(triage, run_id), encoding="utf-8"
    )
    (output_path / "paper_triage.md").write_text(
        generate_paper_triage(triage, run_id), encoding="utf-8"
    )
    (output_path / "idea_candidates.md").write_text(
        generate_idea_candidates(triage, run_id), encoding="utf-8"
    )
    _write_json(output_path / "provenance.json", provenance)
    _write_json(output_path / "validation_report.json", validation_report)


def _rationale(matched: list[str]) -> str:
    if not matched:
        return "No direct keyword match in the public demo scoring rules."
    return "Matches public demo themes: " + ", ".join(matched) + "."


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
