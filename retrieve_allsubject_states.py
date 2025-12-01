import pickle
import requests
import os
import sys

print(os.getcwd())
new_path = '/Users/natemiska/int-brain-lab/GLM-HMM'
os.chdir(new_path)

# sys.path.append('/Users/natemiska/int-brain-lab/GLM-HMM')
sys.path.append('/Users/natemiska/int-brain-lab/ssm')
sys.path.append('/Users/natemiska/python/bias_coding')
# sys.path.append('/Users/natemiska/Projects/Reverse')

# Create panels a-c of Figure 3 of Ashwood et al. (2020)
import json
import pandas as pd
import os
from os.path import join
import matplotlib.pyplot as plt
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

one = ONE(base_url='https://alyx.internationalbrainlab.org')
# one = ONE(mode='remote')

# Settings
try:
    K = int(sys.argv[1])
except:
    K = 4
print("K =", K)
print("-------")

'''

Procedure:
    1. get the `eid`
    2. get the corresponding `subject`
    3. If trials table for `subject` exists
        - get the corresponding `hmm_params` from individual fit
       otherwise
        - get the `hmm_params` from global fit
    4. get the trials info for `eid` and format `input`
    5. run `get_marginal_posterior`
'''

# append posterior probability
def append_data(subject_dict, subject_key, trial_state, posterior_probs):
    if subject_key not in subject_dict:
        subject_dict[subject_key] = []
    subject_dict[subject_key].append(trial_state)
    subject_dict[subject_key].append(posterior_probs)



# load opto metadata 
from metadata_opto_allsessions_B import sessions, find_sessions_by_advanced_criteria

eids, trials_ranges, MouseIDs, stim_params = find_sessions_by_advanced_criteria(
    sessions, 
    # EID = lambda x: x in ['21861d63-c3be-40f4-961b-421cb5fc3913','b1582929-1117-4e44-862e-c775008ca548','c86f4ece-cb61-4f61-a32b-044cc5a7a83f','58f72a9f-471a-4889-a986-49edf7732fc9'],
    # EID = lambda x: x in ['ce616651-aba5-4754-91f3-79d5e929ec70'],
    Mouse_ID = 'SWC_NM_102',
    # Mouse_ID = lambda x: x in ['SWC_NM_072', 'SWC_NM_071', 'SWC_NM_057', 'SWC_NM_058', 'SWC_NM_081', 'SWC_NM_082', 'SWC_NM_085', 'SWC_NM_086', 'SWC_NM_090', 'SWC_NM_091'], ###zapit
    # Mouse_ID = lambda x: x in ['SWC_NM_073', 'SWC_NM_065'], # VLS mice
    # Mouse_ID = lambda x: x in ['SWC_NM_087', 'SWC_NM_073', 'SWC_NM_065', 'SWC_NM_042', 'SWC_NM_043', 'SWC_NM_038', 'SWC_NM_053'],
    # Date = '060324',
    # Hemisphere = 'both',
    # Opsin=lambda x: x in ['GtACR2', 'ChR2'],
    # Opsin='GtACR2',
    # Stimulation_Params ='zapit',
    # Stimulation_Params = 'QPRE',
    # Stimulation_Params = lambda x: x in ['QPRE', 'QPRE*'],
    # Pulse_Params = 'cont', 
    # Pulse_Params = 'motor_bilateral_mask', 
    # Pulse_Params = lambda x: x in ['50hz', '20hz', 'cont_c'],
    # Laser_V = 1,
    # Laser_V = lambda x: x in [0.7, 1],
    # Genetic_Line = 'D1-Cre',
    # Brain_Region = 'motor_bilateral',
    # Brain_Region = 'SNr',
)

"""
state_probability: {
    ['subject']: {
        ['eid']: [state trial labels] <- GLM-HMM trial-by-trial labels [1, 2, 3, 4]
                 [probability x states] <- posterior probability for all GLM-HMM states [expected: N trial x 4 states]
        
        ['eid']
        ['eid']
        ...
    }
    ['subject']    
    ...
    
    }
"""
# initialise dictionary for storing posterior probabilities 
with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
    state_probability = pickle.load(pickle_file)
    

failed_session = {}
for this_subject in np.unique(MouseIDs):

    failed_session[this_subject] = 0

    if this_subject not in state_probability:
            state_probability[this_subject] = {}


# Paths
figure_path, data_path = paths()

dict_dir = join(data_path, 'GLM-HMM')
data_dir = join(data_path, 'GLM-HMM', 'data_by_animal')
output_dir = join(figure_path, 'GLM-HMM', 'individual_sessions')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cols = ['#ff7f00', '#4daf4a', '#377eb8', '#f781bf', '#a65628', '#984ea3',
        '#999999', '#e41a1c', '#dede00']


for i, eid in enumerate(eids):

    if eid == 'b8d63536-7330-40ac-883a-7bf3da6b0215':
        continue

    try: 
        subject = one.get_details(eid)['subject']
        
        if eid not in state_probability[subject]: 
            state_probability[subject][eid] = {}  
        else:
            print(f'eid: {eid} already been previously processed. skipping...')

            # IF ACCIDENTALLY RAN SUBJECT & WOULD LIKE TO OVERWRITE/RERUN, use...
            # del state_probability['SWC_NM_065']
            continue

    except requests.HTTPError as e:
        print(f'Skipping session {eid}: No session matches the given query')
        failed_session[subject] = failed_session[subject] + 1
        continue
    details = one.get_details(eid)
    session_date = (details['date'].year, details['date'].month, details['date'].day)
    print(f"\n{i+1:03d}/{len(eids)} --> {subject}")

    figure_dir = join(output_dir, subject, eid)
    if not os.path.exists(figure_dir):
        os.makedirs(figure_dir)

    try: 
        trials = one.load_object(eid, 'trials')
    
    except Exception as e:
        print(f'Error occurred for session {eid:}: {e}')
        failed_session[subject] = failed_session[subject] + 1
        continue

    try:
        trials_df = pd.read_parquet( join(figure_dir, "trials.pqt") )

    except FileNotFoundError as e:
        print("Trials table for this session not found - this likely reflects a strange trials inconsistency that hasn't yet been resolved")
        # trials_objects_lengths = np.empty(20)
        # trials_objects_lengths[:] = np.nan
        # for j in range(0, len(trials.keys())):
        #     # print(len(trials[j]))
        #     trials_objects_lengths[j] = len(trials[j])
        try:
            trials_df = trials.to_df()
        except:
            print('creating new trials table with elements inserted to maintain correct size')
            lengths = np.empty(18)
            lengths[0] = len(trials.included)
            lengths[1] = len(trials.stimOff_times)
            lengths[2] = len(trials.stimOffTrigger_times)
            lengths[3] = len(trials.stimOnTrigger_times)
            lengths[4] = len(trials.goCueTrigger_times)
            lengths[5] = len(trials.quiescencePeriod)
            lengths[6] = len(trials.goCue_times)
            lengths[7] = len(trials.response_times)
            lengths[8] = len(trials.choice)
            lengths[9] = len(trials.stimOn_times)
            lengths[10] = len(trials.contrastLeft)
            lengths[11] = len(trials.contrastRight)
            lengths[12] = len(trials.feedback_times)
            lengths[13] = len(trials.feedbackType)
            lengths[14] = len(trials.rewardVolume)
            lengths[15] = len(trials.probabilityLeft)
            lengths[16] = len(trials.firstMovement_times)
            lengths[17] = len(trials.intervals)
            for j in range(0,17):
                if lengths[j] < max(lengths):
                    if j == 0:
                        trials.included = np.concatenate((np.array([0]), trials.included))
                    if j == 1:
                        trials.stimOff_times = np.concatenate((np.array([0]), trials.stimOff_times))
                    if j == 2:
                        trials.stimOffTrigger_times = np.concatenate((np.array([0]), trials.stimOffTrigger_times))
                    if j == 3:
                        trials.stimOnTrigger_times = np.concatenate((np.array([0]), trials.stimOnTrigger_times))
                    if j == 4:
                        trials.goCueTrigger_times = np.concatenate((np.array([0]), trials.goCueTrigger_times))
                    if j == 5:
                        trials.quiescencePeriod = np.concatenate((np.array([0]), trials.quiescencePeriod))
                    if j == 6:
                        trials.goCue_times = np.concatenate((np.array([0]), trials.goCue_times))
                    if j == 7:
                        trials.response_times = np.concatenate((np.array([0]), trials.response_times))
                    if j == 8:
                        trials.choice = np.concatenate((np.array([0]), trials.choice))
                    if j == 9:
                        trials.stimOn_times = np.concatenate((np.array([0]), trials.stimOn_times))
                    if j == 10:
                        trials.contrastLeft = np.concatenate((np.array([0]), trials.contrastLeft))
                    if j == 11:
                        trials.contrastRight = np.concatenate((np.array([0]), trials.contrastRight))
                    if j == 12:
                        trials.feedback_times = np.concatenate((np.array([0]), trials.feedback_times))
                    if j == 13:
                        trials.feedbackType = np.concatenate((np.array([0]), trials.feedbackType))
                    if j == 14:
                        trials.rewardVolume = np.concatenate((np.array([0]), trials.rewardVolume))
                    if j == 15:
                        trials.probabilityLeft = np.concatenate((np.array([0]), trials.probabilityLeft))
                    if j == 16:
                        trials.firstMovement_times = np.concatenate((np.array([0]), trials.firstMovement_times))
                    if j == 17:
                        trials.intervals = np.concatenate((np.array([0]), trials.intervals))

            trials_df = trials.to_df()
            print('trials table successfully reformatted!')
        


    # IF THE MOUSE WAS FILTERED OUT AT THE VERY BEGINNING,
    # WE WILL NOT HAVE THE PROPERLY FORMATTED DESIGN MATRIX FOR IT,
    # OR THE PARAMETERS OF THE INDIVIDUAL FIT.
    # WE CREATE THE DESIGN MATRIX FROM SCRATCH AND RUN THE GLM-HMM MODEL
    # WITH THE GLOBAL FIT PARAMETERS.
    try:

        results_dir = join(dict_dir, 'results', 'individual_fit', subject)

        np.random.seed(41)

        # Also get data for subject:
        inpt, y, session = load_data(join(data_dir, subject + '_processed.npz'))
        all_trials = pd.read_parquet( join(data_dir, subject + '_trials_table.pqt') )

        _string = "Using saved design matrix and individual fit parameters"

    except Exception as e:
        print("MISSING SUBJECT DATA:", e)

        results_dir = join(dict_dir, 'results')

        try:
            subject, stim_left, stim_right, rewarded, choice, bias_probs \
                = get_raw_data(eid, one) 
            inpt = create_design_mat(trials.choice,
                                    trials.contrastLeft,
                                    trials.contrastRight,
                                    trials.feedbackType)
            y = np.expand_dims(remap_choice_vals(trials.choice), axis=1)
            session = np.array([eid for j in range(y.shape[0])])
            _string = "Created design matrix and using global fit parameters"

        except Exception as e:
            print("ANOTHER ERROR:", e)
            print("SKIPPING SESSION")
            continue

    print(_string)

    cv_file = join(results_dir, "cvbt_folds_model.npz")
    cvbt_folds_model = load_cv_arr(cv_file)
    with open(join(results_dir, "best_init_cvbt_dict.json"), 'r') as f:
        best_init_cvbt_dict = json.load(f)

    raw_file = get_file_name_for_best_model_fold(cvbt_folds_model, K,
                                                results_dir,
                                                best_init_cvbt_dict)
    hmm_params, lls = load_glmhmm_data(raw_file)
    
    all_sessions, sess_loc = np.unique(session, return_index=True)

    # Create mask:
    # Identify violations for exclusion:
    violation_idx = np.where(y == -1)[0]
    nonviolation_idx, mask = create_violation_mask(violation_idx,
                                                inpt.shape[0])

    y[np.where(y == -1), :] = 1
    inputs, datas, train_masks = partition_data_by_session(
        np.hstack((inpt, np.ones((len(inpt), 1)))), y, mask,
        session)

    print("Computing GLM-HMM posterior")
    posterior_probs = get_marginal_posterior(inputs, datas, train_masks,
                                            hmm_params, K, range(K))
    trials_df[f"glm-hmm_{K}"] = pd.Series(list(posterior_probs))
    trials_df.to_parquet( join(figure_dir, "trials.pqt") )

    ##
    # Add posterior probabilities to dictionary
    trial_state = np.argmax(posterior_probs, axis=1) + 1  # dominant state on each trial
    state_probability[subject][eid] = [trial_state, posterior_probs] # probabilities across all states

    # Plot posterior probabilities
    fig, ax = plt.subplots()

    ax.set_ylabel("Posterior prob.")
    ax.set_xlabel("Trial")
    for k, prob in enumerate(posterior_probs.T):
        ax.plot(prob, label=f"State {k+1}", color=cols[k])
    ax.plot(trials_df.probabilityLeft, c='k', ls='--', label="P(L)")
    ax.set_title(f"{subject:} {session_date:}")
    ax.legend(loc="upper right")

    fig.savefig( join(figure_dir, f"posterior_K={K}.png"))

    plt.close(fig)

print(f'Failed sessions: {failed_session}')

# save processed dataframe
with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'wb') as pickle_file:
    pickle.dump(state_probability, pickle_file)


# double check (ALWAYS IMPORTANT OMG)
with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
    test = pickle.load(pickle_file)


"""
----------------    DATA STRUCTURE    ----------------
state_probability
(subject, eid, state label[0]; posterior probability[1])

dis/engaged_indices
(subject, eid, dis/engaged indices)

"""


# # %% BELOW IS FOR ACQUIRING PREVIOUS TRIAL GLM-HMM STATE INDICES (trial - 1)

# from metadata_opto_allsessions_B import sessions, find_sessions_by_advanced_criteria

# eids, trials_ranges, MouseIDs, stim_params = find_sessions_by_advanced_criteria(
#     sessions, 
#     # EID = lambda x: x in ['21861d63-c3be-40f4-961b-421cb5fc3913','b1582929-1117-4e44-862e-c775008ca548','c86f4ece-cb61-4f61-a32b-044cc5a7a83f','58f72a9f-471a-4889-a986-49edf7732fc9'],
#     # EID = lambda x: x in ['ce616651-aba5-4754-91f3-79d5e929ec70'],
#     # Mouse_ID = 'SWC_AY_006',
#     Mouse_ID = lambda x: x in ['SWC_NM_024', 'SWC_NM_025', 'SWC_NM_026'],
#     # Mouse_ID = lambda x: x in ['SWC_NM_087', 'SWC_NM_073', 'SWC_NM_065', 'SWC_NM_042', 'SWC_NM_043', 'SWC_NM_038', 'SWC_NM_053'],
#     # Date = '060324',
#     # Hemisphere = 'both',
#     # Opsin=lambda x: x in ['GtACR2', 'ChR2'],
#     # Opsin='GtACR2',
#     # Stimulation_Params ='zapit',
#     # Stimulation_Params = 'QPRE',
#     # Stimulation_Params = lambda x: x in ['QPRE', 'QPRE*'],
#     # Pulse_Params = 'cont', 
#     # Pulse_Params = 'motor_bilateral_mask', 
#     # Pulse_Params = lambda x: x in ['50hz', '20hz', 'cont_c'],
#     # Laser_V = 1,
#     # Laser_V = lambda x: x in [0.7, 1],
#     # Genetic_Line = 'D1-Cre',
#     # Brain_Region = 'motor_bilateral',
#     # Brain_Region = 'ZI',
# )

# """
# state_def: String, default = 'current'. Uses GlM-HMM state label for the current trial.
#                 'previous': Uses GLM-HMM state label for trial-1
#                 'following':  Uses GLM-HMM state label for trial+1

# n_states: Integer, 2: Concatenates right/left engaged into a single 'engaged' label. Likewise for 'disengaged'/
#                    4: Returns right/left engaged and right/left disengaged labels.
# """

# RT_threshold = 100 # Keep same as in concatenate_psychometric_curves.py
# state_def = 'previous'
# n_states = 2 # haven't implemented 4 states yet. 

# # load glm-hmm labels
# with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'rb') as pickle_file:
#     state_probability = pickle.load(pickle_file)

# # load trial-1 labels
# with open("/Users/natemiska/int-brain-lab/GLM-HMM/engaged_prevtrial_indices.pkl", 'rb') as pickle_file:
#     engaged_indices = pickle.load(pickle_file)
# with open("/Users/natemiska/int-brain-lab/GLM-HMM/disengaged_prevtrial_indices.pkl", 'rb') as pickle_file: 
#     disengaged_indices = pickle.load(pickle_file)

# # FOR IF YOU ARE RUNNING THE FIRST TIME (without .pkl file)
# # engaged_indices = {}
# # disengaged_indices = {}
    
# # with open("/Users/feiyang/Projects/GLM-HMM/engaged_prevtrial_indices.pkl", 'rb') as pickle_file:
# #     test_eng = pickle.load(pickle_file)
# # with open("/Users/feiyang/Projects/GLM-HMM/disengaged_prevtrial_indices.pkl", 'rb') as pickle_file: 
# #     test_dis = pickle.load(pickle_file)

# # one = ONE(base_url='https://alyx.internationalbrainlab.org')

# for i, eid in enumerate(eids): 

#     try: 
#         if eid in engaged_indices[MouseIDs[i]]:
#             print(f'eid: {eid} already been previously processed. skipping...')
#             continue
#     except: 
#         engaged_indices[MouseIDs[i]] = {}
#         disengaged_indices[MouseIDs[i]] = {}


#     try: 
#         trials = one.load_object(eid, 'trials')

#     except:
#         print('Failed to load eid = ' + eid)

#         engaged_indices[MouseIDs[i]][eid] = []
#         disengaged_indices[MouseIDs[i]][eid] = []
#         continue 

#     subject = one.get_details(eid)['subject']
#     if subject not in engaged_indices:
#         engaged_indices[subject] = {}
#         disengaged_indices[subject] = {}


#     if n_states == 2: 
#         engaged_indices[subject][eid] = []
#         disengaged_indices[subject][eid] = []
#     # elif n_states == 4:                                                                  # HAVEN'T BEEN IMPLEMENTED YET
#     #     left_engaged_indices[subject][eid] = []
#     #     left_disengaged_indices[subject][eid] = []
#     #     right_engaged_indices[subject][eid] = []
#     #     right_disengaged_indices[subject][eid] = []

#     ### retrieve opto indicies
#     if trials_ranges[i] == 'ALL':
#         trials_range = range(0,len(trials['contrastLeft']))
#     elif trials_ranges[i][-1] == 9998: # use last trial as end of range when end of range set to 9999
#         trials_range = [x for x in trials_ranges[i] if x < np.size(trials.probabilityLeft)]
#     else:
#         trials_range = trials_ranges[i]

#     stim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)
#     nonstim_trials_numbers = np.full(len(trials['contrastLeft']), np.nan)



#     try:
#         laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
#         laser_data = 1
#     except:
#         print('Laser intervals data not found for eid = ' + eid + '. Utilizing raw_behavior_data...')
#         dset = '_iblrig_taskData.raw*'
#         data_behav = one.load_dataset(eid, dataset=dset, collection='raw_behavior_data')
#         ses_path = one.eid2path(eid)
#         # ses_path = join(ses_path, 'raw_behavior_data/_iblrig_taskData.raw.jsonable')
#         taskData = load_data(ses_path) ###depricated
#         ### for some reason, I am getting an error here on older sessions. not sure what's the deal?
#         laser_data = 0

#     if laser_data == 1:
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
#     else:
#         for k in trials_range:
#             if taskData[k]['opto'] == 1:
#                 react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                 if react < RT_threshold:
#                     stim_trials_numbers[k] = k
#             else:
#                 react = trials['feedback_times'][k] - trials['goCueTrigger_times'][k]
#                 if react < RT_threshold:
#                     nonstim_trials_numbers[k] = k          


#     states = state_probability[subject][eid][0]                                                
#     modified_stim_trials = stim_trials_numbers.copy()

#     # Get indices of valid (non-NaN) values in nonstim_trials_numbers
#     valid_nonstim = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]

#     for j in range(len(stim_trials_numbers)):
#         if not np.isnan(stim_trials_numbers[j]):  # Only process non-NaN values
#             stim_value = stim_trials_numbers[j]

#             # Find the nearest smaller and larger values
#             smaller_values = valid_nonstim[valid_nonstim < stim_value]
#             larger_values = valid_nonstim[valid_nonstim > stim_value]

#             nearest_smaller = np.max(smaller_values) if smaller_values.size > 0 else np.nan
#             nearest_larger = np.min(larger_values) if larger_values.size > 0 else np.nan

#             # Determine which to use
#             if not np.isnan(nearest_smaller) and abs(stim_value - nearest_smaller) <= 10:
#                 new_state = states[int(nearest_smaller)]  # Use nearest smaller if within 10
#             elif not np.isnan(nearest_larger):  
#                 new_state = states[int(nearest_larger)]  # Otherwise, use nearest larger
#             else:
#                 new_state = np.nan  # If nothing is found, keep NaN

#             # Assign value if valid
#             if not np.isnan(new_state):
#                 modified_stim_trials[j] = new_state    

#     modified_states = np.copy(states)    
#     valid_stim_indices = ~np.isnan(stim_trials_numbers)

#     modified_states[valid_stim_indices] = modified_stim_trials[~np.isnan(modified_stim_trials)]

#     if state_def == 'previous':
#         states = modified_states

#     if n_states == 2:
#         engaged_indices[subject][eid] = np.where(np.logical_or(states == 2, states == 3))[0]  
#         disengaged_indices[subject][eid] = np.where(np.logical_or(states == 1, states == 4))[0]  


# # Save the dictionary to a pickle file
# with open("/Users/natemiska/int-brain-lab/GLM-HMM/all_subject_states.csv", 'wb') as pickle_file:
#     pickle.dump(state_probability, pickle_file)

# with open("/Users/natemiska/int-brain-lab/GLM-HMM/engaged_prevtrial_indices.pkl", "wb") as pickle_file:
#     pickle.dump(engaged_indices, pickle_file)
# with open("/Users/natemiska/int-brain-lab/GLM-HMM/disengaged_prevtrial_indices.pkl", "wb") as pickle_file:
#     pickle.dump(disengaged_indices, pickle_file)

