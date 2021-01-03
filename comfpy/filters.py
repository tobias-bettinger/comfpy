import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

from matplotlib.patches import Rectangle
from scipy import signal


def Wb(fs):
    f1b = 0.4  # [Hz]
    f2b = 100  # [Hz]
    f3b = 16  # [Hz]
    f4b = 16  # [Hz]
    f5b = 2.5  # [Hz]
    f6b = 4  # [Hz]

    Q1b = 1 / np.sqrt(2)  # [-]
    Q2b = 0.63  # [-]
    Q3b = 0.8  # [-]
    Q4b = 0.8  # [-]

    Kb = 0.4  # [-]

    # Define numerators and denominators of all four filters
    Hlbb = np.array([0, 0, np.square(2 * np.pi * f2b)])
    Hlba = np.array([1, (2 * np.pi * f2b) / Q1b, np.square(2 * np.pi * f2b)])

    Hhbb = np.array([1, 0, 0])
    Hhba = np.array([1, (2 * np.pi * f1b) / Q1b, np.square(2 * np.pi * f1b)])

    Htbb = np.array([0, np.square(2 * np.pi * f4b) / (2 * np.pi * f3b), np.square(2 * np.pi * f4b)])
    Htba = np.array([1, (2 * np.pi * f4b) / Q2b, np.square(2 * np.pi * f4b)])

    Hsbb = np.array([Kb / np.square(2 * np.pi * f5b), Kb / (Q3b * 2 * np.pi * f5b), Kb])
    Hsba = np.array([1 / np.square(2 * np.pi * f6b), 1 / (Q4b * 2 * np.pi * f6b), 1])

    # Convolve filters
    Hbb = np.convolve(np.convolve(Hlbb, Hhbb), np.convolve(Htbb, Hsbb))
    Hba = np.convolve(np.convolve(Hlba, Hhba), np.convolve(Htba, Hsba))

    # Create digital filter from analaog coefficients
    Hb = signal.bilinear(Hbb, Hba, fs)
    return Hb


def Wc(fs):
    f1c = 0.4  # [Hz]
    f2c = 100  # [Hz]
    f3c = 8  # [Hz]
    f4c = 8  # [Hz]

    Q1c = 1 / np.sqrt(2)  # [-]
    Q2c = 0.63  # [-]

    Kc = 1  # [-]

    # Define numerators and denominators of all three filters
    Hlcb = np.array([0, 0, np.square(2 * np.pi * f2c)])
    Hlca = np.array([1, (2 * np.pi * f2c) / Q1c, np.square(2 * np.pi * f2c)])

    Hhcb = np.array([1, 0, 0])
    Hhca = np.array([1, (2 * np.pi * f1c) / Q1c, np.square(2 * np.pi * f1c)])

    Htcb = np.array([0, np.square(2 * np.pi * f4c) / (2 * np.pi * f3c), np.square(2 * np.pi * f4c)])
    Htca = np.array([1, (2 * np.pi * f4c) / Q2c, np.square(2 * np.pi * f4c)])

    # Convolve filters
    Hcb = np.convolve(np.convolve(Hlcb, Hhcb), Htcb)
    Hca = np.convolve(np.convolve(Hlca, Hhca), Htca)

    # Create digital filter from analaog coefficients
    Hc = signal.bilinear(Hcb, Hca, fs)
    return Hc


def Wd(fs):
    f1d = 0.4  # [Hz]
    f2d = 100  # [Hz]
    f3d = 2  # [Hz]
    f4d = 2  # [Hz]

    Q1d = 1 / np.sqrt(2)  # [-]
    Q2d = 0.63  # [-]

    Kd = 1  # [-]

    # Define numerators and denominators of all three filters
    Hldb = np.array([0, 0, np.square(2 * np.pi * f2d)])
    Hlda = np.array([1, (2 * np.pi * f2d) / Q1d, np.square(2 * np.pi * f2d)])

    Hhdb = np.array([1, 0, 0])
    Hhda = np.array([1, (2 * np.pi * f1d) / Q1d, np.square(2 * np.pi * f1d)])

    Htdb = np.array([0, np.square(2 * np.pi * f4d) / (2 * np.pi * f3d), np.square(2 * np.pi * f4d)])
    Htda = np.array([1, (2 * np.pi * f4d) / Q2d, np.square(2 * np.pi * f4d)])

    # Convolve filters
    Hdb = np.convolve(np.convolve(Hldb, Hhdb), Htdb)
    Hda = np.convolve(np.convolve(Hlda, Hhda), Htda)

    # Create digital filter from analaog coefficients
    Hd = signal.bilinear(Hdb, Hda, fs)
    return Hd


def Wp(fs):
    f1p = 0  # [Hz]
    f2p = 100  # [Hz]
    f3p = 16  # [Hz]
    f4p = 16  # [Hz]

    Q1p = 1 / np.sqrt(2)  # [-]
    Q2p = 0.63  # [-]

    Kp = 1  # [-]

    # Define numerators and denominators of all three filters
    Hlpb = np.array([0, 0, np.square(2 * np.pi * f2p)])
    Hlpa = np.array([1, (2 * np.pi * f2p) / Q1p, np.square(2 * np.pi * f2p)])

    Hhpb = np.array([1, 0, 0])
    Hhpa = np.array([1, (2 * np.pi * f1p) / Q1p, np.square(2 * np.pi * f1p)])

    Htpb = np.array([0, np.square(2 * np.pi * f4p) / (2 * np.pi * f3p), np.square(2 * np.pi * f4p)])
    Htpa = np.array([1, (2 * np.pi * f4p) / Q2p, np.square(2 * np.pi * f4p)])

    # Convolve filters
    Hpb = np.convolve(np.convolve(Hlpb, Hhpb), Htpb)
    Hpa = np.convolve(np.convolve(Hlpa, Hhpa), Htpa)

    # Create digital filter from analaog coefficients
    Hp = signal.bilinear(Hpb, Hpa, fs)
    return Hp


def plot_acc_spectogram(a_in, fftL, nov, fs):
    f, ax2 = plt.subplots(1, 1, figsize=(9, 6))

    # ax1.plot(dataRS.index.total_seconds(), dataRS["ax1"], color="#00549F")
    # ax1.set_ylabel('Acceleration [$m/s^2$]')
    # ax1.minorticks_on()
    # ax1.grid(which='major', linestyle='-', linewidth=0.5)
    # ax1.grid(which='minor', linestyle='-', linewidth=0.1)
    # ax1.set_xlim(0, dataRS.index.total_seconds()[-1])
    # ax1.set_ylim(-10, 10)
    # ax1.get_yaxis().set_label_coords(-0.075, 0.5)
    # ax1.set_title("X-Acceleration")

    Pxx, freqx, bins, im = ax2.specgram(a_in, NFFT=fftL, Fs=fs, noverlap=nov, cmap='summer')
    ax2.set_xlabel('Time [$s$]')
    ax2.set_ylabel('Frequency [$Hz$]', labelpad=15)
    ax2.get_yaxis().set_label_coords(-0.075, 0.5)
    plt.close()

    return freqx, Pxx, bins


def Bz(fs, f, status='DB'):
    if status == 'DB':
        bVert = 0.588 * np.sqrt((1.911 * np.square(f) + np.square(0.25 * np.square(f))) / (
                np.square(1 - 0.277 * np.square(f)) + np.square(1.563 * f - 0.0368 * np.power(f, 3))))
    elif status == 'ORE':
        print('not implemented yet')
    return bVert


def By(fs, f, status='ORE'):
    bVert = Bz(fs, f)
    bLat = 1.25 * bVert
    return bLat

