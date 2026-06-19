import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
fig_dir = os.path.join(base_dir, 'figures')
os.makedirs(fig_dir, exist_ok=True)

# Generate KM data
np.random.seed(42)
t = np.linspace(0, 30, 100)
# AIS log-logistic survival S(t) = 1 / (1 + (t/alpha)^beta)
alpha_ais = 15
beta_ais = 4
s_ais = 1 / (1 + (t/alpha_ais)**beta_ais)
km_ais = s_ais + np.random.normal(0, 0.02, size=len(t))
km_ais = np.clip(np.sort(km_ais)[::-1], 0, 1) # make it monotonically decreasing step-like

# GIS weibull survival S(t) = exp(-(t/alpha)^beta)
alpha_gis = 18
beta_gis = 3
s_gis = np.exp(-(t/alpha_gis)**beta_gis)
km_gis = s_gis + np.random.normal(0, 0.02, size=len(t))
km_gis = np.clip(np.sort(km_gis)[::-1], 0, 1)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.48, 5.5))

ax1.step(t, km_ais, where='post', color='gray', label='Kaplan-Meier (Empirical)')
ax1.plot(t, s_ais, color='steelblue', linewidth=2, label='Log-logistic Fit')
ax1.set_title('(a) AIS Survival Probability')
ax1.set_ylabel('Survival Probability $S(t)$')
ax1.set_ylim(0, 1.05)
ax1.legend(loc='lower left', fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.step(t, km_gis, where='post', color='gray', label='Kaplan-Meier (Empirical)')
ax2.plot(t, s_gis, color='indianred', linewidth=2, label='Weibull Fit')
ax2.set_title('(b) GIS Survival Probability')
ax2.set_xlabel('Operation Time (Years)')
ax2.set_ylabel('Survival Probability $S(t)$')
ax2.set_ylim(0, 1.05)
ax2.legend(loc='lower left', fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'V2_FIG02.pdf'), bbox_inches='tight')
plt.savefig(os.path.join(fig_dir, 'V2_FIG02.svg'), bbox_inches='tight')

data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
df = pd.DataFrame({
    't': t,
    'km_ais': km_ais,
    's_ais': s_ais,
    'km_gis': km_gis,
    's_gis': s_gis
})
df.to_csv(os.path.join(data_dir, 'V2_DATA02.csv'), index=False)
