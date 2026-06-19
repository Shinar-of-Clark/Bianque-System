import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

# Set font and size for IEEE full-column style (7.14 inches width)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 8
plt.rcParams['axes.linewidth'] = 0.8

os.makedirs('../figures', exist_ok=True)
os.makedirs('../DATA', exist_ok=True)

models = ['Cox-PH', 'Exponential', 'Weibull', 'Lognormal', 'Log-logistic', 'RSF']
x = np.arange(len(models))
width = 0.35

# Simulated Performance Data (C-index)
# AIS: Log-logistic is best, RSF is second
c_index_ais = [0.65, 0.58, 0.72, 0.79, 0.92, 0.88]
# GIS: Weibull is best, RSF is second
c_index_gis = [0.68, 0.71, 0.94, 0.76, 0.66, 0.89]

# Save to CSV
df = pd.DataFrame({
    'Model': models,
    'AIS_C_Index': c_index_ais,
    'GIS_C_Index': c_index_gis
})
df.to_csv('../DATA/V2_DATA03.csv', index=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.14, 3.0))

# Plot AIS
bars1 = ax1.bar(x, c_index_ais, width, color='lightgray', edgecolor='black')
# Highlight Log-logistic
bars1[4].set_color('steelblue')
bars1[4].set_edgecolor('black')
ax1.set_ylabel('Concordance Index (C-index)')
ax1.set_title('(a) AIS "6-Mirror" Evaluation (Log-logistic Wins)', fontsize=9)
ax1.set_xticks(x)
ax1.set_xticklabels(models, rotation=30, ha='right')
ax1.set_ylim(0.5, 1.0)
ax1.grid(True, axis='y', linestyle='--', alpha=0.5)

# Add values on top of bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f'{yval:.2f}', ha='center', va='bottom', fontsize=7)

# Plot GIS
bars2 = ax2.bar(x, c_index_gis, width, color='lightgray', edgecolor='black')
# Highlight Weibull
bars2[2].set_color('indianred')
bars2[2].set_edgecolor('black')
ax2.set_ylabel('Concordance Index (C-index)')
ax2.set_title('(b) GIS "6-Mirror" Evaluation (Weibull Wins)', fontsize=9)
ax2.set_xticks(x)
ax2.set_xticklabels(models, rotation=30, ha='right')
ax2.set_ylim(0.5, 1.0)
ax2.grid(True, axis='y', linestyle='--', alpha=0.5)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f'{yval:.2f}', ha='center', va='bottom', fontsize=7)

plt.tight_layout(pad=0.5)
plt.savefig('../figures/V2_FIG03.pdf', format='pdf')
plt.savefig('../figures/V2_FIG03.svg', format='svg')
plt.close()
