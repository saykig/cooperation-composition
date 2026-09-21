import Receiver

open scoped BigOperators
namespace Cooperation
noncomputable section

abbrev CompletePast {n : ℕ} (h : Info n) : Prop :=
  ∀ j : Fin h.val.length, h.val[j.val] = true

abbrev compatiblePath {n : ℕ} (h : Info n) (a : Bool) (y : Fin n → Bool) : Prop :=
  (∀ j : Fin h.val.length, y ⟨j.val,j.isLt.trans h.property⟩ = h.val[j.val]) ∧
    y ⟨h.val.length,h.property⟩ = a

/-- Likelihood of future actions conditional on the state, past, and forced current action.
Each later sender uses the entire earlier transcript. Type zero can only be silent. -/
def continuationWeight {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x y : Fin n → Bool) : ℝ :=
  if compatiblePath h a y then
    ∏ i : Fin n, if h.val.length < i.val then
      actionProbability (σ (pastInfo (terminalHist y) i)) (x i) (y i) else 1
  else 0

/-- Expected receiver action for a fixed Nature state, enumerating EVERY terminal path. -/
def pathExpectation {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (ρ : (Fin n → Bool) → ℝ) (x : Fin n → Bool) : ℝ :=
  ∑ y : Fin n → Bool, continuationWeight σ h a x y * ρ y

/-- Sender payoff from a forced action, conditional on its positive private bit.
Beliefs here are the unique limits derived from Bayes conditioning in Transcripts. -/
def senderPayoff {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n)
    (ρ : (Fin n → Bool) → ℝ) (η k : ℝ) (a : Bool) : ℝ :=
  η * (∑ x : Fin n → Bool,
    belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h true) x *
      pathExpectation σ h a ρ x) - (if a then k else 0)

theorem path_expectation_complete {n : ℕ} (σ : Strategy n) (h : Info n) (a : Bool)
    (x : Fin n → Bool) :
    pathExpectation σ h a completeRule x = continuationWeight σ h a x (fun _ => true) := by
  classical
  simp [pathExpectation,completeRule]

lemma compatible_complete {n : ℕ} (h : Info n) (a : Bool) :
    compatiblePath h a (fun _ => true) ↔ CompletePast h ∧ a = true := by
  constructor
  · rintro ⟨hh,ha⟩
    exact ⟨fun j => (hh j).symm,ha.symm⟩
  · rintro ⟨hh,ha⟩
    exact ⟨fun j => (hh j).symm,ha.symm⟩

lemma silent_path_zero {n : ℕ} (σ : Strategy n) (h : Info n) (x : Fin n → Bool) :
    pathExpectation σ h false completeRule x = 0 := by
  rw [path_expectation_complete]
  simp [continuationWeight,compatible_complete]

lemma broken_path_zero {n : ℕ} (σ : Strategy n) (h : Info n) (hb : ¬ CompletePast h)
    (a : Bool) (x : Fin n → Bool) :
    pathExpectation σ h a completeRule x = 0 := by
  rw [path_expectation_complete]
  simp [continuationWeight,compatible_complete,hb]

lemma future_private_unseen {n : ℕ} (h : Info n) (i : Fin n) (hi : h.val.length < i.val) :
    privateObserved h true i = .unseen := by
  simp [privateObserved,observed,show i.val ≠ h.val.length by omega,
    show ¬ i.val < h.val.length by omega]

/-- A finite-product integration identity, proved by distributivity over all Nature states.
Coordinates outside the future contribute normalized mass one. -/
theorem future_integration {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n)
    (r : Fin n → ℝ) :
    (∑ x : Fin n → Bool,
      belief p (rateAt σ ⟨h.val,h.property.le⟩) (privateObserved h true) x *
        ∏ i, if h.val.length < i.val then (if x i then r i else 0) else 1) =
      ∏ i, if h.val.length < i.val then p i * r i else 1 := by
  unfold belief nature
  simp_rw [← Finset.prod_mul_distrib]
  rw [← Fintype.prod_sum (fun (i : Fin n) (b : Bool) =>
    bern (posterior (p i) (rateAt σ ⟨h.val,h.property.le⟩ i) (privateObserved h true i)) b *
      (if h.val.length < i.val then (if b then r i else 0) else 1))]
  apply Finset.prod_congr rfl
  intro i _
  by_cases hi : h.val.length < i.val
  · simp [hi,future_private_unseen h i hi,posterior,bern]
  · simp [hi,bern]

/-- This product is obtained only AFTER summing the primitive state/path expectation. -/
theorem sender_gain_complete {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n)
    (hc : CompletePast h) (η k : ℝ) :
    senderPayoff p σ h completeRule η k true - senderPayoff p σ h completeRule η k false =
      η * (∏ i : Fin n, if h.val.length < i.val then
        p i * σ (pastInfo (terminalHist (fun _ => true)) i) else 1) - k := by
  have he (x : Fin n → Bool) :
      pathExpectation σ h true completeRule x =
      ∏ i : Fin n, if h.val.length < i.val then
        (if x i then σ (pastInfo (terminalHist (fun _ => true)) i) else 0) else 1 := by
    rw [path_expectation_complete]
    simp [continuationWeight,compatible_complete,hc,actionProbability]
  simp only [senderPayoff,he,silent_path_zero,mul_zero,Finset.sum_const_zero,
    Bool.false_eq_true,if_false,if_true,sub_zero]
  rw [future_integration]

theorem sender_gain_broken {n : ℕ} (p : Fin n → ℝ) (σ : Strategy n) (h : Info n)
    (hb : ¬ CompletePast h) (η k : ℝ) :
    senderPayoff p σ h completeRule η k true - senderPayoff p σ h completeRule η k false = -k := by
  simp [senderPayoff,broken_path_zero σ h hb]


/-- Strategic bridge: only receiver optimality is assumed, not a stipulated receiver rule
or a sender continuation formula. The belief system was derived in Transcripts. -/
theorem continuation_bridge {n : ℕ} {p : Fin n → ℝ} {σ : Strategy n}
    {A B e : ℝ} (hp : ∀ i, 0 < p i ∧ p i < 1) (hσ : Feasible σ)
    (hA : 0 < A) (hB : 0 < B) (he : 0 ≤ e) (heB : e < B)
    (ht : ∀ i, p i < A/(A+B)) (ρ : (Fin n → Bool) → ℝ)
    (hr : ∀ y, BestReply
      (receiverGain p (rateAt σ (terminalHist y)) (observed (terminalHist y)) A B e) (ρ y))
    (h : Info n) (η k : ℝ) :
    senderPayoff p σ h ρ η k true - senderPayoff p σ h ρ η k false =
      if CompletePast h then
        η * (∏ i : Fin n, if h.val.length < i.val then
          p i * σ (pastInfo (terminalHist (fun _ => true)) i) else 1) - k
      else -k := by
  have hρ : ρ = completeRule := by
    funext y
    exact (terminal_bestReply_below hp hσ hA hB he heB ht y (ρ y)).mp (hr y)
  subst ρ
  split_ifs with hc
  · exact sender_gain_complete p σ h hc η k
  · exact sender_gain_broken p σ h hc η k

/-- Primitive expected payoff under the current sender's mixed action. -/
def mixedPayoff (uR uS a : ℝ) := a*uR + (1-a)*uS

def SenderBestReply (uR uS a : ℝ) : Prop :=
  0 ≤ a ∧ a ≤ 1 ∧ ∀ b : ℝ, 0 ≤ b → b ≤ 1 → mixedPayoff uR uS b ≤ mixedPayoff uR uS a

theorem sender_bestReply_gain (uR uS a : ℝ) :
    SenderBestReply uR uS a ↔ BestReply (uR-uS) a := by
  unfold SenderBestReply BestReply mixedPayoff
  constructor
  · rintro ⟨ha,ha',hb⟩
    refine ⟨ha,ha',?_⟩
    intro b h0 h1
    have := hb b h0 h1
    nlinarith
  · rintro ⟨ha,ha',hb⟩
    refine ⟨ha,ha',?_⟩
    intro b h0 h1
    have := hb b h0 h1
    nlinarith

/-- Strictly negative disclosure gain forces silence even against mixed deviations. -/
theorem sender_strict_silence {uR uS a : ℝ} (hg : uR-uS < 0) :
    SenderBestReply uR uS a ↔ a = 0 := by
  rw [sender_bestReply_gain]
  exact bestReply_negative hg

/-- Strictly positive disclosure gain forces disclosure; zero permits every feasible mixture. -/
theorem sender_strict_report {uR uS a : ℝ} (hg : 0 < uR-uS) :
    SenderBestReply uR uS a ↔ a = 1 := by
  rw [sender_bestReply_gain]
  exact bestReply_positive hg

theorem sender_indifferent {uR uS a : ℝ} (hg : uR-uS = 0) :
    SenderBestReply uR uS a ↔ 0 ≤ a ∧ a ≤ 1 := by
  rw [sender_bestReply_gain,hg,bestReply_zero]

end
end Cooperation
