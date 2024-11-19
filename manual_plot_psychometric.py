from datetime import datetime  # Only for formatting title
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ibllib.io.raw_data_loaders import load_data
from one.api import ONE
import brainbox.behavior.pyschofit as psy
# from ibl_pipeline import behavior, acquisition, subject
# from ibl_pipeline.analyses.behavior import PsychResultsBlock, PsychResults
from scipy import stats

# from brainbox.io.spikeglx import Streamer

one = ONE(base_url='https://alyx.internationalbrainlab.org')
# one=ONE(mode='remote')
# one = ONE(mode='local')

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

# Wrangle the data into the correct form
def signed_contrast(trials):
    """Returns an array of signed contrasts in percent, where -ve values are on the left"""
    # Replace NaNs with zeros, stack and take the difference
    contrast = np.nan_to_num(np.c_[trials.contrastLeft, trials.contrastRight])
    return np.diff(contrast).flatten() * 100

use_trials_after_stim = 0
stim_rt_threshold = 60
stim_rt_min = 0

django_str = []
ins = one.alyx.rest('insertions', 'list', django=django_str)

eid = 'b9bd876e-76c1-4824-8087-a39ae72da73f'
trials = one.load_object(eid, 'trials')
# trials = one.load_object(eid, object="trials", namespace="ibl")
try:
    dset = '_iblrig_taskData.raw*'
    data_behav = one.load_dataset(eid, dataset=dset, collection='raw_behavior_data')
    ses_path = one.eid2path(eid)
    taskData = load_data(ses_path)
except:
    print('no raw task data found...')

trials_range = list(range(0, np.size(trials.probabilityLeft)))
# trials_range = list(range(0,69))+list(range(197,320))
# trials_range = list(range(102, 249)) + list(range(500, np.size(trials.probabilityLeft)))

# trials_range = list(range(90, 400))
# trials_range = list(range(637, np.size(trials.probabilityLeft)))

r = []
for tr in range(len(trials['contrastLeft'])):
    react = trials['feedback_times'][tr] - trials['goCue_times'][tr]
    if react > 59.9:
        continue
    r.append([react])
rt_mean = np.nanmean(r)
print('mean rt =', str(rt_mean))
print('numtrials =', str(len(trials['contrastLeft'])))

stim_trials = trials.copy()
nonstim_trials = trials.copy()
stim_trials_numbers = np.empty(len(trials['contrastLeft']))
stim_trials_numbers[:] = np.NaN
nonstim_trials_numbers = np.empty(len(trials['contrastLeft']))
nonstim_trials_numbers[:] = np.NaN
try:
    for k in trials_range:
        if taskData[k]['opto'] == 1:
            react = trials['feedback_times'][k] - trials['goCue_times'][k]
            if react < stim_rt_threshold:
                stim_trials_numbers[k] = k
        else:
            react = trials['feedback_times'][k] - trials['goCue_times'][k]
            if react < stim_rt_threshold:
                nonstim_trials_numbers[k] = k                
except:
    laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
    for k in trials_range:#range(0,len(trials.intervals)):
        if trials.intervals[k,0] in laser_intervals[:,0]:
            react = trials['feedback_times'][k] - trials['goCue_times'][k]
            if react < stim_rt_threshold:
                stim_trials_numbers[k] = k
        else:
            react = trials['feedback_times'][k] - trials['goCue_times'][k]
            if react < stim_rt_threshold:
                nonstim_trials_numbers[k] = k  
stim_trials_numbers = stim_trials_numbers[~np.isnan(stim_trials_numbers)]
nonstim_trials_numbers = nonstim_trials_numbers[~np.isnan(nonstim_trials_numbers)]
stim_trials_numbers = stim_trials_numbers.astype(int)
nonstim_trials_numbers = nonstim_trials_numbers.astype(int)

# stim_trials_numbers = stim_trials_numbers[stim_trials_numbers>89]

if use_trials_after_stim == 1:
    stim_trials_numbers = stim_trials_numbers +1
    if stim_trials_numbers[np.size(stim_trials_numbers)-1] == len(trials['contrastLeft']):
        stim_trials_numbers = stim_trials_numbers[range(len(stim_trials_numbers)-1)]
# stim_trials_numbers[np.size(stim_trials_numbers)-1] = stim_trials_numbers[np.size(stim_trials_numbers)-1] - 1

# nonstim_trials_numbers = nonstim_trials_numbers[nonstim_trials_numbers>89]

stim_trials.contrastRight = trials.contrastRight[stim_trials_numbers]
stim_trials.contrastLeft = trials.contrastLeft[stim_trials_numbers]
stim_trials.goCueTrigger_times = trials.goCueTrigger_times[stim_trials_numbers]
stim_trials.feedback_times = trials.feedback_times[stim_trials_numbers]
stim_trials.response_times = trials.response_times[stim_trials_numbers]
stim_trials.feedbackType = trials.feedbackType[stim_trials_numbers]
stim_trials.goCue_times = trials.goCue_times[stim_trials_numbers]
stim_trials.firstMovement_times = trials.firstMovement_times[stim_trials_numbers]
# stim_trials.stimOnTrigger_times = trials.stimOnTrigger_times[stim_trials_numbers]
stim_trials.probabilityLeft = trials.probabilityLeft[stim_trials_numbers]
stim_trials.stimOn_times = trials.stimOn_times[stim_trials_numbers]
stim_trials.choice = trials.choice[stim_trials_numbers]
stim_trials.rewardVolume = trials.rewardVolume[stim_trials_numbers]
# stim_trials.included = trials.included[stim_trials_numbers]
stim_trials.intervals = trials.intervals[stim_trials_numbers]

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

stim_trials_contrast = signed_contrast(stim_trials)
nonstim_trials_contrast = signed_contrast(nonstim_trials)

left_block_trials = np.where(trials.probabilityLeft == 0.8)
right_block_trials = np.where(trials.probabilityLeft == 0.2)

rnonstim = []
for tr in range(len(nonstim_trials['contrastLeft'])):
    react = nonstim_trials['feedback_times'][tr] - nonstim_trials['goCue_times'][tr]
    if react > 59.9:
        continue
    rnonstim.append([react])
rt_mean_nonstim = np.nanmean(rnonstim)
print('mean rt nonstim =', str(rt_mean_nonstim))
print('numtrials =', str(len(nonstim_trials['contrastLeft'])))
rstim = []
for tr in range(len(stim_trials['contrastLeft'])):
    react = stim_trials['feedback_times'][tr] - stim_trials['goCue_times'][tr]
    if react > 59.9:
        continue
    rstim.append([react])
rt_mean_stim = np.nanmean(rstim)
print('mean rt stim =', str(rt_mean_stim))
print('numtrials =', str(len(stim_trials['contrastLeft'])))

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
if np.size(np.unique(nonstim_trials.probabilityLeft)) > 2:
    colours = dict(zip(nonstim_trials_data.keys(), ('r', 'k', 'b')))
else:
    colours = dict(zip(nonstim_trials_data.keys(), ('xkcd:tangerine', 'xkcd:violet', 'xkcd:violet')))

trials_contrast = signed_contrast(trials)

# data: a dict whose keys are the block type and values a
# 3 x n matrix where first row corrsponds to stim levels (%), 
# the second to number of trials for each stim level (int),
# the third to proportion rightward (float between 0 and 1)
trials_data = {}
for pL in np.unique(trials.probabilityLeft):
    in_block = trials.probabilityLeft == pL
    xx, nn = np.unique(trials_contrast[in_block], return_counts=True)
    rightward = trials.choice == -1
    pp = np.vectorize(lambda x: np.mean(rightward[(x == trials_contrast) & in_block]))(xx)
    trials_data[pL] = np.vstack((xx, nn, pp))

# Increase bias bounds (kwargs defined in previous section)
kwargs = {
    # parmin: The minimum allowable parameter values, in the form
    # [bias, threshold, lapse_low, lapse_high]
    'parmin': np.array([-50., 10., 0., 0.]),
    # parmax: The maximum allowable parameter values
    'parmax': np.array([50, 100., 1, 1]),
    # Non-zero starting parameters, used to try to avoid local minima
    'parstart': np.array([0., 40., .1, .1]),
    # nfits: The number of fits to run
    'nfits': 50
}

#plotting
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
    ax2.plot(x, psy.erf_psycho_2gammas(pars, x), label=f'{int(pL*100)}', color=colours[pL])#, linestyle='dashed')

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
sns.despine(offset=10, trim=True)

# Get some details for the title
# det = one.get_details(eid)
# ref = f"{datetime.fromisoformat(det['start_time']).date()}_{det['number']:d}_{det['subject']}"

# f.suptitle(ref)
ax1.legend()
ax2.legend()
# ax1.set_ylim([-0.05,1.05])
f.set_size_inches(8, 4, forward=True)
f.show()

# # stats.ttest_ind(rnonstim,rstim,equal_var=False)
# rtfig = plt.figure(figsize=[3.5,4.5])
# plt.bar([0,1],[rt_mean_nonstim,rt_mean_stim], color=['k','b'])
# plt.errorbar(0,rt_mean_nonstim,yerr=stats.sem(rnonstim,nan_policy='omit'),color='r')
# plt.errorbar(1,rt_mean_stim,yerr=stats.sem(rstim,nan_policy='omit'),color='r')
# plt.show()

# abs_react_stim = np.empty([np.size(stim_trials_numbers)])
# abs_react_stim[:] = np.NaN
# for i in np.arange(0,np.size(stim_trials_numbers)):
#     trial_num = stim_trials_numbers[i]
#     # trial_start_time_stim = taskData[trial_num]['behavior_data']['Trial start timestamp']
#     # abs_react_stim[i] = trials.feedback_times[trial_num] - trial_start_time_stim
#     relative_trial_start = taskData[trial_num]['behavior_data']['States timestamps']['trial_start'][0][0]
#     if np.isnan(taskData[trial_num]['behavior_data']['States timestamps']['error'][0][0]) == 1:
#         abs_react_stim[i] = taskData[trial_num]['behavior_data']['States timestamps']['reward'][0][0] - relative_trial_start
#     else:
#         abs_react_stim[i] = taskData[trial_num]['behavior_data']['States timestamps']['error'][0][0] - relative_trial_start

# abs_react_nonstim = np.empty([np.size(nonstim_trials_numbers)])
# abs_react_nonstim[:] = np.NaN
# for i in np.arange(0,np.size(nonstim_trials_numbers)):
#     trial_num = nonstim_trials_numbers[i]
#     # trial_start_time_nonstim = taskData[trial_num]['behavior_data']['Trial start timestamp']
#     # abs_react_nonstim[i] = trials.feedback_times[trial_num] - trial_start_time_nonstim
#     relative_trial_start = taskData[trial_num]['behavior_data']['States timestamps']['trial_start'][0][0]
#     if np.isnan(taskData[trial_num]['behavior_data']['States timestamps']['error'][0][0]) == 1:
#         abs_react_nonstim[i] = taskData[trial_num]['behavior_data']['States timestamps']['reward'][0][0] - relative_trial_start
#     else:
#         abs_react_nonstim[i] = taskData[trial_num]['behavior_data']['States timestamps']['error'][0][0] - relative_trial_start

# rtfig = plt.figure(figsize=[2.5,4.5])
# plt.bar([3,4],[np.nanmean(abs_react_nonstim),np.nanmean(abs_react_stim)], color=['k','b'])
# plt.errorbar(3,np.nanmean(abs_react_nonstim),yerr=stats.sem(abs_react_nonstim,nan_policy='omit'),color='r')
# plt.errorbar(4,np.nanmean(abs_react_stim),yerr=stats.sem(abs_react_stim,nan_policy='omit'),color='r')
# # plt.plot(np.ones(np.size(abs_react_nonstim))*3,abs_react_nonstim,'rx')
# # plt.plot(np.ones(np.size(abs_react_stim))*4,abs_react_stim,'rx')
# # plt.ylim(0,9)
# plt.show()


reaction_times = np.empty([np.size(trials['contrastLeft'])])
reaction_times[:] = np.NaN
quiescent_period_times = np.empty([np.size(trials['contrastLeft'])])
quiescent_period_times[:] = np.NaN
for tr in range(len(trials['contrastLeft'])):
    stimOn_time = trials['stimOn_times'][tr]
    if np.isnan(stimOn_time) == 1:
        # stimOn_time = trials['goCue_times'][tr]
        stimOn_time = trials['goCueTrigger_times'][tr]
    react = trials['feedback_times'][tr] - stimOn_time
    if react > 59.9:
        continue
    # trial_start_time = taskData[tr]['behavior_data']['States timestamps']['trial_start'][0][0]
    trial_start_time = trials['intervals'][tr,0]
    # stimOn_time = taskData[tr]['behavior_data']['States timestamps']['stim_on'][0][0]
    qp = stimOn_time - trial_start_time
    reaction_times[tr] = react
    quiescent_period_times[tr] = qp

rt_stimtrials = reaction_times[stim_trials_numbers]
qp_stimtrials = quiescent_period_times[stim_trials_numbers]
rt_nonstimtrials = reaction_times[nonstim_trials_numbers]
qp_nonstimtrials = quiescent_period_times[nonstim_trials_numbers]

rtfig = plt.figure(figsize=[4.5,4.5])
plt.bar([6,7],[np.nanmean(rt_nonstimtrials),np.nanmean(rt_stimtrials)], color=['k','b'])
plt.errorbar(6,np.nanmean(rt_nonstimtrials),yerr=stats.sem(rt_nonstimtrials,nan_policy='omit'),color='r')
plt.errorbar(7,np.nanmean(rt_stimtrials),yerr=stats.sem(rt_stimtrials,nan_policy='omit'),color='r')
plt.bar([3,4],[np.nanmean(qp_nonstimtrials),np.nanmean(qp_stimtrials)], color=['k','b'])
plt.errorbar(3,np.nanmean(qp_nonstimtrials),yerr=stats.sem(qp_nonstimtrials,nan_policy='omit'),color='r')
plt.errorbar(4,np.nanmean(qp_stimtrials),yerr=stats.sem(qp_stimtrials,nan_policy='omit'),color='r')
plt.show()


###RT_michael

# evts = ['goCue_times', 'feedback_times', 'probabilityLeft',
#         'choice', 'feedbackType']   
# columns = ['contrast','choice','reaction time','pleft','trial number']

# r = []
# for tr in range(len(nonstim_trials['contrastLeft'])):
#     cont = nonstim_trials_contrast[tr]
#     # # skip trial if any key info is nan 
#     # if any(np.isnan([trials[k][tr] for k in evts])):
#     #     continue
#     react = nonstim_trials['feedback_times'][tr] - nonstim_trials['goCue_times'][tr]
#     if react > 59.9:
#         continue
#     pleft = nonstim_trials['probabilityLeft'][tr]
#     # # skip non-block trials   
#     if pleft == 0.5:
#         continue   
#     r.append([cont,nonstim_trials['choice'][tr],react,pleft,tr])
# r_stim = []
# for tr in range(len(stim_trials['contrastLeft'])):
#     cont_stim = stim_trials_contrast[tr]
#     react_stim = stim_trials['feedback_times'][tr] - stim_trials['goCue_times'][tr]
#     if react_stim > 59.9:
#         continue
#     pleft_stim = stim_trials['probabilityLeft'][tr]
#     # # skip non-block trials   
#     if pleft_stim == 0.5:
#         continue   
#     r_stim.append([cont_stim,stim_trials['choice'][tr],react_stim,pleft_stim,tr])

# df  = pd.DataFrame(data=r,columns=columns)  
# df_stim  = pd.DataFrame(data=r_stim,columns=columns)
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12,6))
# palette = ['r','b']
# sns.lineplot(ax=ax1, x="contrast", y="reaction time", hue="pleft",
#             data=df, palette=palette)
# handles, labels = ax1.get_legend_handles_labels()
# # ax1.legend(handles[:2], labels[:2],
# # columnspacing=1,
# # loc="best", ncol=1, frameon=True).set_draggable(1)   
# sns.lineplot(ax=ax2, x="contrast", y="reaction time", hue="pleft",
#             data=df_stim, palette=palette)
# handles, labels = ax2.get_legend_handles_labels()
# # ax2.legend(handles[:2], labels[:2],
# # columnspacing=1,
# # loc="best", ncol=1, frameon=True).set_draggable(1)        
# f.suptitle(f'reaction times per contrast and block \n'
#             f'{eid}')
# ax1.set_ylim(bottom=0, top=15)
# # ax1.ylabel('reaction time [sec]')
# # ax1.tight_layout()   
# plt.show()

###4/21 = session 4 mouse 40

###################################################################################################
###################################################################################################
########################## NOTES
   #SWC_NM_002
# #6/11 6bdb50c2-6250-4b44-bdaf-2d34d975a913
# eid = '6bdb50c2-6250-4b44-bdaf-2d34d975a913'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()
# arr1 = np.arange(100,130)
# arr2 = np.arange(173,226)
# arr3 = np.arange(268,315)
# arr4 = np.arange(344,379)
# arr5 = np.arange(407,448)
# arr1x = np.arange(90,100)
# arr2x = np.arange(130,173)
# arr3x = np.arange(226,268)
# arr4x = np.arange(315,344)
# arr5x = np.arange(379,407)
# stim_trials_numbers = np.concatenate((arr1,arr2,arr3,arr4,arr5),axis=0)
# nonstim_trials_numbers = np.concatenate((arr1x,arr2x,arr3x,arr4x,arr5x),axis=0)

#6/14 6f1b2bc1-3b6d-4a2f-92b3-44fc6572a4c3
# eid = '6f1b2bc1-3b6d-4a2f-92b3-44fc6572a4c3'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()
# arr1 = np.arange(136,178)
# arr2 = np.arange(218,239)
# arr3 = np.arange(275,317)
# arr4 = np.arange(354,401)
# arr5 = np.arange(440,460)
# arr1x = np.arange(90,136)
# arr2x = np.arange(178,218)
# arr3x = np.arange(239,274)
# arr4x = np.arange(317,353)
# arr5x = np.arange(401,439)
# stim_trials_numbers = np.concatenate((arr1,arr2,arr3,arr4,arr5),axis=0)
# nonstim_trials_numbers = np.concatenate((arr1x,arr2x,arr3x,arr4x,arr5x),axis=0)

# #6/15 6bdb50c2-6250-4b44-bdaf-2d34d975a913
# eid = 'f3052a94-110a-4c5b-a2c7-e4f03c1f508f'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()
# arr1 = np.arange(145,205)
# arr2 = np.arange(271,314)
# arr3 = np.arange(350,400)
# arr4 = np.arange(465,520)
# arr5 = np.arange(573,630)
# arr1x = np.arange(205,271)
# arr2x = np.arange(314,350)
# arr3x = np.arange(400,465)
# arr4x = np.arange(520,573)
# arr5x = np.arange(630,698)
# stim_trials_numbers = np.concatenate((arr1,arr2,arr3,arr4,arr5),axis=0)
# nonstim_trials_numbers = np.concatenate((arr1x,arr2x,arr3x,arr4x,arr5x),axis=0)

# #6/16 c13f1308-6a57-4d9a-8802-85318188635e
# eid = 'c13f1308-6a57-4d9a-8802-85318188635e'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()
# arr1 = np.arange(109,160)
# arr2 = np.arange(210,291)
# arr3 = np.arange(366,446)
# arr4 = np.arange(532,594)
# arr5 = np.arange(573,630)
# arr6 = np.arange(638,668)
# arr7 = np.arange(711,745)
# arr1x = np.arange(90,109)
# arr2x = np.arange(160,210)
# arr3x = np.arange(291,366)
# arr4x = np.arange(446,532)
# arr5x = np.arange(594,638)
# arr6x = np.arange(668,711)
# arr7x = np.arange(745,750)
# stim_trials_numbers = np.concatenate((arr1,arr2,arr3,arr4,arr5),axis=0)
# nonstim_trials_numbers = np.concatenate((arr1x,arr2x,arr3x,arr4x,arr5x),axis=0)

# #6/17
# eid = 'd9157642-64d0-48b7-9349-dab21e7f6542'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()

#SWC_NM_001
# #6/25 'c6eedfe3-4cd3-4212-b059-43a894ee329b'
# eid = 'c6eedfe3-4cd3-4212-b059-43a894ee329b'
# trials = one.load_object(eid, 'trials')
# stim_trials = trials.copy()
# nonstim_trials = trials.copy()
# arr1 = np.arange(133,197)
# arr2 = np.arange(253,300)
# arr3 = np.arange(359,437)
# arr4 = np.arange(505,536)
# arr1x = np.arange(90,133)
# arr2x = np.arange(197,253)
# arr3x = np.arange(300,359)
# arr4x = np.arange(437,505)
# arr5x = np.arange(536,573)
# stim_trials_numbers = np.concatenate((arr1,arr2,arr3,arr4),axis=0)
# nonstim_trials_numbers = np.concatenate((arr1x,arr2x,arr3x,arr4x,arr5x),axis=0)
# '65bf2d52-dda7-4b8c-b7d0-cd2d681cf3e3' 6/8 (pre surgery)
# '36617baf-42cf-4fc6-b81d-5059b1bab2b5' 6/21 (ephysCW)
# 'e9f10546-cebb-46ed-866d-cf6e12f19b7d' 6/22
# '109c0f7a-c1d5-4517-bf00-b3bf59ede1ab' 6/23
# '82c11f0a-fc57-411e-ab97-468eff4a9bf8' 6/24
# 'a8de4394-b814-4175-b3cb-c0107cc0a829' 6/28
# '5bbacd35-6871-4d1e-98a7-50b949fc4293' 6/29
# '53f5154c-2f31-4f1a-b4c8-5464b1a046ea' 6/30
# 'd64bd8b7-d289-47be-8c14-6d6ec173411d' 7/01 ephys session

#SWC_NM_009
# '39bd4541-4ea8-4b68-bda9-786a2a52b148' 6/08 behavior rig not unpacking probs properly?
# '2dd3b9db-6a82-4c37-8d8d-bcabdd817785' 6/09 ephys no stim
# '985f0bd7-01db-4461-9b49-24e6dda73585' 6/10 ephys no stim
# '82c0bef1-250c-48b0-be1d-7d543af6b923' 6/11 ephys no stim
#  surgery/recovery
# '6caf51e0-b621-443d-9419-d1aedff5fea1' 6/21 #no stim?
# '823b044f-c509-4370-aadc-c7ecdc15e91d' 6/22 #no stim?
# '93e92e0c-7863-47d6-bbdc-45c61492e6eb' 6/23 #no stim?
# '60614160-a409-407f-b9c3-482c432db066' 6/24
# '63035897-2e0f-4b17-b426-f21698ad44bc' 6/25
# 'd1e121a9-72fa-4d14-b9a1-6a0550c8c143' 6/28
# 'b8b78f04-b618-4168-9808-1e65a4d93606' 6/29
# 'f8ba55d7-6791-4d0f-9abd-cc7b16963cbd' 6/30
# '3eae85d1-56cf-4d92-b2fe-ba0a9a2d4a10' 7/01
# '09500c76-e696-47b3-b993-9426dd4cec0a' 7/02
# 'ca2d68cd-49c8-4f52-806d-9fdd393ce132' 7/05 #1
# 'dc70d8ce-65d4-4702-82fc-5ae5b7ba4d5a' 7/05 #2
# 'b70bf49a-4fff-4f27-8f3a-9689f30daf25' 7/06

#SWC_NM_008
# 'b8c56e2e-dccf-404e-b80c-7bed34c1cbe9' 8/26 pre-surgery
# 'b08d5ae6-0413-4fda-981e-5146b228c3fe' 8/27 pre-surgery
# '20a36270-9657-4cdd-b070-e0dc9b6dc287' 9/6 no stim
# '4808dc5d-2a36-4b44-9580-9e0f8b46b77d' 9/7 no stim
# '5a6457b5-95bb-4026-b825-c38d8adc49e4' 9/8 right stim
# '8a09bb30-a040-41b4-bfe0-492a0cc921e7' 9/9 Left stim
# '2bbae950-9555-43d0-9891-03e47f18b286' 9/10 bilateral
# 'ed27c5bf-7b72-40de-9167-a74eac48a4c8' 9/13 right
# '124cddb8-22d2-4632-be4d-92181901a65e' 9/14 bilateral 2s
# '214fa6cd-9e3e-492b-b330-931223e157ea' 9/15 mock ephys - bilateral 1s at STIM ON
# '167d31ff-6c02-4387-9371-206caf013255' 9/16 left unilateral 1.4sQ
# '5c78ef8b-50d5-4e34-9e05-1ac6964aa551' 9/17 right unilateral 1.4sQ
# 'e0cfaf74-d841-4188-951e-757d417d610f' 9/20
# '15599a78-1df4-4b11-b825-0cf57e878a38' 9/21
# '774edebf-82ed-4780-9657-32ebf67350cf' 9/22
# '32f965f9-b903-4ac5-ba84-b5bc52b40b7c' 9/22 2
# '264f3743-0965-4885-a40e-3ac9ee7a9c85' 9/22 3
# '7e704fd4-cefd-4314-bd5a-e79212c94836' 9/23
# '1cceaf57-cd56-410e-bddb-634ee9840c50' 9/24 #poor baseline accuracy
# 'bb8d5380-69be-40e2-b26b-918f5f48dd5d' 9/27
# 'fb1c5429-6329-4370-8e68-b9f864cb2319' 9/28
# '96aaa6e1-1b1d-46e9-b8a0-47de29d195a7' 9/29
# '238a0a48-392e-4d18-836a-eb5fe0853bfe' 9/30
# '318bffb7-9bca-4145-affe-b52588a5dc1c' 10/1
# '448d7b48-af08-47e0-bace-3167ba4ba9cc' 10/4
# 'be7b5af4-be82-4be4-903d-678c59d8d365' 10/5
# '52f21cc6-6b1c-4fdc-b26e-c04bd4a4ce99' 10/6
# '8e71c2f4-f931-4b1b-8f45-1ccb8b2460e8' 10/7
# 'cd5a5088-bf3b-45a5-846b-95e5399c7fca' 10/8
# '9dd5b158-340e-48f7-b93c-217caa07399b' 10/11
# '6e104af9-7c6b-49a0-98ac-bf09489851d3' 10/12
# 'bef61842-6ed9-474f-96ac-6dbdba09fb47' 10/13
# 'f0bda80c-a195-4f34-9fb5-7c61d4a5d797' 10/14
# '0f02a3bd-22fc-43af-b043-f12b6fdc16a1' 10/15
# '18208ce8-fecd-456b-8d28-551742ec90d5' 10/18
# '67a3d9a8-5ec5-4ed6-9473-f3c16f62d087' 10/19
# '115d98e8-1356-472c-821a-48ad855f0bfc' 10/20
# '0ca6883a-e4a2-418c-b924-79c640b961c9' 10/21 alf object not found
# '409dc01a-c5dc-40cb-8356-e19372e4f546' 10/22
# '2ffa0c58-b277-4d5b-9435-4c73e492baa5' 10/25


#SWC_NM_003
# '959de94a-3e17-404e-9276-0a2c43913291' 9/8
# '8f15cde1-9700-42b2-856e-6d661281b937' 9/9
# '3c237dae-523e-4390-b0d6-5c92cf4d8c0a' 9/10
# 'de01493e-0806-47db-b7a3-8b1d5d7fc4d1' 9/20
# '99939cb9-db76-4b67-968d-83d626eb1669' 9/21
# '9fd356f1-f492-48e9-bb69-43bd0981716f' 9/22
# 'f7cb4811-27b8-4953-a6a1-e8794531c6bd' 9/23
# 'a7222f4a-93aa-42f8-ab93-df0b7868bc25' 9/24
# 'ba7bbd72-c41a-4dbd-9992-4a51489f4289' 9/27
# '87d94eeb-3754-414a-9dba-453f84b0f5fe' 9/28
# '3e3535fb-b06f-4e57-9460-cbe071984171' 9/29
# 'c62ec7e6-96f4-43be-ac68-76773c7f584c' 9/30
# '108c0bf2-1f83-466b-b5d0-e1c449d5f7d7' 10/1
# '3f704200-a246-4276-ae7f-c47c33e29f63' 10/4
# '3cf488ae-c327-4e58-b6f6-7b7d81721628' 10/5
# 'bb3a4433-65db-4640-8690-5bbc81ef8d49' 10/6
# '6f317227-4dab-4dbf-8f1c-9aa1e66d909e' 10/7
# '205e8076-40b3-4432-8044-0dd890839db7' 10/8
# '05edb069-980d-42de-b9fa-178ef0648a21' 10/11
# 'd9dab492-0243-4135-b6aa-09ddc92e2d77' 10/12
# '6f7e2e29-68d1-4c8c-a7a5-4ec0baad08eb' 10/13
# '8b0545fa-3a21-43b2-bfcb-7cfed09961cb' 10/14
# '411d5f71-4f16-4ca5-ae20-a9789a4b49a6' 10/15
# '26ee634d-17a9-4e6d-91e1-08f2e4445eea' 10/18
# '31c864d3-d12c-41c3-b45a-6098e07e8b64' 10/19
# '4b386978-0b46-4fd0-9597-3cb4b71a8661' 10/20
# '335a0eda-f61d-45d2-b1df-1aea44c5abcb' 10/21
# '2b920090-8256-4a13-9923-a4b57952faa7' 10/22
# '98185253-b92d-4d8e-b3f7-9ad4820e96fe' 10/25
# 'c9f6d00a-b6ca-4d83-a1fd-6082453445ee' 10/26
# 'ecf7293d-d97f-4a61-81f8-a8e11c8ef557' 10/27
# '51a67fc5-0930-43d9-8458-5ec54578b773' 10/28
# 'fb0da005-9938-4ba0-b476-7880decfb656' 10/29
# 'c31d23ef-0a95-49b0-8969-708d6c91e1d3' 11/1
# '45f54c9c-9c7b-4cbc-9ef3-cf7f5e7ec65d' 11/2 'opto' error?

#SWC_NM_004
# 'cd74e125-09cf-4a03-89c2-bf0bfe60c4b5' 10/11 no stim
# '8ec84dc5-6b33-4281-a18f-811d3f68bef9' 10/13 no stim
# 'a0117225-6f06-4588-9ee8-39965822d7c6' 10/15
# 'f162137e-73b7-4b5c-bd76-e2846276d2ac' 10/18
# 'edcaf465-4d4e-4d0d-86a0-aec5733ccd13' 10/19
# 'b1dd1c50-6fbe-4f9b-8267-0b48a819c78e' 10/20
# 'c90780f1-9304-4bcf-b74b-6ec9cae581ad' 10/21
# '8c2163f0-41c3-4c2c-8293-b6523790bfb4' 10/22
# '35cd3f60-267d-42b4-8606-a3eb2d763bab' 10/25
# 'e098791a-305b-4338-9f3f-562a89948603' 10/26
# '034bf182-47bb-4866-8340-1e910bdc79c6' 10/27
# '81ac7ba7-fca8-4a31-80b8-095546e888b4' 10/28
# '2b9d920c-a09f-4237-82c0-773b17df06e3' 10/29
# 'a8f4b965-89b6-4905-b953-3f6f7c42bbb7' 11/1
# 'ae981ae0-748d-4edc-9a6f-98ea1b417c34' 11/2 very poor BL performance
# 'dd1815ba-b321-4469-a55d-dcb9987f6b30' 11/3 alf object not found
# 'aa460490-fc4b-4c7b-b7bb-3fbe3f61f0f2' 11/4
# 'c8de3e60-9d97-4c63-89f7-e99935eabbdc' 11/5
# 'c9edd28f-ed33-43fb-812f-9e57c30ad689' 11/8
# '9264704f-85f4-46b9-a269-e09cdba76e02' 11/9
# '23520eca-b5b1-45fb-a629-3ebf3a620c2f' 11/10
# 'f483a2d6-0dd3-42cf-988b-aaf99824abd5' 11/11 (002)
# 'd20889b9-2e2e-43a4-9917-2114b7f05c83' 11/12
# '88726cf3-2821-4075-8bfa-bdfcf1c6bfd8' 11/15
# 'f78cbd4c-4a96-4da4-b2fd-b8d140150841' 11/16
# 'ec4b0489-55bd-47e1-b376-b9d6e45f41d9' 11/17

#SWC_NM_011
# 'fefde89c-53d2-4ed0-b5d6-7c2f05b55767' 11/2
# 'db75a41b-d0d1-4c55-9c94-98c253ffdef2' 11/3 Alf object not found
# 'd71ec5e3-f257-47e2-8690-f943d13e0c13' 11/4
# '9e4b80e4-ae85-4e5e-8e1d-519eb68347be' 11/5
# '3debc803-cabb-444a-ad4b-62b52f34dc1f' 11/8
# '3abd3941-4f14-482b-a9af-d9ee0e4bc69d' 11/9
# '269798e4-4837-42f0-80a8-12feafb5325e' 11/10
# 'f0780250-d261-4337-b736-303658a7848a' 11/12
# '847cdd72-0859-4bb4-9bba-c3b11045d7c8' 11/16
# '16bb91ac-5701-48c4-8098-1861660d8ccb' 11/17
# '7dd4db33-7c27-4491-b0b5-3b5af9f526dd' 11/18
# '997bed88-f960-4d40-9e3b-872727784e3c' 11/19
# '60e0089d-d755-4e32-8a2b-f5dbd6b3a520' 11/22
# 'fddf4805-46fe-482c-ae12-b0a717f0d6a8' 11/23
# '02af576e-0aa1-4784-b631-adbc3792f4d5' 11/24 (mixed stim)
    #50hz= list(range(0,229))+list(range(349,409))+list(range(576,647))
    #continuous= list(range(229,349))+list(range(409,576))+list(range(647,len(trials['contrastLeft'])))
# '7373f901-2f6e-48f4-981c-30192a9299de' 11/25 (mixed stim)
    #50hz= list(range(0,114))+list(range(390,527))
    #continuous= list(range(114,390))+list(range(532,len(trials['contrastLeft'])))
# '28d3ceed-1edb-4ac6-b7c8-e3647ad36370' 11/26
# '6d928f37-783f-4e06-b0a5-2803f6fd61f4' 11/29 #definitely an effect here, though few trials
# '7edc27c7-38b1-41bd-81f2-dbaef62f1c09' 11/30

#SWC_NM_010
# '11a8532c-5718-43a9-8bac-b6f6e0fb4cba' 2/2
# '8e6c8994-6a12-4e2c-b066-958b9f84ab67' 2/3
# '2906167a-d362-4ef8-8555-5c9f8b322e27' 2/4 NO LASER
# '7ade859f-02cb-4b8f-bb9d-957b26ece7be' 2/7
# '330ebac8-a94e-4a0c-a50a-c571fb162b02' 2/15
# '5e37ce85-aa69-4651-b8a0-03101faf4d33' 2/16
# 'b2da6e36-e25c-4b2a-9937-2ab30003ac48' 2/17
# '8b4f0ea4-9185-44eb-a27e-40238563bef7' 2/18
# '2aa240a4-0d31-4271-845d-c33e951e9118' 2/21
# '0a6400bf-3f90-4be2-9b63-19d9f659cf16' 2/22

#SWC_NM_012
# '1f19e366-46b0-46ea-a137-1bf58a3d83c5' 2/2
# 'a4501dd7-8613-4cdf-99ef-ca56971557c5' 2/3
# '2aed2d49-fced-4465-b3bb-58b225079748' 2/4
# '95acdc6e-8959-4d9a-b039-9c28a9f06ee0' 2/7
# 'ccf42b1c-8ed4-4265-afe6-2afb25d10d08' 2/8
# 'ef962323-9464-483f-992c-6a3de096a963' 2/9
# '04260f14-4329-4d71-9061-092cc441e2d7' 2/10
# '03bd9265-4e9e-4c96-8e57-4cc3827aa0d8' 2/11
# '15f0c551-0bc2-4423-ab09-90e03dd240c5' 2/15
# '288b4537-a539-49f3-a56c-c67c80b3704c' 2/16
# '89077217-bd62-499d-9914-e0d591ccedb5' 2/17
# '186f7c0a-81ca-488a-92c0-14d41263edbe' 2/18
# '6c01b126-12cf-4739-8aa3-120bc62e2aee' 2/21
# 'ff54300e-0061-4ab3-9bee-b56a54d71376' 2/22
# 'a418eb79-b949-4fdf-9fad-b5d8b240e638' 2/23
# '2a2efcbf-0269-477b-97f2-89f8ef04decf' 2/24
# '1ca51d6a-80a3-4186-b5b8-b4c3aefdf4ed' 2/25
# '97feaab1-1581-4691-9287-9bf202adeba2' 2/28
# '10758de5-b5ac-4686-9d5c-6b6864f4207e' 3/01
# 'd6f01308-a7c9-455b-855f-6f9ab7a4afbc' 3/02
# '85374e1c-48fd-4d8d-9ca3-a6779394a08f' 3/03
# 'a3e77b0f-7450-4411-bbe0-2b0c1a68baf6' 3/04

#SWC_NM_018
# '3d965f9d-e89d-402f-ae15-c985b1149967' 28/3 #trials_range = list(range(155,len(trials['contrastLeft'])))
# '9428f5fc-a6b9-4689-8200-b0a846933a1d' 29/3 #trials_range = list(range(184,len(trials['contrastLeft'])))
# 'e059b876-c4ef-4a6b-aa1e-6ffc496ed9fc' 30/3
# 'e418cf94-e626-4a1e-9796-e9dcb35a5ad1' 31/3
# '028cca41-d6cf-4487-b0d1-817a3c2ee94f' 1/4
# 'fbbc896c-9f3f-45f6-9d59-5e8e4b728b6b' 4/4 ##issue w/ BNC1 trial start pulses
# 'c2f07cee-682d-4a79-9fa2-8d13d533d16e' 5/4 ##issue w/ BNC1 trial start pulses
# 'b4dd0cff-3aed-4b74-973a-0a015cc2ad11' 6/4 #no video
# '8c070089-7fb4-4bd9-b88e-c99b498f7acf' 7/4
# 'dd64e7e8-eee5-4a68-9799-b776527e3137' 12/4 #trials_range = list(range(100,len(trials['contrastLeft'])))
# '8f022ca3-cd43-41ba-bfa4-66d23e46f66f' 13/4
# '3ed212c8-3bec-425a-8596-a1f7a734c9e7' 14/4
# '866547c2-c965-4278-aedf-0df750e29a7b' 3/5 #R# trials_range = list(range(123,302)) + list(range(614,len(trials['contrastLeft']))) #L# list(range(302,614))
# '6daaa3c9-67c1-497a-932a-e4c521c8cf3d' 4/5 #trials_range = list(range(108,len(trials['contrastLeft'])))
# 'd1a66312-dad9-4951-8a9c-7497c3aaf69f' 5/5 trials_range = list(range(157,len(trials['contrastLeft'])))
# '9f38b8a5-e37e-4c9a-b960-f9849cfefcce' 1/6 no stim

#SWC_NM_016
# '069c4dfa-7ce7-4fca-89a6-f5253ff806f4' 6/4 ## no opto stim
# '0ff9161b-bae8-4ff1-a080-2928fc45cc54' 7/4  #trials_range = list(range(0,342))
# 'efeef8a4-af69-44ef-9cfa-44c91ab67926' 8/4 #trials_range = list(range(197,len(trials['contrastLeft'])))
# '9934246e-0e5a-4fe9-90dc-bf179c84482f' 11/4 #trials_range = list(range(122,len(trials['contrastLeft'])))
# 'ca97595c-1ae9-4bf5-8703-4368abe28c9e' 12/4 #trials_range = list(range(119,len(trials['contrastLeft'])))
# 'cc14dbaf-300b-4df5-8fba-edb4b4b06cf8' 13/4 #trials_range = list(range(100,len(trials['contrastLeft']))) #dafuq?
# '1f05c49c-1b40-418b-ab59-89232916710a' 14/4 #trials_range = list(range(204,len(trials['contrastLeft'])))
# '1d09b08b-8883-4d84-aed0-0e53e91995ea' 15/4 #trials_range = list(range(159,len(trials['contrastLeft'])))
# '9cc77c22-08f2-49cd-b37d-905397fab334' 22/4 #trials_range = list(range(90,len(trials['contrastLeft'])))
# '32cf6ee5-2397-4482-a1f6-bb01745a4b4b' 28/4 #trials_range = list(range(90,len(trials['contrastLeft'])))
# '47b01ca2-9cf2-41f5-9e46-c0bf1b8d7a65' 29/4 #trials_range = list(range(123,len(trials['contrastLeft'])))
# '231a2c63-c614-449e-b265-b6b99cfb6df6' 2/5  #trials_range = list(range(90,len(trials['contrastLeft'])))

#SWC_NM_019
# '5005244f-863e-4538-954d-22b7e56f7cb5' 21/6
# '9f55a07d-7cb6-4662-a4c4-e044e4bf22ba' 22/6
# '7b2bbb52-4dfe-49d5-8796-5b4059216345' 23/6
# '2141e89a-7e01-4afd-8399-204bd1d74703' 24/6
# 'cfa70f60-2ffa-44b5-ac22-b5b6c44f56ae' 27/6 
