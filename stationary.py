import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from filters import Wb, Wc, Wd, Wp
from matplotlib.patches import Rectangle
from scipy import signal


class FrequencyWeighting:
    def __init__(self, standard='en12299', posture='standing', direction='y', fs=None):
        self.standard = standard
        self.posture = posture
        self.direction = direction
        self.fs = fs
        self._validate()

    def _check_fs(self, fs):
        valid = True
        if fs < 0.0:
            raise Exception('fs must be > 0')

        if not isinstance(fs, int):
            raise Exception('fs must be int type but is {}'.format(type(self.fs)))

        return valid

    def _validate(self):
        # TODO: check if final Exception is enough after counting irregular initial values
        if self.standard not in ['en12299', 'iso2631', 'wz']:
            raise Exception("""standard not known, must be in ['en12299', 'iso2631', 'wz']""")

        if self.posture not in ['standing', 'seated']:
            raise Exception("""posture not known, must be in ['standing', 'seated']""")

        if self.direction not in ['x', 'y', 'z']:
            raise Exception("""direction not known, must be in ['x', 'y', 'z']""")

        if self._check_fs(self.fs):
            pass

    def _get_standing(self):
        if self.standard == 'en12299':
            if self.direction == 'y':
                return self._get_Wp()

    def _get_Wp(self):
        return Wp(self.fs)

    def _get_Wb(self):
        return Wb(self.fs)

    def _get_Wc(self):
        return Wc(self.fs)

    def _get_Wd(self):
        return Wd(self.fs)

    def info(self):
        return {'standard': self.standard,
                'posture': self.posture,
                'direction': self.direction,
                'fs': self.fs}

    def get(self, filterstr='Wp'):
        if filterstr == 'Wp':
            return self._get_Wp()
        elif filterstr == 'Wb':
            return self._get_Wb()
        elif filterstr == 'Wc':
            return self._get_Wc()
        elif filterstr == 'Wd':
            return self._get_Wd()
        else:
            raise Exception('No such filtertype --> {}'.format(filterstr))

    def filter(self, filterstr=None, a_unfilt=None, fs=None):
        if filterstr is not None:
            H = self.get(filterstr)
        else:
            raise Exception("""please provide filterstr, e.g. filterstr='Wp'""")

        if a_unfilt is not None:
            if fs is not None:
                if self._check_fs(fs):
                    print('changing sample frequency from {} Hz to fs={} Hz'.format(self.fs, fs))
                    self.fs = fs

            return signal.filtfilt(H[0], H[1], a_unfilt)

        else:
            raise Exception('please provide acceleration signal array')

    def plot_frequency_response(self, filterstr='Wp', savefilename=None):
        H = self.get(filterstr)
        freq, resp = signal.freqz(H[0], H[1], worN=1024)
        angles = np.unwrap(np.angle(resp))

        fig, axes = plt.subplots(2, 1, figsize=(9, 6))
        print(axes, np.shape(axes))
        plt.subplots_adjust(hspace=0.5)

        axes[0].loglog(freq * self.fs / (2 * np.pi), abs(resp), color="#00549F")
        axes[0].set_xlim(0.1, 100)
        axes[0].set_ylim(1e-2, 5)
        axes[0].set_xlabel("Frequency [$Hz$]")
        axes[0].set_ylabel("Wb")
        axes[0].set_title('Magnitude Response $W_b$')
        axes[0].grid(which='both', linestyle='-', linewidth=0.5)

        axes[1].semilogx(freq * self.fs / (2 * np.pi), angles * 180 / np.pi, color="#00549F")
        axes[1].set_xlim(0.1, 100)
        axes[1].set_xlabel("Frequency [$Hz$]")
        axes[1].set_ylabel("Phase [$^\circ$]")
        axes[1].set_title('Phase Response $W_b$')
        axes[1].grid(which='both', linestyle='-', linewidth=0.5)

        if savefilename is not None:
            plt.savefig(savefilename)
        else:
            plt.show()
