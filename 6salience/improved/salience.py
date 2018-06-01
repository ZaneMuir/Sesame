from psychopy import visual, core, event  # import some libraries from PsychoPy
import time
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
import os
import pyglet
import random
import sys
if sys.platform == "win32":
    def elapsed():
        """In windows, clock is better."""
        return time.clock()
else:
    def elapsed():
        """In other systems, time is used."""
        global start_time
        return time.time() - start_time

sessionName = 'demo'

start_time = 1
high_time = 5
low_time = 5   # low time in seconds

black = (-1,-1,-1)
white = (1,1,1)
gray = (0,0,0)

ratio = 0.8

salience_size = 80


def shuffle_pos(size):
    return ((- size[0]/2 + salience_size) * 0.9,
            (random.random() * 2 - 1) * (size[1]/2) * 0.8)

def storeDataIntoFile(_time, marker, lag=(0.0,0.0), name="", _prefix="", _dir="recording"):
    filename = os.path.join(_dir, _prefix+time.strftime("%y%m%d_")+name+".csv")
    if not os.path.isfile(filename):
        with open(filename, "w") as output:
            output.write("time,marker,x,y")
            logger.debug("write new csv file: "+filename)

    with open(filename, "a") as output:
        entry = "\n{time},{marker},{x},{y}".format(
            time=_time, marker=marker, x=lag[0], y=lag[1])
        output.write(entry)


#seq = [()]
def start(windowN=[4,5]):
    #=======windows=========
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    screen_width = screens[-1].width
    screen_height = screens[-1].height
    print("screen size:", screen_width, screen_height)

    controller = visual.Window([300, 300], screen=0, pos=(10, 500), 
                               monitor="DetectMonitor", units='pix', color=black)
    #TODO: controller background color into black.
    if len(screens) > 1:
        player = [visual.Window([screen_width, screen_height],
                                monitor="PHENOSYS", color=gray, screen=i, fullscr=True, units='pix') for i in windowN]
    else:
        player = [visual.Window([screen_width, screen_height], 
                                monitor="PHENOSYS", color=gray, screen=0, fullscr=False, units='pix')]

    #=======stimulus========

    indicator = visual.Rect(win=controller, width=300, height=300, 
        pos=(0, 0), fillColor=black, fillColorSpace='rgb')

    background_gray = [visual.Rect(win=item, width=screen_width, height=screen_height,
                       pos=(0, 0), fillColor=(0,0,0), fillColorSpace='rgb') for item in player]
    background_grating = [visual.GratingStim(
        win=item, mask=None, size=(screen_width, screen_height), pos=(0, 0), sf=0.004, tex='sqr') for item in player]
    salience_stim = visual.Circle(
        win=player[-1], radius=salience_size, pos=[-100, 0], fillColor=(0.1, 0.9, 0.7), fillColorSpace='rgb')

    #======initiation=======
    storeDataIntoFile(time.time(), 'START', name=sessionName)
    timer = core.Clock()
    checker = core.Clock()
    is_stimulus_show = False

    timer.add(start_time)
    while timer.getTime() < 0:
        pass
    
    #======start============
    while True:
        #=====high=====
        timer.add(high_time)
        is_stimulus_show = random.random() <= ratio
        indicator.fillColor = white
        #logging
        newPos = shuffle_pos((screen_width, screen_height))
        print("stim:", is_stimulus_show, newPos)
        # logger.info("stim:"+str(is_stimulus_show)+' '+str(newPos))
        storeDataIntoFile(checker.getTime(), str(is_stimulus_show), 
                          lag=newPos, name=sessionName)
        salience_stim.pos = newPos
        while timer.getTime() < 0:
            [item.setPhase(0.02, '+') for item in background_grating]
            [item.draw() for item in background_grating]
            if is_stimulus_show and (-2 < timer.getTime() < -1):
                salience_stim.draw()
            indicator.draw()

            [item.flip() for item in player]
            controller.flip()
            event.clearEvents()

        #=====low======
        timer.add(low_time)
        indicator.fillColor = black
        [item.draw() for item in background_gray]
        controller.flip()
        [item.flip() for item in player]
        event.clearEvents()

        while timer.getTime() < 0:
            pass
            # [item.draw() for item in background_gray]
            # indicator.draw()

            # controller.flip()
            # [item.flip() for item in player]
            # event.clearEvents()


    #cleanup
    mywin.close()
    core.quit()


if __name__ == '__main__':
    from docopt import docopt
    __usage__ = """
    salience

    Usage:
        salience.py [options] SESSION

    Options:
        -i INITIAL --initial=INITIAL     # initial waiting time [default: 30]
        -r RATIO --ratio=RATIO           # ratio of salience [default: 0.8]
    """

    arguments = docopt(__usage__)
    sessionName = arguments['SESSION']
    print(arguments)
    exit(0)

    start_time = int(arguments['--initial'])
    # high_time = 5
    # low_time = 5   # low time in seconds

    # black = (-1, -1, -1)
    # white = (1, 1, 1)
    # gray = (0, 0, 0)

    ratio = float(arguments['--ratio'])

    # salience_size = 80
    start()
