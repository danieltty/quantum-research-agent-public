from __future__ import annotations

import json
from pathlib import Path

from qra_public_demo.demo_pipeline import write_demo_run
from qra_public_demo.schema_validation import load_json, validate_json_file, validate_run_folder


ROOT = Path(__file__).resolve().parents[1]


def test_sample_paper_records_validate() -> None:
    records = load_json(ROOT / "examples" / "sample_public_papers.json")
    schema_path = ROOT / "schemas" / "paper_record.schema.json"

    assert records
    for index, record in enumerate(records):
        temp_path = ROOT / "examples" / f".test_paper_record_{index}.json"
        try:
            temp_path.write_text(json.dumps(record) + "\n", encoding="utf-8")
            assert validate_json_file(temp_path, schema_path) == []
        finally:
            temp_path.unlink(missing_ok=True)


def test_static_sample_run_manifest_validates() -> None:
    manifest = ROOT / "examples" / "runs" / "2026-06-01-sample" / "run_manifest.json"
    schema = ROOT / "schemas" / "run_manifest.schema.json"

    assert validate_json_file(manifest, schema) == []


def test_generated_demo_run_validates(tmp_path: Path) -> None:
    output_dir = tmp_path / "generated-demo"
    input_path = ROOT / "examples" / "sample_public_papers.json"

    write_demo_run(output_dir=output_dir, input_path=input_path)
    result = validate_run_folder(output_dir, ROOT / "schemas")

    assert result["valid"], result["errors"]
