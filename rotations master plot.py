import sys
sys.path.append('/Users/feiyang/Projects/GLM-HMM')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import ttest_ind
import pickle
from psychometric_utils import standardise_df, add_stat_annotation

# pd.set_option('display.max_columns', 50)                                            # Forces pd. to display up to 50 columns

# Read the DataFrame from the CSV file
df = pd.read_csv('/Volumes/Data/SLEAP_Project_final/inference_mouse_data.csv')        # SWC_NM_ subjects
# df = pd.read_csv('/Users/feiyang/Projects/GLM-HMM/head_rotations.csv')              # SWC_AY_ subjects

# Standardise columns/condition names
df.columns = df.columns.str.replace(' ', '_')
df = standardise_df(df)

# ================ OPTIONS ================
significance_threshold = 0.05                                                         # Threshold for significance
include_LR_comparisons = True                                                         # Include Left vs. Right hemisphere comparisons in the plot?

# For analysing individual mice
plot_individual_mouse = True                                                          # !! IMPORTANT: Switch between False (masterplot) & True (individual analysis)
individual_mouse = 42                                                                 # Individual mouse to analyse

# For running a master plot (multiple regions)
brain_regions = ['SNr', 'ZI', 'STN', 'VLSD1', 'VLSD2', 'VMS', 'DLS', 'PL', 'M2']      # Regions to analyse & plot
mice_to_remove = [93]                                                                 # Mice to exclude from analysis. If analysing individual mice, this is ignored.     
# =========================================

if plot_individual_mouse:
    # Filters data to only include entries from the specified mouse
    re_df = df[df['Mouse_number'] == individual_mouse]
    print(f'Analysing data from mouse #{individual_mouse:}...')

else: 
    # Filters data to exclude entries from the specified mouse
    re_df = df[~df['Mouse_number'].isin(mice_to_remove)]
    print(f'Creating master plot...')

# Animals with true CTR sessions
ids_with_ctr = re_df[re_df['Stimulation'] == 'CTR']['Mouse_number'].unique()
ids_with_ctr = set(ids_with_ctr)

stimulations = ['0HZ', '50HZ']
hemispheres = ["Left", "Right", "Control"]

colors_dict = {
    'Left': {
        '0HZ': 'lightblue',
        '50HZ': 'lightblue',
        '2HZ': '#A1CAF1',
        '4HZ': '#0000FF',
        'stat_significant': '#337CCF',
        'Control': '#D3D3D3'
    },
    'Right': {
        '0HZ': 'lightpink',
        '50HZ': 'lightpink',
        '2HZ': '#FBB982',
        '4HZ': '#FF6103',
        'stat_significant': '#BB2525',
        'Control': '#D3D3D3'
    }
}

# Create a master_data dictionary for more organized access
master_data_dict = {(brain_region, stim): {} for brain_region in brain_regions for stim in stimulations}
p_values = {
    (brain_region, stim, hem): {} 
    for brain_region in brain_regions
    for stim in stimulations
    for hem in ["Left", "Right", "L vs R"]
}

# Loop through each brain region
for brain_region in brain_regions:
    sub_df_all = re_df[re_df['Brain_region'] == brain_region].copy()    
    sub_df_all['Avg_Rotations_per_20_seconds'] = sub_df_all['Total_Rotations'] / (sub_df_all['Frames'] / 500)          # Average number of rotations per 20 s
    
    for stim in stimulations:                                                                                          # Loops through all stimulation types (0 Hz, 50 Hz, CTR)
                                                                                                                       # CTR: True control sessions    
        if stim not in sub_df_all['Stimulation'].values:  
            print(f"No data for {stim} in {brain_region}, skipping...")
            continue

        left_data = sub_df_all[                                    # Left hemisphere stim ON data 
            (sub_df_all['Stimulation'] == stim) &
            (sub_df_all['Hemisphere'] == "Left") &
            (sub_df_all['Session_#'].notna())
        ]['Avg_Rotations_per_20_seconds']
        
        right_data = sub_df_all[                                   # Right hemisphere stim ON data 
            (sub_df_all['Stimulation'] == stim) &
            (sub_df_all['Hemisphere'] == "Right") &
            (sub_df_all['Session_#'].notna())
        ]['Avg_Rotations_per_20_seconds']

        # Statistical comparison between Left and Right hemisphere
        if include_LR_comparisons:
            tstat, pval = ttest_ind(left_data, right_data)
            p_values[(brain_region, stim, 'L vs R')] = pval

        data_for_stim = {}
        ctr_hemispheres = []
        
        for hemi in ['Left', 'Right']:  # 'Control']:
            sub_df = sub_df_all[(sub_df_all['Stimulation'] == stim) & 
                                (sub_df_all['Hemisphere'] == hemi)].copy()

            if not sub_df.empty:
                # Summary stat for stim periods
                stim_df = sub_df[pd.notna(sub_df['Session_#'])]
                mean_rotations = stim_df['Avg_Rotations_per_20_seconds'].mean()
                sem_rotations = stim_df['Avg_Rotations_per_20_seconds'].sem()

                data_for_stim[hemi] = {                                                                                
                    'mean': mean_rotations,
                    'sem': sem_rotations,
                    'color': colors_dict[hemi][stim]      
                }

            # Extract control data              
            # For mice with true CTR sessions...
            true_ctr_df = (sub_df_all[(sub_df_all['Stimulation'] == 'CTR') &
                                        (sub_df_all['Hemisphere'] == hemi) & 
                                        (sub_df_all['Brain_region'] == brain_region)])
            true_control_data = true_ctr_df[pd.notna(true_ctr_df['Session_#'])]['Avg_Rotations_per_20_seconds']

            # Mice WITHOUT true CTR sessions (use ISI instead)...
            mask_no_ctr = (                                                                                            
                ~sub_df['Mouse_number'].isin(ids_with_ctr) &
                pd.notna(sub_df['Control_#'])
            )
            isi_data = sub_df[mask_no_ctr]['Avg_Rotations_per_20_seconds']

            # Concatenate true & ISI CTR data
            control_data = pd.concat([true_control_data, isi_data])                                                    # Average number of rotations during ISI periods (normalised to epoch duration)
            ctr_hemispheres.append(control_data)

            # Stim vs. CTR head rotations (t-test)
            tstat, pval = ttest_ind(stim_df['Avg_Rotations_per_20_seconds'], control_data)
            if pval < significance_threshold:
                data_for_stim[hemi]["color"] = colors_dict[hemi]["stat_significant"]

            # Store p-vals in dictionary
            p_values[(brain_region, stim, hemi)] = pval

        # For plotting purposes, combine data from Left & Right hemisphere
        all_control_data = pd.concat(ctr_hemispheres) 

        if not all_control_data.empty:
            data_for_stim["Control"] = {                                                                           # Summary stats
                'mean': all_control_data.mean(),
                'sem': all_control_data.sem(),
                'color': colors_dict['Right']['Control']  # Control color
            }
            
        # Store data in master_data_dict instead of appending to master_data
        master_data_dict[(brain_region, stim)] = data_for_stim

# Convert master_data_dict to a list format for plotting
master_data = [(brain_region, stim, data) for (brain_region, stim), data in master_data_dict.items() if data]

# ------------- Plotting -------------
if plot_individual_mouse:
    fig, ax = plt.subplots(figsize=(6, 5))  # Smaller plot for a single brain region
else:
    fig, ax = plt.subplots(figsize=(15, 7))  # Larger plot for the master plot
# fig, ax = plt.subplots(figsize=(15, 7))
bar_width = 0.25  # Increased bar width to make bars thicker
index = np.arange(len(master_data))

all_labels = []

# Adjusting loop structure to group by brain regions consecutively
for data_index, (brain_region, stim, data) in enumerate(master_data):
    all_labels.append(f"{brain_region} ({stim})")
        
    left_mean = data["Left"]["mean"] if "Left" in data else 0
    right_mean = data["Right"]["mean"] if "Right" in data else 0
    control_mean = data["Control"]["mean"] if "Control" in data else 0

    left_sem = data["Left"]["sem"] if "Left" in data else 0
    right_sem = data["Right"]["sem"] if "Right" in data else 0
    control_sem = data["Control"]["sem"] if "Control" in data else 0

    left_color = data["Left"]["color"] if "Left" in data else colors_dict["Left"]["Control"]
    right_color = data["Right"]["color"] if "Right" in data else colors_dict["Right"]["Control"]
    control_color = colors_dict["Right"]["Control"]

    # --- Plot bars ---
    ax.bar(index[data_index], left_mean, bar_width, yerr=left_sem, capsize=1, color=left_color, error_kw={'elinewidth': 0.7})
    ax.bar(index[data_index] + bar_width, right_mean, bar_width, yerr=right_sem, capsize=1, color=right_color, error_kw={'elinewidth': 0.7})
    ax.bar(index[data_index] + 2*bar_width, control_mean, bar_width, yerr=control_sem, capsize=1, color=control_color, error_kw={'elinewidth': 0.7})

    # --- Annotate p-values ---
    x_left = index[data_index]
    x_right = index[data_index] + bar_width
    x_control = index[data_index] + 2 * bar_width
    y_max = max(left_mean + left_sem, right_mean + right_sem, control_mean + control_sem)

    # Annotate Left vs Control
    key = (brain_region, stim, 'Left')
    if key in p_values:
        add_stat_annotation(ax, x_left, x_control, y_max + 0.2, 0.05, p_values[key])

    # Annotate Right vs Control
    key = (brain_region, stim, 'Right')
    if key in p_values:
        add_stat_annotation(ax, x_right, x_control, y_max + 0.6, 0.05, p_values[key])

    # Annotate Left vs Right
    if include_LR_comparisons:
        key = (brain_region, stim, 'L vs R')
        if key in p_values:
            add_stat_annotation(ax, x_left, x_right, y_max + 1.0, 0.05, p_values[key])

ax.set_xlabel('Brain Regions (Opto. Stimulation)')
ax.set_ylabel('Mean Rotations per 20 Seconds')
if not plot_individual_mouse: 
    ax.set_title('Head Rotations by Brain Region, Hemisphere and Stimulation')
else: 
    ax.set_title(f'Head Rotations SWC_NM_0{individual_mouse}')
ax.set_xticks(index + 1.5*bar_width)
ax.set_xticklabels(all_labels, rotation=45, ha='right')

handles, labels = ax.get_legend_handles_labels()
labels_out = []
handles_out = []
for handle, label in zip(handles, labels):
    if label not in labels_out:
        labels_out.append(label)
        handles_out.append(handle)
ax.legend(handles_out, labels_out, loc="upper right")

# Add Legend (Key) to the Plot
left_patch = plt.Rectangle((0,0), 1, 1, fc=colors_dict["Left"]["0HZ"], edgecolor="none")
right_patch = plt.Rectangle((0,0), 1, 1, fc=colors_dict["Right"]["0HZ"], edgecolor="none")
control_patch = plt.Rectangle((0,0), 1, 1, fc="#D3D3D3", edgecolor="none")                              # Using neutral color for control
left_sig_patch = plt.Rectangle((0,0), 1, 1, fc=colors_dict["Left"]["stat_significant"], edgecolor="none")
right_sig_patch = plt.Rectangle((0,0), 1, 1, fc=colors_dict["Right"]["stat_significant"], edgecolor="none")

if not plot_individual_mouse:                                                                           # Legend in the top left corner for master plot
    ax.legend([left_patch, right_patch, control_patch, left_sig_patch, right_sig_patch], 
            ["Left Hemisphere", "Right Hemisphere", "Control", "Left Significant", "Right Significant"], 
            loc="upper left")
else:                                                                                                   # Legend outside figure for individual mice
    ax.legend(
        [left_patch, right_patch, control_patch, left_sig_patch, right_sig_patch], 
        ["Left Hemisphere", "Right Hemisphere", "Control", "Left Significant", "Right Significant"], 
        loc="upper left", 
        bbox_to_anchor=(1.02, 1),                                                                       # Pushes legend outside
        borderaxespad=0
    )

plt.tight_layout()

# Save the figure
# plt.savefig(f"/Volumes/Data/masterplot.png", dpi=300)

plt.show()

### End ###

# Saves all p-vals into a .csv file
df_pvals = pd.DataFrame(                                                        # Converts tuple into pd.dataframe form
    [(br, stim, hem, p if isinstance(p, (int, float)) else None)
     for (br, stim, hem), p in p_values.items()],
    columns=["Brain_Region", "Stimulation", "Hemisphere", "p_value"]
)

# df_pvals.to_csv("/Volumes/Data/p_values.csv", index=False)                    # Save file

