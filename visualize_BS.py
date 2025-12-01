# import pickle
import pandas as pd
import numpy as np
from iblatlas.atlas import AllenAtlas, BrainRegions
import matplotlib.pyplot as plt
br = BrainRegions()

pd.set_option('display.max_rows', None)

# with open('/Users/natemiska/Documents/python/saved_figures/bs_analysis_allregions_dataframe_V3.pkl','rb') as f:
#     BS_clusters_dataframe = pickle.load(f)
BS_clusters_dataframe = pd.read_csv('/Users/natemiska/python/saved_figures/bs_analysis_allregions_dataframe_newanalysis.csv')

# only include units with IBLlabel >= some value
BS_clusters_dataframe = BS_clusters_dataframe.loc[BS_clusters_dataframe['IBLlabel'] >= 1]

grouped = BS_clusters_dataframe.groupby('Berylregion')['bs'].agg(['sum','count'])
# grouped = BS_clusters_dataframe.groupby('Allenregion')['bs'].agg(['sum','count'])
grouped['percentage'] = grouped['sum'] / grouped['count'] * 100

grouped = grouped.sort_values(by='percentage', ascending=False)

# grouped99 = BS_clusters_dataframe.groupby('Berylregion')['bs99'].agg(['sum','count'])
# grouped99['percentage'] = grouped99['sum'] / grouped99['count'] * 100

# grouped99 = grouped99.sort_values(by='percentage', ascending=False)

# grouped999 = BS_clusters_dataframe.groupby('Berylregion')['bs999'].agg(['sum','count'])
# grouped999['percentage'] = grouped999['sum'] / grouped999['count'] * 100

# grouped999 = grouped999.sort_values(by='percentage', ascending=False)

print(grouped)

# print(grouped99)

# print(grouped999)


# #####################################################
### For generating scatter of regions; percent BS units versus significance
import statsmodels.api as sm
from scipy.stats import binomtest
from statsmodels.stats.proportion import proportion_confint

# Define a function to calculate the confidence interval and p-value for each row
def get_conf_interval_and_pvalue(row):
    count = row['count']
    successes = row['sum']
    # prop_success = successes / count
    conf_interval = proportion_confint(successes, count)
    p_value = binomtest(successes, count, p=0.05)
    return pd.Series([conf_interval[0], conf_interval[1], p_value], index=['conf_interval_lower', 'conf_interval_upper', 'p_value'])

# Apply the function to each row of the dataframe and save the results in a new column
grouped[['conf_interval_lower', 'conf_interval_upper', 'p_value']] = grouped.apply(get_conf_interval_and_pvalue, axis=1)

# Define a function to calculate the logarithmic measure of p-value
def get_log_pvalue(row):
    p_value = row['p_value']
    log_p_value = -np.log10(p_value)
    return log_p_value

# Add a column to the dataframe containing the logarithmic measure of p-value
grouped['log_p_value'] = grouped.apply(get_log_pvalue, axis=1)

# Define the threshold count
threshold = 0
threshold_log_p = -np.log10(0.05)

# Filter the dataframe to only include regions with count > threshold
filtered_grouped = grouped[grouped['count'] > threshold]
filtered_grouped = grouped[grouped['log_p_value'] > threshold_log_p]

# Get RGB values for each region
# define function to get RGB value for each region
def get_color(acronym):
    rgb = br.descendants(br.acronym2id(acronym)).rgb[0]
    return tuple(rgb / 255)

# plot scatter plot with labeled markers
fig, ax = plt.subplots()
for i, row in filtered_grouped.iterrows():
    ax.scatter(row['percentage'], row['log_p_value'], s=row['count'], label=i, c=[get_color(i)], alpha=0.5)
    ax.annotate(i, (row['percentage'], row['log_p_value']), ha='center', va='center')
    
# plt.axvline(x=5, linestyle='--', color='red', label='null rate')
# set plot properties
plt.xlim(5,15)
# plt.ylim(-10,6500)
ax.set_xlabel('Percentage of bias-selective units')
ax.set_ylabel('-log p value')
ax.set_title('Block bias-selective brain regions')
ax.legend(title='Brain Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()



##################### visualizing whole-brain bias-selective density
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.stats import gaussian_kde
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

# cosmos_indices = np.unique(br.mappings['Cosmos'])
# beryl_indices = np.unique(br.mappings['Beryl'])
# th_index = np.where(br.acronym[cosmos_indices] == 'TH')[0]
# th_children = br.children(ids=th_index)  # This gets all child regions of 'TH'

thalamus_regions = np.array(["VPL", "VPM", "LGd", "LGv", "AD", "AV", "AM", "VA", "VL", "LD", 
                             "MD", "CM", "PVT", "LH", "PoT", "LP", "RH", "RT", "Re", "SMT", 
                             "PIL", "PT", "PCN", "SGN", "SMT", "SPF", "PP", "PVa", "PVp", "PVi", "SCH"])

VPL_and_surrounds = np.array(["VPL", "VPM", "RT", "VAL", "LD", "PO"])

dorsal_cortical_regions = np.array([
    # Orbital areas
    "ORBvl",  # Orbital area, ventrolateral part
    "ORBm",   # Orbital area, medial part
    "ORBl",   # Orbital area, lateral part
    "ORBd",   # Orbital area, dorsolateral part

    # Cingulate areas
    "ACAd",   # Anterior cingulate area, dorsal part
    "ACAv",   # Anterior cingulate area, ventral part
    "PL",     # Prelimbic area
    "ILA",    # Infralimbic area
    "FRP",    # Frontal pole, cerebral cortex

    # Motor areas
    "MOp",    # Primary motor cortex
    "MOs",    # Secondary motor cortex

    # Somatosensory areas
    "SSp-bfd",  # Primary somatosensory area, barrel field
    "SSp-ll",   # Primary somatosensory area, lower limb
    "SSp-m",    # Primary somatosensory area, mouth
    "SSp-n",    # Primary somatosensory area, nose
    "SSp-tr",   # Primary somatosensory area, trunk
    "SSp-ul",   # Primary somatosensory area, upper limb
    "SSs",      # Supplemental somatosensory area

    # Visual areas
    "VISal",  # Visual area, anterolateral part
    "VISam",  # Visual area, anteromedial part
    "VISl",   # Visual area, lateral part
    "VISp",   # Primary visual area
    "VISpm",  # Visual area, posteromedial part
    "VISrl",  # Visual area, rostrolateral part

    # Auditory areas
    "AUDp",  # Primary auditory area
    "AUDd",  # Auditory area, dorsal part
    "AUDv",  # Auditory area, ventral part
    "AUDpo", # Posterior auditory area

    # Temporal association areas
    "TEa",    # Temporal association areas

    # Parietal association areas
    "PTLp",   # Posterior parietal association areas

    # Retrosplenial areas
    "RSPagl", # Retrosplenial area, lateral agranular part
    "RSPd",   # Retrosplenial area, dorsal part
    "RSPv",   # Retrosplenial area, ventral part

    # Entorhinal areas
    "ENTm",   # Entorhinal area, medial part
    "ENTl",   # Entorhinal area, lateral part
    "ECT",    # Ectorhinal area
    "PERI",   # Perirhinal area

    "VISC", #Visceral area
    "GU", #Gustatory areas
])

frontal_regions = np.array([
    # Orbital areas
    "ORBvl",  # Orbital area, ventrolateral part
    "ORBm",   # Orbital area, medial part
    "ORBl",   # Orbital area, lateral part
    "ORBd",   # Orbital area, dorsolateral part

    # Cingulate areas
    "ACAd",   # Anterior cingulate area, dorsal part
    "ACAv",   # Anterior cingulate area, ventral part
    "PL",     # Prelimbic area
    "ILA",    # Infralimbic area
    "FRP",    # Frontal pole, cerebral cortex

    "AId",
    "AIp",
    "AIv",

    # Motor areas
    "MOp",    # Primary motor cortex
    "MOs",    # Secondary motor cortex

    # Somatosensory areas
    "SSp-bfd",  # Primary somatosensory area, barrel field
    "SSp-ll",   # Primary somatosensory area, lower limb
    "SSp-m",    # Primary somatosensory area, mouth
    "SSp-n",    # Primary somatosensory area, nose
    "SSp-tr",   # Primary somatosensory area, trunk
    "SSp-ul",   # Primary somatosensory area, upper limb
    "SSs",      # Supplemental somatosensory area
])

SNr_and_surrounds = np.array(['SNr','SNc','MRN','MB','RN','ZI','PP','PIL','ml','VTA','FF'])

caudoputamen = np.array(['CP'])

hippocampus_and_amygdala = np.array([
    'CA1', 
    'CA2', 
    'CA3', 
    'DG', 
    'SUB', 
    'PRE', 
    'PAR', 
    'ProS', 
    'ENTm', 
    'ENTl', 
    'ECT', 
    'AAA', 
    'AHi', 
    'CEA', 
    'COA', 
    'COAp', 
    'COAa', 
    'BLA', 
    'BLAa', 
    'BLAp', 
    'BMA', 
    'BMAa', 
    'BMAp', 
    'LA', 
    'MEA', 
    'MEAa', 
    'MEAp', 
    'IA', 
    'HATA'
])
# regions_to_use = MOs

somatosensory_areas = np.array([
    "SSp-bfd",  # Primary somatosensory area, barrel field
    "SSp-ll",   # Primary somatosensory area, lower limb
    "SSp-m",    # Primary somatosensory area, mouth
    "SSp-n",    # Primary somatosensory area, nose
    "SSp-tr",   # Primary somatosensory area, trunk
    "SSp-ul",   # Primary somatosensory area, upper limb
    "SSs",      # Supplemental somatosensory area
])

# Get a list of unique 'Berylregion' values and sort them alphabetically
# regions = sorted(BS_clusters_dataframe['Berylregion'].unique())
regions = dorsal_cortical_regions #np.array(['VPL'])

# Filter the dataframe to keep only the rows with 'Berylregion' in ...
# filtered_df = BS_clusters_dataframe[BS_clusters_dataframe['Berylregion'].isin(thalamus_regions)]
filtered_df = BS_clusters_dataframe

# Extract the x, y, z coordinates of all neurons and bs==1 neurons
all_coordinates = filtered_df[['x', 'y', 'z']].values.T
bs1_coordinates = filtered_df[filtered_df['bs'] == 1][['x', 'y', 'z']].values.T

# Define the bandwidth for the KDE function (adjust this value to control the smoothness and spread of the density estimation)
bandwidth = 0.3

# Compute the density of all neurons and bs==1 neurons using a 3D KDE function with the specified bandwidth
kde_all = gaussian_kde(all_coordinates, bw_method=bandwidth)
kde_bs1 = gaussian_kde(bs1_coordinates, bw_method=bandwidth)

density_all = kde_all(all_coordinates)
density_bs1 = kde_bs1(all_coordinates)

# Calculate the ratio of bs==1 neuron density to the sum of densities for both bs==1 and bs==0 neurons
ratio = density_bs1 / (density_bs1 + (density_all - density_bs1))

# Calculate the average ratio for all neurons
average_ratio = np.mean(ratio)

# Calculate the normalized ratio by dividing the ratio at each coordinate by the average ratio for all neurons
normalized_ratio = ratio / average_ratio

neutral_ratio = 1
# normalized_ratio = (normalized_ratio - neutral_ratio) / (np.max(normalized_ratio) - np.min(normalized_ratio))

# Add 'normalized_ratio' to your DataFrame
### Don't run this more than once!
filtered_df['normalized_ratio'] = normalized_ratio

# Manually reverse the RdYlBu colormap
reversed_colormap = px.colors.diverging.RdYlBu[::-1]

# Add custom hover data to the dataframe
# filtered_df["custom_hover"] = filtered_df["Berylregion"]
filtered_df["custom_hover"] = filtered_df['y']

# # Create a 3D scatter plot using Plotly, and color the points according to the normalized ratio
# fig = px.scatter_3d(
#     filtered_df,
#     x='x',
#     y='y',
#     z='z',
#     color=normalized_ratio,
#     color_continuous_scale=reversed_colormap,  # Use the custom colormap
#     color_continuous_midpoint=neutral_ratio,
#     hover_data=["custom_hover"],
#     labels={'color': 'Normalized Ratio'},
#     title="3D heatmap of bias selective neurons (bs==1) compared to all neurons across all brain regions"
# )

# fig.show()


# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])

# Add a trace for each region
for region in regions:
    region_df = filtered_df[filtered_df['Berylregion'] == region]
    fig.add_trace(
        go.Scatter3d(
            x=region_df['x'],
            y=region_df['y'],
            z=region_df['z'],
            mode='markers',
            marker=dict(
                color=region_df['normalized_ratio'],
                colorscale=reversed_colormap,
                cmin=0,
                cmax=2.1,
                colorbar=dict(thickness=20),
                size=5,  # Increase marker size here
                showscale=False  # Do not show color scale for individual traces
            ),
            text=region_df['Berylregion'],
            hoverinfo='text',
            name=region,
            visible=True  # All traces are visible initially
        )
    )

# Set axis range
xaxis_range = [filtered_df['x'].min(), filtered_df['x'].max()]
yaxis_range = [filtered_df['y'].min(), filtered_df['y'].max()]
zaxis_range = [filtered_df['z'].min(), filtered_df['z'].max()]  # Update z-axis range

# Create a list of dictionary for updatemenus argument
updatemenus = [dict(
    buttons=[
        # Button to show all regions
        dict(
            args=[{"visible": [True]*len(regions)}],
            label="All Regions",
            method="update"
        )
    ] + [
        # Buttons for individual regions
        dict(
            args=[{"visible": [region == r for r in regions]}],
            label=region,
            method="update"
        ) for region in regions],
    direction="down",
    pad={"r": 10, "t": 10},
    showactive=True,
    x=0,
    xanchor="left",
    y=1.1,
    yanchor="top"
)]

# Set the scene layout to enforce the axis range and aspect ratio
scene_layout = dict(
    xaxis=dict(range=xaxis_range),
    yaxis=dict(range=yaxis_range),
    zaxis=dict(range=zaxis_range),
    aspectmode='manual',
    aspectratio=dict(x=0.8, y=1.2, z=0.8)  
)

fig.update_layout(updatemenus=updatemenus, scene=scene_layout)


# Add a colorbar to the layout
color_bar = go.Scatter3d(
    x=[None],
    y=[None],
    z=[None],
    mode='markers',
    marker=dict(
        colorscale=reversed_colormap,
        colorbar=dict(thickness=20),
        cmin=0,
        cmax=2.1
    ),
    showlegend=False
)
fig.add_trace(color_bar)

# Set default title
fig.update_layout(title_text="Select a region from dropdown", title_x=0.5)

# Show the plot
fig.show()


## export plot to html file
# pio.write_html(fig, 'interactive_bs_heatplot_v5_3.html')





# ###plotting
# region_clusters_indices_sig = np.where((BS_clusters_dataframe.Berylregion == 'PL') & (BS_clusters_dataframe.bs99 == 1))[0] + 1
# region_clusters_indices_nonsig = np.where((BS_clusters_dataframe.Berylregion == 'PL') & (BS_clusters_dataframe.bs99 == 0))[0] + 1
# # region_clusters_indices_sig = np.where(BS_clusters_dataframe.bs999 == 1)[0] + 1
# # region_clusters_indices_nonsig = np.where(BS_clusters_dataframe.bs999 == 0)[0] + 1
# x_sig = list(BS_clusters_dataframe.x[region_clusters_indices_sig])
# y_sig = list(BS_clusters_dataframe.y[region_clusters_indices_sig])
# z_sig = list(BS_clusters_dataframe.z[region_clusters_indices_sig])
# x_nonsig = list(BS_clusters_dataframe.x[region_clusters_indices_nonsig])
# y_nonsig = list(BS_clusters_dataframe.y[region_clusters_indices_nonsig])
# z_nonsig = list(BS_clusters_dataframe.z[region_clusters_indices_nonsig])
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# #ax = fig.add_subplot(111, projection='3d')
# ax = Axes3D(fig)
# ax.scatter(x_nonsig, y_nonsig, z_nonsig, alpha=0.01)#c='black', s=10)
# ax.scatter(x_sig, y_sig, z_sig, c='red', s=20)
# # ax.scatter(BS_clusters_dataframe.x[region_clusters_indices_sig], BS_clusters_dataframe.y[region_clusters_indices_sig], BS_clusters_dataframe.z[region_clusters_indices_sig], c='red', s=20)
# # plt.xlim(-0.003, 0)
# # plt.ylim(-1, 1)

# proportion_sig = np.size(region_clusters_indices_sig)/(np.size(region_clusters_indices_sig)+np.size(region_clusters_indices_nonsig))
# print('proportion sig =' + str(proportion_sig))
# print('total # units = ' + str((np.size(region_clusters_indices_sig)+np.size(region_clusters_indices_nonsig))))

# plt.show()