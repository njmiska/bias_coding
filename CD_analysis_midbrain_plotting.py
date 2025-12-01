import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_rel

# --- SETUP ---
figures_path = '/Users/natemiska/Documents/Lab_Data/LabMeetingDec2025/CD_analysis'
with open(figures_path + '/CD_population_results.pkl', 'rb') as f:
    pop_data = pickle.load(f)

# Colors
COLOR_CTRL = 'black'
COLOR_OPTO = 'blue'  # Requested Blue

# --- PLOT 1: Grand Average Separation Traces ---
def get_group_stats(data_list, group_name, metric_key_path):
    collected_traces = []
    common_time = data_list[0]['time']
    for session in data_list:
        if session['hemisphere'] != group_name: continue
        val = session
        for k in metric_key_path: val = val[k]
        collected_traces.append(val)
    
    if not collected_traces: return None, None, None
    arr = np.array(collected_traces)
    return common_time, np.nanmean(arr, axis=0), np.nanstd(arr, axis=0)/np.sqrt(arr.shape[0])

def plot_shaded(ax, x, mean, sem, color, label):
    ax.plot(x, mean, color=color, label=label, lw=2)
    ax.fill_between(x, mean-sem, mean+sem, color=color, alpha=0.2)

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
conditions = ['Ipsi', 'Contra']

for i, hemi in enumerate(conditions):
    ax = axes[i]
    time, mu_c, se_c = get_group_stats(pop_data, hemi, ['separation', 'ctrl'])
    _,    mu_o, se_o = get_group_stats(pop_data, hemi, ['separation', 'opto'])
    
    if time is None: continue

    plot_shaded(ax, time, mu_c, se_c, COLOR_CTRL, 'Control')
    plot_shaded(ax, time, mu_o, se_o, COLOR_OPTO, 'SNr Inhibition')
    
    ax.set_title(f"{hemi}lateral SNr Inhibition")
    ax.set_xlabel("Time from Laser Onset (s)")
    ax.axvline(0, color='k', linestyle='--', alpha=0.5)
    ax.axhline(0, color='k', linewidth=0.5)

axes[0].set_ylabel("CD Separation (Block L - Block R)")
axes[0].legend()
plt.tight_layout()
plt.savefig(figures_path + '/GrandAverage_Separation_Blue.png')
plt.show()

# --- PLOT 2: Updated Quantification (Grouped Bars) ---
target_time = 0.5 
long_form_data = []

for session in pop_data:
    t_idx = np.argmin(np.abs(session['time'] - target_time))
    
    # Append TWO rows per session (Long format for Seaborn)
    # Row 1: Control
    long_form_data.append({
        'PID': session['pid'],
        'Hemisphere': session['hemisphere'],
        'Condition': 'Control',
        'Separation': session['separation']['ctrl'][t_idx]
    })
    # Row 2: Opto
    long_form_data.append({
        'PID': session['pid'],
        'Hemisphere': session['hemisphere'],
        'Condition': 'Opto',
        'Separation': session['separation']['opto'][t_idx]
    })

df_long = pd.DataFrame(long_form_data)
# Filter for only Ipsi/Contra (ignore 'Other' if any)
df_long = df_long[df_long['Hemisphere'].isin(['Ipsi', 'Contra'])]

# Plotting
plt.figure(figsize=(7, 6))

# Define palette manually to ensure Control=Black, Opto=Blue
palette = {'Control': 'gray', 'Opto': 'dodgerblue'}

sns.barplot(
    data=df_long, 
    x='Hemisphere', 
    y='Separation', 
    hue='Condition', 
    palette=palette,
    errorbar='se', 
    capsize=0.1,
    alpha=0.9
)

# Add swarmplot/stripplot for individual points
sns.stripplot(
    data=df_long, 
    x='Hemisphere', 
    y='Separation', 
    hue='Condition', 
    palette={'Control': 'black', 'Opto': 'darkblue'}, # Darker dots for visibility
    dodge=True, # Important: aligns dots with the grouped bars
    jitter=True,
    marker='o',
    alpha=0.6,
    legend=False
)

plt.axhline(0, color='k', linewidth=0.5)
plt.ylabel(f"CD Separation at {target_time}s")
plt.title("Effect of SNr Inhibition on Coding Direction")
plt.tight_layout()
plt.savefig(figures_path + '/Quantification_500ms_Grouped.png')
plt.show()

# --- STATISTICS ---
print(f"--- Paired Statistics at {target_time}s ---")
for hemi in ['Ipsi', 'Contra']:
    subset = df_long[df_long['Hemisphere'] == hemi]
    ctrl_vals = subset[subset['Condition'] == 'Control']['Separation'].values
    opto_vals = subset[subset['Condition'] == 'Opto']['Separation'].values
    
    # Ensure they are aligned by PID (Seaborn handles this, but for T-test we must be sure)
    # Assuming the list order preserved pairing, but let's be safe:
    pids = subset['PID'].unique()
    pairs = []
    for pid in pids:
        c = subset[(subset['Condition']=='Control') & (subset['PID']==pid)]['Separation'].values
        o = subset[(subset['Condition']=='Opto') & (subset['PID']==pid)]['Separation'].values
        if len(c)==1 and len(o)==1:
            pairs.append((c[0], o[0]))
            
    c_arr = np.array([p[0] for p in pairs])
    o_arr = np.array([p[1] for p in pairs])
    
    t, p = ttest_rel(c_arr, o_arr)
    print(f"{hemi}: Control Mean={c_arr.mean():.3f}, Opto Mean={o_arr.mean():.3f}")
    print(f"      p-val = {p:.5f} (N={len(c_arr)})")