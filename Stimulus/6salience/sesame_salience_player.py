from psychopy import visual, core, event  # import some libraries from PsychoPy
import time
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
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# sessionName = 'demo'
# start_time = 1
# high_time = 5
# low_time = 5   # low time in seconds

basic_color = {
    'black': (-1, -1, -1),
    'white': (1, 1, 1),
    'gray': (0, 0, 0),
    'red': (1, 0, 0),
    'green': (0, 1, 0),
    'blue': (0, 0, 1)
}

# ratio = 0.8

# salience_size = 80


def storeDataIntoFile(_time, marker, lag='0.0', note='0.0', name="", _prefix="", stim="salience_", _dir="recording"):
    filename = os.path.join(
        _dir, _prefix+time.strftime("%y%m%d_"+stim)+name+".csv")
    if not os.path.isfile(filename):
        with open(filename, "w") as output:
            output.write("time,marker,lag,note")
            logger.debug("write new csv file: "+filename)

    with open(filename, "a") as output:
        entry = "\n{time},{marker},{lag},{note}".format(
            time=_time, marker=marker, lag=lag, note=note)
        output.write(entry)


#seq = [()]
def start(sessionName, background_stim_c, background_anim,
          salience_stim_c, salience_pos, salience_anim,
          windowN=[4, 5], start_time=1, high_time=5, low_time=5, ratio=1,
          reverse=False, reverse_anim=None):
    #=======windows=========
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    screen_width = screens[-1].width
    screen_height = screens[-1].height
    print("screen size:", screen_width, screen_height)

    controller = visual.Window([300, 300], screen=0, pos=(10, 500),
                               monitor="DetectMonitor", units='pix', color=basic_color['black'])

    if len(screens) > 1:
        player = [visual.Window([screen_width, screen_height],
                                monitor="PHENOSYS", color=basic_color['gray'], screen=i, fullscr=True, units='pix') for i in windowN]
    else:
        player = [visual.Window([600, 600],
                                monitor="PHENOSYS", color=basic_color['gray'], screen=0, fullscr=False, units='pix')]

    #=======stimulus========
    indicator = visual.Rect(win=controller, width=300, height=300,
                            pos=(0, 0), fillColor=basic_color['white'], fillColorSpace='rgb')

    background_stim = [background_stim_c(win=item, size=(screen_width, screen_height), pos=(0, 0)) for item in player]
    salience_stim = salience_stim_c(win=player[-1])

    #======initiation=======
    storeDataIntoFile(time.time(), 'START', name=sessionName)
    time.sleep(start_time)

    timer = core.Clock()
    checker = core.Clock()
    is_stimulus_show = False

    #======start============
    while True:
        #=====high=====
        timer.add(high_time)
        is_stimulus_show = random.random() <= ratio

        #logging
        newPos = salience_pos(screen_width, screen_height)
        print("salience:", is_stimulus_show, newPos)
        # logger.info("stim:"+str(is_stimulus_show)+' '+str(newPos))
        storeDataIntoFile(checker.getTime(), str(is_stimulus_show),
                          lag=newPos[0], note=newPos[1], name=sessionName)
        salience_stim.pos = newPos

        while timer.getTime() < 0:
            if reverse:
                reverse_anim(background_stim, salience_stim,
                             is_stimulus_show, timer.getTime())
            else:
                background_anim(background_stim)
                salience_anim(salience_stim, is_stimulus_show, timer.getTime())

            [item.flip() for item in player]

            indicator.draw()
            controller.flip()
            event.clearEvents()

        #=====low======
        if low_time == 0:
            continue
        timer.add(low_time)
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
