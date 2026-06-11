# Memory Compounding Example

Artifact status: `sanitized_real_run`

This is a generalized example derived from the structure of real private run artifacts. It demonstrates how QRA is designed to compound research context over time without publishing private memory contents.

## Pattern

QRA is designed so that a daily run can leave behind structured memory updates. Later runs can use those updates as context for triage, synthesis, and hypothesis generation.

```text
Run N
  source material -> structured notes -> provenance refs -> memory update

Run N + 1
  new source material + prior memory -> relation detection -> refined question

Run N + k
  accumulated context -> candidate hypothesis -> human review
```

## Public Example

| Step | Public description |
| --- | --- |
| Initial observation | A source item raises a question about how a formal assumption relates to an interpretation-level claim. |
| Memory update | QRA records a structured update with provenance and confidence metadata. |
| Later run | A new item is compared against the existing memory rather than treated as an isolated paper. |
| Synthesis signal | The system detects that the new item may pressure or refine an earlier question. |
| Research outcome | QRA generates a follow-up lead for human review instead of presenting it as an established result. |

## Why This Matters

One-shot summarization answers only the current prompt. QRA is designed to preserve research state so repeated runs can become more useful over time.

The public repository does not include the private memory itself. It only shows the pattern: durable context, provenance, confidence labels, and human review.
