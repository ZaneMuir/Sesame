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
    'black':(-1, -1, -1),
    'white':(1, 1, 1),
    'gray':(0, 0, 0),
    'red':(1,0,0),
    'green':(0,1,0),
    'blue':(0,0,1)
}


def storeDataIntoFile(_time, marker, lag=0, name="", _prefix="", _dir="recording"):
    filename = os.path.join(_dir, _prefix+time.strftime("%y%m%d_")+name+".csv")
    if not os.path.isfile(filename):
        with open(filename, "w") as output:
            output.write("time,marker,lag")
            logger.debug("write new csv file: "+filename)

    with open(filename, "a") as output:
        entry = "\n{time},{marker},{lag}".format(
            time=_time, marker=marker, lag=lag)
        output.write(entry)


def start(windowN=[4, 5], grating_config=None, mode='8',
          sessionName='demo',
          start_time=1, high_time=5, low_time=5):
    #=======windows=========
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    screen_width = screens[-1].width
    screen_height = screens[-1].height
    print("screen size:", screen_width, screen_height)

    #=======display setting=========
    controller = visual.Window([300, 300], screen=0, pos=(10, 500),
                               monitor="DetectMonitor", units='pix', color=basic_color['black'])
    if len(screens) > 1:
        player = [visual.Window([screen_width, screen_height],
                                monitor="PHENOSYS", color=basic_color['gray'], screen=i, fullscr=True, units='pix') for i in windowN]
    else:
        player = [visual.Window([300, 300],
                                monitor="PHENOSYS", color=basic_color['gray'], screen=0, fullscr=False, units='pix')]

    #=======stimulus========
    indicator = visual.Rect(win=controller, width=300, height=300,
                            pos=(0, 0), fillColor=basic_color['white'], fillColorSpace='rgb')

    if grating_config == None:
        grating_config = {'sf': 0.004, 'tex':'sqr', 'speed': 0.02}
    grating = [visual.GratingStim(win=item, size=(screen_width, screen_height), pos=(0, 0), 
                                  sf=grating_config['sf'], tex=grating_config['tex']) for item in player] 

    if mode == '8':
        stim_ori = [item * 45 for item in range(8)]
    elif mode=='16':
        stim_ori = [item * 22.5 for item in range(8)]
    else:
        raise ArgumentError("unkown mode: "+str(mode))
    random.shuffle(stim_ori)

    #======initiation=======
    storeDataIntoFile(time.time(), 'START', name=sessionName)
    time.sleep(start_time)

    timer = core.Clock()
    checker = core.Clock()
    # is_stimulus_show = False
    index = 0

    #======start============
    while True:
        #=====high time=====
        timer.add(high_time)
        # is_stimulus_show = True

        #logging
        newOri = stim_ori[index % len(stim_ori)]
        print("stim:", newOri)
        index += 1
        # logger.info("stim:"+str(is_stimulus_show)+' '+str(newPos))
        storeDataIntoFile(checker.getTime(), str(newOri),
                          lag=high_time, name=sessionName)
        
        for item in grating:
            item.ori = newOri

        while timer.getTime() < 0:
            [item.setPhase(grating_config['speed'], '+') for item in grating]
            [item.draw() for item in grating]
            [item.flip() for item in player]

            indicator.draw()
            controller.flip()

            event.clearEvents()

        #=====low======
        timer.add(low_time)

        [item.flip() for item in player]
        controller.flip()

        event.clearEvents()

        while timer.getTime() < 0:
            pass
            # [item.draw() for item in background_gray]
            # indicator.draw()

            # controller.flip()
            # [item.flip() for item in player]
            # event.clearEvents()


if __name__ == '__main__':
    start(mode='16')
