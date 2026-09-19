# Primitive-game checker

Install the pinned `requirements.txt` in a separate environment, then run:

```sh
python check.py --output new-results.json
python -O check.py --output new-optimized-results.json
```

Do not overwrite the retained `results.json`. Timings may differ; mathematical
fields must agree. Explicit exception checks remain active under `python -O`.

## Independence from the formula being audited

`game.py` contains no suffix-product characterization. It enumerates all Nature
states, all relevant public histories, actual future message paths, and terminal
receiver actions. It computes beliefs by perturbing every positive-type behavioral
probability with an exact polynomial in ε, applying Bayes' rule, and extracting
the leading coefficients as ε→0. It checks both actions at every positive-type
information set, and both receiver actions at every terminal information set.
Type-zero agents have one feasible action. Costs are charged only on reporting;
the fine changes only receiver payoffs.

`pure_equilibria` exhausts every pure sender contingent plan and every receiver
pure best reply, including ties. At n=3 there are 2^7=128 sender plans per game;
receiver ties can multiply this count. This is not merely enumeration of behavior
along the all-report path. The backward candidate is also verified at ALL histories
after construction. A noncredible all-silent off-path threat is rejected.

`mixed.py` gives every positive-type information set and every terminal receiver
information set a real probability in [0,1]. Expected gains are built by state/path
enumeration. Best-reply complementarity and the all-silent target are encoded as
exact polynomial constraints. Belief denominators can be cleared because their
positivity was proved from the primitive likelihoods; no cascade condition is
inserted. Z3 QF_NRA decisions cover arbitrary real mixing, not a grid of probabilities.
They retain backend trust and are not external proof-kernel certificates.

Only `historical_prediction` in `check.py` uses R08's formula, on the comparison
side. A code audit can check that it does not feed the candidate construction,
pure enumeration, payoff checker or mixed-equilibrium solver.

## Coverage and what the counts mean

The first retained run checks 20 base games at five fines each, including 0,
B/2, B−10^-20, B and B+1/7. Pure enumeration is done at 0 and B; tree/mixed checks
cover the other fines. Twenty-four shared-family/order cases and fifteen selected
four-sender/fine cases add order and size coverage. Three explicit nonpure tie
assessments are checked directly.

Totals: 3,324 complete pure profiles; 139 mixed-equilibrium queries; 142 fully
audited constructed assessments; 312 information sets with exact posterior limits
under distinct tremble-rate sequences; 100 incomplete-terminal receiver checks.
Two negative strategy controls and four invalid-domain controls are included.
The run took about 16 seconds on its recorded environment. This is not a complexity
or scalability claim.

Pure enumeration alone cannot exclude mixed rescues. The all-mixed written
backward argument is the general proof; exact real-arithmetic queries independently
test finite games. The prior R08 4,802-check receipt is not replayed or replaced:
its original executable was not retained. This is a new, explicitly separate suite.

## Explicit boundaries

Zero/one priors, a prior at or above τ, zero disclosure costs and negative fines
are outside the declared theorem. Invalid input is rejected rather than counted
as a failed theorem. Exact sender ties and the receiver tie at e=B are inside the
theorem and are tested. n=1 is an additional algorithmic boundary case, not a
claim that R08 originally required it. No random sampling or tolerance decides
equilibrium existence.
