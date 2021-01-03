import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from comfpy.weighting import FrequencyWeighting
from comfpy.window import slide
from comfpy.features import calc_rms


class wz:
    def __init__(self, fs=None, channels=None, analyse='full'):
        self.standard = 'wz'
        self.fs = fs
        self.frequencyWeighting = FrequencyWeighting(standard=self.standard, fs=fs)
        self.channels = None
        # self.filteredChannels = {'x': {},
        #                          'y': {},
        #                          'z': {}}
        self.wz = {'x': {},
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

    def filter(self, a=None, direction=None, channelName=None, returnResults=False):
        if a is not None and direction in ['x', 'y', 'z']:
            afilt = None
            if direction in ['x', 'y']:
                afilt = self.frequencyWeighting.filter('By', a)

            elif direction == 'z':
                afilt = self.frequencyWeighting.filter('Bz', a)

            if afilt is not None and channelName is not None:
                self.wz[direction][channelName] = afilt
                print(f'filtered signal and appended to {direction}-channel: {channelName}')

            if returnResults:
                return afilt

        else:
            raise Exception('error in en12299.filter()')

    def get(self, channel=None, result='wz', as_dataframe=True):
        if result == 'wz':
            if channel is not None and channel in self.wz['x'].keys():
                res = {'x': None,
                       'y': None,
                       'z': None}

                for k in res.keys():
                    res[k] = self.wz[k][channel]

                if as_dataframe:
                    return pd.DataFrame(res)

                else:
                    return res
            else:
                raise KeyError(f'{channel} not in x, y or z channel names')
        else:
            print('not implemented yet')
