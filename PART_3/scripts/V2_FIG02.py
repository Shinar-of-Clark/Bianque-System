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

np.random.seed(42)

# --- Subplot 1: Chronic Phase (THD and Delta T) ---
time_chronic = np.linspace(0, 15, 800)

# Simulate THD (stray load stress) - mostly stable with a sudden regime shift at year 5
thd = np.ones_like(time_chronic) * 0.02 + np.random.normal(0, 0.002, len(time_chronic))
thd[time_chronic > 5] += 0.03 # step increase in harmonic stress

# Simulate Delta T (Thermal fatigue)
# Delta T diverges gradually due to THD stress accumulation
delta_T = 1.0 + 0.05 * time_chronic + np.cumsum(thd) * 0.015 + np.random.normal(0, 0.02, len(time_chronic))

# --- Subplot 2: Acute Phase (PD Exponential Growth) ---
time_acute = np.linspace(10, 15, 400)
# PD stays near zero until P-point, then exponential
p_point_time = 11.5
pd_intensity = np.zeros_like(time_acute)
for i, t in enumerate(time_acute):
    if t > p_point_time:
        pd_intensity[i] = 10 * np.exp(1.8 * (t - p_point_time)) + np.random.normal(0, 15)
    else:
        pd_intensity[i] = np.random.normal(5, 2)

# Save DATA
df_chronic = pd.DataFrame({'Time_Years': time_chronic, 'THD': thd, 'Delta_T': delta_T})
df_chronic.to_csv('../DATA/V2_DATA02_Chronic.csv', index=False)
df_acute = pd.DataFrame({'Time_Years': time_acute, 'PD_Intensity': pd_intensity})
df_acute.to_csv('../DATA/V2_DATA02_Acute.csv', index=False)

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.48, 5.5), sharex=False)

# Top Subplot
color1 = 'tab:red'
ax1.set_ylabel('Norm. $\\Delta T$ (-)', color=color1, fontsize=8)
ax1.plot(time_chronic, delta_T, color=color1, linewidth=1.5)
ax1.tick_params(axis='y', labelcolor=color1, labelsize=7)
ax1.tick_params(axis='x', labelsize=7)

ax1_2 = ax1.twinx()
color2 = 'tab:blue'
ax1_2.set_ylabel('THD Stress', color=color2, fontsize=8)
ax1_2.plot(time_chronic, thd, color=color2, alpha=0.5)
ax1_2.tick_params(axis='y', labelcolor=color2, labelsize=7)

ax1.axvline(5, color='gray', linestyle=':', alpha=0.6)
ax1.annotate('THD Shift', xy=(5.2, 1.2), fontsize=7, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.8))

ax1.set_title('Chronic Phase: THD inducing $\\Delta T$', fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.3)

# Bottom Subplot
ax2.plot(time_acute, pd_intensity, color='black', linewidth=1.5, label='PD Intensity')
ax2.axvline(p_point_time, color='orange', linestyle='--', linewidth=1.5, label='P-Point')

f_point_time = 14.8
f_point_pd = 10 * np.exp(1.8 * (f_point_time - p_point_time))
ax2.axvline(f_point_time, color='red', linestyle='-', linewidth=1.5, label='F-Point')

# Bayesian Funnel annotation
ax2.axvspan(p_point_time, f_point_time, color='orange', alpha=0.1)
ax2.annotate('Bayesian\nFunnel', xy=(12.5, 2000), fontsize=7)

ax2.set_xlabel('Operational Time (Years)', fontsize=8)
ax2.set_ylabel('PD Intensity (pC)', fontsize=8)
ax2.set_title('Acute Phase: PD Exponential Growth', fontsize=9)
ax2.legend(loc='upper left', fontsize=7)
ax2.tick_params(axis='both', labelsize=7)
ax2.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('../figures/V2_FIG02.pdf')
plt.savefig('../figures/V2_FIG02.svg')
plt.close()
