import Transcripts

open scoped BigOperators
namespace Cooperation
noncomputable section
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- Receiver's primitive payoff from D; payoff from C is zero. -/
def defectPayoff (A B e : ℝ) (x : ι → Bool) : ℝ :=
  if x = (fun _ => true) then B-e else -A-e

def receiverGain (p q : ι → ℝ) (o : ι → Observation) (A B e : ℝ) : ℝ :=
  ∑ x : ι → Bool, belief p q o x * defectPayoff A B e x

lemma all_positive_mass (p q : ι → ℝ) (o : ι → Observation) :
    belief p q o (fun _ => true) = ∏ i, posterior (p i) (q i) (o i) := by
  simp [belief,nature,bern]

/-- Derivation from the finite expected payoff, using normalization. -/
theorem receiver_gain_formula (p q : ι → ℝ) (o : ι → Observation) (A B e : ℝ) :
    receiverGain p q o A B e = (A+B) * belief p q o (fun _ => true) - A-e := by
  have ht (x : ι → Bool) :
      belief p q o x * defectPayoff A B e x =
      (if x = (fun _ => true) then (A+B)*belief p q o x else 0) -
        (A+e)*belief p q o x := by
    unfold defectPayoff
    split_ifs <;> ring
  unfold receiverGain
  simp_rw [ht]
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum]
  simp [belief_sum]
  ring

lemma all_positive_le_coordinate {p q : ι → ℝ} (o : ι → Observation)
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1) (j : ι) :
    belief p q o (fun _ => true) ≤ posterior (p j) (q j) (o j) := by
  rw [all_positive_mass]
  have h := Finset.prod_le_prod_of_subset_of_le_one
    (s := {j}) (t := Finset.univ) (f := fun i => posterior (p i) (q i) (o i))
    (by simp) (fun i _ => (posterior_bounds (hp i) (hq i) (o i)).1)
    (fun i _ _ => (posterior_bounds (hp i) (hq i) (o i)).2)
  simpa using h

theorem incomplete_receiver_strict {p q : ι → ℝ} {o : ι → Observation}
    {A B e : ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1)
    (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1) (hA : 0 < A) (hB : 0 < B) (he : 0 ≤ e)
    (ht : ∀ i, p i < A/(A+B)) (j : ι) (hj : o j = .silent) :
    receiverGain p q o A B e < 0 := by
  have hm := all_positive_le_coordinate o hp hq j
  rw [hj] at hm
  have hs := (silent_posterior_bounds (hp j) (hq j)).2
  have hqτ := lt_of_le_of_lt (hm.trans hs) (ht j)
  have hv := (lt_div_iff₀ (add_pos hA hB)).mp hqτ
  rw [receiver_gain_formula]
  nlinarith

theorem complete_receiver_gain (p q : ι → ℝ) (A B e : ℝ) :
    receiverGain p q (fun _ => .report) A B e = B-e := by
  rw [receiver_gain_formula,all_positive_mass]
  simp [posterior]

/-- A mixed action is optimal exactly when every action in its support is optimal.
This is derived below from comparison with every feasible mixed deviation. -/
def BestReply (g r : ℝ) : Prop :=
  0 ≤ r ∧ r ≤ 1 ∧ ∀ s : ℝ, 0 ≤ s → s ≤ 1 → s*g ≤ r*g

theorem bestReply_negative {g r : ℝ} (hg : g < 0) : BestReply g r ↔ r = 0 := by
  constructor
  · rintro ⟨hr,_,h⟩
    have h0 := h 0 (by norm_num) (by norm_num)
    nlinarith
  · rintro rfl
    refine ⟨le_rfl,by norm_num,?_⟩
    intro s hs _
    nlinarith

theorem bestReply_positive {g r : ℝ} (hg : 0 < g) : BestReply g r ↔ r = 1 := by
  constructor
  · rintro ⟨_,hr,h⟩
    have h1 := h 1 (by norm_num) le_rfl
    nlinarith
  · rintro rfl
    refine ⟨by norm_num,le_rfl,?_⟩
    intro s _ hs
    nlinarith

theorem bestReply_zero (r : ℝ) : BestReply 0 r ↔ 0 ≤ r ∧ r ≤ 1 := by
  simp [BestReply]


/-- A full transcript represented by its message at each protocol position. -/
def terminalHist {n : ℕ} (y : Fin n → Bool) : Hist n :=
  ⟨List.ofFn y, by simp⟩

def completeRule {n : ℕ} (y : Fin n → Bool) : ℝ := if y = (fun _ => true) then 1 else 0

lemma terminal_observed {n : ℕ} (y : Fin n → Bool) (i : Fin n) :
    observed (terminalHist y) i = if y i then .report else .silent := by
  simp [observed,terminalHist,i.isLt]

/-- The primitive expected payoff uniquely determines the receiver's whole strategy below B. -/
theorem terminal_bestReply_below {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    {A B e : ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (hA : 0 < A) (hB : 0 < B) (he : 0 ≤ e) (heB : e < B)
    (ht : ∀ i, p i < A/(A+B)) (y : Fin n → Bool) (r : ℝ) :
    BestReply (receiverGain p (rateAt σ (terminalHist y)) (observed (terminalHist y)) A B e) r ↔
      r = completeRule y := by
  by_cases hc : y = (fun _ => true)
  · subst y
    have ho : observed (terminalHist (fun _ : Fin n => true)) = (fun _ => .report) := by
      funext i; simp [terminal_observed]
    rw [ho,complete_receiver_gain]
    simpa [completeRule] using (bestReply_positive (r := r) (sub_pos.mpr heB))
  · obtain ⟨i,hi⟩ : ∃ i, y i = false := by
      by_contra! hh
      apply hc
      funext i
      cases hy : y i <;> simp_all
    have hs : observed (terminalHist y) i = .silent := by simp [terminal_observed,hi]
    have hg := incomplete_receiver_strict hp (rate_feasible hσ (terminalHist y)) hA hB he ht i hs
    simpa [completeRule,hc] using (bestReply_negative (r := r) hg)

/-- At the complete report history the boundary fine permits any receiver mixture. -/
theorem complete_bestReply_boundary (p q : ι → ℝ) (A B r : ℝ) :
    BestReply (receiverGain p q (fun _ => .report) A B B) r ↔ 0 ≤ r ∧ r ≤ 1 := by
  simp [complete_receiver_gain,bestReply_zero]

/-- Above B the receiver strictly prefers C even at the complete report history. -/
theorem complete_bestReply_above (p q : ι → ℝ) (A B e r : ℝ) (he : B < e) :
    BestReply (receiverGain p q (fun _ => .report) A B e) r ↔ r = 0 := by
  rw [complete_receiver_gain]
  exact bestReply_negative (sub_neg.mpr he)

end
end Cooperation
