from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKIP_DIR_NAMES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "venv",
}


@dataclass(frozen=True)
class SecretFinding:
    path: str
    line: int
    pattern_name: str
    excerpt: str


def scan_text(text: str, path: str = "<memory>") -> list[SecretFinding]:
    findings: list[SecretFinding] = []
    for name, pattern in _secret_patterns():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            excerpt = match.group(0)[:32]
            findings.append(SecretFinding(path, line, name, excerpt))
    return findings


def scan_file(path: str | Path) -> list[SecretFinding]:
    file_path = Path(path)
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    return scan_text(text, str(file_path))


def scan_paths(paths: Iterable[str | Path]) -> list[SecretFinding]:
    findings: list[SecretFinding] = []
    for path in paths:
        file_path = Path(path)
        if file_path.is_dir():
            for child in iter_text_files(file_path):
                findings.extend(scan_file(child))
        elif file_path.exists():
            findings.extend(scan_file(file_path))
    return findings


def iter_text_files(root: str | Path) -> Iterable[Path]:
    root_path = Path(root)
    for path in sorted(root_path.rglob("*")):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.is_file():
            yield path


def _secret_patterns() -> list[tuple[str, re.Pattern[str]]]:
    return [
        ("openai-key-prefix", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")),
        ("openai-env-var", re.compile("OPENAI" + "_API_KEY")),
        ("anthropic-env-var", re.compile("ANTHROPIC" + "_API_KEY")),
        ("gemini-env-var", re.compile("GEMINI" + "_API_KEY")),
        ("google-env-var", re.compile("GOOGLE" + "_API_KEY")),
        ("github-token-env-var", re.compile("GITHUB" + "_TOKEN")),
        ("github-token-prefix", re.compile(r"\bghp" + r"_[A-Za-z0-9_]{20,}\b")),
        ("google-api-key-prefix", re.compile(r"\bAIza[A-Za-z0-9_-]{20,}\b")),
        ("private-key-block", re.compile("-----BEGIN " + "PRIVATE KEY-----")),
        ("slack-bot-token", re.compile(r"\bxoxb-[A-Za-z0-9-]{10,}\b")),
        ("local-user-path", re.compile(r"/Users/[A-Za-z0-9._ -]+/")),
        ("local-home-path", re.compile(r"/home/[A-Za-z0-9._ -]+/")),
        ("password-assignment", re.compile(r"(?i)\b" + "password" + r"\s*=")),
        ("secret-assignment", re.compile(r"(?i)\b" + "secret" + r"\s*=")),
        ("token-assignment", re.compile(r"(?i)\b" + "token" + r"\s*=")),
    ]
