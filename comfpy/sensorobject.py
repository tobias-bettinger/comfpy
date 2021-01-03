import pandas as pd
import numpy as np


class Sensor:
    def __init__(self):
        self.fs = None
        self.sensorType = None
        self.sensorName = None
        self.geoLocation = None
        # self.channel_values = {'ax': [1,2,3,4,5]}
        self.channels = {}
        self.comfortMeasures = {}
        # uvm.

    def addNewChannel(self, values, name=None):
        if name is not None and name not in self.channels.keys():
            self.channels[name] = values

    def set_config(self, json):
        pass
