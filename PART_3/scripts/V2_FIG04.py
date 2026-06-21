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

# --- Top: Macro Scale (1 Year, SCADA Temp) ---
# Simulating 365 days of oil temperature with seasonal variation
time_macro = np.linspace(-365, 0, 365)
temp_macro = 60 + 15 * np.sin(2 * np.pi * time_macro / 365) + np.random.normal(0, 1.5, 365)
df_macro = pd.DataFrame({'Time_Days': time_macro, 'SCADA_Temp': temp_macro})
df_macro.to_csv('../DATA/V2_DATA04_Macro.csv', index=False)

# --- Middle: Meso Scale (Last 30 Days, PD Count) ---
# Simulating exponential growth of partial discharge over the last month
time_meso = np.linspace(-30, 0, 100)
pd_meso = 10 * np.exp(0.15 * (time_meso + 30)) + np.random.normal(0, 10, 100)
df_meso = pd.DataFrame({'Time_Days': time_meso, 'PD_Count': pd_meso})
df_meso.to_csv('../DATA/V2_DATA04_Meso.csv', index=False)

# --- Bottom: Micro Scale (Last 30 ms, DFR Waveform) ---
# Simulating a 50Hz sine wave with a massive high-frequency transient at t=-5ms
time_micro = np.linspace(-30, 0, 1000) # milliseconds
base_wave = 100 * np.sin(2 * np.pi * 50 * (time_micro / 1000)) # 50Hz Base
transient = np.zeros_like(time_micro)
transient_idx = time_micro > -5
# High frequency oscillation (e.g. 5kHz ringing) decaying exponentially
transient[transient_idx] = 120 * np.exp(-0.8 * (time_micro[transient_idx] + 5)) * np.sin(2 * np.pi * 5000 * (time_micro[transient_idx] / 1000))
wave_micro = base_wave + transient + np.random.normal(0, 3, 1000)
df_micro = pd.DataFrame({'Time_ms': time_micro, 'Voltage_kV': wave_micro})
df_micro.to_csv('../DATA/V2_DATA04_Micro.csv', index=False)

# --- Plotting ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(3.48, 5.8)) # Single column width

# 1. Macro Plot
ax1.plot(time_macro, temp_macro, color='tab:gray', linewidth=1)
ax1.set_title('Macro Scale: 1 Year SCADA (Slow Drift)', fontsize=8)
ax1.set_ylabel('Temp (\u00b0C)', fontsize=7)
ax1.tick_params(axis='both', labelsize=6)
ax1.axvspan(-30, 0, color='tab:red', alpha=0.1) # Highlight last month
ax1.annotate('Zoom to Meso', xy=(-15, 45), xytext=(-100, 40),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=6)
ax1.grid(True, linestyle='--', alpha=0.3)

# 2. Meso Plot
ax2.plot(time_meso, pd_meso, color='tab:blue', linewidth=1.2)
ax2.set_title('Meso Scale: Last 30 Days PD (Exponential Burst)', fontsize=8)
ax2.set_ylabel('PD Intensity (pC)', fontsize=7)
ax2.tick_params(axis='both', labelsize=6)
ax2.axvspan(-0.5, 0, color='tab:red', alpha=0.2) # Highlight last moments
ax2.annotate('Zoom to Micro', xy=(-0.25, 400), xytext=(-15, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=6)
ax2.grid(True, linestyle='--', alpha=0.3)

# 3. Micro Plot
ax3.plot(time_micro, wave_micro, color='black', linewidth=0.8)
ax3.set_title('Micro Scale: Last 30 ms DFR (Algorithmic Autopsy)', fontsize=8)
ax3.set_xlabel('Time to Failure', fontsize=7)
ax3.set_ylabel('Voltage (kV)', fontsize=7)
ax3.tick_params(axis='both', labelsize=6)
# Highlight the transient
ax3.annotate('HF Transient\n(Black Swan)', xy=(-4, 150), xytext=(-20, 180),
             arrowprops=dict(facecolor='tab:red', arrowstyle='->', color='tab:red'), 
             fontsize=7, color='tab:red', fontweight='bold')
ax3.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('../figures/V2_FIG04.pdf')
plt.savefig('../figures/V2_FIG04.svg')
plt.close()
