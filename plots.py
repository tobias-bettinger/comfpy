import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from filters import Wb, Wc, Wd, Wp
from matplotlib.patches import Rectangle
from scipy import signal


def plot_bode(freq, angles, fs, resp, savefilename, filterstr):
    fig, axes = plt.subplots(2, 1, figsize=(9, 6))
    print(axes, np.shape(axes))
    plt.subplots_adjust(hspace=0.5)

    axes[0].loglog(freq * fs / (2 * np.pi), abs(resp), color="#00549F")
    axes[0].set_xlim(0.1, 100)
    axes[0].set_ylim(1e-2, 5)
    axes[0].set_xlabel("Frequency [$Hz$]")
    axes[0].set_ylabel("{}".format(filterstr))
    axes[0].set_title('Magnitude Response {}'.format(filterstr))
    axes[0].grid(which='both', linestyle='-', linewidth=0.5)

    axes[1].semilogx(freq * fs / (2 * np.pi), angles * 180 / np.pi, color="#00549F")
    axes[1].set_xlim(0.1, 100)
    axes[1].set_xlabel("Frequency [$Hz$]")
    axes[1].set_ylabel("Phase [$^\circ$]")
    axes[1].set_title('Phase Response {}'.format(filterstr))
    axes[1].grid(which='both', linestyle='-', linewidth=0.5)

    if savefilename is not None:
        plt.savefig(savefilename)
    else:
        plt.show()
