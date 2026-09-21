# Enforcement-sufficient compression and certified codec

**Research phase:** September 20, 2026.

This phase asks:

> What is the smallest reusable description of an uncertain information component
> that preserves the enforcement decisions we need, including after composition?

The phase identifies an exact enforcement-relevant interface for the current
sequential-disclosure benchmark, calibrates approximation error directly in
incentive-margin terms, derives composition and storage laws, and implements a
proof-carrying planar codec in the originating research package.

## Main results

- Directed interface discrepancy equals the worst permitted contextual
  incentive-margin error; one additional sender can attain it.
- Directed errors add exactly under independent composition; exact surrounding
  components add no error.
- For fixed affine dimension d>=2 and probabilities bounded away from zero,
  reusable storage is achievable in
  `O(gamma^{-(d-1)/2} log(1/gamma))` bits and requires
  `Omega(gamma^{-(d-1)/2})` bits in the worst case for gamma-separated queries.
- The planar codec uses a convex-hull summary plus a rational sandwich certificate
  and returns zero fine, full fine, or `refine` near a decision boundary.
- Finite shared scenario labels can be retained and composed with an explicit
  error rule; erasing the label can invent a profitable cascade.

## Evidence boundary

The originating run passed 19,264 exact rational checks plus 250 valid compact
bundle comparisons and 250 corruption-rejection controls. The complete package
was replayed cleanly again before this repository record was created.

No new Lean, Palomar or external proof-kernel verification was run for R15.
Historical novelty remains unestablished. The strategic interpretation still
inherits the R08/R13 theorem chain.

- [Research note](manuscript/RESEARCH_NOTE.md)
- [Complete mathematical results](math/RESULTS.md)
- [Current state](CURRENT_STATE.md)
- [Verification status](VERIFICATION.json)
- [Source comparison](sources/NOTES.md)
