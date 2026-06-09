# Security Policy

This repository is intended to contain only public documentation, demo code, schemas, and sanitized or sample artifacts.

Do not commit:

- API keys or tokens
- `.env` files
- private repository URLs
- raw production logs
- private prompts
- unpublished research notes
- model traces or hidden reasoning logs
- scheduler or deployment credentials
- private file paths or deployment names

Before publishing new artifacts, run:

```bash
python scripts/validate_public_repo.py
```

If sensitive material is accidentally committed, remove it from history before making the repository public.
