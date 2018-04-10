"""convert phenosys csv into pandas dataframe."""

import numpy as np

acc = 0


def get_stimulus_func(filename, projection):
    """Generate the stimulus function, s(t)."""
    global start_time, acc
    acc = 0
    with open(filename, "r") as inputfile:
        rawFilm = eval(inputfile.readline())

    def accumulate(step):
        global acc
        acc += step
        return acc

    stims = [(projection[color], accumulate(step)) for color, step in rawFilm]

    def search(t):
        for index in range(len(stims)):
            if t < stims[index][1]:
                return stims[index][0]
        return 0

    return search


def get_trial_list(filename, cutoff):
    """Get trial info and time numpy.array from phenosys csv.

    **example**
    [(go/no-go, start_time, end_time), ...]
    """
    with open(filename, "r") as inputfile:
        false = False
        true = True
        sequence = eval(inputfile.readline())

    trial_list = []
    acc_seq = 0
    for item in sequence[0]['trial_sequence']:
        acc_seq += sum([color_seq[1] for color_seq in item['color_sequence']])
        if item['type'] == 'go':
            trial_list.append(
                (1, acc_seq-item['color_sequence'][-1][1], acc_seq-cutoff))
        elif item['type'] == 'no go':
            trial_list.append(
                (-1, acc_seq-item['color_sequence'][-1][1], acc_seq-cutoff))
        else:
            pass
    return np.array(trial_list)


def get_start_time(filename):
    """Get the start Unix timestamp."""
    with open(filename, 'r') as inputfile:
        inputfile.readline()
        start_time = inputfile.readline()
    return float(start_time)
