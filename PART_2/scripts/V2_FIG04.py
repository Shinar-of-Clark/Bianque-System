import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
fig_dir = os.path.join(base_dir, 'figures')

np.random.seed(42)
t = np.linspace(0, 20, 300)
# Degradation: SF6 pressure drops
# normal = 0.6 MPa, P point = 0.55 MPa, F point = 0.5 MPa
pressure = 0.6 - 0.0005 * t**2
noise = np.random.normal(0, 0.005, size=len(t))
sensor_data = pressure + noise

fig, ax = plt.subplots(figsize=(3.48, 3.5))

ax.scatter(t, sensor_data, color='lightgray', s=10, alpha=0.7, label='Raw Sensor Data')
ax.plot(t, pressure, color='darkred', linewidth=2, label='Degradation Trend')

ax.axhline(0.6, color='green', linestyle='--', linewidth=1, label='Healthy Baseline')
ax.axhline(0.55, color='orange', linestyle='--', linewidth=1.5, label='P-Point (Alert)')
ax.axhline(0.5, color='red', linestyle='-', linewidth=2, label='F-Point (Failure)')

# Find P and F time
t_P = t[np.argmin(np.abs(pressure - 0.55))]
t_F = t[np.argmin(np.abs(pressure - 0.5))]

ax.axvline(t_P, color='orange', linestyle=':', alpha=0.8)

# 10 deciles
deciles = np.linspace(0.55, 0.5, 11)

# Deciles 1-8 (Economic checkpoints)
for d in deciles[1:9]:
    t_d = t[np.argmin(np.abs(pressure - d))]
    ax.axvline(t_d, color='blue', linestyle=':', alpha=0.3)

# Decile 9 (Forced schedule warning)
d_9 = deciles[9]
t_9 = t[np.argmin(np.abs(pressure - d_9))]
ax.axvline(t_9, color='red', linestyle=':', alpha=0.8)

# Add Annotations for the 3 core points
ax.annotate('P-Point', xy=(t_P, 0.55), xytext=(t_P, 0.585),
            arrowprops=dict(facecolor='orange', edgecolor='none', shrink=0, width=1.5, headwidth=6),
            fontsize=9, fontweight='bold', color='darkorange', ha='center')

ax.annotate('9th-Warning', xy=(t_9, d_9), xytext=(t_9, d_9 + 0.035),
            arrowprops=dict(facecolor='red', edgecolor='none', shrink=0, width=1.5, headwidth=6),
            fontsize=9, fontweight='bold', color='red', ha='center')

ax.annotate('F-Point', xy=(t_F, 0.5), xytext=(t_F, 0.485),
            arrowprops=dict(facecolor='darkred', edgecolor='none', shrink=0, width=1.5, headwidth=6),
            fontsize=9, fontweight='bold', color='darkred', ha='center', va='top')

ax.set_xlabel('Operation Time (Years)')
ax.set_ylabel('SF6 Gas Pressure (MPa)')
ax.set_xlim(0, 16)
ax.set_ylim(0.48, 0.62)
ax.legend(loc='lower left', fontsize=7)
ax.set_title('P-F Interval & 10-Decile Partition')
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'V2_FIG04.pdf'), bbox_inches='tight')
plt.savefig(os.path.join(fig_dir, 'V2_FIG04.svg'), bbox_inches='tight')

data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
df = pd.DataFrame({
    't': t,
    'pressure': pressure,
    'sensor_data': sensor_data
})
df.to_csv(os.path.join(data_dir, 'V2_DATA04.csv'), index=False)
