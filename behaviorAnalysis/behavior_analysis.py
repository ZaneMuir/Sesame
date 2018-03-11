"""Behavior analysis."""
import numpy as np
# import pandas as pd
import docopt
from phenosys_csv import get_lick_list
from visualStim_recording import get_trial_list, get_start_time

start_time = get_start_time("../demo/data_sample/180311_1934_0.data")
trial_list = get_trial_list("../demo/data_sample/180311_1934_0.data")
lick_list = get_lick_list("../demo/data_sample/Kaleidoscope-18.03.11.csv", start_time)


def get_behavior_result():
    result = {
        'hit': [],
        'miss': 0,
        'correct_reject': 0,
        'false_alarm': []}

    for item in trial_list:
        count = np.where(
            (lick_list > item[1]) & (lick_list < item[2])
            )[0].size

        if item[0] == 1:
            if count == 0:
                result['miss'] += 1
            else:
                result['hit'].append(count)
        else:
            if count == 0:
                result['correct_reject'] += 1
            else:
                result['false_alarm'].append(count)
    return result
