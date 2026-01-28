# 🔄 Love-OS Resync Protocol (Recovery Engine)

[![Module](https://img.shields.io/badge/Module-Resync_Simulator-orange)]()
[![Physics](https://img.shields.io/badge/Dynamics-Nonlinear_Control-blue)]()

> **"Relationships do not persist because they are strong ($k$). They persist because they have a structure to resync when broken."**

## 💡 Overview

In any dynamic N-body system, Phase Drift ($\Delta\theta \neq 0$) is inevitable due to entropy (stress, fatigue, life changes).
The **Resync Simulator** models the metabolic cost of relationship repair. It proves mathematically why "Silence" and "Waiting" are not passive acts, but **optimal engineering strategies** to minimize energy loss during conflict.

## 📐 The Governing Dynamics

We model the Phase Difference $\Delta\theta(t)$ as a driven damped oscillator.

### 1. The State Equation
The evolution of the gap between two people is defined by:

$$
\frac{d(\Delta\theta)}{dt} = \underbrace{\omega_{drift}}_{\text{Entropy}} - \underbrace{\lambda \sin(\Delta\theta)}_{\text{Natural Pull}} - \underbrace{\frac{\text{Force}(t)}{R(t)}}_{\text{Intervention}}
$$

- **Drift:** Natural tendency to grow apart.
- **Natural Pull:** The gravity of the relationship trying to self-correct.
- **Intervention:** Conscious effort to fix the gap. Note that effectiveness is inversely proportional to Resistance ($R$).

### 2. The Cost Function (Why fighting fails)
The energy required to fix a relationship ($E_{sync}$) is:

$$
E_{sync} = \int_{t_0}^{t_1} \text{Effort}(t) \cdot R(t) \, dt
$$

If Resistance ($R$) is high (e.g., during an argument), the energy cost explodes to infinity.
**Conclusion:** You cannot sync phase while $R$ is high.

## 🧪 Simulation Scenarios

This script (`resync_simulator.py`) compares two recovery strategies:

### Method A: The "Ego" Approach (Force)
- **Logic:** "We need to talk and fix this NOW."
- **Physics:** Applies force while $R$ is high.
- **Result:** High energy burnout, oscillations, slow convergence.

### Method B: The Love-OS Protocol (Silence First)
- **Logic:** "Drop Resistance first, Sync second."
- **Physics:** 1.  **Phase 1 (Cooling):** Apply 0 force. Allow $R$ to decay (Silence/Space).
    2.  **Phase 2 (Entrainment):** Apply gentle force once $R \approx 0$.
- **Result:** Minimal energy cost, instant phase lock (vertical convergence).

## 🚀 Usage

```bash
python resync_simulator.py
