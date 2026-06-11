from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qra_public_demo.schema_validation import load_json, validate_json_file, validate_run_folder
from qra_public_demo.secret_scan import scan_paths


REQUIRED_FILES = [
    "README.md",
    "LICENSE_NOTICE.md",
    "SECURITY.md",
    ".gitignore",
    ".env.example",
    "pyproject.toml",
    "docs/architecture.md",
    "docs/evidence_policy.md",
    "docs/demo_mode.md",
    "docs/evaluation.md",
    "docs/limitations.md",
    "docs/claim_language.md",
    "docs/why_qra_is_different.md",
    "docs/roadmap_public.md",
    "examples/README.md",
    "examples/sample_public_papers.json",
    "examples/knowledge_state_sample.md",
    "examples/agent_output_sample.md",
    "schemas/run_manifest.schema.json",
    "schemas/paper_record.schema.json",
    "schemas/provenance.schema.json",
    "schemas/analysis_report.schema.json",
    "scripts/generate_demo_run.py",
    "scripts/validate_public_repo.py",
    "src/qra_public_demo/__init__.py",
    "src/qra_public_demo/demo_pipeline.py",
    "src/qra_public_demo/schema_validation.py",
    "src/qra_public_demo/secret_scan.py",
    "tests/test_schema_validation.py",
    "tests/test_secret_scan.py",
    ".github/workflows/validate.yml",
    "showcase/README.md",
    "showcase/operations_summary.md",
    "showcase/memory_compounding_example.md",
    "showcase/hypothesis_case_study.md",
    "showcase/deep_research_outputs/real_vs_complex_qm_2026-06-sanitized/deep_research_note.md",
    "showcase/deep_research_outputs/real_vs_complex_qm_2026-06-sanitized/provenance.json",
    "showcase/deep_research_outputs/real_vs_complex_qm_2026-06-sanitized/review_status.json",
    "showcase/sanitized_runs/2026-06-10/run_manifest.json",
    "showcase/sanitized_runs/2026-06-10/stage_summary.json",
    "showcase/sanitized_runs/2026-06-10/daily_report.md",
    "showcase/sanitized_runs/2026-06-10/validation_report.json",
]


def main() -> int:
    failures: list[str] = []

    failures.extend(_check_required_files())
    failures.extend(_check_sample_papers())
    failures.extend(_check_run_folders())
    failures.extend(_check_showcase_artifacts())
    failures.extend(_check_secret_scan())

    if failures:
        print("Public repository validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public repository validation passed.")
    print("- Required files present")
    print("- Sample paper records validate")
    print("- Run folders validate")
    print("- Showcase artifacts validate")
    print("- Secret scan passed")
    return 0


def _check_required_files() -> list[str]:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    return [f"missing required file: {path}" for path in missing]


def _check_sample_papers() -> list[str]:
    paper_path = ROOT / "examples" / "sample_public_papers.json"
    schema_path = ROOT / "schemas" / "paper_record.schema.json"
    failures: list[str] = []

    try:
        records = load_json(paper_path)
    except Exception as exc:
        return [f"sample_public_papers.json could not be read: {exc}"]

    if not isinstance(records, list) or not records:
        return ["sample_public_papers.json must contain a non-empty list"]

    for index, record in enumerate(records):
        temp_path = ROOT / "examples" / f".paper_record_{index}.tmp.json"
        try:
            temp_path.write_text(
                __import__("json").dumps(record, indent=2) + "\n", encoding="utf-8"
            )
            errors = validate_json_file(temp_path, schema_path)
            failures.extend(f"sample_public_papers.json[{index}]: {error}" for error in errors)
        finally:
            temp_path.unlink(missing_ok=True)
    return failures


def _check_run_folders() -> list[str]:
    runs_root = ROOT / "examples" / "runs"
    failures: list[str] = []
    for run_path in sorted(path for path in runs_root.iterdir() if path.is_dir()):
        result = validate_run_folder(run_path, ROOT / "schemas")
        failures.extend(result["errors"])
    return failures


def _check_showcase_artifacts() -> list[str]:
    failures: list[str] = []
    manifest = ROOT / "showcase" / "sanitized_runs" / "2026-06-10" / "run_manifest.json"
    failures.extend(
        f"showcase/sanitized_runs/2026-06-10/run_manifest.json: {error}"
        for error in validate_json_file(manifest, ROOT / "schemas" / "run_manifest.schema.json")
    )

    for path in [
        ROOT / "showcase" / "operations_summary.md",
        ROOT / "showcase" / "memory_compounding_example.md",
        ROOT / "showcase" / "hypothesis_case_study.md",
        ROOT / "showcase" / "deep_research_outputs" / "real_vs_complex_qm_2026-06-sanitized" / "deep_research_note.md",
        ROOT / "showcase" / "sanitized_runs" / "2026-06-10" / "daily_report.md",
    ]:
        text = path.read_text(encoding="utf-8")
        if "Artifact status:" not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing artifact status marker")
    return failures


def _check_secret_scan() -> list[str]:
    findings = scan_paths([ROOT])
    return [
        f"possible secret in {finding.path}:{finding.line} ({finding.pattern_name})"
        for finding in findings
    ]


if __name__ == "__main__":
    raise SystemExit(main())
