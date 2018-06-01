from docopt import docopt
from sesame_player import main as player
import logging
logging.basicConfig(level=logging.INFO)

__usage__ = """
    V1RF

    Usage:
        V1RF.py [options] SESSION

    Options:
        --initial=INITIAL     # inital waiting time [default: 30]
        --lowtime=LOW         # off time length [default: 1]
        --velocity=VELOCITY   # grating moving speed [default: 200]
        --barwidth=BARW       # bar width [default: 50]
"""

arguments = docopt(__usage__)

seq = [
    ("0", 0),
    ("45", 45),
    ("90", 90),
    ("135", 135),
    ("180", 180),
    ("225", 225),
    ("270", 270),
    ("315", 315)]

sessionName = arguments['SESSION']
velocity = int(arguments['--velocity'])
low_time = int(arguments['--lowtime'])
inital_wait = int(arguments['--initial'])

bar_width = int(arguments["--barwidth"])
bar_color = (255,255,255,255)

player(sessionName, seq, velocity, low_time,
       bar_width, bar_color, inital_wait)
