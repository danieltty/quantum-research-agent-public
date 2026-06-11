# Conceptual Workflow

This document describes the private research agent at a safe, public level. It is meant to communicate behavior and artifact boundaries without exposing private code architecture, implementation details, prompts, scoring heuristics, deployment configuration, or research memory.

```mermaid
flowchart TD
  A[Daily Cadence] --> B[Public Source Discovery]
  B --> C[Paper Metadata Normalization]
  C --> D[Relevance and Novelty Triage]
  M[Private Research Memory] --> D
  D --> E[Focused Paper Analysis]
  E --> F[Provenance-Backed Notes]
  F --> M
  M --> G[Candidate Connections and Hypotheses]
  G --> H[Human Review]
  H --> I[Accepted Notes / Rejected Leads / Follow-up Tasks]
  I --> M
  I --> B
```

## Workflow Steps

| Stage | Public description |
| --- | --- |
| Daily cadence | Runs the research loop on a regular cadence. |
| Source discovery | Finds public research items such as papers, feeds, and metadata. |
| Metadata normalization | Cleans source records into consistent paper records. |
| Triage | Ranks items by relevance and novelty for the research agenda. |
| Focused analysis | Extracts structured notes from selected items. |
| Provenance-backed notes | Links claims and observations back to source records. |
| Private research memory | Preserves unpublished research context and feeds later triage and synthesis. This layer is not published here. |
| Candidate connections and hypotheses | Proposes research leads for review. These are not final claims. |
| Human review | Final interpretation, acceptance, rejection, and follow-up remain human-led. |
| Feedback loop | Accepted notes and follow-up tasks can update memory and steer later source discovery. |

The public demo implements only a small deterministic simulation of the artifact flow. It does not include the private production pipeline, private code architecture, private prompts, private memory, scheduler configuration, or internal research strategy.
