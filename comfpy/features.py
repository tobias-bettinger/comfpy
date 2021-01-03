import numpy as np
from scipy import signal


def calc_rms(data):
    result = np.sqrt(np.sum(data ** 2) / len(data))
    return result


def calc_vdv(data, T=5):
    result = np.power(np.sum(data ** 4) * T / len(data), 1. / 4)
    return result


def calc_crest_factor(data):
    peak = max(abs(data))
    return np.divide(peak, np.sqrt(np.sum(data ** 2) / len(data)))


def calc_IF(data):
    ifact = kurtosis(data) / 1.5
    result = np.power(abs(ifact), 1. / 4)
    return result


def calc_spectrum_data(data):
    f, Pxx_spec = signal.welch(data, 200, 'flattop', nperseg=400, scaling='spectrum', return_onesided=True)
    return (np.max(Pxx_spec[0:42]))


def calc_abs_max_value(rolled):
    return (np.max(np.abs([rolled.min(), rolled.max()])))


def calc_peak2peak(data):
    return (np.abs(np.max(data) - np.min(data)))
