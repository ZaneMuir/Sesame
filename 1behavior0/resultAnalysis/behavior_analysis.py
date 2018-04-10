"""Behavior analysis."""
import numpy as np
import os
# import pandas as pd
# import docopt
from phenosys_csv import get_lick_list
from visualStim_recording import get_trial_list, get_start_time

# TODO: pip them together.


def get_behavior_result(stim_record, lick_record, needActual=False, cutoff=0):
    """Portal to get major results.

    **return**
    result: {
        'hit': [],
        'miss': 0,
        'correct_reject': 0,
        'false_alarm': []}
    misc: {
        'start_time': start_time,
        'trial_list': trial_list: [(go/no-go, start, end), ...],
        'lick_list': lick_list: [timestamp, ...]}
    """
    if needActual:
        dir_path, stim_path = os.path.split(stim_record)
        stim_record = os.path.join(dir_path, "actual_"+stim_path)

    start_time = get_start_time(stim_record)
    trial_list = get_trial_list(stim_record, cutoff)
    lick_list = get_lick_list(lick_record, start_time)

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
    misc = {
        'start_time': start_time,
        'trial_list': trial_list,
        'lick_list': lick_list}
    return result, misc
