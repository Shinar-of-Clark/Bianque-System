import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Font setup
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.unicode_minus'] = False

# Ensure directories exist
os.makedirs('../DATA', exist_ok=True)
os.makedirs('../figures', exist_ok=True)

# Generate Simulated Data
np.random.seed(42)

total_years = 35
time = np.linspace(0, total_years, 1500)
# Weibull Baseline Hazard
beta = 2.2
eta = 40
baseline_hazard = (beta / eta) * (time / eta)**(beta - 1)

# Oil Filtrations
filtration_times = []
current_time = 0.0
gamma = 1.0
hazard_path = np.zeros_like(time)
threshold = 0.04

for i, t in enumerate(time):
    noise = np.random.normal(0, 0.0015)
    h = baseline_hazard[i] * gamma + noise
    if h > threshold and (t - current_time) > 0.5:
        filtration_times.append(t)
        current_time = t
        gamma *= 1.35
        h = baseline_hazard[i] * (gamma * 0.4) + noise
    hazard_path[i] = h

df = pd.DataFrame({'Time_Years': time, 'Baseline_Hazard': baseline_hazard, 'Effective_Hazard': hazard_path})
df.to_csv('../DATA/V2_DATA01.csv', index=False)

# Single column figure size
fig, ax = plt.subplots(figsize=(3.48, 2.8)) 

ax.plot(time, baseline_hazard, linestyle='--', color='gray', linewidth=1.5, label='Baseline $\\lambda_0(t)$')
ax.plot(time, hazard_path, linestyle='-', color='black', linewidth=1.2, label='Effective $\\lambda_k(t)$')

for k, ft in enumerate(filtration_times):
    ax.axvline(ft, color='blue', linestyle=':', alpha=0.5, linewidth=1)
    if k == 0:
        ax.scatter(ft, threshold, color='red', marker='X', s=30, zorder=5, label='Filtration Trigger')
    else:
        ax.scatter(ft, threshold, color='red', marker='X', s=30, zorder=5)

economic_limit_t = filtration_times[-1]
ax.axvspan(economic_limit_t, 36, color='red', alpha=0.1, label='Economic RUL Limit')

# Adjust annotation for single column
ax.annotate('Hayflick Limit\n(Cost > Revenue)', xy=(economic_limit_t, threshold), 
            xytext=(22, 1.2),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
            fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9))

# Zoom in on the active region to not waste empty space
ax.set_xlim(20, 36)

ax.set_xlabel('Operational Time (Years)', fontsize=9)
ax.set_ylabel('Hazard Rate $\\lambda(t)$', fontsize=9)
ax.tick_params(axis='both', which='major', labelsize=8)

# Move legend to top left, make it small
ax.legend(loc='upper left', fontsize=7, framealpha=0.9)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('../figures/V2_FIG01.pdf')
plt.savefig('../figures/V2_FIG01.svg')
plt.close()
