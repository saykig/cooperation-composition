# Revisiting the research

Start with [PROGRESS.md](PROGRESS.md) to find the phase, then inspect its exact
mathematical statement, assumptions, source notes and evidence. R01–R02 concern
foundations and revision; R03–R15 develop information, disclosure, enforcement, sequential protocol composition and enforcement-sufficient compression.
The games and information assumptions change between phases: their numerical
results cannot be compared without checking those differences.

When fixing a claim, record which premise or calculation failed, which later
results depend on it, and what survives. Add a dated correction to the decision
ledger and link the corrected argument. Keep previous result receipts alongside
new runs instead of presenting a new computation as the old evidence.

Run each experiment using its phase's instructions. Repository-root research paths
in those instructions are relative to this working-ground directory. Source PDFs
and externally supplied inputs are available only where explicitly retained;
a source hash alone does not contain the input. Existing verification receipts
record earlier checks; moving these files is not a new verification run.

The larger revision experiment was prepared but never run. It remains a proposed
experiment, not an inherited result. Future work should not silently treat it as
completed.

For R08, preserve the distinction between (i) an actual model in which private
facts are independent, (ii) the analyst's shared uncertainty constraint over the
local positive probabilities, and (iii) an outer approximation formed from
separate coordinate ranges. The R08 enforcement gap comes from discarding the
shared analyst-side constraint, not from introducing correlation among the
realized private facts.

When extending R08, first test whether the proposed communication protocol makes
the alleged joint constraint reachable by a unilateral deviation. Do not infer a
strategic obstruction merely from an algebraic restriction on joint messages.


Before inheriting a theorem into a later phase, check
[VERIFICATION.md](VERIFICATION.md). A downstream result may rely on a written proof
that is not yet Lean-formalized. That is allowed, but the inherited status must not
be silently upgraded. Every new phase should record which prior statements it
uses and whether those statements are written, computationally checked or formally
proved.


For R15, distinguish the exact model family, its exact downward-hull/support
interface, a certified approximation of that interface, and arbitrary later
revision of the model family. The product/additive-error law applies only to the
declared independent or matched-label compositions. A compact interface is not
permission to answer an unmodeled future revision without recovering the source
family. Near zero margin, `refine` is the correct output.
