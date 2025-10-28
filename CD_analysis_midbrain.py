"""
Developed with AI pair-programming for debugging and refactoring

Coding Direction (CD) analysis inspired by Li et al., 2016 (Nature Neuroscience):
"Robust neuronal dynamics in premotor cortex during motor planning".

This module computes a "coding direction" (cd) that maximally separates two
conditions—in this use-case, BLOCK-LEFT vs BLOCK-RIGHT—using the difference of
mean population responses across neurons, following Li et al.'s choice to use
mean-difference rather than LDA when covariance estimates are noisy.

It then projects trial-by-time population activity onto the cd and quantifies
separation (e.g., ROC AUC at the end of the delay epoch) and tests whether this
separation collapses under SNr optogenetic inhibition (or any perturbation).

-----------------------------------------------------------------------
Required inputs (per session or concatenated across sessions):
-----------------------------------------------------------------------
X : np.ndarray, shape (n_trials, n_time, n_neurons)
    Trial-by-time-bin spike counts or rates (ideally 10 ms bins). If counts,
    they will be smoothed with a 400 ms sliding window by default.

time : np.ndarray, shape (n_time,)
    Time-axis in seconds aligned to a relevant event (e.g., stimulus onset or
    go cue). Used to select sample and delay epochs for cd.

block : array-like, shape (n_trials,)
    Labels for trial block identity. Values should be strings or ints with two
    levels, e.g. {"left", "right"} or {0,1}. This defines the two groups the cd
    separates.

perturbation : array-like of bool, shape (n_trials,)
    True for SNr opto trials (or other perturbation), False for controls.
    The cd is computed **only** from control trials to avoid circularity.

correct : array-like of bool, shape (n_trials,), optional
    If provided, the cd is computed from correct control trials only, mirroring
    the Li et al. procedure. If omitted, all control trials are used.

session_id : array-like, shape (n_trials,), optional
    String/int per-trial session IDs. If provided, projections are mean-centered
    per session (using control trials) before across-session averaging, as in Li
    et al.

Parameters of interest (edit below):
- bin_size_ms: width of the fine time bins in X (default assumes 10 ms).
- window_ms:   width of the sliding window for computing windowed means (400 ms).
- step_ms:     step of the sliding window (10 ms recommended if time bins are 10 ms).
- sample_window, delay_window: epoch bounds in seconds on the provided time axis.

Outputs:
- cd: np.ndarray, shape (n_neurons,), unit vector coding direction.
- proj: np.ndarray, shape (n_trials, n_time), projections cd^T x(t).
- stats dict with:
    - auc_control_end_delay, auc_opto_end_delay
    - block_separation_control/opto (mean difference at end of delay)
    - collapse_delta = separation_control - separation_opto
    - bootstrap CIs and p-values for above

References:
Li N, Daie K, Svoboda K, Druckmann S. Robust neuronal dynamics in premotor
cortex during motor planning. Nat Neurosci. 2016.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, Dict
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

# ----------------------------- Utilities ------------------------------------

def _ensure_bool(arr, default=False):
    if arr is None:
        return None if default is None else np.full(0, default)
    return np.asarray(arr).astype(bool)


def _label_to_bool(block):
    """Map two-level labels to boolean (False/True)."""
    b = np.asarray(block)
    levels = pd.unique(b)
    if len(levels) != 2:
        raise ValueError(f"block has {len(levels)} unique values; expected exactly 2")
    return b == levels[1], levels  # True==levels[1], False==levels[0]


def rolling_window_mean(X: np.ndarray, window_bins: int) -> np.ndarray:
    """Compute sliding-window mean along time axis for X of shape (trials, time, neurons).
    No stride (i.e., same number of time points out). Window is centered using
    a simple uniform kernel via cumulative sums (valid for fixed window).
    """
    if window_bins <= 1:
        return X
    T = X.shape[1]
    pad = window_bins // 2
    # pad along time with edge values
    Xpad = np.pad(X, ((0,0),(pad,pad),(0,0)), mode='edge')
    csum = np.cumsum(Xpad, axis=1)
    win = csum[:, window_bins:, :] - csum[:, :-window_bins, :]
    return win / window_bins


def time_mask(time: np.ndarray, window: Tuple[float, float]) -> np.ndarray:
    t0, t1 = window
    return (time >= t0) & (time <= t1)


# --------------------------- Coding Direction -------------------------------

def compute_cd(
    X: np.ndarray,
    time: np.ndarray,
    block,
    perturbation: np.ndarray,
    correct: Optional[np.ndarray] = None,
    sample_window: Tuple[float, float] = (0.1, 0.5),
    delay_window: Tuple[float, float] = (0.5, 1.0),
    bin_size_ms: float = 10.0,
    window_ms: float = 400.0,
) -> Tuple[np.ndarray, Dict]:
    """
    Compute coding direction (cd) as the average of w_t = mean(block1) - mean(block0)
    across time within sample+delay epochs, using only **control** (non-perturbation)
    trials and (optionally) only correct trials, following Li et al.

    Returns cd as a unit vector (n_neurons,), plus a dict of diagnostics.
    """
    X = np.asarray(X)
    time = np.asarray(time)
    if X.ndim != 3:
        raise ValueError("X must be (n_trials, n_time, n_neurons)")

    # Build mask for trials used to compute cd
    ctrl_mask = ~np.asarray(perturbation, dtype=bool)
    if correct is not None:
        ctrl_mask &= np.asarray(correct, dtype=bool)

    if ctrl_mask.sum() < 10:
        raise ValueError("Not enough control trials to compute cd (need >= 10)")

    # Sliding window smoothing (centered) to 400 ms with ~10 ms bins
    bin_size = bin_size_ms / 1000.0
    window_bins = max(1, int(round(window_ms/1000.0 / bin_size)))
    Xw = rolling_window_mean(X, window_bins)

    # Boolean labels for blocks (False/True)
    block_bool, block_levels = _label_to_bool(block)

    # Epoch selection
    m_sample = time_mask(time, sample_window)
    m_delay  = time_mask(time, delay_window)
    m_epochs = m_sample | m_delay

    # Compute w_t at each time using only control trials
    X_ctrl = Xw[ctrl_mask]
    block_ctrl = block_bool[ctrl_mask]

    mu_true  = X_ctrl[block_ctrl].mean(axis=0)    # (time, neurons)
    mu_false = X_ctrl[~block_ctrl].mean(axis=0)   # (time, neurons)
    w_t = mu_true - mu_false                      # (time, neurons)

    # Average w_t over sample+delay epochs
    if m_epochs.sum() == 0:
        raise ValueError("No time points in sample+delay windows; check epoch bounds")
    cd = w_t[m_epochs].mean(axis=0)               # (neurons,)

    # Normalize cd to unit length for interpretability
    norm = np.linalg.norm(cd)
    if norm > 0:
        cd = cd / norm

    # Stability metric like Li et al.: correlation between late sample and late delay
    def _late(window, frac=0.5):
        idx = np.where(time_mask(time, window))[0]
        if idx.size == 0:
            return None
        start = idx[0] + int((idx.size - 1) * (1 - frac))
        return slice(start, idx[-1]+1)

    s_late = _late(sample_window)
    d_late = _late(delay_window)
    stability = np.nan
    if s_late and d_late:
        ws = w_t[s_late].mean(axis=0)
        wd = w_t[d_late].mean(axis=0)
        if np.std(ws) > 0 and np.std(wd) > 0:
            stability = np.corrcoef(ws, wd)[0,1]

    diags = {
        'block_levels': block_levels.tolist(),
        'window_bins': int(window_bins),
        'stability_corr_late_sample_vs_delay': float(stability),
        'cd_norm': float(norm),
    }
    return cd, diags


def project_cd(X: np.ndarray, cd: np.ndarray, bin_size_ms: float = 10.0, window_ms: float = 400.0) -> np.ndarray:
    """Project trial-by-time activity onto cd: returns (n_trials, n_time) array.
    Applies the same 400 ms sliding-window mean used for cd estimation.
    """
    window_bins = max(1, int(round(window_ms/bin_size_ms)))
    Xw = rolling_window_mean(X, window_bins)
    return np.tensordot(Xw, cd, axes=([2],[0]))  # (trials, time)


# ----------------------------- Statistics -----------------------------------

def _end_of_delay_index(time: np.ndarray, delay_window: Tuple[float,float]) -> int:
    idx = np.where(time_mask(time, delay_window))[0]
    if idx.size == 0:
        raise ValueError("No samples in delay window")
    return idx[-1]


def roc_at_time(proj: np.ndarray, labels_bool: np.ndarray, t_idx: int) -> float:
    scores = proj[:, t_idx]
    y = labels_bool.astype(int)
    # Handle degenerate single-class cases by returning 0.5
    if np.unique(y).size < 2:
        return 0.5
    return float(roc_auc_score(y, scores))


def bootstrap_mean_diff(a: np.ndarray, b: np.ndarray, n_boot: int = 5000, seed: int = 0) -> Dict:
    """Bootstrap the difference of means (a - b). Returns mean, CI, p (two-sided)."""
    rng = np.random.default_rng(seed)
    obs = float(np.nanmean(a) - np.nanmean(b))
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        aa = rng.choice(a, size=a.size, replace=True)
        bb = rng.choice(b, size=b.size, replace=True)
        diffs[i] = np.nanmean(aa) - np.nanmean(bb)
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    p = 2 * min(np.mean(diffs >= 0), np.mean(diffs <= 0))
    return {'obs': obs, 'ci95': (float(lo), float(hi)), 'p_two_sided': float(p)}


@dataclass
class CDResults:
    cd: np.ndarray
    proj: np.ndarray
    time: np.ndarray
    block_bool: np.ndarray
    block_levels: Tuple
    perturbation: np.ndarray
    session_id: Optional[np.ndarray]
    end_delay_idx: int
    diags: Dict
    metrics: Dict


def run_cd_pipeline(
    X: np.ndarray,
    time: np.ndarray,
    block,
    perturbation: np.ndarray,
    correct: Optional[np.ndarray] = None,
    session_id: Optional[np.ndarray] = None,
    sample_window: Tuple[float, float] = (0.1, 0.5),
    delay_window: Tuple[float, float] = (0.5, 1.0),
    bin_size_ms: float = 10.0,
    window_ms: float = 400.0,
    n_boot: int = 5000,
    seed: int = 0,
    epoch_mask: Optional[np.ndarray] = None,
    eval_time_s: Optional[float] = None,
) -> CDResults:
    """Full pipeline: compute cd on control trials, project all trials, compute
    end-of-delay separation and ROC AUC for control and opto, and quantify
    collapse under opto.

    If `epoch_mask` is provided (n_trials, n_time), cd is computed in "masked"
    mode (averaging each trial over its True-mask samples) rather than via
    fixed global sample/delay windows.
    """
    if epoch_mask is not None:
        cd, diags = compute_cd_masked(
            X, time, block, perturbation, epoch_mask, correct,
            bin_size_ms=bin_size_ms, window_ms=window_ms,
        )
    else:
        cd, diags = compute_cd(
            X, time, block, perturbation, correct,
            sample_window=sample_window, delay_window=delay_window,
            bin_size_ms=bin_size_ms, window_ms=window_ms,
        )

    proj = project_cd(X, cd, bin_size_ms=bin_size_ms, window_ms=window_ms)

    block_bool, block_levels = _label_to_bool(block)
    if eval_time_s is not None:
        end_idx = int(np.argmin(np.abs(time - eval_time_s)))
    else:
        end_idx = _end_of_delay_index(time, delay_window)

    ctrl = ~np.asarray(perturbation, dtype=bool)
    opto = ~ctrl

    # Separation metric: mean(proj | block==True) - mean(proj | block==False)
    sep_ctrl = bootstrap_mean_diff(
        proj[ctrl & block_bool, end_idx],
        proj[ctrl & ~block_bool, end_idx], n_boot=n_boot, seed=seed
    )
    sep_opto = bootstrap_mean_diff(
        proj[opto & block_bool, end_idx],
        proj[opto & ~block_bool, end_idx], n_boot=n_boot, seed=seed
    )

    # Collapse under opto: delta = sep_control - sep_opto
    delta_obs = sep_ctrl['obs'] - sep_opto['obs']
    # Bootstrap delta by pairing resamples within each condition
    rng = np.random.default_rng(seed)
    diffs = np.empty(n_boot)
    a_ctrl = proj[ctrl & block_bool, end_idx]
    b_ctrl = proj[ctrl & ~block_bool, end_idx]
    a_opto = proj[opto & block_bool, end_idx]
    b_opto = proj[opto & ~block_bool, end_idx]
    for i in range(n_boot):
        aa_c = rng.choice(a_ctrl, size=a_ctrl.size, replace=True)
        bb_c = rng.choice(b_ctrl, size=b_ctrl.size, replace=True)
        aa_o = rng.choice(a_opto, size=a_opto.size, replace=True)
        bb_o = rng.choice(b_opto, size=b_opto.size, replace=True)
        diffs[i] = (np.nanmean(aa_c) - np.nanmean(bb_c)) - (np.nanmean(aa_o) - np.nanmean(bb_o))
    lo_d, hi_d = np.percentile(diffs, [2.5, 97.5])
    p_delta = 2 * min(np.mean(diffs >= 0), np.mean(diffs <= 0))

    # ROC AUC at end of delay
    auc_ctrl = roc_at_time(proj[ctrl], block_bool[ctrl], end_idx)
    auc_opto = roc_at_time(proj[opto], block_bool[opto], end_idx)

    # Optional per-session mean-centering (offset removal) for plotting/averaging
    if session_id is not None:
        sid = np.asarray(session_id)
        proj_centered = proj.copy()
        for s in np.unique(sid):
            m = (sid == s) & ctrl  # center using control trials only
            if m.any():
                offset = np.nanmean(proj[m])
                proj_centered[sid == s] -= offset
        proj = proj_centered

    metrics = {
        'sep_control': sep_ctrl,
        'sep_opto': sep_opto,
        'collapse_delta': {'obs': float(delta_obs), 'ci95': (float(lo_d), float(hi_d)), 'p_two_sided': float(p_delta)},
        'auc_control_end_delay': float(auc_ctrl),
        'auc_opto_end_delay': float(auc_opto),
        'end_of_delay_time_s': float(time[end_idx]),
    }

    return CDResults(cd, proj, time, block_bool, tuple(block_levels), np.asarray(perturbation, bool), session_id, end_idx, diags, metrics)


# ----------------------------- Binning helpers ------------------------------

def build_binned_X(
    spike_times: np.ndarray,
    spike_clusters: np.ndarray,
    selected_cluster_ids: np.ndarray,
    align_times: np.ndarray,
    t_before: float,
    t_after: float,
    bin_size: float,
    as_rate: bool = False,
):
    """
    Build X with shape (n_trials, n_time, n_neurons) from flat spike arrays.

    Parameters
    ----------
    spike_times : (n_spikes,) array of spike times (s, absolute time)
    spike_clusters : (n_spikes,) array of cluster IDs (int) per spike
    selected_cluster_ids : (n_neurons,) array of cluster IDs to include (order defines neuron order)
    align_times : (n_trials,) array of event times to align to (e.g., trial start)
    t_before, t_after : window size around each align time (s)
    bin_size : width of bins (s)
    as_rate : if True, return rates (spikes/s). Otherwise counts per bin.

    Returns
    -------
    X : (n_trials, n_time, n_neurons) float32
    time : (n_time,) array of bin centers relative to align (s)
    neuron_ids : (n_neurons,) array of cluster IDs in the column order of X
    """
    spike_times = np.asarray(spike_times)
    spike_clusters = np.asarray(spike_clusters)
    neuron_ids = np.asarray(selected_cluster_ids)
    align_times = np.asarray(align_times)

    # Ensure neuron order is exactly as passed (assumed unique)
    neuron_ids = neuron_ids.astype(int)
    n_neurons = neuron_ids.size
    id_to_col = pd.Series(np.arange(n_neurons), index=neuron_ids)

    # Time axis & edges (relative to alignment event)
    # Use integer-bin construction so that 0.0 is represented exactly and masks hit 0 s.
    n_before = int(round(t_before / bin_size))
    n_after  = int(round(t_after  / bin_size))
    idx = np.arange(-n_before, n_after, dtype=int)
    time = idx.astype(np.float64) * bin_size  # guarantees an exact 0.0 sample
    bin_edges = np.concatenate([time, [time[-1] + bin_size]])
    n_time = time.size
    n_trials = align_times.size

    X = np.zeros((n_trials, n_time, n_neurons), dtype=np.float32)

    # Loop over trials; 2D-hist spikes into (time, neuron)
    for j, t_align in enumerate(align_times):
        t0 = t_align - t_before
        t1 = t_align + t_after
        m = (spike_times >= t0) & (spike_times < t1)
        if not np.any(m):
            continue
        rel_t = spike_times[m] - t_align
        cl = spike_clusters[m].astype(int)
        # Map cluster IDs -> column indices; drop spikes from non-selected units
        col = id_to_col.reindex(cl).values  # float; NaN for non-selected
        keep = ~np.isnan(col)
        if not np.any(keep):
            continue
        rel_t = rel_t[keep]
        col = col[keep].astype(int)
        H, _, _ = np.histogram2d(rel_t, col, bins=[bin_edges, np.arange(n_neurons+1)])
        if as_rate:
            H = H / bin_size
        X[j] = H.astype(np.float32)

    return X, time, neuron_ids


def make_quiescent_mask(time: np.ndarray, quiescent_durations: np.ndarray, position: str = "post") -> np.ndarray:
    """Per-trial variable quiescent mask.
    position: "post" means mask [0, +dur) relative to alignment (quiescence at trial start);
              "pre"  means mask [-dur, 0) (quiescence before trial start).
    """
    time = np.asarray(time)
    durations = np.asarray(quiescent_durations, dtype=float)
    n_trials = durations.size
    mask = np.zeros((n_trials, time.size), dtype=bool)
    for i, d in enumerate(durations):
        if not np.isfinite(d) or d <= 0:
            continue
        if position == "post":
            mask[i] = (time >= 0) & (time < d)
        elif position == "pre":
            mask[i] = (time >= -d) & (time < 0)
        else:
            raise ValueError("position must be 'post' or 'pre'")
    return mask


def make_interval_mask(time: np.ndarray, start_rel: np.ndarray, end_rel: np.ndarray) -> np.ndarray:
    """Per-trial variable interval mask on the common time vector.
    For each trial i, marks (time >= start_rel[i]) & (time < end_rel[i]).
    start_rel and end_rel are times **relative to the alignment event** used to
    build X (e.g., trial start if you aligned to trials['intervals'][:,0]).
    Includes a tiny tolerance to avoid floating-point edge misses at 0 s.
    """
    time = np.asarray(time)
    start_rel = np.asarray(start_rel, dtype=float)
    end_rel = np.asarray(end_rel, dtype=float)
    if start_rel.shape != end_rel.shape:
        raise ValueError("start_rel and end_rel must have the same shape")
    n_trials = start_rel.size
    mask = np.zeros((n_trials, time.size), dtype=bool)
    tol = 1e-12
    for i, (s, e) in enumerate(zip(start_rel, end_rel)):
        if not (np.isfinite(s) and np.isfinite(e)):
            continue
        if e <= s:
            continue
        mask[i] = (time >= (s - tol)) & (time < (e + tol))
    return mask


# ------------------------------ Masked CD -----------------------------------

def compute_cd_masked(
    X: np.ndarray,
    time: np.ndarray,
    block,
    perturbation: np.ndarray,
    epoch_mask: np.ndarray,
    correct: Optional[np.ndarray] = None,
    bin_size_ms: float = 10.0,
    window_ms: float = 400.0,
) -> Tuple[np.ndarray, Dict]:
    """Compute cd using a per-trial epoch mask (n_trials, n_time).

    Procedure: for control (and optionally correct) trials, first average each
    trial's activity across its True-mask timepoints to get a single vector per
    trial (neurons,). Then cd = mean(vector | block==True) - mean(vector | block==False).
    """
    X = np.asarray(X)
    epoch_mask = np.asarray(epoch_mask, dtype=bool)

    if X.ndim != 3:
        raise ValueError("X must be (n_trials, n_time, n_neurons)")
    if epoch_mask.shape[:2] != X.shape[:2]:
        raise ValueError("epoch_mask must be (n_trials, n_time) matching X")

    ctrl = ~np.asarray(perturbation, bool)
    if correct is not None:
        ctrl &= np.asarray(correct, bool)
    if ctrl.sum() < 10:
        raise ValueError("Not enough control trials to compute cd (need >= 10)")

    # Apply same smoothing as cd estimation path
    bin_size = bin_size_ms / 1000.0
    window_bins = max(1, int(round(window_ms/1000.0 / bin_size)))
    Xw = rolling_window_mean(X, window_bins)

    block_bool, block_levels = _label_to_bool(block)

    # Masked per-trial means over time -> (n_trials, n_neurons)
    masked = np.where(epoch_mask[..., None], Xw, np.nan)
    with np.errstate(invalid='ignore'):
        trial_vecs = np.nanmean(masked, axis=1)  # (trials, neurons)

    vec_true  = trial_vecs[ctrl & block_bool]
    vec_false = trial_vecs[ctrl & ~block_bool]

    cd = np.nanmean(vec_true, axis=0) - np.nanmean(vec_false, axis=0)
    norm = np.linalg.norm(cd)
    if norm > 0:
        cd = cd / norm

    diags = {
        'block_levels': block_levels.tolist(),
        'window_bins': int(window_bins),
        'stability_corr_late_sample_vs_delay': float('nan'),  # not defined in masked mode
        'cd_norm': float(norm),
        'masked_mode': True,
    }
    return cd, diags


def run_cd_pipeline_with_cd(
    X: np.ndarray,
    time: np.ndarray,
    cd: np.ndarray,
    block,
    perturbation: np.ndarray,
    correct: Optional[np.ndarray] = None,
    session_id: Optional[np.ndarray] = None,
    bin_size_ms: float = 10.0,
    window_ms: float = 400.0,
    n_boot: int = 5000,
    seed: int = 0,
    eval_time_s: Optional[float] = None,
    delay_window: Tuple[float, float] = (0.5, 1.0),
) -> CDResults:
    """Project with a precomputed cd and compute separation/AUC/collapse metrics.
    Skips cd estimation. Useful for dual-alignment workflows (cd computed on
    enforced-QP-aligned X, projections shown trial-/laser-aligned).
    """
    proj = project_cd(X, cd, bin_size_ms=bin_size_ms, window_ms=window_ms)
    block_bool, block_levels = _label_to_bool(block)

    if eval_time_s is not None:
        end_idx = int(np.argmin(np.abs(time - eval_time_s)))
    else:
        end_idx = _end_of_delay_index(time, delay_window)

    ctrl = ~np.asarray(perturbation, dtype=bool)
    opto = ~ctrl

    sep_ctrl = bootstrap_mean_diff(
        proj[ctrl & block_bool, end_idx],
        proj[ctrl & ~block_bool, end_idx], n_boot=n_boot, seed=seed
    )
    sep_opto = bootstrap_mean_diff(
        proj[opto & block_bool, end_idx],
        proj[opto & ~block_bool, end_idx], n_boot=n_boot, seed=seed
    )

    delta_obs = sep_ctrl['obs'] - sep_opto['obs']
    rng = np.random.default_rng(seed)
    diffs = np.empty(n_boot)
    a_ctrl = proj[ctrl & block_bool, end_idx]
    b_ctrl = proj[ctrl & ~block_bool, end_idx]
    a_opto = proj[opto & block_bool, end_idx]
    b_opto = proj[opto & ~block_bool, end_idx]
    for i in range(n_boot):
        aa_c = rng.choice(a_ctrl, size=a_ctrl.size, replace=True)
        bb_c = rng.choice(b_ctrl, size=b_ctrl.size, replace=True)
        aa_o = rng.choice(a_opto, size=a_opto.size, replace=True)
        bb_o = rng.choice(b_opto, size=b_opto.size, replace=True)
        diffs[i] = (np.nanmean(aa_c) - np.nanmean(bb_c)) - (np.nanmean(aa_o) - np.nanmean(bb_o))
    lo_d, hi_d = np.percentile(diffs, [2.5, 97.5])
    p_delta = 2 * min(np.mean(diffs >= 0), np.mean(diffs <= 0))

    auc_ctrl = roc_at_time(proj[ctrl], block_bool[ctrl], end_idx)
    auc_opto = roc_at_time(proj[opto], block_bool[opto], end_idx)

    diags = {'cd_source': 'precomputed', 'cd_norm': float(np.linalg.norm(cd))}
    metrics = {
        'sep_control': sep_ctrl,
        'sep_opto': sep_opto,
        'collapse_delta': {'obs': float(delta_obs), 'ci95': (float(lo_d), float(hi_d)), 'p_two_sided': float(p_delta)},
        'auc_control_end_delay': float(auc_ctrl),
        'auc_opto_end_delay': float(auc_opto),
        'end_of_delay_time_s': float(time[end_idx]),
    }

    return CDResults(cd, proj, time, block_bool, tuple(block_levels), np.asarray(perturbation, bool), session_id, end_idx, diags, metrics)


# ------------------------------ Plotting ------------------------------------

def plot_trajectories(results: CDResults, save_figures, figure_save_path, figure_prefix, smooth_ms: Optional[float] = None, title: Optional[str] = None):
    """Plot mean ± SEM trajectories for control vs opto and block==False/True.
    Uses default matplotlib colors; no explicit color choices.
    """
    proj = results.proj
    time = results.time
    block = results.block_bool
    ctrl = ~results.perturbation
    opto = ~ctrl

    def _mean_sem(mat):
        return np.nanmean(mat, axis=0), np.nanstd(mat, axis=0) / np.sqrt(max(1, mat.shape[0]))

    groups = {
        'Control • Block 0': proj[ctrl & ~block],
        'Control • Block 1': proj[ctrl &  block],
        'Opto • Block 0':    proj[opto & ~block],
        'Opto • Block 1':    proj[opto &  block],
    }

    plt.figure(figsize=(8,4))
    for label, mat in groups.items():
        if mat.size == 0:
            continue
        mu, se = _mean_sem(mat)
        plt.plot(time, mu, label=label)
        plt.fill_between(time, mu - se, mu + se, alpha=0.2)
    plt.axvline(time[results.end_delay_idx], linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Projection (cd^T x)')
    if title:
        plt.title(title)
    plt.legend()
    plt.tight_layout()
    if save_figures == 1:
        plt.savefig(figure_save_path + figure_prefix + '_psych.png')  # Change the path as needed
        plt.close()
    else:
        plt.show()



# ----------------------------- Actual Usage --------------------------------
import seaborn as sns
from ibllib.io.raw_data_loaders import load_data
from one.api import ONE
from brainbox.io.one import SpikeSortingLoader, load_lfp
from iblatlas.atlas import AllenAtlas, BrainRegions
from scipy import stats
import statistics
from pathlib import Path

import sys
sys.path.append('/Users/natemiska/python/bias_coding')
from functions_optostim import isbiasblockselective_03, generate_pseudo_sessions
from metadata_optostim import light_artifact_units_SNr,light_artifact_units_SNr_contra,pids_list_SNr,pids_list_SNr_contra,inhibition_trials_range_list_SNr,inhibition_trials_range_list_SNr_contra,pids_list_SNr_trained,pids_list_SNr_contra_trained,excitation_trials_range_list_SNr_trained,inhibition_trials_range_list_SNr_trained,excitation_trials_range_list_SNr_contra_trained,inhibition_trials_range_list_SNr_contra_trained,light_artifact_units_SNr_trained,light_artifact_units_SNr_contra_trained,pids_list_ZI_trained,pids_list_ZI_trained_contra,excitation_trials_range_list_ZI_trained,inhibition_trials_range_list_ZI_trained,excitation_trials_range_list_ZI_trained_contra,inhibition_trials_range_list_ZI_trained_contra,light_artifact_units_ZI_trained,light_artifact_units_ZI_trained_contra, pids_list_SNr_reverse, excitation_trials_range_list_SNr_reverse, inhibition_trials_range_list_SNr_reverse, light_artifact_units_SNr_reverse

one = ONE(base_url='https://alyx.internationalbrainlab.org', cache_dir=Path.home() / '/Users/natemiska/Downloads/ONE/alyx.internationalbrainlab.org')
# one = ONE(base_url='https://alyx.internationalbrainlab.org')
# one=ONE(mode='remote')

ba = AllenAtlas()
br = BrainRegions()

#####################################################################################

condition = 'SNr_forBSanalysis'#'SNr_forBSanalysis'#'SNr_reverse'#'ZI_forBSanalysis'#'SNr_forBSanalysis' #'SNr_directstim'#'ZI_directstim'#'ZI_contra'#'SNr_ipsi' #'SNr_contra' #'ZI_ipsi'

onset_alignment = 'Laser onset' #'Laser onset' #'Go cue onset'

t_before = 2.5#10
t_after = 5#20
bin_size=0.05

IBL_quality_label_threshold = 0.6

firing_rate_threshold = 1

only_include_BS_units = 0

save_figures = 1
figures_path = '/Users/natemiska/Desktop/for_sonja_102825'


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
elif condition == 'SNr_reverse':
    pids = pids_list_SNr_reverse
    excitation_trials_range_list = excitation_trials_range_list_SNr_reverse
    inhibition_trials_range_list = inhibition_trials_range_list_SNr_reverse
    light_artifact_units_list = light_artifact_units_SNr_reverse
# elif condition == 'SNr_nontrained':
#     pids = pids_list_SNr + pids_list_SNr_contra
#     inhibition_trials_range_list = inhibition_trials_range_list_SNr + inhibition_trials_range_list_SNr_contra
#     light_artifact_units_list = light_artifact_units_SNr + light_artifact_units_SNr_contra
elif condition == 'SNr_ipsi':
    pids = pids_list_SNr
    inhibition_trials_range_list = inhibition_trials_range_list_SNr
    light_artifact_units_list = light_artifact_units_SNr
elif condition == 'SNr_contra':
    pids = pids_list_SNr_contra
    inhibition_trials_range_list = inhibition_trials_range_list_SNr_contra
    light_artifact_units_list = light_artifact_units_SNr_contra

### for incorporating previously calculated BS information
import pickle
clusters_info_DF = pd.read_pickle('~/python/saved_figures/' + condition + '_' + onset_alignment + '_BSdownstream_DF' '.pkl')

with open(condition + '_' + onset_alignment + '_delta_fr.pickle', 'rb') as f:
    data = pickle.load(f)

#####################################################################################

if __name__ == "__main__":

    for main_loop_num in np.arange(0,np.size(pids)):

    # main_loop_num = 0

        #### load data
        pid = pids[main_loop_num]
        ssl = SpikeSortingLoader(pid=pid, one=one, atlas=ba)
        eid = ssl.eid
        trials = one.load_object(eid, 'trials')
        inhibition_trials_range = inhibition_trials_range_list[main_loop_num]
        ses_path = one.eid2path(eid)

        probe_label = ssl.pname
        spikes, clusters, channels = ssl.load_spike_sorting(enforce_version=False)
        clusters = ssl.merge_clusters(spikes, clusters, channels)
        clusters_labels = clusters['label']
        # clusters_regions = clusters['acronym']
        allspikes = spikes

        #### remove low quality and light artifact clusters
        light_artifact_unit_IDs = light_artifact_units_list[main_loop_num]
        thresholded_cluster_IDs = np.where(clusters_labels > IBL_quality_label_threshold)[0]
        thresholded_cluster_IDs = np.setdiff1d(thresholded_cluster_IDs, light_artifact_unit_IDs)
        n_clusters = len(thresholded_cluster_IDs)

        ### time will be obtained from build_binned_X for each alignment; no manual grid here
        # (kept for clarity—removed explicit np.arange to avoid float rounding issues around 0 s)
        pass

        if inhibition_trials_range == 'ALL':
            inhibition_trials_range = range(0,len(trials['contrastLeft']))

        #### block IDs only for inhibition trials range in 80/20 blocks
        block_IDs = (trials.probabilityLeft[inhibition_trials_range] > 0.5).astype(int)

        #### loads laser intervals data
        try:
            laser_intervals = one.load_dataset(eid, '_ibl_laserStimulation.intervals')
            inhibition_trials_numbers = np.empty(max(inhibition_trials_range)+1)
            inhibition_trials_numbers[:] = np.nan
            nonstim_trials_numbers = np.empty(max(inhibition_trials_range)+1)
            nonstim_trials_numbers[:] = np.nan
            for k in inhibition_trials_range: 
                if trials.intervals[k,0] in laser_intervals[:,0]:
                    inhibition_trials_numbers[k] = k
                else:
                    nonstim_trials_numbers[k] = k
        except:
            print('Laser intervals data not found; loading depricated taskData')
            taskData = load_data(ses_path)
            
            inhibition_trials_numbers = np.empty(len(taskData))
            inhibition_trials_numbers[:] = np.nan
            nonstim_trials_numbers = np.empty(len(taskData))
            nonstim_trials_numbers[:] = np.nan
            for k in inhibition_trials_range: 
                if taskData[k]['opto'] == 1:
                    inhibition_trials_numbers[k] = k
                else:
                    nonstim_trials_numbers[k] = k

        inhibition_trials_numbers = inhibition_trials_numbers[np.isnan(inhibition_trials_numbers) == 0]
        nonstim_trials_numbers = nonstim_trials_numbers[np.isnan(nonstim_trials_numbers) == 0]
        excitation_trials_numbers = np.empty(0)
        n_trials = len(inhibition_trials_range)

        #### Bias selectivity analysis
        BS_scores = np.zeros(len(clusters_labels))
        pseudo_20_index_filtered,pseudo_80_index_filtered = generate_pseudo_sessions(trials)

        if only_include_BS_units == 1:
            print('Performing bias selectivity analysis for each cluster...')
            for cluster_num in thresholded_cluster_IDs:
                current_unit_spike_indices = np.where(allspikes.clusters == cluster_num)
                current_unit_spike_indices = current_unit_spike_indices[0]
                current_unit_spike_times = allspikes.times[current_unit_spike_indices]

                BS_score, pval_real, pct95_pseudo, fr_80_trials_nonstim, fr_20_trials_nonstim, fr_80_trials_inhibition, fr_20_trials_inhibition = isbiasblockselective_03(current_unit_spike_times, trials.probabilityLeft, trials.goCue_times, excitation_trials_numbers,inhibition_trials_numbers,nonstim_trials_numbers,
                            pseudo_20_index_filtered, pseudo_80_index_filtered)
                BS_scores[cluster_num] = BS_score

            old_thresholded_cluster_IDs = thresholded_cluster_IDs
            thresholded_cluster_IDs = np.where(BS_scores == 1)[0]
            n_clusters = len(thresholded_cluster_IDs)

        #### creates boolean array to represent stim/nonstim trials in inhibition range
        perturbation = np.isin(inhibition_trials_range, inhibition_trials_numbers)

        #### creates boolean array to represent correct/incorrect trials in inhibition range
        correct = (trials.feedbackType[inhibition_trials_range] > 0)

        #### Quiescent period currently fixed at 400ms - should be changed for each trial
        sample_window = (0.0, 0.4)
        delay_window  = (0.0, 0.4)

        #### define rng
        rng = np.random.default_rng(0)

        #### 1) define quiescent start/end and trial start (absolute)
        goCue_abs      = trials['goCue_times'][inhibition_trials_range]
        enforced_qp_len        = trials['quiescencePeriod'][inhibition_trials_range]
        enforced_qp_start_abs = goCue_abs - enforced_qp_len
        enforced_qp_end_abs   = goCue_abs
        trial_start_abs = trials['intervals'][inhibition_trials_range][:,0]

        #### 2) Build X for cd (aligned to enforced QP start) and for plotting (aligned to trial/laser onset)
        # --- CD alignment (Option B) ---
        t_before_cd = 0.05
        t_after_cd  = 0.75 
        align_times_cd = enforced_qp_start_abs
        X_cd, time_cd, _ = build_binned_X(
            allspikes['times'], allspikes['clusters'],
            thresholded_cluster_IDs, align_times_cd,
            t_before_cd, t_after_cd, bin_size, as_rate=False
        )
        # mask [0, enforced_qp_len_i)
        epoch_mask_cd = make_interval_mask(time_cd, np.zeros_like(enforced_qp_len), enforced_qp_len)

        ### sanity check
        zero_idx = int(np.argmin(np.abs(time_cd - 0.0)))
        print("cd-mask@0s fraction:", np.mean(epoch_mask_cd[:, zero_idx]))
        print("cd-window end median (s):", np.nanmedian(enforced_qp_len))

        # Compute cd from control trials during enforced QP
        cd, diags_cd = compute_cd_masked(
            X_cd, time_cd, block_IDs, perturbation, epoch_mask_cd, correct=correct,
            bin_size_ms=bin_size*1000.0, window_ms=200.0,
        )

        # --- Plot/projection alignment (trial/laser onset) ---
        align_times = trial_start_abs
        X, time, unit_ids = build_binned_X(
            allspikes['times'], allspikes['clusters'],
            thresholded_cluster_IDs, align_times,
            t_before, t_after, bin_size, as_rate=False
        )

        #### run pipeline (with precomputed cd)
        res = run_cd_pipeline_with_cd(
            X, time, cd, block_IDs, perturbation, correct=correct,
            bin_size_ms=bin_size*1000.0, window_ms=200.0,
            n_boot=2000, seed=1,
            eval_time_s=0.0,
        )
        # res = run_cd_pipeline(
        #     X, time, block_IDs, perturbation, correct=correct,
        #     epoch_mask=epoch_mask,
        #     bin_size_ms=bin_size*1000.0, window_ms=200.0,
        #     n_boot=2000, seed=1,
        #     eval_time_s=0.0,                       # onset
        #     # or: eval_time_s=float(np.nanmedian(q_end_rel))  # go cue
        # )


        indices_for_ALL = clusters_info_DF['pid'] == pid
        indices_for_BS = (clusters_info_DF['pid'] == pid) & (clusters_info_DF['BS_score'] == 1)

        num_ALL_units = len(np.where(indices_for_ALL == True)[0])
        num_BS_units = len(np.where(indices_for_BS == True)[0])

        if pid in pids_list_SNr_trained:
            hemisphere = 'ipsi'
        else:
            hemisphere = 'contra'

        print('pid = ' + pid)
        print('eid = ' + str(eid))
        print('hemisphere = ' + hemisphere)
        print('Total num units = ' + str(num_ALL_units))
        print('Total num BS units = ' + str(num_BS_units))
        print('Total num trials = ' + str(n_trials))

        plot_trajectories(res, save_figures, figures_path, pid, title=f'CD Projections — Control vs Opto, Block 0/1 (pid={pid})')