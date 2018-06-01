# from psychopy import visual# import some libraries from PsychoPy
from psychopy.visual.grating import GratingStim
from psychopy.visual.circle import Circle
from psychopy.visual.rect import Rect
from docopt import docopt
from sesame_salience_player import start
import re
import random

__usage__ = '''
salience

Usage:
    salience.py [options] SESSION

Options:
    --backgroundStim=BACKSTIM   # background stimulus type, (grating|gray) [default: gray]
    --salienceStim=SALISTIM     # salience stimulus type,(circle_grating|circle_color) [default: circle_grating]
    --saliencePos=POS           # salience constant position, (#/#|random) [default: 0/0]
    --initial=WAIT              # initial wait [default: 5]
    --hightime=HIGH             # high time [default: 5]
    --lowtime=LOW               # low time [default: 5]
    --ratio=RATIO               # salience ratio [default: 1]
    --salienceSize=SIZE         # salience size [default: 160]
    --reverse                   # reverse the salience (under construction)
'''
arguments = docopt(__usage__)
# print(arguments)
# exit(0)

def background_grating(gratings):
    [item.setPhase(0.02, '+') for item in gratings]
    [item.draw() for item in gratings]


def background_color(gratings):
    # [item.setPhase(0.02, '+') for item in gratings]
    [item.draw() for item in gratings]


def salience_anim_color(salience, isshow, countdown):
    if salience and (-2 < countdown < -1):
        salience.draw()


def salience_anim_grating(salience, isshow, countdown):
    if salience and (-2 < countdown < -1):
        salience.setPhase(0.02, '+')
        salience.draw()


class background_grating(GratingStim):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.mask = 'circle'
        self.sf = 0.004
        self.tex='sqr'


class background_gray(Rect):
        # indicator = visual.Rect(win=controller, width=300, height=300,
        # pos=(0, 0), fillColor=black, fillColorSpace='rgb')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.mask = 'circle'
        self.fillColor = (0,0,0)
        self.fillColorSpace = 'rgb'
        self.width, self.height = self.size 


class salience_circle_grating(GratingStim):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mask = 'circle'
        self.sf = 0.004
        self.tex = 'sqr'
        self.ori = 90
        self.size = (int(arguments['--salienceSize']) * 2, int(arguments['--salienceSize']) * 2)
        self.pos = (0, 0)

class salience_circle_color(Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.mask = None
        # self.sf = 0.004
        # self.tex = 'sqr'
        self.radius = int(arguments['--salienceSize'])
        self.fillColor = (1,1,1)
        self.fillColorSpace = 'rgb'
        self.pos = (0, 0)


def shuffle_pos(width, height):
    return ((300 - int(arguments['--salienceSize'])) * random.random(), (300 - int(arguments['--salienceSize'])) * random.random())

if arguments['--saliencePos'] =='random':
    salience_pos = shuffle_pos
else:
    saliencePos = [float(i) for i in re.split('/', arguments['--saliencePos'])]
    salience_pos = lambda x, y: saliencePos


if arguments['--backgroundStim'] == 'grating':
    my_background = background_grating
    background_anim = background_grating
elif arguments['--backgroundStim'] == 'gray':
    my_background = background_gray
    background_anim = background_color
else:
    raise ValueError("unkown background stim type: "+arguments['--backgroundStim'])

if arguments['--salienceStim'] == 'circle_color':
    my_salience = salience_circle_color
    salience_anim = salience_anim_color
elif arguments['--salienceStim'] == 'circle_grating':
    my_salience = salience_circle_grating
    salience_anim = salience_anim_grating
else:
    raise ValueError("unkown salience stim type: "+arguments['--salienceStim'])



start(
    sessionName=arguments['SESSION'],
    background_stim_c=my_background, background_anim=background_anim,
    salience_stim_c=my_salience, salience_pos=salience_pos,
    salience_anim=salience_anim,
    start_time=float(arguments['--initial']), 
    high_time=float(arguments['--hightime']), 
    low_time=float(arguments['--lowtime']), 
    ratio=float(arguments['--ratio'])
)
