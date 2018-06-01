#!/usr/bin/env python2
from psychopy import visual, core, event  # import some libraries from PsychoPy
import time
import logging
logger = logging.getLogger(__name__)
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

black = (0,0,0)
white = (1,1,1)
gray = (0.5,0.5,0.5)

ratio = 1


def shuffle_pos():
    #return (-20-random.random()*60, -20-random.random()*60)
	return (35,35)

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
    print(screen_width, screen_height)

    controller = visual.Window([200, 200], screen=0, pos=(10,500), monitor="DetectMonitor", color=(0.1,0.1,0.1), colorSpace='rgb')

    if len(screens) > 1:
        player = [visual.Window((1024,1280), monitor="PHENOSYS", screen=i, fullscr=True) for i in windowN]
    else:
        player = [visual.Window([screen_width, screen_height], 
                           monitor="DetectMonitor", screen=0, fullscr=False, unit='cm')]

    #=======stimulus========

    indicator = visual.Rect(win=controller, width=20, height=20, 
        pos=(0, 0), fillColor=black, fillColorSpace='rgb')

    background_gray = visual.Rect(win=controller, width=20, height=20,
                                  pos=(0, 0), fillColor=(0,0,0), fillColorSpace='rgb')
    
    background_grating = [visual.GratingStim(
        win=item, mask=None, size=200, pos=(0, 0), sf=0.1, tex='sqr') for item in player]
    salience_stim = visual.Circle(
        win=player[-1], radius=6, pos=[0, 0], fillColor=(0.1, 0.7, 0.9), fillColorSpace='rgb')

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
        logger.info("stim:"+str(is_stimulus_show))
        newPos = shuffle_pos()
        storeDataIntoFile(checker.getTime(), str(is_stimulus_show), 
                          lag=newPos, name=sessionName)
        salience_stim.pos = newPos
        while timer.getTime() < 0:
            [item.setPhase(0.1, '+') for item in background_grating]
            [item.draw() for item in background_grating]
            if is_stimulus_show and (-2 < timer.getTime() < -1):
                salience_stim.draw()
            indicator.draw()

            [item.flip() for item in player]
            controller.flip()
            event.clearEvents()

        #=====low======
        timer.add(low_time)
        indicator.fillColor = (0,0,0)
        while timer.getTime() < 0:
            background_gray.draw()
            indicator.draw()

            controller.flip()
            [item.flip() for item in player]
            event.clearEvents()


    #cleanup
    mywin.close()
    core.quit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start()
