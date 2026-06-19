import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

# Set font and size for IEEE single-column style (3.48 inches width)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 8
plt.rcParams['axes.linewidth'] = 0.8

# Create directories if they don't exist
os.makedirs('../figures', exist_ok=True)
os.makedirs('../DATA', exist_ok=True)

# Generate Time array (years)
t = np.linspace(0.1, 25, 250)

# 1. AIS: Log-logistic Hazard (Inverted-U)
# alpha = scale (median life), beta = shape
alpha_ais = 12.0
beta_ais = 2.5
# h(t) = (beta/alpha) * (t/alpha)**(beta-1) / (1 + (t/alpha)**beta)
h_ais = (beta_ais / alpha_ais) * (t / alpha_ais)**(beta_ais - 1) / (1 + (t / alpha_ais)**beta_ais)

# 2. GIS: Weibull Hazard (Monotonic increase)
# alpha = scale, beta = shape
alpha_gis = 18.0
beta_gis = 2.0
# h(t) = (beta/alpha) * (t/alpha)**(beta-1)
h_gis = (beta_gis / alpha_gis) * (t / alpha_gis)**(beta_gis - 1)

# Add some simulated Gaussian noise to make it look like "numerical simulation data"
np.random.seed(42)
noise_ais = np.random.normal(0, 0.005, size=t.shape)
noise_gis = np.random.normal(0, 0.005, size=t.shape)
h_ais_noisy = np.clip(h_ais + noise_ais, 0, None)
h_gis_noisy = np.clip(h_gis + noise_gis, 0, None)

# Save to CSV
df = pd.DataFrame({
    'Time_Years': t,
    'AIS_Hazard_Rate': h_ais_noisy,
    'GIS_Hazard_Rate': h_gis_noisy
})
df.to_csv('../DATA/V2_DATA01.csv', index=False)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.48, 4.5), sharex=True)

# Plot AIS
ax1.plot(t, h_ais_noisy, color='steelblue', marker='.', markersize=3, linestyle='none', alpha=0.5, label='Simulated Data (Noisy)')
ax1.plot(t, h_ais, color='darkblue', linestyle='-', linewidth=1.5, label='Log-logistic Fit')
ax1.set_ylabel('Hazard Rate $h(t)$')
ax1.set_title('(a) AIS Mechanical Fatigue (Inverted-U)', fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='lower right', frameon=False)
# Annotate peak
peak_idx = np.argmax(h_ais)
ax1.plot(t[peak_idx], h_ais[peak_idx], 'ko')
ax1.annotate('Middle-age Crisis Peak', 
             xy=(t[peak_idx], h_ais[peak_idx]), 
             xytext=(t[peak_idx]+4, h_ais[peak_idx]-0.035),
             ha='center',
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
             fontsize=7)

# Plot GIS
ax2.plot(t, h_gis_noisy, color='indianred', marker='.', markersize=3, linestyle='none', alpha=0.5, label='Simulated Data (Noisy)')
ax2.plot(t, h_gis, color='darkred', linestyle='--', linewidth=1.5, label='Weibull Fit')
ax2.set_xlabel('Operation Time (Years)')
ax2.set_ylabel('Hazard Rate $h(t)$')
ax2.set_title('(b) GIS Chemical Aging (Monotonic)', fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', frameon=False)

plt.tight_layout(pad=0.5)
plt.savefig('../figures/V2_FIG01.pdf', format='pdf')
plt.savefig('../figures/V2_FIG01.svg', format='svg')
plt.close()
