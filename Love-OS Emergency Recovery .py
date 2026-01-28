"""
Love-OS Recovery Engine (v1.0)
------------------------------
Calculates the optimal path to restore Binding Energy (k).
Includes 'V-Check' safety lock for the operator.
"""

def execute_recovery(person_A, person_B, current_k, max_k):
    print("--- 🚑 INITIATING RECOVERY PROTOCOL ---")
    
    # 0. Safety Check (The Missing Link)
    if person_A['V'] < 3.0:
        return "CRITICAL WARNING: Operator V is too low. ABORT. Recharge Self first."
    
    recovery_steps = []
    current_efficiency = current_k / max_k
    
    # 1. Phase Check (Priority 1)
    if person_A['theta'] != person_B['theta']: # Simply checking drift
        recovery_steps.append(f"[5 min] PHASE SYNC: Breathe together. Target Delta < 25°.")
    
    # 2. Resistance Check (Priority 2)
    if person_B['R'] > 1.12:
        recovery_steps.append(f"[15 min] R-DROP: Active Listening (NVC). Reduce R_B to 1.0.")
        
    # 3. Resonance Check (Priority 3)
    # Assuming rho needs boost if efficiency is still low after steps 1 & 2
    if current_efficiency < 0.9:
        recovery_steps.append(f"[45 min] RESONANCE: Quality Time (No Phones). Boost rho to 1.0.")
        
    if not recovery_steps:
        return "System Stable. No action required."
        
    return "\n".join(recovery_steps)

# --- Test Run ---
# Case: A is tired (V=2), B is stressed (R=1.6), Phase is drifting
User_A = {'L': 10, 'V': 2, 'R': 0, 'theta': 120} # V is low!
Partner_B = {'L': 8, 'V': 8, 'R': 1.6, 'theta': 210} # Out of sync
Current_K = 60000 
Max_K = 128000

print(execute_recovery(User_A, Partner_B, Current_K, Max_K))
