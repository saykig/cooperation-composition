import Continuation

open scoped BigOperators
open Filter Topology
namespace Cooperation
noncomputable section

/-- A single fully mixed assessment sequence, with arbitrary feasible receiver behavior.
Both public and private Bayes beliefs converge simultaneously. -/
theorem full_profile_consistency {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (ρ : (Fin n → Bool) → ℝ) (hρ : ∀ y, 0 ≤ ρ y ∧ ρ y ≤ 1) :
    ∃ (σs : ℕ → Strategy n) (ρs : ℕ → (Fin n → Bool) → ℝ),
      (∀ k, FullyMixed (σs k)) ∧
      (∀ k y, 0 < ρs k y ∧ ρs k y < 1) ∧
      (∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h))) ∧
      (∀ y, Tendsto (fun k => ρs k y) atTop (𝓝 (ρ y))) ∧
      (∀ h x, Tendsto (fun k => transcriptBayes p (σs k) h x) atTop
        (𝓝 (belief p (rateAt σ h) (observed h) x))) ∧
      (∀ h b x, Tendsto (fun k => senderBayes p (σs k) h b x) atTop
        (𝓝 (belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x))) := by
  obtain ⟨σs,hm,hs,hpub,hpriv⟩ := global_consistency_exists hp hσ
  obtain ⟨ρs,hrm,hrs⟩ := receiver_perturbation ρ hρ
  exact ⟨σs,ρs,hm,hrm,hs,hrs,hpub,hpriv⟩

/-- Actual transcript denominators are positive throughout a feasible completely mixed sequence. -/
theorem public_conditioning_positive {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : FullyMixed σ) (h : Hist n) :
    0 < ∑ x : Fin n → Bool, nature p x * prefixLikelihood σ h x := by
  simp only [prefixLikelihood_factor]
  exact normalizer_pos hp (rate_mixed hσ h) (observed h)

theorem private_conditioning_positive {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : FullyMixed σ) (h : Info n) (b : Bool) :
    0 < ∑ x : Fin n → Bool, nature p x * privateLikelihood σ h b x := by
  simp only [privateLikelihood_factor]
  exact normalizer_pos hp (rate_mixed hσ _) (privateObserved h b)

/-- Nonnegative primitive action probabilities sum to one; type zero is deterministic. -/
theorem feasible_action_probability {q : ℝ} (hq : 0 ≤ q ∧ q ≤ 1) (b : Bool) :
    (∀ a, 0 ≤ actionProbability q b a) ∧
      (∑ a : Bool, actionProbability q b a) = 1 := by
  cases b <;> constructor
  all_goals try (intro a; cases a <;> simp [actionProbability] <;> linarith)
  all_goals simp [actionProbability]

/-- Every continuation path weight is nonnegative under feasible behavioral strategies. -/
theorem continuation_weight_nonneg {n : ℕ} {σ : Strategy n} (hσ : Feasible σ)
    (h : Info n) (a : Bool) (x y : Fin n → Bool) :
    0 ≤ continuationWeight σ h a x y := by
  unfold continuationWeight
  split_ifs
  · apply Finset.prod_nonneg
    intro i _
    split_ifs
    · exact (feasible_action_probability (hσ _) (x i)).1 (y i)
    · norm_num
  · exact le_rfl

/-- The familiar mixed-tie payoff follows from the complete state/path expectation. -/
theorem mixed_tie_gain :
    senderPayoff (fun _ : Fin 2 => (1/2:ℝ)) (fun _ => (1/2:ℝ)) ⟨[],by decide⟩
      completeRule 1 (1/4) true -
    senderPayoff (fun _ : Fin 2 => (1/2:ℝ)) (fun _ => (1/2:ℝ)) ⟨[],by decide⟩
      completeRule 1 (1/4) false = 0 := by
  rw [sender_gain_complete _ _ _ (by intro j; exact Fin.elim0 j)]
  norm_num [Fin.prod_univ_two]

/-- Without the strict prior threshold, incomplete histories need not make C strict.
This is a two-sender example at the posterior limit of an off-path report. -/
theorem threshold_equality_counterexample :
    receiverGain (fun _ : Fin 2 => (1/2:ℝ)) (fun _ => 0)
      (fun i => if i = 0 then .silent else .report) 1 1 0 = 0 := by
  rw [receiver_gain_formula,all_positive_mass]
  norm_num [Fin.prod_univ_two,posterior]

/-- Endpoint zero-reach Bayes division is not the consistent limiting posterior. -/
theorem zero_report_requires_limit (p : ℝ) :
    atom p 0 .report true / localMass p 0 .report = 0 ∧ posterior p 0 .report = 1 := by
  simp [atom,evidence,localMass,posterior]

end
end Cooperation
