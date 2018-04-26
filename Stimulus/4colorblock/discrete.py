from sesame_tuning_curve import main
import logging
logging.basicConfig(level=logging.INFO)

_colors = {
    "black":(0,0,0),
    "white":(255,255,255),
    "gray":(128,128,128),
    "green":(0,255,0),
    "blue":(0,0,255),
    "red":(255,0,0)
}

green_down = [
    ("green", lambda _:255, "green_255"),
    ("green", lambda _:128, "green_128"),
    ("green", lambda _:64, "green_64"),
    ("gray", lambda _:255, "gray"),
    ("gray", lambda _:255, "gray")
]

blue_up = [
    ("blue", lambda _:64, "blue_64"),
    ("blue", lambda _:128, "blue_128"),
    ("blue", lambda _:255, "blue_255"),
    ("gray", lambda _:255, "gray"),
    ("gray", lambda _:255, "gray")
]

_stim_seq = green_down + blue_up

main(_colors, _stim_seq, initial_wait=2)
