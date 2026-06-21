import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Font setup
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.unicode_minus'] = False

# Ensure directories exist
os.makedirs('../DATA', exist_ok=True)
os.makedirs('../figures', exist_ok=True)

np.random.seed(42)

# Simulate Bayesian Updating Funnel for RUL (Remaining Useful Life)
x = np.linspace(5, 20, 500)

# 1. Prior Distribution (from Six-Mirror initial competition) - High Uncertainty
prior_mean = 14.0
prior_std = 3.5
prior_pdf = stats.norm.pdf(x, prior_mean, prior_std)

# 2. Intermediate Update (Outer loop incorporating new DGA/SCADA slices)
inter_mean = 12.5
inter_std = 1.8
inter_pdf = stats.norm.pdf(x, inter_mean, inter_std)

# 3. Final Posterior Distribution (The tip of the Bayesian Funnel) - Low Uncertainty
post_mean = 11.8
post_std = 0.75  # Increased std to lower the peak
post_pdf = stats.norm.pdf(x, post_mean, post_std)

# Save DATA
df = pd.DataFrame({
    'RUL_Years': x,
    'Prior_PDF': prior_pdf,
    'Intermediate_PDF': inter_pdf,
    'Posterior_PDF': post_pdf
})
df.to_csv('../DATA/V2_DATA03_Bayesian.csv', index=False)

# --- Plotting ---
# Using single column format (3.48 inches)
fig, ax = plt.subplots(figsize=(3.48, 3.5))

ax.plot(x, prior_pdf, color='tab:gray', linestyle=':', linewidth=2, label='Initial Prior (Wide Variance)')
ax.plot(x, inter_pdf, color='tab:blue', linestyle='--', linewidth=2, label='1st Update (Partial Conv.)')
ax.plot(x, post_pdf, color='tab:red', linestyle='-', linewidth=2.5, label='Final Posterior (Funnel Tip)')

# Fill the posterior to emphasize the convergence
ax.fill_between(x, 0, post_pdf, color='tab:red', alpha=0.2)

# Annotations
ax.axvline(post_mean, color='black', linestyle='-.', alpha=0.5)
ax.annotate('Economic RUL\nTrigger Point', xy=(post_mean, 0.5), xytext=(6, 0.45),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=7)

ax.set_xlabel('Predicted Remaining Useful Life (Years)', fontsize=8)
ax.set_ylabel('Probability Density Function (PDF)', fontsize=8)
ax.set_title('Bayesian Nested Monte Carlo Convergence Funnel', fontsize=9)
ax.legend(loc='upper right', fontsize=7)
ax.tick_params(axis='both', labelsize=7)
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_ylim(0, 0.8)

plt.tight_layout()
plt.savefig('../figures/V2_FIG03.pdf')
plt.savefig('../figures/V2_FIG03.svg')
plt.close()
