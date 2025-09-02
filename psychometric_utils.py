import pickle
import requests
import os
import sys
import re 

print(os.getcwd())
new_path = '/Users/feiyang/Projects/GLM-HMM/ssm/GLM-HMM'
os.chdir(new_path)

sys.path.append('/Users/feiyang/Projects/GLM-HMM')
sys.path.append('/Users/feiyang/Projects/GLM-HMM/ssm')
sys.path.append('/Users/feiyang/Projects/Reverse')

# Create panels a-c of Figure 3 of Ashwood et al. (2020)
import json
import pandas as pd
import os
from os.path import join
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import numpy as np
from data_utils import paths, subjectdict_to_dataframe
from plotting_utils import load_glmhmm_data, load_cv_arr, load_data, \
    get_file_name_for_best_model_fold, partition_data_by_session, \
    create_violation_mask, get_marginal_posterior, get_was_correct, \
    plot_example_sessions, get_state_given_bias, plot_GLMHMM_results, \
    load_bias
from glm_hmm_utils import get_raw_data, create_design_mat, remap_choice_vals
from pprint import pprint
from one.api import ONE
from one.alf.io import AlfBunch



######################## FOR GLM-HMM ANALYSIS ########################

# psychometric_utils
def get_glmhmm_indices(subject, eid, state_probability, n_states):
    """
    n_states: Integer, 2: Concatenates right/left engaged into a single 'engaged' label. Likewise for 'disengaged'/
                    4: Returns right/left engaged and right/left disengaged labels. 
                    
    """
    states = state_probability[subject][eid][0]

    if n_states == 2:
        engaged_indices = np.where(np.logical_or(states == 2, states == 3))[0]  
        disengaged_indices = np.where(np.logical_or(states == 1, states == 4))[0]  

        return engaged_indices, disengaged_indices

    elif n_states == 4: 
        left_engaged_idx = np.where(states == 3)
        left_disengaged_idx = np.where(states == 4)
        right_engaged_idx = np.where(states == 2)
        right_disengaged_idx = np.where(states == 1)

        return left_engaged_idx, left_disengaged_idx, right_engaged_idx, right_disengaged_idx
    



# engaged, disengaged = get_glmhmm_indices(eids, trials_ranges, n_states=2, state_def='previous')

# def get_glmhmm_indices(eids, trials_ranges, n_states, state_def='current', RT_threshold=100):
#     with open("/Users/feiyang/Projects/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
#         state_probability = pickle.load(pickle_file)

#     ### GLM-HMM 
#     if n_states == 2: 
#         engaged_indices = {}
#         disengaged_indices = {}
#     elif n_states == 4: 
#         left_engaged_indices = {}
#         left_disengaged_indices = {}
#         right_engaged_indices = {}
#         right_disengaged_indices = {}
    
#     one = ONE(mode='remote')
#     for i, eid in enumerate(eids): 

#         try: 
#             trials = one.load_object(eid, 'trials')

#         except:
#             print('Failed to load eid = ' + eid)
#             continue 

#         subject = one.get_details(eid)['subject']

#         if n_states == 2: 
#             engaged_indices[eid] = []
#             disengaged_indices[eid] = []
#         elif n_states == 4: 
#             left_engaged_indices[eid] = []
#             left_disengaged_indices[eid] = []
#             right_engaged_indices[eid] = []
#             right_disengaged_indices[eid] = []

#         ### retrieve opto indicies
#         if trials_ranges[i] == 'ALL':
#             trials_range = range(0,len(trials['contrastLeft']))
#         elif trials_ranges[i][-1] == 9998: # use last trial as end of range when end of range set to 9999
#             trials_range = [x for x in trials_ranges[i] if x < np.size(trials.probabilityLeft)]
#         else:
#             trials_range = trials_ranges[i]

#         stim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
#         nonstim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)


#         laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
#         for k in trials_range:#range(0,len(trials.intervals)):

#             if stim_params[i] == 'QPRE':

#                 if trials.intervals[k,0] in laser_intervals[:,0]:
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:  
#                         stim_trials_numbers[k] = k
#                 else:
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:
#                         nonstim_trials_numbers[k] = k  

#             elif stim_params[i] == 'SORE':

#                 start_trial = trials.intervals[k, 0]
#                 end_trial = trials.intervals[k, 1]

#                 if np.any((laser_intervals[:, 0] >= start_trial) & (laser_intervals[:, 0] <= end_trial)):
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:  
#                         stim_trials_numbers[k] = k
#                 else:
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:
#                         nonstim_trials_numbers[k] = k  


#         states = state_probability[subject][eid][0]                                                
#         modified_stim_trials = stim_trials_numbers.copy()

#         # Get indices of valid (non-NaN) values in nonstim_trials_numbers
#         valid_nonstim = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]

#         for i in range(len(stim_trials_numbers)):
#             if not np.isnan(stim_trials_numbers[i]):  # Only process non-NaN values
#                 stim_value = stim_trials_numbers[i]

#                 # Find the nearest smaller and larger values
#                 smaller_values = valid_nonstim[valid_nonstim < stim_value]
#                 larger_values = valid_nonstim[valid_nonstim > stim_value]

#                 nearest_smaller = np.max(smaller_values) if smaller_values.size > 0 else np.nan
#                 nearest_larger = np.min(larger_values) if larger_values.size > 0 else np.nan

#                 # Determine which to use
#                 if not np.isnan(nearest_smaller) and abs(stim_value - nearest_smaller) <= 10:
#                     new_state = states[int(nearest_smaller)]  # Use nearest smaller if within 10
#                 elif not np.isnan(nearest_larger):  
#                     new_state = states[int(nearest_larger)]  # Otherwise, use nearest larger
#                 else:
#                     new_state = np.nan  # If nothing is found, keep NaN

#                 # Assign value if valid
#                 if not np.isnan(new_state):
#                     modified_stim_trials[i] = new_state    

#         modified_states = np.copy(states)    
#         valid_stim_indices = ~np.isnan(stim_trials_numbers)

#         modified_states[valid_stim_indices] = modified_stim_trials[~np.isnan(modified_stim_trials)]

#         if state_def == 'previous':
#             states = modified_states

#         if n_states == 2:
#             engaged_indices[eid] = np.where(np.logical_or(states == 2, states == 3))[0]  
#             disengaged_indices[eid] = np.where(np.logical_or(states == 1, states == 4))[0]  

#         elif n_states == 4: 
#             left_engaged_indices[eid] = np.where(states == 3)
#             left_disengaged_indices[eid] = np.where(states == 4)
#             right_engaged_indices[eid] = np.where(states == 2)
#             right_disengaged_indices[eid] = np.where(states == 1)
    
#     if n_states == 2:
#         return engaged_indices, disengaged_indices
#     if n_states == 4:    
#         return left_engaged_indices, left_disengaged_indices, right_engaged_indices, right_disengaged_indices


def makepretty():
    """A simple function to format our psychometric plots"""
    # Ensure x label is not cut off
    plt.gcf().subplots_adjust(bottom=0.15)
    # Plot lines at zero and .5
    plt.plot((0, 0), (0, 1), 'k:')
    plt.plot((-100, 100), (.5, .5), 'k:')
    # Set limits and labels
    plt.gca().set(ylim=[-.05, 1.05], xlabel='contrast (%)', ylabel='proportion leftward')
    sns.despine(offset=10, trim=True)


def is_eid_successful(state_dict, subject, session_eid):
    """Returns True if the given session EID contains valid glm-hmm data, False otherwise."""
    return bool(state_dict.get(subject, {}).get(session_eid)) 


# Wrangle the data into the correct form
def signed_contrast(trials):
    """Returns an array of signed contrasts in percent, where -ve values are on the left"""
    # Replace NaNs with zeros, stack and take the difference
    contrast = np.nan_to_num(np.c_[trials.contrastLeft, trials.contrastRight])
    return np.diff(contrast).flatten() * 100


def calculate_choice_probability(condition_data, block_type, contrast_level):
    """
    Calculate the probability of making a leftward choice for a given block type and contrast level.

    :param condition_data: Dictionary with condition numbers as keys and lists of trial data as values.
    :param block_type: String, either 'left' or 'right' to specify the block.
    :param contrast_level: Numeric value of the contrast level for which to calculate the probability.
    :return: Probability of making a leftward choice.
    """
    # Filter trials based on block type and contrast level
    if block_type == 'left':
        relevant_trials = [trial for trial in condition_data if trial['contrast'] == contrast_level and trial['probabilityLeft'] == 0.8]
    else:  # 'right' block
        relevant_trials = [trial for trial in condition_data if trial['contrast'] == contrast_level and trial['probabilityLeft'] == 0.2]
    
    # Count the number of rightward choices
    leftward_choices = sum(1 for trial in relevant_trials if trial['choice'] == -1)
    
    # Calculate the probability of rightward choice
    if len(relevant_trials) == 0:
        return None  # Avoid division by zero if there are no relevant trials
    else:
        return leftward_choices / len(relevant_trials)

# # Example usage:
# # Assuming condition_data[53] is a list of trial data dictionaries for nonstim condition
# # and you want to calculate the choice probability for the left block at a contrast of 25
# contrast_level = 25
# left_block_prob = calculate_choice_probability(condition_data[53], 'left', contrast_level)
# print(f'Left block probability at contrast {contrast_level}:', left_block_prob)
    

######################## FOR HEAD ROTATION ANALYSIS ########################
    
def moving_average(data, window_size=5):
    # Sliding window for smoothing

    kernel = np.ones(window_size) / window_size
    smoothed = np.convolve(data, kernel, mode='valid')  # Apply convolution

    # Pad edges with nearest valid values to avoid artefacts
    pad_size = (window_size - 1) // 2
    smoothed = np.pad(smoothed, (pad_size, pad_size), mode='edge')

    return smoothed


def interpolate_array(x, y):
    """Interpolate missing values (NaN) in x and y arrays."""
    # Create DataFrames to handle interpolation easily
    x_df = pd.DataFrame(x)
    y_df = pd.DataFrame(y)
    
    # Perform linear interpolation
    x_interpolated = x_df.interpolate(method='linear', limit_direction='both').values.flatten()
    y_interpolated = y_df.interpolate(method='linear', limit_direction='both').values.flatten()
    
    return x_interpolated, y_interpolated


def calculate_head_angles(interp_nodes, angle_type='radian'):

    """
    Calculates frame-by-frame head angle using neck-nose vector 

    interp_nodes: Dictionary, containing node xy-coordinates as .keys()
    angle_type: String. Returns head_angle as either 'radian' (default) or 'degree'
    """

    # Extract interpolated arrays
    neck_x_interp, neck_y_interp = interp_nodes["neck"]
    nose_x_interp, nose_y_interp = interp_nodes["nose"]

    head_angles = []
    for i in range(len(nose_x_interp)):
        # Current frame coordinates
        nose = np.array([nose_x_interp[i], nose_y_interp[i]])
        neck = np.array([neck_x_interp[i], neck_y_interp[i]])

        # Compute vectors
        vector_neck = neck - nose  # Nose-to-neck vector
        V_x, V_y = vector_neck[0], vector_neck[1]  # Extract x and y components

        # Compute head angle relative to the x-axis
        angle_rad = np.arctan2(V_y, V_x)  # Angle in radians
        angle_deg = np.degrees(angle_rad) # Convert to degree

        if angle_type == 'degree': 
            head_angles.append(angle_deg)
        elif angle_type == 'radian':
            head_angles.append(angle_rad)

    head_angles = np.array(head_angles) # Convert list to np.array for easier manipulation

    return head_angles


def calculate_total_rotations(angles_rad, smoothing_window=5):

    """
    Calculates total signed rotations from head angles in radians.
    - Positive = Counterclockwise
    - Negative = Clockwise
    """
    
    # Initialize raw angular velocities
    raw_ang_velocities = []

    # Calculate raw angular velocities
    prev_angle = angles_rad[0]
    for angle in angles_rad[1:]:
        # Calculate difference from previous angle
        diff = angle - prev_angle
        # If the difference is large (the mouse crossed the 0=2*pi line)...
        if diff > np.pi:
            # Subtract 2*pi from the difference
            diff -= 2*np.pi
        elif diff < -np.pi:
            # Add 2*pi to the difference
            diff += 2*np.pi

        # Add to raw angular velocities
        raw_ang_velocities.append(diff)

        # This angle becomes the previous angle for the next iteration
        prev_angle = angle

    # Smooth angular velocities
    smoothed_ang_velocities = pd.Series(raw_ang_velocities).rolling(window=smoothing_window, center=True, min_periods=1).mean()

    # Calculate total rotations (integral of angular velocity)
    total_rotations = np.trapz(smoothed_ang_velocities) / (2*np.pi)

    # Separate clockwise and counterclockwise rotations
    counterclockwise_rotations = np.trapz(smoothed_ang_velocities[smoothed_ang_velocities < 0]) / (2 * np.pi)
    clockwise_rotations = np.trapz(smoothed_ang_velocities[smoothed_ang_velocities > 0]) / (2 * np.pi)

    return total_rotations, clockwise_rotations, counterclockwise_rotations


def average_sessions(all_head_angles, merge_repeats=True, normalisation=True):
    """
    Averages head angles across subjects.
    
    Parameters:
        all_head_angles (dict): Dictionary of subjects containing their session data.
        merge_variants (bool): If True, combines duplicate sessions (e.g. left_snr_0hz and left_snr_0hz_2).

    Returns:
        dict: A dictionary with averaged head angles in radians.
    """
    sessions_averaged = {}  # Final output
    session_data = {}  # Temporary storage for sessions before averaging
    sessions_std = {}

    # Organize sessions by session type
    for subject, sessions in all_head_angles.items():
        for session_name, angles in sessions.items():
            # Extract the session type by removing the subject number
            session_type = "_".join(session_name.split("_")[1:])  # Removes subject number

            # If merge_variants is True, remove "_2" at the end
            if merge_repeats:
                session_type = re.sub(r"_2$", "", session_type)

            # Store the data under its session type
            if session_type not in session_data:
                session_data[session_type] = []

            # Process the angles
            continuous_angles = np.concatenate(angles)  # Collapses to a continuous session
            corrected_angles = np.unwrap(continuous_angles)  # Removes angle discontinuity

            # Apply z-score normalisation
            if normalisation:
                mean_val = np.nanmean(corrected_angles)
                std_val = np.nanstd(corrected_angles)
                corrected_angles = (corrected_angles - mean_val) / std_val  

            session_data[session_type].append(corrected_angles)

    # Compute averages
    for session_type, angle_lists in session_data.items():
        max_length = max(len(a) for a in angle_lists)  # Find the longest session
        
        # Pad shorter sequences with NaNs
        padded_arrays = np.full((len(angle_lists), max_length), np.nan)
        for i, a in enumerate(angle_lists):
            padded_arrays[i, :len(a)] = a  # Fill with actual values

        # Compute mean, ignoring NaNs (to account for different session lengths)
        sessions_averaged[session_type] = np.nanmean(padded_arrays, axis=0)
        sessions_std[session_type] = np.nanstd(padded_arrays, axis=0)

    return session_data, sessions_averaged, sessions_std


def process_head_angles(angles, cutoff_freq=5.0, sampling_rate=100, baseline_correction=True):
    """
    Applies a low-pass filter, baseline correction, and z-score normalization to the head angles data.

    Parameters:
        angles (np.array): The continuous head angles data.
        cutoff_freq (float): Cutoff frequency for the low-pass filter (Hz).
        sampling_rate (int): Sampling rate in Hz.
        baseline_correction (bool): If True, subtracts the initial baseline value.

    Returns:
        np.array: Processed head angles.
    """

    # --- Step 1: Apply Low-Pass Filter ---
    def lowpass_filter(data, cutoff, fs, order=4):
        nyquist = 0.5 * fs  # Nyquist frequency
        normal_cutoff = cutoff / nyquist  # Normalize cutoff frequency
        b, a = butter(order, normal_cutoff, btype='low', analog=False)  # Design filter
        return filtfilt(b, a, data)  # Apply filter

    smoothed_angles = lowpass_filter(angles, cutoff_freq, sampling_rate)

    # --- Step 2: Baseline Correction (Optional) ---
    if baseline_correction:
        baseline_value = np.nanmean(smoothed_angles[:100])  # Mean of first 100 samples (adjustable)
        smoothed_angles -= baseline_value  # Subtract baseline

    return smoothed_angles


def add_stat_annotation(ax, x1, x2, y, h, p_val):
    """Draw simple significance annotations with stars only."""
    # Decide stars based on p-value
    if p_val < 0.001:
        stars = '***'
    elif p_val < 0.01:
        stars = '**'
    elif p_val < 0.05:
        stars = '*'
    else:  
    # else:
    #     stars = 'ns'
        return

    # Draw a simple straight line
    ax.plot([x1, x2], [y, y], lw=1.2, c='black')
    ax.text((x1 + x2) * 0.5, y + h, stars, ha='center', va='bottom', color='black')


def annotate_p_value(ax, x1, x2, y, p_value):
    ax.annotate("", xy=(x1, y), xycoords='data', xytext=(x2, y), textcoords='data', 
                arrowprops=dict(arrowstyle="-", lw=1.5, color="black"))
    ax.text((x1 + x2) * .5, y, f"p = {p_value:.3f}", ha="center", va="bottom", color="black")



def standardise_df(df):
    # Ensure Mouse_number is integer
    df['Mouse_number'] = pd.to_numeric(df['Mouse_number'], errors='coerce').astype('Int64')
    
    # Standardize Hemisphere: map variations to "Left" or "Right"
    hemisphere_map = {
        'l': 'Left', 'L': 'Left', 'left': 'Left', 'Left': 'Left',
        'r': 'Right', 'R': 'Right', 'right': 'Right', 'Right': 'Right'
    }
    df['Hemisphere'] = df['Hemisphere'].astype(str).str.strip().map(hemisphere_map)
    
    # Standardize Stimulation: uppercase everything (e.g., 50hz -> 50HZ)
    df['Stimulation'] = df['Stimulation'].astype(str).str.strip().str.upper()
    
    return df
