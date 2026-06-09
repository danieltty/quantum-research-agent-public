from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


REQUIRED_RUN_FILES = {
    "run_manifest.json",
    "daily_report.md",
    "paper_triage.md",
    "idea_candidates.md",
    "provenance.json",
    "validation_report.json",
}


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_json_file(path: str | Path, schema_path: str | Path) -> list[str]:
    payload = load_json(path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def validate_run_folder(path: str | Path, schemas_dir: str | Path | None = None) -> dict[str, Any]:
    run_path = Path(path)
    schema_root = Path(schemas_dir) if schemas_dir else Path("schemas")
    errors: list[str] = []

    missing = sorted(REQUIRED_RUN_FILES - {item.name for item in run_path.iterdir()}) if run_path.exists() else sorted(REQUIRED_RUN_FILES)
    if missing:
        errors.append(f"missing required run files: {', '.join(missing)}")

    manifest_path = run_path / "run_manifest.json"
    if manifest_path.exists():
        errors.extend(
            f"run_manifest.json: {error}"
            for error in validate_json_file(manifest_path, schema_root / "run_manifest.schema.json")
        )

    provenance_path = run_path / "provenance.json"
    if provenance_path.exists():
        errors.extend(
            f"provenance.json: {error}"
            for error in validate_json_file(provenance_path, schema_root / "provenance.schema.json")
        )

    artifact_errors = check_artifact_status_markers(run_path)
    errors.extend(artifact_errors)

    return {
        "path": str(run_path),
        "valid": not errors,
        "errors": errors,
    }


def check_artifact_status_markers(path: str | Path) -> list[str]:
    root = Path(path)
    if not root.exists():
        return [f"{root}: path does not exist"]

    errors: list[str] = []
    for item in sorted(root.rglob("*")):
        if not item.is_file():
            continue
        if item.suffix == ".json":
            try:
                payload = load_json(item)
            except json.JSONDecodeError as exc:
                errors.append(f"{item}: invalid JSON: {exc}")
                continue
            if not _json_has_artifact_status(payload):
                errors.append(f"{item}: missing artifact_status")
        elif item.suffix in {".md", ".txt"}:
            text = item.read_text(encoding="utf-8")
            if "artifact status" not in text.lower():
                errors.append(f"{item}: missing artifact status marker")
    return errors


def _json_has_artifact_status(payload: Any) -> bool:
    if isinstance(payload, dict):
        if "artifact_status" in payload:
            return True
        return any(_json_has_artifact_status(value) for value in payload.values())
    if isinstance(payload, list):
        return any(_json_has_artifact_status(item) for item in payload)
    return False
