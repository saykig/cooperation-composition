import Beliefs

open scoped BigOperators
open Filter Topology

namespace Cooperation
noncomputable section

abbrev Hist (n : ℕ) := { h : List Bool // h.length ≤ n }
abbrev Info (n : ℕ) := { h : List Bool // h.length < n }
abbrev Strategy (n : ℕ) := Info n → ℝ

def Feasible {n : ℕ} (σ : Strategy n) := ∀ h, 0 ≤ σ h ∧ σ h ≤ 1
def FullyMixed {n : ℕ} (σ : Strategy n) := ∀ h, 0 < σ h ∧ σ h < 1

/-- Type zero has only silence; type one uses its behavior at the whole prefix. -/
def actionProbability (q : ℝ) (bit report : Bool) : ℝ :=
  if bit then (if report then q else 1-q) else (if report then 0 else 1)

def pastInfo {n : ℕ} (h : Hist n) (i : Fin n) : Info n :=
  ⟨h.val.take i.val, by
    have : (h.val.take i.val).length ≤ i.val := by simp
    exact this.trans_lt i.isLt⟩

def rateAt {n : ℕ} (σ : Strategy n) (h : Hist n) (i : Fin n) : ℝ :=
  if i.val < h.val.length then σ (pastInfo h i) else 1/2

def observed {n : ℕ} (h : Hist n) (i : Fin n) : Observation :=
  if hi : i.val < h.val.length then
    if h.val[i.val] then .report else .silent
  else .unseen

/-- Chain-rule path likelihood, defined from feasible action probabilities. -/
def prefixLikelihood {n : ℕ} (σ : Strategy n) (h : Hist n) (x : Fin n → Bool) : ℝ :=
  ∏ i, if hi : i.val < h.val.length then
    actionProbability (σ (pastInfo h i)) (x i) h.val[i.val]
    else 1

/-- Bayesian conditioning on the actual public transcript, not a stipulated posterior. -/
def transcriptBayes {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Hist n)
    (x : Fin n → Bool) : ℝ :=
  (nature p x * prefixLikelihood σ h x) /
    ∑ y : Fin n → Bool, nature p y * prefixLikelihood σ h y

theorem prefixLikelihood_factor {n : ℕ} (σ : Strategy n) (h : Hist n) (x : Fin n → Bool) :
    prefixLikelihood σ h x = likelihood (rateAt σ h) (observed h) x := by
  apply Finset.prod_congr rfl
  intro i _
  unfold rateAt observed
  split_ifs with hi hb
  all_goals cases hx : x i <;> simp_all [actionProbability, evidence]

theorem transcriptBayes_eq {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Hist n)
    (x : Fin n → Bool) :
    transcriptBayes p σ h x = bayes p (rateAt σ h) (observed h) x := by
  simp only [transcriptBayes, prefixLikelihood_factor, bayes, normalizer, joint]

lemma rate_feasible {n : ℕ} {σ : Strategy n} (hσ : Feasible σ) (h : Hist n) :
    ∀ i, 0 ≤ rateAt σ h i ∧ rateAt σ h i ≤ 1 := by
  intro i; unfold rateAt; split_ifs
  · exact hσ _
  · norm_num

lemma rate_mixed {n : ℕ} {σ : Strategy n} (hσ : FullyMixed σ) (h : Hist n) :
    ∀ i, 0 < rateAt σ h i ∧ rateAt σ h i < 1 := by
  intro i; unfold rateAt; split_ifs
  · exact hσ _
  · norm_num

lemma rate_tendsto {n : ℕ} {σs : ℕ → Strategy n} {σ : Strategy n}
    (hs : ∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h))) (h : Hist n) (i : Fin n) :
    Tendsto (fun k => rateAt (σs k) h i) atTop (𝓝 (rateAt σ h i)) := by
  unfold rateAt
  split_ifs
  · exact hs _
  · exact tendsto_const_nhds

theorem transcript_bayes_limit {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    {σs : ℕ → Strategy n} (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (hm : ∀ k, FullyMixed (σs k))
    (hs : ∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h)))
    (h : Hist n) (x : Fin n → Bool) :
    Tendsto (fun k => transcriptBayes p (σs k) h x) atTop
      (𝓝 (belief p (rateAt σ h) (observed h) x)) := by
  simp only [transcriptBayes_eq]
  exact bayes_tendsto hp (rate_feasible hσ h) (fun k => rate_mixed (hm k) h)
    (rate_tendsto hs h) (observed h) x

def privateObserved {n : ℕ} (h : Info n) (b : Bool) : Fin n → Observation :=
  fun i => if i.val = h.val.length then .known b else observed ⟨h.val,h.property.le⟩ i

def privateLikelihood {n : ℕ} (σ : Strategy n) (h : Info n) (b : Bool)
    (x : Fin n → Bool) : ℝ :=
  prefixLikelihood σ ⟨h.val,h.property.le⟩ x *
    if x ⟨h.val.length,h.property⟩ = b then 1 else 0

def senderBayes {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n) (b : Bool)
    (x : Fin n → Bool) : ℝ :=
  (nature p x * privateLikelihood σ h b x) /
    ∑ y : Fin n → Bool, nature p y * privateLikelihood σ h b y

theorem privateLikelihood_factor {n : ℕ} (σ : Strategy n) (h : Info n) (b : Bool)
    (x : Fin n → Bool) :
    privateLikelihood σ h b x =
      likelihood (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x := by
  classical
  let j : Fin n := ⟨h.val.length,h.property⟩
  let H : Hist n := ⟨h.val,h.property.le⟩
  have ho : observed H j = .unseen := by simp [observed,H,j]
  have heq (i : Fin n) :
      evidence (rateAt σ H i) (privateObserved h b i) (x i) =
      evidence (rateAt σ H i) (observed H i) (x i) *
        (if i = j then (if x j = b then 1 else 0) else 1) := by
    by_cases hi : i = j
    · subst i; simp [privateObserved,j,ho,evidence,H,observed]
    · have hv : i.val ≠ h.val.length := by
        intro hv; apply hi; apply Fin.ext; exact hv
      simp [privateObserved,hv,hi,H]
  change privateLikelihood σ h b x = ∏ i, evidence (rateAt σ H i) (privateObserved h b i) (x i)
  simp_rw [heq]
  rw [Finset.prod_mul_distrib]
  simp [privateLikelihood, prefixLikelihood_factor,likelihood,j,H]

theorem senderBayes_eq {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n) (b : Bool)
    (x : Fin n → Bool) :
    senderBayes p σ h b x =
      bayes p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x := by
  simp only [senderBayes, privateLikelihood_factor, bayes, normalizer, joint]

theorem sender_bayes_limit {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    {σs : ℕ → Strategy n} (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (hm : ∀ k, FullyMixed (σs k))
    (hs : ∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h)))
    (h : Info n) (b : Bool) (x : Fin n → Bool) :
    Tendsto (fun k => senderBayes p (σs k) h b x) atTop
      (𝓝 (belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x)) := by
  simp only [senderBayes_eq]
  exact bayes_tendsto hp (rate_feasible hσ _) (fun k => rate_mixed (hm k) _)
    (rate_tendsto hs _) (privateObserved h b) x

theorem global_consistency_exists {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ) :
    ∃ σs : ℕ → Strategy n,
      (∀ k, FullyMixed (σs k)) ∧
      (∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h))) ∧
      (∀ h x, Tendsto (fun k => transcriptBayes p (σs k) h x) atTop
        (𝓝 (belief p (rateAt σ h) (observed h) x))) ∧
      (∀ h b x, Tendsto (fun k => senderBayes p (σs k) h b x) atTop
        (𝓝 (belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x))) := by
  let σs : ℕ → Strategy n := fun k h => tremble k (σ h)
  have hm : ∀ k, FullyMixed (σs k) := fun k h => tremble_mixed k (hσ h)
  have hs : ∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h)) := fun h => tremble_tendsto _
  exact ⟨σs,hm,hs,transcript_bayes_limit hp hσ hm hs,sender_bayes_limit hp hσ hm hs⟩


/-- Uniqueness against an arbitrary convergent, fully mixed GLOBAL strategy sequence. -/
theorem global_consistency_unique {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    {σs : ℕ → Strategy n} (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (hm : ∀ k, FullyMixed (σs k))
    (hs : ∀ h, Tendsto (fun k => σs k h) atTop (𝓝 (σ h)))
    (μ : Hist n → (Fin n → Bool) → ℝ)
    (ν : Info n → Bool → (Fin n → Bool) → ℝ)
    (hμ : ∀ h x, Tendsto (fun k => transcriptBayes p (σs k) h x) atTop (𝓝 (μ h x)))
    (hν : ∀ h b x, Tendsto (fun k => senderBayes p (σs k) h b x) atTop (𝓝 (ν h b x))) :
    (∀ h x, μ h x = belief p (rateAt σ h) (observed h) x) ∧
    (∀ h b x, ν h b x =
      belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h b) x) := by
  constructor
  · intro h x
    exact tendsto_nhds_unique (hμ h x) (transcript_bayes_limit hp hσ hm hs h x)
  · intro h b x
    exact tendsto_nhds_unique (hν h b x) (sender_bayes_limit hp hσ hm hs h b x)

/-- Receiver behavior can be perturbed along the very same sequence index.
It never enters transcript likelihoods: the receiver moves strictly after every sender. -/
theorem receiver_perturbation {n : ℕ} (ρ : (Fin n → Bool) → ℝ)
    (hρ : ∀ y, 0 ≤ ρ y ∧ ρ y ≤ 1) :
    ∃ ρs : ℕ → (Fin n → Bool) → ℝ,
      (∀ k y, 0 < ρs k y ∧ ρs k y < 1) ∧
      (∀ y, Tendsto (fun k => ρs k y) atTop (𝓝 (ρ y))) := by
  exact ⟨fun k y => tremble k (ρ y), fun k y => tremble_mixed k (hρ y),
    fun y => tremble_tendsto (ρ y)⟩

end
end Cooperation
