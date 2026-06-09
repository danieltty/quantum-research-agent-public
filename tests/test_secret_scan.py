from __future__ import annotations

from qra_public_demo.secret_scan import scan_text


def test_openai_env_var_is_flagged() -> None:
    secret_name = "OPENAI" + "_API_KEY"

    findings = scan_text(f"{secret_name}=example")

    assert findings
    assert findings[0].pattern_name == "openai-env-var"


def test_github_token_prefix_is_flagged() -> None:
    github_value = "ghp" + "_abcdefghijklmnopqrstuvwxyz"

    findings = scan_text(github_value)

    assert findings
    assert findings[0].pattern_name == "github-token-prefix"


def test_normal_sample_text_is_not_flagged() -> None:
    text = "Artifact status: sample. This public demo contains fictional paper records."

    assert scan_text(text) == []
