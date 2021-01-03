import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from comfpy.weighting import FrequencyWeighting
from comfpy.window import slide
from comfpy.features import calc_rms


# TODO: return also time vector based on window options
# TODO: add pCT
# TODO: add pDE

class en12299:
    def __init__(self, fs=None, channels=None, analyse='full'):
        self.standard = 'en12299'
        self.fs = fs
        self.frequencyWeighting = FrequencyWeighting(standard=self.standard, fs=fs)
        self.channels = None
        self.filteredChannels = {'x': {},
                                 'y': {},
                                 'z': {}}
        self.cc = {'x': {},
                   'y': {},
                   'z': {}}
        self._process(channels, analyse)

    def _process(self, channels, analyse):
        if isinstance(channels, dict):
            if list(channels.keys()) == ['x', 'y', 'z']:
                self.channels = channels
                self._analyse(analyse)

    def _analyse(self, analyse='full'):
        if analyse == 'full':
            for direction, channel in zip(self.channels.keys(), self.channels.values()):
                for channelName in channel.keys():
                    a = self.filter(a=channel[channelName],
                                    direction=direction,
                                    channelName=channelName,
                                    returnResults=True)
                    cc = self.calcContiuousComfortValues(a=a)
                    self.cc[direction][channelName] = cc

    def filter(self, a=None, direction=None, channelName=None, returnResults=False):
        if a is not None and direction in ['x', 'y', 'z']:
            afilt = None
            if direction in ['x', 'y']:
                afilt = self.frequencyWeighting.filter('Wd', a)

            elif direction == 'z':
                afilt = self.frequencyWeighting.filter('Wb', a)

            if afilt is not None and channelName is not None:
                self.filteredChannels[direction][channelName] = afilt
                print(f'filtered signal and appended to {direction}-channel: {channelName}')

            if returnResults:
                return afilt

        else:
            raise Exception('error in en12299.filter()')

    def calcContiuousComfortValues(self, a=None, windowLenght=5, overlap=0.1):
        windowLenght = int(windowLenght*self.fs)
        overlap = int(overlap*self.fs)
        windows = slide(a, windowLenght, overlap)
        cc = np.array([])
        for w in windows:
            cc = np.append(cc, calc_rms(w))
        return cc

    def continuousComfortFromChannels(self, windowLenght=5, overlap=0.1):
        for direction in ['x', 'y', 'z']:
            for channel in self.filteredChannels[direction].keys():
                atemp = self.filteredChannels[direction][channel]
                cc_temp = self.calcContiuousComfortValues(atemp, windowLenght, overlap)
                self.cc[direction][channel] = cc_temp

    def plot(self, target='cc'):
        nrows = len(self.cc.keys())
        fig, axes = plt.subplots(nrows, 1)
        for i, direction in zip(range(nrows), self.cc.keys()):
            channel = self.cc[direction]
            channelNames = channel.keys()
            # print('channel', channel)
            for j, name in zip(range(len(channelNames)), channelNames):
                cc = channel[name]
                axes[i].bar(range(len(cc)), cc, color=sns.color_palette('Paired', 8)[j], label='name')
                print('channel', channel, 'name', name)
            # axes[i].legend()

    def get(self, channel=None, result='cc', as_dataframe=True):
        if result == 'cc':
            if channel is not None and channel in self.cc['x'].keys():
                res = {'x': None,
                       'y': None,
                       'z': None}

                for k in res.keys():
                    res[k] = self.cc[k][channel]

                if as_dataframe:
                    return pd.DataFrame(res)

                else:
                    return res
            else:
                raise KeyError(f'{channel} not in x, y or z channel names')
        else:
            print('not implemented yet')
