import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 🔄 LOVE-OS RESYNC ENGINE
# ==========================================

def simulate_resync(initial_delta_theta, R_total, method="standard"):
    """
    Simulates the phase synchronization process over time.
    initial_delta_theta: Initial phase difference (degrees)
    R_total: Sum of resistance (R_A + R_B)
    method: 'force' (Argue) vs 'love-os' (Drop R -> Sync)
    """
    dt = 0.1
    time_steps = np.arange(0, 10, dt)
    theta = initial_delta_theta
    history = []
    energy_cost = 0.0
    
    # Parameters
    natural_pull = 5.0 # How strong the connection is naturally
    
    for t in time_steps:
        # 1. Determine Intervention Force based on Method
        if method == "force":
            # Forceful sync: High effort, fights against R
            # Efficiency drops as R increases
            force = 20.0 / (R_total + 0.1) 
            current_cost = force * R_total # High R = High Burnout
            
        elif method == "love-os":
            # Protocol: 
            # Step 1: Silence (t < 3) -> Drop R effectively to 0
            # Step 2: Gentle Sync (t >= 3) -> High efficiency
            if t < 3.0:
                effective_R = 0.0 # Virtual R is 0 during Silence
                force = 0.0       # No forcing
                current_cost = 0.0 # No cost
                # Natural pull works better in silence? (Let's assume weak pull)
                theta -= (natural_pull * 0.2) * dt 
            else:
                effective_R = 0.1 # R is lowered
                force = 15.0      # Gentle push
                current_cost = force * effective_R
                theta -= force * dt

        # 2. Update Phase (Physics)
        # Apply force to reduce theta
        if method == "force":
            theta -= force * dt
        
        # Add noise/drift
        theta += np.random.normal(0, 0.5) 
        
        # Clamp theta
        if theta < 0: theta = 0
            
        history.append(theta)
        energy_cost += current_cost * dt

    return time_steps, history, energy_cost

# ==========================================
# 🧪 EXPERIMENT: The Cost of Synchronization
# ==========================================

# Scenario: Phase is drifted to 90 degrees (Disconnect)
# Condition: High Stress (R_total = 3.0)

# Method A: "We need to talk!" (Force)
t1, h1, cost1 = simulate_resync(90.0, R_total=3.0, method="force")

# Method B: "Silent Hug & Wait" (Love-OS Protocol)
t2, h2, cost2 = simulate_resync(90.0, R_total=3.0, method="love-os")

# Visualization
plt.figure(figsize=(10, 5))

plt.plot(t1, h1, label=f"Method A: Force Talk (Cost={cost1:.0f})", color='red', linestyle='--')
plt.plot(t2, h2, label=f"Method B: Love-OS Protocol (Cost={cost2:.0f})", color='blue', linewidth=3)

plt.axhline(0, color='black', linewidth=1, linestyle=':')
plt.title("Resynchronization Dynamics: Force vs Protocol", fontsize=14)
plt.ylabel("Phase Difference (Degrees)")
plt.xlabel("Time (Arbitrary Units)")
plt.legend()
plt.grid(True, alpha=0.3)

# Add Annotation
plt.text(1.0, 40, "Silence Phase\n(R dropping...)", color='blue', fontsize=10)
plt.text(4.0, 10, "Sync Phase\n(Fast Convergence)", color='blue', fontsize=10)

plt.show()

print(f"--- RESYNC REPORT ---")
print(f"Method A (Force): Energy Cost = {cost1:.0f} | Final Delta = {h1[-1]:.1f}°")
print(f"Method B (Love-OS): Energy Cost = {cost2:.0f} | Final Delta = {h2[-1]:.1f}°")
print(f"CONCLUSION: Love-OS is {cost1/cost2:.1f}x more efficient.")
