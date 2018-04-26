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


def _up(shiftt): return 50 + 50 * shiftt


def _down(shiftt): return 255 - 50 * shiftt


_stim_seq = [
    ("green", _down , "green_down"),
    ("blue", _up , "blue_up")
]

main(_colors, _stim_seq, initial_wait=2, 
     high_duration=4, low_duration=4)
