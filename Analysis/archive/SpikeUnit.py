
import pandas as pd
import numpy as np
# import scipy.io
import h5py
import os

class SpikeUnit(object):
    """docstring for [object Object]."""
    def __init__(self, session, mouse_id, channel, spike_train):
        self.session = session
        self.mouse_id = mouse_id
        self.channel = channel
        self.spike_train = spike_train

class SpikeMarker(object):
    """docstring for [object Object]."""
    def __init__(self, session, mouse_id, markers, raw_stim_marker):
        self.session = session
        self.mouse_id = mouse_id
        self.markers = markers
        self._raw_stim = raw_stim_marker
        self.grouped_marker = self.get_grouped_markers()

    def get_marker_time_series(self):
        return np.array([time for (time, name) in self.markers])

    def get_marker_of(self, stim_name):
        return [time for (time, name) in self.markers if name == stim_name]

    def get_grouped_markers(self):
        result = {}
        names = set([name for (time, name) in self.markers])
        for name in names:
            result[name] = self.get_marker_of(stim_name=name)
        return result


# ts5_V1_180329_GBL
def readin_electrode_data(session, mouse_id, data_dir="./data", marker_name='DIG01'):
    mat = os.path.join(data_dir, "{id}_{session}.mat".format(id=mouse_id, session=session))
    csv = os.path.join(data_dir, "{id}_{session}.csv".format(id=mouse_id, session=session))

    data_dict = {}
    with h5py.File(mat,"r") as f:
        neuron_name = list(f.keys())
        for name in neuron_name:
            data_dict[name] = f.get(name)['times'].value[0]

    stim_csv = pd.read_csv(csv)

    shift = len(stim_csv)-2 - len(data_dict[marker_name])
    if shift >= 0:
        start_d = data_dict[marker_name][0] - stim_csv.startstamp[1]
        end_d = data_dict[marker_name][-1] - stim_csv.startstamp[len(stim_csv)-2-shift]
        if np.abs(start_d - end_d) <= 2.0:
            pass  # valid
        else:
            raise ValueError("marker value not match!")
    else:
        raise ValueError("electrode markers exceed stimulus markers!")

    marker_times = data_dict.pop(marker_name)
    marker_name = stim_csv.colorname[1:len(stim_csv)-shift-1]
    marker = SpikeMarker(session, mouse_id, list(zip(marker_times, marker_name)), stim_csv)

    neurons = {}
    for (channel, spiketrain) in data_dict.items():
        neurons[channel] = SpikeUnit(session, mouse_id, channel, spiketrain)

    return marker, neurons
