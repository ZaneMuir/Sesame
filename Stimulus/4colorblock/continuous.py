from sesame_tuning_curve import main
import logging
logging.basicConfig(level=logging.INFO)

_colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "red": (255, 0, 0)
}


def _up_linear(shiftt): return 50 + 50 * shiftt


def _down_linear(shiftt): return 255 - 50 * shiftt


_stim_seq = [
    ("green", _down_linear , "green_down"),
    ("blue", _up_linear , "blue_up")
]


def start_experiment(subject, suffix, windown, initialwait, high, low):
    main(_colors, _stim_seq, initial_wait=initialwait,
         high_duration=high, low_duration=low,
         subject=subject, suffix=suffix, window_num=windown)
