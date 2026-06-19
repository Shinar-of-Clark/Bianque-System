import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

# Directories
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
fig_dir = os.path.join(base_dir, 'figures')
data_dir = os.path.join(base_dir, 'DATA')

os.makedirs(fig_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)

# 1. Generate data
# (a) Error Funnel
t_P = 15.0 # P point at year 15 (Realistic for AIS/GIS)
t_F = 25.0 # True F point at year 25
P_F_interval = t_F - t_P
deciles = np.linspace(t_P, t_F, 11)[:-1] # 0 to 9th decile
true_RUL = t_F - deciles

# Funnel boundaries
# Starts very wide, narrows down exponentially
funnel_upper = true_RUL + 5.0 * np.exp(-0.4 * (deciles - t_P))
funnel_lower = true_RUL - 3.0 * np.exp(-0.4 * (deciles - t_P))

# Continuous line for plotting the funnel
t_continuous = np.linspace(t_P, t_F, 100)
true_RUL_cont = t_F - t_continuous
funnel_upper_cont = true_RUL_cont + 5.0 * np.exp(-0.4 * (t_continuous - t_P))
funnel_lower_cont = true_RUL_cont - 3.0 * np.exp(-0.4 * (t_continuous - t_P))

# (b) Optimal Stopping
tau = np.linspace(10, 30, 200)
Cp = 100
Cu = 500
# Weibull survival function with alpha=28, beta=12
alpha = 28
beta = 12
S_tau = np.exp(- (tau/alpha)**beta)
F_tau = 1 - S_tau
expected_time = np.array([np.trapz(np.exp(-(np.linspace(0, t, 100)/alpha)**beta), np.linspace(0, t, 100)) for t in tau])

cost_preventive = Cp * S_tau / expected_time
cost_penalty = Cu * F_tau / expected_time
total_cost = cost_preventive + cost_penalty
optimal_idx = np.argmin(total_cost)
tau_star = tau[optimal_idx]
min_cost = total_cost[optimal_idx]

# Save data
df = pd.DataFrame({
    'tau': tau,
    'S_tau': S_tau,
    'total_cost': total_cost
})
df.to_csv(os.path.join(data_dir, 'V2_DATA05.csv'), index=False)

# 2. Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.14, 4.0))

# Subplot (a)
ax1.plot(t_continuous, true_RUL_cont, color='darkblue', linewidth=2, label='True RUL')
ax1.fill_between(t_continuous, funnel_lower_cont, funnel_upper_cont, color='lightblue', alpha=0.5, label='95% Confidence Interval')
ax1.scatter(deciles, true_RUL, color='red', zorder=5, label='Decile Calibration Points')
ax1.set_xlabel('Operation Time (Years)')
ax1.set_ylabel('Remaining Useful Life (Years)')
ax1.set_xlim(10, 30)
ax1.set_title('(a) 10-Decile Bayesian Error Funnel')
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=1)
ax1.grid(True, linestyle='--', alpha=0.5)

# Subplot (b)
ax2.plot(tau, cost_preventive, color='green', linestyle='--', label=r'Expected Preventive Cost ($C_p$)')
ax2.plot(tau, cost_penalty, color='red', linestyle='--', label=r'Expected Penalty Cost ($C_u$)')
ax2.plot(tau, total_cost, color='black', linewidth=2, label=r'Total Expected Cost $C(\tau)$')
ax2.scatter([tau_star], [min_cost], color='gold', marker='*', s=200, zorder=5, edgecolors='black', label='Optimal Stopping Point $\\tau^*$')
ax2.set_xlabel('Replacement Time $\\tau$ (Years)')
ax2.set_ylabel('Cost per Unit Time')
ax2.set_xlim(10, 30)
ax2.set_title('(b) Age Replacement Optimal Cost Curve')
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=1)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
fig.subplots_adjust(bottom=0.35)
plt.savefig(os.path.join(fig_dir, 'V2_FIG05.pdf'), bbox_inches='tight')
plt.savefig(os.path.join(fig_dir, 'V2_FIG05.svg'), bbox_inches='tight')
