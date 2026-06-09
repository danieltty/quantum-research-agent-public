# Demo Mode

Demo mode is designed to show the public artifact format and pipeline behavior. It is not the full research agent and does not include private research memory, production prompts, private scoring logic, scheduler configuration, or proprietary implementation details.

The demo:

- Reads `examples/sample_public_papers.json`.
- Avoids external API calls by default.
- Avoids production credentials.
- Generates a local run folder.
- Produces a daily report, triage table, provenance file, idea candidate file, manifest, and validation report.
- Marks generated artifacts as `demo`.
- Does not update private memory.

Run it with:

```bash
python scripts/generate_demo_run.py
```

The generated output is written to:

```text
examples/runs/generated-demo/
```

The demo scoring logic is intentionally simple and transparent. It is not the private production ranking logic.
