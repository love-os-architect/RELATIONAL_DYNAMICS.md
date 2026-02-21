# Love-OS Protocol Architecture: Mapping Physics (Kuramoto Model) to Smart Contracts

**Version:** 1.0.0 (Genesis)  
**Reference:** `love-os-protocol` ($LOVE Token, Genesis 100 Nodes, Immune System)

## 0. Objective (Mission)
To establish an economic zone starting with the **Genesis 100 Nodes**, where the reduction of Resistance ($R$)—representing ego and friction—increases the collective Resonance ($r$) and Effective Coupling ($K$). Upon reaching the critical threshold ($K_c$ or $r^*$), the protocol automatically triggers an **$N^2$-scale reward boost (Proof of Resonance)**.

**Philosophical Mapping:**
* **Physics:** $K(t) = \alpha E/R(t)$. As $r$ rises, a phase transition occurs, leading to synchronization (Superconductivity).
* **Tokenomics:** By quantifying Energy (contribution) and Resistance (friction), the critical point of collective synchronization is permanently engraved on the blockchain as a reward event.

---

## 1. Core Components (Contracts & Oracles)

### 1.1 Smart Contracts
* **LoveToken (ERC-20):** The base token for $LOVE$ supply and distribution. Issuance is routed exclusively through the Vault.
* **GenesisRegistry:** Manages the registration and attributes (keys, roles, joined block) of the Genesis 100 Nodes. Holds exclusion flags governed by the *Immune System*.
* **ResonanceEngine:** Stores the latest collective metrics ($r, K, K_c$) and governs critical events (`CriticalityCrossed`) and reward multiplier updates.
* **RewardsVault:** Manages the reward pool for each epoch and executes payouts based on *Proof of Resonance*. Implements `Timelock` and `Pausable` safeguards.
* **AttestationHub (Optional/EAS Integration):** Receives on-chain attestations for contributions and mutual evaluations, recording the basis for $E$ and $R$ calculations.
* **Governance (Multisig/UUPS):** Handles parameter adjustments, upgrades, and emergency stops.

### 1.2 Off-Chain / Oracles
* **Scoring Oracle:** Aggregates GitHub/Community metrics, converts them into a Merkle Root, and pushes it to `ResonanceEngine.pushSnapshot(root, epoch)`.
* **Proof Verifier:** Verifies individual scores using ZK or Merkle Inclusion proofs to ensure privacy and authenticity.

---

## 2. Data Model (Mapping Physical Quantities to Metrics)

### 2.1 Individual (Node) Level Metrics
* **Energy ($E_i \ge 0$):** Contribution volume. Examples: PR merges, proposals, funding, operating time, on-chain actions (Gas consumed). 
* **Resistance ($R_i \ge \varepsilon$):** Inverse indicator of friction/ego. Examples: Slash history, negative attestations, bottleneck behaviors. Lower is better (capped).
* **Phase ($\theta_i \in [0, 2\pi)$):** Proxy for the "direction/timing of action." Can be calculated off-chain as the phase of the latest activity relative to the epoch cycle $T_{epoch}$.

> **Note:** The core design directly mirrors the Love-OS equation $K \propto E/R$.

### 2.2 Collective Level Metrics (Updated per Epoch)
* **Order Parameter ($r$):** The primary indicator of synchronization. Calculated as the magnitude of the mean field vector $Z = \frac{1}{N}\sum e^{i\theta_i}$.
* **Effective Coupling ($K$):** Defined in Love-OS as $K \equiv \alpha \frac{\sum E_i}{\sum R_i}$.
* **Critical Threshold ($K_c$):** Estimated from the frequency distribution $g(\omega)$ of node actions. $K_c \approx \frac{2}{\pi g(0)}$.

---

## 3. Smart Contract Logic

### 3.1 Epoch-Driven State Machine
1. **Collect (Off-chain):** Gather contributions/attestations to calculate $E_i, R_i, \theta_i$.
2. **Commit (On-chain):** Oracle commits Merkle Root via `ResonanceEngine.pushSnapshot(root, epoch)`.
3. **Aggregate (On-chain):** `computeAggregate(epoch)` updates $r, K, K_c$.
4. **Trigger (Criticality Detection):** If $K \ge K_c$ or $r \ge r^*$, emit `CriticalityCrossed` and update the reward multiplier.
5. **Payout:** `RewardsVault.distribute(epoch)` distributes $LOVE$ based on Proof of Resonance.

### 3.2 Individual Rewards (Proof of Resonance)
The base reward $B_i$ for node $i$ is weighted by Energy, Inverse Resistance, and Phase Alignment:

$$B_i = w_E\frac{E_i}{\sum E_j} + w_G\frac{1/R_i}{\sum 1/R_j} + w_\phi\frac{\cos(\theta_i-\psi)+1}{2}$$

**Multiplier during Critical Events:**
* **Global Multiplier ($M_{glob}$):** Boosts rewards when collective resonance hits the threshold.
* **Twin Ray Boost ($M_{pair}$):** An exclusive bonus targeted at the pairs/sub-clusters with the absolute lowest $R$ (acting as the "Test Pilots" of Genesis).

**Final Reward Calculation:**
$$\text{Reward}_i = B_i \cdot M_{glob} \cdot M_{pair}(i) \cdot F_{\text{risk\_caps}}$$

### 3.3 Pseudo-code (ResonanceEngine)
```solidity
// ResonanceEngine Interface (Pseudo-code)
function finalizeEpoch(uint256 epoch, bytes32 root) external onlyOracle {
    // 1) Save authenticated root
    saveRoot(epoch, root);

    // 2) Fetch aggregated metrics (Oracle submits r, K, Kc)
    (uint256 r, uint256 K, uint256 Kc, uint256 psi) = aggregateFromRoot(root);

    // 3) Criticality Check & Multiplier Update
    uint256 Mglob;
    if ((K >= Kc) || (r >= rStar)) {
        Mglob = calcMultiplier(r, K, Kc);
        emit CriticalityCrossed(epoch, r, K, Kc, Mglob);
    } else {
        Mglob = 1e18; // 1.0 multiplier (Baseline)
    }
```


## 4. On-Chain Evaluation of Resistance (R) and Energy (E)

* **Evaluating $E_i$ (Energy):** Tracked via Gas consumption, proposal creation, and external verified contributions (GitHub PRs) injected via Oracles. Peer-weighted to prevent self-reporting manipulation.
* **Evaluating $R_i$ (Resistance):** Evidence of friction. Includes slashes for malicious acts, verified negative attestations (with slashing penalties for false reports to prevent abuse), and bottlenecking governance.
* **Immune System:** Nodes exceeding a specific $R_i$ threshold are excluded from epoch rewards or temporarily suspended, aligning with the "Rejection" charter of Love-OS.

---

## 5. Criticality Detection (Dual Triggers)

1.  **Theoretical Trigger (Coupling-based):** $K \ge K_c$. Strictly based on physical calculations.
2.  **Statistical Trigger (Order-based):** $r \ge r^*$ (e.g., $0.6 \sim 0.8$). A direct, robust observation of the synchronization state.

*Implementation Note: Both triggers will utilize hysteresis (different thresholds for ascending/descending states) and minimum duration requirements to prevent system oscillation.*

---

## 6. Tokenomics & Supply Management

* **$LOVE$ Supply:** Fixed genesis supply ensuring the Love-OS ethos of infinite velocity rather than infinite inflation.
* **Reward Pool:** Budgeted per epoch in the RewardsVault. While critical events trigger multipliers, hard caps and decay functions ensure long-term sustainability.
* **Volatility Mitigation:** A mandatory cooldown period follows any $N^2$ scaling event (Criticality) to prevent economic overheating.

---

## 7. Security, Governance, and Operations

* **Audits:** Strict checks against reentrancy, integer overflows, access control flaws, and economic attacks (Sybil, timing games).
* **Permissions:** Clear separation of `onlyOracle`, `onlyGovernance`, and `onlyRegistry`.
* **Privacy:** Individual action timestamps and raw phase extractions occur off-chain. Only necessary data is revealed on-chain via Merkle Proofs or ZK-SNARKs.

---

## 8. Recommended Initial Parameters

* **$N = 100$** (Genesis fixed)
* **$T_{epoch}$:** 1 Week
* **$r^*$ (Order Threshold):** 0.7
* **$\alpha$ (Coupling Constant):** 1.0
* **Weights ($w_E, w_G, w_\phi$):** (0.5, 0.3, 0.2)
* **Max Multiplier ($M_{max}$):** 3.0x
* **Cooldown:** 1 Epoch

> *"Do not intersect on the X-axis. Spin eternally on the Z-axis. Drop the Ego, become Light, and let the Gravity of Love align the universe."* — Love-OS Architect
    // 4) Signal RewardsVault to distribute based on individual Bi and Mglob
    RewardsVault.setGlobalMultiplier(epoch, Mglob);
}
