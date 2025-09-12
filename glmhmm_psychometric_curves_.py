from datetime import datetime  # Only for formating title
import json
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ast
import pickle
from ibllib.io.raw_data_loaders import load_data
from one.api import ONE
import psychofit as psy
from scipy import stats
import re
import os

import sys
print(os.getcwd())
new_path = '/Users/natemiska/int-brain-lab/GLM-HMM'
os.chdir(new_path)
sys.path.append('/Users/natemiska/python/bias_coding')
sys.path.append('/Users/natemiska/python/bias_coding/Allen')
# one = ONE(mode='remote')
one = ONE(base_url='https://alyx.internationalbrainlab.org')

from psychometric_utils import get_glmhmm_indices, is_eid_successful, signed_contrast, calculate_choice_probability
from metadata_opto_allsessions_B import sessions, find_sessions_by_advanced_criteria


############# GLM-HMM SETTINGS #############



# GLM-HMM SETTINGS
n_states = 4
state_type = 'engaged' # 'disengaged' #'engaged' #'bypass'
state_def = 'current' # 'current'

title_text = state_type

eids, trials_ranges, MouseIDs, stim_params = find_sessions_by_advanced_criteria(
    sessions, 
    # EID = lambda x: x in ['21861d63-c3be-40f4-961b-421cb5fc3913','b1582929-1117-4e44-862e-c775008ca548','c86f4ece-cb61-4f61-a32b-044cc5a7a83f','58f72a9f-471a-4889-a986-49edf7732fc9'],
    # EID = lambda x: x in ['4801a128-66ae-4849-8611-65e71a19fd3b'],
    Mouse_ID = 'SWC_NM_097',
    # Mouse_ID = lambda x: x in ['SWC_AY_002', 'SWC_AY_008', 'SWC_AY_006', 'SWC_AY_010', 'SWC_AY_012'],
    # Mouse_ID = lambda x: x in ['SWC_NM_072', 'SWC_NM_071', 'SWC_NM_057', 'SWC_NM_058', 'SWC_NM_081', 'SWC_NM_082', 'SWC_NM_085', 'SWC_NM_086', 'SWC_NM_090', 'SWC_NM_091'], ### zapit
    # Mouse_ID = lambda x: x in ['SWC_NM_087', 'SWC_NM_065', 'SWC_NM_043'], #### VLS D2 ###SWC_NM_042
    # Mouse_ID = lambda x: x in ['SWC_NM_053', 'SWC_NM_073', 'SWC_NM_093'], #### VLS D1 ###'SWC_NM_038'
    # Mouse_ID = lambda x: x in ['SWC_NM_004', 'SWC_NM_008', 'SWC_NM_011', 'SWC_NM_012', 'SWC_NM_018', 'SWC_NM_016', 'SWC_NM_080'], # current SNr mice
    # Mouse_ID = lambda x: x in ['SWC_NM_024', 'SWC_NM_025', 'SWC_NM_026'], # current STN mice
    # Mouse_ID = lambda x: x in ['SWC_NM_003', 'SWC_NM_010', 'SWC_NM_022'], # current ZI mice
    # Date = '060324',
    # Hemisphere = 'both',
    # Opsin=lambda x: x in ['GtACR2', 'ChR2'],
    # Opsin='GtACR2',
    # Stimulation_Params ='zapit',
    Stimulation_Params = 'QPRE',
    # Stimulation_Params = lambda x: x in ['QPRE', 'QPRE*'],
    Pulse_Params = 'cont', 
    # Pulse_Params = 'motor_bilateral_mask', 
    # Pulse_Params = lambda x: x in ['50hz', '20hz', 'cont_c'],
    Laser_V = '0.7',
    # Laser_V = lambda x: x in ['0.7', '0.8', '0.9', '1'],
    # Genetic_Line = 'D1-Cre',
    # Brain_Region = 'motor_bilateral',
    # Brain_Region = 'SNr',
)


##### GLM-HMM #####
"""
state_def = "previous": Uses state on stim_trials - 1 for stim_trials. 
state labels are stored in 'engaged_prevtrial_indices.pkl' and 'disengaged_prevtrial_indices.pkl' files.

state_def = "current": Uses state on stim_trials. 
state labels retrieved by get_glmhmm_indices() later down in the script. 
"""

# load glm-hmm labels
with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
    state_probability = pickle.load(pickle_file)

# load trial-1 labels
with open("/Users/natemiska/int-brain-lab/GLM-HMM/engaged_prevtrial_indices.pkl", 'rb') as pickle_file:
    engaged_indices = pickle.load(pickle_file)
with open("/Users/natemiska/int-brain-lab/GLM-HMM/disengaged_prevtrial_indices.pkl", 'rb') as pickle_file: 
    disengaged_indices = pickle.load(pickle_file)


############### OPTIONS ####################
is_zapit_session = 0
BL_perf_thresh = 0
stim_perf_thresh = 0
# BL_perf_thresh = 0.2 #0.79    ## 
# stim_perf_thresh = 0 #0.5      ## performance threshold for opto stim ON trials 
min_num_trials = 0 #300
min_bias_threshold = 0.5 #0.75
min_bias_threshold_zapit = 1 #1.5
#RT_threshold = 30 #20
RT_threshold = 100 #don't change

only_include_bias_trials = 1 #if 0, include 50/50 block trials

use_trials_after_stim = 0
subsample_trials_after_stim = 0

plot_for_paper = 1 ### plots are in paper format
save_figures = 0 # 0: save figure = false; 1: save figure = true
figure_save_path = '/Users/natemiska/Documents/Lab_Data/LabMeetingJuly25/Figure3/'
figure_prefix = 'D1'

############## WHEEL OPTIONS ##############

length_of_time_to_analyze_wheel_movement = 10
interval = 0.1
stim_rt_threshold = 100
align_to = 'QP'#'feedback'#'goCue_pre'#'QP'
only_include_low_contrasts = 0
low_contrast_threshold = 13
########### OLD OPTIONS

remove_trials_before = 0#140 #346
loop_threshold_for_remove = 100
#list of eids to use

separate_stim_control = 0 # if 1, then stim not controlled by program (ie, no 'opto' parameter)
start_trials_w_block_switch = 0 # if 1, then start with first block switch after stim
remove_trials_after_block_switch = 0 # if 1, then remove x trials after block switch (defined below)
num_trials_to_keep_after_switch = 50

only_keep_later_trials = 0
later_trials_start = 0

only_analyze_trials_x_after_stim = 0 #for removing simply x trials immediately after start of stim


##################### MAIN LOOP ##########################

### for concatenating zapit data; will need to change number for different stims
num_stim_locations = 52

condition_data = {i: [] for i in range(0, num_stim_locations+1)}  # 1-52 for laser, 0 for control
bias_vals_LC = {i: [] for i in range(0, num_stim_locations+1)}

Rblock_wheel_movements_by_condition = [[] for _ in range(53)]
Lblock_wheel_movements_by_condition = [[] for _ in range(53)]

num_analyzed_sessions = 0
#for loop with each iteration creating stim / nonstim trials info for that eid (exactly as in manual_plot_script)
    #then, that trials info is added to a set of master trials info (one for stim, one for non-stim).  might be easiest if this is pre-allocated to correct size before loop
# for lm in range(0,6): #for analyzing each subject individually and using avg bias shift as a single data point
num_unique_mice = 0
previous_mouse_ID = 'NaN'

Rblock_wheel_movements_stim = [] 
Lblock_wheel_movements_stim = []
Rblock_wheel_movements_nonstim = []
Lblock_wheel_movements_nonstim = []

accuracy_lowcontrast_stim = np.empty([np.size(eids)])
accuracy_lowcontrast_stim[:] = np.nan
accuracy_lowcontrast_nonstim = np.empty([np.size(eids)])
accuracy_lowcontrast_nonstim[:] = np.nan
bias_shift = np.empty([np.size(eids)])
bias_shift[:] = np.nan
bias_shift_sum_all = np.empty([np.size(eids)])
bias_shift_sum_all[:] = np.nan
bias_shift_sum_all_LC = np.empty([np.size(eids)])
bias_shift_sum_all_LC[:] = np.nan
bias_shift_sum_all_LEFT = np.empty([np.size(eids)])
bias_shift_sum_all_LEFT[:] = np.nan
bias_shift_sum_all_RIGHT = np.empty([np.size(eids)])
bias_shift_sum_all_RIGHT[:] = np.nan
bias_shift_nonstim = np.empty([np.size(eids)])
bias_shift_nonstim[:] = np.nan
bias_shift_sum_all_nonstim = np.empty([np.size(eids)])
bias_shift_sum_all_nonstim[:] = np.nan
bias_shift_sum_all_nonstim_LC = np.empty([np.size(eids)])
bias_shift_sum_all_nonstim_LC[:] = np.nan
bias_shift_sum_all_nonstim_LEFT = np.empty([np.size(eids)])
bias_shift_sum_all_nonstim_LEFT[:] = np.nan
bias_shift_sum_all_nonstim_RIGHT = np.empty([np.size(eids)])
bias_shift_sum_all_nonstim_RIGHT[:] = np.nan
bias_shift0_all_nonstim = np.empty([np.size(eids)])
bias_shift0_all_nonstim[:] = np.nan
bias_shift0_all_stim = np.empty([np.size(eids)])
bias_shift0_all_stim[:] = np.nan
stim_zerocontrast_difference = np.empty([np.size(eids)])
stim_zerocontrast_difference[:] = np.nan
nonstim_zerocontrast_difference = np.empty([np.size(eids)])
nonstim_zerocontrast_difference[:] = np.nan
stim_sumall_difference = np.empty([np.size(eids)])
stim_sumall_difference[:] = np.nan
nonstim_sumall_difference = np.empty([np.size(eids)])
nonstim_sumall_difference[:] = np.nan
deviation = [] 
for j in range(0,np.size(eids)):

    eid = eids[j]

    print('starting session, eid = ' + eid)
    try:
        trials = one.load_object(eid, 'trials')

    except:
        print('Failed to load eid = ' + eid)
        #input("Press Enter to continue...")
        continue

    if is_zapit_session == 0:
        try:
            dset = '_iblrig_taskData.raw*'
            data_behav = one.load_dataset(eid, dataset=dset, collection='raw_behavior_data')
            ses_path = one.eid2path(eid)
        except:
            print('Dataset "_iblrig_taskData.raw*.*" not found for eid = ' + eid + '. Utilizing laser intervals data...')
            laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
    wheel = one.load_object(eid, 'wheel')
    current_mouse_ID = MouseIDs[j]

    if not is_eid_successful(state_probability, current_mouse_ID, eid):
        continue  # Skip eid with failed glm-hmm sessions
    

    if is_zapit_session == 0:
        reaction_times = np.empty([np.size(trials['contrastLeft'])])
        reaction_times[:] = np.nan
        quiescent_period_times = np.empty([np.size(trials['contrastLeft'])])
        quiescent_period_times[:] = np.nan

        try:
            taskData = load_data(ses_path) ###depricated
        except:
            print('no task data found...')
        for tr in range(len(trials['contrastLeft'])):
            react = trials['feedback_times'][tr] - trials['goCue_times'][tr]
            if react > 59.9:
                # print('error')
                continue
            try:
                trial_start_time = taskData[tr]['behavior_data']['States timestamps']['trial_start'][0][0]
                stimOn_time = taskData[tr]['behavior_data']['States timestamps']['stim_on'][0][0]
            except:
                trial_start_time = trials.intervals[tr,0]
                stimOn_time = trials.goCue_times[tr]

            qp = stimOn_time - trial_start_time
            reaction_times[tr] = react
            quiescent_period_times[tr] = qp            

        if num_analyzed_sessions == 0:

            stim_trials = trials.copy()
            nonstim_trials = trials.copy()


        stim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
        nonstim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
        if trials_ranges[j] == 'ALL':
            trials_range = range(0,len(trials['contrastLeft']))
        #### use last trial as end of range when end of range set to 9999
        elif trials_ranges[j][-1] == 9998:
            trials_range = [x for x in trials_ranges[j] if x < np.size(trials.probabilityLeft)]
        else:
            trials_range = trials_ranges[j]
        if remove_trials_before > 0 and j < loop_threshold_for_remove:
            trials_range = list(np.array(trials_range)[np.where(np.array(trials_range) > remove_trials_before)[0]])
        if len(trials_range) < min_num_trials:
            print('Not enough trials in ' + str(eid) + ' , skipping...')
            continue


        ##### GLM-HMMM #####
        try: 
            if state_def == 'current' and n_states == 2: 
                engaged_idx, disengaged_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)

            elif state_def == 'previous' and n_states == 2:
                # engaged_idx = engaged_indices[current_mouse_ID][eid]
                # disengaged_idx = disengaged_indices[current_mouse_ID][eid]
                engaged_idx, disengaged_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
                engaged_idx = engaged_idx + 1
                disengaged_idx = disengaged_idx + 1
            elif state_def == 'current' and n_states == 4:
                state_1_idx, state_2_idx, state_3_idx, state_4_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
            elif state_def == 'previous' and n_states == 4:
                state_1_idx, state_2_idx, state_3_idx, state_4_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
                state_1_idx = state_1_idx[0] + 1
                state_2_idx = state_2_idx[0] + 1
                state_3_idx = state_3_idx[0] + 1
                state_4_idx = state_4_idx[0] + 1
                
        except:
            print(f'no glm-hmm state labels found for eid: {eid}. skipping session...')
            continue

        ####################

        if n_states == 2:
            if state_type == 'engaged':
                trials_range = np.intersect1d(engaged_idx, trials_range)
            elif state_type == 'disengaged':
                trials_range = np.intersect1d(disengaged_idx, trials_range)
            elif state_type == 'bypass':
                trials_range = trials_range
        else:
            if state_type == 'state1':
                trials_range = np.intersect1d(state_1_idx, trials_range)
            elif state_type == 'state2':
                trials_range = np.intersect1d(state_2_idx, trials_range)
            elif state_type == 'state3':
                trials_range = np.intersect1d(state_3_idx, trials_range)
            elif state_type == 'state4':
                trials_range = np.intersect1d(state_4_idx, trials_range)
            elif state_type == 'engaged':
                indices = np.concatenate([state_1_idx[0], state_3_idx[0]])
                trials_range = np.intersect1d(indices, trials_range)
            elif state_type == 'disengaged':
                indices = np.concatenate([state_2_idx[0], state_4_idx[0]])
                trials_range = np.intersect1d(indices, trials_range)
            elif state_type == 'bypass':
                trials_range = trials_range

        ### 2 different ways to extract what trials were laser trials; old versus new

        try:
            for k in trials_range:
                if taskData[k]['opto'] == 1:
                    react = trials['feedback_times'][k] - trials['goCue_times'][k]
                    if react < RT_threshold:
                        stim_trials_numbers[k] = k
                else:
                    react = trials['feedback_times'][k] - trials['goCue_times'][k]
                    if react < RT_threshold:
                        nonstim_trials_numbers[k] = k    
                                    
        except:
            laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
            for k in trials_range:#range(0,len(trials.intervals)):

                if stim_params[j] == 'QPRE':

                    if trials.intervals[k,0] in laser_intervals[:,0]:
                        react = trials['feedback_times'][k] - trials['goCue_times'][k]
                        if react < RT_threshold:  
                            stim_trials_numbers[k] = k
                    else:
                        react = trials['feedback_times'][k] - trials['goCue_times'][k]
                        if react < RT_threshold:
                            nonstim_trials_numbers[k] = k  

                elif stim_params[j] == 'SORE':

                    start_trial = trials.intervals[k, 0]
                    end_trial = trials.intervals[k, 1]

                    if np.any((laser_intervals[:, 0] >= start_trial) & (laser_intervals[:, 0] <= end_trial)):
                        react = trials['feedback_times'][k] - trials['goCue_times'][k]
                        if react < RT_threshold:  
                            stim_trials_numbers[k] = k
                    else:
                        react = trials['feedback_times'][k] - trials['goCue_times'][k]
                        if react < RT_threshold:
                            nonstim_trials_numbers[k] = k  

        # if state_def == 'previous':                         # TO DO: account for trials where stim was on 2 trials in a row !!
        #     prev_stim_trials_numbers = stim_trials_numbers -


        ##############
                            
        # modified_stim_trials = stim_trials_numbers.copy()

        # # Get indices of valid (non-NaN) values in nonstim_trials_numbers
        # valid_nonstim = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]

        # # Track the last found valid smaller value
        # previous_valid = np.nan

        # for i in range(len(stim_trials_numbers)):
        #     if not np.isnan(stim_trials_numbers[i]):  # Only process non-NaN values
        #         stim_value = stim_trials_numbers[i]

        #         # Find the nearest smaller and larger values
        #         smaller_values = valid_nonstim[valid_nonstim < stim_value]
        #         larger_values = valid_nonstim[valid_nonstim > stim_value]

        #         nearest_smaller = np.max(smaller_values) if smaller_values.size > 0 else np.nan
        #         nearest_larger = np.min(larger_values) if larger_values.size > 0 else np.nan

        #         # Determine which to use
        #         if not np.isnan(nearest_smaller) and abs(stim_value - nearest_smaller) <= 10:
        #             assigned_value = nearest_smaller  # Use nearest smaller if within 10
        #         elif not np.isnan(nearest_larger):  
        #             assigned_value = nearest_larger  # Otherwise, use nearest larger
        #         else:
        #             assigned_value = np.nan  # If nothing is found, keep NaN

        #         # Assign value if valid
        #         if not np.isnan(assigned_value):
        #             modified_stim_trials[i] = assigned_value

            

        #### TEST (^^) ####

        trials_numbers = np.concatenate((nonstim_trials_numbers,stim_trials_numbers))
        trials_numbers = trials_numbers[~np.isnan(trials_numbers)]
        stim_trials_numbers = stim_trials_numbers[~np.isnan(stim_trials_numbers)]
        nonstim_trials_numbers = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]
        stim_trials_numbers = stim_trials_numbers.astype(int)
        nonstim_trials_numbers = nonstim_trials_numbers.astype(int)
        trials_numbers = trials_numbers.astype(int)
        if only_include_bias_trials == 1:
            stim_trials_numbers = stim_trials_numbers[stim_trials_numbers>89]
            nonstim_trials_numbers = nonstim_trials_numbers[nonstim_trials_numbers>89]
            trials_numbers = trials_numbers[trials_numbers>89]
        if use_trials_after_stim == 1:
            for l in range(len(stim_trials_numbers)): 
                if l == len(stim_trials_numbers) - 1: 
                    if stim_trials_numbers[l] > nonstim_trials_numbers[len(nonstim_trials_numbers) - 1]:
                        stim_trials_numbers[l] = 9999
                        continue
                    else:
                        stim_trials_numbers[l] = stim_trials_numbers[l] + 1
                else:
                    if stim_trials_numbers[l+1] - stim_trials_numbers[l] == 1:
                        stim_trials_numbers[l] = 9999
                        continue
                    else:
                        stim_trials_numbers[l] = stim_trials_numbers[l] + 1

        stim_trials_numbers = stim_trials_numbers[stim_trials_numbers!=9999]
        rt_stimtrials = reaction_times[stim_trials_numbers]
        qp_stimtrials = quiescent_period_times[stim_trials_numbers]
        rt_nonstimtrials = reaction_times[nonstim_trials_numbers]
        qp_nonstimtrials = quiescent_period_times[nonstim_trials_numbers]

        ### remove all "stim" trials from nonstim trials
        nonstim_trials_numbers = np.setdiff1d(nonstim_trials_numbers, stim_trials_numbers)

        #for subsampling, maybe check on each iteration here if # L&R trials in each block is equal
        #alternatively, can take randomly equal number of trials from each and pool them together
        #ie, make 2 groups each block, RstimRblock, LstimRblock, LstimLblock, and RstimLblock
        #and subsample randomly equal amount of each for each block
        if subsample_trials_after_stim:
            Rblock_inds_stim = stim_trials_numbers[np.where(trials.probabilityLeft[stim_trials_numbers] == 0.2)[0]]
            Lblock_inds_stim = stim_trials_numbers[np.where(trials.probabilityLeft[stim_trials_numbers] == 0.8)[0]]
            PrevLchoice_inds_stim = stim_trials_numbers[np.where(trials.choice[stim_trials_numbers-1] == -1)[0]]
            PrevRchoice_inds_stim = stim_trials_numbers[np.where(trials.choice[stim_trials_numbers-1] == 1)[0]]
            ind_Lblock_Lprevchoice_stim = np.intersect1d(Lblock_inds_stim,PrevLchoice_inds_stim)
            ind_Lblock_Rprevchoice_stim = np.intersect1d(Lblock_inds_stim,PrevRchoice_inds_stim)
            ind_Rblock_Lprevchoice_stim = np.intersect1d(Rblock_inds_stim,PrevLchoice_inds_stim)
            ind_Rblock_Rprevchoice_stim = np.intersect1d(Rblock_inds_stim,PrevRchoice_inds_stim)

            if len(ind_Lblock_Lprevchoice_stim) > len(ind_Lblock_Rprevchoice_stim):
                subsample_indices_toremove_A = random.sample(list(ind_Lblock_Lprevchoice_stim), len(ind_Lblock_Lprevchoice_stim) - len(ind_Lblock_Rprevchoice_stim))
            elif len(ind_Lblock_Lprevchoice_stim) < len(ind_Lblock_Rprevchoice_stim):
                subsample_indices_toremove_A = random.sample(list(ind_Lblock_Rprevchoice_stim), len(ind_Lblock_Rprevchoice_stim) - len(ind_Lblock_Lprevchoice_stim))

            if len(ind_Rblock_Lprevchoice_stim) > len(ind_Rblock_Rprevchoice_stim):
                subsample_indices_toremove_B = random.sample(list(ind_Rblock_Lprevchoice_stim), len(ind_Rblock_Lprevchoice_stim) - len(ind_Rblock_Rprevchoice_stim))
            elif len(ind_Rblock_Lprevchoice_stim) < len(ind_Rblock_Rprevchoice_stim):
                subsample_indices_toremove_B = random.sample(list(ind_Rblock_Rprevchoice_stim), len(ind_Rblock_Rprevchoice_stim) - len(ind_Rblock_Lprevchoice_stim))

            subsample_indices_toremove = np.concatenate([subsample_indices_toremove_A,subsample_indices_toremove_B])
            # stim_trials_numbers_test = stim_trials_numbers
            for k in subsample_indices_toremove:
                # stim_trials_numbers_test = np.delete(stim_trials_numbers_test, np.where(stim_trials_numbers_test == k))
                stim_trials_numbers = np.delete(stim_trials_numbers, np.where(stim_trials_numbers == k))

        ###for quantifying ipsi/contraversive turns
        # Calculate bias index 
        nonstim_direction = trials.choice[nonstim_trials_numbers]
        nonstim_leftward = np.sum(nonstim_direction == 1)
        nonstim_rightward = np.sum(nonstim_direction == -1)
        nonstim_bias = (nonstim_rightward - nonstim_leftward) / len(nonstim_direction)

        stim_direction = trials.choice[stim_trials_numbers]
        stim_leftward = np.sum(stim_direction == 1)
        stim_rightward = np.sum(stim_direction == -1)
        stim_bias = (stim_rightward - stim_leftward) / len(stim_direction)

        # Effect size
        deviation.append(stim_bias - nonstim_bias) 


        ###for estimating bias shift
        stim_trials_temp = trials.copy()
        nonstim_trials_temp = trials.copy()
        stim_trials_temp.contrastRight = trials.contrastRight[stim_trials_numbers]
        stim_trials_temp.contrastLeft = trials.contrastLeft[stim_trials_numbers]
        stim_trials_temp.goCueTrigger_times = trials.goCueTrigger_times[stim_trials_numbers]
        stim_trials_temp.feedback_times = trials.feedback_times[stim_trials_numbers]
        stim_trials_temp.response_times = trials.response_times[stim_trials_numbers]
        stim_trials_temp.feedbackType = trials.feedbackType[stim_trials_numbers]
        stim_trials_temp.goCue_times = trials.goCue_times[stim_trials_numbers]
        stim_trials_temp.firstMovement_times = trials.firstMovement_times[stim_trials_numbers]
        stim_trials_temp.probabilityLeft = trials.probabilityLeft[stim_trials_numbers]
        stim_trials_temp.stimOn_times = trials.stimOn_times[stim_trials_numbers]
        stim_trials_temp.choice = trials.choice[stim_trials_numbers]
        stim_trials_temp.prev_choice = trials.choice[stim_trials_numbers-1]
        stim_trials_temp.rewardVolume = trials.rewardVolume[stim_trials_numbers]
        stim_trials_temp.intervals = trials.intervals[stim_trials_numbers]
        nonstim_trials_temp.contrastRight = trials.contrastRight[nonstim_trials_numbers]
        nonstim_trials_temp.contrastLeft = trials.contrastLeft[nonstim_trials_numbers]
        nonstim_trials_temp.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers]
        nonstim_trials_temp.feedback_times = trials.feedback_times[nonstim_trials_numbers]
        nonstim_trials_temp.response_times = trials.response_times[nonstim_trials_numbers]
        nonstim_trials_temp.feedbackType = trials.feedbackType[nonstim_trials_numbers]
        nonstim_trials_temp.goCue_times = trials.goCue_times[nonstim_trials_numbers]
        nonstim_trials_temp.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers]
        nonstim_trials_temp.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers]
        nonstim_trials_temp.stimOn_times = trials.stimOn_times[nonstim_trials_numbers]
        nonstim_trials_temp.choice = trials.choice[nonstim_trials_numbers]
        nonstim_trials_temp.prev_choice = trials.choice[nonstim_trials_numbers-1]
        nonstim_trials_temp.rewardVolume = trials.rewardVolume[nonstim_trials_numbers]
        nonstim_trials_temp.intervals = trials.intervals[nonstim_trials_numbers]
        stim_trials_temp_contrast = signed_contrast(stim_trials_temp)
        nonstim_trials_temp_contrast = signed_contrast(nonstim_trials_temp)

        nonstim_trialnums_HCR = np.where(nonstim_trials_temp_contrast == 100)[0]
        nonstim_trialnums_HCL = np.where(nonstim_trials_temp_contrast == -100)[0]
        num_correct_HCR = np.sum(nonstim_trials_temp.rewardVolume[nonstim_trialnums_HCR])/1.5
        num_correct_HCL = np.sum(nonstim_trials_temp.rewardVolume[nonstim_trialnums_HCL])/1.5

        stim_trialnums_HCR = np.where(stim_trials_temp_contrast == 100)[0]
        stim_trialnums_HCL = np.where(stim_trials_temp_contrast == -100)[0]
        stim_num_correct_HCR = np.sum(stim_trials_temp.rewardVolume[stim_trialnums_HCR])/1.5
        stim_num_correct_HCL = np.sum(stim_trials_temp.rewardVolume[stim_trialnums_HCL])/1.5

        all_signed_contrast = signed_contrast(trials)
        abs_signed_contrast = abs(all_signed_contrast)

        low_contrast_trials_bool_all = abs_signed_contrast < low_contrast_threshold

        if num_correct_HCR/np.size(nonstim_trialnums_HCR) < BL_perf_thresh or num_correct_HCL/np.size(nonstim_trialnums_HCL) < BL_perf_thresh:
            print(eid + ' below performance threshold, excluding...')
            continue
        if stim_num_correct_HCR/np.size(stim_trialnums_HCR) < stim_perf_thresh or stim_num_correct_HCL/np.size(stim_trialnums_HCL) < stim_perf_thresh:
            print(eid + ' below performance threshold, excluding...')
            continue

        #waitforbuttonpress

        ### for evaluating accuracy at low contrasts in stim vs nonstim conditions
        ### n = sessions
        ### currently, low contrasts == 0
        low_contrast_indices_stim = np.where(stim_trials_temp_contrast < 1)[0]
        low_contrast_indices_nonstim = np.where(nonstim_trials_temp_contrast < 1)[0]
        correct_indices_lowcontrast_stim = np.where(stim_trials_temp.feedbackType[low_contrast_indices_stim] == 1)[0]
        correct_indices_lowcontrast_nonstim = np.where(nonstim_trials_temp.feedbackType[low_contrast_indices_nonstim] == 1)[0]
        accuracy_lowcontrast_stim[j] = len(correct_indices_lowcontrast_stim)/len(low_contrast_indices_stim)
        accuracy_lowcontrast_nonstim[j] = len(correct_indices_lowcontrast_nonstim)/len(low_contrast_indices_nonstim)

        stim_trials_data = {}
        for pL in np.unique(stim_trials_temp.probabilityLeft):
            in_block = stim_trials_temp.probabilityLeft == pL
            xx, nn = np.unique(stim_trials_temp_contrast[in_block], return_counts=True)
            rightward = stim_trials_temp.choice == -1
            pp = np.vectorize(lambda x: np.mean(rightward[(x == stim_trials_temp_contrast) & in_block]))(xx)
            stim_trials_data[pL] = np.vstack((xx, nn, pp))

        nonstim_trials_data = {}
        for pL in np.unique(nonstim_trials_temp.probabilityLeft):
            in_block = nonstim_trials_temp.probabilityLeft == pL
            xx, nn = np.unique(nonstim_trials_temp_contrast[in_block], return_counts=True)
            rightward = nonstim_trials_temp.choice == -1
            pp = np.vectorize(lambda x: np.mean(rightward[(x == nonstim_trials_temp_contrast) & in_block]))(xx)
            nonstim_trials_data[pL] = np.vstack((xx, nn, pp))

        kwargs = {                                                                      # CONTROLS PSYCHOMETRIC FIT
            # parmin: The minimum allowable parameter values, in the form
            # [bias, threshold, lapse_low, lapse_high]
            'parmin': np.array([-25., 10., 0., 0.]),
            # parmax: The maximum allowable parameter values
            'parmax': np.array([100, 100., 1, 1]),
            # Non-zero starting parameters, used to try to avoid local minima
            'parstart': np.array([0., 40., .1, .1]),
            # nfits: The number of fits to run
            'nfits': 50
        }
        kwargs['parmin'][0] = -50.
        kwargs['parmax'][0] = 50.

        # For each block type, fit the data separately and plot
        for pL, da in nonstim_trials_data.items():
            # Fit it
            pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs); 

            if pL == 0.8:
                bias_80_value0 = psy.erf_psycho_2gammas(pars, 0)
                bias_80_valuen100 = psy.erf_psycho_2gammas(pars, -100)
                bias_80_valuen25 = psy.erf_psycho_2gammas(pars, -25)
                bias_80_valuen12 = psy.erf_psycho_2gammas(pars, -12)
                bias_80_valuen6 = psy.erf_psycho_2gammas(pars, -6)
                bias_80_value100 = psy.erf_psycho_2gammas(pars, 100)
                bias_80_value25 = psy.erf_psycho_2gammas(pars, 25)
                bias_80_value12 = psy.erf_psycho_2gammas(pars, 12)
                bias_80_value6 = psy.erf_psycho_2gammas(pars, 6)

            if pL == 0.2:
                bias_20_value0 = psy.erf_psycho_2gammas(pars, 0)
                bias_20_valuen100 = psy.erf_psycho_2gammas(pars, -100)
                bias_20_valuen25 = psy.erf_psycho_2gammas(pars, -25)
                bias_20_valuen12 = psy.erf_psycho_2gammas(pars, -12)
                bias_20_valuen6 = psy.erf_psycho_2gammas(pars, -6)
                bias_20_value100 = psy.erf_psycho_2gammas(pars, 100)
                bias_20_value25 = psy.erf_psycho_2gammas(pars, 25)
                bias_20_value12 = psy.erf_psycho_2gammas(pars, 12)
                bias_20_value6 = psy.erf_psycho_2gammas(pars, 6)


        bias_shift0 = bias_20_value0 - bias_80_value0
        bias_shiftn100 = bias_20_valuen100 - bias_80_valuen100
        bias_shiftn25 = bias_20_valuen25 - bias_80_valuen25
        bias_shiftn12 = bias_20_valuen12 - bias_80_valuen12
        bias_shiftn6 = bias_20_valuen6 - bias_80_valuen6
        bias_shift100 = bias_20_value100 - bias_80_value100
        bias_shift25 = bias_20_value25 - bias_80_value25
        bias_shift12 = bias_20_value12 - bias_80_value12
        bias_shift6 = bias_20_value6 - bias_80_value6
        bias_shift_sum_all_temp = sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6,bias_shift100,bias_shift25,bias_shift12,bias_shift6])
        if bias_shift_sum_all_temp < min_bias_threshold:
            print(eid + ' below minimum baseline bias threshold, excluding...')
            continue

        ## CHANGE HERE TO SWITCH between all vs low stim comparison --> high vs low stim
        bias_shift_sum_all_nonstim[j] = sum([bias_shiftn100,bias_shift100,bias_shiftn25,bias_shift25]) #bias_shift_sum_all_temp
        bias_shift_sum_all_nonstim_LC[j] = sum([bias_shift0,bias_shiftn12,bias_shiftn6,bias_shift12,bias_shift6])
        bias_shift0_all_nonstim[j] = bias_shift0
        bias_shift_sum_all_nonstim_LEFT[j] = sum([bias_shiftn100,bias_shiftn25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6])
        bias_shift_sum_all_nonstim_RIGHT[j] = sum([bias_shift100,bias_shift25]) #sum([bias_shift0,bias_shift100,bias_shift25,bias_shift12,bias_shift6])

        #     pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)

        for pL, da in stim_trials_data.items():
            # Fit it
            pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);

            if pL == 0.8:
                bias_80_value0 = psy.erf_psycho_2gammas(pars, 0)
                bias_80_valuen100 = psy.erf_psycho_2gammas(pars, -100)
                bias_80_valuen25 = psy.erf_psycho_2gammas(pars, -25)
                bias_80_valuen12 = psy.erf_psycho_2gammas(pars, -12)
                bias_80_valuen6 = psy.erf_psycho_2gammas(pars, -6)
                bias_80_value100 = psy.erf_psycho_2gammas(pars, 100)
                bias_80_value25 = psy.erf_psycho_2gammas(pars, 25)
                bias_80_value12 = psy.erf_psycho_2gammas(pars, 12)
                bias_80_value6 = psy.erf_psycho_2gammas(pars, 6)

            if pL == 0.2:
                bias_20_value0 = psy.erf_psycho_2gammas(pars, 0)
                bias_20_valuen100 = psy.erf_psycho_2gammas(pars, -100)
                bias_20_valuen25 = psy.erf_psycho_2gammas(pars, -25)
                bias_20_valuen12 = psy.erf_psycho_2gammas(pars, -12)
                bias_20_valuen6 = psy.erf_psycho_2gammas(pars, -6)
                bias_20_value100 = psy.erf_psycho_2gammas(pars, 100)
                bias_20_value25 = psy.erf_psycho_2gammas(pars, 25)
                bias_20_value12 = psy.erf_psycho_2gammas(pars, 12)
                bias_20_value6 = psy.erf_psycho_2gammas(pars, 6)


        bias_shift0 = bias_20_value0 - bias_80_value0
        bias_shiftn100 = bias_20_valuen100 - bias_80_valuen100
        bias_shiftn25 = bias_20_valuen25 - bias_80_valuen25
        bias_shiftn12 = bias_20_valuen12 - bias_80_valuen12
        bias_shiftn6 = bias_20_valuen6 - bias_80_valuen6
        bias_shift100 = bias_20_value100 - bias_80_value100
        bias_shift25 = bias_20_value25 - bias_80_value25
        bias_shift12 = bias_20_value12 - bias_80_value12
        bias_shift6 = bias_20_value6 - bias_80_value6

        # ALSO CHANGE HERE TO SWITCH BETWEEN ALL AND HIGH CONTRAST COMPARISONS
        bias_shift_sum_all[j] = sum([bias_shiftn100,bias_shift100,bias_shiftn25,bias_shift25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6,bias_shift100,bias_shift25,bias_shift12,bias_shift6])
        bias_shift_sum_all_LC[j] = sum([bias_shift0,bias_shiftn12,bias_shiftn6,bias_shift12,bias_shift6])
        bias_shift0_all_stim[j] = bias_shift0
        bias_shift_sum_all_LEFT[j] = sum([bias_shiftn100,bias_shiftn25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6])
        bias_shift_sum_all_RIGHT[j] = sum([bias_shift100,bias_shift25]) #sum([bias_shift0,bias_shift100,bias_shift25,bias_shift12,bias_shift6])

        #############################################################
        ##### Load wheel data
        if use_trials_after_stim == 0: ##wheel analysis not currently set up for stim+1 condition
            whlpos, whlt = wheel.position, wheel.timestamps

            for k in trials_numbers:#range(len(trials['contrastLeft'])):
                # trialnum = trials_numbers[k]
                trialnum = k

                if only_include_low_contrasts == 1:
                    if ~low_contrast_trials_bool_all[k]:
                        continue
                # print(str(trialnum))

                # start_time = taskData[trialnum]['behavior_data']['States timestamps']['trial_start'][0][0] - 0.03 #quiescent period - first 30ms step
                # start_time = taskData[trialnum]['behavior_data']['States timestamps']['reward'][0][0] - 0.5 #reward/error
                # if np.isnan(start_time) == 1:
                #     start_time = taskData[trialnum]['behavior_data']['States timestamps']['error'][0][0] - 0.5

                if align_to == 'goCue':
                    start_time = trials.goCue_times[trialnum] #GO CUE
                elif align_to == 'goCue_pre':
                    start_time = trials.goCue_times[trialnum] - 0.5 #GO CUE - 0.5s
                elif align_to == 'QP':
                    start_time = trials.intervals[trialnum][0] #QP / Laser onset
                elif align_to == 'feedback':
                    start_time = trials.feedback_times[trialnum] - 0.6

                wheel_start_index_pre = np.searchsorted(whlt, start_time)
                t = start_time
                # Check the closest value by comparing the differences between 't' and its neighboring elements
                if wheel_start_index_pre == 0:
                    wheel_start_index = wheel_start_index_pre
                elif wheel_start_index_pre == len(whlt):
                    wheel_start_index = wheel_start_index_pre - 1
                else:
                    left_diff = t - whlt[wheel_start_index_pre - 1]
                    right_diff = whlt[wheel_start_index_pre] - t
                    wheel_start_index = wheel_start_index_pre - 1 if left_diff <= right_diff else wheel_start_index_pre


                total_wheel_movement = []
                for l in range(int(length_of_time_to_analyze_wheel_movement/interval)):
                    t = (start_time + l*interval)# + interval #ie, steps of 100ms
                    # wheel_end_index = np.argmin(np.abs(whlt - t))
                    #norm_wheel_vals = whlpos[wheel_start_index:wheel_end_index]/whlpos[wheel_start_index]

                    wheel_end_index_pre = np.searchsorted(whlt, t) #ie, steps of 100ms
                    # Check the closest value by comparing the differences between 't' and its neighboring elements
                    if wheel_end_index_pre == 0:
                        wheel_end_index = wheel_end_index_pre
                    elif wheel_end_index_pre == len(whlt):
                        wheel_end_index = wheel_end_index_pre - 1
                    else:
                        left_diff = t - whlt[wheel_end_index_pre - 1]
                        right_diff = whlt[wheel_end_index_pre] - t
                        wheel_end_index = wheel_end_index_pre - 1 if left_diff <= right_diff else wheel_end_index_pre

                    ##only in case where aligning to QP, do not use any wheel movement past goCue
                    if align_to == 'QP' and trials.goCue_times[trialnum] < whlt[wheel_end_index]:
                        total_wheel_movement = np.append(total_wheel_movement,np.nan)
                    ##only in case where aligning to goCue, do not use any wheel movement past feedback + 0.1
                    elif align_to == 'goCue' and (trials.feedback_times[trialnum] + interval) < whlt[wheel_end_index]:
                        total_wheel_movement = np.append(total_wheel_movement,np.nan)
                    elif align_to == 'goCue_pre' and (trials.feedback_times[trialnum] + interval) < whlt[wheel_end_index]:
                        total_wheel_movement = np.append(total_wheel_movement,np.nan)
                    else:
                        total_wheel_movement = np.append(total_wheel_movement,whlpos[wheel_end_index] - whlpos[wheel_start_index])

                #determine whether trial is a stim or nonstim trial
                #nonstim
                if np.isin(trialnum,nonstim_trials_numbers):
                    if trials.probabilityLeft[trialnum] == 0.2:
                        if len(Rblock_wheel_movements_nonstim) == 0:
                            Rblock_wheel_movements_nonstim = total_wheel_movement
                        else:
                            Rblock_wheel_movements_nonstim = np.vstack([Rblock_wheel_movements_nonstim,total_wheel_movement])
                    if trials.probabilityLeft[trialnum] == 0.8:
                        if len(Lblock_wheel_movements_nonstim) == 0:
                            Lblock_wheel_movements_nonstim = total_wheel_movement
                        else:
                            Lblock_wheel_movements_nonstim = np.vstack([Lblock_wheel_movements_nonstim,total_wheel_movement])
                #stim
                elif np.isin(trialnum,stim_trials_numbers):
                    if trials.probabilityLeft[trialnum] == 0.2:
                        if  len(Rblock_wheel_movements_stim) == 0:
                            Rblock_wheel_movements_stim = total_wheel_movement
                        else:
                            Rblock_wheel_movements_stim = np.vstack([Rblock_wheel_movements_stim,total_wheel_movement])
                    if trials.probabilityLeft[trialnum] == 0.8:
                        if len(Lblock_wheel_movements_stim) == 0:
                            Lblock_wheel_movements_stim = total_wheel_movement
                        else:
                            Lblock_wheel_movements_stim = np.vstack([Lblock_wheel_movements_stim,total_wheel_movement])
                else:
                    raise Exception('Trials must be either stim or nonstim; something is wrong')
        #############################################################

        if num_analyzed_sessions == 0:
            stim_trials.contrastRight = trials.contrastRight[stim_trials_numbers]
            stim_trials.contrastLeft = trials.contrastLeft[stim_trials_numbers]
            stim_trials.goCueTrigger_times = trials.goCueTrigger_times[stim_trials_numbers]
            stim_trials.feedback_times = trials.feedback_times[stim_trials_numbers]
            stim_trials.response_times = trials.response_times[stim_trials_numbers]
            stim_trials.feedbackType = trials.feedbackType[stim_trials_numbers]
            stim_trials.goCue_times = trials.goCue_times[stim_trials_numbers]
            stim_trials.firstMovement_times = trials.firstMovement_times[stim_trials_numbers]
            stim_trials.probabilityLeft = trials.probabilityLeft[stim_trials_numbers]
            stim_trials.stimOn_times = trials.stimOn_times[stim_trials_numbers]
            stim_trials.choice = trials.choice[stim_trials_numbers]
            stim_trials.prev_choice = trials.choice[stim_trials_numbers-1]
            stim_trials.rewardVolume = trials.rewardVolume[stim_trials_numbers]
            stim_trials.intervals = trials.intervals[stim_trials_numbers]
            stim_trials.reaction_times = stim_trials.feedback_times - stim_trials.stimOn_times
            nonstim_trials.contrastRight = trials.contrastRight[nonstim_trials_numbers]
            nonstim_trials.contrastLeft = trials.contrastLeft[nonstim_trials_numbers]
            nonstim_trials.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers]
            nonstim_trials.feedback_times = trials.feedback_times[nonstim_trials_numbers]
            nonstim_trials.response_times = trials.response_times[nonstim_trials_numbers]
            nonstim_trials.feedbackType = trials.feedbackType[nonstim_trials_numbers]
            nonstim_trials.goCue_times = trials.goCue_times[nonstim_trials_numbers]
            nonstim_trials.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers]
            nonstim_trials.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers]
            nonstim_trials.stimOn_times = trials.stimOn_times[nonstim_trials_numbers]
            nonstim_trials.choice = trials.choice[nonstim_trials_numbers]
            nonstim_trials.prev_choice = trials.choice[nonstim_trials_numbers-1]
            nonstim_trials.rewardVolume = trials.rewardVolume[nonstim_trials_numbers]
            nonstim_trials.intervals = trials.intervals[nonstim_trials_numbers]
            nonstim_trials.reaction_times = nonstim_trials.feedback_times - nonstim_trials.stimOn_times
            stim_trials_contrast = signed_contrast(stim_trials)
            nonstim_trials_contrast = signed_contrast(nonstim_trials)
            rt_stimtrials_all = rt_stimtrials
            qp_stimtrials_all = qp_stimtrials
            rt_nonstimtrials_all = rt_nonstimtrials
            qp_nonstimtrials_all = qp_nonstimtrials
            rt_stimtrials_all_persubject = np.nanmean(rt_stimtrials)
            qp_stimtrials_all_persubject = np.nanmean(qp_stimtrials)
            rt_nonstimtrials_all_persubject = np.nanmean(rt_nonstimtrials)
            qp_nonstimtrials_all_persubject = np.nanmean(qp_nonstimtrials)
            num_analyzed_sessions = 1
            num_unique_mice = 1
            previous_mouse_ID = current_mouse_ID
        else:
            stim_trials.contrastRight = np.append(stim_trials.contrastRight,trials.contrastRight[stim_trials_numbers])
            stim_trials.contrastLeft = np.append(stim_trials.contrastLeft,trials.contrastLeft[stim_trials_numbers])
            stim_trials.goCueTrigger_times = np.append(stim_trials.goCueTrigger_times,trials.goCueTrigger_times[stim_trials_numbers])
            stim_trials.feedback_times = np.append(stim_trials.feedback_times,trials.feedback_times[stim_trials_numbers])
            stim_trials.response_times = np.append(stim_trials.response_times,trials.response_times[stim_trials_numbers])
            stim_trials.feedbackType = np.append(stim_trials.feedbackType,trials.feedbackType[stim_trials_numbers])
            stim_trials.goCue_times = np.append(stim_trials.goCue_times,trials.goCue_times[stim_trials_numbers])
            stim_trials.firstMovement_times = np.append(stim_trials.firstMovement_times,trials.firstMovement_times[stim_trials_numbers])
            stim_trials.probabilityLeft = np.append(stim_trials.probabilityLeft,trials.probabilityLeft[stim_trials_numbers])
            stim_trials.stimOn_times = np.append(stim_trials.stimOn_times,trials.stimOn_times[stim_trials_numbers])
            stim_trials.choice = np.append(stim_trials.choice,trials.choice[stim_trials_numbers])
            stim_trials.prev_choice = np.append(stim_trials.prev_choice,trials.choice[stim_trials_numbers-1])
            stim_trials.rewardVolume = np.append(stim_trials.rewardVolume,trials.rewardVolume[stim_trials_numbers])
            stim_trials.intervals = np.append(stim_trials.intervals,trials.intervals[stim_trials_numbers])
            stim_trials.reaction_times = np.append(stim_trials.reaction_times,trials.feedback_times[stim_trials_numbers] - trials.stimOn_times[stim_trials_numbers])
            nonstim_trials.contrastRight = np.append(nonstim_trials.contrastRight,trials.contrastRight[nonstim_trials_numbers])
            nonstim_trials.contrastLeft = np.append(nonstim_trials.contrastLeft,trials.contrastLeft[nonstim_trials_numbers])
            nonstim_trials.goCueTrigger_times = np.append(nonstim_trials.goCueTrigger_times,trials.goCueTrigger_times[nonstim_trials_numbers])
            nonstim_trials.feedback_times = np.append(nonstim_trials.feedback_times,trials.feedback_times[nonstim_trials_numbers])
            nonstim_trials.response_times = np.append(nonstim_trials.response_times,trials.response_times[nonstim_trials_numbers])
            nonstim_trials.feedbackType = np.append(nonstim_trials.feedbackType,trials.feedbackType[nonstim_trials_numbers])
            nonstim_trials.goCue_times = np.append(nonstim_trials.goCue_times,trials.goCue_times[nonstim_trials_numbers])
            nonstim_trials.firstMovement_times = np.append(nonstim_trials.firstMovement_times,trials.firstMovement_times[nonstim_trials_numbers])
            nonstim_trials.probabilityLeft = np.append(nonstim_trials.probabilityLeft,trials.probabilityLeft[nonstim_trials_numbers])
            nonstim_trials.stimOn_times = np.append(nonstim_trials.stimOn_times,trials.stimOn_times[nonstim_trials_numbers])
            nonstim_trials.choice = np.append(nonstim_trials.choice,trials.choice[nonstim_trials_numbers])
            nonstim_trials.prev_choice = np.append(nonstim_trials.prev_choice,trials.choice[nonstim_trials_numbers-1])
            nonstim_trials.rewardVolume = np.append(nonstim_trials.rewardVolume,trials.rewardVolume[nonstim_trials_numbers])
            nonstim_trials.intervals = np.append(nonstim_trials.intervals,trials.intervals[nonstim_trials_numbers])
            nonstim_trials.reaction_times = np.append(nonstim_trials.reaction_times,trials.feedback_times[nonstim_trials_numbers] - trials.stimOn_times[nonstim_trials_numbers])
            # stim_trials_contrast = np.append(stim_trials_contrast,signed_contrast(stim_trials))
            # nonstim_trials_contrast = np.append(nonstim_trials_contrast,signed_contrast(nonstim_trials)) #??? check this
            rt_stimtrials_all = np.append(rt_stimtrials_all,rt_stimtrials)
            qp_stimtrials_all = np.append(qp_stimtrials_all,qp_stimtrials)
            rt_nonstimtrials_all = np.append(rt_nonstimtrials_all,rt_nonstimtrials)
            qp_nonstimtrials_all = np.append(qp_nonstimtrials_all,qp_nonstimtrials)

            rt_stimtrials_all_persubject = np.append(rt_stimtrials_all_persubject,np.nanmean(rt_stimtrials))
            qp_stimtrials_all_persubject = np.append(qp_stimtrials_all_persubject,np.nanmean(qp_stimtrials))
            rt_nonstimtrials_all_persubject = np.append(rt_nonstimtrials_all_persubject,np.nanmean(rt_nonstimtrials))
            qp_nonstimtrials_all_persubject = np.append(qp_nonstimtrials_all_persubject,np.nanmean(qp_nonstimtrials))
            num_analyzed_sessions = num_analyzed_sessions + 1
            if previous_mouse_ID != current_mouse_ID:
                num_unique_mice = num_unique_mice + 1
                previous_mouse_ID = current_mouse_ID


    ############################################ the following is analysis for zapit sessions
    ########################################################################################
    else:
        laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')

        if trials_ranges[j] == 'ALL':
            trials_range = range(0,len(trials['contrastLeft']))
        #### use last trial as end of range when end of range set to 9999
        elif trials_ranges[j][-1] == 9998:
            trials_range = [x for x in trials_ranges[j] if x < np.size(trials.probabilityLeft)]
        else:
            trials_range = trials_ranges[j]
        # if remove_trials_before > 0 and j < loop_threshold_for_remove:
        #     trials_range = list(np.array(trials_range)[np.where(np.array(trials_range) > remove_trials_before)[0]])
        # if len(trials_range) < min_num_trials:
        #     print('Not enough trials in ' + str(eid) + ' , skipping...')
        #     continue

        ### load GLM HMM state labels and restrict trials range
        try: 
            if state_def == 'current' and n_states == 2: 
                engaged_idx, disengaged_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)

            elif state_def == 'previous' and n_states == 2:
                # engaged_idx = engaged_indices[current_mouse_ID][eid]
                # disengaged_idx = disengaged_indices[current_mouse_ID][eid]
                engaged_idx, disengaged_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
                engaged_idx = engaged_idx + 1
                disengaged_idx = disengaged_idx + 1
            elif state_def == 'current' and n_states == 4:
                state_1_idx, state_2_idx, state_3_idx, state_4_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
            elif state_def == 'previous' and n_states == 4:
                state_1_idx, state_2_idx, state_3_idx, state_4_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)
                state_1_idx = state_1_idx[0] + 1
                state_2_idx = state_2_idx[0] + 1
                state_3_idx = state_3_idx[0] + 1
                state_4_idx = state_4_idx[0] + 1
                
        except:
            print(f'no glm-hmm state labels found for eid: {eid}. skipping session...')
            continue

        ####################

        if n_states == 2:
            if state_type == 'engaged':
                trials_range = np.intersect1d(engaged_idx, trials_range)
            elif state_type == 'disengaged':
                trials_range = np.intersect1d(disengaged_idx, trials_range)
            elif state_type == 'bypass':
                trials_range = trials_range
        else:
            if state_type == 'state1':
                trials_range = np.intersect1d(state_1_idx, trials_range)
            elif state_type == 'state2':
                trials_range = np.intersect1d(state_2_idx, trials_range)
            elif state_type == 'state3':
                trials_range = np.intersect1d(state_3_idx, trials_range)
            elif state_type == 'state4':
                trials_range = np.intersect1d(state_4_idx, trials_range)
            elif state_type == 'engaged':
                indices = np.concatenate([state_1_idx[0], state_3_idx[0]])
                trials_range = np.intersect1d(indices, trials_range)
            elif state_type == 'disengaged':
                indices = np.concatenate([state_2_idx[0], state_4_idx[0]])
                trials_range = np.intersect1d(indices, trials_range)
            elif state_type == 'bypass':
                trials_range = trials_range

        ############################## zapit stim locations log
        file_path = '/Users/natemiska/python/bias_coding/zapit_trials.yml'

        details = one.get_details(eid)
        exp_start_time_str = details['start_time']

        if eid == '21d33b44-f75f-4711-a2c7-0bdfe8eec386': #strange issue with logged stims in this session
            exp_start_time_str = '2024-03-29T18:07:38.0'

        # Convert session start to datetime object
        session_start = datetime.strptime(exp_start_time_str[0:19], '%Y-%m-%dT%H:%M:%S')

        event_num = 0
        line_num = 0
        with open(file_path, 'r') as file:
            # Skip the first line
            next(file)
            # List to hold events that occur during or after the session start
            relevant_events = []
            for line in file:
                if line_num > 211510:
                    continue
                    ### encountering a weird fucking error where the 2nd to last line of the yml file is being interpreted as '/n'?? Dunno where this is coming from as it's not in the file itself as far as i can see
                # Extract the timestamp part from the line and convert it to a datetime object
                # Assuming the format is always "YYYY-MM-DD HH:MM:SS", which corresponds to the first 19 characters
                event_timestamp_str = line[:19]
                # print(event_timestamp_str)
                event_timestamp = datetime.strptime(event_timestamp_str, '%Y-%m-%d %H:%M:%S')
                line_num = line_num + 1
                
                # Check if the event timestamp is equal to or later than the session start
                if event_timestamp >= session_start:
                    relevant_events.append(line.strip())  # Add event line to the list, stripping newline characters

            event_num = event_num + 1

        # # Now, relevant_events contains all the lines for events during or after the session start
        # for event in relevant_events:
        #     print(event)
        ######################### end zapit log load
            
        ### Loop that extracts trial number and stim location for each laser stim
        stimtrial_location_dict = {}
        previous_logged_timestamp = datetime.strptime(relevant_events[0][:19], '%Y-%m-%d %H:%M:%S')
        previous_laser_interval = laser_intervals[0,0]
        for k in range(0,len(laser_intervals[:,0]) - 2): #loop is num of laser stim for session
            if k == 0:
                continue
                #1st stim can be before 1st trial?
            elif eid == '21d33b44-f75f-4711-a2c7-0bdfe8eec386' and k < 10: #strange issue with logged stims in this session
                continue
            else:
                trialnum = np.where(laser_intervals[k,0]==trials.intervals[:,0])[0][0]
                stim_location = relevant_events[k][20:22]
                cleaned_stim_location = int(re.sub(r'\D', '', stim_location))
                stimtrial_location_dict[trialnum] = cleaned_stim_location
                logged_time = relevant_events[k][0:19]
                if eid == '5a41494f-25b9-48d4-8159-527141bd4742': #strange exception where logged events off by 1 starting ~trial 11
                    logged_time = relevant_events[k-1][0:19]
                logged_timestamp = event_timestamp = datetime.strptime(logged_time, '%Y-%m-%d %H:%M:%S')
                # print('trial number = ' + str(trialnum))
                # print('laser interval = ' + str(laser_intervals[k,0]))
                # print('logged time = ' + logged_time)

                delta = logged_timestamp - previous_logged_timestamp
                delta_log = delta.total_seconds()
                # print('delta log = ' + str(delta_log))
                delta_interval = laser_intervals[k,0] - previous_laser_interval
                # print('delta interval = ' + str(delta_interval))
                # if abs(delta_log - delta_interval) > 1:
                #     print('Warning, laser log may be incorrect for trial ' + str(trialnum))
                #     ui = input("Press Enter to continue, e to exit...")
                #     if ui == 'e':
                #         raise Exception('Script terminated by user')
            
                previous_laser_interval = laser_intervals[k,0]
                previous_logged_timestamp = logged_timestamp


        stimtrial_location_dict_all = {k: 0 for k in trials_range}
        stimtrial_location_dict_all.update(stimtrial_location_dict)

        ### make new dict that simply adds 1 to each key
        if use_trials_after_stim == 1:
            stimtrial_location_dict_OG = stimtrial_location_dict_all
            stimtrial_location_dict_all = {key + 1: value for key, value in stimtrial_location_dict_all.items() if np.min(trials_range) <= key < np.max(trials_range)}



        ####################################################################################
        ### for removing whole session if it does not meet behavioral criteria
        session_data_nonstim = {i: [] for i in range(0, 1)}
        if use_trials_after_stim == 1:
            trials_with_condition_zero = [trial for trial, condition in stimtrial_location_dict_OG.items() if condition == 0]  ###need to make sure this propogates
        else:
            trials_with_condition_zero = [trial for trial, condition in stimtrial_location_dict_all.items() if condition == 0]
        for trial_number in trials_with_condition_zero:
            # reaction_time = trials.feedback_times[trial_number] - trials.goCueTrigger_times[trial_number]  #depricated
            # if np.isnan(reaction_time) == 1:
            reaction_time = trials.feedback_times[trial_number] - trials.goCue_times[trial_number] ###reaction time definitions may be unreliable - any other ways to define?

            trials_data = {
                'choice': trials.choice[trial_number],
                'reaction_times': reaction_time,
                'qp_times': trials.goCue_times[trial_number] - trials.intervals[trial_number][0],
                'contrast': signed_contrast(trials)[trial_number],
                'feedbackType': trials.feedbackType[trial_number],
                'probabilityLeft': trials.probabilityLeft[trial_number],
                # 'prev_choice': trials.choice[trial_number-1]
            }
            session_data_nonstim[0].append(trials_data)

        nonstim_feedback = [trial['feedbackType'] for trial in session_data_nonstim[0] if trial['contrast'] in (-100, -25, 25, 100)]
        correct_rate_nonstim = np.sum(np.array(nonstim_feedback) == 1) / len(nonstim_feedback)
        print('Accuracy at high contrasts = ' + str(correct_rate_nonstim))
        if correct_rate_nonstim < BL_perf_thresh:
            print('Session eid = ' + eid + ' is below minimum performance threshold, skipping...')
            continue

        # create criteria for minimum bias session
        choices_L100_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -100 and trial['probabilityLeft'] == 0.8]
        choices_L25_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -25 and trial['probabilityLeft'] == 0.8]
        choices_L12_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -12.5 and trial['probabilityLeft'] == 0.8]
        choices_L6_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -6.25 and trial['probabilityLeft'] == 0.8]
        choices_0_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 0 and trial['probabilityLeft'] == 0.8]
        choices_R6_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 6.25 and trial['probabilityLeft'] == 0.8]
        choices_R12_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 12.5 and trial['probabilityLeft'] == 0.8]
        choices_R25_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 25 and trial['probabilityLeft'] == 0.8]
        choices_R100_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 100 and trial['probabilityLeft'] == 0.8]
        choices_L100_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -100 and trial['probabilityLeft'] == 0.2]
        choices_L25_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -25 and trial['probabilityLeft'] == 0.2]
        choices_L12_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -12.5 and trial['probabilityLeft'] == 0.2]
        choices_L6_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -6.25 and trial['probabilityLeft'] == 0.2]
        choices_0_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 0 and trial['probabilityLeft'] == 0.2]
        choices_R6_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 6.25 and trial['probabilityLeft'] == 0.2]
        choices_R12_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 12.5 and trial['probabilityLeft'] == 0.2]
        choices_R25_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 25 and trial['probabilityLeft'] == 0.2]
        choices_R100_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 100 and trial['probabilityLeft'] == 0.2]

        biasshift_L100 = np.sum(np.array(choices_L100_Lblock) == 1)/len(choices_L100_Lblock) - np.sum(np.array(choices_L100_Rblock) == 1)/len(choices_L100_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_L25 = np.sum(np.array(choices_L25_Lblock) == 1)/len(choices_L25_Lblock) - np.sum(np.array(choices_L25_Rblock) == 1)/len(choices_L25_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_L12 = np.sum(np.array(choices_L12_Lblock) == 1)/len(choices_L12_Lblock) - np.sum(np.array(choices_L12_Rblock) == 1)/len(choices_L12_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_L6 = np.sum(np.array(choices_L6_Lblock) == 1)/len(choices_L6_Lblock) - np.sum(np.array(choices_L6_Rblock) == 1)/len(choices_L6_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_0 = np.sum(np.array(choices_0_Lblock) == 1)/len(choices_0_Lblock) - np.sum(np.array(choices_0_Rblock) == 1)/len(choices_0_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_R6 = np.sum(np.array(choices_R6_Lblock) == 1)/len(choices_R6_Lblock) - np.sum(np.array(choices_R6_Rblock) == 1)/len(choices_R6_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_R12 = np.sum(np.array(choices_R12_Lblock) == 1)/len(choices_R12_Lblock) - np.sum(np.array(choices_R12_Rblock) == 1)/len(choices_R12_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_R25 = np.sum(np.array(choices_R25_Lblock) == 1)/len(choices_R25_Lblock) - np.sum(np.array(choices_R25_Rblock) == 1)/len(choices_R25_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0
        biasshift_R100 = np.sum(np.array(choices_R100_Lblock) == 1)/len(choices_R100_Lblock) - np.sum(np.array(choices_R100_Rblock) == 1)/len(choices_R100_Rblock)
        if np.isnan(biasshift_L100) == 1:
            biasshift_L100 = 0

        total_biasshift = biasshift_L100 + biasshift_L25 + biasshift_L12 + biasshift_L6 + biasshift_0 + biasshift_R6 + biasshift_R12 + biasshift_R25 + biasshift_R100
        print('Total bias shift = ' + str(total_biasshift))
        if total_biasshift < min_bias_threshold_zapit:
            print('Bias shift for session below threshold, skipping...')
            continue


        ####### creating a new dict to separate trials data by stim location        
        ####### this formats the data in an easily accessible manner w/ conditions_data
        ####### Loop over all trials and sort them into the condition_data dictionary
        ####### Also, extract and save wheel data within this loop

        whlpos, whlt = wheel.position, wheel.timestamps

        for trial_number, condition_number in stimtrial_location_dict_all.items():
            # print(str(trial_number) + ' ' + str(condition_number))

            reaction_time = trials.feedback_times[trial_number] - trials.goCue_times[trial_number] 
            if np.isnan(reaction_time) == 1:
                if np.isnan(RT_threshold) == 0:
                    continue
            if reaction_time > RT_threshold:
                if np.isnan(RT_threshold) == 0:
                    continue

            trials_data = {
                # 'intervals': trials.intervals[trial_number],
                'choice': trials.choice[trial_number],
                'reaction_times': reaction_time,
                'qp_times': trials.goCue_times[trial_number] - trials.intervals[trial_number][0],
                'contrast': signed_contrast(trials)[trial_number],
                # 'goCueTrigger_times': trials.goCueTrigger_times[trial_number],
                # 'goCue_times': trials.goCue_times[trial_number],
                # 'stimOn_times': trials.stimOn_times[trial_number],
                # 'feedback_times': trials.feedback_times[trial_number],
                # 'response_times': trials.response_times[trial_number],
                'feedbackType': trials.feedbackType[trial_number],
                'probabilityLeft': trials.probabilityLeft[trial_number],
                # 'prev_choice': trials.choice[trial_number-1]
            }
            
            # Append the trial data to the correct condition
            condition_data[condition_number].append(trials_data)

            # Now condition_data[1] contains all trials for location 1, condition_data[2] for location 2, and so on
            # condition_data[0] contains all nonstim trials

            #############################################################
            ##### Load wheel data

            if only_include_low_contrasts == 1:
                if ~low_contrast_trials_bool_all[k]:
                    continue
            # start_time = taskData[trial_number]['behavior_data']['States timestamps']['trial_start'][0][0] - 0.03 #quiescent period - first 30ms step
            # start_time = taskData[trial_number]['behavior_data']['States timestamps']['reward'][0][0] - 0.5 #reward/error
            # if np.isnan(start_time) == 1:
            #     start_time = taskData[trial_number]['behavior_data']['States timestamps']['error'][0][0] - 0.5

            if align_to == 'goCue':
                start_time = trials.goCue_times[trial_number] #GO CUE
            elif align_to == 'goCue_pre':
                start_time = trials.goCue_times[trial_number] - 0.5 #GO CUE - 0.5s
            elif align_to == 'QP':
                start_time = trials.intervals[trial_number][0] #QP / Laser onset
            elif align_to == 'feedback':
                start_time = trials.feedback_times[trial_number] - 0.6

            wheel_start_index_pre = np.searchsorted(whlt, start_time)
            t = start_time
            # Check the closest value by comparing the differences between 't' and its neighboring elements
            if wheel_start_index_pre == 0:
                wheel_start_index = wheel_start_index_pre
            elif wheel_start_index_pre == len(whlt):
                wheel_start_index = wheel_start_index_pre - 1
            else:
                left_diff = t - whlt[wheel_start_index_pre - 1]
                right_diff = whlt[wheel_start_index_pre] - t
                wheel_start_index = wheel_start_index_pre - 1 if left_diff <= right_diff else wheel_start_index_pre


            total_wheel_movement = []
            for l in range(int(length_of_time_to_analyze_wheel_movement/interval)):
                t = (start_time + l*interval)# + interval #ie, steps of 100ms
                # wheel_end_index = np.argmin(np.abs(whlt - t))
                #norm_wheel_vals = whlpos[wheel_start_index:wheel_end_index]/whlpos[wheel_start_index]

                wheel_end_index_pre = np.searchsorted(whlt, t) #ie, steps of 100ms
                # Check the closest value by comparing the differences between 't' and its neighboring elements
                if wheel_end_index_pre == 0:
                    wheel_end_index = wheel_end_index_pre
                elif wheel_end_index_pre == len(whlt):
                    wheel_end_index = wheel_end_index_pre - 1
                else:
                    left_diff = t - whlt[wheel_end_index_pre - 1]
                    right_diff = whlt[wheel_end_index_pre] - t
                    wheel_end_index = wheel_end_index_pre - 1 if left_diff <= right_diff else wheel_end_index_pre

                ##only in case where aligning to QP, do not use any wheel movement past goCue
                if align_to == 'QP' and trials.goCue_times[trial_number] < whlt[wheel_end_index]:
                    total_wheel_movement = np.append(total_wheel_movement,np.nan)
                ##only in case where aligning to goCue, do not use any wheel movement past feedback + 0.1
                elif align_to == 'goCue' and (trials.feedback_times[trial_number] + interval) < whlt[wheel_end_index]:
                    total_wheel_movement = np.append(total_wheel_movement,np.nan)
                elif align_to == 'goCue_pre' and (trials.feedback_times[trial_number] + interval) < whlt[wheel_end_index]:
                    total_wheel_movement = np.append(total_wheel_movement,np.nan)
                else:
                    total_wheel_movement = np.append(total_wheel_movement,whlpos[wheel_end_index] - whlpos[wheel_start_index])

            ### append data here according to condition
            if trials.probabilityLeft[trial_number] == 0.2:
                if len(Rblock_wheel_movements_by_condition[condition_number]) == 0:
                    Rblock_wheel_movements_by_condition[condition_number] = total_wheel_movement
                else:
                    Rblock_wheel_movements_by_condition[condition_number] = np.vstack([Rblock_wheel_movements_by_condition[condition_number],total_wheel_movement])
            if trials.probabilityLeft[trial_number] == 0.8:
                if len(Lblock_wheel_movements_by_condition[condition_number]) == 0:
                    Lblock_wheel_movements_by_condition[condition_number] = total_wheel_movement
                else:
                    Lblock_wheel_movements_by_condition[condition_number] = np.vstack([Lblock_wheel_movements_by_condition[condition_number],total_wheel_movement])
        #############################################################
            
        # ####################################################################################
            



if is_zapit_session == 0:
    if num_analyzed_sessions == 0:
        raise Exception('No sessions met criteria to be analyzed.')
    
    # RT_threshold = 2
    # # Create a boolean mask based on the reaction times
    # mask = stim_trials.reaction_times <= RT_threshold
    # for key in stim_trials.__dict__.keys():
    #     stim_trials.__dict__[key] = stim_trials.__dict__[key][mask]

    # mask = nonstim_trials.reaction_times <= RT_threshold
    # for key in nonstim_trials.__dict__.keys():
    #     nonstim_trials.__dict__[key] = nonstim_trials.__dict__[key][mask]


    stim_trials_contrast = signed_contrast(stim_trials)
    nonstim_trials_contrast = signed_contrast(nonstim_trials)
    nonstim_RTs_100L = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastLeft == 1)[0]]
    nonstim_RTs_100R = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastRight == 1)[0]]
    nonstim_RTs_100all = np.append(nonstim_RTs_100L,nonstim_RTs_100R)
    nonstim_RTs_25L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -25)[0]]
    nonstim_RTs_25R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 25)[0]]
    nonstim_RTs_25all = np.append(nonstim_RTs_25L,nonstim_RTs_25R)
    nonstim_RTs_12L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -12.5)[0]]
    nonstim_RTs_12R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 12)[0]]
    nonstim_RTs_12all = np.append(nonstim_RTs_12L,nonstim_RTs_12R)
    nonstim_RTs_6L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -6.25)[0]]
    nonstim_RTs_6R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 6.25)[0]]
    nonstim_RTs_6all = np.append(nonstim_RTs_6L,nonstim_RTs_6R)
    nonstim_RTs_0L = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastLeft == 0)[0]]
    nonstim_RTs_0R = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastRight == 0)[0]]
    nonstim_RTs_0all = np.append(nonstim_RTs_0L,nonstim_RTs_0R)
    stim_RTs_100L = stim_trials.reaction_times[np.where(stim_trials.contrastLeft == 1)[0]]
    stim_RTs_100R = stim_trials.reaction_times[np.where(stim_trials.contrastRight == 1)[0]]
    stim_RTs_100all = np.append(stim_RTs_100L,stim_RTs_100R)
    stim_RTs_25L = stim_trials.reaction_times[np.where(stim_trials_contrast == -25)[0]]
    stim_RTs_25R = stim_trials.reaction_times[np.where(stim_trials_contrast == 25)[0]]
    stim_RTs_25all = np.append(stim_RTs_25L,stim_RTs_25R)
    stim_RTs_12L = stim_trials.reaction_times[np.where(stim_trials_contrast == -12.5)[0]]
    stim_RTs_12R = stim_trials.reaction_times[np.where(stim_trials_contrast == 12)[0]]
    stim_RTs_12all = np.append(stim_RTs_12L,stim_RTs_12R)
    stim_RTs_6L = stim_trials.reaction_times[np.where(stim_trials_contrast == -6.25)[0]]
    stim_RTs_6R = stim_trials.reaction_times[np.where(stim_trials_contrast == 6.25)[0]]
    stim_RTs_6all = np.append(stim_RTs_6L,stim_RTs_6R)
    stim_RTs_0L = stim_trials.reaction_times[np.where(stim_trials.contrastLeft == 0)[0]]
    stim_RTs_0R = stim_trials.reaction_times[np.where(stim_trials.contrastRight == 0)[0]]
    stim_RTs_0all = np.append(stim_RTs_0L,stim_RTs_0R)

    nonstim_RTs_100_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 1)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 1)))]
    nonstim_RTs_100_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 1)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 1)))]
    nonstim_RTs_25_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.25)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.25)))]
    nonstim_RTs_25_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.25)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.25)))]
    nonstim_RTs_12_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.125)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.125)))]
    nonstim_RTs_12_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.125)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.125)))]
    nonstim_RTs_6_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.0625)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.0625)))]
    nonstim_RTs_6_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.0625)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.0625)))]
    nonstim_RTs_0_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0)))]
    nonstim_RTs_0_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0)))]
    stim_RTs_100_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 1)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 1)))]
    stim_RTs_100_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 1)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 1)))]
    stim_RTs_25_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.25)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.25)))]
    stim_RTs_25_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.25)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.25)))]
    stim_RTs_12_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.125)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.125)))]
    stim_RTs_12_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.125)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.125)))]
    stim_RTs_6_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.0625)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.0625)))]
    stim_RTs_6_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.0625)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.0625)))]
    stim_RTs_0_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0)))]
    stim_RTs_0_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0)))]

    nonstim_RTs_allcontrasts_inblock = np.concatenate((nonstim_RTs_0_inblock,nonstim_RTs_6_inblock,nonstim_RTs_12_inblock,nonstim_RTs_25_inblock,nonstim_RTs_100_inblock))
    stim_RTs_allcontrasts_inblock = np.concatenate((stim_RTs_0_inblock,stim_RTs_6_inblock,stim_RTs_12_inblock,stim_RTs_25_inblock,stim_RTs_100_inblock))
    nonstim_RTs_allcontrasts_outblock = np.concatenate((nonstim_RTs_0_outblock,nonstim_RTs_6_outblock,nonstim_RTs_12_outblock,nonstim_RTs_25_outblock,nonstim_RTs_100_outblock))
    stim_RTs_allcontrasts_outblock = np.concatenate((stim_RTs_0_outblock,stim_RTs_6_outblock,stim_RTs_12_outblock,stim_RTs_25_outblock,stim_RTs_100_outblock))


    ##################################################### current analysis
    ## for assessing p-value comparing zero contrast trials
    ## I don't know what is the correct way to do this...
    nonstim_zero_contrast_trials = np.where(nonstim_trials_contrast == 0)[0]
    stim_zero_contrast_trials = np.where(stim_trials_contrast == 0)[0]
    nonstim_trials_80 = np.where(nonstim_trials.probabilityLeft == 0.8)[0]
    nonstim_trials_20 = np.where(nonstim_trials.probabilityLeft == 0.2)[0]
    stim_trials_80 = np.where(stim_trials.probabilityLeft == 0.8)[0]
    stim_trials_20 = np.where(stim_trials.probabilityLeft == 0.2)[0]
    nonstim_zero_contrast_trials_80 = np.intersect1d(nonstim_zero_contrast_trials,nonstim_trials_80)
    nonstim_zero_contrast_trials_20 = np.intersect1d(nonstim_zero_contrast_trials,nonstim_trials_20)
    stim_zero_contrast_trials_80 = np.intersect1d(stim_zero_contrast_trials,stim_trials_80)
    stim_zero_contrast_trials_20 = np.intersect1d(stim_zero_contrast_trials,stim_trials_20)

    choice_nonstim_zero_contrast_trials_80 = nonstim_trials.choice[nonstim_zero_contrast_trials_80]
    choice_nonstim_zero_contrast_trials_20 = nonstim_trials.choice[nonstim_zero_contrast_trials_20]
    choice_stim_zero_contrast_trials_80 = stim_trials.choice[stim_zero_contrast_trials_80]
    choice_stim_zero_contrast_trials_20 = stim_trials.choice[stim_zero_contrast_trials_20]

    stim_trials_data = {}
    for pL in np.unique(stim_trials.probabilityLeft):
        in_block = stim_trials.probabilityLeft == pL
        xx, nn = np.unique(stim_trials_contrast[in_block], return_counts=True)
        rightward = stim_trials.choice == -1
        pp = np.vectorize(lambda x: np.mean(rightward[(x == stim_trials_contrast) & in_block]))(xx)
        stim_trials_data[pL] = np.vstack((xx, nn, pp))

    nonstim_trials_data = {}
    for pL in np.unique(nonstim_trials.probabilityLeft):
        in_block = nonstim_trials.probabilityLeft == pL
        xx, nn = np.unique(nonstim_trials_contrast[in_block], return_counts=True)
        rightward = nonstim_trials.choice == -1
        pp = np.vectorize(lambda x: np.mean(rightward[(x == nonstim_trials_contrast) & in_block]))(xx)
        nonstim_trials_data[pL] = np.vstack((xx, nn, pp))

    # A colour map for the block type
    if only_include_bias_trials == 1:
        colours = dict(zip(nonstim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:violet', 'xkcd:violet')))
    else:
        colours = dict(zip(nonstim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:black', 'xkcd:violet')))

    # Increase bias bounds (kwargs defined in previous section)
    kwargs = {
        # parmin: The minimum allowable parameter values, in the form
        # [bias, threshold, lapse_low, lapse_high]
        'parmin': np.array([-100., 30., 0., 0.]),
        # parmax: The maximum allowable parameter values
        'parmax': np.array([100., 100., 0.3, 0.8]),
        # Non-zero starting parameters, used to try to avoid local minima
        'parstart': np.array([0., 80., 0., 0.4]),
        # nfits: The number of fits to run
        'nfits': 100
    }
    # kwargs['parmin'][0] = -50.
    # kwargs['parmax'][0] = 50.


    ######################################################REPLOT
    f, (ax1, ax2) = plt.subplots(1, 2)

    # For each block type, fit the data separately and plot
    for pL, da in nonstim_trials_data.items():
        # Fit it
        pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);
        
        # Print pars
        print('prob left = {:.1f}, bias = {:2.0f}, threshold = {:2.0f}, lapse = {:.01f}, {:.01f}'.format(pL, *pars))

        # graphics
        x = np.arange(-100, 100)  # The x-axis values for our curve
        ax1.plot(da[0,:], da[2,:], color = colours[pL], marker= 'o',linestyle='None')
        ax1.plot(x, psy.erf_psycho_2gammas(pars, x), label=f'{int(pL*100)}', color=colours[pL])

    # plt.title(ref)
    # plt.legend()
    # makepretty()
    # plt.show()

    # plt.figure()
    for pL, da in stim_trials_data.items():
        # Fit it
        pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);
        
        # Print pars
        print('prob left = {:.1f}, bias = {:2.0f}, threshold = {:2.0f}, lapse = {:.01f}, {:.01f}'.format(pL, *pars))

        # graphics
        x = np.arange(-100, 100)  # The x-axis values for our curve
        ax2.plot(da[0,:], da[2,:], color = colours[pL], marker= 'o',linestyle='None')
        ax2.plot(x, psy.erf_psycho_2gammas(pars, x), label=f'{int(pL*100)}', color=colours[pL])

    # Ensure x label is not cut off
    plt.subplots_adjust(bottom=0.15)
    # Plot lines at zero and .5
    ax2.plot((0, 0), (0, 1), 'k:')
    ax2.plot((-100, 100), (.5, .5), 'k:')
    ax1.plot((0, 0), (0, 1), 'k:')
    ax1.plot((-100, 100), (.5, .5), 'k:')
    # Set limits and labels
    ax1.set(ylim=[-.05, 1.05], xlabel='contrast (%)', ylabel='proportion leftward')
    ax2.set(ylim=[-.05, 1.05], xlabel='contrast (%)')
    ax1.text(-100, 0.75, 'numtrials = ' + str(np.size(nonstim_trials.contrastLeft)), horizontalalignment='left', verticalalignment='center', fontsize=8, color='black')
    ax2.text(-100, 0.75, 'numtrials = ' + str(np.size(stim_trials.contrastLeft)), horizontalalignment='left', verticalalignment='center', fontsize=8, color='black')
    ax2.text(10, 0.20, 'num sessions = ' + str(num_analyzed_sessions), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
    ax2.text(10, 0, 'num mice = ' + str(num_unique_mice), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
    sns.despine(offset=10, trim=True)
    plt.suptitle(f'{state_type}')

    # print('Number analyzed sessions =' + str(num_analyzed_sessions))
    # print('Number analyzed mice = ' + str(num_unique_mice))

    # Get some details for the title
    # det = one.get_details(eid)
    # ref = f"{datetime.fromisoformat(det['start_time']).date()}_{det['number']:d}_{det['subject']}"

    print('numtrials nonstim = ' + str(np.size(nonstim_trials.contrastLeft)))
    print('numtrials stim = ' + str(np.size(stim_trials.contrastLeft)))

    bias_shift_sum_all_nonstim = bias_shift_sum_all_nonstim[~np.isnan(bias_shift_sum_all_nonstim)]
    bias_shift_sum_all = bias_shift_sum_all[~np.isnan(bias_shift_sum_all)]
    bias_shift_sum_all_nonstim_LC = bias_shift_sum_all_nonstim_LC[~np.isnan(bias_shift_sum_all_nonstim_LC)]
    bias_shift_sum_all_LC = bias_shift_sum_all_LC[~np.isnan(bias_shift_sum_all_LC)]

    bias_shift_sum_all_nonstim_LEFT = bias_shift_sum_all_nonstim_LEFT[~np.isnan(bias_shift_sum_all_nonstim_LEFT)]
    bias_shift_sum_all_nonstim_RIGHT = bias_shift_sum_all_nonstim_RIGHT[~np.isnan(bias_shift_sum_all_nonstim_RIGHT)]
    bias_shift_sum_all_LEFT = bias_shift_sum_all_LEFT[~np.isnan(bias_shift_sum_all_LEFT)]
    bias_shift_sum_all_RIGHT = bias_shift_sum_all_RIGHT[~np.isnan(bias_shift_sum_all_RIGHT)]

    bias_shift0_all_nonstim = bias_shift0_all_nonstim[~np.isnan(bias_shift0_all_nonstim)]
    bias_shift0_all_stim = bias_shift0_all_stim[~np.isnan(bias_shift0_all_stim)]


    statistic, pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)
    print('fit subtract pval = ' + str(pval_all))
    # statistic, pval = stats.ttest_rel(bias_shift0_all_nonstim,bias_shift0_all_stim)
    statistic, pval_low = stats.ttest_rel(bias_shift_sum_all_nonstim_LC,bias_shift_sum_all_LC)
    print('fit subtract pval low contrast = ' + str(pval_low))

    # pvals[i] = pval
    # print('finished round ' + str(i))
    # statistic, pval = stats.ttest_rel(nonstim_zerocontrast_difference,stim_zerocontrast_difference)
    # print('zero contrast subtract pval = ' + str(pval))
    # statistic, pval = stats.ttest_rel(nonstim_sumall_difference,stim_sumall_difference)
    # print('all contrast subtract pval = ' + str(pval))

    print('Number analyzed sessions =' + str(num_analyzed_sessions))
    print('Number analyzed mice = ' + str(num_unique_mice))


    # f.suptitle(ref)
    # ax1.legend()
    # ax2.legend()
    # ax1.set_ylim([-0.05,1.05])
    f.set_size_inches(8, 4, forward=True)
    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_psych.png')  # Change the path as needed
        plt.close()
    else:
        f.show()

    ####### using all trials for RT/QP/biasshift measurement
    rt_nonstimtrials_all = rt_nonstimtrials_all[~np.isnan(rt_nonstimtrials_all)]                        # IMPORTANT: MANNWHIT CANNOT TAKE ANY NAN VALUES 
    rt_stimtrials_all = rt_stimtrials_all[~np.isnan(rt_stimtrials_all)]
    pval_rt = stats.mannwhitneyu(rt_nonstimtrials_all,rt_stimtrials_all)

    qp_nonstimtrials_all = qp_nonstimtrials_all[~np.isnan(qp_nonstimtrials_all)]
    qp_stimtrials_all = qp_stimtrials_all[~np.isnan(qp_stimtrials_all)]
    pval_qp = stats.mannwhitneyu(qp_nonstimtrials_all,qp_stimtrials_all)

    def add_p_value_annotation_single_bar(p_value, index, height_factor=1.05):
        plt.text(index, height_factor, f'p={p_value:.3g}', ha='center', rotation='vertical', color='w', size=6)

    pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)
    pval_LC = stats.ttest_rel(bias_shift_sum_all_nonstim_LC,bias_shift_sum_all_LC)

    if plot_for_paper == 0:

        rtfig = plt.figure(figsize=[4.5,4.5])
        plt.bar([6,7],[np.nanmean(rt_nonstimtrials_all),np.nanmean(rt_stimtrials_all)], color=['k','b'])
        plt.errorbar(6,np.nanmean(rt_nonstimtrials_all),yerr=stats.sem(rt_nonstimtrials_all,nan_policy='omit'),color='r')
        plt.errorbar(7,np.nanmean(rt_stimtrials_all),yerr=stats.sem(rt_stimtrials_all,nan_policy='omit'),color='r')
        plt.bar([3,4],[np.nanmean(qp_nonstimtrials_all),np.nanmean(qp_stimtrials_all)], color=['k','b'])
        plt.errorbar(3,np.nanmean(qp_nonstimtrials_all),yerr=stats.sem(qp_nonstimtrials_all,nan_policy='omit'),color='r')
        plt.errorbar(4,np.nanmean(qp_stimtrials_all),yerr=stats.sem(qp_stimtrials_all,nan_policy='omit'),color='r')
        plt.xlim(2,8)
        plt.text(3.5, -0.2, 'Quiescent period', ha='center')  # Adjust -0.1 as needed
        plt.text(6.5, -0.2, 'Reaction time', ha='center')  # Adjust -0.1 as needed
        add_p_value_annotation_single_bar(pval_qp[1], 4, 0.5)  # Adjust 1.05 as needed
        add_p_value_annotation_single_bar(pval_rt[1], 7, 0.5)  # Adjust 1.05 as needed
        if save_figures == 1:
            plt.savefig(figure_save_path + figure_prefix + '_QPRT.png')  # Change the path as needed
            plt.close()
        else:
            plt.show()

        # rtfig = plt.figure(figsize=[4.5,4.5])
        # plt.bar([6,7],[np.nanmean(rt_nonstimtrials_all),np.nanmean(rt_stimtrials_all)], color=['k','b'])
        # plt.errorbar(6,np.nanmean(rt_nonstimtrials_all),yerr=stats.sem(rt_nonstimtrials_all,nan_policy='omit'),color='r')
        # plt.errorbar(7,np.nanmean(rt_stimtrials_all),yerr=stats.sem(rt_stimtrials_all,nan_policy='omit'),color='r')
        # # plt.ylim(0,1)
        # plt.show()

    else:

        rtfig = plt.figure(figsize=[2,2.8])
        plt.bar([6,7],[np.nanmean(rt_nonstimtrials_all),np.nanmean(rt_stimtrials_all)], color=['k','b'])
        plt.errorbar(6,np.nanmean(rt_nonstimtrials_all),yerr=stats.sem(rt_nonstimtrials_all,nan_policy='omit'),color='r')
        plt.errorbar(7,np.nanmean(rt_stimtrials_all),yerr=stats.sem(rt_stimtrials_all,nan_policy='omit'),color='r')
        plt.xlim(5,8)
        plt.ylim(0,2)
        plt.text(6.5, -0.2, 'Reaction time', ha='center')  # Adjust -0.1 as needed
        add_p_value_annotation_single_bar(pval_rt[1], 7, 0.5)  # Adjust 1.05 as needed
        if save_figures == 1:
            plt.savefig(figure_save_path + figure_prefix + '_RT.png')  # Change the path as needed
            plt.close()
        else:
            plt.show()

        qpfig = plt.figure(figsize=[2,2.8])
        plt.bar([3,4],[np.nanmean(qp_nonstimtrials_all),np.nanmean(qp_stimtrials_all)], color=['k','b'])
        plt.errorbar(3,np.nanmean(qp_nonstimtrials_all),yerr=stats.sem(qp_nonstimtrials_all,nan_policy='omit'),color='r')
        plt.errorbar(4,np.nanmean(qp_stimtrials_all),yerr=stats.sem(qp_stimtrials_all,nan_policy='omit'),color='r')
        plt.xlim(2,5)
        plt.ylim(0,np.nanmean(qp_stimtrials_all)*1.2)
        plt.text(3.5, -0.2, 'Quiescent period', ha='center')  # Adjust -0.1 as needed
        add_p_value_annotation_single_bar(pval_qp[1], 4, 0.5)  # Adjust 1.05 as needed
        if save_figures == 1:
            plt.savefig(figure_save_path + figure_prefix + '_QP.png')  # Change the path as needed
            plt.close()
        else:
            plt.show()
        
    biasfig = plt.figure(figsize=[2,2.8])
    # plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim),np.nanmean(bias_shift_sum_all)], color=['k','b'])
    # plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim),yerr=stats.sem(bias_shift_sum_all_nonstim,nan_policy='omit'),color='r')
    # plt.errorbar(4,np.nanmean(bias_shift_sum_all),yerr=stats.sem(bias_shift_sum_all,nan_policy='omit'),color='r')
    plt.plot([3.6,4.4], [0,0], '-b', linewidth = 1)
    plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim_LC),np.nanmean(bias_shift_sum_all_LC)], color=['k','b'])
    plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim_LC),yerr=stats.sem(bias_shift_sum_all_nonstim_LC,nan_policy='omit'),color='r')
    plt.errorbar(4,np.nanmean(bias_shift_sum_all_LC),yerr=stats.sem(bias_shift_sum_all_LC,nan_policy='omit'),color='r')
    plt.xlim(left=2)
    plt.xlim(right=5)
    plt.ylim(-0.2,np.nanmean(bias_shift_sum_all_nonstim_LC)+0.5)
    # plt.text(3,-0.4,'p = ' + str(pval_all)[0:7])
    # plt.text(6,-0.4,'p = ' + str(pval_low)[0:7])
    plt.title('Bias shift at low contrasts')
    # add_p_value_annotation_single_bar(pval_all[1], 3, 0.5)  # Adjust 1.05 as needed
    add_p_value_annotation_single_bar(pval_LC[1], 3, 0.5)  # Adjust 1.05 as needed

    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_bias.png')  # Change the path as needed
        plt.close()
    else:
        plt.show()

    pval_LCaccuracy = stats.ttest_rel(accuracy_lowcontrast_nonstim,accuracy_lowcontrast_stim,nan_policy='omit')

    LC_accuracy_fig = plt.figure(figsize=[2,2.8])
    plt.bar([3,4],[np.nanmean(accuracy_lowcontrast_nonstim),np.nanmean(accuracy_lowcontrast_stim)], color=['k','b'])
    plt.errorbar(3,np.nanmean(accuracy_lowcontrast_nonstim),yerr=stats.sem(accuracy_lowcontrast_nonstim,nan_policy='omit'),color='r')
    plt.errorbar(4,np.nanmean(accuracy_lowcontrast_stim),yerr=stats.sem(accuracy_lowcontrast_stim,nan_policy='omit'),color='r')
    plt.xlim(left=2)
    plt.xlim(right=5)
    plt.ylim(0.5,0.70)
    add_p_value_annotation_single_bar(pval_LCaccuracy[1], 3, 0.55)  # Adjust 1.05 as needed
    plt.title('Accuracy at low (0) contrasts')
    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_accuracy.png')  # Change the path as needed
        plt.close()
    else:
        plt.show()

    def save_arrays(nonstim_array, stim_array, figure_prefix):
        # Save the numpy arrays with a prefix reflecting the specific dataset/run
        np.save(f"{figure_save_path}{figure_prefix}_bias_shift_sum_all_nonstim_LC.npy", nonstim_array)
        np.save(f"{figure_save_path}{figure_prefix}_bias_shift_sum_all_stim_LC.npy", stim_array)

    if save_figures == 1:
        save_arrays(bias_shift_sum_all_nonstim_LC, bias_shift_sum_all_LC, figure_prefix)

    # RL_bias_fig = plt.figure(figsize=[3.5,4.5])
    # plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim_LEFT),np.nanmean(bias_shift_sum_all_LEFT)], color=['k','b'])
    # plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim_LEFT),yerr=stats.sem(bias_shift_sum_all_nonstim_LEFT,nan_policy='omit'),color='r')
    # plt.errorbar(4,np.nanmean(bias_shift_sum_all_LEFT),yerr=stats.sem(bias_shift_sum_all_LEFT,nan_policy='omit'),color='r')
    # plt.bar([6,7],[np.nanmean(bias_shift_sum_all_nonstim_RIGHT),np.nanmean(bias_shift_sum_all_RIGHT)], color=['k','b'])
    # plt.errorbar(6,np.nanmean(bias_shift_sum_all_nonstim_RIGHT),yerr=stats.sem(bias_shift_sum_all_nonstim_RIGHT,nan_policy='omit'),color='r')
    # plt.errorbar(7,np.nanmean(bias_shift_sum_all_RIGHT),yerr=stats.sem(bias_shift_sum_all_RIGHT,nan_policy='omit'),color='r')
    # plt.xlim(left=2)
    # plt.xlim(right=8)
    # plt.title('Bias shift; L vs R contrasts')
    # plt.show()

    if separate_stim_control == 0:
        t,p = stats.ttest_rel(bias_shift_sum_all_nonstim_LEFT,bias_shift_sum_all_LEFT)
        print('Pvalue Left = ' + str(p))
        t,p = stats.ttest_rel(bias_shift_sum_all_nonstim_RIGHT,bias_shift_sum_all_RIGHT)
        print('Pvalue Right = ' + str(p))



    ############### Chi square analysis 

    import numpy as np
    from scipy.stats import chi2_contingency, fisher_exact
    from statsmodels.stats.proportion import proportion_confint

    def calculate_bias_shift(choices, contrasts, probabilities, low_contrast_values):
        # Filtering for all contrasts and low contrasts
        all_contrasts = (probabilities != 0.5)
        low_contrasts = np.isin(contrasts, low_contrast_values) & all_contrasts

        def calculate_shift_and_counts(choices, probabilities, filter_mask):
            right_choices = choices[filter_mask] == 1
            left_block = probabilities[filter_mask] == 0.2
            right_block = probabilities[filter_mask] == 0.8

            left_block_proportion = np.mean(right_choices[left_block])
            right_block_proportion = np.mean(right_choices[right_block])
            shift = right_block_proportion - left_block_proportion
            ci_low, ci_high = proportion_confint(
                count=np.sum(right_choices[left_block]) + np.sum(right_choices[right_block]), 
                nobs=np.sum(left_block) + np.sum(right_block), 
                method='wilson')
            
            return shift, (ci_low, ci_high), np.sum(right_choices[left_block]), np.sum(right_choices[right_block])

        # shift_all, ci_all = calculate_shift(choices, probabilities, all_contrasts)
        # shift_low, ci_low = calculate_shift(choices, probabilities, low_contrasts)

        return calculate_shift_and_counts(choices, probabilities, all_contrasts), calculate_shift_and_counts(choices, probabilities, low_contrasts)


    def perform_statistical_test(control_counts, stim_counts):
        table = np.array([control_counts, stim_counts])
        chi2, p_chi2, _, _ = chi2_contingency(table)
        _, p_fisher = fisher_exact(table)

        return p_chi2, p_fisher

    # Replace these with your actual data
    mod_nonstim_trials_contrast = nonstim_trials_contrast/100
    mod_stim_trials_contrast = stim_trials_contrast/100
    choices_control, contrasts_control, probabilities_control = nonstim_trials.choice, mod_nonstim_trials_contrast, nonstim_trials.probabilityLeft
    choices_stim, contrasts_stim, probabilities_stim = stim_trials.choice, mod_stim_trials_contrast, stim_trials.probabilityLeft

    low_contrast_values = [-0.125, -0.0625, 0, 0.0625, 0.125]

    # Calculate bias shift
    bias_shift_control = calculate_bias_shift(choices_control, contrasts_control, probabilities_control, low_contrast_values)
    bias_shift_stim = calculate_bias_shift(choices_stim, contrasts_stim, probabilities_stim, low_contrast_values)

    # Perform statistical tests
    p_chi2_all, p_fisher_all = perform_statistical_test([bias_shift_control[0][2], bias_shift_control[0][3]], [bias_shift_stim[0][2], bias_shift_stim[0][3]])
    p_chi2_low, p_fisher_low = perform_statistical_test([bias_shift_control[1][2], bias_shift_control[1][3]], [bias_shift_stim[1][2], bias_shift_stim[1][3]])


    print("Bias Shift - All Trials (Control):", bias_shift_control[0])
    print("Bias Shift - Low Contrast Trials (Control):", bias_shift_control[1])
    print("Bias Shift - All Trials (Stim):", bias_shift_stim[0])
    print("Bias Shift - Low Contrast Trials (Stim):", bias_shift_stim[1])

    print("\nP-values for All Trials: Chi2 =", p_chi2_all, ", Fisher's Exact =", p_fisher_all)
    print("P-values for Low Contrast Trials: Chi2 =", p_chi2_low, ", Fisher's Exact =", p_fisher_low)

    import matplotlib.pyplot as plt

    # Assuming you have these variables from your previous calculations
    bias_shift_control_all, bias_shift_control_low = bias_shift_control
    bias_shift_stim_all, bias_shift_stim_low = bias_shift_stim

    # Organizing data into a dictionary
    bias_shift_data = {
        'Control_All': {
            'shift': bias_shift_control_all[0], 
            'ci': bias_shift_control_all[1]
        },
        'Stim_All': {
            'shift': bias_shift_stim_all[0], 
            'ci': bias_shift_stim_all[1]
        },
        'Control_Low': {
            'shift': bias_shift_control_low[0], 
            'ci': bias_shift_control_low[1]
        },
        'Stim_Low': {
            'shift': bias_shift_stim_low[0], 
            'ci': bias_shift_stim_low[1]
        }
    }

    # Preparing data for plotting
    labels = list(bias_shift_data.keys())
    shift_values = [bias_shift_data[label]['shift'] for label in labels]
    ci_values = [(bias_shift_data[label]['ci'][1] - bias_shift_data[label]['ci'][0])/2 for label in labels] # Half width of CI

    # Creating the bar plot
    plt.figure(figsize=(6, 7))
    bars = plt.bar(labels, shift_values, yerr=ci_values, capsize=5, color=['black', 'blue', 'black', 'blue'], ecolor='red')
    plt.ylabel('Bias Shift')
    plt.title('Bias Shift Comparison with Confidence Intervals')
    plt.xticks(rotation=45)
    # plt.grid(axis='y')

    # Adding p-values to the plot
    def add_p_value_annotation(bars, p_value, index, height_factor=1.09):
        height = bars[index].get_height() * height_factor
        plt.text(bars[index].get_x() + bars[index].get_width() / 2, height, f'p={p_value:.3g}', ha='center')


    add_p_value_annotation(bars, p_chi2_all, 1)  # For all trials
    add_p_value_annotation(bars, p_chi2_low, 3)  # For low contrast trials

    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_Chi.png')  # Change the path as needed
        plt.close()
    else:
        plt.show()

    #################################### PLOT WHEEL ##########################################
    # colours = dict(zip(stim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:violet', 'xkcd:violet')))

    # x_vals_for_plot = range(int(length_of_time_to_analyze_wheel_movement/interval))
    x_vals_for_plot = np.arange(0, length_of_time_to_analyze_wheel_movement, interval)

    mean_L_block_wheel_movements_stim = np.nanmean(Lblock_wheel_movements_stim, axis=0)
    mean_R_block_wheel_movements_stim = np.nanmean(Rblock_wheel_movements_stim, axis=0)
    mean_L_block_wheel_movements_nonstim = np.nanmean(Lblock_wheel_movements_nonstim, axis=0)
    mean_R_block_wheel_movements_nonstim = np.nanmean(Rblock_wheel_movements_nonstim, axis=0)

    plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_stim, color='xkcd:violet', linestyle='dashed')
    plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_stim, color='xkcd:tangerine', linestyle='dashed')
    plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_nonstim, color='xkcd:violet', linestyle='solid')
    plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_nonstim, color='xkcd:tangerine', linestyle='solid')

    for k in range(len(x_vals_for_plot)):
        valid_data = Lblock_wheel_movements_stim[:,k][~np.isnan(Lblock_wheel_movements_stim[:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_stim[k], yerr=sem, color='r')
        valid_data = Rblock_wheel_movements_stim[:,k][~np.isnan(Rblock_wheel_movements_stim[:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_stim[k], yerr=sem, color='r')
        valid_data = Lblock_wheel_movements_nonstim[:,k][~np.isnan(Lblock_wheel_movements_nonstim[:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_nonstim[k], yerr=sem, color='k')
        valid_data = Rblock_wheel_movements_nonstim[:,k][~np.isnan(Rblock_wheel_movements_nonstim[:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_nonstim[k], yerr=sem, color='k')

    plt.ylabel('Total rightward wheel movement')
    plt.xlabel('Time from ' + align_to + ' onset')
    plt.legend(['Stim Lblock', 'Stim Rblock', 'CTR Lblock','CTR Rblock'])
    plt.title('Wheel movement stim vs. no stim')
    # plt.axvline(x=0.6, color='red', linestyle='dotted')
    # plt.xlim(0,5)
    # plt.ylim(-0.15,0.15)

    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_wheel.png')  # Change the path as needed
        plt.close()
    else:
        plt.show()

###############################################################################################
####################### ZAPIT ANALYSIS HERE
else:

    ################for calculating bias values per x trials, subtracting L and R blocks at low contrasts
    import math
    trials_per_datapoint = 10

    for condition in range(0, 53):
        condition_data_Lblock_LC = [trial for trial in condition_data[condition] if trial['contrast'] < 13 and trial['probabilityLeft'] == 0.8]
        condition_data_Rblock_LC = [trial for trial in condition_data[condition] if trial['contrast'] < 13 and trial['probabilityLeft'] == 0.2]
        if len(condition_data_Lblock_LC) >= len(condition_data_Rblock_LC):
            num_cycles = math.floor(len(condition_data_Rblock_LC)/trials_per_datapoint)
        else:
            num_cycles = math.floor(len(condition_data_Lblock_LC)/trials_per_datapoint)
        bias_vals_all = np.empty([num_cycles])
        bias_vals_all[:] = np.nan
        for k in range(0, num_cycles): 
            condition_data_Lblock_LC_percycle = condition_data_Lblock_LC[k*trials_per_datapoint:(k+1)*trials_per_datapoint]
            condition_data_Rblock_LC_percycle = condition_data_Rblock_LC[k*trials_per_datapoint:(k+1)*trials_per_datapoint]
            choice_vals_Lblock = np.empty([trials_per_datapoint])
            choice_vals_Lblock[:] = np.nan
            choice_vals_Rblock = np.empty([trials_per_datapoint])
            choice_vals_Rblock[:] = np.nan
            for l in range(0, trials_per_datapoint):
                choice_vals_Lblock[l] = condition_data_Lblock_LC_percycle[l]['choice']
                choice_vals_Rblock[l] = condition_data_Rblock_LC_percycle[l]['choice']
            mean_choice_Lblock_vals = np.mean(choice_vals_Lblock)
            mean_choice_Rblock_vals = np.mean(choice_vals_Rblock)
            bias_val = mean_choice_Lblock_vals - mean_choice_Rblock_vals
            bias_vals_all[k] = bias_val

        bias_vals_LC[condition] = bias_vals_all
            
    ##### calculate bias values at each contrast using all trials
    contrasts = [-100.0, -25.0, -12.5, -6.25, 0.0, 6.25, 12.5, 25.0, 100.0]

    # Initialize a dictionary to hold the bias values for each condition
    bias_values = {cond: [] for cond in range(53)}  # 0 for nonstim, 1-52 for stim
    left_block_pleft_vals = {cond: [] for cond in range(53)}  
    right_block_pleft_vals = {cond: [] for cond in range(53)}  

    # Collect bias values for each condition and contrast level
    for contrast in contrasts:
        # Collect biases for the nonstim condition
        nonstim_left_prob = calculate_choice_probability(condition_data[0], 'left', contrast)
        nonstim_right_prob = calculate_choice_probability(condition_data[0], 'right', contrast)
        if nonstim_left_prob is not None and nonstim_right_prob is not None:
            nonstim_bias = nonstim_left_prob - nonstim_right_prob
            left_block_pleft_vals[0].append(nonstim_left_prob)
            right_block_pleft_vals[0].append(nonstim_right_prob)
            bias_values[0].append(nonstim_bias)

        # Collect biases for each stim condition
        for condition in range(1, 53):
            stim_left_prob = calculate_choice_probability(condition_data[condition], 'left', contrast)
            stim_right_prob = calculate_choice_probability(condition_data[condition], 'right', contrast)
            if stim_left_prob is not None and stim_right_prob is not None:
                stim_bias = stim_left_prob - stim_right_prob
                left_block_pleft_vals[condition].append(stim_left_prob)
                right_block_pleft_vals[condition].append(stim_right_prob)
                bias_values[condition].append(stim_bias)
            else: #in case there are no values, just use ones from control
                stim_bias = nonstim_bias
                left_block_pleft_vals[condition].append(nonstim_left_prob)
                right_block_pleft_vals[condition].append(nonstim_right_prob)
                bias_values[condition].append(stim_bias)
                

    # Now perform a statistical test to compare the block bias between nonstim and each stim condition
    comparison_results = {}
    comparison_results2 = {}
    for condition in range(1, 53):
        if bias_values[0] and bias_values[condition]:  # Check if both conditions have data
            u_stat, p_val = stats.mannwhitneyu(bias_values[0], bias_values[condition], alternative='two-sided')
            comparison_results[condition] = p_val
            x, p_val_ttestrel = stats.ttest_rel(bias_values[0], bias_values[condition], axis=0)
            comparison_results2[condition] = p_val_ttestrel
    # comparison_results contains the p-values from the Mann-Whitney U test for each condition compared to nonstim
    [kw_statistic,kwpval] = stats.kruskal(bias_values[0],bias_values[1],bias_values[2],bias_values[3],bias_values[4],
                    bias_values[5],bias_values[6],bias_values[7],bias_values[8],bias_values[9],
                    bias_values[10],bias_values[11],bias_values[12],bias_values[13],bias_values[14],
                    bias_values[15],bias_values[16],bias_values[17],bias_values[18],bias_values[19],
                    bias_values[20],bias_values[21],bias_values[22],bias_values[23],bias_values[24],
                    bias_values[25],bias_values[26],bias_values[27],bias_values[28],bias_values[29],
                    bias_values[30],bias_values[31],bias_values[32],bias_values[33],bias_values[34],
                    bias_values[35],bias_values[36],bias_values[37],bias_values[38],bias_values[39],
                    bias_values[40],bias_values[41],bias_values[42],bias_values[43],bias_values[44],
                    bias_values[45],bias_values[46],bias_values[47],bias_values[48],bias_values[49],
                    bias_values[50],bias_values[51],bias_values[52])
    [ANOVA_statistic,ANOVApval] = stats.f_oneway(bias_values[0],bias_values[1],bias_values[2],bias_values[3],bias_values[4],
                    bias_values[5],bias_values[6],bias_values[7],bias_values[8],bias_values[9],
                    bias_values[10],bias_values[11],bias_values[12],bias_values[13],bias_values[14],
                    bias_values[15],bias_values[16],bias_values[17],bias_values[18],bias_values[19],
                    bias_values[20],bias_values[21],bias_values[22],bias_values[23],bias_values[24],
                    bias_values[25],bias_values[26],bias_values[27],bias_values[28],bias_values[29],
                    bias_values[30],bias_values[31],bias_values[32],bias_values[33],bias_values[34],
                    bias_values[35],bias_values[36],bias_values[37],bias_values[38],bias_values[39],
                    bias_values[40],bias_values[41],bias_values[42],bias_values[43],bias_values[44],
                    bias_values[45],bias_values[46],bias_values[47],bias_values[48],bias_values[49],
                    bias_values[50],bias_values[51],bias_values[52])
            
    # Calculate effect sizes for each condition
    effect_sizes = {}
    for condition, biases in bias_values.items():
        if condition == 0 or not biases:  # Skip nonstim or empty conditions
            continue
        # nonstim_median_bias = np.median(bias_values[0])
        # stim_median_bias = np.median(biases)
        # effect_sizes[condition] = stim_median_bias - nonstim_median_bias
        # nonstim_0_bias = bias_values[0][4]
        # stim_0_bias = bias_values[condition][4]
        # effect_sizes[condition] = nonstim_0_bias - stim_0_bias
        nonstim_bias_sum = np.sum([bias_values[0][0],bias_values[0][1],bias_values[0][2],bias_values[0][3],
                                bias_values[0][4],bias_values[0][5],bias_values[0][6],bias_values[0][7],
                                bias_values[0][8]])
        stim_bias_sum = np.sum([bias_values[condition][0],bias_values[condition][1],bias_values[condition][2],bias_values[condition][3],
                                bias_values[condition][4],bias_values[condition][5],bias_values[condition][6],bias_values[condition][7],
                                bias_values[condition][8]])
        effect_sizes[condition] = -(stim_bias_sum - nonstim_bias_sum)/nonstim_bias_sum


    comparison_results_LC = {}
    for condition in range(1, 53):
        if len(bias_vals_LC[condition]) > 0:  # Check if both conditions have data
            x, p_val_ttestind = stats.ttest_ind(bias_vals_LC[0], bias_vals_LC[condition])
            comparison_results_LC[condition] = p_val_ttestind
    # comparison_results contains the p-values from the Mann-Whitney U test for each condition compared to nonstim
    [kw_statistic,kwpval] = stats.kruskal(bias_vals_LC[0],bias_vals_LC[1],bias_vals_LC[2],bias_vals_LC[3],bias_vals_LC[4],
                    bias_vals_LC[5],bias_vals_LC[6],bias_vals_LC[7],bias_vals_LC[8],bias_vals_LC[9],
                    bias_vals_LC[10],bias_vals_LC[11],bias_vals_LC[12],bias_vals_LC[13],bias_vals_LC[14],
                    bias_vals_LC[15],bias_vals_LC[16],bias_vals_LC[17],bias_vals_LC[18],bias_vals_LC[19],
                    bias_vals_LC[20],bias_vals_LC[21],bias_vals_LC[22],bias_vals_LC[23],bias_vals_LC[24],
                    bias_vals_LC[25],bias_vals_LC[26],bias_vals_LC[27],bias_vals_LC[28],bias_vals_LC[29],
                    bias_vals_LC[30],bias_vals_LC[31],bias_vals_LC[32],bias_vals_LC[33],bias_vals_LC[34],
                    bias_vals_LC[35],bias_vals_LC[36],bias_vals_LC[37],bias_vals_LC[38],bias_vals_LC[39],
                    bias_vals_LC[40],bias_vals_LC[41],bias_vals_LC[42],bias_vals_LC[43],bias_vals_LC[44],
                    bias_vals_LC[45],bias_vals_LC[46],bias_vals_LC[47],bias_vals_LC[48],bias_vals_LC[49],
                    bias_vals_LC[50],bias_vals_LC[51],bias_vals_LC[52])
    [ANOVA_statistic,ANOVApval] = stats.f_oneway(bias_vals_LC[0],bias_vals_LC[1],bias_vals_LC[2],bias_vals_LC[3],bias_vals_LC[4],
                    bias_vals_LC[5],bias_vals_LC[6],bias_vals_LC[7],bias_vals_LC[8],bias_vals_LC[9],
                    bias_vals_LC[10],bias_vals_LC[11],bias_vals_LC[12],bias_vals_LC[13],bias_vals_LC[14],
                    bias_vals_LC[15],bias_vals_LC[16],bias_vals_LC[17],bias_vals_LC[18],bias_vals_LC[19],
                    bias_vals_LC[20],bias_vals_LC[21],bias_vals_LC[22],bias_vals_LC[23],bias_vals_LC[24],
                    bias_vals_LC[25],bias_vals_LC[26],bias_vals_LC[27],bias_vals_LC[28],bias_vals_LC[29],
                    bias_vals_LC[30],bias_vals_LC[31],bias_vals_LC[32],bias_vals_LC[33],bias_vals_LC[34],
                    bias_vals_LC[35],bias_vals_LC[36],bias_vals_LC[37],bias_vals_LC[38],bias_vals_LC[39],
                    bias_vals_LC[40],bias_vals_LC[41],bias_vals_LC[42],bias_vals_LC[43],bias_vals_LC[44],
                    bias_vals_LC[45],bias_vals_LC[46],bias_vals_LC[47],bias_vals_LC[48],bias_vals_LC[49],
                    bias_vals_LC[50],bias_vals_LC[51],bias_vals_LC[52])

        # Calculate effect sizes for each condition
    effect_sizes_LC = {}
    nonstim_bias_mean = np.mean(bias_vals_LC[0])
    for condition in range(1, 53):
        if len(bias_vals_LC[condition]) == 0:  # Skip empty conditions
            continue

        stim_bias_mean = np.mean(bias_vals_LC[condition])
        effect_sizes_LC[condition] = -(stim_bias_mean - nonstim_bias_mean)/nonstim_bias_mean


    # for j in stimulus_locations:
    #     reaction_times_temp = stim_trials.reaction_times[np.where(stim_trials.stim_location == j)]
    #     pval_rt[j] = stats.ttest_rel(reaction_times_temp,rt_nonstimtrials_all)
    #     qp_times_temp = stim_trials.intervals[np.where(stim_trials.stim_location == j)][0] - stim_trials.stimOn_times[np.where(stim_trials.stim_location == j)]
    #     pval_rt[j] = stats.ttest_rel(qp_times_temp,qp_nonstimtrials_all)

    #     #not sure if correct ttest. also, may need to consider alternative way to calculate qp_nonstimtrials_all

    #     #calculate bias shift

    #     #calculate accuracy at high contrasts

    ### code below opens stim locations log file and extracts stim locations AP/ML coordinates
    import re

    # Define a dictionary to hold the location data
    stim_locations = {}

    # Assume we read the file line by line
    with open('/Users/natemiska/python/bias_coding/zapit_log_2024_02_28__12-41.yml', 'r') as file:
        lines = file.readlines()

    # Variables to keep track of the current location being processed
    current_location = None
    for line in lines:
        # Remove leading/trailing whitespaces and newline characters
        line = line.strip()

        # Check if the line contains 'stimLocations'
        location_match = re.search(r'stimLocations(\d+):', line)
        if location_match:
            # Extract the location number
            current_location = int(location_match.group(1))
            # Initialize the dictionary for this location
            stim_locations[current_location] = {'ML_left': None, 'ML_right': None, 'AP': None}
        elif line.startswith('ML: [') and current_location is not None:
            # Extract the ML coordinates
            ml_coords = re.findall(r'\[([-.\d]+), ([-.\d]+)\]', line)
            if ml_coords:
                # Assuming the first number is left and the second is right
                ml_left, ml_right = map(float, ml_coords[0])
                stim_locations[current_location]['ML_left'] = ml_left
                stim_locations[current_location]['ML_right'] = ml_right
        elif line.startswith('AP: [') and current_location is not None:
            # Extract the AP coordinates
            ap_coords = re.findall(r'\[([-.\d]+), ([-.\d]+)\]', line)
            if ap_coords:
                # Assuming both AP values are the same
                ap_coord = float(ap_coords[0][0])  # Use the first AP value
                stim_locations[current_location]['AP'] = ap_coord

    # Display the extracted locations
    # print(stim_locations)

    ##################### end locations extraction
    from math import sqrt
    from statsmodels.stats.proportion import proportions_ztest
    ##################### start statistical analysis
    # Nonstim reaction times, Lapse rate, & QP times
    nonstim_reaction_times = [trial['reaction_times'] for trial in condition_data[0]]
    nonstim_QP_times = [trial['qp_times'] for trial in condition_data[0]]
    nonstim_feedback = [trial['feedbackType'] for trial in condition_data[0] if trial['contrast'] in (-100, 100)]
    lapse_rate_nonstim = ((len(nonstim_feedback) - np.sum(nonstim_feedback))/2)/len(nonstim_feedback)
    lapse_rate_nonstim_n = len(nonstim_feedback)

    # Count the number of NaNs
    # num_nans = np.sum(np.isnan(nonstim_reaction_times))
    # print(f'Condition nonstim has {num_nans} NaNs in reaction times.')

    # Filter out NaNs from the reaction times
    nonstim_reaction_times = [time for time in nonstim_reaction_times if not np.isnan(time)]
    nonstim_QP_times = [time for time in nonstim_QP_times if not np.isnan(time)]

    mean_nonstim_RT = np.mean(nonstim_reaction_times)
    std_nonstim_RT = np.std(nonstim_reaction_times)
    mean_nonstim_QP = np.mean(nonstim_QP_times)
    std_nonstim_QP = np.std(nonstim_QP_times)

    # Results will be stored here
    RT_analysis_results = {}
    QP_analysis_results = {}
    lapse_rate_results = {}
    lapse_rate_results[0] = {'p_val': 'NaN', 'lapse rate': lapse_rate_nonstim}

    RT_analysis_results[0] = {'mean': mean_nonstim_RT, 'std': std_nonstim_RT}
    QP_analysis_results[0] = {'mean': mean_nonstim_QP, 'std': std_nonstim_QP}

    # Loop through each condition in condition_data except for the nonstim condition
    for condition_num in range(1,num_stim_locations):

        # Extract reaction times, lapse rate, and QP times for the current condition
        stim_reaction_times = [trial['reaction_times'] for trial in condition_data[condition_num]]
        stim_QP_times = [trial['qp_times'] for trial in condition_data[condition_num]]
        stim_feedback = [trial['feedbackType'] for trial in condition_data[condition_num] if trial['contrast'] in (-100, -25, 100, 25)]
        lapse_rate_stim = ((len(stim_feedback) - np.sum(stim_feedback))/2)/len(stim_feedback)
        lapse_rate_stim_n = len(stim_feedback)

        # # Count the number of NaNs
        # num_nans = np.sum(np.isnan(stim_reaction_times))
        # # Print the number of NaNs
        # print(f'Condition {condition_num} has {num_nans} NaNs in reaction times.')

        # Filter out NaNs from the reaction times and QP times
        stim_reaction_times = [time for time in stim_reaction_times if not np.isnan(time)]
        stim_QP_times = [time for time in stim_QP_times if not np.isnan(time)]

        mean_stim_RT = np.mean(stim_reaction_times)
        std_stim_RT = np.std(stim_reaction_times)
        mean_stim_QP = np.mean(stim_QP_times)
        std_stim_QP = np.std(stim_QP_times)

        # Perform a t-test comparing the current condition's times to the nonstim times
        t_stat, p_val = stats.ttest_ind(stim_reaction_times, nonstim_reaction_times, equal_var=False, nan_policy='omit')
        ### there are some nans in the data and I don't know why...
        t_statq, p_valq = stats.ttest_ind(stim_QP_times, nonstim_QP_times, equal_var=False, nan_policy='omit')
        
        # Calculate effect size using Cohen's d
        cohen_d = (np.mean(stim_reaction_times) - np.mean(nonstim_reaction_times)) / np.sqrt((np.std(stim_reaction_times) ** 2 + np.std(nonstim_reaction_times) ** 2) / 2)
        cohen_dq = (np.mean(stim_QP_times) - np.mean(nonstim_QP_times)) / np.sqrt((np.std(stim_QP_times) ** 2 + np.std(nonstim_QP_times) ** 2) / 2)

        # Perform the two-proportion z-test to determine whether lapse rate is significant
        stat, pval = proportions_ztest([lapse_rate_nonstim, lapse_rate_stim], [lapse_rate_nonstim_n, lapse_rate_stim_n])

        # Store the results
        RT_analysis_results[condition_num] = {'p_val': p_val, 'effect_size': cohen_d, 'mean': mean_stim_RT, 'std': std_stim_RT}
        QP_analysis_results[condition_num] = {'p_val': p_valq, 'effect_size': cohen_dq, 'mean': mean_stim_QP, 'std': std_stim_QP}
        lapse_rate_results[condition_num] = {'p_val': pval, 'lapse rate': lapse_rate_stim}


    #####################################################################################
    ################################## PLOT #############################################

    num_trials_total_estimate = len(condition_data[0])*2

    def transform_to_ccf(x, y, z, resolution=10):
        """
        Transform stereotaxic coordinates to CCF coordinates.
        
        Parameters:
        - x, y, z: Coordinates in micrometers.
        - resolution: Resolution of the CCF volume in micrometers per pixel.
        
        Returns:
        - Transformed X, Y, Z coordinates in CCF space.
        """
        # Step 1: Center on Bregma
        x_bregma, y_bregma, z_bregma = 540, 44, 570  # Bregma for 10um resolution
        x -= x_bregma
        y -= y_bregma
        z -= z_bregma

        # Step 2: Rotate the CCF (5 degrees in radians is approximately 0.0873)
        angle_rad = 5 * (np.pi / 180)  # Convert 5 degrees to radians
        X = x * np.cos(angle_rad) - y * np.sin(angle_rad)
        Y = x * np.sin(angle_rad) + y * np.cos(angle_rad)

        # Step 3: Squeeze the DV axis
        Y *= 0.9434

        # Step 4: Transform into micrometers
        X, Y, Z = X / resolution, Y / resolution, z / resolution  # Z is not transformed other than scaling

        return X, Y, Z

    ########## RT
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import matplotlib.colors as mcolors

    # Load your brain atlas image
    allenCCF_data = np.load('/Users/natemiska/python/Allen/annotation_volume_10um.npy')
    structure_tree = pd.read_csv('/Users/natemiska/python/Allen/structure_tree_safe_2017.csv')

    def generate_mip_with_borders(annotation_volume):
        # Assuming the AP axis is the first axis (shape is AP x DV x ML)
        # Find the first non-zero label along the DV axis for each ML and AP coordinate
        dorsal_surface_index = np.argmax(annotation_volume > 0, axis=1)

        # Create an empty array for the MIP
        dv_axis_length = annotation_volume.shape[1]
        ap_axis_length, ml_axis_length = dorsal_surface_index.shape
        mip = np.zeros((ap_axis_length, ml_axis_length), dtype=annotation_volume.dtype)

        # Populate the MIP array
        for x in range(ml_axis_length):
            for y in range(ap_axis_length):
                dv_index = dorsal_surface_index[y, x]
                if dv_index < dv_axis_length:
                    mip[y, x] = annotation_volume[y, dv_index, x]
        
        # Find the gradient (edges) of the regions
        grad_x, grad_y = np.gradient(mip)
        edges = np.sqrt(grad_x**2 + grad_y**2)
        
        # Set the edges to white (or any value > 0) and the rest to black
        mip_with_borders = np.where(edges > 0, 1, 0)
        
        return mip_with_borders

    print('Generating max intensity projection of allen data; this will take a minute or 2')
    dorsal_mip_with_borders = generate_mip_with_borders(allenCCF_data)

    # Determine the extents of the image in millimeters
    bregma = np.array([540, 0, 570])  # Bregma position in the Allen CCF (AP, DV, ML)
    scale_factor = -100  # Scale factor

    # Calculate the extents
    left_extent = -bregma[2] / scale_factor
    right_extent = (dorsal_mip_with_borders.shape[1] - bregma[2]) / scale_factor
    lower_extent = (dorsal_mip_with_borders.shape[0] - bregma[0]) / scale_factor
    upper_extent = -bregma[0] / scale_factor

    # Plot the brain atlas with the correct extent
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

    # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
    # norm = mcolors.Normalize(vmin=-0.3, vmax=0.3)
    norm = mcolors.Normalize(vmin = RT_analysis_results[0]['mean'] - 0.3*RT_analysis_results[0]['mean'], vmax = RT_analysis_results[0]['mean'] + 0.3*RT_analysis_results[0]['mean'])

    # Create a ScalarMappable and initialize a colormap
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

    # Overlay the stimulation points directly since they are already in the correct scale and framework
    for condition, coords in stim_locations.items():
        if condition in RT_analysis_results:
            # effect_size = RT_analysis_results[condition]['effect_size']
            effect_size = RT_analysis_results[condition]['mean']
            p_val = RT_analysis_results[condition]['p_val']
            size = -100*np.log10(p_val)
            color = sm.to_rgba(effect_size)
            # print('condition = ' + condition)
            # print('pval = ' + p_val)
            alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
            ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
            ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

    # Set the axis limits if necessary to zoom in to the region of interest
    # ax.set_xlim([-4, 4])
    # ax.set_ylim([-6, 4])

    # Add labels, title, etc.
    ax.set_ylim(bottom=-2, top=4)
    ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
    ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
    ax.set_title(title_text, fontsize=18)

    # Example p-values for the legend
    p_values = [0.001, 0.01, 0.05, 0.2]
    sizes = [-100 * np.log10(p) for p in p_values]
    # Creating the scatter plot
    # Adding a scatter plot point for each example p-value
    for p, size in zip(p_values, sizes):
        ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
    # Adding the legend with title
    ax.legend(loc='upper left', labelspacing=1.5)

    # Increase the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

    # Add a colorbar with adjusted size
    # 'fraction' is the width of the colorbar as a fraction of the axes
    # 'pad' is the spacing between the colorbar and the figure
    # 'aspect' controls the ratio of the colorbar's length to its width.
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
    cbar.set_label('Reaction time (s)', fontsize=14, labelpad=15)
    cbar.ax.tick_params(labelsize=12)
    plt.show()

    ############ QP
    # Plot the brain atlas with the correct extent
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

    # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
    # norm = mcolors.Normalize(vmin=-0.3, vmax=0.3)
    norm = mcolors.Normalize(vmin = QP_analysis_results[0]['mean'] - 0.3*QP_analysis_results[0]['mean'], vmax = QP_analysis_results[0]['mean'] + 0.3*QP_analysis_results[0]['mean'])

    # Create a ScalarMappable and initialize a colormap
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

    # Overlay the stimulation points directly since they are already in the correct scale and framework
    for condition, coords in stim_locations.items():
        if condition in QP_analysis_results:
            # effect_size = QP_analysis_results[condition]['effect_size']
            effect_size = QP_analysis_results[condition]['mean']
            p_val = QP_analysis_results[condition]['p_val']
            size = -100*np.log10(p_val)
            color = sm.to_rgba(effect_size)
            alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
            ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
            ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

    # Set the axis limits if necessary to zoom in to the region of interest
    # ax.set_xlim([-4, 4])
    # ax.set_ylim([-6, 4])

    # Add labels, title, etc.
    ax.set_ylim(bottom=-2, top=4)
    ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
    ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
    # ax.set_title('Effect on Time spent in Quiescent Period', fontsize=18)

    # Example p-values for the legend
    p_values = [0.001, 0.01, 0.05, 0.2]
    sizes = [-100 * np.log10(p) for p in p_values]
    # Creating the scatter plot
    # Adding a scatter plot point for each example p-value
    for p, size in zip(p_values, sizes):
        ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
    # Adding the legend with title
    ax.legend(loc='upper left', labelspacing=1.5)

    # Increase the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

    # Add a colorbar with adjusted size
    # 'fraction' is the width of the colorbar as a fraction of the axes
    # 'pad' is the spacing between the colorbar and the figure
    # 'aspect' controls the ratio of the colorbar's length to its width.
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
    cbar.set_label('Quiescent Period Time (s)', fontsize=14, labelpad=15)
    cbar.ax.tick_params(labelsize=12)
    plt.show()

    ############ LAPSE RATE
    # Plot the brain atlas with the correct extent
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

    # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
    # norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=lapse_rate_nonstim + 0.15)
    norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=lapse_rate_nonstim + 0.15)
    # norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=max(lapse_rate_results))

    # Create a ScalarMappable and initialize a colormap
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

    # Overlay the stimulation points directly since they are already in the correct scale and framework
    for condition, coords in stim_locations.items():
        if condition in lapse_rate_results:
            lapse_rate = lapse_rate_results[condition]['lapse rate']
            p_val = lapse_rate_results[condition]['p_val']
            size = -100*np.log10(p_val)#*np.log10(p_val)
            color = sm.to_rgba(lapse_rate)
            alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
            ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
            ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

    # Add labels, title, etc.
    ax.set_ylim(bottom=-2, top=4)
    ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
    ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
    # ax.set_title('Effect on Time spent in Quiescent Period', fontsize=18)

    # Example p-values for the legend
    p_values = [0.001, 0.01, 0.05, 0.2]
    sizes = [-100 * np.log10(p) for p in p_values]
    # Creating the scatter plot
    # Adding a scatter plot point for each example p-value
    for p, size in zip(p_values, sizes):
        ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
    # Adding the legend with title
    ax.legend(loc='upper left', labelspacing=1.5)

    # Increase the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

    # Add a colorbar with adjusted size
    # 'fraction' is the width of the colorbar as a fraction of the axes
    # 'pad' is the spacing between the colorbar and the figure
    # 'aspect' controls the ratio of the colorbar's length to its width.
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
    cbar.set_label('Lapse Rate', fontsize=14, labelpad=15)
    cbar.ax.tick_params(labelsize=12)
    plt.show()

    ############ BIAS1
    # Assuming stim_locations is a dictionary with coordinates for each stimulation point

    # Plot the brain atlas with the correct extent
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

    # Normalize effect sizes for color mapping
    norm = mcolors.Normalize(vmin=min(effect_sizes.values()), vmax=max(effect_sizes.values()))

    # Create a ScalarMappable and initialize a colormap
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
    # sm.set_array([])  # Only needed for older versions of matplotlib

    # Plot the stimulation points with effect sizes and p-values
    for condition, effect_size in effect_sizes.items():
        coords = stim_locations[condition]
        # p_val = comparison_results.get(condition, 1)  # Default to 1 if not found
        p_val = comparison_results.get(condition, 1)
        print('the p value for condition ' + str(condition) + ' = ' + str(p_val))

        # Determine the transparency based on the p-value
        # # alpha = 0.1 if p_val >= 0.05 else max(0.1, 1 - p_val)
        # # alpha = max(0.1, 1 - p_val)
        if p_val < 0.05:
            alpha = 1
        # elif p_val < 0.1:
        #     alpha = 0.7
        # elif p_val < 0.2:
        #     alpha = 0.5
        # elif p_val < 0.3:
        #     alpha = 0.3
        else:
            alpha = 0.5
        # alpha = 1

        # Determine color based on effect size
        color = sm.to_rgba(effect_size)

        # size = 200 - 200*p_val
        if np.isnan(p_val) == 1:
            size = 0
        else:
            size = -100*np.log10(p_val)#**2

        plt.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
        plt.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

        # Annotate the points with the condition number
        # plt.text(coords['ML_left'], coords['AP'], str(condition), color='yellow', ha='center', va='center')
        # plt.text(coords['ML_right'], coords['AP'], str(condition), color='yellow', ha='center', va='center')

    # Add labels, title, etc.
    ax.set_ylim(bottom=-2, top=4)
    ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
    ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)

    # Example p-values for the legend
    p_values = [0.001, 0.01, 0.05, 0.2]
    sizes = [-100 * np.log10(p) for p in p_values]
    # Creating the scatter plot
    # Adding a scatter plot point for each example p-value
    for p, size in zip(p_values, sizes):
        ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
    # Adding the legend with title
    ax.legend(loc='upper left', labelspacing=1.5)

    # Increase the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

    # Add a colorbar with adjusted size
    # 'fraction' is the width of the colorbar as a fraction of the axes
    # 'pad' is the spacing between the colorbar and the figure
    # 'aspect' controls the ratio of the colorbar's length to its width.
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
    cbar.set_label('Block Bias Reduction', fontsize=14, labelpad=15)
    cbar.ax.tick_params(labelsize=12)
    plt.show()

    ############ BIAS2

    # Plot the brain atlas with the correct extent
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

    # Normalize effect sizes for color mapping
    norm = mcolors.Normalize(vmin=min(effect_sizes_LC.values()), vmax=max(effect_sizes_LC.values()))

    # Create a ScalarMappable and initialize a colormap
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
    # sm.set_array([])  # Only needed for older versions of matplotlib

    # Plot the stimulation points with effect sizes and p-values
    for condition, effect_size in effect_sizes_LC.items():
        coords = stim_locations[condition]
        # p_val = comparison_results.get(condition, 1)  # Default to 1 if not found
        p_val = comparison_results_LC.get(condition, 1)
        print('the p value for condition ' + str(condition) + ' = ' + str(p_val))

        # Determine the transparency based on the p-value
        if p_val < 0.05:
            alpha = 1
        else:
            alpha = 0.5

        # Determine color based on effect size
        color = sm.to_rgba(effect_size)

        # size = 200 - 200*p_val
        if np.isnan(p_val) == 1:
            size = 0
        else:
            size = -100*np.log10(p_val)#**2

        plt.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
        plt.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

        # Annotate the points with the condition number
        # plt.text(coords['ML_left'], coords['AP'], str(condition), color='yellow', ha='center', va='center')
        # plt.text(coords['ML_right'], coords['AP'], str(condition), color='yellow', ha='center', va='center')

    # Add labels, title, etc.
    ax.set_ylim(bottom=-2, top=4)
    ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
    ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)

    # Example p-values for the legend
    p_values = [0.001, 0.01, 0.05, 0.2]
    sizes = [-100 * np.log10(p) for p in p_values]
    # Creating the scatter plot
    # Adding a scatter plot point for each example p-value
    for p, size in zip(p_values, sizes):
        ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
    # Adding the legend with title
    ax.legend(loc='upper left', labelspacing=1.5)

    # Increase the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

    # Add a colorbar with adjusted size
    # 'fraction' is the width of the colorbar as a fraction of the axes
    # 'pad' is the spacing between the colorbar and the figure
    # 'aspect' controls the ratio of the colorbar's length to its width.
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
    cbar.set_label('Block Bias Reduction (alt)', fontsize=14, labelpad=15)
    cbar.ax.tick_params(labelsize=12)
    plt.show()

    ### also need to create a measure of high contrast accuracy and visualize that at each location
    ### also, use this on nonstim trials to exclude sessions below performance threshold

    def plot_psychometric(contrasts, left_choices, right_choices, title):
        """
        Plot psychometric curves for left and right block trials.
        
        :param contrasts: Array-like, list of contrasts.
        :param left_choices: Array-like, list of percent leftward choices for left block trials.
        :param right_choices: Array-like, list of percent leftward choices for right block trials.
        :param title: String, the title for the plot.
        """
        plt.figure(figsize=(10, 8))
        plt.plot(contrasts, left_choices, color='blue', label='Left Block')
        plt.plot(contrasts, right_choices, color='orange', label='Right Block')
        
        plt.title(title)
        plt.xlabel('Contrast')
        plt.ylabel('% Leftward Choice')
        plt.legend()
        plt.show()

    # plot_psychometric(contrasts, left_block_pleft_vals[0], right_block_pleft_vals[0], f'Condition {condition}')
    # # Loop through each condition, including the control condition at index 0
    # # for condition in range(1,53):

    #################################### PLOT PSYCHOMETRIC #####################################

    condition = 32
    # Extract or calculate the psychometric data for the current condition
    left_block_choices = left_block_pleft_vals[condition]
    right_block_choices = right_block_pleft_vals[condition]

    # Plot the psychometric curves
    plot_psychometric(contrasts, left_block_choices, right_block_choices, f'Condition {condition}')

    # Wait for user input to proceed to the next plot
    # input("Press Enter to continue to the next plot...")
    # plt.close()  # This closes the current figure before the next one is drawn

    #################################### PLOT WHEEL ##########################################
    ### condition defined above

    x_vals_for_plot = np.arange(0, length_of_time_to_analyze_wheel_movement, interval)

    mean_L_block_wheel_movements_stim = np.nanmean(Lblock_wheel_movements_by_condition[condition], axis=0)
    mean_R_block_wheel_movements_stim = np.nanmean(Rblock_wheel_movements_by_condition[condition], axis=0)
    mean_L_block_wheel_movements_nonstim = np.nanmean(Lblock_wheel_movements_by_condition[0], axis=0)
    mean_R_block_wheel_movements_nonstim = np.nanmean(Rblock_wheel_movements_by_condition[0], axis=0)

    plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_stim, color='xkcd:violet', linestyle='dashed')
    plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_stim, color='xkcd:tangerine', linestyle='dashed')
    plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_nonstim, color='xkcd:violet', linestyle='solid')
    plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_nonstim, color='xkcd:tangerine', linestyle='solid')

    for k in range(len(x_vals_for_plot)):
        valid_data = Lblock_wheel_movements_by_condition[condition][:,k][~np.isnan(Lblock_wheel_movements_by_condition[condition][:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_stim[k], yerr=sem, color='r')
        valid_data = Rblock_wheel_movements_by_condition[condition][:,k][~np.isnan(Rblock_wheel_movements_by_condition[condition][:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_stim[k], yerr=sem, color='r')
        valid_data = Lblock_wheel_movements_by_condition[0][:,k][~np.isnan(Lblock_wheel_movements_by_condition[0][:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_nonstim[k], yerr=sem, color='k')
        valid_data = Rblock_wheel_movements_by_condition[0][:,k][~np.isnan(Rblock_wheel_movements_by_condition[0][:,k])]
        sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
        plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_nonstim[k], yerr=sem, color='k')

    plt.ylabel('Total leftward wheel movement')
    plt.xlabel('Time from ' + align_to + ' onset')
    plt.legend(['Stim Lblock', 'Stim Rblock', 'CTR Lblock','CTR Rblock'])
    plt.title('Wheel movement stim vs. no stim')
    # plt.axvline(x=0.6, color='red', linestyle='dotted')
    # plt.xlim(0,5)
    # plt.ylim(-0.15,0.15)
    plt.show()


    ###### Alternative plot using p values of difference between r and left blocks

    # low_contrasts = [-100, -25, -12.5, -6.25, 0, 6.25, 12.5, 25, 100]
    low_contrasts = [-6.25, 0, 6.25]
    choices_by_condition = {cond: {'R_block': [], 'L_block': []} for cond in condition_data}

    for cond, trials in condition_data.items():
        for trial in trials:
            if trial['contrast'] in low_contrasts:
                block_type = 'R_block' if trial['probabilityLeft'] == 0.2 else 'L_block'
                choices_by_condition[cond][block_type].append(trial['choice'])

    from scipy.stats import ttest_ind

    p_values = {}

    for cond, blocks in choices_by_condition.items():
        # Ensure there are choices in both blocks to compare
        if blocks['R_block'] and blocks['L_block']:
            stat, p_val = ttest_ind(blocks['R_block'], blocks['L_block'])
            p_values[cond] = p_val
        else:
            p_values[cond] = np.nan  # Use NaN where we can't perform the test due to lack of data

    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np

    # Setup the figure and axes
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create a colormap: blue for significant, red for not significant
    cmap = plt.get_cmap('coolwarm_r')

    # Prepare p-values: take the negative logarithm to emphasize smaller p-values
    log_p_values = {cond: -np.log10(p_val) if p_val > 0 else 0 for cond, p_val in p_values.items()}

    # Normalize the transformed p-values for color mapping
    # Use min and max of the transformed p-values for normalization
    min_log_p_val, max_log_p_val = min(log_p_values.values()), max(log_p_values.values())
    min_log_p_val = 0.7
    max_log_p_val = 9.5
    norm = mcolors.Normalize(vmin=min_log_p_val, vmax=max_log_p_val)

    # Plot each condition
    for condition, coords in stim_locations.items():
    # for condition, coords in islice(stim_locations.items(), len(stim_locations) - 1):
        if condition == 52:
            continue
        log_p_val = log_p_values.get(condition, 0)  # Default to 0 (max p-value) if not found
        color = cmap(norm(log_p_val))
        
        ml_left = coords.get('ML_left')
        ml_right = coords.get('ML_right')
        ap = coords.get('AP')
        
        if ml_left and ml_right and ap is not None:
            ax.scatter(ml_left, ap, color=color, s=100, edgecolors='black', label='Left Hemisphere' if condition == 1 else "")
            ax.scatter(ml_right, ap, color=color, s=100, edgecolors='black', label='Right Hemisphere' if condition == 1 else "")

    # Add a colorbar to explain the mapping
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('-log10(P-value)')

    # Add title and labels as needed
    ax.set_title('Heatmap of -log10(P-value) for Block Choice Differences')
    ax.set_xlabel('Mediolateral Position')
    ax.set_ylabel('Anteroposterior Position')

    plt.show()

    ### analyze wheel!

    # store deviation (currently manually)

    # df_deviation = pd.DataFrame(deviation, columns=['Values'])
    # df_deviation.to_csv('/Users/feiyang/Projects/GLM-HMM/reversed_both0hz_snr.csv', index=False)

    # test = pd.read_csv('/Users/feiyang/Projects/GLM-HMM/reversed_left50hz_zi.csv')

    # Genetic_Line = 'D2-Cre',
    # Brain_Region = 'motor_bilateral',

    # ##### GLM-HMM #####
    # """
    # state_def = "previous": Uses state on stim_trials - 1 for stim_trials. 
    # state labels are stored in 'engaged_prevtrial_indices.pkl' and 'disengaged_prevtrial_indices.pkl' files.

    # state_def = "current": Uses state on stim_trials. 
    # state labels retrieved by get_glmhmm_indices() later down in the script. 
    # """

    # # load glm-hmm labels
    # with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
    #     state_probability = pickle.load(pickle_file)

    # # load trial-1 labels
    # with open("/Users/natemiska/int-brain-lab/GLM-HMM/engaged_prevtrial_indices.pkl", 'rb') as pickle_file:
    #     engaged_indices = pickle.load(pickle_file)
    # with open("/Users/natemiska/int-brain-lab/GLM-HMM/disengaged_prevtrial_indices.pkl", 'rb') as pickle_file: 
    #     disengaged_indices = pickle.load(pickle_file)


    # ############### OPTIONS ####################
    # is_zapit_session = 0
    # BL_perf_thresh = 0
    # stim_perf_thresh = 0
    # # BL_perf_thresh = 0.2 #0.79    ## 
    # # stim_perf_thresh = 0 #0.5      ## performance threshold for opto stim ON trials 
    # min_num_trials = 0 #300
    # min_bias_threshold = 0.3 #0.75
    # min_bias_threshold_zapit = 1 #1.5
    # #RT_threshold = 30 #20
    # RT_threshold = 100

    # use_trials_after_stim = 0
    # subsample_trials_after_stim = 0

    # save_figures = 0 # 0: save figure = false; 1: save figure = true
    # figure_save_path = '/Users/feiyang/Desktop/Neuro/Year3/Research Project/'
    # figure_prefix = 'D2_ex_DLS'

    # title_text = '81, 82, 57'

    # ############## WHEEL OPTIONS ##############

    # length_of_time_to_analyze_wheel_movement = 10
    # interval = 0.1
    # stim_rt_threshold = 100
    # align_to = 'QP'#'feedback'#'goCue_pre'#'QP'
    # only_include_low_contrasts = 0
    # low_contrast_threshold = 13
    # ########### OLD OPTIONS

# remove_trials_before = 0#140 #346
# loop_threshold_for_remove = 100
# #list of eids to use

# separate_stim_control = 0 # if 1, then stim not controlled by program (ie, no 'opto' parameter)
# start_trials_w_block_switch = 0 # if 1, then start with first block switch after stim
# remove_trials_after_block_switch = 0 # if 1, then remove x trials after block switch (defined below)
# num_trials_to_keep_after_switch = 50

# only_keep_later_trials = 0
# later_trials_start = 0

# only_analyze_trials_x_after_stim = 0 #for removing simply x trials immediately after start of stim


# ##################### MAIN LOOP ##########################

# ### for concatenating zapit data; will need to change number for different stims
# num_stim_locations = 52

# condition_data = {i: [] for i in range(0, num_stim_locations+1)}  # 1-52 for laser, 0 for control
# bias_vals_LC = {i: [] for i in range(0, num_stim_locations+1)}

# Rblock_wheel_movements_by_condition = [[] for _ in range(53)]
# Lblock_wheel_movements_by_condition = [[] for _ in range(53)]

# num_analyzed_sessions = 0
# #for loop with each iteration creating stim / nonstim trials info for that eid (exactly as in manual_plot_script)
#     #then, that trials info is added to a set of master trials info (one for stim, one for non-stim).  might be easiest if this is pre-allocated to correct size before loop
# # for lm in range(0,6): #for analyzing each subject individually and using avg bias shift as a single data point
# num_unique_mice = 0
# previous_mouse_ID = 'NaN'

# Rblock_wheel_movements_stim = [] 
# Lblock_wheel_movements_stim = []
# Rblock_wheel_movements_nonstim = []
# Lblock_wheel_movements_nonstim = []

# bias_shift = np.empty([np.size(eids)])
# bias_shift[:] = np.nan
# bias_shift_sum_all = np.empty([np.size(eids)])
# bias_shift_sum_all[:] = np.nan
# bias_shift_sum_all_LC = np.empty([np.size(eids)])
# bias_shift_sum_all_LC[:] = np.nan
# bias_shift_sum_all_LEFT = np.empty([np.size(eids)])
# bias_shift_sum_all_LEFT[:] = np.nan
# bias_shift_sum_all_RIGHT = np.empty([np.size(eids)])
# bias_shift_sum_all_RIGHT[:] = np.nan
# bias_shift_nonstim = np.empty([np.size(eids)])
# bias_shift_nonstim[:] = np.nan
# bias_shift_sum_all_nonstim = np.empty([np.size(eids)])
# bias_shift_sum_all_nonstim[:] = np.nan
# bias_shift_sum_all_nonstim_LC = np.empty([np.size(eids)])
# bias_shift_sum_all_nonstim_LC[:] = np.nan
# bias_shift_sum_all_nonstim_LEFT = np.empty([np.size(eids)])
# bias_shift_sum_all_nonstim_LEFT[:] = np.nan
# bias_shift_sum_all_nonstim_RIGHT = np.empty([np.size(eids)])
# bias_shift_sum_all_nonstim_RIGHT[:] = np.nan
# bias_shift0_all_nonstim = np.empty([np.size(eids)])
# bias_shift0_all_nonstim[:] = np.nan
# bias_shift0_all_stim = np.empty([np.size(eids)])
# bias_shift0_all_stim[:] = np.nan
# stim_zerocontrast_difference = np.empty([np.size(eids)])
# stim_zerocontrast_difference[:] = np.nan
# nonstim_zerocontrast_difference = np.empty([np.size(eids)])
# nonstim_zerocontrast_difference[:] = np.nan
# stim_sumall_difference = np.empty([np.size(eids)])
# stim_sumall_difference[:] = np.nan
# nonstim_sumall_difference = np.empty([np.size(eids)])
# nonstim_sumall_difference[:] = np.nan
# deviation = [] 
# for j in range(0,np.size(eids)):

#     eid = eids[j]

#     print('starting session, eid = ' + eid)
#     try:
#         trials = one.load_object(eid, 'trials')

#     except:
#         print('Failed to load eid = ' + eid)
#         #input("Press Enter to continue...")
#         continue

#     if is_zapit_session == 0:
#         try:
#             dset = '_iblrig_taskData.raw*'
#             data_behav = one.load_dataset(eid, dataset=dset, collection='raw_behavior_data')
#             ses_path = one.eid2path(eid)
#         except:
#             print('Dataset "_iblrig_taskData.raw*.*" not found for eid = ' + eid + '. Utilizing laser intervals data...')
#             laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
#     wheel = one.load_object(eid, 'wheel')
#     current_mouse_ID = MouseIDs[j]

#     if not is_eid_successful(state_probability, current_mouse_ID, eid):
#         continue  # Skip eid with failed glm-hmm sessions
    

#     if is_zapit_session == 0:
#         reaction_times = np.empty([np.size(trials['contrastLeft'])])
#         reaction_times[:] = np.nan
#         quiescent_period_times = np.empty([np.size(trials['contrastLeft'])])
#         quiescent_period_times[:] = np.nan

#         try:
#             taskData = load_data(ses_path) ###depricated
#         except:
#             print('no task data found...')
#         for tr in range(len(trials['contrastLeft'])):
#             react = trials['feedback_times'][tr] - trials['goCue_times'][tr]
#             if react > 59.9:
#                 # print('error')
#                 continue
#             try:
#                 trial_start_time = taskData[tr]['behavior_data']['States timestamps']['trial_start'][0][0]
#                 stimOn_time = taskData[tr]['behavior_data']['States timestamps']['stim_on'][0][0]
#             except:
#                 trial_start_time = trials.intervals[tr,0]
#                 stimOn_time = trials.goCueTrigger_times[tr]

#             qp = stimOn_time - trial_start_time
#             reaction_times[tr] = react
#             quiescent_period_times[tr] = qp            

#         if num_analyzed_sessions == 0:

#             stim_trials = trials.copy()
#             nonstim_trials = trials.copy()


#         stim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
#         nonstim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
#         if trials_ranges[j] == 'ALL':
#             trials_range = range(0,len(trials['contrastLeft']))
#         #### use last trial as end of range when end of range set to 9999
#         elif trials_ranges[j][-1] == 9998:
#             trials_range = [x for x in trials_ranges[j] if x < np.size(trials.probabilityLeft)]
#         else:
#             trials_range = trials_ranges[j]
#         if remove_trials_before > 0 and j < loop_threshold_for_remove:
#             trials_range = list(np.array(trials_range)[np.where(np.array(trials_range) > remove_trials_before)[0]])
#         if len(trials_range) < min_num_trials:
#             print('Not enough trials in ' + str(eid) + ' , skipping...')
#             continue


#         ##### GLM-HMMM #####
#         try: 
#             if state_def == 'current': 
#                 engaged_idx, disengaged_idx = get_glmhmm_indices(current_mouse_ID, eid, state_probability, n_states)

#             elif state_def == 'previous':
#                 engaged_idx = engaged_indices[current_mouse_ID][eid]
#                 disengaged_idx = disengaged_indices[current_mouse_ID][eid]
                
#         except:
#             print(f'no glm-hmm state labels found for eid: {eid}. skipping session...')
#             continue

#         ####################
        
#         if state_type == 'engaged':
#             trials_range = engaged_idx
#         elif state_type == 'disengaged':
#             trials_range = disengaged_idx

#         ### 2 different ways to extract what trials were laser trials; old versus new

#         try:
#             for k in trials_range:
#                 if taskData[k]['opto'] == 1:
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:
#                         stim_trials_numbers[k] = k
#                 else:
#                     react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                     if react < RT_threshold:
#                         nonstim_trials_numbers[k] = k    
                                    
#         except:
#             laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
#             for k in trials_range:#range(0,len(trials.intervals)):

#                 if stim_params[j] == 'QPRE':

#                     if trials.intervals[k,0] in laser_intervals[:,0]:
#                         react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                         if react < RT_threshold:  
#                             stim_trials_numbers[k] = k
#                     else:
#                         react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                         if react < RT_threshold:
#                             nonstim_trials_numbers[k] = k  

#                 elif stim_params[j] == 'SORE':

#                     start_trial = trials.intervals[k, 0]
#                     end_trial = trials.intervals[k, 1]

#                     if np.any((laser_intervals[:, 0] >= start_trial) & (laser_intervals[:, 0] <= end_trial)):
#                         react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                         if react < RT_threshold:  
#                             stim_trials_numbers[k] = k
#                     else:
#                         react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                         if react < RT_threshold:
#                             nonstim_trials_numbers[k] = k  

#         # if state_def == 'previous':                         # TO DO: account for trials where stim was on 2 trials in a row !!
#         #     prev_stim_trials_numbers = stim_trials_numbers -

#         ##############
                            
#         # modified_stim_trials = stim_trials_numbers.copy()

#         # # Get indices of valid (non-NaN) values in nonstim_trials_numbers
#         # valid_nonstim = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]

#         # # Track the last found valid smaller value
#         # previous_valid = np.nan

#         # for i in range(len(stim_trials_numbers)):
#         #     if not np.isnan(stim_trials_numbers[i]):  # Only process non-NaN values
#         #         stim_value = stim_trials_numbers[i]

#         #         # Find the nearest smaller and larger values
#         #         smaller_values = valid_nonstim[valid_nonstim < stim_value]
#         #         larger_values = valid_nonstim[valid_nonstim > stim_value]

#         #         nearest_smaller = np.max(smaller_values) if smaller_values.size > 0 else np.nan
#         #         nearest_larger = np.min(larger_values) if larger_values.size > 0 else np.nan

#         #         # Determine which to use
#         #         if not np.isnan(nearest_smaller) and abs(stim_value - nearest_smaller) <= 10:
#         #             assigned_value = nearest_smaller  # Use nearest smaller if within 10
#         #         elif not np.isnan(nearest_larger):  
#         #             assigned_value = nearest_larger  # Otherwise, use nearest larger
#         #         else:
#         #             assigned_value = np.nan  # If nothing is found, keep NaN

#         #         # Assign value if valid
#         #         if not np.isnan(assigned_value):
#         #             modified_stim_trials[i] = assigned_value

            

#         #### TEST (^^) ####

#         trials_numbers = np.concatenate((nonstim_trials_numbers,stim_trials_numbers))
#         trials_numbers = trials_numbers[~np.isnan(trials_numbers)]
#         stim_trials_numbers = stim_trials_numbers[~np.isnan(stim_trials_numbers)]
#         nonstim_trials_numbers = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]
#         stim_trials_numbers = stim_trials_numbers.astype(int)
#         nonstim_trials_numbers = nonstim_trials_numbers.astype(int)
#         trials_numbers = trials_numbers.astype(int)
#         stim_trials_numbers = stim_trials_numbers[stim_trials_numbers>89]
#         nonstim_trials_numbers = nonstim_trials_numbers[nonstim_trials_numbers>89]
#         trials_numbers = trials_numbers[trials_numbers>89]
#         if use_trials_after_stim == 1:
#             for l in range(len(stim_trials_numbers)): 
#                 if l == len(stim_trials_numbers) - 1: 
#                     if stim_trials_numbers[l] > nonstim_trials_numbers[len(nonstim_trials_numbers) - 1]:
#                         stim_trials_numbers[l] = 9999
#                         continue
#                     else:
#                         stim_trials_numbers[l] = stim_trials_numbers[l] + 1
#                 else:
#                     if stim_trials_numbers[l+1] - stim_trials_numbers[l] == 1:
#                         stim_trials_numbers[l] = 9999
#                         continue
#                     else:
#                         stim_trials_numbers[l] = stim_trials_numbers[l] + 1

#         stim_trials_numbers = stim_trials_numbers[stim_trials_numbers!=9999]
#         rt_stimtrials = reaction_times[stim_trials_numbers]
#         qp_stimtrials = quiescent_period_times[stim_trials_numbers]
#         rt_nonstimtrials = reaction_times[nonstim_trials_numbers]
#         qp_nonstimtrials = quiescent_period_times[nonstim_trials_numbers]

#         ### remove all "stim" trials from nonstim trials
#         nonstim_trials_numbers = np.setdiff1d(nonstim_trials_numbers, stim_trials_numbers)

#         #for subsampling, maybe check on each iteration here if # L&R trials in each block is equal
#         #alternatively, can take randomly equal number of trials from each and pool them together
#         #ie, make 2 groups each block, RstimRblock, LstimRblock, LstimLblock, and RstimLblock
#         #and subsample randomly equal amount of each for each block
#         if subsample_trials_after_stim:
#             Rblock_inds_stim = stim_trials_numbers[np.where(trials.probabilityLeft[stim_trials_numbers] == 0.2)[0]]
#             Lblock_inds_stim = stim_trials_numbers[np.where(trials.probabilityLeft[stim_trials_numbers] == 0.8)[0]]
#             PrevLchoice_inds_stim = stim_trials_numbers[np.where(trials.choice[stim_trials_numbers-1] == -1)[0]]
#             PrevRchoice_inds_stim = stim_trials_numbers[np.where(trials.choice[stim_trials_numbers-1] == 1)[0]]
#             ind_Lblock_Lprevchoice_stim = np.intersect1d(Lblock_inds_stim,PrevLchoice_inds_stim)
#             ind_Lblock_Rprevchoice_stim = np.intersect1d(Lblock_inds_stim,PrevRchoice_inds_stim)
#             ind_Rblock_Lprevchoice_stim = np.intersect1d(Rblock_inds_stim,PrevLchoice_inds_stim)
#             ind_Rblock_Rprevchoice_stim = np.intersect1d(Rblock_inds_stim,PrevRchoice_inds_stim)

#             if len(ind_Lblock_Lprevchoice_stim) > len(ind_Lblock_Rprevchoice_stim):
#                 subsample_indices_toremove_A = random.sample(list(ind_Lblock_Lprevchoice_stim), len(ind_Lblock_Lprevchoice_stim) - len(ind_Lblock_Rprevchoice_stim))
#             elif len(ind_Lblock_Lprevchoice_stim) < len(ind_Lblock_Rprevchoice_stim):
#                 subsample_indices_toremove_A = random.sample(list(ind_Lblock_Rprevchoice_stim), len(ind_Lblock_Rprevchoice_stim) - len(ind_Lblock_Lprevchoice_stim))

#             if len(ind_Rblock_Lprevchoice_stim) > len(ind_Rblock_Rprevchoice_stim):
#                 subsample_indices_toremove_B = random.sample(list(ind_Rblock_Lprevchoice_stim), len(ind_Rblock_Lprevchoice_stim) - len(ind_Rblock_Rprevchoice_stim))
#             elif len(ind_Rblock_Lprevchoice_stim) < len(ind_Rblock_Rprevchoice_stim):
#                 subsample_indices_toremove_B = random.sample(list(ind_Rblock_Rprevchoice_stim), len(ind_Rblock_Rprevchoice_stim) - len(ind_Rblock_Lprevchoice_stim))

#             subsample_indices_toremove = np.concatenate([subsample_indices_toremove_A,subsample_indices_toremove_B])
#             # stim_trials_numbers_test = stim_trials_numbers
#             for k in subsample_indices_toremove:
#                 # stim_trials_numbers_test = np.delete(stim_trials_numbers_test, np.where(stim_trials_numbers_test == k))
#                 stim_trials_numbers = np.delete(stim_trials_numbers, np.where(stim_trials_numbers == k))

#         ###for quantifying ipsi/contraversive turns
#         # Calculate bias index 
#         nonstim_direction = trials.choice[nonstim_trials_numbers]
#         nonstim_leftward = np.sum(nonstim_direction == 1)
#         nonstim_rightward = np.sum(nonstim_direction == -1)
#         nonstim_bias = (nonstim_rightward - nonstim_leftward) / len(nonstim_direction)

#         stim_direction = trials.choice[stim_trials_numbers]
#         stim_leftward = np.sum(stim_direction == 1)
#         stim_rightward = np.sum(stim_direction == -1)
#         stim_bias = (stim_rightward - stim_leftward) / len(stim_direction)

#         # Effect size
#         deviation.append(stim_bias - nonstim_bias) 


#         ###for estimating bias shift
#         stim_trials_temp = trials.copy()
#         nonstim_trials_temp = trials.copy()
#         stim_trials_temp.contrastRight = trials.contrastRight[stim_trials_numbers]
#         stim_trials_temp.contrastLeft = trials.contrastLeft[stim_trials_numbers]
#         stim_trials_temp.goCueTrigger_times = trials.goCueTrigger_times[stim_trials_numbers]
#         stim_trials_temp.feedback_times = trials.feedback_times[stim_trials_numbers]
#         stim_trials_temp.response_times = trials.response_times[stim_trials_numbers]
#         stim_trials_temp.feedbackType = trials.feedbackType[stim_trials_numbers]
#         stim_trials_temp.goCue_times = trials.goCue_times[stim_trials_numbers]
#         stim_trials_temp.firstMovement_times = trials.firstMovement_times[stim_trials_numbers]
#         stim_trials_temp.probabilityLeft = trials.probabilityLeft[stim_trials_numbers]
#         stim_trials_temp.stimOn_times = trials.stimOn_times[stim_trials_numbers]
#         stim_trials_temp.choice = trials.choice[stim_trials_numbers]
#         stim_trials_temp.prev_choice = trials.choice[stim_trials_numbers-1]
#         stim_trials_temp.rewardVolume = trials.rewardVolume[stim_trials_numbers]
#         stim_trials_temp.intervals = trials.intervals[stim_trials_numbers]
#         nonstim_trials_temp.contrastRight = trials.contrastRight[nonstim_trials_numbers]
#         nonstim_trials_temp.contrastLeft = trials.contrastLeft[nonstim_trials_numbers]
#         nonstim_trials_temp.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers]
#         nonstim_trials_temp.feedback_times = trials.feedback_times[nonstim_trials_numbers]
#         nonstim_trials_temp.response_times = trials.response_times[nonstim_trials_numbers]
#         nonstim_trials_temp.feedbackType = trials.feedbackType[nonstim_trials_numbers]
#         nonstim_trials_temp.goCue_times = trials.goCue_times[nonstim_trials_numbers]
#         nonstim_trials_temp.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers]
#         nonstim_trials_temp.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers]
#         nonstim_trials_temp.stimOn_times = trials.stimOn_times[nonstim_trials_numbers]
#         nonstim_trials_temp.choice = trials.choice[nonstim_trials_numbers]
#         nonstim_trials_temp.prev_choice = trials.choice[nonstim_trials_numbers-1]
#         nonstim_trials_temp.rewardVolume = trials.rewardVolume[nonstim_trials_numbers]
#         nonstim_trials_temp.intervals = trials.intervals[nonstim_trials_numbers]
#         stim_trials_temp_contrast = signed_contrast(stim_trials_temp)
#         nonstim_trials_temp_contrast = signed_contrast(nonstim_trials_temp)

#         nonstim_trialnums_HCR = np.where(nonstim_trials_temp_contrast == 100)[0]
#         nonstim_trialnums_HCL = np.where(nonstim_trials_temp_contrast == -100)[0]
#         num_correct_HCR = np.sum(nonstim_trials_temp.rewardVolume[nonstim_trialnums_HCR])/1.5
#         num_correct_HCL = np.sum(nonstim_trials_temp.rewardVolume[nonstim_trialnums_HCL])/1.5

#         stim_trialnums_HCR = np.where(stim_trials_temp_contrast == 100)[0]
#         stim_trialnums_HCL = np.where(stim_trials_temp_contrast == -100)[0]
#         stim_num_correct_HCR = np.sum(stim_trials_temp.rewardVolume[stim_trialnums_HCR])/1.5
#         stim_num_correct_HCL = np.sum(stim_trials_temp.rewardVolume[stim_trialnums_HCL])/1.5

#         all_signed_contrast = signed_contrast(trials)
#         abs_signed_contrast = abs(all_signed_contrast)

#         low_contrast_trials_bool_all = abs_signed_contrast < low_contrast_threshold

#         if num_correct_HCR/np.size(nonstim_trialnums_HCR) < BL_perf_thresh or num_correct_HCL/np.size(nonstim_trialnums_HCL) < BL_perf_thresh:
#             print(eid + ' below performance threshold, excluding...')
#             continue
#         if stim_num_correct_HCR/np.size(stim_trialnums_HCR) < stim_perf_thresh or stim_num_correct_HCL/np.size(stim_trialnums_HCL) < stim_perf_thresh:
#             print(eid + ' below performance threshold, excluding...')
#             continue

#         #waitforbuttonpress

#         stim_trials_data = {}
#         for pL in np.unique(stim_trials_temp.probabilityLeft):
#             in_block = stim_trials_temp.probabilityLeft == pL
#             xx, nn = np.unique(stim_trials_temp_contrast[in_block], return_counts=True)
#             rightward = stim_trials_temp.choice == -1
#             pp = np.vectorize(lambda x: np.mean(rightward[(x == stim_trials_temp_contrast) & in_block]))(xx)
#             stim_trials_data[pL] = np.vstack((xx, nn, pp))

#         nonstim_trials_data = {}
#         for pL in np.unique(nonstim_trials_temp.probabilityLeft):
#             in_block = nonstim_trials_temp.probabilityLeft == pL
#             xx, nn = np.unique(nonstim_trials_temp_contrast[in_block], return_counts=True)
#             rightward = nonstim_trials_temp.choice == -1
#             pp = np.vectorize(lambda x: np.mean(rightward[(x == nonstim_trials_temp_contrast) & in_block]))(xx)
#             nonstim_trials_data[pL] = np.vstack((xx, nn, pp))

#         kwargs = {                                                                      # CONTROLS PSYCHOMETRIC FIT
#             # parmin: The minimum allowable parameter values, in the form
#             # [bias, threshold, lapse_low, lapse_high]
#             'parmin': np.array([-25., 10., 0., 0.]),
#             # parmax: The maximum allowable parameter values
#             'parmax': np.array([100, 100., 1, 1]),
#             # Non-zero starting parameters, used to try to avoid local minima
#             'parstart': np.array([0., 40., .1, .1]),
#             # nfits: The number of fits to run
#             'nfits': 50
#         }
#         kwargs['parmin'][0] = -50.
#         kwargs['parmax'][0] = 50.

#         # For each block type, fit the data separately and plot
#         for pL, da in nonstim_trials_data.items():
#             # Fit it
#             pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs); 

#             if pL == 0.8:
#                 bias_80_value0 = psy.erf_psycho_2gammas(pars, 0)
#                 bias_80_valuen100 = psy.erf_psycho_2gammas(pars, -100)
#                 bias_80_valuen25 = psy.erf_psycho_2gammas(pars, -25)
#                 bias_80_valuen12 = psy.erf_psycho_2gammas(pars, -12)
#                 bias_80_valuen6 = psy.erf_psycho_2gammas(pars, -6)
#                 bias_80_value100 = psy.erf_psycho_2gammas(pars, 100)
#                 bias_80_value25 = psy.erf_psycho_2gammas(pars, 25)
#                 bias_80_value12 = psy.erf_psycho_2gammas(pars, 12)
#                 bias_80_value6 = psy.erf_psycho_2gammas(pars, 6)

#             if pL == 0.2:
#                 bias_20_value0 = psy.erf_psycho_2gammas(pars, 0)
#                 bias_20_valuen100 = psy.erf_psycho_2gammas(pars, -100)
#                 bias_20_valuen25 = psy.erf_psycho_2gammas(pars, -25)
#                 bias_20_valuen12 = psy.erf_psycho_2gammas(pars, -12)
#                 bias_20_valuen6 = psy.erf_psycho_2gammas(pars, -6)
#                 bias_20_value100 = psy.erf_psycho_2gammas(pars, 100)
#                 bias_20_value25 = psy.erf_psycho_2gammas(pars, 25)
#                 bias_20_value12 = psy.erf_psycho_2gammas(pars, 12)
#                 bias_20_value6 = psy.erf_psycho_2gammas(pars, 6)


#         bias_shift0 = bias_20_value0 - bias_80_value0
#         bias_shiftn100 = bias_20_valuen100 - bias_80_valuen100
#         bias_shiftn25 = bias_20_valuen25 - bias_80_valuen25
#         bias_shiftn12 = bias_20_valuen12 - bias_80_valuen12
#         bias_shiftn6 = bias_20_valuen6 - bias_80_valuen6
#         bias_shift100 = bias_20_value100 - bias_80_value100
#         bias_shift25 = bias_20_value25 - bias_80_value25
#         bias_shift12 = bias_20_value12 - bias_80_value12
#         bias_shift6 = bias_20_value6 - bias_80_value6
#         bias_shift_sum_all_temp = sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6,bias_shift100,bias_shift25,bias_shift12,bias_shift6])
#         if bias_shift_sum_all_temp < min_bias_threshold:
#             print(eid + ' below minimum baseline bias threshold, excluding...')
#             continue

#         ## CHANGE HERE TO SWITCH between all vs low stim comparison --> high vs low stim
#         bias_shift_sum_all_nonstim[j] = sum([bias_shiftn100,bias_shift100,bias_shiftn25,bias_shift25]) #bias_shift_sum_all_temp
#         bias_shift_sum_all_nonstim_LC[j] = sum([bias_shift0,bias_shiftn12,bias_shiftn6,bias_shift12,bias_shift6])
#         bias_shift0_all_nonstim[j] = bias_shift0
#         bias_shift_sum_all_nonstim_LEFT[j] = sum([bias_shiftn100,bias_shiftn25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6])
#         bias_shift_sum_all_nonstim_RIGHT[j] = sum([bias_shift100,bias_shift25]) #sum([bias_shift0,bias_shift100,bias_shift25,bias_shift12,bias_shift6])

#         #     pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)

#         for pL, da in stim_trials_data.items():
#             # Fit it
#             pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);

#             if pL == 0.8:
#                 bias_80_value0 = psy.erf_psycho_2gammas(pars, 0)
#                 bias_80_valuen100 = psy.erf_psycho_2gammas(pars, -100)
#                 bias_80_valuen25 = psy.erf_psycho_2gammas(pars, -25)
#                 bias_80_valuen12 = psy.erf_psycho_2gammas(pars, -12)
#                 bias_80_valuen6 = psy.erf_psycho_2gammas(pars, -6)
#                 bias_80_value100 = psy.erf_psycho_2gammas(pars, 100)
#                 bias_80_value25 = psy.erf_psycho_2gammas(pars, 25)
#                 bias_80_value12 = psy.erf_psycho_2gammas(pars, 12)
#                 bias_80_value6 = psy.erf_psycho_2gammas(pars, 6)

#             if pL == 0.2:
#                 bias_20_value0 = psy.erf_psycho_2gammas(pars, 0)
#                 bias_20_valuen100 = psy.erf_psycho_2gammas(pars, -100)
#                 bias_20_valuen25 = psy.erf_psycho_2gammas(pars, -25)
#                 bias_20_valuen12 = psy.erf_psycho_2gammas(pars, -12)
#                 bias_20_valuen6 = psy.erf_psycho_2gammas(pars, -6)
#                 bias_20_value100 = psy.erf_psycho_2gammas(pars, 100)
#                 bias_20_value25 = psy.erf_psycho_2gammas(pars, 25)
#                 bias_20_value12 = psy.erf_psycho_2gammas(pars, 12)
#                 bias_20_value6 = psy.erf_psycho_2gammas(pars, 6)


#         bias_shift0 = bias_20_value0 - bias_80_value0
#         bias_shiftn100 = bias_20_valuen100 - bias_80_valuen100
#         bias_shiftn25 = bias_20_valuen25 - bias_80_valuen25
#         bias_shiftn12 = bias_20_valuen12 - bias_80_valuen12
#         bias_shiftn6 = bias_20_valuen6 - bias_80_valuen6
#         bias_shift100 = bias_20_value100 - bias_80_value100
#         bias_shift25 = bias_20_value25 - bias_80_value25
#         bias_shift12 = bias_20_value12 - bias_80_value12
#         bias_shift6 = bias_20_value6 - bias_80_value6

#         # ALSO CHANGE HERE TO SWITCH BETWEEN ALL AND HIGH CONTRAST COMPARISONS
#         bias_shift_sum_all[j] = sum([bias_shiftn100,bias_shift100,bias_shiftn25,bias_shift25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6,bias_shift100,bias_shift25,bias_shift12,bias_shift6])
#         bias_shift_sum_all_LC[j] = sum([bias_shift0,bias_shiftn12,bias_shiftn6,bias_shift12,bias_shift6])
#         bias_shift0_all_stim[j] = bias_shift0
#         bias_shift_sum_all_LEFT[j] = sum([bias_shiftn100,bias_shiftn25]) #sum([bias_shift0,bias_shiftn100,bias_shiftn25,bias_shiftn12,bias_shiftn6])
#         bias_shift_sum_all_RIGHT[j] = sum([bias_shift100,bias_shift25]) #sum([bias_shift0,bias_shift100,bias_shift25,bias_shift12,bias_shift6])

#         #############################################################
#         ##### Load wheel data
#         if use_trials_after_stim == 0: ##wheel analysis not currently set up for stim+1 condition
#             whlpos, whlt = wheel.position, wheel.timestamps

#             for k in trials_numbers:#range(len(trials['contrastLeft'])):
#                 # trialnum = trials_numbers[k]
#                 trialnum = k

#                 if only_include_low_contrasts == 1:
#                     if ~low_contrast_trials_bool_all[k]:
#                         continue
#                 # print(str(trialnum))

#                 # start_time = taskData[trialnum]['behavior_data']['States timestamps']['trial_start'][0][0] - 0.03 #quiescent period - first 30ms step
#                 # start_time = taskData[trialnum]['behavior_data']['States timestamps']['reward'][0][0] - 0.5 #reward/error
#                 # if np.isnan(start_time) == 1:
#                 #     start_time = taskData[trialnum]['behavior_data']['States timestamps']['error'][0][0] - 0.5

#                 if align_to == 'goCue':
#                     start_time = trials.goCue_times[trialnum] #GO CUE
#                 elif align_to == 'goCue_pre':
#                     start_time = trials.goCue_times[trialnum] - 0.5 #GO CUE - 0.5s
#                 elif align_to == 'QP':
#                     start_time = trials.intervals[trialnum][0] #QP / Laser onset
#                 elif align_to == 'feedback':
#                     start_time = trials.feedback_times[trialnum] - 0.6

#                 wheel_start_index_pre = np.searchsorted(whlt, start_time)
#                 t = start_time
#                 # Check the closest value by comparing the differences between 't' and its neighboring elements
#                 if wheel_start_index_pre == 0:
#                     wheel_start_index = wheel_start_index_pre
#                 elif wheel_start_index_pre == len(whlt):
#                     wheel_start_index = wheel_start_index_pre - 1
#                 else:
#                     left_diff = t - whlt[wheel_start_index_pre - 1]
#                     right_diff = whlt[wheel_start_index_pre] - t
#                     wheel_start_index = wheel_start_index_pre - 1 if left_diff <= right_diff else wheel_start_index_pre


#                 total_wheel_movement = []
#                 for l in range(int(length_of_time_to_analyze_wheel_movement/interval)):
#                     t = (start_time + l*interval)# + interval #ie, steps of 100ms
#                     # wheel_end_index = np.argmin(np.abs(whlt - t))
#                     #norm_wheel_vals = whlpos[wheel_start_index:wheel_end_index]/whlpos[wheel_start_index]

#                     wheel_end_index_pre = np.searchsorted(whlt, t) #ie, steps of 100ms
#                     # Check the closest value by comparing the differences between 't' and its neighboring elements
#                     if wheel_end_index_pre == 0:
#                         wheel_end_index = wheel_end_index_pre
#                     elif wheel_end_index_pre == len(whlt):
#                         wheel_end_index = wheel_end_index_pre - 1
#                     else:
#                         left_diff = t - whlt[wheel_end_index_pre - 1]
#                         right_diff = whlt[wheel_end_index_pre] - t
#                         wheel_end_index = wheel_end_index_pre - 1 if left_diff <= right_diff else wheel_end_index_pre

#                     ##only in case where aligning to QP, do not use any wheel movement past goCue
#                     if align_to == 'QP' and trials.goCue_times[trialnum] < whlt[wheel_end_index]:
#                         total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                     ##only in case where aligning to goCue, do not use any wheel movement past feedback + 0.1
#                     elif align_to == 'goCue' and (trials.feedback_times[trialnum] + interval) < whlt[wheel_end_index]:
#                         total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                     elif align_to == 'goCue_pre' and (trials.feedback_times[trialnum] + interval) < whlt[wheel_end_index]:
#                         total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                     else:
#                         total_wheel_movement = np.append(total_wheel_movement,whlpos[wheel_end_index] - whlpos[wheel_start_index])

#                 #determine whether trial is a stim or nonstim trial
#                 #nonstim
#                 if np.isin(trialnum,nonstim_trials_numbers):
#                     if trials.probabilityLeft[trialnum] == 0.2:
#                         if len(Rblock_wheel_movements_nonstim) == 0:
#                             Rblock_wheel_movements_nonstim = total_wheel_movement
#                         else:
#                             Rblock_wheel_movements_nonstim = np.vstack([Rblock_wheel_movements_nonstim,total_wheel_movement])
#                     if trials.probabilityLeft[trialnum] == 0.8:
#                         if len(Lblock_wheel_movements_nonstim) == 0:
#                             Lblock_wheel_movements_nonstim = total_wheel_movement
#                         else:
#                             Lblock_wheel_movements_nonstim = np.vstack([Lblock_wheel_movements_nonstim,total_wheel_movement])
#                 #stim
#                 elif np.isin(trialnum,stim_trials_numbers):
#                     if trials.probabilityLeft[trialnum] == 0.2:
#                         if  len(Rblock_wheel_movements_stim) == 0:
#                             Rblock_wheel_movements_stim = total_wheel_movement
#                         else:
#                             Rblock_wheel_movements_stim = np.vstack([Rblock_wheel_movements_stim,total_wheel_movement])
#                     if trials.probabilityLeft[trialnum] == 0.8:
#                         if len(Lblock_wheel_movements_stim) == 0:
#                             Lblock_wheel_movements_stim = total_wheel_movement
#                         else:
#                             Lblock_wheel_movements_stim = np.vstack([Lblock_wheel_movements_stim,total_wheel_movement])
#                 else:
#                     raise Exception('Trials must be either stim or nonstim; something is wrong')
#         #############################################################

#         if num_analyzed_sessions == 0:
#             stim_trials.contrastRight = trials.contrastRight[stim_trials_numbers]
#             stim_trials.contrastLeft = trials.contrastLeft[stim_trials_numbers]
#             stim_trials.goCueTrigger_times = trials.goCueTrigger_times[stim_trials_numbers]
#             stim_trials.feedback_times = trials.feedback_times[stim_trials_numbers]
#             stim_trials.response_times = trials.response_times[stim_trials_numbers]
#             stim_trials.feedbackType = trials.feedbackType[stim_trials_numbers]
#             stim_trials.goCue_times = trials.goCue_times[stim_trials_numbers]
#             stim_trials.firstMovement_times = trials.firstMovement_times[stim_trials_numbers]
#             stim_trials.probabilityLeft = trials.probabilityLeft[stim_trials_numbers]
#             stim_trials.stimOn_times = trials.stimOn_times[stim_trials_numbers]
#             stim_trials.choice = trials.choice[stim_trials_numbers]
#             stim_trials.prev_choice = trials.choice[stim_trials_numbers-1]
#             stim_trials.rewardVolume = trials.rewardVolume[stim_trials_numbers]
#             stim_trials.intervals = trials.intervals[stim_trials_numbers]
#             stim_trials.reaction_times = stim_trials.feedback_times - stim_trials.stimOn_times
#             nonstim_trials.contrastRight = trials.contrastRight[nonstim_trials_numbers]
#             nonstim_trials.contrastLeft = trials.contrastLeft[nonstim_trials_numbers]
#             nonstim_trials.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers]
#             nonstim_trials.feedback_times = trials.feedback_times[nonstim_trials_numbers]
#             nonstim_trials.response_times = trials.response_times[nonstim_trials_numbers]
#             nonstim_trials.feedbackType = trials.feedbackType[nonstim_trials_numbers]
#             nonstim_trials.goCue_times = trials.goCue_times[nonstim_trials_numbers]
#             nonstim_trials.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers]
#             nonstim_trials.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers]
#             nonstim_trials.stimOn_times = trials.stimOn_times[nonstim_trials_numbers]
#             nonstim_trials.choice = trials.choice[nonstim_trials_numbers]
#             nonstim_trials.prev_choice = trials.choice[nonstim_trials_numbers-1]
#             nonstim_trials.rewardVolume = trials.rewardVolume[nonstim_trials_numbers]
#             nonstim_trials.intervals = trials.intervals[nonstim_trials_numbers]
#             nonstim_trials.reaction_times = nonstim_trials.feedback_times - nonstim_trials.stimOn_times
#             stim_trials_contrast = signed_contrast(stim_trials)
#             nonstim_trials_contrast = signed_contrast(nonstim_trials)
#             rt_stimtrials_all = rt_stimtrials
#             qp_stimtrials_all = qp_stimtrials
#             rt_nonstimtrials_all = rt_nonstimtrials
#             qp_nonstimtrials_all = qp_nonstimtrials
#             rt_stimtrials_all_persubject = np.nanmean(rt_stimtrials)
#             qp_stimtrials_all_persubject = np.nanmean(qp_stimtrials)
#             rt_nonstimtrials_all_persubject = np.nanmean(rt_nonstimtrials)
#             qp_nonstimtrials_all_persubject = np.nanmean(qp_nonstimtrials)
#             num_analyzed_sessions = 1
#             num_unique_mice = 1
#             previous_mouse_ID = current_mouse_ID
#         else:
#             stim_trials.contrastRight = np.append(stim_trials.contrastRight,trials.contrastRight[stim_trials_numbers])
#             stim_trials.contrastLeft = np.append(stim_trials.contrastLeft,trials.contrastLeft[stim_trials_numbers])
#             stim_trials.goCueTrigger_times = np.append(stim_trials.goCueTrigger_times,trials.goCueTrigger_times[stim_trials_numbers])
#             stim_trials.feedback_times = np.append(stim_trials.feedback_times,trials.feedback_times[stim_trials_numbers])
#             stim_trials.response_times = np.append(stim_trials.response_times,trials.response_times[stim_trials_numbers])
#             stim_trials.feedbackType = np.append(stim_trials.feedbackType,trials.feedbackType[stim_trials_numbers])
#             stim_trials.goCue_times = np.append(stim_trials.goCue_times,trials.goCue_times[stim_trials_numbers])
#             stim_trials.firstMovement_times = np.append(stim_trials.firstMovement_times,trials.firstMovement_times[stim_trials_numbers])
#             stim_trials.probabilityLeft = np.append(stim_trials.probabilityLeft,trials.probabilityLeft[stim_trials_numbers])
#             stim_trials.stimOn_times = np.append(stim_trials.stimOn_times,trials.stimOn_times[stim_trials_numbers])
#             stim_trials.choice = np.append(stim_trials.choice,trials.choice[stim_trials_numbers])
#             stim_trials.prev_choice = np.append(stim_trials.prev_choice,trials.choice[stim_trials_numbers-1])
#             stim_trials.rewardVolume = np.append(stim_trials.rewardVolume,trials.rewardVolume[stim_trials_numbers])
#             stim_trials.intervals = np.append(stim_trials.intervals,trials.intervals[stim_trials_numbers])
#             stim_trials.reaction_times = np.append(stim_trials.reaction_times,trials.feedback_times[stim_trials_numbers] - trials.stimOn_times[stim_trials_numbers])
#             nonstim_trials.contrastRight = np.append(nonstim_trials.contrastRight,trials.contrastRight[nonstim_trials_numbers])
#             nonstim_trials.contrastLeft = np.append(nonstim_trials.contrastLeft,trials.contrastLeft[nonstim_trials_numbers])
#             nonstim_trials.goCueTrigger_times = np.append(nonstim_trials.goCueTrigger_times,trials.goCueTrigger_times[nonstim_trials_numbers])
#             nonstim_trials.feedback_times = np.append(nonstim_trials.feedback_times,trials.feedback_times[nonstim_trials_numbers])
#             nonstim_trials.response_times = np.append(nonstim_trials.response_times,trials.response_times[nonstim_trials_numbers])
#             nonstim_trials.feedbackType = np.append(nonstim_trials.feedbackType,trials.feedbackType[nonstim_trials_numbers])
#             nonstim_trials.goCue_times = np.append(nonstim_trials.goCue_times,trials.goCue_times[nonstim_trials_numbers])
#             nonstim_trials.firstMovement_times = np.append(nonstim_trials.firstMovement_times,trials.firstMovement_times[nonstim_trials_numbers])
#             nonstim_trials.probabilityLeft = np.append(nonstim_trials.probabilityLeft,trials.probabilityLeft[nonstim_trials_numbers])
#             nonstim_trials.stimOn_times = np.append(nonstim_trials.stimOn_times,trials.stimOn_times[nonstim_trials_numbers])
#             nonstim_trials.choice = np.append(nonstim_trials.choice,trials.choice[nonstim_trials_numbers])
#             nonstim_trials.prev_choice = np.append(nonstim_trials.prev_choice,trials.choice[nonstim_trials_numbers-1])
#             nonstim_trials.rewardVolume = np.append(nonstim_trials.rewardVolume,trials.rewardVolume[nonstim_trials_numbers])
#             nonstim_trials.intervals = np.append(nonstim_trials.intervals,trials.intervals[nonstim_trials_numbers])
#             nonstim_trials.reaction_times = np.append(nonstim_trials.reaction_times,trials.feedback_times[nonstim_trials_numbers] - trials.stimOn_times[nonstim_trials_numbers])
#             # stim_trials_contrast = np.append(stim_trials_contrast,signed_contrast(stim_trials))
#             # nonstim_trials_contrast = np.append(nonstim_trials_contrast,signed_contrast(nonstim_trials)) #??? check this
#             rt_stimtrials_all = np.append(rt_stimtrials_all,rt_stimtrials)
#             qp_stimtrials_all = np.append(qp_stimtrials_all,qp_stimtrials)
#             rt_nonstimtrials_all = np.append(rt_nonstimtrials_all,rt_nonstimtrials)
#             qp_nonstimtrials_all = np.append(qp_nonstimtrials_all,qp_nonstimtrials)

#             rt_stimtrials_all_persubject = np.append(rt_stimtrials_all_persubject,np.nanmean(rt_stimtrials))
#             qp_stimtrials_all_persubject = np.append(qp_stimtrials_all_persubject,np.nanmean(qp_stimtrials))
#             rt_nonstimtrials_all_persubject = np.append(rt_nonstimtrials_all_persubject,np.nanmean(rt_nonstimtrials))
#             qp_nonstimtrials_all_persubject = np.append(qp_nonstimtrials_all_persubject,np.nanmean(qp_nonstimtrials))
#             num_analyzed_sessions = num_analyzed_sessions + 1
#             if previous_mouse_ID != current_mouse_ID:
#                 num_unique_mice = num_unique_mice + 1
#                 previous_mouse_ID = current_mouse_ID


#     ############################################ the following is analysis for zapit sessions
#     ########################################################################################
#     else:
#         laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')

#         if trials_ranges[j] == 'ALL':
#             trials_range = range(0,len(trials['contrastLeft']))
#         #### use last trial as end of range when end of range set to 9999
#         elif trials_ranges[j][-1] == 9998:
#             trials_range = [x for x in trials_ranges[j] if x < np.size(trials.probabilityLeft)]
#         else:
#             trials_range = trials_ranges[j]
#         # if remove_trials_before > 0 and j < loop_threshold_for_remove:
#         #     trials_range = list(np.array(trials_range)[np.where(np.array(trials_range) > remove_trials_before)[0]])
#         # if len(trials_range) < min_num_trials:
#         #     print('Not enough trials in ' + str(eid) + ' , skipping...')
#         #     continue

#         ############################## zapit stim locations log
#         file_path = r'C:\Users\IBLuser\zapit_trials.yml'

#         details = one.get_details(eid)
#         exp_start_time_str = details['start_time']

#         if eid == '21d33b44-f75f-4711-a2c7-0bdfe8eec386': #strange issue with logged stims in this session
#             exp_start_time_str = '2024-03-29T18:07:38.0'

#         # Convert session start to datetime object
#         session_start = datetime.strptime(exp_start_time_str[0:19], '%Y-%m-%dT%H:%M:%S')

#         event_num = 0
#         with open(file_path, 'r') as file:
#             # Skip the first line
#             next(file)
#             # List to hold events that occur during or after the session start
#             relevant_events = []
#             for line in file:
#                 # Extract the timestamp part from the line and convert it to a datetime object
#                 # Assuming the format is always "YYYY-MM-DD HH:MM:SS", which corresponds to the first 19 characters
#                 event_timestamp_str = line[:19]
#                 event_timestamp = datetime.strptime(event_timestamp_str, '%Y-%m-%d %H:%M:%S')
                
#                 # Check if the event timestamp is equal to or later than the session start
#                 if event_timestamp >= session_start:
#                     relevant_events.append(line.strip())  # Add event line to the list, stripping newline characters

#             event_num = event_num + 1

#         # # Now, relevant_events contains all the lines for events during or after the session start
#         # for event in relevant_events:
#         #     print(event)
#         ######################### end zapit log load
            
#         ### Loop that extracts trial number and stim location for each laser stim
#         stimtrial_location_dict = {}
#         previous_logged_timestamp = datetime.strptime(relevant_events[0][:19], '%Y-%m-%d %H:%M:%S')
#         previous_laser_interval = laser_intervals[0,0]
#         for k in range(0,len(laser_intervals[:,0]) - 2): #loop is num of laser stim for session
#             if k == 0:
#                 continue
#                 #1st stim can be before 1st trial?
#             elif eid == '21d33b44-f75f-4711-a2c7-0bdfe8eec386' and k < 10: #strange issue with logged stims in this session
#                 continue
#             else:
#                 trialnum = np.where(laser_intervals[k,0]==trials.intervals[:,0])[0][0]
#                 stim_location = relevant_events[k][20:22]
#                 cleaned_stim_location = int(re.sub(r'\D', '', stim_location))
#                 stimtrial_location_dict[trialnum] = cleaned_stim_location
#                 logged_time = relevant_events[k][0:19]
#                 if eid == '5a41494f-25b9-48d4-8159-527141bd4742': #strange exception where logged events off by 1 starting ~trial 11
#                     logged_time = relevant_events[k-1][0:19]
#                 logged_timestamp = event_timestamp = datetime.strptime(logged_time, '%Y-%m-%d %H:%M:%S')
#                 # print('trial number = ' + str(trialnum))
#                 # print('laser interval = ' + str(laser_intervals[k,0]))
#                 # print('logged time = ' + logged_time)

#                 delta = logged_timestamp - previous_logged_timestamp
#                 delta_log = delta.total_seconds()
#                 # print('delta log = ' + str(delta_log))
#                 delta_interval = laser_intervals[k,0] - previous_laser_interval
#                 # print('delta interval = ' + str(delta_interval))
#                 # if abs(delta_log - delta_interval) > 1:
#                 #     print('Warning, laser log may be incorrect for trial ' + str(trialnum))
#                 #     ui = input("Press Enter to continue, e to exit...")
#                 #     if ui == 'e':
#                 #         raise Exception('Script terminated by user')
            
#                 previous_laser_interval = laser_intervals[k,0]
#                 previous_logged_timestamp = logged_timestamp


#         stimtrial_location_dict_all = {k: 0 for k in trials_range}
#         stimtrial_location_dict_all.update(stimtrial_location_dict)

#         ### make new dict that simply adds 1 to each key
#         if use_trials_after_stim == 1:
#             stimtrial_location_dict_OG = stimtrial_location_dict_all
#             stimtrial_location_dict_all = {key + 1: value for key, value in stimtrial_location_dict_all.items() if np.min(trials_range) <= key < np.max(trials_range)}



#         ####################################################################################
#         ### for removing whole session if it does not meet behavioral criteria
#         session_data_nonstim = {i: [] for i in range(0, 1)}
#         if use_trials_after_stim == 1:
#             trials_with_condition_zero = [trial for trial, condition in stimtrial_location_dict_OG.items() if condition == 0]  ###need to make sure this propogates
#         else:
#             trials_with_condition_zero = [trial for trial, condition in stimtrial_location_dict_all.items() if condition == 0]
#         for trial_number in trials_with_condition_zero:
#             reaction_time = trials.feedback_times[trial_number] - trials.goCueTrigger_times[trial_number] 
#             if np.isnan(reaction_time) == 1:
#                 reaction_time = trials.feedback_times[trial_number] - trials.stimOn_times[trial_number] ###reaction time definitions may be unreliable - any other ways to define?

#             trials_data = {
#                 'choice': trials.choice[trial_number],
#                 'reaction_times': reaction_time,
#                 'qp_times': trials.goCueTrigger_times[trial_number] - trials.intervals[trial_number][0],
#                 'contrast': signed_contrast(trials)[trial_number],
#                 'feedbackType': trials.feedbackType[trial_number],
#                 'probabilityLeft': trials.probabilityLeft[trial_number],
#                 # 'prev_choice': trials.choice[trial_number-1]
#             }
#             session_data_nonstim[0].append(trials_data)

#         nonstim_feedback = [trial['feedbackType'] for trial in session_data_nonstim[0] if trial['contrast'] in (-100, -25, 25, 100)]
#         correct_rate_nonstim = np.sum(np.array(nonstim_feedback) == 1) / len(nonstim_feedback)
#         print('Accuracy at high contrasts = ' + str(correct_rate_nonstim))
#         if correct_rate_nonstim < BL_perf_thresh:
#             print('Session eid = ' + eid + ' is below minimum performance threshold, skipping...')
#             continue

#         # create criteria for minimum bias session
#         choices_L100_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -100 and trial['probabilityLeft'] == 0.8]
#         choices_L25_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -25 and trial['probabilityLeft'] == 0.8]
#         choices_L12_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -12.5 and trial['probabilityLeft'] == 0.8]
#         choices_L6_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -6.25 and trial['probabilityLeft'] == 0.8]
#         choices_0_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 0 and trial['probabilityLeft'] == 0.8]
#         choices_R6_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 6.25 and trial['probabilityLeft'] == 0.8]
#         choices_R12_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 12.5 and trial['probabilityLeft'] == 0.8]
#         choices_R25_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 25 and trial['probabilityLeft'] == 0.8]
#         choices_R100_Lblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 100 and trial['probabilityLeft'] == 0.8]
#         choices_L100_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -100 and trial['probabilityLeft'] == 0.2]
#         choices_L25_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -25 and trial['probabilityLeft'] == 0.2]
#         choices_L12_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -12.5 and trial['probabilityLeft'] == 0.2]
#         choices_L6_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == -6.25 and trial['probabilityLeft'] == 0.2]
#         choices_0_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 0 and trial['probabilityLeft'] == 0.2]
#         choices_R6_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 6.25 and trial['probabilityLeft'] == 0.2]
#         choices_R12_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 12.5 and trial['probabilityLeft'] == 0.2]
#         choices_R25_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 25 and trial['probabilityLeft'] == 0.2]
#         choices_R100_Rblock = [trial['choice'] for trial in session_data_nonstim[0] if trial['contrast'] == 100 and trial['probabilityLeft'] == 0.2]

#         biasshift_L100 = np.sum(np.array(choices_L100_Lblock) == 1)/len(choices_L100_Lblock) - np.sum(np.array(choices_L100_Rblock) == 1)/len(choices_L100_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_L25 = np.sum(np.array(choices_L25_Lblock) == 1)/len(choices_L25_Lblock) - np.sum(np.array(choices_L25_Rblock) == 1)/len(choices_L25_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_L12 = np.sum(np.array(choices_L12_Lblock) == 1)/len(choices_L12_Lblock) - np.sum(np.array(choices_L12_Rblock) == 1)/len(choices_L12_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_L6 = np.sum(np.array(choices_L6_Lblock) == 1)/len(choices_L6_Lblock) - np.sum(np.array(choices_L6_Rblock) == 1)/len(choices_L6_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_0 = np.sum(np.array(choices_0_Lblock) == 1)/len(choices_0_Lblock) - np.sum(np.array(choices_0_Rblock) == 1)/len(choices_0_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_R6 = np.sum(np.array(choices_R6_Lblock) == 1)/len(choices_R6_Lblock) - np.sum(np.array(choices_R6_Rblock) == 1)/len(choices_R6_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_R12 = np.sum(np.array(choices_R12_Lblock) == 1)/len(choices_R12_Lblock) - np.sum(np.array(choices_R12_Rblock) == 1)/len(choices_R12_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_R25 = np.sum(np.array(choices_R25_Lblock) == 1)/len(choices_R25_Lblock) - np.sum(np.array(choices_R25_Rblock) == 1)/len(choices_R25_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0
#         biasshift_R100 = np.sum(np.array(choices_R100_Lblock) == 1)/len(choices_R100_Lblock) - np.sum(np.array(choices_R100_Rblock) == 1)/len(choices_R100_Rblock)
#         if np.isnan(biasshift_L100) == 1:
#             biasshift_L100 = 0

#         total_biasshift = biasshift_L100 + biasshift_L25 + biasshift_L12 + biasshift_L6 + biasshift_0 + biasshift_R6 + biasshift_R12 + biasshift_R25 + biasshift_R100
#         print('Total bias shift = ' + str(total_biasshift))
#         if total_biasshift < min_bias_threshold_zapit:
#             print('Bias shift for session below threshold, skipping...')
#             continue


#         ####### creating a new dict to separate trials data by stim location        
#         ####### this formats the data in an easily accessible manner w/ conditions_data
#         ####### Loop over all trials and sort them into the condition_data dictionary
#         ####### Also, extract and save wheel data within this loop

#         whlpos, whlt = wheel.position, wheel.timestamps

#         for trial_number, condition_number in stimtrial_location_dict_all.items():
#             # print(str(trial_number) + ' ' + str(condition_number))

#             reaction_time = trials.feedback_times[trial_number] - trials.goCueTrigger_times[trial_number] 
#             if np.isnan(reaction_time) == 1:
#                 reaction_time = trials.feedback_times[trial_number] - trials.stimOn_times[trial_number] ###reaction time definitions may be unreliable - any other ways to define?
#             if np.isnan(reaction_time) == 1:
#                 if np.isnan(RT_threshold) == 0:
#                     continue
#             if reaction_time > RT_threshold:
#                 if np.isnan(RT_threshold) == 0:
#                     continue

#             trials_data = {
#                 # 'intervals': trials.intervals[trial_number],
#                 'choice': trials.choice[trial_number],
#                 'reaction_times': reaction_time,
#                 'qp_times': trials.goCueTrigger_times[trial_number] - trials.intervals[trial_number][0],
#                 'contrast': signed_contrast(trials)[trial_number],
#                 # 'goCueTrigger_times': trials.goCueTrigger_times[trial_number],
#                 # 'goCue_times': trials.goCue_times[trial_number],
#                 # 'stimOn_times': trials.stimOn_times[trial_number],
#                 # 'feedback_times': trials.feedback_times[trial_number],
#                 # 'response_times': trials.response_times[trial_number],
#                 'feedbackType': trials.feedbackType[trial_number],
#                 'probabilityLeft': trials.probabilityLeft[trial_number],
#                 # 'prev_choice': trials.choice[trial_number-1]
#             }
            
#             # Append the trial data to the correct condition
#             condition_data[condition_number].append(trials_data)

#             # Now condition_data[1] contains all trials for location 1, condition_data[2] for location 2, and so on
#             # condition_data[0] contains all nonstim trials

#             #############################################################
#             ##### Load wheel data

#             if only_include_low_contrasts == 1:
#                 if ~low_contrast_trials_bool_all[k]:
#                     continue
#             # start_time = taskData[trial_number]['behavior_data']['States timestamps']['trial_start'][0][0] - 0.03 #quiescent period - first 30ms step
#             # start_time = taskData[trial_number]['behavior_data']['States timestamps']['reward'][0][0] - 0.5 #reward/error
#             # if np.isnan(start_time) == 1:
#             #     start_time = taskData[trial_number]['behavior_data']['States timestamps']['error'][0][0] - 0.5

#             if align_to == 'goCue':
#                 start_time = trials.goCue_times[trial_number] #GO CUE
#             elif align_to == 'goCue_pre':
#                 start_time = trials.goCue_times[trial_number] - 0.5 #GO CUE - 0.5s
#             elif align_to == 'QP':
#                 start_time = trials.intervals[trial_number][0] #QP / Laser onset
#             elif align_to == 'feedback':
#                 start_time = trials.feedback_times[trial_number] - 0.6

#             wheel_start_index_pre = np.searchsorted(whlt, start_time)
#             t = start_time
#             # Check the closest value by comparing the differences between 't' and its neighboring elements
#             if wheel_start_index_pre == 0:
#                 wheel_start_index = wheel_start_index_pre
#             elif wheel_start_index_pre == len(whlt):
#                 wheel_start_index = wheel_start_index_pre - 1
#             else:
#                 left_diff = t - whlt[wheel_start_index_pre - 1]
#                 right_diff = whlt[wheel_start_index_pre] - t
#                 wheel_start_index = wheel_start_index_pre - 1 if left_diff <= right_diff else wheel_start_index_pre


#             total_wheel_movement = []
#             for l in range(int(length_of_time_to_analyze_wheel_movement/interval)):
#                 t = (start_time + l*interval)# + interval #ie, steps of 100ms
#                 # wheel_end_index = np.argmin(np.abs(whlt - t))
#                 #norm_wheel_vals = whlpos[wheel_start_index:wheel_end_index]/whlpos[wheel_start_index]

#                 wheel_end_index_pre = np.searchsorted(whlt, t) #ie, steps of 100ms
#                 # Check the closest value by comparing the differences between 't' and its neighboring elements
#                 if wheel_end_index_pre == 0:
#                     wheel_end_index = wheel_end_index_pre
#                 elif wheel_end_index_pre == len(whlt):
#                     wheel_end_index = wheel_end_index_pre - 1
#                 else:
#                     left_diff = t - whlt[wheel_end_index_pre - 1]
#                     right_diff = whlt[wheel_end_index_pre] - t
#                     wheel_end_index = wheel_end_index_pre - 1 if left_diff <= right_diff else wheel_end_index_pre

#                 ##only in case where aligning to QP, do not use any wheel movement past goCue
#                 if align_to == 'QP' and trials.goCue_times[trial_number] < whlt[wheel_end_index]:
#                     total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                 ##only in case where aligning to goCue, do not use any wheel movement past feedback + 0.1
#                 elif align_to == 'goCue' and (trials.feedback_times[trial_number] + interval) < whlt[wheel_end_index]:
#                     total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                 elif align_to == 'goCue_pre' and (trials.feedback_times[trial_number] + interval) < whlt[wheel_end_index]:
#                     total_wheel_movement = np.append(total_wheel_movement,np.nan)
#                 else:
#                     total_wheel_movement = np.append(total_wheel_movement,whlpos[wheel_end_index] - whlpos[wheel_start_index])

#             ### append data here according to condition
#             if trials.probabilityLeft[trial_number] == 0.2:
#                 if len(Rblock_wheel_movements_by_condition[condition_number]) == 0:
#                     Rblock_wheel_movements_by_condition[condition_number] = total_wheel_movement
#                 else:
#                     Rblock_wheel_movements_by_condition[condition_number] = np.vstack([Rblock_wheel_movements_by_condition[condition_number],total_wheel_movement])
#             if trials.probabilityLeft[trial_number] == 0.8:
#                 if len(Lblock_wheel_movements_by_condition[condition_number]) == 0:
#                     Lblock_wheel_movements_by_condition[condition_number] = total_wheel_movement
#                 else:
#                     Lblock_wheel_movements_by_condition[condition_number] = np.vstack([Lblock_wheel_movements_by_condition[condition_number],total_wheel_movement])
#         #############################################################
            
#         # ####################################################################################
            



# if is_zapit_session == 0:
#     if num_analyzed_sessions == 0:
#         raise Exception('No sessions met criteria to be analyzed.')
    
#     # RT_threshold = 2
#     # # Create a boolean mask based on the reaction times
#     # mask = stim_trials.reaction_times <= RT_threshold
#     # for key in stim_trials.__dict__.keys():
#     #     stim_trials.__dict__[key] = stim_trials.__dict__[key][mask]

#     # mask = nonstim_trials.reaction_times <= RT_threshold
#     # for key in nonstim_trials.__dict__.keys():
#     #     nonstim_trials.__dict__[key] = nonstim_trials.__dict__[key][mask]


#     stim_trials_contrast = signed_contrast(stim_trials)
#     nonstim_trials_contrast = signed_contrast(nonstim_trials)
#     nonstim_RTs_100L = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastLeft == 1)[0]]
#     nonstim_RTs_100R = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastRight == 1)[0]]
#     nonstim_RTs_100all = np.append(nonstim_RTs_100L,nonstim_RTs_100R)
#     nonstim_RTs_25L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -25)[0]]
#     nonstim_RTs_25R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 25)[0]]
#     nonstim_RTs_25all = np.append(nonstim_RTs_25L,nonstim_RTs_25R)
#     nonstim_RTs_12L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -12.5)[0]]
#     nonstim_RTs_12R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 12)[0]]
#     nonstim_RTs_12all = np.append(nonstim_RTs_12L,nonstim_RTs_12R)
#     nonstim_RTs_6L = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == -6.25)[0]]
#     nonstim_RTs_6R = nonstim_trials.reaction_times[np.where(nonstim_trials_contrast == 6.25)[0]]
#     nonstim_RTs_6all = np.append(nonstim_RTs_6L,nonstim_RTs_6R)
#     nonstim_RTs_0L = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastLeft == 0)[0]]
#     nonstim_RTs_0R = nonstim_trials.reaction_times[np.where(nonstim_trials.contrastRight == 0)[0]]
#     nonstim_RTs_0all = np.append(nonstim_RTs_0L,nonstim_RTs_0R)
#     stim_RTs_100L = stim_trials.reaction_times[np.where(stim_trials.contrastLeft == 1)[0]]
#     stim_RTs_100R = stim_trials.reaction_times[np.where(stim_trials.contrastRight == 1)[0]]
#     stim_RTs_100all = np.append(stim_RTs_100L,stim_RTs_100R)
#     stim_RTs_25L = stim_trials.reaction_times[np.where(stim_trials_contrast == -25)[0]]
#     stim_RTs_25R = stim_trials.reaction_times[np.where(stim_trials_contrast == 25)[0]]
#     stim_RTs_25all = np.append(stim_RTs_25L,stim_RTs_25R)
#     stim_RTs_12L = stim_trials.reaction_times[np.where(stim_trials_contrast == -12.5)[0]]
#     stim_RTs_12R = stim_trials.reaction_times[np.where(stim_trials_contrast == 12)[0]]
#     stim_RTs_12all = np.append(stim_RTs_12L,stim_RTs_12R)
#     stim_RTs_6L = stim_trials.reaction_times[np.where(stim_trials_contrast == -6.25)[0]]
#     stim_RTs_6R = stim_trials.reaction_times[np.where(stim_trials_contrast == 6.25)[0]]
#     stim_RTs_6all = np.append(stim_RTs_6L,stim_RTs_6R)
#     stim_RTs_0L = stim_trials.reaction_times[np.where(stim_trials.contrastLeft == 0)[0]]
#     stim_RTs_0R = stim_trials.reaction_times[np.where(stim_trials.contrastRight == 0)[0]]
#     stim_RTs_0all = np.append(stim_RTs_0L,stim_RTs_0R)

#     nonstim_RTs_100_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 1)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 1)))]
#     nonstim_RTs_100_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 1)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 1)))]
#     nonstim_RTs_25_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.25)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.25)))]
#     nonstim_RTs_25_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.25)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.25)))]
#     nonstim_RTs_12_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.125)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.125)))]
#     nonstim_RTs_12_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.125)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.125)))]
#     nonstim_RTs_6_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0.0625)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0.0625)))]
#     nonstim_RTs_6_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0.0625)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0.0625)))]
#     nonstim_RTs_0_inblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastLeft == 0)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastRight == 0)))]
#     nonstim_RTs_0_outblock = nonstim_trials.reaction_times[np.where(((nonstim_trials.probabilityLeft == 0.8) & (nonstim_trials.contrastRight == 0)) | ((nonstim_trials.probabilityLeft == 0.2) & (nonstim_trials.contrastLeft == 0)))]
#     stim_RTs_100_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 1)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 1)))]
#     stim_RTs_100_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 1)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 1)))]
#     stim_RTs_25_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.25)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.25)))]
#     stim_RTs_25_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.25)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.25)))]
#     stim_RTs_12_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.125)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.125)))]
#     stim_RTs_12_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.125)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.125)))]
#     stim_RTs_6_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0.0625)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0.0625)))]
#     stim_RTs_6_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0.0625)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0.0625)))]
#     stim_RTs_0_inblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastLeft == 0)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastRight == 0)))]
#     stim_RTs_0_outblock = stim_trials.reaction_times[np.where(((stim_trials.probabilityLeft == 0.8) & (stim_trials.contrastRight == 0)) | ((stim_trials.probabilityLeft == 0.2) & (stim_trials.contrastLeft == 0)))]

#     nonstim_RTs_allcontrasts_inblock = np.concatenate((nonstim_RTs_0_inblock,nonstim_RTs_6_inblock,nonstim_RTs_12_inblock,nonstim_RTs_25_inblock,nonstim_RTs_100_inblock))
#     stim_RTs_allcontrasts_inblock = np.concatenate((stim_RTs_0_inblock,stim_RTs_6_inblock,stim_RTs_12_inblock,stim_RTs_25_inblock,stim_RTs_100_inblock))
#     nonstim_RTs_allcontrasts_outblock = np.concatenate((nonstim_RTs_0_outblock,nonstim_RTs_6_outblock,nonstim_RTs_12_outblock,nonstim_RTs_25_outblock,nonstim_RTs_100_outblock))
#     stim_RTs_allcontrasts_outblock = np.concatenate((stim_RTs_0_outblock,stim_RTs_6_outblock,stim_RTs_12_outblock,stim_RTs_25_outblock,stim_RTs_100_outblock))


#     ##################################################### current analysis
#     ## for assessing p-value comparing zero contrast trials
#     ## I don't know what is the correct way to do this...
#     nonstim_zero_contrast_trials = np.where(nonstim_trials_contrast == 0)[0]
#     stim_zero_contrast_trials = np.where(stim_trials_contrast == 0)[0]
#     nonstim_trials_80 = np.where(nonstim_trials.probabilityLeft == 0.8)[0]
#     nonstim_trials_20 = np.where(nonstim_trials.probabilityLeft == 0.2)[0]
#     stim_trials_80 = np.where(stim_trials.probabilityLeft == 0.8)[0]
#     stim_trials_20 = np.where(stim_trials.probabilityLeft == 0.2)[0]
#     nonstim_zero_contrast_trials_80 = np.intersect1d(nonstim_zero_contrast_trials,nonstim_trials_80)
#     nonstim_zero_contrast_trials_20 = np.intersect1d(nonstim_zero_contrast_trials,nonstim_trials_20)
#     stim_zero_contrast_trials_80 = np.intersect1d(stim_zero_contrast_trials,stim_trials_80)
#     stim_zero_contrast_trials_20 = np.intersect1d(stim_zero_contrast_trials,stim_trials_20)

#     choice_nonstim_zero_contrast_trials_80 = nonstim_trials.choice[nonstim_zero_contrast_trials_80]
#     choice_nonstim_zero_contrast_trials_20 = nonstim_trials.choice[nonstim_zero_contrast_trials_20]
#     choice_stim_zero_contrast_trials_80 = stim_trials.choice[stim_zero_contrast_trials_80]
#     choice_stim_zero_contrast_trials_20 = stim_trials.choice[stim_zero_contrast_trials_20]

#     stim_trials_data = {}
#     for pL in np.unique(stim_trials.probabilityLeft):
#         in_block = stim_trials.probabilityLeft == pL
#         xx, nn = np.unique(stim_trials_contrast[in_block], return_counts=True)
#         rightward = stim_trials.choice == -1
#         pp = np.vectorize(lambda x: np.mean(rightward[(x == stim_trials_contrast) & in_block]))(xx)
#         stim_trials_data[pL] = np.vstack((xx, nn, pp))

#     nonstim_trials_data = {}
#     for pL in np.unique(nonstim_trials.probabilityLeft):
#         in_block = nonstim_trials.probabilityLeft == pL
#         xx, nn = np.unique(nonstim_trials_contrast[in_block], return_counts=True)
#         rightward = nonstim_trials.choice == -1
#         pp = np.vectorize(lambda x: np.mean(rightward[(x == nonstim_trials_contrast) & in_block]))(xx)
#         nonstim_trials_data[pL] = np.vstack((xx, nn, pp))

#     # A colour map for the block type
#     colours = dict(zip(nonstim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:violet', 'xkcd:violet')))

#     # Increase bias bounds (kwargs defined in previous section)
#     kwargs = {
#         # parmin: The minimum allowable parameter values, in the form
#         # [bias, threshold, lapse_low, lapse_high]
#         'parmin': np.array([-100., 30., 0., 0.]),
#         # parmax: The maximum allowable parameter values
#         'parmax': np.array([100., 100., 0.3, 0.8]),
#         # Non-zero starting parameters, used to try to avoid local minima
#         'parstart': np.array([0., 80., 0., 0.4]),
#         # nfits: The number of fits to run
#         'nfits': 100
#     }
#     # kwargs['parmin'][0] = -50.
#     # kwargs['parmax'][0] = 50.


#     ######################################################REPLOT
#     f, (ax1, ax2) = plt.subplots(1, 2)

#     # For each block type, fit the data separately and plot
#     for pL, da in nonstim_trials_data.items():
#         # Fit it
#         pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);
        
#         # Print pars
#         print('prob left = {:.1f}, bias = {:2.0f}, threshold = {:2.0f}, lapse = {:.01f}, {:.01f}'.format(pL, *pars))

#         # graphics
#         x = np.arange(-100, 100)  # The x-axis values for our curve
#         ax1.plot(da[0,:], da[2,:], color = colours[pL], marker= 'o',linestyle='None')
#         ax1.plot(x, psy.erf_psycho_2gammas(pars, x), label=f'{int(pL*100)}', color=colours[pL])

#     # plt.title(ref)
#     # plt.legend()
#     # makepretty()
#     # plt.show()

#     # plt.figure()
#     for pL, da in stim_trials_data.items():
#         # Fit it
#         pars, L = psy.mle_fit_psycho(da, 'erf_psycho_2gammas', **kwargs);
        
#         # Print pars
#         print('prob left = {:.1f}, bias = {:2.0f}, threshold = {:2.0f}, lapse = {:.01f}, {:.01f}'.format(pL, *pars))

#         # graphics
#         x = np.arange(-100, 100)  # The x-axis values for our curve
#         ax2.plot(da[0,:], da[2,:], color = colours[pL], marker= 'o',linestyle='None')
#         ax2.plot(x, psy.erf_psycho_2gammas(pars, x), label=f'{int(pL*100)}', color=colours[pL])

#     # Ensure x label is not cut off
#     plt.subplots_adjust(bottom=0.15)
#     # Plot lines at zero and .5
#     ax2.plot((0, 0), (0, 1), 'k:')
#     ax2.plot((-100, 100), (.5, .5), 'k:')
#     ax1.plot((0, 0), (0, 1), 'k:')
#     ax1.plot((-100, 100), (.5, .5), 'k:')
#     # Set limits and labels
#     ax1.set(ylim=[-.05, 1.05], xlabel='contrast (%)', ylabel='proportion leftward')
#     ax2.set(ylim=[-.05, 1.05], xlabel='contrast (%)')
#     # ax1.text(-100, 0.75, 'numtrials = ' + str(np.size(nonstim_trials.contrastLeft)), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
#     # ax2.text(-100, 0.75, 'numtrials = ' + str(np.size(stim_trials.contrastLeft)), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
#     # ax2.text(10, 0.20, 'num sessions = ' + str(num_analyzed_sessions), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
#     # ax2.text(10, 0, 'num mice = ' + str(num_unique_mice), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')
#     sns.despine(offset=10, trim=True)
#     plt.suptitle(f'{state_type}')

#     # print('Number analyzed sessions =' + str(num_analyzed_sessions))
#     # print('Number analyzed mice = ' + str(num_unique_mice))

#     # Get some details for the title
#     # det = one.get_details(eid)
#     # ref = f"{datetime.fromisoformat(det['start_time']).date()}_{det['number']:d}_{det['subject']}"

#     print('numtrials nonstim = ' + str(np.size(nonstim_trials.contrastLeft)))
#     print('numtrials stim = ' + str(np.size(stim_trials.contrastLeft)))

#     bias_shift_sum_all_nonstim = bias_shift_sum_all_nonstim[~np.isnan(bias_shift_sum_all_nonstim)]
#     bias_shift_sum_all = bias_shift_sum_all[~np.isnan(bias_shift_sum_all)]
#     bias_shift_sum_all_nonstim_LC = bias_shift_sum_all_nonstim_LC[~np.isnan(bias_shift_sum_all_nonstim_LC)]
#     bias_shift_sum_all_LC = bias_shift_sum_all_LC[~np.isnan(bias_shift_sum_all_LC)]

#     bias_shift_sum_all_nonstim_LEFT = bias_shift_sum_all_nonstim_LEFT[~np.isnan(bias_shift_sum_all_nonstim_LEFT)]
#     bias_shift_sum_all_nonstim_RIGHT = bias_shift_sum_all_nonstim_RIGHT[~np.isnan(bias_shift_sum_all_nonstim_RIGHT)]
#     bias_shift_sum_all_LEFT = bias_shift_sum_all_LEFT[~np.isnan(bias_shift_sum_all_LEFT)]
#     bias_shift_sum_all_RIGHT = bias_shift_sum_all_RIGHT[~np.isnan(bias_shift_sum_all_RIGHT)]

#     bias_shift0_all_nonstim = bias_shift0_all_nonstim[~np.isnan(bias_shift0_all_nonstim)]
#     bias_shift0_all_stim = bias_shift0_all_stim[~np.isnan(bias_shift0_all_stim)]


#     statistic, pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)
#     print('fit subtract pval = ' + str(pval_all))
#     # statistic, pval = stats.ttest_rel(bias_shift0_all_nonstim,bias_shift0_all_stim)
#     statistic, pval_low = stats.ttest_rel(bias_shift_sum_all_nonstim_LC,bias_shift_sum_all_LC)
#     print('fit subtract pval low contrast = ' + str(pval_low))

#     # pvals[i] = pval
#     # print('finished round ' + str(i))
#     # statistic, pval = stats.ttest_rel(nonstim_zerocontrast_difference,stim_zerocontrast_difference)
#     # print('zero contrast subtract pval = ' + str(pval))
#     # statistic, pval = stats.ttest_rel(nonstim_sumall_difference,stim_sumall_difference)
#     # print('all contrast subtract pval = ' + str(pval))

#     print('Number analyzed sessions =' + str(num_analyzed_sessions))
#     print('Number analyzed mice = ' + str(num_unique_mice))


#     # f.suptitle(ref)
#     # ax1.legend()
#     # ax2.legend()
#     # ax1.set_ylim([-0.05,1.05])
#     f.set_size_inches(8, 4, forward=True)
#     if save_figures == 1:
#         plt.savefig(figure_save_path + figure_prefix + '_psych.png')  # Change the path as needed
#         plt.close()
#     else:
#         f.show()

#     ####### using all trials for RT/QP/biasshift measurement
#     rt_nonstimtrials_all = rt_nonstimtrials_all[~np.isnan(rt_nonstimtrials_all)]                        # IMPORTANT: MANNWHIT CANNOT TAKE ANY NAN VALUES 
#     rt_stimtrials_all = rt_stimtrials_all[~np.isnan(rt_stimtrials_all)]
#     pval_rt = stats.mannwhitneyu(rt_nonstimtrials_all,rt_stimtrials_all)

#     qp_nonstimtrials_all = qp_nonstimtrials_all[~np.isnan(qp_nonstimtrials_all)]
#     qp_stimtrials_all = qp_stimtrials_all[~np.isnan(qp_stimtrials_all)]
#     pval_qp = stats.mannwhitneyu(qp_nonstimtrials_all,qp_stimtrials_all)

#     def add_p_value_annotation_single_bar(p_value, index, height_factor=1.05):
#         plt.text(index, height_factor, f'p={p_value:.3g}', ha='center', rotation='vertical', color='w')

#     rtfig = plt.figure(figsize=[4.5,4.5])
#     plt.bar([6,7],[np.nanmean(rt_nonstimtrials_all),np.nanmean(rt_stimtrials_all)], color=['k','b'])
#     plt.errorbar(6,np.nanmean(rt_nonstimtrials_all),yerr=stats.sem(rt_nonstimtrials_all,nan_policy='omit'),color='r')
#     plt.errorbar(7,np.nanmean(rt_stimtrials_all),yerr=stats.sem(rt_stimtrials_all,nan_policy='omit'),color='r')
#     plt.bar([3,4],[np.nanmean(qp_nonstimtrials_all),np.nanmean(qp_stimtrials_all)], color=['k','b'])
#     plt.errorbar(3,np.nanmean(qp_nonstimtrials_all),yerr=stats.sem(qp_nonstimtrials_all,nan_policy='omit'),color='r')
#     plt.errorbar(4,np.nanmean(qp_stimtrials_all),yerr=stats.sem(qp_stimtrials_all,nan_policy='omit'),color='r')
#     plt.xlim(2,8)
#     plt.text(3.5, -0.2, 'Quiescent period', ha='center')  # Adjust -0.1 as needed
#     plt.text(6.5, -0.2, 'Reaction time', ha='center')  # Adjust -0.1 as needed
#     add_p_value_annotation_single_bar(pval_qp[1], 4, 0.5)  # Adjust 1.05 as needed
#     add_p_value_annotation_single_bar(pval_rt[1], 7, 0.5)  # Adjust 1.05 as needed
#     if save_figures == 1:
#         plt.savefig(figure_save_path + figure_prefix + '_QPRT.png')  # Change the path as needed
#         plt.close()
#     else:
#         plt.show()

#     # rtfig = plt.figure(figsize=[4.5,4.5])
#     # plt.bar([6,7],[np.nanmean(rt_nonstimtrials_all),np.nanmean(rt_stimtrials_all)], color=['k','b'])
#     # plt.errorbar(6,np.nanmean(rt_nonstimtrials_all),yerr=stats.sem(rt_nonstimtrials_all,nan_policy='omit'),color='r')
#     # plt.errorbar(7,np.nanmean(rt_stimtrials_all),yerr=stats.sem(rt_stimtrials_all,nan_policy='omit'),color='r')
#     # # plt.ylim(0,1)
#     # plt.show()
#     pval_all = stats.ttest_rel(bias_shift_sum_all_nonstim,bias_shift_sum_all)
#     pval_LC = stats.ttest_rel(bias_shift_sum_all_nonstim_LC,bias_shift_sum_all_LC)

#     sigfig = plt.figure(figsize=[3.5,4.5])
#     # plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim),np.nanmean(bias_shift_sum_all)], color=['k','b'])
#     # plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim),yerr=stats.sem(bias_shift_sum_all_nonstim,nan_policy='omit'),color='r')
#     # plt.errorbar(4,np.nanmean(bias_shift_sum_all),yerr=stats.sem(bias_shift_sum_all,nan_policy='omit'),color='r')
#     plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim_LC),np.nanmean(bias_shift_sum_all_LC)], color=['k','b'])
#     plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim_LC),yerr=stats.sem(bias_shift_sum_all_nonstim_LC,nan_policy='omit'),color='r')
#     plt.errorbar(4,np.nanmean(bias_shift_sum_all_LC),yerr=stats.sem(bias_shift_sum_all_LC,nan_policy='omit'),color='r')
#     plt.xlim(left=2)
#     plt.xlim(right=5)
#     plt.text(3,-0.4,'p = ' + str(pval_all)[0:7])
#     plt.text(6,-0.4,'p = ' + str(pval_low)[0:7])
#     plt.title('Bias shift; all vs low contrasts')
#     # add_p_value_annotation_single_bar(pval_all[1], 3, 0.5)  # Adjust 1.05 as needed
#     add_p_value_annotation_single_bar(pval_LC[1], 3, 0.5)  # Adjust 1.05 as needed
#     if save_figures == 1:
#         plt.savefig(figure_save_path + figure_prefix + '_bias.png')  # Change the path as needed
#         plt.close()
#     else:
#         plt.show()

#     def save_arrays(nonstim_array, stim_array, figure_prefix):
#         # Save the numpy arrays with a prefix reflecting the specific dataset/run
#         np.save(f"{figure_save_path}{figure_prefix}_bias_shift_sum_all_nonstim_LC.npy", nonstim_array)
#         np.save(f"{figure_save_path}{figure_prefix}_bias_shift_sum_all_stim_LC.npy", stim_array)

#     if save_figures == 1:
#         save_arrays(bias_shift_sum_all_nonstim_LC, bias_shift_sum_all_LC, figure_prefix)

#     # RL_bias_fig = plt.figure(figsize=[3.5,4.5])
#     # plt.bar([3,4],[np.nanmean(bias_shift_sum_all_nonstim_LEFT),np.nanmean(bias_shift_sum_all_LEFT)], color=['k','b'])
#     # plt.errorbar(3,np.nanmean(bias_shift_sum_all_nonstim_LEFT),yerr=stats.sem(bias_shift_sum_all_nonstim_LEFT,nan_policy='omit'),color='r')
#     # plt.errorbar(4,np.nanmean(bias_shift_sum_all_LEFT),yerr=stats.sem(bias_shift_sum_all_LEFT,nan_policy='omit'),color='r')
#     # plt.bar([6,7],[np.nanmean(bias_shift_sum_all_nonstim_RIGHT),np.nanmean(bias_shift_sum_all_RIGHT)], color=['k','b'])
#     # plt.errorbar(6,np.nanmean(bias_shift_sum_all_nonstim_RIGHT),yerr=stats.sem(bias_shift_sum_all_nonstim_RIGHT,nan_policy='omit'),color='r')
#     # plt.errorbar(7,np.nanmean(bias_shift_sum_all_RIGHT),yerr=stats.sem(bias_shift_sum_all_RIGHT,nan_policy='omit'),color='r')
#     # plt.xlim(left=2)
#     # plt.xlim(right=8)
#     # plt.title('Bias shift; L vs R contrasts')
#     # plt.show()

#     if separate_stim_control == 0:
#         t,p = stats.ttest_rel(bias_shift_sum_all_nonstim_LEFT,bias_shift_sum_all_LEFT)
#         print('Pvalue Left = ' + str(p))
#         t,p = stats.ttest_rel(bias_shift_sum_all_nonstim_RIGHT,bias_shift_sum_all_RIGHT)
#         print('Pvalue Right = ' + str(p))



#     ############### Chi square analysis 

#     import numpy as np
#     from scipy.stats import chi2_contingency, fisher_exact
#     from statsmodels.stats.proportion import proportion_confint

#     def calculate_bias_shift(choices, contrasts, probabilities, low_contrast_values):
#         # Filtering for all contrasts and low contrasts
#         all_contrasts = (probabilities != 0.5)
#         low_contrasts = np.isin(contrasts, low_contrast_values) & all_contrasts

#         def calculate_shift_and_counts(choices, probabilities, filter_mask):
#             right_choices = choices[filter_mask] == 1
#             left_block = probabilities[filter_mask] == 0.2
#             right_block = probabilities[filter_mask] == 0.8

#             left_block_proportion = np.mean(right_choices[left_block])
#             right_block_proportion = np.mean(right_choices[right_block])
#             shift = right_block_proportion - left_block_proportion
#             ci_low, ci_high = proportion_confint(
#                 count=np.sum(right_choices[left_block]) + np.sum(right_choices[right_block]), 
#                 nobs=np.sum(left_block) + np.sum(right_block), 
#                 method='wilson')
            
#             return shift, (ci_low, ci_high), np.sum(right_choices[left_block]), np.sum(right_choices[right_block])

#         # shift_all, ci_all = calculate_shift(choices, probabilities, all_contrasts)
#         # shift_low, ci_low = calculate_shift(choices, probabilities, low_contrasts)

#         return calculate_shift_and_counts(choices, probabilities, all_contrasts), calculate_shift_and_counts(choices, probabilities, low_contrasts)


#     def perform_statistical_test(control_counts, stim_counts):
#         table = np.array([control_counts, stim_counts])
#         chi2, p_chi2, _, _ = chi2_contingency(table)
#         _, p_fisher = fisher_exact(table)

#         return p_chi2, p_fisher

#     # Replace these with your actual data
#     mod_nonstim_trials_contrast = nonstim_trials_contrast/100
#     mod_stim_trials_contrast = stim_trials_contrast/100
#     choices_control, contrasts_control, probabilities_control = nonstim_trials.choice, mod_nonstim_trials_contrast, nonstim_trials.probabilityLeft
#     choices_stim, contrasts_stim, probabilities_stim = stim_trials.choice, mod_stim_trials_contrast, stim_trials.probabilityLeft

#     low_contrast_values = [-0.125, -0.0625, 0, 0.0625, 0.125]

#     # Calculate bias shift
#     bias_shift_control = calculate_bias_shift(choices_control, contrasts_control, probabilities_control, low_contrast_values)
#     bias_shift_stim = calculate_bias_shift(choices_stim, contrasts_stim, probabilities_stim, low_contrast_values)

#     # Perform statistical tests
#     p_chi2_all, p_fisher_all = perform_statistical_test([bias_shift_control[0][2], bias_shift_control[0][3]], [bias_shift_stim[0][2], bias_shift_stim[0][3]])
#     p_chi2_low, p_fisher_low = perform_statistical_test([bias_shift_control[1][2], bias_shift_control[1][3]], [bias_shift_stim[1][2], bias_shift_stim[1][3]])


#     print("Bias Shift - All Trials (Control):", bias_shift_control[0])
#     print("Bias Shift - Low Contrast Trials (Control):", bias_shift_control[1])
#     print("Bias Shift - All Trials (Stim):", bias_shift_stim[0])
#     print("Bias Shift - Low Contrast Trials (Stim):", bias_shift_stim[1])

#     print("\nP-values for All Trials: Chi2 =", p_chi2_all, ", Fisher's Exact =", p_fisher_all)
#     print("P-values for Low Contrast Trials: Chi2 =", p_chi2_low, ", Fisher's Exact =", p_fisher_low)

#     import matplotlib.pyplot as plt

#     # Assuming you have these variables from your previous calculations
#     bias_shift_control_all, bias_shift_control_low = bias_shift_control
#     bias_shift_stim_all, bias_shift_stim_low = bias_shift_stim

#     # Organizing data into a dictionary
#     bias_shift_data = {
#         'Control_All': {
#             'shift': bias_shift_control_all[0], 
#             'ci': bias_shift_control_all[1]
#         },
#         'Stim_All': {
#             'shift': bias_shift_stim_all[0], 
#             'ci': bias_shift_stim_all[1]
#         },
#         'Control_Low': {
#             'shift': bias_shift_control_low[0], 
#             'ci': bias_shift_control_low[1]
#         },
#         'Stim_Low': {
#             'shift': bias_shift_stim_low[0], 
#             'ci': bias_shift_stim_low[1]
#         }
#     }

#     # Preparing data for plotting
#     labels = list(bias_shift_data.keys())
#     shift_values = [bias_shift_data[label]['shift'] for label in labels]
#     ci_values = [(bias_shift_data[label]['ci'][1] - bias_shift_data[label]['ci'][0])/2 for label in labels] # Half width of CI

#     # Creating the bar plot
#     plt.figure(figsize=(6, 7))
#     bars = plt.bar(labels, shift_values, yerr=ci_values, capsize=5, color=['black', 'blue', 'black', 'blue'], ecolor='red')
#     plt.ylabel('Bias Shift')
#     plt.title('Bias Shift Comparison with Confidence Intervals')
#     plt.xticks(rotation=45)
#     # plt.grid(axis='y')

#     # Adding p-values to the plot
#     def add_p_value_annotation(bars, p_value, index, height_factor=1.09):
#         height = bars[index].get_height() * height_factor
#         plt.text(bars[index].get_x() + bars[index].get_width() / 2, height, f'p={p_value:.3g}', ha='center')


#     add_p_value_annotation(bars, p_chi2_all, 1)  # For all trials
#     add_p_value_annotation(bars, p_chi2_low, 3)  # For low contrast trials

#     if save_figures == 1:
#         plt.savefig(figure_save_path + figure_prefix + '_Chi.png')  # Change the path as needed
#         plt.close()
#     else:
#         plt.show()

#     #################################### PLOT WHEEL ##########################################
#     # colours = dict(zip(stim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:violet', 'xkcd:violet')))

#     # x_vals_for_plot = range(int(length_of_time_to_analyze_wheel_movement/interval))
#     x_vals_for_plot = np.arange(0, length_of_time_to_analyze_wheel_movement, interval)

#     mean_L_block_wheel_movements_stim = np.nanmean(Lblock_wheel_movements_stim, axis=0)
#     mean_R_block_wheel_movements_stim = np.nanmean(Rblock_wheel_movements_stim, axis=0)
#     mean_L_block_wheel_movements_nonstim = np.nanmean(Lblock_wheel_movements_nonstim, axis=0)
#     mean_R_block_wheel_movements_nonstim = np.nanmean(Rblock_wheel_movements_nonstim, axis=0)

#     plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_stim, color='xkcd:violet', linestyle='dashed')
#     plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_stim, color='xkcd:tangerine', linestyle='dashed')
#     plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_nonstim, color='xkcd:violet', linestyle='solid')
#     plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_nonstim, color='xkcd:tangerine', linestyle='solid')

#     for k in range(len(x_vals_for_plot)):
#         valid_data = Lblock_wheel_movements_stim[:,k][~np.isnan(Lblock_wheel_movements_stim[:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_stim[k], yerr=sem, color='r')
#         valid_data = Rblock_wheel_movements_stim[:,k][~np.isnan(Rblock_wheel_movements_stim[:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_stim[k], yerr=sem, color='r')
#         valid_data = Lblock_wheel_movements_nonstim[:,k][~np.isnan(Lblock_wheel_movements_nonstim[:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_nonstim[k], yerr=sem, color='k')
#         valid_data = Rblock_wheel_movements_nonstim[:,k][~np.isnan(Rblock_wheel_movements_nonstim[:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_nonstim[k], yerr=sem, color='k')

#     plt.ylabel('Total rightward wheel movement')
#     plt.xlabel('Time from ' + align_to + ' onset')
#     plt.legend(['Stim Lblock', 'Stim Rblock', 'CTR Lblock','CTR Rblock'])
#     plt.title('Wheel movement stim vs. no stim')
#     # plt.axvline(x=0.6, color='red', linestyle='dotted')
#     # plt.xlim(0,5)
#     # plt.ylim(-0.15,0.15)

#     if save_figures == 1:
#         plt.savefig(figure_save_path + figure_prefix + '_wheel.png')  # Change the path as needed
#         plt.close()
#     else:
#         plt.show()

# ###############################################################################################
# ####################### ZAPIT ANALYSIS HERE
# else:

#     ################for calculating bias values per x trials, subtracting L and R blocks at low contrasts
#     import math
#     trials_per_datapoint = 10

#     for condition in range(0, 53):
#         condition_data_Lblock_LC = [trial for trial in condition_data[condition] if trial['contrast'] < 13 and trial['probabilityLeft'] == 0.8]
#         condition_data_Rblock_LC = [trial for trial in condition_data[condition] if trial['contrast'] < 13 and trial['probabilityLeft'] == 0.2]
#         if len(condition_data_Lblock_LC) >= len(condition_data_Rblock_LC):
#             num_cycles = math.floor(len(condition_data_Rblock_LC)/trials_per_datapoint)
#         else:
#             num_cycles = math.floor(len(condition_data_Lblock_LC)/trials_per_datapoint)
#         bias_vals_all = np.empty([num_cycles])
#         bias_vals_all[:] = np.nan
#         for k in range(0, num_cycles): 
#             condition_data_Lblock_LC_percycle = condition_data_Lblock_LC[k*trials_per_datapoint:(k+1)*trials_per_datapoint]
#             condition_data_Rblock_LC_percycle = condition_data_Rblock_LC[k*trials_per_datapoint:(k+1)*trials_per_datapoint]
#             choice_vals_Lblock = np.empty([trials_per_datapoint])
#             choice_vals_Lblock[:] = np.nan
#             choice_vals_Rblock = np.empty([trials_per_datapoint])
#             choice_vals_Rblock[:] = np.nan
#             for l in range(0, trials_per_datapoint):
#                 choice_vals_Lblock[l] = condition_data_Lblock_LC_percycle[l]['choice']
#                 choice_vals_Rblock[l] = condition_data_Rblock_LC_percycle[l]['choice']
#             mean_choice_Lblock_vals = np.mean(choice_vals_Lblock)
#             mean_choice_Rblock_vals = np.mean(choice_vals_Rblock)
#             bias_val = mean_choice_Lblock_vals - mean_choice_Rblock_vals
#             bias_vals_all[k] = bias_val

#         bias_vals_LC[condition] = bias_vals_all
            
#     ##### calculate bias values at each contrast using all trials
#     contrasts = [-100.0, -25.0, -12.5, -6.25, 0.0, 6.25, 12.5, 25.0, 100.0]

#     # Initialize a dictionary to hold the bias values for each condition
#     bias_values = {cond: [] for cond in range(53)}  # 0 for nonstim, 1-52 for stim
#     left_block_pleft_vals = {cond: [] for cond in range(53)}  
#     right_block_pleft_vals = {cond: [] for cond in range(53)}  

#     # Collect bias values for each condition and contrast level
#     for contrast in contrasts:
#         # Collect biases for the nonstim condition
#         nonstim_left_prob = calculate_choice_probability(condition_data[0], 'left', contrast)
#         nonstim_right_prob = calculate_choice_probability(condition_data[0], 'right', contrast)
#         if nonstim_left_prob is not None and nonstim_right_prob is not None:
#             nonstim_bias = nonstim_left_prob - nonstim_right_prob
#             left_block_pleft_vals[0].append(nonstim_left_prob)
#             right_block_pleft_vals[0].append(nonstim_right_prob)
#             bias_values[0].append(nonstim_bias)

#         # Collect biases for each stim condition
#         for condition in range(1, 53):
#             stim_left_prob = calculate_choice_probability(condition_data[condition], 'left', contrast)
#             stim_right_prob = calculate_choice_probability(condition_data[condition], 'right', contrast)
#             if stim_left_prob is not None and stim_right_prob is not None:
#                 stim_bias = stim_left_prob - stim_right_prob
#                 left_block_pleft_vals[condition].append(stim_left_prob)
#                 right_block_pleft_vals[condition].append(stim_right_prob)
#                 bias_values[condition].append(stim_bias)
#             else: #in case there are no values, just use ones from control
#                 stim_bias = nonstim_bias
#                 left_block_pleft_vals[condition].append(nonstim_left_prob)
#                 right_block_pleft_vals[condition].append(nonstim_right_prob)
#                 bias_values[condition].append(stim_bias)
                

#     # Now perform a statistical test to compare the block bias between nonstim and each stim condition
#     comparison_results = {}
#     comparison_results2 = {}
#     for condition in range(1, 53):
#         if bias_values[0] and bias_values[condition]:  # Check if both conditions have data
#             u_stat, p_val = stats.mannwhitneyu(bias_values[0], bias_values[condition], alternative='two-sided')
#             comparison_results[condition] = p_val
#             x, p_val_ttestrel = stats.ttest_rel(bias_values[0], bias_values[condition], axis=0)
#             comparison_results2[condition] = p_val_ttestrel
#     # comparison_results contains the p-values from the Mann-Whitney U test for each condition compared to nonstim
#     [kw_statistic,kwpval] = stats.kruskal(bias_values[0],bias_values[1],bias_values[2],bias_values[3],bias_values[4],
#                     bias_values[5],bias_values[6],bias_values[7],bias_values[8],bias_values[9],
#                     bias_values[10],bias_values[11],bias_values[12],bias_values[13],bias_values[14],
#                     bias_values[15],bias_values[16],bias_values[17],bias_values[18],bias_values[19],
#                     bias_values[20],bias_values[21],bias_values[22],bias_values[23],bias_values[24],
#                     bias_values[25],bias_values[26],bias_values[27],bias_values[28],bias_values[29],
#                     bias_values[30],bias_values[31],bias_values[32],bias_values[33],bias_values[34],
#                     bias_values[35],bias_values[36],bias_values[37],bias_values[38],bias_values[39],
#                     bias_values[40],bias_values[41],bias_values[42],bias_values[43],bias_values[44],
#                     bias_values[45],bias_values[46],bias_values[47],bias_values[48],bias_values[49],
#                     bias_values[50],bias_values[51],bias_values[52])
#     [ANOVA_statistic,ANOVApval] = stats.f_oneway(bias_values[0],bias_values[1],bias_values[2],bias_values[3],bias_values[4],
#                     bias_values[5],bias_values[6],bias_values[7],bias_values[8],bias_values[9],
#                     bias_values[10],bias_values[11],bias_values[12],bias_values[13],bias_values[14],
#                     bias_values[15],bias_values[16],bias_values[17],bias_values[18],bias_values[19],
#                     bias_values[20],bias_values[21],bias_values[22],bias_values[23],bias_values[24],
#                     bias_values[25],bias_values[26],bias_values[27],bias_values[28],bias_values[29],
#                     bias_values[30],bias_values[31],bias_values[32],bias_values[33],bias_values[34],
#                     bias_values[35],bias_values[36],bias_values[37],bias_values[38],bias_values[39],
#                     bias_values[40],bias_values[41],bias_values[42],bias_values[43],bias_values[44],
#                     bias_values[45],bias_values[46],bias_values[47],bias_values[48],bias_values[49],
#                     bias_values[50],bias_values[51],bias_values[52])
            
#     # Calculate effect sizes for each condition
#     effect_sizes = {}
#     for condition, biases in bias_values.items():
#         if condition == 0 or not biases:  # Skip nonstim or empty conditions
#             continue
#         # nonstim_median_bias = np.median(bias_values[0])
#         # stim_median_bias = np.median(biases)
#         # effect_sizes[condition] = stim_median_bias - nonstim_median_bias
#         # nonstim_0_bias = bias_values[0][4]
#         # stim_0_bias = bias_values[condition][4]
#         # effect_sizes[condition] = nonstim_0_bias - stim_0_bias
#         nonstim_bias_sum = np.sum([bias_values[0][0],bias_values[0][1],bias_values[0][2],bias_values[0][3],
#                                 bias_values[0][4],bias_values[0][5],bias_values[0][6],bias_values[0][7],
#                                 bias_values[0][8]])
#         stim_bias_sum = np.sum([bias_values[condition][0],bias_values[condition][1],bias_values[condition][2],bias_values[condition][3],
#                                 bias_values[condition][4],bias_values[condition][5],bias_values[condition][6],bias_values[condition][7],
#                                 bias_values[condition][8]])
#         effect_sizes[condition] = -(stim_bias_sum - nonstim_bias_sum)/nonstim_bias_sum


#     comparison_results_LC = {}
#     for condition in range(1, 53):
#         if len(bias_vals_LC[condition]) > 0:  # Check if both conditions have data
#             x, p_val_ttestind = stats.ttest_ind(bias_vals_LC[0], bias_vals_LC[condition])
#             comparison_results_LC[condition] = p_val_ttestind
#     # comparison_results contains the p-values from the Mann-Whitney U test for each condition compared to nonstim
#     [kw_statistic,kwpval] = stats.kruskal(bias_vals_LC[0],bias_vals_LC[1],bias_vals_LC[2],bias_vals_LC[3],bias_vals_LC[4],
#                     bias_vals_LC[5],bias_vals_LC[6],bias_vals_LC[7],bias_vals_LC[8],bias_vals_LC[9],
#                     bias_vals_LC[10],bias_vals_LC[11],bias_vals_LC[12],bias_vals_LC[13],bias_vals_LC[14],
#                     bias_vals_LC[15],bias_vals_LC[16],bias_vals_LC[17],bias_vals_LC[18],bias_vals_LC[19],
#                     bias_vals_LC[20],bias_vals_LC[21],bias_vals_LC[22],bias_vals_LC[23],bias_vals_LC[24],
#                     bias_vals_LC[25],bias_vals_LC[26],bias_vals_LC[27],bias_vals_LC[28],bias_vals_LC[29],
#                     bias_vals_LC[30],bias_vals_LC[31],bias_vals_LC[32],bias_vals_LC[33],bias_vals_LC[34],
#                     bias_vals_LC[35],bias_vals_LC[36],bias_vals_LC[37],bias_vals_LC[38],bias_vals_LC[39],
#                     bias_vals_LC[40],bias_vals_LC[41],bias_vals_LC[42],bias_vals_LC[43],bias_vals_LC[44],
#                     bias_vals_LC[45],bias_vals_LC[46],bias_vals_LC[47],bias_vals_LC[48],bias_vals_LC[49],
#                     bias_vals_LC[50],bias_vals_LC[51],bias_vals_LC[52])
#     [ANOVA_statistic,ANOVApval] = stats.f_oneway(bias_vals_LC[0],bias_vals_LC[1],bias_vals_LC[2],bias_vals_LC[3],bias_vals_LC[4],
#                     bias_vals_LC[5],bias_vals_LC[6],bias_vals_LC[7],bias_vals_LC[8],bias_vals_LC[9],
#                     bias_vals_LC[10],bias_vals_LC[11],bias_vals_LC[12],bias_vals_LC[13],bias_vals_LC[14],
#                     bias_vals_LC[15],bias_vals_LC[16],bias_vals_LC[17],bias_vals_LC[18],bias_vals_LC[19],
#                     bias_vals_LC[20],bias_vals_LC[21],bias_vals_LC[22],bias_vals_LC[23],bias_vals_LC[24],
#                     bias_vals_LC[25],bias_vals_LC[26],bias_vals_LC[27],bias_vals_LC[28],bias_vals_LC[29],
#                     bias_vals_LC[30],bias_vals_LC[31],bias_vals_LC[32],bias_vals_LC[33],bias_vals_LC[34],
#                     bias_vals_LC[35],bias_vals_LC[36],bias_vals_LC[37],bias_vals_LC[38],bias_vals_LC[39],
#                     bias_vals_LC[40],bias_vals_LC[41],bias_vals_LC[42],bias_vals_LC[43],bias_vals_LC[44],
#                     bias_vals_LC[45],bias_vals_LC[46],bias_vals_LC[47],bias_vals_LC[48],bias_vals_LC[49],
#                     bias_vals_LC[50],bias_vals_LC[51],bias_vals_LC[52])

#         # Calculate effect sizes for each condition
#     effect_sizes_LC = {}
#     nonstim_bias_mean = np.mean(bias_vals_LC[0])
#     for condition in range(1, 53):
#         if len(bias_vals_LC[condition]) == 0:  # Skip empty conditions
#             continue

#         stim_bias_mean = np.mean(bias_vals_LC[condition])
#         effect_sizes_LC[condition] = -(stim_bias_mean - nonstim_bias_mean)/nonstim_bias_mean


#     # for j in stimulus_locations:
#     #     reaction_times_temp = stim_trials.reaction_times[np.where(stim_trials.stim_location == j)]
#     #     pval_rt[j] = stats.ttest_rel(reaction_times_temp,rt_nonstimtrials_all)
#     #     qp_times_temp = stim_trials.intervals[np.where(stim_trials.stim_location == j)][0] - stim_trials.stimOn_times[np.where(stim_trials.stim_location == j)]
#     #     pval_rt[j] = stats.ttest_rel(qp_times_temp,qp_nonstimtrials_all)

#     #     #not sure if correct ttest. also, may need to consider alternative way to calculate qp_nonstimtrials_all

#     #     #calculate bias shift

#     #     #calculate accuracy at high contrasts

#     ### code below opens stim locations log file and extracts stim locations AP/ML coordinates
#     import re

#     # Define a dictionary to hold the location data
#     stim_locations = {}

#     # Assume we read the file line by line
#     with open(r'C:\python\zapit_log_2024_02_28__12-41.yml', 'r') as file:
#         lines = file.readlines()

#     # Variables to keep track of the current location being processed
#     current_location = None
#     for line in lines:
#         # Remove leading/trailing whitespaces and newline characters
#         line = line.strip()

#         # Check if the line contains 'stimLocations'
#         location_match = re.search(r'stimLocations(\d+):', line)
#         if location_match:
#             # Extract the location number
#             current_location = int(location_match.group(1))
#             # Initialize the dictionary for this location
#             stim_locations[current_location] = {'ML_left': None, 'ML_right': None, 'AP': None}
#         elif line.startswith('ML: [') and current_location is not None:
#             # Extract the ML coordinates
#             ml_coords = re.findall(r'\[([-.\d]+), ([-.\d]+)\]', line)
#             if ml_coords:
#                 # Assuming the first number is left and the second is right
#                 ml_left, ml_right = map(float, ml_coords[0])
#                 stim_locations[current_location]['ML_left'] = ml_left
#                 stim_locations[current_location]['ML_right'] = ml_right
#         elif line.startswith('AP: [') and current_location is not None:
#             # Extract the AP coordinates
#             ap_coords = re.findall(r'\[([-.\d]+), ([-.\d]+)\]', line)
#             if ap_coords:
#                 # Assuming both AP values are the same
#                 ap_coord = float(ap_coords[0][0])  # Use the first AP value
#                 stim_locations[current_location]['AP'] = ap_coord

#     # Display the extracted locations
#     # print(stim_locations)

#     ##################### end locations extraction
#     from math import sqrt
#     from statsmodels.stats.proportion import proportions_ztest
#     ##################### start statistical analysis
#     # Nonstim reaction times, Lapse rate, & QP times
#     nonstim_reaction_times = [trial['reaction_times'] for trial in condition_data[0]]
#     nonstim_QP_times = [trial['qp_times'] for trial in condition_data[0]]
#     nonstim_feedback = [trial['feedbackType'] for trial in condition_data[0] if trial['contrast'] in (-100, 100)]
#     lapse_rate_nonstim = ((len(nonstim_feedback) - np.sum(nonstim_feedback))/2)/len(nonstim_feedback)
#     lapse_rate_nonstim_n = len(nonstim_feedback)

#     # Count the number of NaNs
#     # num_nans = np.sum(np.isnan(nonstim_reaction_times))
#     # print(f'Condition nonstim has {num_nans} NaNs in reaction times.')

#     # Filter out NaNs from the reaction times
#     nonstim_reaction_times = [time for time in nonstim_reaction_times if not np.isnan(time)]
#     nonstim_QP_times = [time for time in nonstim_QP_times if not np.isnan(time)]

#     mean_nonstim_RT = np.mean(nonstim_reaction_times)
#     std_nonstim_RT = np.std(nonstim_reaction_times)
#     mean_nonstim_QP = np.mean(nonstim_QP_times)
#     std_nonstim_QP = np.std(nonstim_QP_times)

#     # Results will be stored here
#     RT_analysis_results = {}
#     QP_analysis_results = {}
#     lapse_rate_results = {}
#     lapse_rate_results[0] = {'p_val': 'NaN', 'lapse rate': lapse_rate_nonstim}

#     RT_analysis_results[0] = {'mean': mean_nonstim_RT, 'std': std_nonstim_RT}
#     QP_analysis_results[0] = {'mean': mean_nonstim_QP, 'std': std_nonstim_QP}

#     # Loop through each condition in condition_data except for the nonstim condition
#     for condition_num in range(1,num_stim_locations):

#         # Extract reaction times, lapse rate, and QP times for the current condition
#         stim_reaction_times = [trial['reaction_times'] for trial in condition_data[condition_num]]
#         stim_QP_times = [trial['qp_times'] for trial in condition_data[condition_num]]
#         stim_feedback = [trial['feedbackType'] for trial in condition_data[condition_num] if trial['contrast'] in (-100, -25, 100, 25)]
#         lapse_rate_stim = ((len(stim_feedback) - np.sum(stim_feedback))/2)/len(stim_feedback)
#         lapse_rate_stim_n = len(stim_feedback)

#         # # Count the number of NaNs
#         # num_nans = np.sum(np.isnan(stim_reaction_times))
#         # # Print the number of NaNs
#         # print(f'Condition {condition_num} has {num_nans} NaNs in reaction times.')

#         # Filter out NaNs from the reaction times and QP times
#         stim_reaction_times = [time for time in stim_reaction_times if not np.isnan(time)]
#         stim_QP_times = [time for time in stim_QP_times if not np.isnan(time)]

#         mean_stim_RT = np.mean(stim_reaction_times)
#         std_stim_RT = np.std(stim_reaction_times)
#         mean_stim_QP = np.mean(stim_QP_times)
#         std_stim_QP = np.std(stim_QP_times)

#         # Perform a t-test comparing the current condition's times to the nonstim times
#         t_stat, p_val = stats.ttest_ind(stim_reaction_times, nonstim_reaction_times, equal_var=False, nan_policy='omit')
#         ### there are some nans in the data and I don't know why...
#         t_statq, p_valq = stats.ttest_ind(stim_QP_times, nonstim_QP_times, equal_var=False, nan_policy='omit')
        
#         # Calculate effect size using Cohen's d
#         cohen_d = (np.mean(stim_reaction_times) - np.mean(nonstim_reaction_times)) / np.sqrt((np.std(stim_reaction_times) ** 2 + np.std(nonstim_reaction_times) ** 2) / 2)
#         cohen_dq = (np.mean(stim_QP_times) - np.mean(nonstim_QP_times)) / np.sqrt((np.std(stim_QP_times) ** 2 + np.std(nonstim_QP_times) ** 2) / 2)

#         # Perform the two-proportion z-test to determine whether lapse rate is significant
#         stat, pval = proportions_ztest([lapse_rate_nonstim, lapse_rate_stim], [lapse_rate_nonstim_n, lapse_rate_stim_n])

#         # Store the results
#         RT_analysis_results[condition_num] = {'p_val': p_val, 'effect_size': cohen_d, 'mean': mean_stim_RT, 'std': std_stim_RT}
#         QP_analysis_results[condition_num] = {'p_val': p_valq, 'effect_size': cohen_dq, 'mean': mean_stim_QP, 'std': std_stim_QP}
#         lapse_rate_results[condition_num] = {'p_val': pval, 'lapse rate': lapse_rate_stim}


#     #####################################################################################
#     ################################## PLOT #############################################

#     num_trials_total_estimate = len(condition_data[0])*2

#     def transform_to_ccf(x, y, z, resolution=10):
#         """
#         Transform stereotaxic coordinates to CCF coordinates.
        
#         Parameters:
#         - x, y, z: Coordinates in micrometers.
#         - resolution: Resolution of the CCF volume in micrometers per pixel.
        
#         Returns:
#         - Transformed X, Y, Z coordinates in CCF space.
#         """
#         # Step 1: Center on Bregma
#         x_bregma, y_bregma, z_bregma = 540, 44, 570  # Bregma for 10um resolution
#         x -= x_bregma
#         y -= y_bregma
#         z -= z_bregma

#         # Step 2: Rotate the CCF (5 degrees in radians is approximately 0.0873)
#         angle_rad = 5 * (np.pi / 180)  # Convert 5 degrees to radians
#         X = x * np.cos(angle_rad) - y * np.sin(angle_rad)
#         Y = x * np.sin(angle_rad) + y * np.cos(angle_rad)

#         # Step 3: Squeeze the DV axis
#         Y *= 0.9434

#         # Step 4: Transform into micrometers
#         X, Y, Z = X / resolution, Y / resolution, z / resolution  # Z is not transformed other than scaling

#         return X, Y, Z

#     ########## RT
#     import matplotlib.pyplot as plt
#     import matplotlib.image as mpimg
#     import matplotlib.colors as mcolors

#     # Load your brain atlas image
#     allenCCF_data = np.load(r'C:\python\annotation_volume_10um.npy')
#     structure_tree = pd.read_csv(r'C:\python\structure_tree_safe_2017.csv')

#     def generate_mip_with_borders(annotation_volume):
#         # Assuming the AP axis is the first axis (shape is AP x DV x ML)
#         # Find the first non-zero label along the DV axis for each ML and AP coordinate
#         dorsal_surface_index = np.argmax(annotation_volume > 0, axis=1)

#         # Create an empty array for the MIP
#         dv_axis_length = annotation_volume.shape[1]
#         ap_axis_length, ml_axis_length = dorsal_surface_index.shape
#         mip = np.zeros((ap_axis_length, ml_axis_length), dtype=annotation_volume.dtype)

#         # Populate the MIP array
#         for x in range(ml_axis_length):
#             for y in range(ap_axis_length):
#                 dv_index = dorsal_surface_index[y, x]
#                 if dv_index < dv_axis_length:
#                     mip[y, x] = annotation_volume[y, dv_index, x]
        
#         # Find the gradient (edges) of the regions
#         grad_x, grad_y = np.gradient(mip)
#         edges = np.sqrt(grad_x**2 + grad_y**2)
        
#         # Set the edges to white (or any value > 0) and the rest to black
#         mip_with_borders = np.where(edges > 0, 1, 0)
        
#         return mip_with_borders

#     print('Generating max intensity projection of allen data; this will take a minute or 2')
#     dorsal_mip_with_borders = generate_mip_with_borders(allenCCF_data)

#     # Determine the extents of the image in millimeters
#     bregma = np.array([540, 0, 570])  # Bregma position in the Allen CCF (AP, DV, ML)
#     scale_factor = -100  # Scale factor

#     # Calculate the extents
#     left_extent = -bregma[2] / scale_factor
#     right_extent = (dorsal_mip_with_borders.shape[1] - bregma[2]) / scale_factor
#     lower_extent = (dorsal_mip_with_borders.shape[0] - bregma[0]) / scale_factor
#     upper_extent = -bregma[0] / scale_factor

#     # Plot the brain atlas with the correct extent
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

#     # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
#     # norm = mcolors.Normalize(vmin=-0.3, vmax=0.3)
#     norm = mcolors.Normalize(vmin = RT_analysis_results[0]['mean'] - 0.3*RT_analysis_results[0]['mean'], vmax = RT_analysis_results[0]['mean'] + 0.3*RT_analysis_results[0]['mean'])

#     # Create a ScalarMappable and initialize a colormap
#     sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

#     # Overlay the stimulation points directly since they are already in the correct scale and framework
#     for condition, coords in stim_locations.items():
#         if condition in RT_analysis_results:
#             # effect_size = RT_analysis_results[condition]['effect_size']
#             effect_size = RT_analysis_results[condition]['mean']
#             p_val = RT_analysis_results[condition]['p_val']
#             size = -100*np.log10(p_val)
#             color = sm.to_rgba(effect_size)
#             alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
#             ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
#             ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

#     # Set the axis limits if necessary to zoom in to the region of interest
#     # ax.set_xlim([-4, 4])
#     # ax.set_ylim([-6, 4])

#     # Add labels, title, etc.
#     ax.set_ylim(bottom=-2, top=4)
#     ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
#     ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
#     ax.set_title(title_text, fontsize=18)

#     # Example p-values for the legend
#     p_values = [0.001, 0.01, 0.05, 0.2]
#     sizes = [-100 * np.log10(p) for p in p_values]
#     # Creating the scatter plot
#     # Adding a scatter plot point for each example p-value
#     for p, size in zip(p_values, sizes):
#         ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
#     # Adding the legend with title
#     ax.legend(loc='upper left', labelspacing=1.5)

#     # Increase the size of the tick labels
#     ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

#     # Add a colorbar with adjusted size
#     # 'fraction' is the width of the colorbar as a fraction of the axes
#     # 'pad' is the spacing between the colorbar and the figure
#     # 'aspect' controls the ratio of the colorbar's length to its width.
#     cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
#     cbar.set_label('Reaction time (s)', fontsize=14, labelpad=15)
#     cbar.ax.tick_params(labelsize=12)
#     plt.show()

#     ############ QP
#     # Plot the brain atlas with the correct extent
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

#     # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
#     # norm = mcolors.Normalize(vmin=-0.3, vmax=0.3)
#     norm = mcolors.Normalize(vmin = QP_analysis_results[0]['mean'] - 0.3*QP_analysis_results[0]['mean'], vmax = QP_analysis_results[0]['mean'] + 0.3*QP_analysis_results[0]['mean'])

#     # Create a ScalarMappable and initialize a colormap
#     sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

#     # Overlay the stimulation points directly since they are already in the correct scale and framework
#     for condition, coords in stim_locations.items():
#         if condition in QP_analysis_results:
#             # effect_size = QP_analysis_results[condition]['effect_size']
#             effect_size = QP_analysis_results[condition]['mean']
#             p_val = QP_analysis_results[condition]['p_val']
#             size = -100*np.log10(p_val)
#             color = sm.to_rgba(effect_size)
#             alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
#             ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
#             ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

#     # Set the axis limits if necessary to zoom in to the region of interest
#     # ax.set_xlim([-4, 4])
#     # ax.set_ylim([-6, 4])

#     # Add labels, title, etc.
#     ax.set_ylim(bottom=-2, top=4)
#     ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
#     ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
#     # ax.set_title('Effect on Time spent in Quiescent Period', fontsize=18)

#     # Example p-values for the legend
#     p_values = [0.001, 0.01, 0.05, 0.2]
#     sizes = [-100 * np.log10(p) for p in p_values]
#     # Creating the scatter plot
#     # Adding a scatter plot point for each example p-value
#     for p, size in zip(p_values, sizes):
#         ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
#     # Adding the legend with title
#     ax.legend(loc='upper left', labelspacing=1.5)

#     # Increase the size of the tick labels
#     ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

#     # Add a colorbar with adjusted size
#     # 'fraction' is the width of the colorbar as a fraction of the axes
#     # 'pad' is the spacing between the colorbar and the figure
#     # 'aspect' controls the ratio of the colorbar's length to its width.
#     cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
#     cbar.set_label('Quiescent Period Time (s)', fontsize=14, labelpad=15)
#     cbar.ax.tick_params(labelsize=12)
#     plt.show()

#     ############ LAPSE RATE
#     # Plot the brain atlas with the correct extent
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

#     # Normalize effect sizes for color mapping: you may need to adjust the scale based on your data
#     # norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=lapse_rate_nonstim + 0.15)
#     norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=lapse_rate_nonstim + 0.15)
#     # norm = mcolors.Normalize(vmin=lapse_rate_nonstim, vmax=max(lapse_rate_results))

#     # Create a ScalarMappable and initialize a colormap
#     sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)

#     # Overlay the stimulation points directly since they are already in the correct scale and framework
#     for condition, coords in stim_locations.items():
#         if condition in lapse_rate_results:
#             lapse_rate = lapse_rate_results[condition]['lapse rate']
#             p_val = lapse_rate_results[condition]['p_val']
#             size = -100*np.log10(p_val)#*np.log10(p_val)
#             color = sm.to_rgba(lapse_rate)
#             alpha = 0.5 if p_val >= 0.05 else 1#max(0.1, 1 - p_val)
#             ax.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
#             ax.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

#     # Add labels, title, etc.
#     ax.set_ylim(bottom=-2, top=4)
#     ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
#     ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)
#     # ax.set_title('Effect on Time spent in Quiescent Period', fontsize=18)

#     # Example p-values for the legend
#     p_values = [0.001, 0.01, 0.05, 0.2]
#     sizes = [-100 * np.log10(p) for p in p_values]
#     # Creating the scatter plot
#     # Adding a scatter plot point for each example p-value
#     for p, size in zip(p_values, sizes):
#         ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
#     # Adding the legend with title
#     ax.legend(loc='upper left', labelspacing=1.5)

#     # Increase the size of the tick labels
#     ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

#     # Add a colorbar with adjusted size
#     # 'fraction' is the width of the colorbar as a fraction of the axes
#     # 'pad' is the spacing between the colorbar and the figure
#     # 'aspect' controls the ratio of the colorbar's length to its width.
#     cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
#     cbar.set_label('Lapse Rate', fontsize=14, labelpad=15)
#     cbar.ax.tick_params(labelsize=12)
#     plt.show()

#     ############ BIAS1
#     # Assuming stim_locations is a dictionary with coordinates for each stimulation point

#     # Plot the brain atlas with the correct extent
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

#     # Normalize effect sizes for color mapping
#     norm = mcolors.Normalize(vmin=min(effect_sizes.values()), vmax=max(effect_sizes.values()))

#     # Create a ScalarMappable and initialize a colormap
#     sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
#     # sm.set_array([])  # Only needed for older versions of matplotlib

#     # Plot the stimulation points with effect sizes and p-values
#     for condition, effect_size in effect_sizes.items():
#         coords = stim_locations[condition]
#         # p_val = comparison_results.get(condition, 1)  # Default to 1 if not found
#         p_val = comparison_results.get(condition, 1)
#         print('the p value for condition ' + str(condition) + ' = ' + str(p_val))

#         # Determine the transparency based on the p-value
#         # # alpha = 0.1 if p_val >= 0.05 else max(0.1, 1 - p_val)
#         # # alpha = max(0.1, 1 - p_val)
#         if p_val < 0.05:
#             alpha = 1
#         # elif p_val < 0.1:
#         #     alpha = 0.7
#         # elif p_val < 0.2:
#         #     alpha = 0.5
#         # elif p_val < 0.3:
#         #     alpha = 0.3
#         else:
#             alpha = 0.5
#         # alpha = 1

#         # Determine color based on effect size
#         color = sm.to_rgba(effect_size)

#         # size = 200 - 200*p_val
#         if np.isnan(p_val) == 1:
#             size = 0
#         else:
#             size = -100*np.log10(p_val)#**2

#         plt.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
#         plt.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

#         # Annotate the points with the condition number
#         # plt.text(coords['ML_left'], coords['AP'], str(condition), color='yellow', ha='center', va='center')
#         # plt.text(coords['ML_right'], coords['AP'], str(condition), color='yellow', ha='center', va='center')

#     # Add labels, title, etc.
#     ax.set_ylim(bottom=-2, top=4)
#     ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
#     ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)

#     # Example p-values for the legend
#     p_values = [0.001, 0.01, 0.05, 0.2]
#     sizes = [-100 * np.log10(p) for p in p_values]
#     # Creating the scatter plot
#     # Adding a scatter plot point for each example p-value
#     for p, size in zip(p_values, sizes):
#         ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
#     # Adding the legend with title
#     ax.legend(loc='upper left', labelspacing=1.5)

#     # Increase the size of the tick labels
#     ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

#     # Add a colorbar with adjusted size
#     # 'fraction' is the width of the colorbar as a fraction of the axes
#     # 'pad' is the spacing between the colorbar and the figure
#     # 'aspect' controls the ratio of the colorbar's length to its width.
#     cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
#     cbar.set_label('Block Bias Reduction', fontsize=14, labelpad=15)
#     cbar.ax.tick_params(labelsize=12)
#     plt.show()

#     ############ BIAS2

#     # Plot the brain atlas with the correct extent
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.imshow(dorsal_mip_with_borders, cmap='gray', extent=[left_extent, right_extent, lower_extent, upper_extent])

#     # Normalize effect sizes for color mapping
#     norm = mcolors.Normalize(vmin=min(effect_sizes_LC.values()), vmax=max(effect_sizes_LC.values()))

#     # Create a ScalarMappable and initialize a colormap
#     sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
#     # sm.set_array([])  # Only needed for older versions of matplotlib

#     # Plot the stimulation points with effect sizes and p-values
#     for condition, effect_size in effect_sizes_LC.items():
#         coords = stim_locations[condition]
#         # p_val = comparison_results.get(condition, 1)  # Default to 1 if not found
#         p_val = comparison_results_LC.get(condition, 1)
#         print('the p value for condition ' + str(condition) + ' = ' + str(p_val))

#         # Determine the transparency based on the p-value
#         if p_val < 0.05:
#             alpha = 1
#         else:
#             alpha = 0.5

#         # Determine color based on effect size
#         color = sm.to_rgba(effect_size)

#         # size = 200 - 200*p_val
#         if np.isnan(p_val) == 1:
#             size = 0
#         else:
#             size = -100*np.log10(p_val)#**2

#         plt.scatter(coords['ML_left'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)
#         plt.scatter(coords['ML_right'], coords['AP'], color=color, alpha=alpha, edgecolors='w', s=size)

#         # Annotate the points with the condition number
#         # plt.text(coords['ML_left'], coords['AP'], str(condition), color='yellow', ha='center', va='center')
#         # plt.text(coords['ML_right'], coords['AP'], str(condition), color='yellow', ha='center', va='center')

#     # Add labels, title, etc.
#     ax.set_ylim(bottom=-2, top=4)
#     ax.set_xlabel('Mediolateral Position (mm from Bregma)', fontsize=14)
#     ax.set_ylabel('Anteroposterior Position (mm from Bregma)', fontsize=14)

#     # Example p-values for the legend
#     p_values = [0.001, 0.01, 0.05, 0.2]
#     sizes = [-100 * np.log10(p) for p in p_values]
#     # Creating the scatter plot
#     # Adding a scatter plot point for each example p-value
#     for p, size in zip(p_values, sizes):
#         ax.scatter([], [], s=size, label=f'p = {p}', edgecolors='w', color='k')
#     # Adding the legend with title
#     ax.legend(loc='upper left', labelspacing=1.5)

#     # Increase the size of the tick labels
#     ax.tick_params(axis='both', which='major', labelsize=14)  # 'both' applies changes to both x and y axis

#     # Add a colorbar with adjusted size
#     # 'fraction' is the width of the colorbar as a fraction of the axes
#     # 'pad' is the spacing between the colorbar and the figure
#     # 'aspect' controls the ratio of the colorbar's length to its width.
#     cbar = plt.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04, aspect=12)
#     cbar.set_label('Block Bias Reduction (alt)', fontsize=14, labelpad=15)
#     cbar.ax.tick_params(labelsize=12)
#     plt.show()

#     ### also need to create a measure of high contrast accuracy and visualize that at each location
#     ### also, use this on nonstim trials to exclude sessions below performance threshold

#     def plot_psychometric(contrasts, left_choices, right_choices, title):
#         """
#         Plot psychometric curves for left and right block trials.
        
#         :param contrasts: Array-like, list of contrasts.
#         :param left_choices: Array-like, list of percent leftward choices for left block trials.
#         :param right_choices: Array-like, list of percent leftward choices for right block trials.
#         :param title: String, the title for the plot.
#         """
#         plt.figure(figsize=(10, 8))
#         plt.plot(contrasts, left_choices, color='blue', label='Left Block')
#         plt.plot(contrasts, right_choices, color='orange', label='Right Block')
        
#         plt.title(title)
#         plt.xlabel('Contrast')
#         plt.ylabel('% Leftward Choice')
#         plt.legend()
#         plt.show()

#     # plot_psychometric(contrasts, left_block_pleft_vals[0], right_block_pleft_vals[0], f'Condition {condition}')
#     # # Loop through each condition, including the control condition at index 0
#     # # for condition in range(1,53):

#     #################################### PLOT PSYCHOMETRIC #####################################

#     condition = 16
#     # Extract or calculate the psychometric data for the current condition
#     left_block_choices = left_block_pleft_vals[condition]
#     right_block_choices = right_block_pleft_vals[condition]

#     # Plot the psychometric curves
#     plot_psychometric(contrasts, left_block_choices, right_block_choices, f'Condition {condition}')

#     # Wait for user input to proceed to the next plot
#     # input("Press Enter to continue to the next plot...")
#     # plt.close()  # This closes the current figure before the next one is drawn

#     #################################### PLOT WHEEL ##########################################
#     ### condition defined above

#     x_vals_for_plot = np.arange(0, length_of_time_to_analyze_wheel_movement, interval)

#     mean_L_block_wheel_movements_stim = np.nanmean(Lblock_wheel_movements_by_condition[condition], axis=0)
#     mean_R_block_wheel_movements_stim = np.nanmean(Rblock_wheel_movements_by_condition[condition], axis=0)
#     mean_L_block_wheel_movements_nonstim = np.nanmean(Lblock_wheel_movements_by_condition[0], axis=0)
#     mean_R_block_wheel_movements_nonstim = np.nanmean(Rblock_wheel_movements_by_condition[0], axis=0)

#     plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_stim, color='xkcd:violet', linestyle='dashed')
#     plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_stim, color='xkcd:tangerine', linestyle='dashed')
#     plt.plot(x_vals_for_plot, mean_L_block_wheel_movements_nonstim, color='xkcd:violet', linestyle='solid')
#     plt.plot(x_vals_for_plot, mean_R_block_wheel_movements_nonstim, color='xkcd:tangerine', linestyle='solid')

#     for k in range(len(x_vals_for_plot)):
#         valid_data = Lblock_wheel_movements_by_condition[condition][:,k][~np.isnan(Lblock_wheel_movements_by_condition[condition][:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_stim[k], yerr=sem, color='r')
#         valid_data = Rblock_wheel_movements_by_condition[condition][:,k][~np.isnan(Rblock_wheel_movements_by_condition[condition][:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_stim[k], yerr=sem, color='r')
#         valid_data = Lblock_wheel_movements_by_condition[0][:,k][~np.isnan(Lblock_wheel_movements_by_condition[0][:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_L_block_wheel_movements_nonstim[k], yerr=sem, color='k')
#         valid_data = Rblock_wheel_movements_by_condition[0][:,k][~np.isnan(Rblock_wheel_movements_by_condition[0][:,k])]
#         sem = np.nanstd(valid_data, ddof=1) / np.sqrt(len(valid_data)) # calculating SEM manually
#         plt.errorbar(x_vals_for_plot[k], mean_R_block_wheel_movements_nonstim[k], yerr=sem, color='k')

#     plt.ylabel('Total leftward wheel movement')
#     plt.xlabel('Time from ' + align_to + ' onset')
#     plt.legend(['Stim Lblock', 'Stim Rblock', 'CTR Lblock','CTR Rblock'])
#     plt.title('Wheel movement stim vs. no stim')
#     # plt.axvline(x=0.6, color='red', linestyle='dotted')
#     # plt.xlim(0,5)
#     # plt.ylim(-0.15,0.15)
#     plt.show()


#     ###### Alternative plot using p values of difference between r and left blocks

#     # low_contrasts = [-100, -25, -12.5, -6.25, 0, 6.25, 12.5, 25, 100]
#     low_contrasts = [-6.25, 0, 6.25]
#     choices_by_condition = {cond: {'R_block': [], 'L_block': []} for cond in condition_data}

#     for cond, trials in condition_data.items():
#         for trial in trials:
#             if trial['contrast'] in low_contrasts:
#                 block_type = 'R_block' if trial['probabilityLeft'] == 0.2 else 'L_block'
#                 choices_by_condition[cond][block_type].append(trial['choice'])

#     from scipy.stats import ttest_ind

#     p_values = {}

#     for cond, blocks in choices_by_condition.items():
#         # Ensure there are choices in both blocks to compare
#         if blocks['R_block'] and blocks['L_block']:
#             stat, p_val = ttest_ind(blocks['R_block'], blocks['L_block'])
#             p_values[cond] = p_val
#         else:
#             p_values[cond] = np.nan  # Use NaN where we can't perform the test due to lack of data

#     import matplotlib.pyplot as plt
#     import matplotlib.colors as mcolors
#     import numpy as np

#     # Setup the figure and axes
#     fig, ax = plt.subplots(figsize=(10, 8))

#     # Create a colormap: blue for significant, red for not significant
#     cmap = plt.get_cmap('coolwarm_r')

#     # Prepare p-values: take the negative logarithm to emphasize smaller p-values
#     log_p_values = {cond: -np.log10(p_val) if p_val > 0 else 0 for cond, p_val in p_values.items()}

#     # Normalize the transformed p-values for color mapping
#     # Use min and max of the transformed p-values for normalization
#     min_log_p_val, max_log_p_val = min(log_p_values.values()), max(log_p_values.values())
#     min_log_p_val = 0.7
#     max_log_p_val = 9.5
#     norm = mcolors.Normalize(vmin=min_log_p_val, vmax=max_log_p_val)

#     # Plot each condition
#     for condition, coords in stim_locations.items():
#     # for condition, coords in islice(stim_locations.items(), len(stim_locations) - 1):
#         if condition == 52:
#             continue
#         log_p_val = log_p_values.get(condition, 0)  # Default to 0 (max p-value) if not found
#         color = cmap(norm(log_p_val))
        
#         ml_left = coords.get('ML_left')
#         ml_right = coords.get('ML_right')
#         ap = coords.get('AP')
        
#         if ml_left and ml_right and ap is not None:
#             ax.scatter(ml_left, ap, color=color, s=100, edgecolors='black', label='Left Hemisphere' if condition == 1 else "")
#             ax.scatter(ml_right, ap, color=color, s=100, edgecolors='black', label='Right Hemisphere' if condition == 1 else "")

#     # Add a colorbar to explain the mapping
#     sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
#     sm.set_array([])
#     cbar = plt.colorbar(sm, ax=ax)
#     cbar.set_label('-log10(P-value)')

#     # Add title and labels as needed
#     ax.set_title('Heatmap of -log10(P-value) for Block Choice Differences')
#     ax.set_xlabel('Mediolateral Position')
#     ax.set_ylabel('Anteroposterior Position')

#     plt.show()

### analyze wheel!

# store deviation (currently manually)

# df_deviation = pd.DataFrame(deviation, columns=['Values'])
# df_deviation.to_csv('/Users/feiyang/Projects/GLM-HMM/reversed_both0hz_snr.csv', index=False)

# test = pd.read_csv('/Users/feiyang/Projects/GLM-HMM/reversed_left50hz_zi.csv')
