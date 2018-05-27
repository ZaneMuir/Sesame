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

green_down = [
    ("green", lambda _:255, "green_255"),
    ("green", lambda _:128, "green_128"),
    ("green", lambda _:64, "green_64"),
    ("green", lambda _:32, "green_32"),
    ("black", lambda _:0, "black"),
]

blue_up = [
    ("blue", lambda _:32, "blue_32"),
    ("blue", lambda _:64, "blue_64"),
    ("blue", lambda _:128, "blue_128"),
    ("blue", lambda _:255, "blue_255"),
]

_stim_seq = green_down + blue_up


def start_experiment(subject, suffix, windown, initialwait, high, low):
    main(_colors, _stim_seq, initial_wait=initialwait,
         high_duration=high, low_duration=low,
         subject=subject, suffix=suffix, window_num=windown, shuffle=True)
