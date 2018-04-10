"""generate visual stimuli sequence from json file."""

import random

import logging
logger = logging.getLogger(__name__)


def shuffleStimItem(paradigm):
    """Return a playlist with right weight for each stimulus."""
    weights = [item['weight'] for item in paradigm['playlist'].values()]
    shuffledItems = []
    index = 0
    for stim_name, each_stim in paradigm['playlist'].items():
        each_stim.update({"name": stim_name})
        for _ in range(weights[index]):
            shuffledItems.append(each_stim)
        index += 1
    return shuffledItems


def generateSingleTrial(stimTrial,
                        gapTrial={"color": "black", "length": 5},
                        length=1, interval=1, isUtility=False):
    """Return a single trial sequence."""
    if not isUtility:
        newTrial = []

        for colorname in stimTrial['paradigm']:
            newTrial.append((colorname, length))
            newTrial.append((gapTrial['color'], interval))

        newTrial.pop()

        newTrial.append((gapTrial['color'], gapTrial['length']))

        return {"name": stimTrial['name'],
                "type": stimTrial['type'],
                "stimulus": stimTrial['stimulus'],
                "color_sequence": newTrial}
    else:
        return {"name": stimTrial['name'],
                "type": 'utility',
                "stimulus": False,
                "color_sequence": [(stimTrial['color'], stimTrial['length'])]}


def generateTrialSequence(paradigm):
    """
    Return a new session sequence.

    trial_sequence[
        {name,
        type,
        stimulus,
        color_sequence[(color, stamp)]}
    ]
    """
    newTrialSequence = []
    utilityTrial = paradigm['utility']
    newTrialSequence.append(
        generateSingleTrial(utilityTrial['starting'], isUtility=True))

    if paradigm['shuffle']:
        stimPool = shuffleStimItem(paradigm)
        for _ in range(paradigm['trial_count']):
            newTrialSequence.append(
                generateSingleTrial(
                    random.sample(stimPool, 1)[0],
                    utilityTrial['gap'],
                    paradigm['length'], paradigm['interval']))
    else:
        pass  # TODO: not shuffle one!

    newTrialSequence.append(
        generateSingleTrial(utilityTrial['quiting'], isUtility=True))
    return newTrialSequence


def generatePlaylist(paradigm):
    """
    Return a playlist.

    playlist[
        session{
            session_name,
            trial_sequence[...]
                }
            ]
        }
    ]
    """
    playlist = []
    for _ in range(paradigm['loop'] or 1):
        newSession = {
            'session_name': paradigm['session_name'],
            'trial_sequence': generateTrialSequence(paradigm)}
        playlist.append(newSession)
    return playlist
