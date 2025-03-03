import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from brainbox import singlecell
from brainbox.task.closed_loop import generate_pseudo_blocks
from scipy import stats
from scipy.stats import ranksums
from statsmodels.stats.multitest import multipletests
import statistics


def signed_contrast(trials):
    """Returns an array of signed contrasts in percent, where -ve values are on the left"""
    # Replace NaNs with zeros, stack and take the difference
    contrast = np.nan_to_num(np.c_[trials.contrastLeft, trials.contrastRight])
    return np.diff(contrast).flatten() * 100

def peri_event_time_histogram(
        spike_times, spike_clusters, events, cluster_id,  # Everything you need for a basic plot
        t_before=0.2, t_after=0.5, bin_size=0.025, smoothing=0.025, as_rate=True,
        include_raster=False, n_rasters=None, error_bars='std', ax=None, yticks=False,
        normalize_to_baseline = 0,
        pethline_kwargs={'color': 'blue', 'lw': 2},
        errbar_kwargs={'color': 'blue', 'alpha': 0.5},
        eventline_kwargs={'color': 'black', 'alpha': 0.5},
        raster_kwargs={'color': 'black', 'lw': 0.5}, **kwargs):
    """
    Plot peri-event time histograms, with the meaning firing rate of units centered on a given
    series of events. Can optionally add a raster underneath the PETH plot of individual spike
    trains about the events.

    Parameters
    ----------
    spike_times : array_like
        Spike times (in seconds)
    spike_clusters : array-like
        Cluster identities for each element of spikes
    events : array-like
        Times to align the histogram(s) to
    cluster_id : int
        Identity of the cluster for which to plot a PETH

    t_before : float, optional
        Time before event to plot (default: 0.2s)
    t_after : float, optional
        Time after event to plot (default: 0.5s)
    bin_size :float, optional
        Width of bin for histograms (default: 0.025s)
    smoothing : float, optional
        Sigma of gaussian smoothing to use in histograms. (default: 0.025s)
    as_rate : bool, optional
        Whether to use spike counts or rates in the plot (default: `True`, uses rates)
    include_raster : bool, optional
        Whether to put a raster below the PETH of individual spike trains (default: `False`)
    n_rasters : int, optional
        If include_raster is True, the number of rasters to include. If `None`
        will default to plotting rasters around all provided events. (default: `None`)
    error_bars : {'std', 'sem', 'none'}, optional
        Defines which type of error bars to plot. Options are:
        -- `'std'` for 1 standard deviation
        -- `'sem'` for standard error of the mean
        -- `'none'` for only plotting the mean value
        (default: `'std'`)
    ax : matplotlib axes, optional
        If passed, the function will plot on the passed axes. Note: current
        behavior causes whatever was on the axes to be cleared before plotting!
        (default: `None`)
    pethline_kwargs : dict, optional
        Dict containing line properties to define PETH plot line. Default
        is a blue line with weight of 2. Needs to have color. See matplotlib plot documentation
        for more options.
        (default: `{'color': 'blue', 'lw': 2}`)
    errbar_kwargs : dict, optional
        Dict containing fill-between properties to define PETH error bars.
        Default is a blue fill with 50 percent opacity.. Needs to have color. See matplotlib
        fill_between documentation for more options.
        (default: `{'color': 'blue', 'alpha': 0.5}`)
    eventline_kwargs : dict, optional
        Dict containing fill-between properties to define line at event.
        Default is a black line with 50 percent opacity.. Needs to have color. See matplotlib
        vlines documentation for more options.
        (default: `{'color': 'black', 'alpha': 0.5}`)
    raster_kwargs : dict, optional
        Dict containing properties defining lines in the raster plot.
        Default is black lines with line width of 0.5. See matplotlib vlines for more options.
        (default: `{'color': 'black', 'lw': 0.5}`)

    Returns
    -------
        ax : matplotlib axes
            Axes with all of the plots requested.
    """

    # Check to make sure if we fail, we fail in an informative way
    if not len(spike_times) == len(spike_clusters):
        raise ValueError('Spike times and clusters are not of the same shape')
    if len(events) == 1:
        raise ValueError('Cannot make a PETH with only one event.')
    if error_bars not in ('std', 'sem', 'none'):
        raise ValueError('Invalid error bar type was passed.')
    if not all(np.isfinite(events)):
        raise ValueError('There are NaN or inf values in the list of events passed. '
                         ' Please remove non-finite data points and try again.')

    # Compute peths
    peths, binned_spikes = singlecell.calculate_peths(spike_times, spike_clusters, cluster_id,
                                                        events, t_before, t_after, bin_size,
                                                        smoothing, as_rate)

    # Construct an axis object if none passed
    if ax is None:
        plt.figure()
        ax = plt.gca()
    # Plot the curve and add error bars
    if len(cluster_id) > 1:
        mean = np.mean(peths.means, axis=0)
        norm_factor = np.mean(mean[0:int(t_before/bin_size)])
        if normalize_to_baseline == 1:
            mean = mean/norm_factor
    else:
        mean = peths.means[0, :]
        norm_factor = np.mean(mean[0:int(t_before/bin_size)])
        if normalize_to_baseline == 1:
            mean = mean/norm_factor
    ax.plot(peths.tscale, mean, **pethline_kwargs)
    if error_bars == 'std':
        if len(cluster_id) > 1:
            bars = np.mean(peths.stds, axis=0)/np.sqrt(len(cluster_id))  ######THIS IS PROBABLY NOT CORRECT, NEED TO DO ERROR PROPAGATION
            if normalize_to_baseline == 1:
                bars = bars/norm_factor
        else:
            bars = peths.stds[0, :]
            if normalize_to_baseline == 1:
                bars = bars/norm_factor
    elif error_bars == 'sem':
        if len(cluster_id) > 1:
            bars = (peths.stds[0, :] / np.sqrt(len(events)))/np.sqrt(len(cluster_id))  ######THIS IS PROBABLY NOT CORRECT, NEED TO DO ERROR PROPAGATION
            if normalize_to_baseline == 1:
                bars = bars/norm_factor
        else:
            bars = peths.stds[0, :] / np.sqrt(len(events))
            if normalize_to_baseline == 1:
                bars = bars/norm_factor
    else:
        bars = np.zeros_like(mean)
    if error_bars != 'none':
        ax.fill_between(peths.tscale, mean - bars, mean + bars, **errbar_kwargs)

    # Plot the event marker line. Extends to 5% higher than max value of means plus any error bar.
    plot_edge = (mean.max() + bars[mean.argmax()]) * 1.05
    ax.vlines(0., 0., plot_edge, **eventline_kwargs)
    # Set the limits on the axes to t_before and t_after. Either set the ylim to the 0 and max
    # values of the PETH, or if we want to plot a spike raster below, create an equal amount of
    # blank space below the zero where the raster will go.
    ax.set_xlim([-t_before, t_after])
    # ax.set_ylim([-plot_edge if include_raster else 0., plot_edge]) #needs to be changed for multi-plot
    ax.set_ylim([0., 100])
    # Put y ticks only at min, max, and zero
    if yticks:
        if mean.min() != 0:
            ax.set_yticks([0, mean.mean(), mean.max()])
        else:
            ax.set_yticks([0., mean.max()])
    # Move the x axis line from the bottom of the plotting space to zero if including a raster,
    # Then plot the raster
    if include_raster:
        if n_rasters is None:
            n_rasters = len(events)
        if n_rasters > 60:
            warn("Number of raster traces is greater than 60. This might look bad on the plot.")
        ax.axhline(0., color='black')
        tickheight = plot_edge / len(events[:n_rasters])  # How much space per trace
        tickedges = np.arange(0., -plot_edge - 1e-5, -tickheight)
        clu_spks = spike_times[spike_clusters == cluster_id]
        for i, t in enumerate(events[:n_rasters]):
            idx = np.bitwise_and(clu_spks >= t - t_before, clu_spks <= t + t_after)
            event_spks = clu_spks[idx]
            ax.vlines(event_spks - t, tickedges[i + 1], tickedges[i], **raster_kwargs)
        ax.set_ylabel('Firing Rate' if as_rate else 'Number of spikes', y=0.75)
    else:
        ax.set_ylabel('Firing Rate' if as_rate else 'Number of spikes')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Time (s) after event')
    return ax, plot_edge, peths

def generate_pseudo_sessions(trials, num_pseudo_sessions = 1000, filterval = 10):
    ### generate pseudo-sessions to be used for this session
    print('Generating pseudo-sessions')
    pseudo_trials = []
    pseudo_20_index_filtered = []
    pseudo_80_index_filtered = []

    for k in range(num_pseudo_sessions):     
        pseudo_trials.append(list(generate_pseudo_blocks(np.size(trials.feedback_times))))
        pseudo_20_index_filtered_vals = np.zeros((1, np.size(trials.feedback_times)), dtype=int)
        pseudo_80_index_filtered_vals = np.zeros((1, np.size(trials.feedback_times)), dtype=int)                   
        previous_trial_block_ID = 0.5
        current_trial_length = 0
        for l in range(0, np.size(pseudo_trials[k])):
            current_trial_block_ID = pseudo_trials[k][l]
            if current_trial_block_ID == previous_trial_block_ID:
                current_trial_length = current_trial_length + 1
                if current_trial_block_ID == 0.2:
                    if current_trial_length > filterval:
                        pseudo_20_index_filtered_vals[:,l] = l
                if current_trial_block_ID == 0.8:
                    if current_trial_length > filterval:
                        pseudo_80_index_filtered_vals[:,l] = l
            else:
                current_trial_length = 1

            previous_trial_block_ID = current_trial_block_ID

        pseudo_80_index_filtered_vals = pseudo_80_index_filtered_vals[(0.1 < pseudo_80_index_filtered_vals)]
        pseudo_20_index_filtered_vals = pseudo_20_index_filtered_vals[(0.1 < pseudo_20_index_filtered_vals)]
        pseudo_20_index_filtered.append(list(pseudo_20_index_filtered_vals))
        pseudo_80_index_filtered.append(list(pseudo_80_index_filtered_vals))

    return(pseudo_20_index_filtered,pseudo_80_index_filtered)

def isbiasblockselective_02(current_unit_spike_times, trials, excitation_trials_numbers, inhibition_trials_numbers,
                         pseudo_20_index_filtered, pseudo_80_index_filtered,
                         blocklength_filterval = 10, before_gocue_start_time = 0.4, before_gocue_end_time = 0.05,
                         BS_pval_threshold = 0.05):
 
    fr_per_trial = np.empty((1, np.size(trials.probabilityLeft)))
    fr_per_trial[:] = np.NaN
    fr_per_trial = fr_per_trial[0]
    block_80_trials_filtered = np.zeros((1, np.size(trials.probabilityLeft)), dtype=int)
    block_20_trials_filtered = np.zeros((1, np.size(trials.probabilityLeft)), dtype=int)
    # block_80_trials = np.where(trials_probabilityLeft == 0.8)[0]
    # block_20_trials = np.where(trials_probabilityLeft == 0.2)[0]
    for k in np.arange(0,np.size(trials.probabilityLeft)):
        current_trial_start_time = trials.goCue_times[k] - before_gocue_start_time
        current_trial_end_time = trials.goCue_times[k] - before_gocue_end_time

        numspikes_current_trial = np.where(np.logical_and(current_unit_spike_times>current_trial_start_time, current_unit_spike_times<current_trial_end_time))
        numspikes_current_trial = numspikes_current_trial[0]
        numspikes_current_trial = np.size(numspikes_current_trial)
        fr_per_trial[k] = numspikes_current_trial/(before_gocue_start_time - before_gocue_end_time)
        
        if k < 90:
            continue
        if k == 90:
            if trials.probabilityLeft[k] == 0.8:
                current_block_ID = 80
                current_block_length = 0
                if blocklength_filterval == 0:
                    block_80_trials_filtered[:,k] = k
                previous_block_ID = 80
                current_block_length = 1
                continue


            else:
                current_block_ID = 20
                current_block_length = 0
                if blocklength_filterval == 0:
                    block_20_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = 1
                continue

        current_block_ID = int(trials.probabilityLeft[k] * 100)
        if current_block_ID == previous_block_ID:
            if current_block_ID == 20:
                if current_block_length > blocklength_filterval:
                    block_20_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = current_block_length + 1
                continue
            if current_block_ID == 80:
                if current_block_length > blocklength_filterval:
                    block_80_trials_filtered[:,k] = k
                current_block_length = current_block_length + 1
                previous_block_ID = 80
                continue
        else:
            current_block_length = 0
            if current_block_ID == 80:
                if blocklength_filterval == 0:
                    block_80_trials_filtered[:,k] = k
                previous_block_ID = 80
                current_block_length = 1
                continue
            if current_block_ID == 20:
                if blocklength_filterval == 0:
                    block_80_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = 1
                continue
    stim_trials_numbers = np.concatenate((excitation_trials_numbers,inhibition_trials_numbers))
    fr_per_trial[stim_trials_numbers] = np.NaN
    block_80_trials_filtered = block_80_trials_filtered[(0.1 < block_80_trials_filtered)]
    block_20_trials_filtered = block_20_trials_filtered[(0.1 < block_20_trials_filtered)]
    fr_80_trials = fr_per_trial[block_80_trials_filtered]
    fr_20_trials = fr_per_trial[block_20_trials_filtered]
    fr_80_trials = fr_80_trials[~np.isnan(fr_80_trials)]
    fr_20_trials = fr_20_trials[~np.isnan(fr_20_trials)]

    t, pval_real = stats.ttest_ind(fr_80_trials, fr_20_trials, equal_var=False)

    ##### pseudo-block analysis
    num_pseudo_blocks = np.size(pseudo_80_index_filtered)
    pseudo_pvals = np.empty(num_pseudo_blocks)
    pseudo_pvals[:] = np.NaN
    for k in range(num_pseudo_blocks):     
        fr_80_trials_pseudo = fr_per_trial[pseudo_80_index_filtered[k]]
        fr_20_trials_pseudo = fr_per_trial[pseudo_20_index_filtered[k]]

        t2, pval_pseudo = stats.ttest_ind(fr_80_trials_pseudo, fr_20_trials_pseudo, equal_var=False)
        pseudo_pvals[k] = pval_pseudo

    pct50_pseudo = np.percentile(pseudo_pvals,50)
    pct95_pseudo = np.percentile(pseudo_pvals,5)
    #how significance assessed

    if pval_real < BS_pval_threshold and pval_real < pct50_pseudo:
        isbiasselective = 1
    else:
        isbiasselective = 0

    return isbiasselective, pval_real, pct50_pseudo

def isbiasblockselective_03(current_unit_spike_times, trials_probabilityLeft, trials_goCue_times, excitation_trials_numbers,inhibition_trials_numbers,nonstim_trials_numbers,
                         pseudo_20_index_filtered, pseudo_80_index_filtered,
                         blocklength_filterval = 10, before_gocue_start_time = 0.4, before_gocue_end_time = 0.05, 
                         BS_pval_threshold = 0.05):
 
    fr_per_trial = np.empty((1, np.size(trials_probabilityLeft)))
    fr_per_trial[:] = np.NaN
    fr_per_trial = fr_per_trial[0]
    block_80_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    block_20_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    block_80_excitation_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    block_20_excitation_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    block_80_inhibition_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    block_20_inhibition_trials_filtered = np.zeros((1, np.size(trials_probabilityLeft)), dtype=int)
    # block_80_trials = np.where(trials_probabilityLeft == 0.8)[0]
    # block_20_trials = np.where(trials_probabilityLeft == 0.2)[0]
    for k in np.arange(0,np.size(trials_probabilityLeft)):
        current_trial_start_time = trials_goCue_times[k] - before_gocue_start_time
        current_trial_end_time = trials_goCue_times[k] - before_gocue_end_time
        numspikes_current_trial = np.where(np.logical_and(current_unit_spike_times>current_trial_start_time, current_unit_spike_times<current_trial_end_time))
        numspikes_current_trial = numspikes_current_trial[0]
        numspikes_current_trial = np.size(numspikes_current_trial)
        fr_per_trial[k] = numspikes_current_trial/(before_gocue_start_time - before_gocue_end_time)
        
        if k < 90:
            continue
        if k == 90:
            if trials_probabilityLeft[k] == 0.8:
                current_block_ID = 80
                current_block_length = 0
                if blocklength_filterval == 0:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_80_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_80_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_80_inhibition_trials_filtered[:,k] = k
                previous_block_ID = 80
                current_block_length = 1
                continue


            else:
                current_block_ID = 20
                current_block_length = 0
                if blocklength_filterval == 0:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_20_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_20_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_20_inhibition_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = 1
                continue

        current_block_ID = int(trials_probabilityLeft[k] * 100)
        if current_block_ID == previous_block_ID:
            if current_block_ID == 20:
                if current_block_length > blocklength_filterval:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_20_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_20_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_20_inhibition_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = current_block_length + 1
                continue
            if current_block_ID == 80:
                if current_block_length > blocklength_filterval:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_80_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_80_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_80_inhibition_trials_filtered[:,k] = k
                current_block_length = current_block_length + 1
                previous_block_ID = 80
                continue
        else:
            current_block_length = 0
            if current_block_ID == 80:
                if blocklength_filterval == 0:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_80_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_80_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_80_inhibition_trials_filtered[:,k] = k
                previous_block_ID = 80
                current_block_length = 1
                continue
            if current_block_ID == 20:
                if blocklength_filterval == 0:
                    if np.isin(k,nonstim_trials_numbers) == 1:
                        block_80_trials_filtered[:,k] = k
                    if np.isin(k,excitation_trials_numbers) == 1:
                        block_80_excitation_trials_filtered[:,k] = k
                    if np.isin(k,inhibition_trials_numbers) == 1:
                        block_80_inhibition_trials_filtered[:,k] = k
                previous_block_ID = 20
                current_block_length = 1
                continue


    block_80_trials_filtered = block_80_trials_filtered[(0.1 < block_80_trials_filtered)]
    block_20_trials_filtered = block_20_trials_filtered[(0.1 < block_20_trials_filtered)]
    block_80_excitation_trials_filtered = block_80_excitation_trials_filtered[(0.1 < block_80_excitation_trials_filtered)]
    block_20_excitation_trials_filtered = block_20_excitation_trials_filtered[(0.1 < block_20_excitation_trials_filtered)]
    block_80_inhibition_trials_filtered = block_80_inhibition_trials_filtered[(0.1 < block_80_inhibition_trials_filtered)]
    block_20_inhibition_trials_filtered = block_20_inhibition_trials_filtered[(0.1 < block_20_inhibition_trials_filtered)]
    fr_80_trials_nonstim = fr_per_trial[block_80_trials_filtered]
    fr_20_trials_nonstim = fr_per_trial[block_20_trials_filtered]
    fr_80_trials_inhibition = fr_per_trial[block_80_inhibition_trials_filtered]
    fr_20_trials_inhibition = fr_per_trial[block_20_inhibition_trials_filtered]

    # t, pval_real = stats.ttest_ind(fr_80_trials_nonstim, fr_20_trials_nonstim, equal_var=False)
    pval_real = ranksums(fr_80_trials_nonstim, fr_20_trials_nonstim).pvalue

    # ##### pseudo-block analysis
    num_pseudo_blocks = len(pseudo_80_index_filtered)
    pseudo_pvals = np.empty(num_pseudo_blocks)
    pseudo_pvals[:] = np.NaN
    for k in range(num_pseudo_blocks):     
        fr_80_trials_pseudo = fr_per_trial[pseudo_80_index_filtered[k]]
        fr_20_trials_pseudo = fr_per_trial[pseudo_20_index_filtered[k]]

        # t2, pval_pseudo = stats.ttest_ind(fr_80_trials_pseudo, fr_20_trials_pseudo, equal_var=False)
        pval_pseudo = ranksums(fr_80_trials_pseudo, fr_20_trials_pseudo).pvalue
        pseudo_pvals[k] = pval_pseudo

    pct50_pseudo = np.percentile(pseudo_pvals,50)
    pct95_pseudo = np.percentile(pseudo_pvals,5)
    
    #how significance assessed
    # Apply the FDR correction to the set of pseudo p-values
    reject, fdr_pvals, _, _ = multipletests(pseudo_pvals, alpha=BS_pval_threshold, method='fdr_bh')

    # Check if the real p-value is significant after FDR correction
    if pval_real < BS_pval_threshold and pval_real < fdr_pvals.min():
        isbiasselective = 1
    else:
        isbiasselective = 0

    # if pval_real < BS_pval_threshold and pval_real < pct50_pseudo:
    # if pval_real < pct95_pseudo:
    #     isbiasselective = 1
    # else:
    #     isbiasselective = 0

    return isbiasselective, pval_real, pct95_pseudo, fr_80_trials_nonstim, fr_20_trials_nonstim, fr_80_trials_inhibition, fr_20_trials_inhibition

