# Privacy And Sanitization

Use an allowlist publication model. Only publish artifacts created specifically for this public repo or manually reviewed and sanitized from production outputs.

## Do Not Publish

Before publishing an artifact, check that it does not contain:

- API keys, tokens, webhook URLs, credentials, private config, or private repository URLs.
- Raw model traces or hidden reasoning logs.
- Full prompts from the production agent.
- Private research notes or unpublished proof attempts.
- Personal data, emails, messages, or private documents.
- Internal scoring heuristics that reveal the actual research strategy.
- File paths, machine names, deployment names, branch names, or commit hashes that should remain private.
- Scheduler credentials, deployment settings, database URLs, or private infrastructure details.

## Allowed Public Material

Allowed material includes:

- High-level architecture.
- Public paper metadata.
- Short sanitized summaries.
- Example JSON schemas.
- Demo scripts using fake or sample inputs.
- Public-facing documentation.
- Sanitized run manifests after manual review.
- Validation scripts that check for secrets and required fields.

## Review Process

1. Create or export the artifact outside the private source tree.
2. Remove private notes, prompts, raw traces, private paths, and unpublished proof details.
3. Mark the artifact with the correct `artifact_status`.
4. Run `python scripts/validate_public_repo.py`.
5. Manually inspect the artifact before publishing.
