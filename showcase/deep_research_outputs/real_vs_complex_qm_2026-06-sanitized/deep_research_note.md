# Deep Research Note: Real vs Complex Quantum Mechanics

Artifact status: `sanitized_real_run`

This is a sanitized long-form research note derived from a real QRA research cluster. It has been rewritten for public review. It is not a raw model trace, not a prompt transcript, and not a peer-reviewed result.

Private prompts, internal scoring signals, private memory contents, raw logs, private paths, and unpublished proof strategy have been removed.

## Source Cluster

The public source cluster centers on the question:

> Are complex numbers physically necessary in quantum mechanics, or are they a compact representation of a deeper real-valued structure?

Public sources used for this sanitized note:

- [Quantum theory based on real numbers can be experimentally falsified](https://arxiv.org/abs/2101.10873)
- [Quantum theory does not need complex numbers](https://arxiv.org/abs/2504.02808)
- [Quantum mechanics over real numbers fully reproduces standard quantum theory](https://arxiv.org/abs/2604.19482)
- [Imaginarity witness](https://arxiv.org/abs/2606.04763)

## Executive Summary

The live issue is not simply whether complex numbers appear in the standard Hilbert-space formalism. They obviously do. The sharper question is whether complex numbers are physically forced by empirical structure, or whether they are one representation of a deeper structure that can be encoded over real numbers if the composition rule, state space, or resource accounting is changed.

The cluster has three competing pressures.

First, the 2021 network-Bell style result argues that real and complex quantum theories can make different predictions in multipartite network scenarios. This shifts the question from taste in mathematical notation to possible empirical distinguishability.

Second, newer real-valued reconstruction attempts argue that this conclusion depends on which real theory is being tested. If the tested real theory uses an inadequate composition rule or an incomplete state-space characterization, then the falsification may apply to that restricted model rather than to every possible real-valued reformulation of quantum mechanics.

Third, resource-theoretic work on imaginarity treats the imaginary component of states or operators as an operational resource. That does not automatically prove complex numbers are ontologically fundamental, but it gives a more precise way to ask where "imaginarity" does work: in states, measurements, witnesses, transformations, or composition rules.

The provisional research conclusion is therefore cautious:

> The current evidence weakens the simple claim that complex numbers are straightforwardly forced by quantum phenomena. It does not yet settle whether real-valued formulations are explanatory equivalents, representational encodings, or physically revealing alternatives. The decisive issue appears to be composition: how independently prepared systems, local operations, and network correlations are represented in the real formulation.

## Claim Typing

| Claim | Type | Status |
| --- | --- | --- |
| Standard quantum mechanics uses complex Hilbert spaces. | formal | established background |
| Some network scenarios distinguish standard real quantum theory from complex quantum theory. | empirical/formal | supported by the 2021 falsification line, under its modeling assumptions |
| Newer real-valued frameworks claim to reproduce standard complex quantum predictions. | formal | active claim requiring careful comparison of assumptions |
| Complex numbers may be representationally convenient rather than physically fundamental. | interpretive | plausible but not settled |
| Imaginarity can be treated as a resource with witnesses and measures. | methodological/formal | supported by resource-theoretic work |
| The ontology of complex numbers is settled. | philosophical | not established |

## What The Agent Notices

The interesting feature of this cluster is that the papers do not merely disagree about a theorem. They appear to disagree about the target of the theorem.

One side says, in effect: if quantum systems are represented over real Hilbert spaces with the usual restrictions, there are network correlations that expose a gap between real and complex quantum theory.

The other side says: that target is too narrow. A real formulation can preserve the empirical content of quantum mechanics if the real state space and composition rule are constructed differently.

This makes the debate structurally similar to many reconstruction disputes. A no-go theorem often rules out a family of models under a precise set of assumptions. A later reconstruction may avoid the no-go result not by refuting the theorem, but by changing which assumption carries the physical load.

That is why the useful research question is not:

> Are complex numbers necessary?

but rather:

> Which structural role usually played by complex numbers must be preserved, and where can that role be moved in a real-valued formulation?

Possible locations for that role include:

- the single-system state space
- the composition rule for multipartite systems
- the allowed transformations
- the representation of local operations
- the treatment of independent sources
- the resource theory of imaginarity
- the operational constraints used in network experiments

## Why Composition Is The Load-Bearing Point

The 2021 falsification result is powerful because it uses multipartite network structure. The claim is not just that a single system can be represented one way or another. The issue is whether independent preparations and measurements across a network can be represented while preserving the same operational predictions.

That matters because single-system real encodings are comparatively easy to imagine. A complex vector can often be represented by real coordinates with extra structure. But a many-system theory must also say how systems combine, how locality is represented, and how independent sources remain independent.

The newer real-valued approaches appear to push back exactly at this point. They suggest that the conventional real tensor product may not be the only admissible composition rule for a real formulation intended to reproduce the full structure of complex quantum mechanics. If that is right, then the 2021 result may show that a particular real composition rule fails, not that every real-valued reconstruction fails.

This creates a useful diagnostic question for future reading:

> Does the real-valued theory preserve locality and independence as physical constraints, or does it recover empirical predictions by moving complex structure into a less visible part of the formalism?

If the latter, then the real theory may be empirically equivalent but explanatorily less revealing. If the former, then the real theory could be a serious challenge to the idea that complex numbers are physically necessary.

## Role Of Imaginarity Witnesses

The imaginarity-witness work sharpens the discussion from a different direction. Instead of asking whether the whole formalism can be made real, it asks how to detect and quantify non-real structure within a chosen reference basis.

This matters because it converts a philosophical question into a resource question:

- Which states count as real relative to a basis?
- Which observables reveal imaginary components?
- Can a finite witness family detect all imaginary states?
- Does the resulting measure coincide with existing measures such as robustness or trace-norm imaginarity?

This does not directly decide whether nature "uses" complex numbers. Resource theories are often representation-sensitive, and a reference-basis-dependent resource should not be immediately read as ontology. But the witness framework is still valuable because it marks where imaginary structure becomes operationally testable within a formal setting.

The research lead is to compare two notions:

1. **Eliminability:** Can the complete empirical theory be reformulated over real numbers?
2. **Operational visibility:** Given a formalism, can imaginary structure be witnessed, consumed, or measured as a resource?

These notions may come apart. Complex numbers might be eliminable at the level of global representation while imaginarity remains a useful resource within a particular operational description.

## Candidate Hypothesis

Status: `speculative`

The right distinction may not be "real vs complex" but "where the phase structure lives."

In standard quantum mechanics, complex phase is explicit in the scalar field. In a real-valued reconstruction, the same functional role may be redistributed into state-space geometry, a modified composition rule, or a hidden symplectic structure. In a resource theory of imaginarity, phase-like structure becomes visible again as a resource relative to a chosen basis.

Candidate hypothesis:

> Complex numbers may be mathematically eliminable from the scalar field while the structural role of complex phase remains unavoidable somewhere in the theory's composition, transformation, or resource structure.

This would reconcile part of both sides:

- The pro-real side may be right that complex scalars are not empirically forced as primitive objects.
- The pro-complex side may be right that the structure carried by complex phase cannot simply disappear.
- Imaginarity witnesses may help identify where that structure reappears operationally.

## What Would Falsify Or Weaken This Hypothesis

The hypothesis becomes weaker if a real-valued theory can satisfy all of the following without hiding complex structure elsewhere:

- reproduce all standard predictions
- preserve a physically natural notion of independent composition
- preserve local operation representation
- avoid additional constraints that look like complex structure in disguise
- give a simpler or more explanatory account than the complex formalism

It becomes stronger if every successful real reconstruction must introduce an equivalent replacement for complex phase, such as a special composition rule, symplectic structure, or resource constraint.

## Open Questions For Human Review

1. Does the newer real-valued construction preserve the same operational independence assumptions used in network Bell scenarios?
2. Is the modified composition rule physically motivated, or is it selected because it reproduces the complex theory?
3. Can imaginarity witnesses be made basis-independent enough to speak to the real-vs-complex debate?
4. Does "experimental indistinguishability" imply "foundational equivalence," or only empirical equivalence?
5. What minimal axioms force the structure usually represented by multiplication by `i`?

## Why This Is A Good QRA Example

This note is not just a paper summary. It shows the kind of long-form research behavior QRA is meant to support:

- grouping multiple public papers into a single active question
- separating formal, empirical, methodological, interpretive, and speculative claims
- tracking how a later paper pressures the conclusion of an earlier result
- turning a literature cluster into a candidate hypothesis
- marking what remains unresolved for human review

The value is not that the agent declares the debate solved. The value is that it preserves the structure of the debate and produces sharper next questions.

## Human Review Status

Status: `reviewed_for_publication`

This note is suitable as a public showcase artifact. It is not an accepted research result and should not be cited as a scientific claim independent of the source papers.
