# Evaluation And Evidence

This document explains what the public repository currently demonstrates and what remains deliberately out of scope.

## What Is Demonstrated

| Area | Public evidence |
| --- | --- |
| Always-on operation | Sanitized aggregate run history in `showcase/operations_summary.md`. |
| Structured pipeline | Conceptual workflow plus sample and sanitized run manifests. |
| Provenance discipline | Artifact schemas, provenance samples, and sanitized memory-update evidence. |
| Memory compounding | Public-safe example of how later runs use prior research context. |
| Hypothesis generation | Sanitized case study showing candidate leads separated from reviewed claims. |
| Long-form analysis | Sanitized deep-research note in `showcase/deep_research_outputs/`. |
| Reliability guardrails | CI workflow, schema validation, artifact-label checks, and secret scanning. |

## Current Sanitized Operating Snapshot

Artifact status: `sanitized_real_run`

The private system's reviewed local artifacts show:

- 86 recorded daily run manifests from 2026-03-08 through 2026-06-10.
- 80 run manifests marked `complete`.
- 31 latest consecutive run manifests marked `complete` as of 2026-06-10.
- Four recorded stages per run: ingest, analyze, synthesize, notify.
- 85 daily digest artifacts.
- 80 days with memory update records.
- 2,964 total memory update records across reviewed update-record artifacts.

These are aggregate counts from manually reviewed local artifacts. Raw logs, private source queues, prompts, hashes, private notes, scoring signals, and unpublished research details are not published.

## What Is Not Yet Claimed

This public repository does not claim:

- Independent proof of new physics.
- Peer-reviewed scientific discovery.
- Fully automated replacement of expert judgment.
- Public access to the production system.
- Publication of the private memory or production architecture.

The current evidence supports a narrower claim: QRA is an always-on research-assistance pipeline that produces structured, provenance-aware artifacts and candidate research leads for human review.

## Evaluation Priorities

The next useful public evaluations are:

- Expert review of selected candidate hypotheses.
- Before/after examples showing how memory changes later triage.
- Precision checks for high-priority paper recommendations.
- Failure-mode notes for cases where the system recommends no full read.
- Human ratings of whether a daily output saved research time.

Any future evaluation should keep private research IP, raw prompts, raw traces, and unpublished proof details out of the public repo.
