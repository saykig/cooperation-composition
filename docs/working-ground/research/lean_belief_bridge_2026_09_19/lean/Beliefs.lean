import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Tactic

open scoped BigOperators
open Filter Topology

namespace Cooperation
noncomputable section

/-- Independent Bernoulli mass, with `true` denoting a positive fact. -/
def bern (p : ℝ) (b : Bool) : ℝ := if b then p else 1 - p

inductive Observation
  | unseen | silent | report | known (b : Bool)
  deriving DecidableEq

/-- A fixed transcript contributes one conditional action likelihood per bit.
`known` is the current sender's private observation, not another message. -/
def evidence (q : ℝ) (o : Observation) (b : Bool) : ℝ :=
  match o with
  | .unseen => 1
  | .silent => if b then 1 - q else 1
  | .report => if b then q else 0
  | .known a => if b = a then 1 else 0

def atom (p q : ℝ) (o : Observation) (b : Bool) := bern p b * evidence q o b
def localMass (p q : ℝ) (o : Observation) := ∑ b : Bool, atom p q o b

/-- Candidate extension; its identification with Bayes and all consistent limits
is a theorem below, not an axiom of the model. -/
def posterior (p q : ℝ) : Observation → ℝ
  | .unseen => p
  | .silent => p * (1-q) / (1-p*q)
  | .report => 1
  | .known a => if a then 1 else 0

lemma bern_sum (p : ℝ) : ∑ b : Bool, bern p b = 1 := by
  simp [bern, Fintype.sum_bool]

lemma mass_unseen (p q : ℝ) : localMass p q .unseen = 1 := by
  simp [localMass, atom, evidence, bern, Fintype.sum_bool]

lemma mass_silent (p q : ℝ) : localMass p q .silent = 1-p*q := by
  simp [localMass, atom, evidence, bern, Fintype.sum_bool]
  ring

lemma mass_report (p q : ℝ) : localMass p q .report = p*q := by
  simp [localMass, atom, evidence, bern, Fintype.sum_bool]

lemma mass_known (p q : ℝ) (b : Bool) : localMass p q (.known b) = bern p b := by
  cases b <;> simp [localMass, atom, evidence, bern, Fintype.sum_bool]

lemma silent_den_pos {p q : ℝ} (hp : 0 < p ∧ p < 1) (hq : 0 ≤ q ∧ q ≤ 1) :
    0 < 1-p*q := by
  have := mul_le_mul_of_nonneg_left hq.2 hp.1.le
  nlinarith [hp.2]

lemma localMass_pos {p q : ℝ} (hp : 0 < p ∧ p < 1) (hq : 0 < q ∧ q < 1)
    (o : Observation) : 0 < localMass p q o := by
  cases o with
  | unseen => rw [mass_unseen]; norm_num
  | silent => rw [mass_silent]; exact silent_den_pos hp ⟨hq.1.le,hq.2.le⟩
  | report => rw [mass_report]; exact mul_pos hp.1 hq.1
  | known b => rw [mass_known]; cases b <;> simp [bern] <;> linarith [hp.1,hp.2]

lemma atom_factor {p q : ℝ} (hp : 0 < p ∧ p < 1) (hq : 0 ≤ q ∧ q ≤ 1)
    (o : Observation) (b : Bool) :
    atom p q o b = localMass p q o * bern (posterior p q o) b := by
  have hd := ne_of_gt (silent_den_pos hp hq)
  cases o with
  | unseen => rw [mass_unseen]; simp [atom, evidence, posterior]
  | report => rw [mass_report]; cases b <;> simp [atom, evidence, bern, posterior]
  | known a => rw [mass_known]; cases a <;> cases b <;> simp [atom, evidence, bern, posterior]
  | silent =>
      rw [mass_silent]
      cases b <;> simp [atom, evidence, bern, posterior]
      all_goals (field_simp [hd] <;> ring)

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def nature (p : ι → ℝ) (x : ι → Bool) := ∏ i, bern (p i) (x i)
def likelihood (q : ι → ℝ) (o : ι → Observation) (x : ι → Bool) :=
  ∏ i, evidence (q i) (o i) (x i)
def joint (p q : ι → ℝ) (o : ι → Observation) (x : ι → Bool) :=
  nature p x * likelihood q o x
def normalizer (p q : ι → ℝ) (o : ι → Observation) := ∑ x : ι → Bool, joint p q o x
def bayes (p q : ι → ℝ) (o : ι → Observation) (x : ι → Bool) :=
  joint p q o x / normalizer p q o
def belief (p q : ι → ℝ) (o : ι → Observation) (x : ι → Bool) :=
  nature (fun i => posterior (p i) (q i) (o i)) x

theorem nature_sum (p : ι → ℝ) : ∑ x : ι → Bool, nature p x = 1 := by
  unfold nature
  rw [← Fintype.prod_sum]
  simp [bern]

theorem joint_product (p q : ι → ℝ) (o : ι → Observation) (x : ι → Bool) :
    joint p q o x = ∏ i, atom (p i) (q i) (o i) (x i) := by
  simp [joint, nature, likelihood, atom, Finset.prod_mul_distrib]

theorem normalizer_product (p q : ι → ℝ) (o : ι → Observation) :
    normalizer p q o = ∏ i, localMass (p i) (q i) (o i) := by
  simp only [normalizer, joint_product, localMass]
  exact (Fintype.prod_sum _).symm

theorem normalizer_pos {p q : ι → ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1)
    (hq : ∀ i, 0 < q i ∧ q i < 1) (o : ι → Observation) :
    0 < normalizer p q o := by
  rw [normalizer_product]
  exact Finset.prod_pos (fun i _ => localMass_pos (hp i) (hq i) (o i))

theorem bayes_factorization {p q : ι → ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1)
    (hq : ∀ i, 0 < q i ∧ q i < 1) (o : ι → Observation) (x : ι → Bool) :
    bayes p q o x = belief p q o x := by
  have hn := ne_of_gt (normalizer_pos hp hq o)
  unfold bayes
  apply (div_eq_iff hn).2
  rw [joint_product, normalizer_product]
  simp only [belief, nature]
  rw [← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i _
  rw [atom_factor (hp i) ⟨(hq i).1.le,(hq i).2.le⟩]
  ring

theorem belief_sum (p q : ι → ℝ) (o : ι → Observation) :
    ∑ x : ι → Bool, belief p q o x = 1 := nature_sum _

lemma silent_posterior_bounds {p q : ℝ} (hp : 0 < p ∧ p < 1)
    (hq : 0 ≤ q ∧ q ≤ 1) :
    0 ≤ posterior p q .silent ∧ posterior p q .silent ≤ p := by
  have hd := silent_den_pos hp hq
  constructor
  · exact div_nonneg (mul_nonneg hp.1.le (sub_nonneg.mpr hq.2)) hd.le
  · change p*(1-q)/(1-p*q) ≤ p
    apply (div_le_iff₀ hd).2
    have hz := mul_nonneg (mul_nonneg hp.1.le hq.1) (sub_nonneg.mpr hp.2.le)
    nlinarith

lemma posterior_bounds {p q : ℝ} (hp : 0 < p ∧ p < 1)
    (hq : 0 ≤ q ∧ q ≤ 1) (o : Observation) :
    0 ≤ posterior p q o ∧ posterior p q o ≤ 1 := by
  cases o with
  | unseen => exact ⟨hp.1.le,hp.2.le⟩
  | silent => exact ⟨(silent_posterior_bounds hp hq).1,
      (silent_posterior_bounds hp hq).2.trans hp.2.le⟩
  | report => simp [posterior]
  | known b => cases b <;> simp [posterior]

lemma bern_nonneg {p : ℝ} (hp : 0 ≤ p ∧ p ≤ 1) (b : Bool) : 0 ≤ bern p b := by
  cases b <;> simp [bern] <;> linarith [hp.1,hp.2]

theorem nature_nonneg {p : ι → ℝ} (hp : ∀ i, 0 ≤ p i ∧ p i ≤ 1)
    (x : ι → Bool) : 0 ≤ nature p x :=
  Finset.prod_nonneg (fun i _ => bern_nonneg (hp i) (x i))

theorem belief_nonneg {p q : ι → ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1)
    (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1) (o : ι → Observation) (x : ι → Bool) :
    0 ≤ belief p q o x :=
  nature_nonneg (fun i => posterior_bounds (hp i) (hq i) (o i)) x

lemma posterior_tendsto {p q : ℝ} {qs : ℕ → ℝ}
    (hp : 0 < p ∧ p < 1) (hq : 0 ≤ q ∧ q ≤ 1)
    (hs : Tendsto qs atTop (𝓝 q)) (o : Observation) :
    Tendsto (fun k => posterior p (qs k) o) atTop (𝓝 (posterior p q o)) := by
  cases o with
  | unseen => exact tendsto_const_nhds
  | report => exact tendsto_const_nhds
  | known b => exact tendsto_const_nhds
  | silent =>
      exact (tendsto_const_nhds.mul (tendsto_const_nhds.sub hs)).div
        (tendsto_const_nhds.sub (tendsto_const_nhds.mul hs))
        (ne_of_gt (silent_den_pos hp hq))

theorem belief_tendsto {p q : ι → ℝ} {qs : ℕ → ι → ℝ}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1)
    (hs : ∀ i, Tendsto (fun k => qs k i) atTop (𝓝 (q i)))
    (o : ι → Observation) (x : ι → Bool) :
    Tendsto (fun k => belief p (qs k) o x) atTop (𝓝 (belief p q o x)) := by
  unfold belief nature
  apply tendsto_finsetProd
  intro i _
  have h := posterior_tendsto (hp i) (hq i) (hs i) (o i)
  cases x i <;> simp only [bern, Bool.false_eq_true, ↓reduceIte]
  · exact tendsto_const_nhds.sub h
  · exact h

theorem bayes_tendsto {p q : ι → ℝ} {qs : ℕ → ι → ℝ}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1)
    (hm : ∀ k i, 0 < qs k i ∧ qs k i < 1)
    (hs : ∀ i, Tendsto (fun k => qs k i) atTop (𝓝 (q i)))
    (o : ι → Observation) (x : ι → Bool) :
    Tendsto (fun k => bayes p (qs k) o x) atTop (𝓝 (belief p q o x)) := by
  have heq : (fun k => bayes p (qs k) o x) = fun k => belief p (qs k) o x := by
    funext k; exact bayes_factorization hp (hm k) o x
  rw [heq]
  exact belief_tendsto hp hq hs o x

def tremble (k : ℕ) (q : ℝ) : ℝ :=
  (q + 1 / ((k : ℝ)+1)) / (1 + 2*(1 / ((k : ℝ)+1)))

lemma tremble_mixed (k : ℕ) {q : ℝ} (hq : 0 ≤ q ∧ q ≤ 1) :
    0 < tremble k q ∧ tremble k q < 1 := by
  have he : 0 < 1 / ((k : ℝ)+1) := by positivity
  have hd : 0 < 1 + 2*(1 / ((k : ℝ)+1)) := by positivity
  constructor
  · exact div_pos (by linarith [hq.1]) hd
  · unfold tremble
    apply (div_lt_one hd).2
    linarith [hq.2]

lemma tremble_tendsto (q : ℝ) : Tendsto (fun k => tremble k q) atTop (𝓝 q) := by
  have he : Tendsto (fun k : ℕ => 1 / ((k : ℝ)+1)) atTop (𝓝 0) :=
    tendsto_one_div_add_atTop_nhds_zero_nat
  have ht := ((tendsto_const_nhds (x := q)).add he).div
    (tendsto_const_nhds.add (tendsto_const_nhds.mul he)) (by norm_num : (1:ℝ)+2*0 ≠ 0)
  change Tendsto (fun k : ℕ => (q + 1 / ((k : ℝ)+1)) / (1 + 2*(1 / ((k : ℝ)+1)))) atTop (𝓝 ((q+0)/(1+2*0))) at ht
  simpa only [add_zero, mul_zero, div_one, tremble] using ht

/-- One sequence works for every observation and state simultaneously. -/
theorem consistent_beliefs_exist {p q : ι → ℝ}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1) :
    ∃ qs : ℕ → ι → ℝ,
      (∀ k i, 0 < qs k i ∧ qs k i < 1) ∧
      (∀ i, Tendsto (fun k => qs k i) atTop (𝓝 (q i))) ∧
      (∀ o x, Tendsto (fun k => bayes p (qs k) o x) atTop (𝓝 (belief p q o x))) := by
  refine ⟨fun k i => tremble k (q i), ?_, ?_, ?_⟩
  · exact fun k i => tremble_mixed k (hq i)
  · exact fun i => tremble_tendsto (q i)
  · intro o x
    exact bayes_tendsto hp hq (fun k i => tremble_mixed k (hq i))
      (fun i => tremble_tendsto (q i)) o x

theorem consistent_beliefs_unique {p q : ι → ℝ} {qs : ℕ → ι → ℝ}
    (hp : ∀ i, 0 < p i ∧ p i < 1) (hq : ∀ i, 0 ≤ q i ∧ q i ≤ 1)
    (hm : ∀ k i, 0 < qs k i ∧ qs k i < 1)
    (hs : ∀ i, Tendsto (fun k => qs k i) atTop (𝓝 (q i)))
    (o : ι → Observation) (x : ι → Bool) (b : ℝ)
    (hb : Tendsto (fun k => bayes p (qs k) o x) atTop (𝓝 b)) :
    b = belief p q o x := tendsto_nhds_unique hb (bayes_tendsto hp hq hm hs o x)

end
end Cooperation
