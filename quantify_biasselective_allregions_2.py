import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns
from brainbox.io.one import SpikeSortingLoader

from one.api import ONE
from pathlib import Path
from scipy import stats
from os.path import join
import pickle
from iblatlas.atlas import AllenAtlas, BrainRegions
from scipy.stats import ranksums
from statsmodels.stats.multitest import multipletests

import sys
sys.path.append('/Users/natemiska/python/bias_coding')
from functions_optostim import signed_contrast, peri_event_time_histogram, generate_pseudo_sessions, isbiasblockselective_perm_vector

ba = AllenAtlas()
br = BrainRegions()
###currently manually defining which to use

def filter_trials(stim_choice, stim_contrast, stim_side):
    if (stim_choice == 'all') & (stim_contrast == 'all') & (stim_side == 'both'):
        trials_id = np.arange(len(trials.choice))
    if (stim_choice == 'all') & (stim_contrast == 'all') & (stim_side != 'both'):
        contrast = 'contrastRight' if stim_side == 'right' else 'contrastLeft'
        trials_id = np.where(np.isfinite(trials[contrast]))[0]
    if (stim_choice == 'all') & (stim_contrast != 'all') & (stim_side == 'both'):
        trials_id = np.where((trials['contrastRight'] == stim_contrast) | (trials['contrastLeft'] == stim_contrast))[0]
    if (stim_choice != 'all') & (stim_contrast == 'all') & (stim_side == 'both'):
        outcome = 1 if stim_choice == 'correct' else -1
        trials_id = np.where(trials['feedbackType'] == outcome)[0]
    if (stim_choice == 'all') & (stim_contrast != 'all') & (stim_side != 'both'):
        contrast = 'contrastRight' if stim_side == 'right' else 'contrastLeft'
        trials_id = np.where(trials[contrast] == stim_contrast)[0]
    if (stim_choice != 'all') & (stim_contrast == 'all') & (stim_side != 'both'):
        contrast = 'contrastRight' if stim_side == 'right' else 'contrastLeft'
        outcome = 1 if stim_choice == 'correct' else -1
        trials_id = np.where((trials['feedbackType'] == outcome) & (np.isfinite(trials[contrast])))[0]  
    if  (stim_choice != 'all') & (stim_contrast != 'all') & (stim_side == 'both'):
        outcome = 1 if stim_choice == 'correct' else -1
        trials_id = np.where(((trials['contrastLeft'] == stim_contrast) | (trials['contrastRight'] == stim_contrast)) & (trials['feedbackType'] == outcome))[0]
    if (stim_choice != 'all') & (stim_contrast != 'all') & (stim_side != 'both'):
        contrast = 'contrastRight' if stim_side == 'right' else 'contrastLeft'
        outcome = 1 if stim_choice == 'correct' else -1
        trials_id = np.where((trials[contrast] == stim_contrast) & (trials['feedbackType'] == outcome))[0]
    return trials_id

### below may be depricated
def query_sessions_pids_all(selection='resolved-behavior'):
    # from one.api import ONE
    one = ONE(base_url='https://alyx.internationalbrainlab.org')

    if selection == 'all':
        # Query all ephysChoiceWorld sessions
        ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                               'session__qc__lt,50')
    if selection == 'behavior':
        # Query all ephysChoiceWorld sessions
        ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                               'session__qc__lt,50,'
                               'session__extended_qc__behavior,1')
    elif selection == 'aligned':
        # Query all sessions with at least one alignment
        ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                               'session__qc__lt,50,'
                               'json__extended_qc__alignment_count__gt,0')
    elif selection == 'resolved':
        # Query all sessions with resolved alignment
         ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                               'session__qc__lt,50,'
                               'json__extended_qc__alignment_resolved,True')
    elif selection == 'aligned-behavior':
        # Query sessions with at least one alignment and that meet behavior criterion
        ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                               'session__qc__lt,50,'
                               'json__extended_qc__alignment_count__gt,0,'
                               'session__extended_qc__behavior,1')
    elif selection == 'resolved-behavior':
        # Query sessions with resolved alignment and that meet behavior criterion
        ins = one.alyx.rest('insertions', 'list',
                        django='session__project__name__icontains,ibl_neuropixel_brainwide_01,'
                                'session__qc__lt,50,'
                                'json__extended_qc__alignment_resolved,True,'
                                'session__extended_qc__behavior,1')
    else:
        ins = []

    # Get list of eids and probes
    all_pids = np.array([item['id'] for item in ins])
    # all_probes = np.array([i['name'] for i in ins])
    all_pids = np.unique(all_pids)
    # probes = []

    # for i, eid in enumerate(eids):
    #     probes.append(all_probes[[s == eid for s in all_eids]])
    return all_pids

one = ONE(base_url='https://alyx.internationalbrainlab.org')

# ins_str_query = 'datasets__tags__name,Brainwidemap'
# aligned_pids = one.alyx.rest('insertions', 'list', django=ins_str_query) ### satisfies behaviour criteria

# aligned_pids = query_sessions_pids_all(selection='resolved-behavior')
# aligned_pids = np.unique(aligned_pids_all, axis=0)
aligned_pids = one.search_insertions(datasets='spikes.times.npy', project='brainwide')

aligned_pids_df = pd.DataFrame(aligned_pids)
aligned_pids_df.to_pickle('~/python/saved_figures/' + 'aligned_pids_df_all' + '.pkl')
   
    # np.save('aligned_eids.npy', aligned_eids)
    # np.save('aligned_probe_labels.npy', aligned_eids)
    ###save aligned eids in case of crash

########################## OPTIONS ############################

cluster_label_threshold = 0.3

FR_threshold = 1

###############################################################
num_failed_sessions = 0
region_clusters_info = pd.DataFrame()
delta_FR_higher = np.empty([1000,12])
delta_FR_higher[:] = np.nan
delta_FR_lower = np.empty([1000,12])
delta_FR_lower[:] = np.nan
allunits_FR_block_length_20 = np.empty([1000,30])
allunits_FR_block_length_20[:] = np.nan
allunits_FR_block_length_80 = np.empty([1000,30])
allunits_FR_block_length_80[:] = np.nan
allunits_FR_block_length_20_higher = np.empty([1000,30])
allunits_FR_block_length_20_higher[:] = np.nan
allunits_FR_block_length_80_higher = np.empty([1000,30])
allunits_FR_block_length_80_higher[:] = np.nan
allunits_FR_block_length_20_lower = np.empty([1000,30])
allunits_FR_block_length_20_lower[:] = np.nan
allunits_FR_block_length_80_lower = np.empty([1000,30])
allunits_FR_block_length_80_lower[:] = np.nan
num_units = 0
for k in np.arange(0,np.size(aligned_pids)):

    try:
        print('\nProcessing session %d of %d' % (k+1, len(aligned_pids)))

        pid = aligned_pids[k]
        ssl = SpikeSortingLoader(pid=pid, one=one, atlas=ba)
        eid = ssl.eid
        trials = one.load_object(eid, 'trials')
        ses_path = one.eid2path(eid)

        print(eid)
        ses_info = one.get_details(eid)
        subject = ses_info['subject']
        date = ses_info['start_time'][:10]

        # probe_labels = aligned_probe_labels[k]

        ###load and initialize trial data
        # ses_path = one.eid2path(eid)
        # _ = one.load(eid, dataset_types=['trials.stimOn_times', 'trials.probabilityLeft',
        #                                 'trials.contrastLeft', 'trials.contrastRight',
        #                                 'trials.feedbackType', 'trials.choice',
        #                                 'trials.feedback_times'],
        #             download_only=True, clobber=True)
        # trials = alf.io.load_object(join(ses_path, 'alf'), 'trials')
        #rt = load_wheel_reaction_times(eid)
        trials_leftprob = trials.probabilityLeft
        alltrials = filter_trials(stim_choice='all',stim_contrast='all', stim_side='both')
        left_trials_100 = filter_trials(stim_choice='all', stim_contrast=1, stim_side='left')
        left_trials_25 = filter_trials(stim_choice='all', stim_contrast=0.25, stim_side='left')
        left_trials_12 = filter_trials(stim_choice='all', stim_contrast=0.125, stim_side='left')
        left_trials_6 = filter_trials(stim_choice='all', stim_contrast=0.0625, stim_side='left')
        left_trials_all = np.concatenate((left_trials_100, left_trials_25, left_trials_12, left_trials_6), axis=0)
        left_trials_all = np.sort(left_trials_all)
        left_trials_0 = filter_trials(stim_choice='all', stim_contrast=0, stim_side='left')
        right_trials_100 = filter_trials(stim_choice='all', stim_contrast=1, stim_side='right')
        right_trials_25 = filter_trials(stim_choice='all', stim_contrast=0.25, stim_side='right')
        right_trials_12 = filter_trials(stim_choice='all', stim_contrast=0.125, stim_side='right')
        right_trials_6 = filter_trials(stim_choice='all', stim_contrast=0.0625, stim_side='right')
        right_trials_all = np.concatenate((right_trials_100, right_trials_25, right_trials_12, right_trials_6), axis=0)
        right_trials_all = np.sort(right_trials_all)
        right_trials_0 = filter_trials(stim_choice='all', stim_contrast=0, stim_side='right')
        moverightcorrect_trials = filter_trials(stim_choice='correct', stim_contrast='all', stim_side='left')
        moverightincorrect_trials = filter_trials(stim_choice='incorrect', stim_contrast='all', stim_side='right')
        moveleftcorrect_trials = filter_trials(stim_choice='correct', stim_contrast='all', stim_side='right')
        moveleftincorrect_trials = filter_trials(stim_choice='incorrect', stim_contrast='all', stim_side='left')
        moveright_trials = np.concatenate((moverightcorrect_trials, moveleftincorrect_trials), axis=0)
        moveleft_trials = np.concatenate((moveleftcorrect_trials, moverightincorrect_trials), axis=0)
        correct_trials = np.concatenate((moveleftcorrect_trials, moverightcorrect_trials), axis=0)
        #correct_trials = filter_trials(stim_choice='correct', stim_contrast='all', stim_side='all')
        incorrect_trials = filter_trials(stim_choice='incorrect', stim_contrast='all', stim_side='all')
        trials_100 = filter_trials(stim_choice='all',stim_contrast=1, stim_side='both')
        trials_25 = filter_trials(stim_choice='all',stim_contrast=0.25, stim_side='both')
        hc_trials = np.concatenate((trials_100,trials_25),axis=0)
        trials_0 = filter_trials(stim_choice='all',stim_contrast=0, stim_side='both')
        trials_6 = filter_trials(stim_choice='all',stim_contrast=0.0625, stim_side='both')
        lc_trials = np.concatenate((trials_0,trials_6),axis=0)
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

        ###load neural data and analyze for each probe
        # for l in np.arange(0,np.size(probe_labels)):
        spikes, clusters, channels = ssl.load_spike_sorting()
        probe_label = ssl.pname
        clusters = ssl.merge_clusters(spikes, clusters, channels)
        # spike_wfs = one.load_object(ssl.eid, '_phy_spikes_subset', collection=ssl.collection)
        # wf_clusterIDs = spikes['clusters'][spike_wfs['spikes']]
        clusters_labels = clusters['label']

        # probe_label = probe_labels[l]
        # spikes = allspikes[probe_label]
        # labels = clusters[probe_label]['metrics']['ks2_label']
        brain_acronyms_percluster = clusters['acronym']
        allclusters_array = np.arange(0, np.size(brain_acronyms_percluster))
        max_index = np.size(allclusters_array)
        mean_firing_rates = clusters['firing_rate']

        ###generate 1000 pseudo sessions
        pseudo_20_index_filtered,pseudo_80_index_filtered = generate_pseudo_sessions(trials)

        ### legacy code; remove and simplify at some point
        isregion = np.ones(np.size(brain_acronyms_percluster))
        region_indices = np.where(isregion == 1)[0]

        ### calculate FR
        print('Adding clusters to dataframe')

        for j in region_indices: ### legacy code
            if j in spikes.clusters and clusters_labels[j] >= cluster_label_threshold and mean_firing_rates[j] > FR_threshold:
                # print(j)
                ### calculate FR (400ms:gocue)
                current_unit_allen_label = brain_acronyms_percluster[j]
                current_unit_spike_indices = np.where(spikes.clusters == j)
                current_unit_spike_indices = current_unit_spike_indices[0]
                current_unit_spike_times = spikes.times[current_unit_spike_indices]
                fr_per_trial = np.empty((1, np.size(alltrials)))
                fr_per_trial[:] = np.nan
                fr_per_trial = fr_per_trial[0]
                isbiasselective, p_empirical, pval_real, stat_real, stat_pseudo, fr_80_trials_nonstim, fr_20_trials_nonstim, [], [] = isbiasblockselective_perm_vector(
                        current_unit_spike_times, trials.probabilityLeft, trials.goCue_times,
                        [], range(0,len(trials.probabilityLeft)-1),
                        pseudo_20_index_filtered, pseudo_80_index_filtered,
                        trials.quiescencePeriod,
                        blocklength_filterval = 10, before_gocue_end_time = 0.01, 
                        alpha = 0.05)

                # for k in np.arange(0,np.size(trials.goCue_times)):
                #     current_trial_start_time = trials.goCue_times[k] - 0.4
                #     current_trial_end_time = trials.goCue_times[k] - 0.05
                #     numspikes_current_trial = np.where(np.logical_and(current_unit_spike_times>current_trial_start_time, current_unit_spike_times<current_trial_end_time))
                #     numspikes_current_trial = numspikes_current_trial[0]
                #     numspikes_current_trial = np.size(numspikes_current_trial)
                #     fr_per_trial[k] = numspikes_current_trial/0.35
                    
                # #     ###calculate block trial # dependent firing
                # #     if k+1 < 91:
                # #         current_block_length = current_block_length + 1
                # #         ###5050 block here
                # #         continue
                # #     if k+1 = 91:
                # #         if np.isin(k+1,alltrialcounts_80_index):
                # #             current_block_ID = 80
                # #             current_block_length = 1
                # #         else:
                # #             current_block_ID = 20
                # #             current_block_length = 1

                # fr_80_trials = fr_per_trial[alltrialcounts_80_index_filtered]
                # fr_20_trials = fr_per_trial[alltrialcounts_20_index_filtered]

                # FR_block_length_80 = np.empty(30,)
                # FR_block_length_80[:] = np.nan
                # FR_block_length_20 = np.empty(30,)
                # FR_block_length_20[:] = np.nan
                # for k in np.arange(0,30):
                #     trials_where_length = np.where(alltrialcounts_80==k+1)[1]
                #     FR_block_length_80[k] = np.nanmean(fr_per_trial[trials_where_length])
                #     trials_where_length = np.where(alltrialcounts_20==k+1)[1]
                #     FR_block_length_20[k] = np.nanmean(fr_per_trial[trials_where_length])

                # norm_FR_block_length_80 = FR_block_length_80/np.nanmean(fr_per_trial)
                # norm_FR_block_length_20 = FR_block_length_20/np.nanmean(fr_per_trial)

                # t, pval_real = stats.ttest_ind(fr_80_trials, fr_20_trials, equal_var=False)

                # # print('Performing pseudo-block analysis')
                # pseudo_pvals = np.empty(num_pseudo_blocks)
                # pseudo_pvals[:] = np.nan
                # for k in range(num_pseudo_blocks):     
                #     fr_80_trials_pseudo = fr_per_trial[pseudo_80_index_filtered[k]]
                #     fr_20_trials_pseudo = fr_per_trial[pseudo_20_index_filtered[k]]
                #     t, pval_pseudo = stats.ttest_ind(fr_80_trials_pseudo, fr_20_trials_pseudo, equal_var=False)
                #     pseudo_pvals[k] = pval_pseudo

                # pct50_pseudo = np.percentile(pseudo_pvals,50)
                # pct95_pseudo = np.percentile(pseudo_pvals,5)
                # pct99_pseudo = np.percentile(pseudo_pvals,1)
                # pct999_pseudo = np.percentile(pseudo_pvals,0.1)
                # #how significance assessed

                # if pval_real < pct999_pseudo:
                #     isbiasselective999 = 1
                #     isbiasselective99 = 1
                #     isbiasselective95 = 1

                # elif pval_real < pct99_pseudo:
                #     isbiasselective999 = 0
                #     isbiasselective99 = 1
                #     isbiasselective95 = 1

                # elif pval_real < pct95_pseudo:
                #     isbiasselective999 = 0
                #     isbiasselective99 = 0
                #     isbiasselective95 = 1

                # else:
                #     isbiasselective999 = 0
                #     isbiasselective99 = 0
                #     isbiasselective95 = 0

                # ### new definition BS unit: pval_real < 0.05 (or 0.01) AND pval_real < 50th percentile of pseudo blocks
                # if pval_real < 0.01 and pval_real < pct50_pseudo:
                #     isbiasselective01_new = 1
                #     isbiasselective05_new = 1
                # elif pval_real < 0.05 and pval_real < pct50_pseudo:
                #     isbiasselective01_new = 0
                #     isbiasselective05_new = 1
                # else:
                #     isbiasselective01_new = 0
                #     isbiasselective05_new = 0

                current_unit_beryl_label = br.acronym2acronym(current_unit_allen_label, mapping='Beryl')

                x_coord = clusters['x'][j] ###save x/y/z coordinates of bs ZI clusters
                y_coord = clusters['y'][j]
                z_coord = clusters['z'][j]
                region_clusters_info = pd.concat([region_clusters_info,pd.DataFrame(
                    index=[region_clusters_info.shape[0] + 1], data={
                                        'Allenregion': current_unit_allen_label,
                                        'Berylregion': current_unit_beryl_label,
                                        'pid': pid,
                                        'z': z_coord,
                                        'y': y_coord,
                                        'x': x_coord,
                                        'IBLlabel': clusters_labels[j],
                                        'clustnum': j,
                                        'pval': p_empirical,
                                        # 'pct95_ps': pct95_pseudo,
                                        'bs': isbiasselective})])
                #save dataframe
                # region_clusters_info.to_pickle('~/Documents/python/saved_figures/' + 'bs_analysis_allregions_dataframe_V5' + '.pkl')
                region_clusters_info.to_csv('~/python/saved_figures/' + 'bs_analysis_allregions_dataframe_newanalysis.csv', index=False)

                # pd.set_option('display.max_rows', None)

    except Exception as error_message:
        print(error_message)
        print('Skipping session...')
        num_failed_sessions = num_failed_sessions + 1


# ###plotting
# # region_clusters_info = region_clusters_info[region_clusters_info.x<0] ###remove R hemisphere

# # region_clusters_indices_95 = np.where(region_clusters_info.pval > 0.05)[0] + 1
# # region_clusters_indices_05 = np.where(np.logical_and(region_clusters_info.pval < 0.05, region_clusters_info.pval > 0.01))[0] + 1
# # region_clusters_indices_01 = np.where(np.logical_and(region_clusters_info.pval < 0.01, region_clusters_info.pval > 0.001))[0] + 1
# # region_clusters_indices_001 = np.where(region_clusters_info.pval < 0.001)[0] + 1
# region_clusters_indices_sig = np.where(region_clusters_info.bs == 1)[0] + 1
# region_clusters_indices_nonsig = np.where(region_clusters_info.bs == 0)[0] + 1
# # x_05 = list(region_clusters_info.x[region_clusters_indices_05])
# # y_05 = list(region_clusters_info.y[region_clusters_indices_05])
# # z_05 = list(region_clusters_info.z[region_clusters_indices_05])
# # x_01 = list(region_clusters_info.x[region_clusters_indices_01])
# # y_01 = list(region_clusters_info.y[region_clusters_indices_01])
# # z_01 = list(region_clusters_info.z[region_clusters_indices_01])
# # x_001 = list(region_clusters_info.x[region_clusters_indices_001])
# # y_001 = list(region_clusters_info.y[region_clusters_indices_001])
# # z_001 = list(region_clusters_info.z[region_clusters_indices_001])
# # x_95 = list(region_clusters_info.x[region_clusters_indices_95])
# # y_95 = list(region_clusters_info.y[region_clusters_indices_95])
# # z_95 = list(region_clusters_info.z[region_clusters_indices_95])
# x_sig = list(region_clusters_info.x[region_clusters_indices_sig])
# y_sig = list(region_clusters_info.y[region_clusters_indices_sig])
# z_sig = list(region_clusters_info.z[region_clusters_indices_sig])
# x_nonsig = list(region_clusters_info.x[region_clusters_indices_nonsig])
# y_nonsig = list(region_clusters_info.y[region_clusters_indices_nonsig])
# z_nonsig = list(region_clusters_info.z[region_clusters_indices_nonsig])
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# #ax = fig.add_subplot(111, projection='3d')
# ax = Axes3D(fig)
# ax.scatter(x_nonsig, y_nonsig, z_nonsig, alpha=0.1)#c='black', s=10)
# # ax.scatter(x_05, y_05, z_05, c='yellow', s=20)#c=None, depthshade=True, *args, **kwargs)
# # ax.scatter(x_01, y_01, z_01, c='orange', s=20)
# ax.scatter(x_sig, y_sig, z_sig, c='red', s=20)
# # plt.xlim(-0.003, 0)
# # plt.ylim(-1, 1)

# proportion_sig = np.size(region_clusters_indices_sig)/(np.size(region_clusters_indices_sig)+np.size(region_clusters_indices_nonsig))
# print('proportion sig =' + str(proportion_sig))
# print('total # units = ' + str((np.size(region_clusters_indices_sig)+np.size(region_clusters_indices_nonsig))))

# plt.show()


# # min_x = np.min(region_clusters_info.x)
# # max_x = np.max(region_clusters_info.x)
# # min_y = np.min(region_clusters_info.y)
# # max_y = np.max(region_clusters_info.y)
# # min_z = np.min(region_clusters_info.z)
# # max_z = np.max(region_clusters_info.z)

# # voxel_size = 0.0006
# # num_edges_x = round(((max_x - min_x)/voxel_size) + 0.5)
# # num_edges_y = round(((max_y - min_y)/voxel_size) + 0.5)
# # num_edges_z = round(((max_z - min_z)/voxel_size) + 0.5)
# # num_voxels = num_edges_x * num_edges_y * num_edges_z
# # x_coord_plotting = list()
# # y_coord_plotting = list()
# # z_coord_plotting = list()
# # proportion_plotting = list()
# # for i in np.arange(0,num_edges_x):
# #     for j in np.arange(0,num_edges_y):
# #         for k in np.arange(0,num_edges_z):
# #             lower_x_voxel = min_x + (i*voxel_size)
# #             upper_x_voxel = min_x + ((i+1)*voxel_size)
# #             lower_y_voxel = min_y + (j*voxel_size)
# #             upper_y_voxel = min_y + ((j+1)*voxel_size)
# #             lower_z_voxel = min_z + (k*voxel_size)
# #             upper_z_voxel = min_z + ((k+1)*voxel_size)
# #             x_coord_plotting.append(lower_x_voxel + (voxel_size/2))
# #             y_coord_plotting.append(lower_y_voxel + (voxel_size/2))
# #             z_coord_plotting.append(lower_z_voxel + (voxel_size/2))
# #             total_units_invoxel = 0
# #             total_BS_units_invoxel = 0
# #             for l in np.arange(np.min(region_clusters_info.index),np.max(region_clusters_info.index)+1):
# #                 if region_clusters_info.x[l] >= lower_x_voxel and region_clusters_info.x[l] < upper_x_voxel and region_clusters_info.y[l] >= lower_y_voxel and region_clusters_info.y[l] < upper_y_voxel and region_clusters_info.z[l] >= lower_z_voxel and region_clusters_info.z[l] < upper_z_voxel:
# #                     total_units_invoxel = total_units_invoxel + 1
# #                     if region_clusters_info.bs[l] == 1:
# #                         total_BS_units_invoxel = total_BS_units_invoxel + 1
# #             if total_units_invoxel == 0:
# #                 proportion_plotting.append(np.nan)
# #             else:
# #                 proportion_plotting.append(total_BS_units_invoxel/total_units_invoxel)
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D
# # fig = plt.figure()
# # ax = Axes3D(fig)
# # ax.scatter(x_coord_plotting, y_coord_plotting, z_coord_plotting, c=proportion_plotting, cmap='hot_r', marker = 's', s=200)
# # ax.scatter(x_nonsig, y_nonsig, z_nonsig, c='black', s=20, marker='x')
# # ax.scatter(x_sig, y_sig, z_sig, c='red', s=40)
# # plt.show()

# # #save dataframe
# # region_clusters_info.to_pickle('~/Documents/python/saved_figures/' + region_of_interest + '.pkl')

# # import pickle
# # import numpy as np 
# # import matplotlib.pyplot as plt
# # import pandas as pd

# # cd ~/Documents/python/saved_figures/
# # with open('MOp' + '.pkl', 'rb') as f:
# #     data = pickle.load(f)

# # region_clusters_info = data
# # # region_clusters_info[region_clusters_info.y>-0.0028]
# # # a = region_clusters_info[region_clusters_info.bs==1]

# # ###plotting delta FR as function of # trials within block
# # mean_FR_block_length_80 = np.empty([1,30])[0]
# # mean_FR_block_length_80[:] = np.nan
# # mean_FR_block_length_20 = np.empty([1,30])[0]
# # mean_FR_block_length_20[:] = np.nan
# # sem_FR_block_length_80 = np.empty([1,30])[0]
# # sem_FR_block_length_80[:] = np.nan
# # sem_FR_block_length_20 = np.empty([1,30])[0]
# # sem_FR_block_length_20[:] = np.nan
# # mean_FR_block_length_80_higher = np.empty([1,30])[0]
# # mean_FR_block_length_80_higher[:] = np.nan
# # mean_FR_block_length_20_higher = np.empty([1,30])[0]
# # mean_FR_block_length_20_higher[:] = np.nan
# # sem_FR_block_length_80_higher = np.empty([1,30])[0]
# # sem_FR_block_length_80_higher[:] = np.nan
# # sem_FR_block_length_20_higher = np.empty([1,30])[0]
# # sem_FR_block_length_20_higher[:] = np.nan
# # mean_FR_block_length_80_lower = np.empty([1,30])[0]
# # mean_FR_block_length_80_lower[:] = np.nan
# # mean_FR_block_length_20_lower = np.empty([1,30])[0]
# # mean_FR_block_length_20_lower[:] = np.nan
# # sem_FR_block_length_80_lower = np.empty([1,30])[0]
# # sem_FR_block_length_80_lower[:] = np.nan
# # sem_FR_block_length_20_lower = np.empty([1,30])[0]
# # sem_FR_block_length_20_lower[:] = np.nan
# # for k in np.arange(0,30):
# #     mean_FR_block_length_80[k] = np.nanmean(allunits_FR_block_length_80[:,k])
# #     mean_FR_block_length_20[k] = np.nanmean(allunits_FR_block_length_20[:,k])
# #     sem_FR_block_length_80[k] = stats.sem(allunits_FR_block_length_80[:,k],nan_policy = 'omit')
# #     sem_FR_block_length_20[k] = stats.sem(allunits_FR_block_length_20[:,k],nan_policy = 'omit')
# #     mean_FR_block_length_80_higher[k] = np.nanmean(allunits_FR_block_length_80_higher[:,k])
# #     mean_FR_block_length_20_higher[k] = np.nanmean(allunits_FR_block_length_20_higher[:,k])
# #     sem_FR_block_length_80_higher[k] = stats.sem(allunits_FR_block_length_80_higher[:,k],nan_policy = 'omit')
# #     sem_FR_block_length_20_higher[k] = stats.sem(allunits_FR_block_length_20_higher[:,k],nan_policy = 'omit')
# #     mean_FR_block_length_80_lower[k] = np.nanmean(allunits_FR_block_length_80_lower[:,k])
# #     mean_FR_block_length_20_lower[k] = np.nanmean(allunits_FR_block_length_20_lower[:,k])
# #     sem_FR_block_length_80_lower[k] = stats.sem(allunits_FR_block_length_80_lower[:,k],nan_policy = 'omit')
# #     sem_FR_block_length_20_lower[k] = stats.sem(allunits_FR_block_length_20_lower[:,k],nan_policy = 'omit')

# # plt.errorbar(np.arange(1,30),mean_FR_block_length_80[1:30],sem_FR_block_length_80[1:30], ecolor='r')
# # plt.errorbar(np.arange(1,30),mean_FR_block_length_20[1:30],sem_FR_block_length_20[1:30], ecolor='r')
# # plt.show()

# # plt.errorbar(np.arange(1,30),mean_FR_block_length_80_higher[1:30],sem_FR_block_length_80_higher[1:30], ecolor='r')
# # plt.errorbar(np.arange(1,30),mean_FR_block_length_20_higher[1:30],sem_FR_block_length_20_higher[1:30], ecolor='r')
# # plt.show()

# # plt.errorbar(np.arange(1,30),mean_FR_block_length_80_lower[1:30],sem_FR_block_length_80_lower[1:30], ecolor='r')
# # plt.errorbar(np.arange(1,30),mean_FR_block_length_20_lower[1:30],sem_FR_block_length_20_lower[1:30], ecolor='r')
# # plt.show()

# # ###plotting delta FR as function of # consecutive left or right trials
# # mean_deltaFR_left_6_higher = np.nanmean(delta_FR_higher[:,0])
# # mean_deltaFR_left_5_higher = np.nanmean(delta_FR_higher[:,1])
# # mean_deltaFR_left_4_higher = np.nanmean(delta_FR_higher[:,2])
# # mean_deltaFR_left_3_higher = np.nanmean(delta_FR_higher[:,3])
# # mean_deltaFR_left_2_higher = np.nanmean(delta_FR_higher[:,4])
# # mean_deltaFR_left_1_higher = np.nanmean(delta_FR_higher[:,5])
# # mean_deltaFR_right_1_higher = np.nanmean(delta_FR_higher[:,6])
# # mean_deltaFR_right_2_higher = np.nanmean(delta_FR_higher[:,7])
# # mean_deltaFR_right_3_higher = np.nanmean(delta_FR_higher[:,8])
# # mean_deltaFR_right_4_higher = np.nanmean(delta_FR_higher[:,9])
# # mean_deltaFR_right_5_higher = np.nanmean(delta_FR_higher[:,10])
# # mean_deltaFR_right_6_higher = np.nanmean(delta_FR_higher[:,11])
# # sem_deltaFR_left_6_higher = stats.sem(delta_FR_higher[:,0],nan_policy = 'omit')
# # sem_deltaFR_left_5_higher = stats.sem(delta_FR_higher[:,1],nan_policy = 'omit')
# # sem_deltaFR_left_4_higher = stats.sem(delta_FR_higher[:,2],nan_policy = 'omit')
# # sem_deltaFR_left_3_higher = stats.sem(delta_FR_higher[:,3],nan_policy = 'omit')
# # sem_deltaFR_left_2_higher = stats.sem(delta_FR_higher[:,4],nan_policy = 'omit')
# # sem_deltaFR_left_1_higher = stats.sem(delta_FR_higher[:,5],nan_policy = 'omit')
# # sem_deltaFR_right_1_higher = stats.sem(delta_FR_higher[:,6],nan_policy = 'omit')
# # sem_deltaFR_right_2_higher = stats.sem(delta_FR_higher[:,7],nan_policy = 'omit')
# # sem_deltaFR_right_3_higher = stats.sem(delta_FR_higher[:,8],nan_policy = 'omit')
# # sem_deltaFR_right_4_higher = stats.sem(delta_FR_higher[:,9],nan_policy = 'omit')
# # sem_deltaFR_right_5_higher = stats.sem(delta_FR_higher[:,10],nan_policy = 'omit')
# # sem_deltaFR_right_6_higher = stats.sem(delta_FR_higher[:,11],nan_policy = 'omit')
# # mean_deltaFR_left_6_lower = np.nanmean(delta_FR_lower[:,0])
# # mean_deltaFR_left_5_lower = np.nanmean(delta_FR_lower[:,1])
# # mean_deltaFR_left_4_lower = np.nanmean(delta_FR_lower[:,2])
# # mean_deltaFR_left_3_lower = np.nanmean(delta_FR_lower[:,3])
# # mean_deltaFR_left_2_lower = np.nanmean(delta_FR_lower[:,4])
# # mean_deltaFR_left_1_lower = np.nanmean(delta_FR_lower[:,5])
# # mean_deltaFR_right_1_lower = np.nanmean(delta_FR_lower[:,6])
# # mean_deltaFR_right_2_lower = np.nanmean(delta_FR_lower[:,7])
# # mean_deltaFR_right_3_lower = np.nanmean(delta_FR_lower[:,8])
# # mean_deltaFR_right_4_lower = np.nanmean(delta_FR_lower[:,9])
# # mean_deltaFR_right_5_lower = np.nanmean(delta_FR_lower[:,10])
# # mean_deltaFR_right_6_lower = np.nanmean(delta_FR_lower[:,11])
# # sem_deltaFR_left_6_lower = stats.sem(delta_FR_lower[:,0],nan_policy = 'omit')
# # sem_deltaFR_left_5_lower = stats.sem(delta_FR_lower[:,1],nan_policy = 'omit')
# # sem_deltaFR_left_4_lower = stats.sem(delta_FR_lower[:,2],nan_policy = 'omit')
# # sem_deltaFR_left_3_lower = stats.sem(delta_FR_lower[:,3],nan_policy = 'omit')
# # sem_deltaFR_left_2_lower = stats.sem(delta_FR_lower[:,4],nan_policy = 'omit')
# # sem_deltaFR_left_1_lower = stats.sem(delta_FR_lower[:,5],nan_policy = 'omit')
# # sem_deltaFR_right_1_lower = stats.sem(delta_FR_lower[:,6],nan_policy = 'omit')
# # sem_deltaFR_right_2_lower = stats.sem(delta_FR_lower[:,7],nan_policy = 'omit')
# # sem_deltaFR_right_3_lower = stats.sem(delta_FR_lower[:,8],nan_policy = 'omit')
# # sem_deltaFR_right_4_lower = stats.sem(delta_FR_lower[:,9],nan_policy = 'omit')
# # sem_deltaFR_right_5_lower = stats.sem(delta_FR_lower[:,10],nan_policy = 'omit')
# # sem_deltaFR_right_6_lower = stats.sem(delta_FR_lower[:,11],nan_policy = 'omit')

# # heights_higher_left = np.array([mean_deltaFR_left_6_higher,mean_deltaFR_left_5_higher,mean_deltaFR_left_4_higher,mean_deltaFR_left_3_higher,mean_deltaFR_left_2_higher,mean_deltaFR_left_1_higher])
# # heights_higher_right = np.array([mean_deltaFR_right_1_higher,mean_deltaFR_right_2_higher,mean_deltaFR_right_3_higher,mean_deltaFR_right_4_higher,mean_deltaFR_right_5_higher,mean_deltaFR_right_6_higher])
# # heights_lower_left = np.array([mean_deltaFR_left_6_lower,mean_deltaFR_left_5_lower,mean_deltaFR_left_4_lower,mean_deltaFR_left_3_lower,mean_deltaFR_left_2_lower,mean_deltaFR_left_1_lower])
# # heights_lower_right = np.array([mean_deltaFR_right_1_lower,mean_deltaFR_right_2_lower,mean_deltaFR_right_3_lower,mean_deltaFR_right_4_lower,mean_deltaFR_right_5_lower,mean_deltaFR_right_6_lower])
# # error_higher_left = np.array([sem_deltaFR_left_6_higher,sem_deltaFR_left_5_higher,sem_deltaFR_left_4_higher,sem_deltaFR_left_3_higher,sem_deltaFR_left_2_higher,sem_deltaFR_left_1_higher])
# # error_higher_right = np.array([sem_deltaFR_right_1_higher,sem_deltaFR_right_2_higher,sem_deltaFR_right_3_higher,sem_deltaFR_right_4_higher,sem_deltaFR_right_5_higher,sem_deltaFR_right_6_higher])
# # error_lower_left = np.array([sem_deltaFR_left_6_lower,sem_deltaFR_left_5_lower,sem_deltaFR_left_4_lower,sem_deltaFR_left_3_lower,sem_deltaFR_left_2_lower,sem_deltaFR_left_1_lower])
# # error_lower_right = np.array([sem_deltaFR_right_1_lower,sem_deltaFR_right_2_lower,sem_deltaFR_right_3_lower,sem_deltaFR_right_4_lower,sem_deltaFR_right_5_lower,sem_deltaFR_right_6_lower])
# # plt.bar(np.arange(0,6),heights_higher_left,color='steelblue',yerr=error_higher_left)
# # plt.bar(np.arange(6,12),heights_higher_right,color='red',yerr=error_higher_right)
# # plt.show()

# # plt.bar(np.arange(0,6),heights_lower_left,color='steelblue',yerr=error_lower_left)
# # plt.bar(np.arange(6,12),heights_lower_right,color='red',yerr=error_lower_right)
# # plt.show()

# # higher_vals = delta_FR_higher[:,5]
# # higher_vals = higher_vals[~np.isnan(higher_vals)]
# # num_higher = np.size(higher_vals)

# # lower_vals = delta_FR_lower[:,5]
# # lower_vals = lower_vals[~np.isnan(lower_vals)]
# # num_lower = np.size(lower_vals)