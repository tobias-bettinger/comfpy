import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from comfpy.filters import Wb, Wc, Wd, Wp, By, Bz, plot_acc_spectogram
from matplotlib.patches import Rectangle
from matplotlib import cm
import seaborn as sns
from scipy import signal
from comfpy.plots import plot_bode
from comfpy.features import *


class FrequencyWeighting:
    def __init__(self, standard='en12299', fs=None):
        self.standard = standard
        self.fs = fs
        self.posture = None
        self.direction = None
        self._validate()

    def _check_fs(self, fs):
        valid = True
        if fs is None:
            raise Exception('please provide sample frequency fs as int value')

        if fs < 0.0:
            raise Exception('fs must fulfill criterion fs > 0')

        if not isinstance(fs, int):
            raise Exception('fs must be int type but is {}'.format(type(self.fs)))

        return valid

    def _validate(self):
        # TODO: check if final Exception is enough after counting irregular initial values
        if self.standard not in ['en12299', 'iso2631', 'wz']:
            raise Exception("""standard not known, must be in ['en12299', 'iso2631', 'wz']""")

        if self._check_fs(self.fs):
            pass

    def _get_Wp(self):
        return Wp(self.fs)

    def _get_Wb(self):
        return Wb(self.fs)

    def _get_Wc(self):
        return Wc(self.fs)

    def _get_Wd(self):
        return Wd(self.fs)

    def _get_By(self, **kwargs):
        return By(self.fs, **kwargs)

    def _get_Bz(self, **kwargs):
        return Bz(self.fs, **kwargs)

    def info(self):
        return {'standard': self.standard,
                'posture': self.posture,
                'direction': self.direction,
                'fs': self.fs}

    def get(self, filterstr='Wp', **kwargs):
        if filterstr == 'Wp':
            return self._get_Wp()
        elif filterstr == 'Wb':
            return self._get_Wb()
        elif filterstr == 'Wc':
            return self._get_Wc()
        elif filterstr == 'Wd':
            return self._get_Wd()
        elif filterstr == 'By':
            return self._get_By(**kwargs)
        elif filterstr == 'Bz':
            return self._get_Bz(**kwargs)
        else:
            raise Exception('No such filtertype --> {}'.format(filterstr))

    def _filter_en(self, filterstr=None, a_unfilt=None, fs=None):
        if filterstr is not None:
            H = self.get(filterstr)
        else:
            raise Exception("""please provide filterstr, e.g. filterstr='Wp'""")

        if a_unfilt is not None:
            return signal.filtfilt(H[0], H[1], a_unfilt)

        else:
            raise Exception('please provide acceleration signal array')

    def _filter_wz(self, filterstr=None, a_infilt=None, fs=None):
        if filterstr is not None:
            fftL = fs * 5  # 5 second window length
            nov = int(fs * 1 / 10)  # 100 ms overlap
            freqx, Pxx, bins = plot_acc_spectogram(a_infilt, fftL, nov, fs)
            B = self.get(filterstr, f=freqx)
            cWz = np.dot(np.diag(np.square(100 * B)), Pxx)

            return cWz, freqx, Pxx

        else:
            raise Exception("""please provide filterstr, e.g. filterstr='By'""")

    def filter(self, filterstr=None, a_unfilt=None, fs=None):
        if fs is not None:
            if self._check_fs(fs):
                print('changing sample frequency from {} Hz to fs={} Hz'.format(self.fs, fs))
                self.fs = fs

        if self.standard == 'en12299':
            return self._filter_en(filterstr, a_unfilt, fs)

        elif self.standard == 'wz':
            cWz, freqx, Pxx = self._filter_wz(filterstr, a_unfilt, self.fs)
            return self.calculate_Wz(cWz, freqx)

    def calculate_Wz(self, cWz, freqx):
        return np.power(2 * np.trapz(cWz, freqx, axis=0), 0.15)

    def plot_frequency_response(self, filterstr='Wp', savefilename=None):
        H = self.get(filterstr)
        freq, resp = signal.freqz(H[0], H[1], worN=1024)
        angles = np.unwrap(np.angle(resp))
        plot_bode(freq, angles, self.fs, resp, savefilename, filterstr)
