import Bridge

open scoped BigOperators
namespace Cooperation
noncomputable section

/-- Recursive binary-tree path probability, independent of any product formula. -/
def treeMass (w : List Bool → Bool → ℝ) : List Bool → List Bool → ℝ
  | _, [] => 1
  | h, b :: ys => w h b * treeMass w (h ++ [b]) ys

lemma sum_states_succ {m : ℕ} (f : (Fin (m+1) → Bool) → ℝ) :
    (∑ y, f y) = ∑ b : Bool, ∑ ys : Fin m → Bool, f (Fin.cons b ys) := by
  rw [← (Fin.consEquiv (fun _ : Fin (m+1) => Bool)).sum_comp f]
  rw [Fintype.sum_prod_type]
  rfl

/-- Every finite binary behavioral tree has total mass one, even with arbitrary history dependence. -/
theorem tree_mass_sum (w : List Bool → Bool → ℝ)
    (hw : ∀ h, w h false + w h true = 1) (m : ℕ) (h : List Bool) :
    (∑ y : Fin m → Bool, treeMass w h (List.ofFn y)) = 1 := by
  induction m generalizing h with
  | zero => simp [treeMass]
  | succ m ih =>
    rw [sum_states_succ]
    simp_rw [List.ofFn_cons,treeMass,← Finset.mul_sum,ih]
    simpa [add_comm] using hw h

/-- Unrolling the recursive path probability yields the chain-rule product. -/
theorem tree_mass_product (w : List Bool → Bool → ℝ) {m : ℕ} (h : List Bool)
    (y : Fin m → Bool) :
    treeMass w h (List.ofFn y) = ∏ i : Fin m, w (h ++ (List.ofFn y).take i.val) (y i) := by
  induction m generalizing h with
  | zero => simp [treeMass]
  | succ m ih =>
    rw [List.ofFn_succ,treeMass,ih,Fin.prod_univ_succ]
    simp only [Fin.val_zero,List.take_zero,List.append_nil,Fin.val_succ,List.take_succ_cons]
    congr 1
    apply Finset.prod_congr rfl
    intro i _
    simp [List.append_assoc]

/-- Transition rule for the conditional continuation tree. Earlier messages and the
current forced action are deterministic; all later nodes use the declared strategies. -/
def forcedTransition {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x : Fin n → Bool) (past : List Bool) (b : Bool) : ℝ :=
  if hlen : past.length < h.val.length then
    if b = h.val[past.length] then 1 else 0
  else if past.length = h.val.length then
    if b = a then 1 else 0
  else if hn : past.length < n then
    actionProbability (σ ⟨past,hn⟩) (x ⟨past.length,hn⟩) b
  else if b = false then 1 else 0

lemma forced_transition_sum {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x : Fin n → Bool) (past : List Bool) :
    forcedTransition σ h a x past false + forcedTransition σ h a x past true = 1 := by
  unfold forcedTransition
  split_ifs <;> simp_all [actionProbability]
  all_goals split <;> simp_all


lemma forced_transition_at {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x y : Fin n → Bool) (i : Fin n) :
    forcedTransition σ h a x ((List.ofFn y).take i.val) (y i) =
      if hi : i.val < h.val.length then (if y i = h.val[i.val] then 1 else 0)
      else if i.val = h.val.length then (if y i = a then 1 else 0)
      else actionProbability (σ (pastInfo (terminalHist y) i)) (x i) (y i) := by
  simp [forcedTransition,List.length_take,i.isLt,
    pastInfo,terminalHist]

/-- The continuation weights used in the payoff calculation are exactly the recursively
constructed tree probabilities, including the fixed past and forced current action. -/
theorem continuation_weight_tree {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x y : Fin n → Bool) :
    treeMass (forcedTransition σ h a x) [] (List.ofFn y) = continuationWeight σ h a x y := by
  rw [tree_mass_product]
  simp only [List.nil_append]
  unfold continuationWeight
  by_cases hc : compatiblePath h a y
  · rw [if_pos hc]
    apply Finset.prod_congr rfl
    intro i _
    rw [forced_transition_at]
    by_cases hi : i.val < h.val.length
    · have hy := hc.1 ⟨i.val,hi⟩
      have hn : ¬ h.val.length < i.val := by omega
      simpa [hi,hn] using congrArg (fun b => if b = h.val[i.val] then (1:ℝ) else 0) hy
    · by_cases he : i.val = h.val.length
      · have hj : i = ⟨h.val.length,h.property⟩ := Fin.ext he
        subst i
        simp [hc.2]
      · have hg : h.val.length < i.val := by omega
        simp [hi,he,hg]
  · rw [if_neg hc]
    rcases not_and_or.mp hc with hh | ha
    · push Not at hh
      obtain ⟨j,hj⟩ := hh
      let i : Fin n := ⟨j.val,j.isLt.trans h.property⟩
      apply Finset.prod_eq_zero (Finset.mem_univ i)
      rw [forced_transition_at]
      simp [i,j.isLt,hj]
    · let i : Fin n := ⟨h.val.length,h.property⟩
      apply Finset.prod_eq_zero (Finset.mem_univ i)
      rw [forced_transition_at]
      simp [i,ha]

/-- The actual full continuation kernel is normalized for every state and forced action. -/
theorem continuation_weight_sum {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x : Fin n → Bool) :
    (∑ y : Fin n → Bool, continuationWeight σ h a x y) = 1 := by
  simp_rw [← continuation_weight_tree]
  exact tree_mass_sum _ (forced_transition_sum σ h a x) n []

/-- Together with nonnegativity, the primitive kernel is a probability distribution. -/
theorem continuation_probability_kernel {n : ℕ} {σ : Strategy n} (hσ : Feasible σ)
    (h : Info n) (a : Bool) (x : Fin n → Bool) :
    (∀ y, 0 ≤ continuationWeight σ h a x y) ∧
      (∑ y : Fin n → Bool, continuationWeight σ h a x y) = 1 := by
  exact ⟨continuation_weight_nonneg hσ h a x,continuation_weight_sum σ h a x⟩

end
end Cooperation
