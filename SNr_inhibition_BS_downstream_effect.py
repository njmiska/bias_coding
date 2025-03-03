# from datetime import datetime  # Only for formatting title
# import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ibllib.io.raw_data_loaders import load_data
from one.api import ONE
# import brainbox.io.one as bbone
# from brainbox.io.one import load_spike_sorting
from brainbox.io.one import SpikeSortingLoader, load_lfp
# import brainbox.plot as bbp
from iblatlas.atlas import AllenAtlas, BrainRegions
# import brainbox.behavior.pyschofit as psy
# from ibl_pipeline import behavior, acquisition, subject
# from ibl_pipeline.analyses.behavior import PsychResultsBlock, PsychResults
from scipy import stats
import statistics

import sys
sys.path.append('/Users/natemiska/python/bias_coding')
from functions_optostim import signed_contrast, peri_event_time_histogram, generate_pseudo_sessions, isbiasblockselective_03
from metadata_optostim import pids_list_SNr_trained,pids_list_SNr_contra_trained,excitation_trials_range_list_SNr_trained,inhibition_trials_range_list_SNr_trained,excitation_trials_range_list_SNr_contra_trained,inhibition_trials_range_list_SNr_contra_trained,light_artifact_units_SNr_trained,light_artifact_units_SNr_contra_trained,pids_list_ZI_trained,pids_list_ZI_trained_contra,excitation_trials_range_list_ZI_trained,inhibition_trials_range_list_ZI_trained,excitation_trials_range_list_ZI_trained_contra,inhibition_trials_range_list_ZI_trained_contra,light_artifact_units_ZI_trained,light_artifact_units_ZI_trained_contra

one = ONE(base_url='https://alyx.internationalbrainlab.org')
ba = AllenAtlas()
br = BrainRegions()

#####################################################################################
#####################################################################################
#####################################################################################
condition = 'ZI_forBSanalysis'#'ZI_forBSanalysis'#'SNr_forBSanalysis' #'SNr_directstim'#'ZI_directstim'#'ZI_contra'#'SNr_ipsi' #'SNr_contra' #'ZI_ipsi'

onset_alignment = 'Laser onset' #'Laser onset' #'Go cue onset'

t_before = 10
t_after = 20

### Parameters
bin_size=0.05
smoothing=0.05

IBL_quality_label_threshold = 0.3

firing_rate_threshold = 1

### Options

plot_each_cluster = 1

# normalize_to_baseline = 0

# normalize_to_baseline_post_analysis = 0
# zscore_normalize = 0
# z_score_threshold = 5

# analyze_latency = 0
# use_latency_threshold = 0
# latency_threshold = 0.002
# only_analyze_responsive_units = 0
# responsive_window = 0.1


#####################################################################################
if condition == 'SNr_forBSanalysis':
    pids = pids_list_SNr_trained + pids_list_SNr_contra_trained
    excitation_trials_range_list = excitation_trials_range_list_SNr_trained + excitation_trials_range_list_SNr_contra_trained
    inhibition_trials_range_list = inhibition_trials_range_list_SNr_trained + inhibition_trials_range_list_SNr_contra_trained
    light_artifact_units_list = light_artifact_units_SNr_trained + light_artifact_units_SNr_contra_trained
elif condition == 'ZI_forBSanalysis':
    pids = pids_list_ZI_trained + pids_list_ZI_trained_contra
    excitation_trials_range_list = excitation_trials_range_list_ZI_trained + excitation_trials_range_list_ZI_trained_contra
    inhibition_trials_range_list = inhibition_trials_range_list_ZI_trained + inhibition_trials_range_list_ZI_trained_contra
    light_artifact_units_list = light_artifact_units_ZI_trained + light_artifact_units_ZI_trained_contra

# if condition == 'SNr_ipsi':
#     pids = pids_list_SNr
#     excitation_trials_range_list = excitation_trials_range_list_SNr
#     inhibition_trials_range_list = inhibition_trials_range_list_SNr
#     light_artifact_units_list = light_artifact_units_SNr
# elif condition == 'SNr_contra':
#     pids = pids_list_SNr_contra
#     excitation_trials_range_list = excitation_trials_range_list_SNr_contra
#     inhibition_trials_range_list = inhibition_trials_range_list_SNr_contra
#     light_artifact_units_list = light_artifact_units_SNr_contra
# if condition == 'ZI_ipsi':
#     pids = pids_list_ZI
#     excitation_trials_range_list = excitation_trials_range_list_ZI
#     inhibition_trials_range_list = inhibition_trials_range_list_ZI
#     light_artifact_units_list = light_artifact_units_ZI
# elif condition == 'ZI_contra':
#     pids = pids_list_ZI_contra
#     excitation_trials_range_list = excitation_trials_range_list_ZI_contra
#     inhibition_trials_range_list = inhibition_trials_range_list_ZI_contra
#     light_artifact_units_list = light_artifact_units_ZI_contra
# elif condition == 'ZI_directstim':
#     pids = pids_list_ZI_directstim
#     excitation_trials_range_list = excitation_trials_range_list_ZI_directstim
#     inhibition_trials_range_list = inhibition_trials_range_list_ZI_directstim
#     light_artifact_units_list = light_artifact_units_ZI_directstim
# elif condition == 'SNr_directstim':
#     pids = pids_list_SNr_directstim
#     excitation_trials_range_list = excitation_trials_range_list_SNr_directstim
#     inhibition_trials_range_list = inhibition_trials_range_list_SNr_directstim
#     light_artifact_units_list = light_artifact_units_SNr_directstim


clusters_of_interest = list()
acronyms_for_clusters_of_interest = list()
pids_per_cluster = list()
BS_score_per_cluster = list()
pval_ex_per_cluster = list()
pval_in_per_cluster = list()
delta_fr_nonstim_all = list()
delta_fr_inhibition_all = list()
zscore_all = list()

excitation_traces_percluster = list()
inhibition_traces_percluster = list()
nonstim_traces_percluster = list()
excitation_stds_percluster = list()
inhibition_stds_percluster = list()
nonstim_stds_percluster = list()

clusters_info_DF = pd.DataFrame()

normalize_to_baseline = 0

##### start main loop
for main_loop_num in np.arange(0,np.size(pids)):

    pid = pids[main_loop_num]
    print('starting analysis of pid = ' + pid)
    ssl = SpikeSortingLoader(pid=pid, one=one, atlas=ba)

    eid = ssl.eid
    trials = one.load_object(eid, 'trials')
    dset = '_iblrig_taskData.raw*'
    data_behav = one.load_dataset(eid, dataset=dset, collection='raw_behavior_data')
    ses_path = one.eid2path(eid)

    # LFP_data = load_lfp(eid, one=one, dataset_types=None)

    light_artifact_units = light_artifact_units_list[main_loop_num]
    excitation_trials_range = excitation_trials_range_list[main_loop_num]
    inhibition_trials_range = inhibition_trials_range_list[main_loop_num]

    probe_label = ssl.pname
    spikes, clusters, channels = ssl.load_spike_sorting()
    clusters = ssl.merge_clusters(spikes, clusters, channels)
    spike_wfs = one.load_object(ssl.eid, '_phy_spikes_subset', collection=ssl.collection)
    wf_clusterIDs = spikes['clusters'][spike_wfs['spikes']]
    clusters_labels = clusters['label']
    # clusters_ks2labels = clusters.ks2_label

    allspikes = spikes

    # spikes, clusters = load_spike_sorting(eid, one=one, probe=probe_label, spike_sorter='pykilosort')
    # clusters_labels = clusters[probe_label]['metrics']['label']
    # allspikes = spikes[probe_label]

    excitation_trials = trials.copy()
    inhibition_trials = trials.copy()
    nonstim_trials = trials.copy()
    nonstim_trials_ex = trials.copy()
    nonstim_trials_in = trials.copy()
    taskData = load_data(ses_path)
    excitation_trials_numbers = np.empty(len(taskData))
    excitation_trials_numbers[:] = np.NaN
    inhibition_trials_numbers = np.empty(len(taskData))
    inhibition_trials_numbers[:] = np.NaN
    nonstim_trials_numbers = np.empty(len(taskData))
    nonstim_trials_numbers[:] = np.NaN
    nonstim_trials_numbers_ex = np.empty(len(taskData))
    nonstim_trials_numbers_ex[:] = np.NaN
    nonstim_trials_numbers_in = np.empty(len(taskData))
    nonstim_trials_numbers_in[:] = np.NaN
    for k in excitation_trials_range:
        if taskData[k]['opto'] == 1:
            # react = trials['feedback_times'][k] - trials['goCue_times'][k]
            # if react < stim_rt_threshold:
            excitation_trials_numbers[k] = k
        else:
            # react = trials['feedback_times'][k] - trials['goCue_times'][k]
            # if react < stim_rt_threshold:
            nonstim_trials_numbers[k] = k
            nonstim_trials_numbers_ex[k] = k
    for k in inhibition_trials_range:
        if taskData[k]['opto'] == 1:
            # react = trials['feedback_times'][k] - trials['goCue_times'][k]
            # if react < stim_rt_threshold:
            inhibition_trials_numbers[k] = k
        else:
            # react = trials['feedback_times'][k] - trials['goCue_times'][k]
            # if react < stim_rt_threshold:
            nonstim_trials_numbers[k] = k
            nonstim_trials_numbers_in[k] = k

    excitation_trials_numbers = excitation_trials_numbers[~np.isnan(excitation_trials_numbers)]
    inhibition_trials_numbers = inhibition_trials_numbers[~np.isnan(inhibition_trials_numbers)]
    nonstim_trials_numbers = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]
    nonstim_trials_numbers_ex = nonstim_trials_numbers_ex[~np.isnan(nonstim_trials_numbers_ex)]
    nonstim_trials_numbers_in = nonstim_trials_numbers_in[~np.isnan(nonstim_trials_numbers_in)]
    excitation_trials_numbers = excitation_trials_numbers.astype(int)
    inhibition_trials_numbers = inhibition_trials_numbers.astype(int)
    nonstim_trials_numbers = nonstim_trials_numbers.astype(int)
    nonstim_trials_numbers_ex = nonstim_trials_numbers_ex.astype(int)
    nonstim_trials_numbers_in = nonstim_trials_numbers_in.astype(int)

    if pid == 'e44cb3ae-d436-4149-9110-415a276fb58e':
        trials_to_remove = list([6, 9, 10, 11, 15, 17, 23, 26, 28, 30, 31, 32, 39, 41, 44, 46, 50, 51, 53, 54, 63, 64, 70, 71, 72, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 89, 91, 92, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 111, 113, 114, 117, 118, 119, 123, 125, 126, 130, 131, 133, 134, 135, 136, 137, 139, 140, 143, 144, 145, 146, 149, 150, 156, 157, 166, 169, 170, 171, 172, 173, 175, 176, 178, 179, 183, 190, 191, 192, 193, 194, 195, 197, 198, 204])
        for f in trials_to_remove:
            if np.where(excitation_trials_numbers == f)[0].size == 1:
                excitation_trials_numbers = excitation_trials_numbers[np.where(excitation_trials_numbers != f)]
            if np.where(inhibition_trials_numbers == f)[0].size == 1:
                inhibition_trials_numbers = inhibition_trials_numbers[np.where(inhibition_trials_numbers != f)]
            if np.where(nonstim_trials_numbers == f)[0].size == 1:
                nonstim_trials_numbers = nonstim_trials_numbers[np.where(nonstim_trials_numbers != f)]
            if np.where(nonstim_trials_numbers_ex == f)[0].size == 1:
                nonstim_trials_numbers_ex = nonstim_trials_numbers_ex[np.where(nonstim_trials_numbers_ex != f)]
            if np.where(nonstim_trials_numbers_in == f)[0].size == 1:
                nonstim_trials_numbers_in = nonstim_trials_numbers_in[np.where(nonstim_trials_numbers_in != f)]
    if pid == 'bfa8f605-2eda-4b31-80fb-4a889fa0e22a':
        trials_to_remove = list([6, 7, 10, 17, 18, 19, 20, 21, 22, 23, 31, 34, 35, 36, 45, 47, 49, 50, 51, 52, 53, 57, 58, 59, 60, 63, 72, 73, 74, 75, 79, 80, 84, 87, 88, 89, 93, 94, 95, 97, 99, 100, 103, 104, 108, 109, 110, 112, 114, 115, 116, 117, 120, 123, 124, 126, 127, 128, 129, 130, 135, 142, 143, 145, 146, 147, 149, 150, 154, 155, 159, 160, 165, 166, 167, 168, 169, 170, 177, 179, 182, 183, 184, 185, 188, 189, 191, 192, 193, 196, 202, 204, 206, 207, 209, 211, 212, 215, 219, 225, 227, 232, 234, 235, 237, 238, 239, 240, 244, 249, 250, 251, 252, 253, 256, 260, 262, 266, 268, 270, 271, 272, 275, 277, 280, 281, 282, 283, 284, 285, 288, 290, 294, 303, 308, 310, 313, 317, 318, 321, 326, 334, 336, 342, 343, 344, 345, 352, 353, 357, 363, 365])
        for f in trials_to_remove:
            if np.where(excitation_trials_numbers == f)[0].size == 1:
                excitation_trials_numbers = excitation_trials_numbers[np.where(excitation_trials_numbers != f)]
            if np.where(inhibition_trials_numbers == f)[0].size == 1:
                inhibition_trials_numbers = inhibition_trials_numbers[np.where(inhibition_trials_numbers != f)]
            if np.where(nonstim_trials_numbers == f)[0].size == 1:
                nonstim_trials_numbers = nonstim_trials_numbers[np.where(nonstim_trials_numbers != f)]
            if np.where(nonstim_trials_numbers_ex == f)[0].size == 1:
                nonstim_trials_numbers_ex = nonstim_trials_numbers_ex[np.where(nonstim_trials_numbers_ex != f)]
            if np.where(nonstim_trials_numbers_in == f)[0].size == 1:
                nonstim_trials_numbers_in = nonstim_trials_numbers_in[np.where(nonstim_trials_numbers_in != f)]
    if pid == '9fedd1c6-33eb-48b6-b508-8deebe3ee44c':
        trials_to_remove = list([1,2,3,20,32,33,35,36,37,42,46,47,48,57,61,64,82,83,84,85,86,87,90,95,104,106,109,110,116,117,124,129,130,131,132,136,138,140,141,142,149,153,156,158])
        for f in trials_to_remove:
            if np.where(excitation_trials_numbers == f)[0].size == 1:
                excitation_trials_numbers = excitation_trials_numbers[np.where(excitation_trials_numbers != f)]
            if np.where(inhibition_trials_numbers == f)[0].size == 1:
                inhibition_trials_numbers = inhibition_trials_numbers[np.where(inhibition_trials_numbers != f)]
            if np.where(nonstim_trials_numbers == f)[0].size == 1:
                nonstim_trials_numbers = nonstim_trials_numbers[np.where(nonstim_trials_numbers != f)]
            if np.where(nonstim_trials_numbers_ex == f)[0].size == 1:
                nonstim_trials_numbers_ex = nonstim_trials_numbers_ex[np.where(nonstim_trials_numbers_ex != f)]
            if np.where(nonstim_trials_numbers_in == f)[0].size == 1:
                nonstim_trials_numbers_in = nonstim_trials_numbers_in[np.where(nonstim_trials_numbers_in != f)]

    # if use_trials_after_stim == 1:
    #     stim_trials_numbers = stim_trials_numbers +1
    #     if stim_trials_numbers[np.size(stim_trials_numbers)-1] == len(trials['contrastLeft']):
    #         stim_trials_numbers = stim_trials_numbers[range(len(stim_trials_numbers)-1)]

    excitation_trials.contrastRight = trials.contrastRight[excitation_trials_numbers]
    excitation_trials.contrastLeft = trials.contrastLeft[excitation_trials_numbers]
    excitation_trials.goCueTrigger_times = trials.goCueTrigger_times[excitation_trials_numbers]
    excitation_trials.feedback_times = trials.feedback_times[excitation_trials_numbers]
    excitation_trials.response_times = trials.response_times[excitation_trials_numbers]
    excitation_trials.feedbackType = trials.feedbackType[excitation_trials_numbers]
    excitation_trials.goCue_times = trials.goCue_times[excitation_trials_numbers]
    excitation_trials.firstMovement_times = trials.firstMovement_times[excitation_trials_numbers]
    # excitation_trials.excitationOnTrigger_times = trials.stimOnTrigger_times[excitation_trials_numbers]
    excitation_trials.probabilityLeft = trials.probabilityLeft[excitation_trials_numbers]
    excitation_trials.stimOn_times = trials.stimOn_times[excitation_trials_numbers]
    excitation_trials.choice = trials.choice[excitation_trials_numbers]
    excitation_trials.rewardVolume = trials.rewardVolume[excitation_trials_numbers]
    # excitation_trials.included = trials.included[excitation_trials_numbers]
    excitation_trials.intervals = trials.intervals[excitation_trials_numbers]

    inhibition_trials.contrastRight = trials.contrastRight[inhibition_trials_numbers]
    inhibition_trials.contrastLeft = trials.contrastLeft[inhibition_trials_numbers]
    inhibition_trials.goCueTrigger_times = trials.goCueTrigger_times[inhibition_trials_numbers]
    inhibition_trials.feedback_times = trials.feedback_times[inhibition_trials_numbers]
    inhibition_trials.response_times = trials.response_times[inhibition_trials_numbers]
    inhibition_trials.feedbackType = trials.feedbackType[inhibition_trials_numbers]
    inhibition_trials.goCue_times = trials.goCue_times[inhibition_trials_numbers]
    inhibition_trials.firstMovement_times = trials.firstMovement_times[inhibition_trials_numbers]
    # inhibition_trials.inhibitionOnTrigger_times = trials.stimOnTrigger_times[inhibition_trials_numbers]
    inhibition_trials.probabilityLeft = trials.probabilityLeft[inhibition_trials_numbers]
    inhibition_trials.stimOn_times = trials.stimOn_times[inhibition_trials_numbers]
    inhibition_trials.choice = trials.choice[inhibition_trials_numbers]
    inhibition_trials.rewardVolume = trials.rewardVolume[inhibition_trials_numbers]
    # inhibition_trials.included = trials.included[inhibition_trials_numbers]
    inhibition_trials.intervals = trials.intervals[inhibition_trials_numbers]
    nonstim_trials.contrastRight = trials.contrastRight[nonstim_trials_numbers]
    nonstim_trials.contrastLeft = trials.contrastLeft[nonstim_trials_numbers]
    nonstim_trials.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers]
    nonstim_trials.feedback_times = trials.feedback_times[nonstim_trials_numbers]
    nonstim_trials.response_times = trials.response_times[nonstim_trials_numbers]
    nonstim_trials.feedbackType = trials.feedbackType[nonstim_trials_numbers]
    nonstim_trials.goCue_times = trials.goCue_times[nonstim_trials_numbers]
    nonstim_trials.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers]
    # nonstim_trials.stimOnTrigger_times = trials.stimOnTrigger_times[nonstim_trials_numbers]
    nonstim_trials.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers]
    nonstim_trials.stimOn_times = trials.stimOn_times[nonstim_trials_numbers]
    nonstim_trials.choice = trials.choice[nonstim_trials_numbers]
    nonstim_trials.rewardVolume = trials.rewardVolume[nonstim_trials_numbers]
    # nonstim_trials.included = trials.included[nonstim_trials_numbers]
    nonstim_trials.intervals = trials.intervals[nonstim_trials_numbers]
    nonstim_trials_ex.contrastRight = trials.contrastRight[nonstim_trials_numbers_ex]
    nonstim_trials_ex.contrastLeft = trials.contrastLeft[nonstim_trials_numbers_ex]
    nonstim_trials_ex.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.feedback_times = trials.feedback_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.response_times = trials.response_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.feedbackType = trials.feedbackType[nonstim_trials_numbers_ex]
    nonstim_trials_ex.goCue_times = trials.goCue_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers_ex]
    # nonstim_trials_ex.stimOnTrigger_times = trials.stimOnTrigger_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers_ex]
    nonstim_trials_ex.stimOn_times = trials.stimOn_times[nonstim_trials_numbers_ex]
    nonstim_trials_ex.choice = trials.choice[nonstim_trials_numbers_ex]
    nonstim_trials_ex.rewardVolume = trials.rewardVolume[nonstim_trials_numbers_ex]
    # nonstim_trials_ex.included = trials.included[nonstim_trials_numbers_ex]
    nonstim_trials_ex.intervals = trials.intervals[nonstim_trials_numbers_ex]
    nonstim_trials_in.contrastRight = trials.contrastRight[nonstim_trials_numbers_in]
    nonstim_trials_in.contrastLeft = trials.contrastLeft[nonstim_trials_numbers_in]
    nonstim_trials_in.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers_in]
    nonstim_trials_in.feedback_times = trials.feedback_times[nonstim_trials_numbers_in]
    nonstim_trials_in.response_times = trials.response_times[nonstim_trials_numbers_in]
    nonstim_trials_in.feedbackType = trials.feedbackType[nonstim_trials_numbers_in]
    nonstim_trials_in.goCue_times = trials.goCue_times[nonstim_trials_numbers_in]
    nonstim_trials_in.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers_in]
    # nonstim_trials_in.stimOnTrigger_times = trials.stimOnTrigger_times[nonstim_trials_numbers_in]
    nonstim_trials_in.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers_in]
    nonstim_trials_in.stimOn_times = trials.stimOn_times[nonstim_trials_numbers_in]
    nonstim_trials_in.choice = trials.choice[nonstim_trials_numbers_in]
    nonstim_trials_in.rewardVolume = trials.rewardVolume[nonstim_trials_numbers_in]
    # nonstim_trials_in.included = trials.included[nonstim_trials_numbers_in]
    nonstim_trials_in.intervals = trials.intervals[nonstim_trials_numbers_in]

    excitation_trials_contrast = signed_contrast(excitation_trials)
    inhibition_trials_contrast = signed_contrast(inhibition_trials)
    nonstim_trials_contrast = signed_contrast(nonstim_trials)
    nonstim_trials_ex_contrast = signed_contrast(nonstim_trials_ex)
    nonstim_trials_in_contrast = signed_contrast(nonstim_trials_in)

    brain_acronyms_percluster = clusters['acronym']

    ######copypasta ; turn this shit into a function or something
    trials_leftprob = trials.probabilityLeft
    filterval = 10 ###number of trials to remove at beginning of block
    early_block_trials_threshold = 15
    late_block_trials_threshold = 16
    earlytrials_50 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    latetrials_50 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    earlytrials_20 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    latetrials_20 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    earlytrials_80 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    latetrials_80 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_50 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_20 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_80 = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_20_index = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_80_index = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_20_index_filtered = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrialcounts_80_index_filtered = np.zeros((1, np.size(trials_leftprob)), dtype=int)
    alltrials_block_length = np.zeros((1, np.size(trials_leftprob)))
    previous_trial_block_ID = 0.5
    current_trial_length = 0
    for l in range(0, np.size(trials_leftprob)):
        current_trial_block_ID = trials_leftprob[l]
        if current_trial_block_ID == previous_trial_block_ID:
            current_trial_length = current_trial_length + 1
            alltrials_block_length[:,l] = current_trial_length
            if current_trial_block_ID == 0.5:
                alltrialcounts_50[:,l] = current_trial_length
            if current_trial_block_ID == 0.2:
                alltrialcounts_20[:,l] = current_trial_length
                alltrialcounts_20_index[:,l] = l
                if current_trial_length > filterval:
                    alltrialcounts_20_index_filtered[:,l] = l
            if current_trial_block_ID == 0.8:
                alltrialcounts_80[:,l] = current_trial_length
                alltrialcounts_80_index[:,l] = l
                if current_trial_length > filterval:
                    alltrialcounts_80_index_filtered[:,l] = l
            if current_trial_block_ID == 0.5 and current_trial_length <= early_block_trials_threshold:
                earlytrials_50[:,l] = l
            if current_trial_block_ID == 0.5 and current_trial_length >= early_block_trials_threshold:
                latetrials_50[:,l] = l
            if current_trial_block_ID == 0.2 and current_trial_length <= early_block_trials_threshold:
                earlytrials_20[:,l] = l
            if current_trial_block_ID == 0.2 and current_trial_length >= early_block_trials_threshold:
                latetrials_20[:,l] = l
            if current_trial_block_ID == 0.8 and current_trial_length <= early_block_trials_threshold:
                earlytrials_80[:,l] = l
            if current_trial_block_ID == 0.8 and current_trial_length >= early_block_trials_threshold:
                latetrials_80[:,l] = l
        else:
            current_trial_length = 1
            alltrials_block_length[:,l] = 1
            if current_trial_block_ID == 0.5:
                alltrialcounts_50[:,l] = 1
            if current_trial_block_ID == 0.2:
                alltrialcounts_20[:,l] = 1
            if current_trial_block_ID == 0.8:
                alltrialcounts_80[:,l] = 1
            if current_trial_block_ID == 0.5:
                earlytrials_50[:,l] = l
            if current_trial_block_ID == 0.2:
                earlytrials_20[:,l] = l
            if current_trial_block_ID == 0.8:
                earlytrials_80[:,l] = l

        previous_trial_block_ID = current_trial_block_ID

    earlytrials_50 = earlytrials_50[(0.1 < earlytrials_50)]
    latetrials_50 = latetrials_50[(0.1 < latetrials_50)]
    earlytrials_20 = earlytrials_20[(0.1 < earlytrials_20)]
    latetrials_20 = latetrials_20[(0.1 < latetrials_20)]
    earlytrials_80 = earlytrials_80[(0.1 < earlytrials_80)]
    latetrials_80 = latetrials_80[(0.1 < latetrials_80)]
    alltrialcounts_80_index_filtered = alltrialcounts_80_index_filtered[(0.1 < alltrialcounts_80_index_filtered)]
    alltrialcounts_20_index_filtered = alltrialcounts_20_index_filtered[(0.1 < alltrialcounts_20_index_filtered)]

    inhibition_trials_numbers_on_80_block = list(set(inhibition_trials_numbers).intersection(alltrialcounts_80_index_filtered))
    inhibition_trials_numbers_on_20_block = list(set(inhibition_trials_numbers).intersection(alltrialcounts_20_index_filtered))

    ###############
    ### could use nonstim_trials_numbers_in, though that includes less trials and also is not what is used for BS calculation
    nonstim_trials_numbers_on_80_block = list(set(nonstim_trials_numbers_in).intersection(alltrialcounts_80_index_filtered))
    nonstim_trials_numbers_on_20_block = list(set(nonstim_trials_numbers_in).intersection(alltrialcounts_20_index_filtered))
    # nonstim_trials_numbers_on_80_block = list(set(nonstim_trials_numbers).intersection(alltrialcounts_80_index_filtered))
    # nonstim_trials_numbers_on_20_block = list(set(nonstim_trials_numbers).intersection(alltrialcounts_20_index_filtered))

    inhibition_trials_80 = trials.copy()
    inhibition_trials_20 = trials.copy()
    nonstim_trials_80 = trials.copy()
    nonstim_trials_20 = trials.copy()
    inhibition_trials_80.contrastRight = trials.contrastRight[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.contrastLeft = trials.contrastLeft[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.goCueTrigger_times = trials.goCueTrigger_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.feedback_times = trials.feedback_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.response_times = trials.response_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.feedbackType = trials.feedbackType[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.goCue_times = trials.goCue_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.firstMovement_times = trials.firstMovement_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.probabilityLeft = trials.probabilityLeft[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.stimOn_times = trials.stimOn_times[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.choice = trials.choice[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.rewardVolume = trials.rewardVolume[inhibition_trials_numbers_on_80_block]
    inhibition_trials_80.intervals = trials.intervals[inhibition_trials_numbers_on_80_block]
    inhibition_trials_20.contrastRight = trials.contrastRight[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.contrastLeft = trials.contrastLeft[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.goCueTrigger_times = trials.goCueTrigger_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.feedback_times = trials.feedback_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.response_times = trials.response_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.feedbackType = trials.feedbackType[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.goCue_times = trials.goCue_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.firstMovement_times = trials.firstMovement_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.probabilityLeft = trials.probabilityLeft[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.stimOn_times = trials.stimOn_times[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.choice = trials.choice[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.rewardVolume = trials.rewardVolume[inhibition_trials_numbers_on_20_block]
    inhibition_trials_20.intervals = trials.intervals[inhibition_trials_numbers_on_20_block]

    nonstim_trials_80.contrastRight = trials.contrastRight[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.contrastLeft = trials.contrastLeft[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.feedback_times = trials.feedback_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.response_times = trials.response_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.feedbackType = trials.feedbackType[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.goCue_times = trials.goCue_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.stimOn_times = trials.stimOn_times[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.choice = trials.choice[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.rewardVolume = trials.rewardVolume[nonstim_trials_numbers_on_80_block]
    nonstim_trials_80.intervals = trials.intervals[nonstim_trials_numbers_on_80_block]
    nonstim_trials_20.contrastRight = trials.contrastRight[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.contrastLeft = trials.contrastLeft[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.goCueTrigger_times = trials.goCueTrigger_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.feedback_times = trials.feedback_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.response_times = trials.response_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.feedbackType = trials.feedbackType[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.goCue_times = trials.goCue_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.firstMovement_times = trials.firstMovement_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.probabilityLeft = trials.probabilityLeft[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.stimOn_times = trials.stimOn_times[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.choice = trials.choice[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.rewardVolume = trials.rewardVolume[nonstim_trials_numbers_on_20_block]
    nonstim_trials_20.intervals = trials.intervals[nonstim_trials_numbers_on_20_block]

    ###generate 1000 pseudo sessions
    pseudo_20_index_filtered,pseudo_80_index_filtered = generate_pseudo_sessions(trials)

    # for j in clusters[probe_label].metrics['cluster_id']:
    for j in clusters['cluster_id']:
        
        if np.isin(j,light_artifact_units):
            continue
        if clusters_labels[j] < IBL_quality_label_threshold:
            continue
        print('cluster # = ' + str(j) + ', label = ' + str(clusters_labels[j]) + ', depth = ' + str(clusters.depths[j]) + ', region = ' + brain_acronyms_percluster[j])

        # brain_region = brain_acronyms_percluster[j]

        # if clusters.depths[j] < 1300:
        #     continue

        current_cluster_spike_indices = np.where(allspikes.clusters == j)
        current_cluster_spike_indices = current_cluster_spike_indices[0]
        current_cluster_spike_times = allspikes.times[current_cluster_spike_indices]

        ### get waveforms
        wf_idx = np.where(wf_clusterIDs == j)[0]
        wfs = spike_wfs['waveforms'][wf_idx, :, :]
        # Compute average waveform on channel with max signal (chn_index 0)
        wf_avg_chn_max = np.mean(wfs[:, :, 0], axis=0)
        wf_avg_chn_max_nonnorm = wf_avg_chn_max
        wf_avg_chn_max = wf_avg_chn_max - np.mean(wf_avg_chn_max[0:15])

        if np.size(wf_idx) < 5:  #this is strangely way lower than total spike count
            print('Not enough spikes for waveform analysis, skipping...')
            plt.close('all')
            continue

        if max(wf_avg_chn_max) > 4e-4 or min(wf_avg_chn_max) < -4e-4:
        # if max(wf_avg_chn_max) < 4e-4 or min(wf_avg_chn_max) > -4e-4:
            print('Light artifact unit, skipping...')
            plt.close('all')
            continue

        spike_times_per_cluster = spikes.times[np.where(spikes.clusters == j)]
        firing_rate = np.size(spike_times_per_cluster)/spikes.times[np.size(spikes.times)-1]
        # if clusters['firing_rate'][j] <= firing_rate_threshold:
        if firing_rate <= firing_rate_threshold:
            print('Firing rate below 1hz, skipping...')
            plt.close('all')
            continue

        # try:
        if plot_each_cluster == 1:
            plt.rcParams["figure.figsize"] = (15,6)
            fig, (ax1,ax2,ax3) = plt.subplots(1, 3)
        else:
            ax1 = None
            ax2 = None
            ax3 = None

        if onset_alignment == 'Laser onset':
            PETH1_onset = nonstim_trials_80.intervals[:,0]
            PETH2_onset = inhibition_trials_80.intervals[:,0]
            PETH3_onset = nonstim_trials_20.intervals[:,0]
            PETH4_onset = inhibition_trials_20.intervals[:,0]
            PETH5_onset = nonstim_trials.intervals[:,0]
            PETH6_onset = inhibition_trials.intervals[:,0]
        else:
            PETH1_onset = nonstim_trials_80.goCue_times
            PETH2_onset = inhibition_trials_80.goCue_times
            PETH3_onset = nonstim_trials_20.goCue_times
            PETH4_onset = inhibition_trials_20.goCue_times
            PETH5_onset = nonstim_trials.goCue_times
            PETH6_onset = inhibition_trials.goCue_times

        ###plot 80 block trials nonstim
        ax1, plot_edge2, nonstim_80_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH1_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'blue', 'lw': 2},
                                    errbar_kwargs={'color': 'blue', 'alpha': 0.5},
                                    eventline_kwargs={'color': 'black', 'alpha': 0},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)
        ###plot 80 block trials STIM
        ax1, plot_edge3, stim_80_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH2_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'blue', 'lw': 1,'linestyle': 'dashed'},
                                    errbar_kwargs={'color': 'blue', 'alpha': 0.5},
                                    eventline_kwargs={'color': 'black', 'alpha': 0},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)
        ###plot 20 block trials nonstim
        ax1, plot_edge1, nonstim_20_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH3_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'red', 'lw': 2},
                                    errbar_kwargs={'color': 'red', 'alpha': 0.5},
                                    eventline_kwargs={'color': 'black', 'alpha': 0},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)
        ###plot 20 block trials STIM
        ax1, plot_edge, stim_20_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH4_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'red', 'lw': 1,'linestyle': 'dashed'},
                                    errbar_kwargs={'color': 'red', 'alpha': 0.5},
                                    eventline_kwargs={'color': 'black', 'alpha': 0.6},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)
        ###plot all nonstim trials
        ax1, plot_edge, nonstim_all_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH5_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'black', 'lw': 2},
                                    errbar_kwargs={'color': 'black', 'alpha': 0.5},
                                    eventline_kwargs={'color': 'black', 'alpha': 0.6},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)
        ###plot all stim trials
        ax1, plot_edge, stim_all_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
                                    allspikes.clusters,  # Then cluster ids
                                    PETH6_onset,
                                    [j],  # Identity of the cluster we plot
                                    t_before=t_before, t_after=t_after,  # Time before and after the event
                                    error_bars='sem',  # Whether we want Stdev, SEM, or no error
                                    smoothing=smoothing,
                                    bin_size=bin_size,
                                    include_raster=False,  # adds a raster to the bottom
                                    n_rasters=55,  # How many raster traces to include
                                    ax=ax1,  # Make sure we plot to the axis we created
                                    yticks=False,
                                    pethline_kwargs={'color': 'green', 'lw': 0.5},
                                    errbar_kwargs={'color': 'black', 'alpha': 0.2},
                                    eventline_kwargs={'color': 'black', 'alpha': 0.6},
                                    raster_kwargs={'color': 'black', 'lw': 0.5},
                                    normalize_to_baseline = normalize_to_baseline)

        nonstim_80_means = nonstim_80_peth.means[0]
        nonstim_20_means = nonstim_20_peth.means[0]
        stim_80_means = stim_80_peth.means[0]
        stim_20_means = stim_20_peth.means[0]
        nonstim_80_means_err = nonstim_80_peth.stds[0]
        nonstim_20_means_err = nonstim_20_peth.stds[0]
        stim_80_means_err = stim_80_peth.stds[0]
        stim_20_means_err = stim_20_peth.stds[0]
        nonstim_all_means = nonstim_all_peth.means[0]
        stim_all_means = stim_all_peth.means[0]

        # for k in range(np.size(delta_FR_8020_nonstim)):
        #     if stim_80_means[k] - stim_20_means[k] > 0 and delta_FR_8020_nonstim[k] > 0:
        #         delta_FR_8020_stim[k] = stim_80_means[k] - stim_20_means[k]
        #     elif stim_80_means[k] - stim_20_means[k] > 0 and delta_FR_8020_nonstim[k] < 0:
        #         delta_FR_8020_stim[k] = (stim_80_means[k] - stim_20_means[k]) * -1
        #     elif stim_80_means[k] - stim_20_means[k] < 0 and delta_FR_8020_nonstim[k] < 0:
        #         delta_FR_8020_stim[k] = (stim_80_means[k] - stim_20_means[k]) * -1
        #     elif stim_80_means[k] - stim_20_means[k] < 0 and delta_FR_8020_nonstim[k] > 0:
        #         delta_FR_8020_stim[k] = (stim_80_means[k] - stim_20_means[k])
        #     else:
        #         print('theres some problem with your delta FR measurement, skipping...')
        #         plt.close('all')
        #         continue

        ###calculate indices for quiescent period
        if onset_alignment == 'Go cue onset':
            first_index_for_mean = int((t_before/bin_size) - 0.4/bin_size)
            last_index_for_mean = int((t_before/bin_size))
        elif onset_alignment == 'Laser onset':
            first_index_for_mean = int((t_before/bin_size) + 0.2/bin_size)
            last_index_for_mean = int((t_before/bin_size) + 0.8/bin_size)

        QP_firing_rate = (np.nanmean(nonstim_80_means[first_index_for_mean:last_index_for_mean]) + np.nanmean(nonstim_20_means[first_index_for_mean:last_index_for_mean])) / 2

        ### calculate difference in firing rate curves
        # delta_FR_8020_nonstim = nonstim_80_means - nonstim_20_means
        # ### way to ensure delta_FR_8020_stim reflects sign of change relative to nonstim
        # delta_FR_8020_stim = (stim_80_means - stim_20_means) * np.sign(delta_FR_8020_nonstim)
        # ### delta_FR_8020_nonstim should always be positive
        # delta_FR_8020_nonstim = abs(delta_FR_8020_nonstim)

        ############CONTROL: add curves instead of subtracting
        delta_FR_8020_nonstim = nonstim_80_means - nonstim_20_means
        delta_FR_8020_stim = stim_80_means - stim_20_means

        ### calculate z-score
        delta_FR_8020_nonstim_err_est = np.sqrt((nonstim_80_means_err**2 / len(nonstim_trials_80.intervals[:,0])) + (nonstim_20_means_err**2 / len(nonstim_trials_20.intervals[:,0])))
        delta_FR_8020_stim_err_est = np.sqrt((stim_80_means_err**2 / len(inhibition_trials_80.intervals[:,0])) + (stim_20_means_err**2 / len(inhibition_trials_20.intervals[:,0])))

        z_score = (delta_FR_8020_stim - delta_FR_8020_nonstim) / np.sqrt(delta_FR_8020_nonstim_err_est**2 + delta_FR_8020_stim_err_est**2)

        if np.logical_or(np.isnan(z_score), np.isinf(z_score)).any():
            print('Z-score contains INF or NaN values, skipping...')
            plt.close('all')
            continue
        elif np.logical_or(z_score > 5, z_score < -5).any():
            print('Z-score out of reasonable bounds, skipping...')
            plt.close('all')
            continue

        ### normalization for plotting
        ### replace any values that are 0 to prevent infinite values
        nonstim_all_means[nonstim_all_means==0] = 0.1
        stim_all_means[stim_all_means==0] = 0.1
        # delta_FR_8020_nonstim_normalized = delta_FR_8020_nonstim/QP_firing_rate
        delta_FR_8020_nonstim_normalized = delta_FR_8020_nonstim/nonstim_all_means
        # delta_FR_8020_stim_normalized = delta_FR_8020_stim/QP_firing_rate
        delta_FR_8020_stim_normalized = delta_FR_8020_stim/stim_all_means

        mean_delta_FR_8020_nonstim = np.nanmean(delta_FR_8020_nonstim_normalized[first_index_for_mean:last_index_for_mean])
        mean_delta_FR_8020_stim = np.nanmean(delta_FR_8020_stim_normalized[first_index_for_mean:last_index_for_mean])
        if np.isnan(mean_delta_FR_8020_nonstim) or np.isnan(mean_delta_FR_8020_stim) or np.nanmean(delta_FR_8020_nonstim_normalized) > 100:
            ###the last or statement is to remove a few cells with deltaFRs on the order of 10^20? clearly some artifact.
            print('theres some problem with your MEAN delta FR measurement, skipping...')
            plt.close('all')
            continue

        current_unit_spike_indices = np.where(allspikes.clusters == j)
        current_unit_spike_indices = current_unit_spike_indices[0]
        current_unit_spike_times = allspikes.times[current_unit_spike_indices]
    
        #### perform BS analysis using previously created pseudo sessions
        # BS_score, pval_real, pct50_pseudo = isbiasblockselective_02(current_unit_spike_times, trials, pseudo_20_index_filtered, pseudo_80_index_filtered)
        #updated BS function is not working correctly; pvalues obviously fucked up.  not sure what is issue...

        BS_score, pval_real, pct95_pseudo, fr_80_trials_nonstim, fr_20_trials_nonstim, fr_80_trials_inhibition, fr_20_trials_inhibition = isbiasblockselective_03(current_unit_spike_times, trials.probabilityLeft, trials.goCue_times, excitation_trials_numbers,inhibition_trials_numbers,nonstim_trials_numbers,
                        pseudo_20_index_filtered, pseudo_80_index_filtered)

        # if exclude_drifty_units == 1:
        #     if pct50_pseudo < 0.05:
        #         print('Drifty unit, skipping...')
        #         plt.close('all')
        #         continue
            
        # delta_fr_nonstim = np.nanmean(fr_80_trials_nonstim) - np.nanmean(fr_20_trials_nonstim)
        # delta_fr_inhibition = np.nanmean(fr_80_trials_inhibition) - np.nanmean(fr_20_trials_inhibition)
        
        if max(wf_avg_chn_max) + min(wf_avg_chn_max) > 0:
            axonal_unit_score = 1
        else:
            axonal_unit_score = 0

        print('Axonal unit score = ' + str(axonal_unit_score))

        print('BS score = ' + str(BS_score) + ', P value real = ' + str(pval_real) + ', 95% pseudo pval = ' + str(pct95_pseudo))
        print('Mean FR change nonstim = ' + str(mean_delta_FR_8020_nonstim) + ', QP FR = ' + str(QP_firing_rate))
        print('Mean FR change stim = ' + str(mean_delta_FR_8020_stim))

        # if analyze_latency == 1:

        #     latencies = np.empty(len(trials.intervals[excitation_trials_numbers][:,0]))
        #     latencies[:] = np.NaN
        #     for k in np.arange(0,np.size(trials.intervals[excitation_trials_numbers][:,0])):
        #         if current_cluster_spike_times[np.where(current_cluster_spike_times > trials.intervals[excitation_trials_numbers][:,0][k])].size == 0:
        #             continue
        #         latencies[k] = current_cluster_spike_times[np.where(current_cluster_spike_times > trials.intervals[excitation_trials_numbers][:,0][k])][0] - trials.intervals[excitation_trials_numbers][:,0][k]

        #     print('median EX latency = ' + str(np.nanmedian(latencies)))
        #     print('mean EX latency = ' + str(np.nanmean(latencies)))
        #     percent_below_2ms = np.size(np.where(latencies < 0.002))/np.size(latencies[~np.isnan(latencies)]) * 100
        #     print('percent EX latency below 2ms = ' + str(percent_below_2ms))
        #     # print('latency confidence 90 = ' + str(np.nanpercentile(latencies,10)))
        #     # print('latency confidence 85 = ' + str(np.nanpercentile(latencies,15)))
        #     # print('latency confidence 80 = ' + str(np.nanpercentile(latencies,20)))
        #     latencies_EX = latencies

        #     latencies = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
        #     latencies[:] = np.NaN
        #     for k in np.arange(0,np.size(trials.intervals[inhibition_trials_numbers][:,0])):
        #         if current_cluster_spike_times[np.where(current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k])].size == 0:
        #             continue
        #         latencies[k] = current_cluster_spike_times[np.where(current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k])][0] - trials.intervals[inhibition_trials_numbers][:,0][k]

        #     print('median IN latency = ' + str(np.nanmedian(latencies)))
        #     print('mean IN latency = ' + str(np.nanmean(latencies)))
        #     percent_below_2ms = np.size(np.where(latencies < 0.002))/np.size(latencies[~np.isnan(latencies)]) * 100
        #     print('percent IN latency below 2ms = ' + str(percent_below_2ms))

        #     latencies_IN = latencies

        #     pre_inhibition_FR = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
        #     pre_inhibition_FR[:] = np.NaN
        #     post_inhibition_FR = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
        #     post_inhibition_FR[:] = np.NaN
        #     inhibition_latency_period = latency_threshold
        #     for k in np.arange(0,np.size(trials.intervals[inhibition_trials_numbers][:,0])):
        #         spike_times_in_post_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k], current_cluster_spike_times < trials.intervals[inhibition_trials_numbers][:,0][k] + inhibition_latency_period))[0]]
        #         spike_times_in_pre_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times < trials.intervals[inhibition_trials_numbers][:,0][k], current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k] - inhibition_latency_period))[0]]
        #         post_inhibition_FR[k] = np.size(spike_times_in_post_stim)/inhibition_latency_period
        #         pre_inhibition_FR[k] = np.size(spike_times_in_pre_stim)/inhibition_latency_period

        #     if np.nanmean(pre_inhibition_FR) == 0:
        #         print('no spikes detected in any pre trials, skipping...')
        #         plt.close('all')
        #         continue

        #     x, pval_inverselatency = stats.wilcoxon(post_inhibition_FR,pre_inhibition_FR)
        #     print('pval inverse latency = ' + str(pval_inverselatency))
                
        #     if use_latency_threshold == 1:
        #         if np.nanmedian(latencies_EX) > latency_threshold and np.nanmedian(latencies_IN) > latency_threshold and pval_inverselatency > 0.05:
        #             print('Opto latency below threshold, skipping...')
        #             plt.close('all')
        #             continue

        # if only_analyze_responsive_units == 1:
        #     inhibition_FR_pre_responsive = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
        #     inhibition_FR_pre_responsive[:] = np.NaN
        #     inhibition_FR_post_responsive = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
        #     inhibition_FR_post_responsive[:] = np.NaN
        #     inhibition_latency_period = responsive_window
        #     for k in np.arange(0,np.size(trials.intervals[inhibition_trials_numbers][:,0])):
        #         spike_times_in_post_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k], current_cluster_spike_times < trials.intervals[inhibition_trials_numbers][:,0][k] + inhibition_latency_period))[0]]
        #         spike_times_in_pre_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times < trials.intervals[inhibition_trials_numbers][:,0][k], current_cluster_spike_times > trials.intervals[inhibition_trials_numbers][:,0][k] - inhibition_latency_period))[0]]
        #         inhibition_FR_post_responsive[k] = np.size(spike_times_in_post_stim)/inhibition_latency_period
        #         inhibition_FR_pre_responsive[k] = np.size(spike_times_in_pre_stim)/inhibition_latency_period

        #     if np.nanmean(inhibition_FR_post_responsive) == 0 and np.nanmean(inhibition_FR_pre_responsive) == 0:
        #         print('No firing in pre or post responsive window, skipping...')
        #         plt.close('all')
        #         continue
        #     x, pval_responsive_inhibition = stats.wilcoxon(inhibition_FR_post_responsive,inhibition_FR_pre_responsive)
        #     print('pval inhibition response = ' + str(pval_responsive_inhibition))

        #     excitation_FR_pre_responsive = np.empty(len(trials.intervals[excitation_trials_numbers][:,0]))
        #     excitation_FR_pre_responsive[:] = np.NaN
        #     excitation_FR_post_responsive = np.empty(len(trials.intervals[excitation_trials_numbers][:,0]))
        #     excitation_FR_post_responsive[:] = np.NaN
        #     excitation_latency_period = responsive_window
        #     for k in np.arange(0,np.size(trials.intervals[excitation_trials_numbers][:,0])):
        #         spike_times_in_post_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times > trials.intervals[excitation_trials_numbers][:,0][k], current_cluster_spike_times < trials.intervals[excitation_trials_numbers][:,0][k] + excitation_latency_period))[0]]
        #         spike_times_in_pre_stim = current_cluster_spike_times[np.where(np.logical_and(current_cluster_spike_times < trials.intervals[excitation_trials_numbers][:,0][k], current_cluster_spike_times > trials.intervals[excitation_trials_numbers][:,0][k] - excitation_latency_period))[0]]
        #         excitation_FR_post_responsive[k] = np.size(spike_times_in_post_stim)/excitation_latency_period
        #         excitation_FR_pre_responsive[k] = np.size(spike_times_in_pre_stim)/excitation_latency_period

        #     if np.nanmean(excitation_FR_post_responsive) == 0 and np.nanmean(excitation_FR_post_responsive) == 0:
        #         print('No firing in pre or post responsive window, skipping...')
        #         plt.close('all')
        #         continue
        #     x, pval_responsive_excitation = stats.wilcoxon(excitation_FR_post_responsive,excitation_FR_pre_responsive)
        #     print('pval excitation response = ' + str(pval_responsive_excitation))

        #     if pval_responsive_excitation > 0.01 and pval_responsive_inhibition > 0.01:
        #         print('Non-responsive unit! (not skipping yet)')
                
        current_unit_allen_label = brain_acronyms_percluster[j]
        current_unit_beryl_label = br.acronym2acronym(current_unit_allen_label, mapping='Beryl')


        ### All data gets appended here
        delta_fr_nonstim_all.append(delta_FR_8020_nonstim_normalized)
        delta_fr_inhibition_all.append(delta_FR_8020_stim_normalized)
        zscore_all.append(z_score)

        clusters_info_DF = pd.concat([clusters_info_DF,pd.DataFrame(
            index=[clusters_info_DF.shape[0] + 1], data={
                                'Allenregion': current_unit_allen_label,
                                'Berylregion': current_unit_beryl_label,
                                'pid': pid,
                                'clustnum': j,
                                'IBL_label':clusters_labels[j],
                                # 'KS2_label':clusters_ks2labels[j],
                                'ax_unit': axonal_unit_score,
                                'pval': pval_real,
                                'pct95_ps': pct95_pseudo,
                                'BS_score': BS_score,
                                'Delta_nonstim': mean_delta_FR_8020_nonstim,
                                'Delta_stim': mean_delta_FR_8020_stim})])

        # if excitation_traces_percluster == []:
        #     if zscore_normalize == 0:
        #         nonstim80_traces_percluster = nonstim_80_means
        #         nonstim20_traces_percluster = nonstim_20_means
        #         stim80_traces_percluster = stim_80_means
        #         stim20_traces_percluster = stim_20_means
        #     # else:
        #         # excitation_traces_percluster = excitation_means_z
        #         # inhibition_traces_percluster = inhibition_means_z
        # else:
        #     if zscore_normalize == 0:
        #         nonstim80_traces_percluster = np.vstack([nonstim80_traces_percluster, nonstim_80_means])
        #         nonstim20_traces_percluster = np.vstack([nonstim20_traces_percluster, nonstim_20_means])
        #         stim80_traces_percluster = np.vstack([stim80_traces_percluster, stim_80_means])
        #         stim20_traces_percluster = np.vstack([stim20_traces_percluster, stim_20_means])
        #     # else:
        #     #     excitation_traces_percluster = np.vstack([excitation_traces_percluster, excitation_means_z])
        #     #     inhibition_traces_percluster = np.vstack([inhibition_traces_percluster, inhibition_means_z])

        rand_indices_wav = np.random.choice(wf_idx,15)
        for k in rand_indices_wav:
            rand_wf = spike_wfs['waveforms'][k, :, 0]
            if plot_each_cluster == 1:
                ax3.plot(rand_wf,'r-',linewidth=0.5)

        if plot_each_cluster == 1:
            ax3.plot(wf_avg_chn_max_nonnorm,'k-',linewidth = 3)
            # ax2.plot(delta_FR_8020_nonstim,'k-',linewidth = 3)
            # ax2.plot(delta_FR_8020_stim,'r-',linewidth = 3)
            ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1)
            ax2.plot(z_score,'b-',linewidth = 3)

            if plot_edge1 > plot_edge:
                plot_limit = plot_edge1
            else:
                plot_limit = plot_edge

            if np.isnan(plot_limit) == 1:
                plot_limit = 1

            if np.isinf(plot_limit) == 1:
                plot_limit = 100

            if plot_limit > 100:
                ax1.set_yticks(np.arange(0, 200, step=20))
            if plot_limit < 100 and plot_limit > 20:
                ax1.set_yticks(np.arange(0, 100, step=5))
            if plot_limit < 20:
                ax1.set_yticks(np.arange(0, 20, step=1))
            ax1.set_ylim([0, plot_limit])
            ax1.set_xlabel('Time from laser onset (s)', fontsize = 13)
            ax1.set_ylabel('Firing rate (spikes/s)', fontsize = 13)
            plt.show()
            plt.waitforbuttonpress
            plt.close('all')
        # except:
        #     print('Error with cluster (numspikes = ' + str(np.size(current_cluster_spike_indices)) + '). Skipping cluster...')
        #     continue

################# SAVE

import pickle
clusters_info_DF.to_pickle('~/python/saved_figures/' + condition + '_' + onset_alignment + '_BSdownstream_DF' '.pkl')

delta_fr_data = {'delta_fr_nonstim_all': delta_fr_nonstim_all, 'delta_fr_inhibition_all': delta_fr_inhibition_all, 'zscore_all': zscore_all}
with open(condition + '_' + onset_alignment + '_delta_fr.pickle', 'wb') as f:
    pickle.dump(delta_fr_data, f)

print('Pickle dumped!')

# #################################################################################################
# ########### Post Analysis

################# LOAD
clusters_info_DF = pd.read_pickle('~/python/saved_figures/' + condition + '_' + onset_alignment + '_BSdownstream_DF' '.pkl')

with open(condition + '_' + onset_alignment + '_delta_fr.pickle', 'rb') as f:
    data = pickle.load(f)

delta_fr_nonstim_all = data['delta_fr_nonstim_all']
delta_fr_inhibition_all = data['delta_fr_inhibition_all']
zscore_all = data['zscore_all']
#################

allen_regions_formidbrain = ['SCsg','SCzo','SCop','SCig','SCiw','SCdg','MB','MRN','RN','PPN','PAG','CUN','PRNr']
beryl_regions_forcortex = ['RSPd','RSPagl','VISp']

pd.set_option('display.max_rows', None)
x_values_for_plot = np.arange(-t_before,t_after,0.05) #need to change w/ different bin sizes

###### ALL UNITS
indices_to_use = clusters_info_DF['BS_score'] >= 0
title_str = 'All units'

###### ALL IBL GOOD UNITS
indices_to_use = (clusters_info_DF['IBL_label'] == 1.0)
title_str = 'All units'

###### ALL IBL 'OK' UNITS
indices_to_use = (clusters_info_DF['IBL_label'] > 0.6)
title_str = 'All units'

###### ALL BS UNITS
indices_to_use = clusters_info_DF['BS_score'] == 1
title_str = 'All BS units'

###### ALL MIDBRAIN UNITS
indices_to_use = clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)
title_str = 'All midbrain units'

###### ALL MRN UNITS
indices_to_use = clusters_info_DF['Allenregion'].isin(['MRN'])
title_str = 'All MRN units'

###### ALL SC UNITS
indices_to_use = clusters_info_DF['Allenregion'].isin(['SCsg','SCzo','SCop','SCig','SCiw','SCdg'])
title_str = 'All SC units'

###### ALL IBL 'OK' SC UNITS
indices_to_use = (clusters_info_DF['Allenregion'].isin(['SCsg','SCzo','SCop','SCig','SCiw','SCdg'])) & (clusters_info_DF['IBL_label'] > 0.6)
title_str = 'All SC units'

###### ALL BS SC UNITS
indices_to_use = (clusters_info_DF['Allenregion'].isin(['SCsg','SCzo','SCop','SCig','SCiw','SCdg'])) & (clusters_info_DF['BS_score'] == 1)
title_str = 'All SC units'

###### ALL BS MIDBRAIN UNITS
indices_to_use = clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain) & clusters_info_DF['BS_score'] == 1
title_str = 'All Bias-selective midbrain units'

###### ALL IBL 'OK' MIDBRAIN UNITS
indices_to_use = (clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)) & (clusters_info_DF['IBL_label'] > 0.6)
title_str = 'All Good midbrain units'

###### ALL IBL GOOD BS MIDBRAIN UNITS
indices_to_use = (clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)) & (clusters_info_DF['BS_score'] == 1) & (clusters_info_DF['IBL_label'] == 1.0)
title_str = 'All Good bias-selective midbrain units'

###### ALL IBL 'OK' BS MIDBRAIN UNITS
indices_to_use = (clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)) & (clusters_info_DF['BS_score'] == 1) & (clusters_info_DF['IBL_label'] > 0.6)
title_str = 'All Good bias-selective midbrain units'

###### ALL CORTEX UNITS
indices_to_use = clusters_info_DF['Berylregion'].isin(beryl_regions_forcortex)
title_str = 'All cortex units'

###### ALL AXONAL UNITS
indices_to_use = clusters_info_DF['ax_unit'] == 1
title_str = 'All axonal units'

###### NO AXONAL UNITS
indices_to_use = clusters_info_DF['ax_unit'] == 0
title_str = 'No axonal units'

###### ALL IPSI UNITS
indices_to_use = clusters_info_DF['pid'].isin(pids_list_ZI_trained) | clusters_info_DF['pid'].isin(pids_list_SNr_trained)
title_str = 'All ipsi units'

###### ALL CONTRA UNITS
indices_to_use = clusters_info_DF['pid'].isin(pids_list_ZI_trained_contra) | clusters_info_DF['pid'].isin(pids_list_SNr_contra_trained)
title_str = 'All contra units'


#################################################################################################
indices_to_use_plt = indices_to_use.values.astype(bool)
indices_to_use_plt = np.where(indices_to_use == True)[0]

selected_arrays_nonstim = [delta_fr_nonstim_all[i] for i in indices_to_use_plt]
selected_arrays_stim = [delta_fr_inhibition_all[i] for i in indices_to_use_plt]
mean_delta_trace_nonstim = np.nanmean(selected_arrays_nonstim, axis=0) * 100
mean_delta_trace_stim = np.nanmean(selected_arrays_stim, axis=0) * 100
stderr_mean_delta_trace_nonstim = np.std(selected_arrays_nonstim,axis=0)/np.sqrt(len(selected_arrays_nonstim)) * 100
stderr_mean_delta_trace_stim = np.std(selected_arrays_stim,axis=0)/np.sqrt(len(selected_arrays_stim)) * 100

plt.plot(x_values_for_plot,mean_delta_trace_nonstim,color='k',linewidth=3,label='Delta FR (%) control')
plt.plot(x_values_for_plot,mean_delta_trace_stim,color='b',linewidth=3,label='Delta FR (%) Laser')
plt.fill_between(x_values_for_plot, mean_delta_trace_nonstim-stderr_mean_delta_trace_nonstim, mean_delta_trace_nonstim+stderr_mean_delta_trace_nonstim, color='k', alpha=0.2)
plt.fill_between(x_values_for_plot, mean_delta_trace_stim-stderr_mean_delta_trace_stim, mean_delta_trace_stim+stderr_mean_delta_trace_stim, color='b', alpha=0.2)
plt.axvline(x=0, linestyle='--', color='red', label=onset_alignment)
plt.xlabel('Time from' + onset_alignment + ' (s)')
plt.ylabel('Delta FR 80/20 blocks (% baseline)')
plt.xlim(-10,20)
# plt.ylim(-20,100)
plt.title(title_str + ', n = ' + str(len(selected_arrays_nonstim)))
plt.legend()
plt.show()

selected_arrays = [zscore_all[i] for i in indices_to_use_plt]
mean_zscore = np.nanmean(selected_arrays, axis=0)
stderr_mean_zscore = np.std(selected_arrays,axis=0)/np.sqrt(len(selected_arrays))

plt.plot(x_values_for_plot,mean_zscore,color='b',linewidth=4,label='Z-scored delta FR (stim)')
plt.fill_between(x_values_for_plot, mean_zscore-stderr_mean_zscore, mean_zscore+stderr_mean_zscore, color='k', alpha=0.2)
plt.axvline(x=0, linestyle='--', color='red', label=onset_alignment)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1)
plt.xlabel('Time from' + onset_alignment + ' (s)')
plt.ylabel('Delta FR 80/20 blocks (% baseline)')
plt.xlim(-10,20)
# plt.ylim(-1,0.5)
plt.title(title_str + ', n = ' + str(len(selected_arrays_nonstim)))
plt.legend()
plt.show()

######################################

meandelta_nonstim = clusters_info_DF.loc[indices_to_use, 'Delta_nonstim']
meandelta_stim = clusters_info_DF.loc[indices_to_use, 'Delta_stim']
stderr_meandelta_nonstim = np.std(meandelta_nonstim,axis=0)/np.sqrt(np.size(meandelta_nonstim))
stderr_meandelta_stim = np.std(meandelta_stim,axis=0)/np.sqrt(np.size(meandelta_stim))

plt.bar(1,np.nanmean(meandelta_nonstim),color='black',yerr=stderr_meandelta_nonstim,ecolor='red')
plt.bar(2,np.nanmean(meandelta_stim),color='blue',yerr=stderr_meandelta_stim,ecolor='red')

plt.show()

t_stat, p_val = stats.ttest_rel(meandelta_nonstim, meandelta_stim)




# ###### ALL UNITS
# mean_delta_trace_nonstim = np.nanmean(delta_fr_nonstim_all, axis=0) * 100
# mean_delta_trace_stim = np.nanmean(delta_fr_inhibition_all, axis=0) * 100

# stderr_mean_delta_trace_nonstim = np.std(delta_fr_nonstim_all,axis=0)/np.sqrt(len(delta_fr_nonstim_all)) * 100
# stderr_mean_delta_trace_stim = np.std(delta_fr_inhibition_all,axis=0)/np.sqrt(len(delta_fr_inhibition_all)) * 100

# plt.plot(x_values_for_plot,mean_delta_trace_nonstim,color='k',linewidth=3,label='Delta FR (%) control')
# plt.plot(x_values_for_plot,mean_delta_trace_stim,color='b',linewidth=3,label='Delta FR (%) Laser')
# plt.fill_between(x_values_for_plot, mean_delta_trace_nonstim-stderr_mean_delta_trace_nonstim, mean_delta_trace_nonstim+stderr_mean_delta_trace_nonstim, color='k', alpha=0.2)
# plt.fill_between(x_values_for_plot, mean_delta_trace_stim-stderr_mean_delta_trace_stim, mean_delta_trace_stim+stderr_mean_delta_trace_stim, color='b', alpha=0.2)
# plt.axvline(x=0, linestyle='--', color='red', label='Go cue onset')
# plt.xlabel('Time from go cue (s)')
# plt.ylabel('Delta FR 80/20 blocks (% baseline)')
# plt.title('All Units, n = ' + str(len(delta_fr_nonstim_all)))
# # plt.xlim(-0.6,1)
# # plt.ylim(-100,300)
# plt.legend()
# plt.show()

# meandelta_allregions_allunits_nonstim = clusters_info_DF.Delta_nonstim
# meandelta_allregions_allunits_stim = clusters_info_DF.Delta_stim

# stderr_meandelta_allregions_allunits_nonstim = np.std(meandelta_allregions_allunits_nonstim,axis=0)/np.sqrt(np.size(meandelta_allregions_allunits_nonstim))
# stderr_meandelta_allregions_allunits_stim = np.std(meandelta_allregions_allunits_stim,axis=0)/np.sqrt(np.size(meandelta_allregions_allunits_stim))

# plt.bar(1,np.nanmean(meandelta_allregions_allunits_nonstim),color='black',yerr=stderr_meandelta_allregions_allunits_nonstim,ecolor='red')
# plt.bar(2,np.nanmean(meandelta_allregions_allunits_stim),color='blue',yerr=stderr_meandelta_allregions_allunits_stim,ecolor='red')

# plt.show()

# t_stat, p_val = stats.ttest_rel(meandelta_allregions_allunits_nonstim, meandelta_allregions_allunits_stim)


# meandelta_allregions_BSunits_nonstim = clusters_info_DF.loc[clusters_info_DF['pval'] < 0.0001, 'Delta_nonstim']
# meandelta_allregions_BSunits_stim = clusters_info_DF.loc[clusters_info_DF['pval'] < 0.0001, 'Delta_stim']
# stderr_meandelta_allregions_BSunits_nonstim = np.std(meandelta_allregions_BSunits_nonstim,axis=0)/np.sqrt(np.size(meandelta_allregions_BSunits_nonstim))
# stderr_meandelta_allregions_BSunits_stim = np.std(meandelta_allregions_BSunits_stim,axis=0)/np.sqrt(np.size(meandelta_allregions_BSunits_stim))

# plt.bar(1,np.nanmean(meandelta_allregions_BSunits_nonstim),color='black',yerr=stderr_meandelta_allregions_BSunits_nonstim,ecolor='red')
# plt.bar(2,np.nanmean(meandelta_allregions_BSunits_stim),color='blue',yerr=stderr_meandelta_allregions_BSunits_stim,ecolor='red')

# plt.show()

# t_stat, p_val = stats.ttest_rel(meandelta_allregions_BSunits_nonstim, meandelta_allregions_BSunits_stim)

############ Midbrain, all units

# indices_to_use = clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)
# indices_to_use = indices_to_use.values.astype(bool)
# indices_to_use = np.where(indices_to_use == True)[0]

# selected_arrays_nonstim = [delta_fr_nonstim_all[i] for i in indices_to_use]
# selected_arrays_stim = [delta_fr_inhibition_all[i] for i in indices_to_use]

# mean_delta_trace_nonstim = np.nanmean(selected_arrays_nonstim, axis=0) * 100
# mean_delta_trace_stim = np.nanmean(selected_arrays_stim, axis=0) * 100
# stderr_mean_delta_trace_nonstim = np.std(selected_arrays_nonstim,axis=0)/np.sqrt(len(selected_arrays_nonstim)) * 100
# stderr_mean_delta_trace_stim = np.std(selected_arrays_stim,axis=0)/np.sqrt(len(selected_arrays_stim)) * 100

# plt.plot(x_values_for_plot,mean_delta_trace_nonstim,color='k',linewidth=3,label='Delta FR (%) control')
# plt.plot(x_values_for_plot,mean_delta_trace_stim,color='b',linewidth=3,label='Delta FR (%) Laser')
# plt.fill_between(x_values_for_plot, mean_delta_trace_nonstim-stderr_mean_delta_trace_nonstim, mean_delta_trace_nonstim+stderr_mean_delta_trace_nonstim, color='k', alpha=0.2)
# plt.fill_between(x_values_for_plot, mean_delta_trace_stim-stderr_mean_delta_trace_stim, mean_delta_trace_stim+stderr_mean_delta_trace_stim, color='b', alpha=0.2)
# plt.axvline(x=0, linestyle='--', color='red', label='Go cue onset')
# plt.xlabel('Time from go cue (s)')
# plt.ylabel('Delta FR 80/20 blocks (% baseline)')
# plt.xlim(-0.6,0.5)
# plt.ylim(-50,200)
# plt.title('Midbrain Units, n = ' + str(len(selected_arrays_nonstim)))
# plt.legend()
# plt.show()

# meandelta_allregions_MBunits_nonstim = clusters_info_DF.loc[clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain), 'Delta_nonstim']
# meandelta_allregions_MBunits_stim = clusters_info_DF.loc[clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain), 'Delta_stim']
# stderr_meandelta_allregions_MBunits_nonstim = np.std(meandelta_allregions_MBunits_nonstim,axis=0)/np.sqrt(np.size(meandelta_allregions_MBunits_nonstim))
# stderr_meandelta_allregions_MBunits_stim = np.std(meandelta_allregions_MBunits_stim,axis=0)/np.sqrt(np.size(meandelta_allregions_MBunits_stim))

# plt.bar(1,np.nanmean(meandelta_allregions_MBunits_nonstim),color='black',yerr=stderr_meandelta_allregions_MBunits_nonstim,ecolor='red')
# plt.bar(2,np.nanmean(meandelta_allregions_MBunits_stim),color='blue',yerr=stderr_meandelta_allregions_MBunits_stim,ecolor='red')

# plt.show()

# t_stat, p_val = stats.ttest_rel(meandelta_allregions_MBunits_nonstim, meandelta_allregions_MBunits_stim)


# ############ Midbrain, BS units

# indices_to_use = clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain) & clusters_info_DF['BS_score'] == 1
# indices_to_use = indices_to_use.values.astype(bool)
# indices_to_use = np.where(indices_to_use == True)[0]

# selected_arrays_nonstim = [delta_fr_nonstim_all[i] for i in indices_to_use]
# selected_arrays_stim = [delta_fr_inhibition_all[i] for i in indices_to_use]

# mean_delta_trace_nonstim = np.nanmean(selected_arrays_nonstim, axis=0) * 100
# mean_delta_trace_stim = np.nanmean(selected_arrays_stim, axis=0) * 100
# stderr_mean_delta_trace_nonstim = np.std(selected_arrays_nonstim,axis=0)/np.sqrt(len(selected_arrays_nonstim)) * 100
# stderr_mean_delta_trace_stim = np.std(selected_arrays_stim,axis=0)/np.sqrt(len(selected_arrays_stim)) * 100

# plt.plot(x_values_for_plot,mean_delta_trace_nonstim,color='k',linewidth=3,label='Delta FR (%) control')
# plt.plot(x_values_for_plot,mean_delta_trace_stim,color='b',linewidth=3,label='Delta FR (%) Laser')
# plt.fill_between(x_values_for_plot, mean_delta_trace_nonstim-stderr_mean_delta_trace_nonstim, mean_delta_trace_nonstim+stderr_mean_delta_trace_nonstim, color='k', alpha=0.2)
# plt.fill_between(x_values_for_plot, mean_delta_trace_stim-stderr_mean_delta_trace_stim, mean_delta_trace_stim+stderr_mean_delta_trace_stim, color='b', alpha=0.2)
# plt.axvline(x=0, linestyle='--', color='red', label='Go cue onset')
# plt.xlabel('Time from go cue (s)')
# plt.ylabel('Delta FR 80/20 blocks (% baseline)')
# plt.title('Midbrain Bias-selective Units, n = ' + str(len(selected_arrays_nonstim)))
# plt.xlim(-0.6,0.5)
# plt.ylim(-100,300)
# plt.legend()
# plt.show()

# meandelta_allregions_MBunits_nonstim = clusters_info_DF.loc[(clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)) & (clusters_info_DF['BS_score'] == 1), 'Delta_nonstim']
# meandelta_allregions_MBunits_stim = clusters_info_DF.loc[(clusters_info_DF['Allenregion'].isin(allen_regions_formidbrain)) & (clusters_info_DF['BS_score'] == 1), 'Delta_stim']
# stderr_meandelta_allregions_MBunits_nonstim = np.std(meandelta_allregions_MBunits_nonstim,axis=0)/np.sqrt(np.size(meandelta_allregions_MBunits_nonstim))
# stderr_meandelta_allregions_MBunits_stim = np.std(meandelta_allregions_MBunits_stim,axis=0)/np.sqrt(np.size(meandelta_allregions_MBunits_stim))

# plt.bar(1,np.nanmean(meandelta_allregions_MBunits_nonstim),color='black',yerr=stderr_meandelta_allregions_MBunits_nonstim,ecolor='red')
# plt.bar(2,np.nanmean(meandelta_allregions_MBunits_stim),color='blue',yerr=stderr_meandelta_allregions_MBunits_stim,ecolor='red')

# plt.show()

# t_stat, p_val = stats.ttest_rel(meandelta_allregions_MBunits_nonstim, meandelta_allregions_MBunits_stim)


# ############ Cortex, all units

# indices_to_use = clusters_info_DF['Berylregion'].isin(beryl_regions_forcortex)
# indices_to_use = indices_to_use.values.astype(bool)
# indices_to_use = np.where(indices_to_use == True)[0]

# selected_arrays_nonstim = [delta_fr_nonstim_all[i] for i in indices_to_use]
# selected_arrays_stim = [delta_fr_inhibition_all[i] for i in indices_to_use]

# mean_delta_trace_nonstim = np.nanmean(selected_arrays_nonstim, axis=0) * 100
# mean_delta_trace_stim = np.nanmean(selected_arrays_stim, axis=0) * 100
# stderr_mean_delta_trace_nonstim = np.std(selected_arrays_nonstim,axis=0)/np.sqrt(len(selected_arrays_nonstim)) * 100
# stderr_mean_delta_trace_stim = np.std(selected_arrays_stim,axis=0)/np.sqrt(len(selected_arrays_stim)) * 100

# plt.plot(x_values_for_plot,mean_delta_trace_nonstim,color='k',linewidth=3,label='Delta FR (%) control')
# plt.plot(x_values_for_plot,mean_delta_trace_stim,color='b',linewidth=3,label='Delta FR (%) Laser')
# plt.fill_between(x_values_for_plot, mean_delta_trace_nonstim-stderr_mean_delta_trace_nonstim, mean_delta_trace_nonstim+stderr_mean_delta_trace_nonstim, color='k', alpha=0.2)
# plt.fill_between(x_values_for_plot, mean_delta_trace_stim-stderr_mean_delta_trace_stim, mean_delta_trace_stim+stderr_mean_delta_trace_stim, color='b', alpha=0.2)
# plt.axvline(x=0, linestyle='--', color='red', label='Go cue onset')
# plt.xlabel('Time from go cue (s)')
# plt.ylabel('Delta FR 80/20 blocks (% baseline)')
# plt.title('Cortex Units, n = ' + str(len(selected_arrays_nonstim)))
# plt.xlim(-0.6,0.5)
# plt.ylim(-100,300)
# plt.legend()
# plt.show()

# meandelta_CTXunits_nonstim = clusters_info_DF.loc[clusters_info_DF['Berylregion'].isin(beryl_regions_forcortex), 'Delta_nonstim']
# meandelta_CTXunits_stim = clusters_info_DF.loc[clusters_info_DF['Berylregion'].isin(beryl_regions_forcortex), 'Delta_stim']
# stderr_meandelta_CTXunits_nonstim = np.std(meandelta_CTXunits_nonstim,axis=0)/np.sqrt(np.size(meandelta_CTXunits_nonstim))
# stderr_meandelta_CTXunits_stim = np.std(meandelta_CTXunits_stim,axis=0)/np.sqrt(np.size(meandelta_CTXunits_stim))

# plt.bar(1,np.nanmean(meandelta_CTXunits_nonstim),color='black',yerr=stderr_meandelta_CTXunits_nonstim,ecolor='red')
# plt.bar(2,np.nanmean(meandelta_CTXunits_stim),color='blue',yerr=stderr_meandelta_CTXunits_stim,ecolor='red')

# plt.show()

# t_stat, p_val = stats.ttest_rel(meandelta_CTXunits_nonstim, meandelta_CTXunits_stim)




###### Look aligned to laser onset!


# # # if zscore_normalize == 0:
# # avg_delta_fr_nonstim_all = np.average(delta_fr_nonstim_all,axis=0)
# # avg_delta_fr_inhibition_all = np.average(delta_fr_inhibition_all,axis=0)

# # BS_indices = np.where(np.array(BS_score_per_cluster) == 1)[0]
# # delta_fr_nonstim_all_array = np.array(delta_fr_nonstim_all)
# # delta_fr_inhibition_all_array = np.array(delta_fr_inhibition_all)

# # avg_delta_fr_nonstim_BS = np.average(delta_fr_nonstim_all_array[BS_indices],axis=0)
# # avg_delta_fr_inhibition_BS = np.average(delta_fr_inhibition_all_array[BS_indices],axis=0)

# # acronyms_for_clusters_of_interest = brain_acronyms_percluster[clusters_of_interest]

# avg_excitation_trace_MRN = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MRN')[0]],axis=0)
# avg_inhibition_trace_MRN = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MRN')[0]],axis=0)
# avg_nonstim_trace_MRN = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MRN')[0]],axis=0)
# num_units_MRN = np.size(np.where(acronyms_for_clusters_of_interest == 'MRN')[0])

# avg_excitation_trace_SCdg = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCdg')[0]],axis=0)
# avg_inhibition_trace_SCdg = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCdg')[0]],axis=0)
# avg_nonstim_trace_SCdg = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCdg')[0]],axis=0)
# num_units_SCdg = np.size(np.where(acronyms_for_clusters_of_interest == 'SCdg')[0])

# clustersx = np.array([]).astype(int)
# for m in np.arange(0,np.size(acronyms_for_clusters_of_interest)):
#     if acronyms_for_clusters_of_interest[m].find('SCdg') == 0 or acronyms_for_clusters_of_interest[m].find('SCdw') == 0:
#         clustersx = np.append(clustersx,m)
# clustersx = clustersx.astype(int)
# avg_excitation_trace_SCdeep = np.average(excitation_traces_percluster[clustersx],axis=0)
# avg_inhibition_trace_SCdeep = np.average(inhibition_traces_percluster[clustersx],axis=0)
# avg_nonstim_trace_SCdeep = np.average(nonstim_traces_percluster[clustersx],axis=0)
# num_units_SCdeep = np.size(clustersx)

# avg_excitation_trace_SCiw = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCiw')[0]],axis=0)
# avg_inhibition_trace_SCiw = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCiw')[0]],axis=0)
# avg_nonstim_trace_SCiw = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCiw')[0]],axis=0)
# num_units_SCiw = np.size(np.where(acronyms_for_clusters_of_interest == 'SCiw')[0])

# avg_excitation_trace_SCig = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCig')[0]],axis=0)
# avg_inhibition_trace_SCig = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCig')[0]],axis=0)
# avg_nonstim_trace_SCig = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCig')[0]],axis=0)
# num_units_SCig = np.size(np.where(acronyms_for_clusters_of_interest == 'SCig')[0])

# avg_excitation_trace_SCop = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCop')[0]],axis=0)
# avg_inhibition_trace_SCop = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCop')[0]],axis=0)
# avg_nonstim_trace_SCop = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCop')[0]],axis=0)
# num_units_SCop = np.size(np.where(acronyms_for_clusters_of_interest == 'SCop')[0])

# avg_excitation_trace_SCzo = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCzo')[0]],axis=0)
# avg_inhibition_trace_SCzo = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCzo')[0]],axis=0)
# avg_nonstim_trace_SCzo = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCzo')[0]],axis=0)
# num_units_SCzo = np.size(np.where(acronyms_for_clusters_of_interest == 'SCzo')[0])

# avg_excitation_trace_SCsg = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCsg')[0]],axis=0)
# avg_inhibition_trace_SCsg = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCsg')[0]],axis=0)
# avg_nonstim_trace_SCsg = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SCsg')[0]],axis=0)
# num_units_SCsg = np.size(np.where(acronyms_for_clusters_of_interest == 'SCsg')[0])


# clustersx = np.array([]).astype(int)
# for m in np.arange(0,np.size(acronyms_for_clusters_of_interest)):
#     if acronyms_for_clusters_of_interest[m].find('ZI') == 0 or acronyms_for_clusters_of_interest[m].find('FF') == 0:
#         clustersx = np.append(clustersx,m)
# clustersx = clustersx.astype(int)
# excitation_traces = excitation_traces_percluster[clustersx]
# inhibition_traces = inhibition_traces_percluster[clustersx]
# nonstim_traces = nonstim_traces_percluster[clustersx]
# avg_excitation_trace_ZI = np.mean(excitation_traces,axis=0)
# avg_inhibition_trace_ZI = np.mean(inhibition_traces,axis=0)
# avg_nonstim_trace_ZI = np.average(nonstim_traces,axis=0)
# num_units_ZI = np.size(np.where(acronyms_for_clusters_of_interest == 'ZI')[0])
# # for m in np.arange(0,num_units_ZI):
# #     plt.plot(excitation_traces[m],'b')
# #     plt.plot(inhibition_traces[m],'r')
# #     plt.show()
# #     plt.waitforbuttonpress
# #     plt.close('all')

# std_avg_excitation_trace_ZI = np.std(excitation_traces,axis=0)/np.sqrt(np.size(excitation_traces[:,0]))
# std_avg_inhibition_trace_ZI = np.std(inhibition_traces,axis=0)/np.sqrt(np.size(inhibition_traces[:,0]))
# std_avg_nonstim_trace_ZI = np.std(nonstim_traces,axis=0)/np.sqrt(np.size(nonstim_traces[:,0]))

# excitation_traces = excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SNr')[0]]
# inhibition_traces = inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SNr')[0]]
# nonstim_traces = nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'SNr')[0]]
# avg_excitation_trace_SNr = np.average(excitation_traces,axis=0)
# avg_inhibition_trace_SNr = np.average(inhibition_traces,axis=0)
# avg_nonstim_trace_SNr = np.average(nonstim_traces,axis=0)
# num_units_SNr = np.size(np.where(acronyms_for_clusters_of_interest == 'SNr')[0])
# std_avg_excitation_trace_SNr = np.std(excitation_traces,axis=0)/np.sqrt(np.size(excitation_traces[:,0]))
# std_avg_inhibition_trace_SNr = np.std(inhibition_traces,axis=0)/np.sqrt(np.size(inhibition_traces[:,0]))
# std_avg_nonstim_trace_SNr = np.std(nonstim_traces,axis=0)/np.sqrt(np.size(nonstim_traces[:,0]))

# avg_excitation_trace_APN = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'APN')[0]],axis=0)
# avg_inhibition_trace_APN = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'APN')[0]],axis=0)
# avg_nonstim_trace_APN = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'APN')[0]],axis=0)
# num_units_APN = np.size(np.where(acronyms_for_clusters_of_interest == 'APN')[0])

# clustersx = np.array([]).astype(int)
# for m in np.arange(0,np.size(acronyms_for_clusters_of_interest)):
#     if acronyms_for_clusters_of_interest[m].find('SCsg') == 0 or acronyms_for_clusters_of_interest[m].find('SCzo') == 0 or acronyms_for_clusters_of_interest[m].find('SCop') == 0:
#         clustersx = np.append(clustersx,m)
# clustersx = clustersx.astype(int)
# avg_excitation_trace_SCsup_all = np.average(excitation_traces_percluster[clustersx],axis=0)
# avg_inhibition_trace_SCsup_all = np.average(inhibition_traces_percluster[clustersx],axis=0)
# avg_nonstim_trace_SCsup_all = np.average(nonstim_traces_percluster[clustersx],axis=0)
# num_units_SCsup_all = np.size(clustersx)

# avg_excitation_trace_RSPd23 = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd2/3')[0]],axis=0)
# avg_inhibition_trace_RSPd23 = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd2/3')[0]],axis=0)
# avg_nonstim_trace_RSPd23 = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd2/3')[0]],axis=0)
# num_units_RSPd23 = np.size(np.where(acronyms_for_clusters_of_interest == 'RSPd2/3')[0])

# avg_excitation_trace_RSPd5 = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd5')[0]],axis=0)
# avg_inhibition_trace_RSPd5 = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd5')[0]],axis=0)
# avg_nonstim_trace_RSPd5 = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPd5')[0]],axis=0)
# num_units_RSPd5 = np.size(np.where(acronyms_for_clusters_of_interest == 'RSPd5')[0])

# avg_excitation_trace_RSPagl5 = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPagl5')[0]],axis=0)
# avg_inhibition_trace_RSPagl5 = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPagl5')[0]],axis=0)
# avg_nonstim_trace_RSPagl5 = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RSPagl5')[0]],axis=0)
# num_units_RSPagl5 = np.size(np.where(acronyms_for_clusters_of_interest == 'RSPagl5')[0])

# clustersx = np.array([]).astype(int)
# for m in np.arange(0,np.size(acronyms_for_clusters_of_interest)):
#     if acronyms_for_clusters_of_interest[m].find('RSP') == 0:
#         clustersx = np.append(clustersx,m)
# clustersx = clustersx.astype(int)
# avg_excitation_trace_RSP_all = np.average(excitation_traces_percluster[clustersx],axis=0)
# avg_inhibition_trace_RSP_all = np.average(inhibition_traces_percluster[clustersx],axis=0)
# avg_nonstim_trace_RSP_all = np.average(nonstim_traces_percluster[clustersx],axis=0)
# num_units_RSP_all = np.size(clustersx)

# clustersx = np.array([]).astype(int)
# for m in np.arange(0,np.size(acronyms_for_clusters_of_interest)):
#     if acronyms_for_clusters_of_interest[m].find('VISp') == 0:
#         clustersx = np.append(clustersx,m)
# clustersx = clustersx.astype(int)
# avg_excitation_trace_VISp_all = np.average(excitation_traces_percluster[clustersx],axis=0)
# avg_inhibition_trace_VISp_all = np.average(inhibition_traces_percluster[clustersx],axis=0)
# avg_nonstim_trace_VISp_all = np.average(nonstim_traces_percluster[clustersx],axis=0)
# num_units_VISp_all = np.size(clustersx)

# avg_excitation_trace_PPN = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PPN')[0]],axis=0)
# avg_inhibition_trace_PPN = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PPN')[0]],axis=0)
# avg_nonstim_trace_PPN = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PPN')[0]],axis=0)
# num_units_PPN = np.size(np.where(acronyms_for_clusters_of_interest == 'PPN')[0])

# avg_excitation_trace_PRNr = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PRNr')[0]],axis=0)
# avg_inhibition_trace_PRNr = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PRNr')[0]],axis=0)
# avg_nonstim_trace_PRNr = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PRNr')[0]],axis=0)
# num_units_PRNr = np.size(np.where(acronyms_for_clusters_of_interest == 'PRNr')[0])

# avg_excitation_trace_MB = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MB')[0]],axis=0)
# avg_inhibition_trace_MB = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MB')[0]],axis=0)
# avg_nonstim_trace_MB = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'MB')[0]],axis=0)
# num_units_MB = np.size(np.where(acronyms_for_clusters_of_interest == 'MB')[0])

# avg_excitation_trace_RN = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RN')[0]],axis=0)
# avg_inhibition_trace_RN = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RN')[0]],axis=0)
# avg_nonstim_trace_RN = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'RN')[0]],axis=0)
# num_units_RN = np.size(np.where(acronyms_for_clusters_of_interest == 'RN')[0])

# avg_excitation_trace_PAG = np.average(excitation_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PAG')[0]],axis=0)
# avg_inhibition_trace_PAG = np.average(inhibition_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PAG')[0]],axis=0)
# avg_nonstim_trace_PAG = np.average(nonstim_traces_percluster[np.where(acronyms_for_clusters_of_interest == 'PAG')[0]],axis=0)
# num_units_PAG = np.size(np.where(acronyms_for_clusters_of_interest == 'PAG')[0])

# times  = np.arange(0,t_before + t_after,bin_size)


# fig, axs = plt.subplots(4, 2)
# axs[0,0].plot(times, avg_nonstim_trace_SCsup_all,'k')
# axs[0,0].plot(times, avg_excitation_trace_SCsup_all,'b')
# axs[0,0].plot(times, avg_inhibition_trace_SCsup_all,'r')
# axs[0,0].xaxis.set_ticklabels([])
# axs[0,0].set_title('SC superficial, ' + str(num_units_SCsup_all) + ' units')

# axs[1,0].plot(times, avg_nonstim_trace_SCiw,'k')
# axs[1,0].plot(times, avg_excitation_trace_SCiw,'b')
# axs[1,0].plot(times, avg_inhibition_trace_SCiw,'r')
# axs[1,0].xaxis.set_ticklabels([])
# axs[1,0].set_title('SCiw, ' + str(num_units_SCiw) + ' units')

# axs[2,0].plot(times, avg_nonstim_trace_SCig,'k')
# axs[2,0].plot(times, avg_excitation_trace_SCig,'b')
# axs[2,0].plot(times, avg_inhibition_trace_SCig,'r')
# axs[2,0].xaxis.set_ticklabels([])
# axs[2,0].set_title('SCig, ' + str(num_units_SCig) + ' units')

# axs[3,0].plot(times, avg_nonstim_trace_SCdeep,'k')
# axs[3,0].plot(times, avg_excitation_trace_SCdeep,'b')
# axs[3,0].plot(times, avg_inhibition_trace_SCdeep,'r')
# axs[3,0].set_title('SC deep, ' + str(num_units_SCdeep) + ' units')
# axs[3,0].set(xlabel='time (s)')

# axs[0,1].plot(times, avg_nonstim_trace_MRN,'k')
# axs[0,1].plot(times, avg_excitation_trace_MRN,'b')
# axs[0,1].plot(times, avg_inhibition_trace_MRN,'r')
# axs[0,1].xaxis.set_ticklabels([])
# axs[0,1].set_title('MRN, ' + str(num_units_MRN) + ' units')

# axs[1,1].plot(times, avg_nonstim_trace_MB,'k')
# axs[1,1].plot(times, avg_excitation_trace_MB,'b')
# axs[1,1].plot(times, avg_inhibition_trace_MB,'r')
# axs[1,1].xaxis.set_ticklabels([])
# axs[1,1].set_title('MB, ' + str(num_units_MB) + ' units')

# # axs[2,1].plot(times, avg_nonstim_trace_PPN,'k')
# # axs[2,1].plot(times, avg_excitation_trace_PPN,'b')
# # axs[2,1].plot(times, avg_inhibition_trace_PPN,'r')
# # axs[2,1].xaxis.set_ticklabels([])
# # axs[2,1].set_title('PPN, ' + str(num_units_PPN) + ' units')

# # axs[3,1].plot(times, avg_nonstim_trace_PRNr,'k')
# # axs[3,1].plot(times, avg_excitation_trace_PRNr,'b')
# # axs[3,1].plot(times, avg_inhibition_trace_PRNr,'r')
# # axs[3,1].set_title('PRNr, ' + str(num_units_PRNr) + ' units')

# axs[2,1].plot(times, avg_nonstim_trace_RN,'k')
# axs[2,1].plot(times, avg_excitation_trace_RN,'b')
# axs[2,1].plot(times, avg_inhibition_trace_RN,'r')
# axs[2,1].xaxis.set_ticklabels([])
# axs[2,1].set_title('Red Nuc, ' + str(num_units_RN) + ' units')

# # axs[1,2].plot(times, avg_nonstim_trace_PAG,'k')
# # axs[1,2].plot(times, avg_excitation_trace_PAG,'b')
# # axs[1,2].plot(times, avg_inhibition_trace_PAG,'r')
# # axs[1,2].xaxis.set_ticklabels([])
# # axs[1,2].set_title('PAG, ' + str(num_units_PAG) + ' units')

# # axs[2,1].plot(times, avg_nonstim_trace_VISp_all,'k')
# # axs[2,1].plot(times, avg_excitation_trace_VISp_all,'b')
# # axs[2,1].plot(times, avg_inhibition_trace_VISp_all,'r')
# # axs[2,1].xaxis.set_ticklabels([])
# # axs[2,1].set_title('VISp_all, ' + str(num_units_VISp_all) + ' units')

# axs[3,1].plot(times, avg_nonstim_trace_RSP_all,'k')
# axs[3,1].plot(times, avg_excitation_trace_RSP_all,'b')
# axs[3,1].plot(times, avg_inhibition_trace_RSP_all,'r')
# axs[3,1].set_title('RSP_all, ' + str(num_units_RSP_all) + ' units')
# axs[3,1].set(xlabel='time (s)')

# for ax in axs.flat:
#     ax.set(ylabel='FR')
# # # Hide x labels and tick labels for top plots and y ticks for right plots.
# # for ax in axs.flat:
# #     ax.label_outer()

# plt.show()



# filler_array = np.zeros((8,np.size(all_excitation_trace_SCsup[0,:])))
# import seaborn as sns
# ##### sorting for 0.05 bin size!
# for i in np.arange(0,6):
#     # fig, axs = plt.subplots(1, 1)
#     # fig.set_size_inches(4, 7)
#     if i == 0:
#         traces = all_excitation_trace_SCsup
#         # axs.set_title('SCsup continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCsup = traces[sorted_indices,:]
#     if i == 1:
#         traces = all_excitation_trace_SCint
#         # axs.set_title('SCint continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCint = traces[sorted_indices,:]
#     if i == 2:
#         traces = all_excitation_trace_SCdeep
#         # axs.set_title('SCdeep continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCdeep = traces[sorted_indices,:]
#     if i == 3:
#         traces = all_excitation_trace_MRN
#         # axs.set_title('MRN continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_MRN = traces[sorted_indices,:]
#     if i == 4:
#         traces = all_excitation_trace_allMB
#         fig, axs = plt.subplots(1, 1)
#         fig.set_size_inches(4, 7)
#         axs.set_title('All midbrain 50hz laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces = traces[sorted_indices,:]
#         sns.heatmap(sorted_traces,vmin=-2,vmax=2,ax=axs,cmap='gnuplot2')
#         plt.show()
#         plt.waitforbuttonpress
#         plt.close('all')
# fig, axs = plt.subplots(1, 1)
# fig.set_size_inches(4, 7)
# axs.set_title('All midbrain 50hz laser')
# sorted_traces = np.concatenate((sorted_traces_SCsup,filler_array,sorted_traces_SCint,filler_array,sorted_traces_SCdeep,filler_array,sorted_traces_MRN),axis=0)
# sns.heatmap(sorted_traces,vmin=-2,vmax=2,ax=axs,cmap='gnuplot2')
# plt.show()
# plt.waitforbuttonpress
# plt.close('all')
# ##### sorting for 0.05 bin size!
# for i in np.arange(0,6):
#     # fig, axs = plt.subplots(1, 1)
#     # fig.set_size_inches(4, 7)
#     if i == 0:
#         traces = all_inhibition_trace_SCsup
#         # axs.set_title('SCsup continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCsup = traces[sorted_indices,:]
#     if i == 1:
#         traces = all_inhibition_trace_SCint
#         # axs.set_title('SCint continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCint = traces[sorted_indices,:]
#     if i == 2:
#         traces = all_inhibition_trace_SCdeep
#         # axs.set_title('SCdeep continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_SCdeep = traces[sorted_indices,:]
#     if i == 3:
#         traces = all_inhibition_trace_MRN
#         # axs.set_title('MRN continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces_MRN = traces[sorted_indices,:]
#     if i == 4:
#         traces = all_inhibition_trace_allMB
#         fig, axs = plt.subplots(1, 1)
#         fig.set_size_inches(4, 7)
#         axs.set_title('All midbrain continuous laser')
#         sorted_indices = np.argsort(np.nanmean(traces[:,21:33],axis=1))  ### 600ms for 0.05s bin size
#         sorted_traces = traces[sorted_indices,:]
#         sns.heatmap(sorted_traces,vmin=-2,vmax=2,ax=axs,cmap='gnuplot2')
#         plt.show()
#         plt.waitforbuttonpress
#         plt.close('all')
# fig, axs = plt.subplots(1, 1)
# fig.set_size_inches(4, 7)
# axs.set_title('All midbrain continuous laser')
# sorted_traces = np.concatenate((sorted_traces_SCsup,filler_array,sorted_traces_SCint,filler_array,sorted_traces_SCdeep,filler_array,sorted_traces_MRN),axis=0)
# sns.heatmap(sorted_traces,vmin=-2,vmax=2,ax=axs,cmap='gnuplot2')
# plt.show()
# plt.waitforbuttonpress
# plt.close('all')

# delta_fr_inhibition_all = np.abs(delta_fr_inhibition_all)
# delta_fr_nonstim_all = np.abs(delta_fr_nonstim_all)
# stats.ttest_rel(delta_fr_inhibition_all,delta_fr_nonstim_all)

# mean_all_excitation_trace_allMB = np.nanmean(all_excitation_trace_allMB,axis=0)
# mean_all_inhibition_trace_allMB = np.nanmean(all_inhibition_trace_allMB,axis=0)

# fig, axs = plt.subplots(1, 1)
# axs.plot(times, mean_all_excitation_trace_allMB,'b')
# axs.plot(times, mean_all_inhibition_trace_allMB,'r')
# axs.fill_between(times, mean_all_inhibition_trace_allMB - stderr_all_inhibition_trace_allMB, mean_all_inhibition_trace_allMB + stderr_all_inhibition_trace_allMB, color = 'red', alpha = 0.3)
# axs.fill_between(times, mean_all_excitation_trace_allMB - stderr_all_excitation_trace_allMB, mean_all_excitation_trace_allMB + stderr_all_excitation_trace_allMB, color = 'blue', alpha = 0.3)
# axs.set_title('All midbrain, ' + str(num_units_allMB) + ' units')
# fig.set_size_inches(5, 4)
# axs.set_ylim(bottom=-0.3, top=0.3)
# axs.set(xlabel='time (s)')

# plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_MRN,'k')
# # plt.plot(avg_excitation_trace_MRN,'b')
# # plt.plot(avg_inhibition_trace_MRN,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_MRN[0:15]) + 3,str(num_units_MRN))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCdg,'k')
# # plt.plot(avg_excitation_trace_SCdg,'b')
# # plt.plot(avg_inhibition_trace_SCdg,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCdg[0:15]) + 3,str(num_units_SCdg))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCiw,'k')
# # plt.plot(avg_excitation_trace_SCiw,'b')
# # plt.plot(avg_inhibition_trace_SCiw,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCiw[0:15]) + 3,str(num_units_SCiw))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCig,'k')
# # plt.plot(avg_excitation_trace_SCig,'b')
# # plt.plot(avg_inhibition_trace_SCig,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCig[0:15]) + 3,str(num_units_SCig))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCop,'k')
# # plt.plot(avg_excitation_trace_SCop,'b')
# # plt.plot(avg_inhibition_trace_SCop,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCop[0:15]) + 3,str(num_units_SCop))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCzo,'k')
# # plt.plot(avg_excitation_trace_SCzo,'b')
# # plt.plot(avg_inhibition_trace_SCzo,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCzo[0:15]) + 3,str(num_units_SCzo))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_SCsg,'k')
# # plt.plot(avg_excitation_trace_SCsg,'b')
# # plt.plot(avg_inhibition_trace_SCsg,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_SCsg[0:15]) + 3,str(num_units_SCsg))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_RSPd23,'k')
# # plt.plot(avg_excitation_trace_RSPd23,'b')
# # plt.plot(avg_inhibition_trace_RSPd23,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_RSPd23[0:15]) + 3,str(num_units_RSPd23))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_RSPd5,'k')
# # plt.plot(avg_excitation_trace_RSPd5,'b')
# # plt.plot(avg_inhibition_trace_RSPd5,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_RSPd5[0:15]) + 3,str(num_units_RSPd5))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_RSPagl5,'k')
# # plt.plot(avg_excitation_trace_RSPagl5,'b')
# # plt.plot(avg_inhibition_trace_RSPagl5,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_RSPagl5[0:15]) + 3,str(num_units_RSPagl5))
# # plt.show()

# # plt.figure()
# # plt.plot(avg_nonstim_trace_PPN,'k')
# # plt.plot(avg_excitation_trace_PPN,'b')
# # plt.plot(avg_inhibition_trace_PPN,'r')
# # plt.text(5,np.nanmean(avg_nonstim_trace_PPN[0:15]) + 3,str(num_units_PPN))
# # plt.show()


# # # ##### for average PETH of whatever clusters
# # # # 'b5f7d49f-183e-4a4e-892c-6a1dac7750ce' #SWC_NM_010 4/3/22 penetration 1
# # # # non-SC (MRN): [0,2,3,4,6,7,8,9,10,12,13,14,16,17,range(19,41),range(42,48),49,50,52]
# # # dunno [53,54,56,57,78,84,85,88,89,92,94,95,96,97,98,99,100,101,102,106,108,109,112,116,121,122,124,125,129,138]
# # # # SC: [53,54,56,57,78,84,85,88,89,92,94:102,106,108,109,112,116,121,122,124,125,129,138]
# # # # SWC_NM_021 SNr: [20,21,29,32,36,37,43,44,46,50,53,56,57,217]
# # # #1-4, 7, 10, 21, 28, 30, 42, 44
# # # #VM [6, 12, 21, 24, 32, 42, 48, 54, 56, 393, 398, 399]

# # modified_spikes_clusters = allspikes.clusters
# # # clusters_of_interest = [6, 12, 21, 24, 32, 42, 48, 54, 56, 393, 398, 399]
# # a = np.isin(modified_spikes_clusters,clusters_of_interest)
# # modified_spikes_clusters = np.where(np.isin(allspikes.clusters,clusters_of_interest),999,0)

# # t_before = 1
# # t_after = 2

# # fig = plt.figure()
# # ax = plt.gca()
# # ax, plot_edge2 = peri_event_time_histogram(allspikes.times,  # Spike times first
# #                             allspikes.clusters,  # Then cluster ids
# #                             nonstim_trials.intervals[:,0],  # Event markers we want to plot against
# #                             clusters_of_interest,  # Identity of the cluster we plot
# #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #                             include_raster=False,  # adds a raster to the bottom
# #                             n_rasters=55,  # How many raster traces to include
# #                             ax=ax,  # Make sure we plot to the axis we created
# #                             yticks=False,
# #                             pethline_kwargs={'color': 'black', 'lw': 2},
# #                             errbar_kwargs={'color': 'black', 'alpha': 0.5},
# #                             eventline_kwargs={'color': 'black', 'alpha': 0},
# #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #                             normalize_to_baseline = normalize_to_baseline)
# # ax, plot_edge1 = peri_event_time_histogram(allspikes.times,  # Spike times first
# #                             allspikes.clusters,  # Then cluster ids
# #                             excitation_trials.intervals[:,0],  # Event markers we want to plot against
# #                             clusters_of_interest,  # Identity of the cluster we plot
# #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #                             include_raster=False,  # adds a raster to the bottom
# #                             n_rasters=55,  # How many raster traces to include
# #                             ax=ax,  # Make sure we plot to the axis we created
# #                             yticks=False,
# #                             pethline_kwargs={'color': 'blue', 'lw': 2},
# #                             errbar_kwargs={'color': 'blue', 'alpha': 0.5},
# #                             eventline_kwargs={'color': 'black', 'alpha': 0},
# #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #                             normalize_to_baseline = normalize_to_baseline)
# # ax, plot_edge = peri_event_time_histogram(allspikes.times,  # Spike times first
# #                             allspikes.clusters,  # Then cluster ids
# #                             inhibition_trials.intervals[:,0],  # Event markers we want to plot against
# #                             clusters_of_interest,  # Identity of the cluster we plot
# #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #                             include_raster=False,  # adds a raster to the bottom
# #                             n_rasters=55,  # How many raster traces to include
# #                             ax=ax,  # Make sure we plot to the axis we created
# #                             yticks=False,
# #                             pethline_kwargs={'color': 'red', 'lw': 2},
# #                             errbar_kwargs={'color': 'red', 'alpha': 0.5},
# #                             eventline_kwargs={'color': 'black', 'alpha': 0.6},
# #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #                             normalize_to_baseline = normalize_to_baseline)

# # # peths, binned_spikes = singlecell.calculate_peths(allspikes.times, allspikes.clusters, [j], inhibition_trials.intervals[:,0], t_before, t_after, 0.025, 0.025, True)
# # ax.set_ylim([0, max(plot_edge,plot_edge1,plot_edge2)])
# # # plt.figure(num=1, figsize=(1, 0.75))
# # plt.xticks(fontsize = 11)
# # plt.yticks(fontsize = 11)
# # plt.xlabel('Time from laser onset (s)', fontsize = 13)
# # plt.ylabel('Firing rate (spikes/s)', fontsize = 13)
# # plt.show()

# # # spike_times = allspikes.times
# # # spike_clusters = allspikes.clusters
# # # events = nonstim_trials_ex.intervals[:,0]
# # # cluster_id  = [j]
# # # t_before=2 
# # # t_after=5 
# # # bin_size=0.025 
# # # smoothing=0.025 
# # # as_rate=True
# # # include_raster=False 
# # # n_rasters=None 
# # # error_bars='sem' 
# # # ax=None 
# # # yticks=False
# # # normalize_to_baseline = 1
# # # pethline_kwargs={'color': 'blue', 'lw': 2}
# # # errbar_kwargs={'color': 'blue', 'alpha': 0.5}
# # # eventline_kwargs={'color': 'black', 'alpha': 0.5}
# # # raster_kwargs={'color': 'black', 'lw': 0.5}


# # # import atlaselectrophysiology.plot_data as pd
# # from neurodsp import voltage
# # from one.api import ONE
# # from scipy import signal
# # import scipy.signal
# # from brainbox.io.spikeglx import Streamer
# # import numpy as np
# # import matplotlib.pyplot as plt

# # LFP_RESAMPLE_FACTOR = 10

# # # one = ONE()
# # # pid = 'ecd07b7e-6450-4e31-bef1-f195129eb3d3'
# # # eid, _ = one.pid2eid(pid)

# # trial_no = 0

# # for j in np.arange(0,np.size(trials.choice)):

# #     t0 = trials.intervals[j][0]
# #     t1 = t0 + 5

# #     # Download raw LFP data for timepoints between t0 and t1
# #     sr = Streamer(pid=pid, one=one, typ='lf')
# #     tsel = slice(int(t0 * sr.fs), int(t1 * sr.fs))
# #     raw = sr[tsel, :-sr.nsync].T

# #     # Destripe and subsample the lfp data
# #     destripe = voltage.destripe_lfp(raw, fs=sr.fs, neuropixel_version=1)
# #     destripe = scipy.signal.decimate(destripe, LFP_RESAMPLE_FACTOR, axis=1, ftype='fir')
# #     fs_out = sr.fs / LFP_RESAMPLE_FACTOR

# #     # Compute power spectral density
# #     f, psd = scipy.signal.periodogram(raw, fs_out)

# #     # Alternative way 
# #     # WELCH_WIN_LENGTH_SAMPLES = 1024
# #     # f, psd = scipy.signal.welch(raw, fs=fs_out, window='hann', nperseg=WELCH_WIN_LENGTH_SAMPLES,
# #     #                             detrend='constant', return_onesided=True, scaling='density', axis=-1)

# #     # Plot using brainbox plotting function
# #     from brainbox.ephys_plots import image_lfp_spectrum_plot
# #     data, fig, ax = image_lfp_spectrum_plot(psd.T, f, display=True)

# #     plt.show()
# #     plt.waitforbuttonpress
# #     plt.close('all')

# # # # This basically does this
# # # plt.imshow(10 * np.log10(psd), extent=[f[0], f[-1], 0, psd.shape[0]], origin='lower', aspect='auto')


# # ####for looking at individual trials

# # t_before = 1
# # t_after = 2
# # for j in clusters['cluster_id']:
# #     if brain_acronyms_percluster[j] == 'ZI' or brain_acronyms_percluster[j] == 'FF':# or brain_acronyms_percluster[j] == 'SNr':
# #         #clusters_labels[j] > 0.3

# #         current_cluster_spike_indices = np.where(allspikes.clusters == j)
# #         current_cluster_spike_indices = current_cluster_spike_indices[0]
# #         current_cluster_spike_times = allspikes.times[current_cluster_spike_indices]

# #         ### get waveforms
# #         wf_idx = np.where(wf_clusterIDs == j)[0]
# #         wfs = spike_wfs['waveforms'][wf_idx, :, :]
# #         # Compute average waveform on channel with max signal (chn_index 0)
# #         wf_avg_chn_max = np.mean(wfs[:, :, 0], axis=0)

# #         if np.size(wf_idx) < 5:  #this is strangely way lower than total spike count
# #             print('Not enough spikes for waveform analysis, skipping...')
# #             plt.close('all')
# #             continue

# #         if max(wf_avg_chn_max) > 4e-4 or min(wf_avg_chn_max) < -4e-4:
# #             print('Light artifact unit, skipping...')
# #             plt.close('all')
# #             continue

# #         for k in np.arange(0,np.size(trials.contrastRight)):
# #             # try:
# #             plt.rcParams["figure.figsize"] = (15,6)
# #             fig, (ax1, ax2) = plt.subplots(1, 2)

# #             ax1, plot_edge2, nonstim_ex_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
# #                                         allspikes.clusters,  # Then cluster ids
# #                                         # nonstim_trials_ex.intervals[:,0],  # Event markers we want to plot against
# #                                         trials.intervals[k,0],  # Event markers we want to plot against
# #                                         [j],  # Identity of the cluster we plot
# #                                         t_before=t_before, t_after=t_after,  # Time before and after the event
# #                                         error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #                                         include_raster=False,  # adds a raster to the bottom
# #                                         n_rasters=55,  # How many raster traces to include
# #                                         ax=ax1,  # Make sure we plot to the axis we created
# #                                         yticks=False,
# #                                         pethline_kwargs={'color': 'black', 'lw': 2},
# #                                         errbar_kwargs={'color': 'blue', 'alpha': 0.5},
# #                                         eventline_kwargs={'color': 'black', 'alpha': 0},
# #                                         raster_kwargs={'color': 'black', 'lw': 0.5},
# #                                         normalize_to_baseline = normalize_to_baseline)

# #             nonstim_trace = nonstim_ex_peth
# #             # excitation_trace = ex_peth.means[0]
# #             # inhibition_trace = in_peth.means[0]

# #             # if excitation_traces_percluster == []:
# #             #     excitation_traces_percluster = excitation_trace
# #             #     inhibition_traces_percluster = inhibition_trace
# #             #     nonstim_traces_percluster = nonstim_trace
# #             # else:
# #             #     excitation_traces_percluster = np.vstack([excitation_traces_percluster, excitation_trace])
# #             #     inhibition_traces_percluster = np.vstack([inhibition_traces_percluster, inhibition_trace])
# #             #     nonstim_traces_percluster = np.vstack([nonstim_traces_percluster, nonstim_trace])

# #             # rand_indices_wav = np.random.choice(wf_idx,15)
# #             # for k in rand_indices_wav:
# #             #     rand_wf = spike_wfs['waveforms'][k, :, 0]
# #             #     ax2 = plt.plot(rand_wf,'r-',linewidth=0.5)

# #             # ax2 = plt.plot(wf_avg_chn_max,'k-',linewidth = 3)

# #             # if plot_edge1 > plot_edge:
# #             #     plot_limit = plot_edge1
# #             # else:
# #             #     plot_limit = plot_edge

# #             # if np.isnan(plot_limit) == 1:
# #             #     plot_limit = 1

# #             # # plt.figure(num=1, figsize=(1, 0.75))
# #             # # ax1.set_xticks(fontsize = 11)
# #             # # ax1.set_yticks(fontsize = 11)
# #             # if plot_limit > 100:
# #             #     ax1.set_yticks(np.arange(0, 200, step=20))
# #             # if plot_limit < 100 and plot_limit > 20:
# #             #     ax1.set_yticks(np.arange(0, 100, step=5))
# #             # if plot_limit < 20:
# #             #     ax1.set_yticks(np.arange(0, 20, step=1))
# #             # ax1.set_ylim([0, plot_limit])
# #             ax1.set_xlabel('Time from laser onset (s)', fontsize = 13)
# #             ax1.set_ylabel('Firing rate (spikes/s)', fontsize = 13)
# #             plt.figure()
# #             plt.plot(nonstim_trace,'k')
# #             plt.show()
# #             plt.waitforbuttonpress
# #             plt.close('all')
# #             # except:
# #             #     print('Error with cluster (numspikes = ' + str(np.size(current_cluster_spike_indices)) + '). Skipping cluster...')
# #             #     continue


# # # avg_excitation_trace = np.average(excitation_traces_percluster,axis=0)
# # # avg_inhibition_trace = np.average(inhibition_traces_percluster,axis=0)
# # # avg_nonstim_trace = np.average(nonstim_traces_percluster,axis=0)

# # # plt.figure()
# # # plt.plot(nonstim_trace,'k')
# # # # plt.plot(avg_excitation_trace,'b')
# # # # plt.plot(avg_inhibition_trace,'r')
# # # plt.show()


# # ### for lower raster plots


# # # for j in clusters[probe_label].metrics['cluster_id']:
# # for j in np.arange(0,10):#clusters['cluster_id']:
# #     # if brain_acronyms_percluster[j] == 'ZI' or brain_acronyms_percluster[j] == 'FF' or brain_acronyms_percluster[j] == 'HY':
# #     # if brain_acronyms_percluster[j] == 'SNr':
# #     # if brain_acronyms_percluster[j] == 'MRN' or brain_acronyms_percluster[j] == 'RN':
# #     #clusters_labels[j] > 0.3
# #     if np.isin(j,light_artifact_units):
# #         continue
# #     print('cluster # = ' + str(j) + ', label = ' + str(clusters_labels[j]) + ', depth = ' + str(clusters.depths[j]) + ', region = ' + brain_acronyms_percluster[j])

# #     # brain_region = brain_acronyms_percluster[j]

# #     # if clusters.depths[j] < 1300:
# #     #     continue

# #     current_cluster_spike_indices = np.where(allspikes.clusters == j)
# #     current_cluster_spike_indices = current_cluster_spike_indices[0]
# #     current_cluster_spike_times = allspikes.times[current_cluster_spike_indices]

# #     ### get waveforms
# #     wf_idx = np.where(wf_clusterIDs == j)[0]
# #     wfs = spike_wfs['waveforms'][wf_idx, :, :]
# #     # Compute average waveform on channel with max signal (chn_index 0)
# #     wf_avg_chn_max = np.mean(wfs[:, :, 0], axis=0)

# #     if np.size(wf_idx) < 5:  #this is strangely way lower than total spike count
# #         print('Not enough spikes for waveform analysis, skipping...')
# #         plt.close('all')
# #         continue

# #     if max(wf_avg_chn_max) > 4e-4 or min(wf_avg_chn_max) < -4e-4:
# #         print('Light artifact unit, skipping...')
# #         plt.close('all')
# #         continue

# #     clusters_of_interest.append(j)

# #     # try:
# #     plt.rcParams["figure.figsize"] = (15,6)
# #     fig, (ax1, ax2) = plt.subplots(1, 2)

    
# #     # ax1, plot_edge2, nonstim_ex_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
# #     #                             allspikes.clusters,  # Then cluster ids
# #     #                             nonstim_trials_ex.intervals[:,0],  # Event markers we want to plot against
# #     #                             [j],  # Identity of the cluster we plot
# #     #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #     #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #     #                             include_raster=False,  # adds a raster to the bottom
# #     #                             n_rasters=55,  # How many raster traces to include
# #     #                             ax=ax1,  # Make sure we plot to the axis we created
# #     #                             yticks=False,
# #     #                             pethline_kwargs={'color': 'black', 'lw': 2},
# #     #                             errbar_kwargs={'color': 'blue', 'alpha': 0.5},
# #     #                             eventline_kwargs={'color': 'black', 'alpha': 0},
# #     #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #     #                             normalize_to_baseline = normalize_to_baseline)
# #     # ax1, plot_edge3, nonstim_in_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
# #     #                             allspikes.clusters,  # Then cluster ids
# #     #                             nonstim_trials_in.intervals[:,0],  # Event markers we want to plot against
# #     #                             [j],  # Identity of the cluster we plot
# #     #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #     #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #     #                             include_raster=False,  # adds a raster to the bottom
# #     #                             n_rasters=55,  # How many raster traces to include
# #     #                             ax=ax1,  # Make sure we plot to the axis we created
# #     #                             yticks=False,
# #     #                             pethline_kwargs={'color': 'black', 'lw': 2},
# #     #                             errbar_kwargs={'color': 'red', 'alpha': 0.5},
# #     #                             eventline_kwargs={'color': 'black', 'alpha': 0},
# #     #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #     #                             normalize_to_baseline = normalize_to_baseline)
# #     ax1, plot_edge1, ex_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
# #                                 allspikes.clusters,  # Then cluster ids
# #                                 excitation_trials.intervals[:,0],  # Event markers we want to plot against
# #                                 [j],  # Identity of the cluster we plot
# #                                 t_before=t_before, t_after=t_after,  # Time before and after the event
# #                                 error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #                                 include_raster=True,  # adds a raster to the bottom
# #                                 n_rasters=55,  # How many raster traces to include
# #                                 # ax=ax1,  # Make sure we plot to the axis we created
# #                                 yticks=False,
# #                                 pethline_kwargs={'color': 'blue', 'lw': 2},
# #                                 errbar_kwargs={'color': 'blue', 'alpha': 0.5},
# #                                 eventline_kwargs={'color': 'black', 'alpha': 0},
# #                                 raster_kwargs={'color': 'black', 'lw': 0.5},
# #                                 normalize_to_baseline = normalize_to_baseline)
# #     # ax1, plot_edge, in_peth = peri_event_time_histogram(allspikes.times,  # Spike times first
# #     #                             allspikes.clusters,  # Then cluster ids
# #     #                             inhibition_trials.intervals[:,0],  # Event markers we want to plot against
# #     #                             [j],  # Identity of the cluster we plot
# #     #                             t_before=t_before, t_after=t_after,  # Time before and after the event
# #     #                             error_bars='sem',  # Whether we want Stdev, SEM, or no error
# #     #                             include_raster=False,  # adds a raster to the bottom
# #     #                             n_rasters=55,  # How many raster traces to include
# #     #                             ax=ax1,  # Make sure we plot to the axis we created
# #     #                             yticks=False,
# #     #                             pethline_kwargs={'color': 'red', 'lw': 2},
# #     #                             errbar_kwargs={'color': 'red', 'alpha': 0.5},
# #     #                             eventline_kwargs={'color': 'black', 'alpha': 0.6},
# #     #                             raster_kwargs={'color': 'black', 'lw': 0.5},
# #     #                             normalize_to_baseline = normalize_to_baseline)

# #     # nonstim_trace = np.average(np.array([nonstim_ex_peth.means[0],nonstim_in_peth.means[0]]), axis=0)
# #     # excitation_trace = ex_peth.means[0]
# #     # inhibition_trace = in_peth.means[0]

# #     # if excitation_traces_percluster == []:
# #     #     excitation_traces_percluster = excitation_trace
# #     #     inhibition_traces_percluster = inhibition_trace
# #     #     nonstim_traces_percluster = nonstim_trace
# #     # else:
# #     #     excitation_traces_percluster = np.vstack([excitation_traces_percluster, excitation_trace])
# #     #     inhibition_traces_percluster = np.vstack([inhibition_traces_percluster, inhibition_trace])
# #     #     nonstim_traces_percluster = np.vstack([nonstim_traces_percluster, nonstim_trace])

# #     rand_indices_wav = np.random.choice(wf_idx,15)
# #     for k in rand_indices_wav:
# #         rand_wf = spike_wfs['waveforms'][k, :, 0]
# #         ax2 = plt.plot(rand_wf,'r-',linewidth=0.5)

# #     ax2 = plt.plot(wf_avg_chn_max,'k-',linewidth = 3)

# #     # if plot_edge1 > plot_edge:
# #     #     plot_limit = plot_edge1
# #     # else:
# #     #     plot_limit = plot_edge

# #     # if np.isnan(plot_limit) == 1:
# #     #     plot_limit = 1

# #     # # plt.figure(num=1, figsize=(1, 0.75))
# #     # # ax1.set_xticks(fontsize = 11)
# #     # # ax1.set_yticks(fontsize = 11)
# #     # if plot_limit > 100:
# #     #     ax1.set_yticks(np.arange(0, 200, step=20))
# #     # if plot_limit < 100 and plot_limit > 20:
# #     #     ax1.set_yticks(np.arange(0, 100, step=5))
# #     # if plot_limit < 20:
# #     #     ax1.set_yticks(np.arange(0, 20, step=1))
# #     # ax1.set_ylim([0, plot_limit])
# #     ax1.set_xlabel('Time from laser onset (s)', fontsize = 13)
# #     ax1.set_ylabel('Firing rate (spikes/s)', fontsize = 13)
# #     plt.show()
# #     plt.waitforbuttonpress
# #     plt.close('all')
# #     # except:
# #     #     print('Error with cluster (numspikes = ' + str(np.size(current_cluster_spike_indices)) + '). Skipping cluster...')
# #     #     continue

# # cluster_num = 36
# # spike_indices = np.where(allspikes.clusters == cluster_num)
# # spike_times = allspikes.times[spike_indices]
# # plt.plot(spike_times,np.zeros((len(spike_times),), dtype=int),'k+')
# # plt.plot(excitation_trials.intervals[:,0],np.zeros((len(excitation_trials.intervals[:,0]),), dtype=int),'bo')
# # plt.plot(inhibition_trials.intervals[:,0],np.zeros((len(inhibition_trials.intervals[:,0]),), dtype=int),'ro')
# # plt.show()
# # try:



# # j = 46
# # # for j in clusters['cluster_id']:

# # # if clusters_labels[j] == 0:
# # #     continue
# # # print('cluster # = ' + str(j) + ', label = ' + str(clusters_labels[j]) + ', depth = ' + str(clusters.depths[j]) + ', region = ' + brain_acronyms_percluster[j])

# # plt.rcParams["figure.figsize"] = (15,6)
# # fig, ax1 = plt.subplots(1, 1)

# # spike_times_for_this_cluster = allspikes.times[np.where(allspikes.clusters == j)[0]]

# # plt.vlines(spike_times_for_this_cluster, -1, 1)
# # plt.vlines(trials.intervals[:,0], -1, 1, colors = 'r')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0],np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0]+0.02,np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0]+0.04,np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0]+0.06,np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0]+0.08,np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[excitation_trials_numbers][:,0]+0.1,np.zeros(np.size(excitation_trials_numbers)).astype(int),'bx')
# # plt.plot(trials.intervals[inhibition_trials_numbers][:,0],np.zeros(np.size(inhibition_trials_numbers)).astype(int),'rx')
# # plt.plot(trials.feedback_times,np.zeros(np.size(trials.feedback_times)).astype(int),'gx')


# # for n in np.arange(0,np.size(trials.probabilityLeft)):
# #     plt.text(trials.intervals[n,0],0,str(n))

# # plt.show()
# # plt.waitforbuttonpress
# # plt.close('all')

# # latencies = np.empty(len(trials.intervals[excitation_trials_numbers][:,0]))
# # latencies[:] = np.NaN
# # for k in np.arange(0,np.size(trials.intervals[excitation_trials_numbers][:,0])):
# #     latencies[k] = spike_times_for_this_cluster[np.where(spike_times_for_this_cluster > trials.intervals[excitation_trials_numbers][:,0][k])][0] - trials.intervals[excitation_trials_numbers][:,0][k]

# # np.percentile(latencies,95)

# # latencies = np.empty(len(trials.intervals[inhibition_trials_numbers][:,0]))
# # latencies[:] = np.NaN
# # for k in np.arange(0,np.size(trials.intervals[inhibition_trials_numbers][:,0])):
# #     latencies[k] = spike_times_for_this_cluster[np.where(spike_times_for_this_cluster > trials.intervals[inhibition_trials_numbers][:,0][k])][0] - trials.intervals[inhibition_trials_numbers][:,0][k]

# # np.percentile(latencies,95)