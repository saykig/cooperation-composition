# Cooperation & Enforcement

[![Research verification](https://github.com/saykig/cooperation-enforcement/actions/workflows/research-verification.yml/badge.svg)](https://github.com/saykig/cooperation-enforcement/actions/workflows/research-verification.yml)

This repository records the development of my MA major thesis: the questions, proofs, counterexamples, literature notes, computational experiments, failed directions, and changes in argument as the research develops.

Current literature already has substantial work on cooperation, information design, signaling, incentives, enforcement, and strategic communication. I am not trying to rebuild those literatures; instead, I am interested in a place where they seem to remain somewhat fragmented. Consider the following question: **what happens to cooperation when different information sources and strategic actors are connected, and when institutions can respond by changing either who learns what or how strongly cooperation is enforced?**

This is an abstract mathematical question, but the structure appears in real security institutions. In Ukraine, increasingly autonomous systems combine battlefield information, targeting and human decision authority, as seen in [Reuters reporting on Ukrainian drone units using AI guidance and targeting](https://www.reuters.com/business/aerospace-defense/ukrainian-drone-pilots-look-ai-battlefield-edge-2025-11-29/). Across NATO and the Arctic, uncrewed surveillance systems collect, fuse and distribute information across states before it reaches military decision-makers, including through [NATO's expansion of its intelligence, surveillance and reconnaissance fleet for the Arctic and High North](https://www.nato.int/en/news-and-events/articles/news/2026/07/07/nato-expands-its-intelligence-surveillance-and-reconnaissance-fleet-with-the-purchase-of-triton-aircraft). These systems raise a broader question: when information is distributed across actors and technologies, how does connecting it change the incentives and enforcement required for cooperation?

## Current evolving research question

> How do connected information structures determine the incentives or enforcement required to sustain cooperation?

## Broader programme and current proving ground

This thesis is the current proving ground for a broader research programme:
building reusable mathematical interfaces for consequential decision-making under
uncertainty, strategic interaction and changing information.

“Universal” here does not mean one equation that predicts every outcome. It means
that the mathematical pieces should be interoperable: uncertainty, dynamics,
strategy, incentives, enforcement and other components should be reusable across
different domains when their assumptions and interfaces match.

Cooperation and enforcement are the current test case. Security and war are
important applications, not the intended boundary of the mathematics. The same
underlying interfaces should eventually be testable in other settings such as AI
coordination, biosecurity and institutional bargaining.

The canonical research-purpose statement, including the September 20 clarification,
is recorded in the [research north star](docs/working-ground/research/foundations/NORTH_STAR.md).


*The current research question is in its rough draft and will evolve over time. The purpose of this repository is to preserve the research trajectory of the paper*

## Working ground

The [research working ground](docs/working-ground/README.md) collects the mathematical research, progress ledger, counterexamples and evidence, beginning August 13, 2026. The [verification ledger](docs/working-ground/VERIFICATION.md) states exactly which results have written proofs, computational checks, or Lean coverage.

The latest [enforcement-sufficient compression phase](docs/working-ground/research/enforcement_codec_2026_09_20/manuscript/RESEARCH_NOTE.md)
asks what a minimal reusable information interface must retain to preserve
enforcement decisions under composition. It derives an operational error measure,
composition law and fixed-dimensional storage bounds, and records a proof-carrying
planar codec from the originating run. These new compression results remain
written proofs plus exact computational evidence; they are not yet Lean-verified.
