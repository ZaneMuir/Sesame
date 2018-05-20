import pyglet
from pyglet.window import key
from pyglet import app
import sesame_generator as gen
import time
import os
import logging
# import random
logger = logging.getLogger(__name__)
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

from math import cos, sin, pi, sqrt
def sign(x):
    if x > 1e-3:
        return 1
    elif x < -1e-3:
        return -1
    else:
        return 0


start_time = 0
is_stimulus_show = False
indicator_map = None
grating_v = 0  # velocity
off_time = 0   # low time in seconds
timer = 0

current_idx = -1   # current index point to the stimulus in mapping_seq
mapping_seq = []  # [(name, direction)]
the_bar = None
screen_size = (0,0)  # width,height

sessionName = ""
counter = 0

def flick(dt):
    # TODO: shuffle the sequence?
    global is_stimulus_show
    global grating_v, counter
    global off_time, timer, sessionName
    global current_idx, mapping_seq, the_bar, screen_size

    if elapsed() > timer and not is_stimulus_show:
        current_idx = (current_idx + 1) % len(mapping_seq)
        name, ori = mapping_seq[current_idx]

        x_prime = (1 - sign(cos(ori/180*pi))) * 0.5 * screen_size[0]
        y_prime = (1 - sign(sin(ori/180*pi))) * 0.5 * screen_size[1]

        the_bar.x = x_prime + sin(ori/180*pi) * the_bar.height / 2
        the_bar.y = y_prime - cos(ori/180*pi) * the_bar.height / 2
        the_bar.rotation = -ori

        is_stimulus_show = True

        total_length = screen_size[0] / cos(ori/180*pi) if abs(
            cos(ori/180*pi)) > 1e-3 else screen_size[1] / sin(ori/180*pi)

        lag = abs(total_length) / grating_v
        storeDataIntoFile(elapsed(), name, lag, sessionName)
        timer += lag


        loop = int(counter / len(mapping_seq))
        num = counter % len(mapping_seq) + 1
        logger.info("{round}:{num}/{total}:{name}-{lag}".format(round=loop, num=num,
                                                          total=len(mapping_seq), name=name,
                                                          lag=lag))
        counter += 1

    elif elapsed() > timer and is_stimulus_show:
        is_stimulus_show = False
        timer += off_time
        storeDataIntoFile(elapsed(), "OFF", sessionName)

    if is_stimulus_show:
        ori = - the_bar.rotation
        the_bar.x += grating_v * cos(ori/180*pi) * dt
        the_bar.y += grating_v * sin(ori/180*pi) * dt


def storeDataIntoFile(_time, marker, lag=0, name="", _prefix="", _dir="recording"):
    filename = os.path.join(_dir, _prefix+time.strftime("%y%m%d_")+name+".csv")
    if not os.path.isfile(filename):
        with open(filename, "w") as output:
            output.write("time,marker,lag")
            logger.debug("write new csv file: "+filename)

    with open(filename, "a") as output:
        entry = "\n{time},{marker},{lag}".format(time=_time,marker=marker,lag=lag)
        output.write(entry)

# ==============================================================

def start(bar_width, bar_color, windowN=1):
    global indicator_map, screen_size, sessionName, start_time, the_bar
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    fps_display = pyglet.clock.ClockDisplay()

    screen_width = screens[-1].width
    screen_height = screens[-1].height

    screen_size = (screen_width, screen_height)
    indicator_map = gen.getIndicatorMap(screen_width, screen_height)
    bar_height = screen_width * 2
    the_bar = gen.getSingleBar(bar_width, int(bar_height), bar_color)

    controller = pyglet.window.Window()
    windows = [pyglet.window.Window() for _ in range(windowN)]

    @controller.event
    def on_key_press(symbol, modifier):
        "quiting sequence"
        if symbol == key.ESCAPE or symbol == key.Q:
            storeDataIntoFile(time.time(), "QUIT", sessionName)
            exit(0)

    @controller.event
    def on_draw():
        "stimulus monitor"
        global is_stimulus_show, indicator_map

        controller.clear()
        if is_stimulus_show:
            indicator_map['white'].blit(0,0)
        else:
            indicator_map['black'].blit(0,0)
        fps_display.draw()

    # player drawer
    def drawer(screen):
        def temp():
            global mapping_seq, current_idx
            global indicator_map
            global is_stimulus_show
            screen.clear()
            indicator_map["gray"].blit(0, 0)
            if is_stimulus_show:
                the_bar.draw()
        return temp

    for item in windows:
        item.on_draw = drawer(item)

    # =========================================================
    start_time = time.time()  # absolute time of starting
    storeDataIntoFile(start_time, "START", sessionName)

    pyglet.clock.schedule(flick)
    for index in range(windowN):
        try:
            windows[index].set_fullscreen(screen=screens[index+1])
        except IndexError:
            windows[index].set_size(screen_width, screen_height)
            logger.warn("secondary screens not found.")

    app.run()

def main(session, seq, velocity, low_time, bar_width, bar_color, inital_wait=31):
    global sessionName, mapping_seq, grating_v, off_time, timer
    sessionName = session
    mapping_seq = seq
    grating_v = velocity
    off_time = low_time
    timer = inital_wait

    start(bar_width, bar_color)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    demo = [
        ("0",0),
        ("45",45),
        ("90",90),
        ("135",135),
        ("180",180),
        ("225",225),
        ("270",270),
        ("315",315)]
    main("demo", demo, 300, 1, 20, (255,255,255,255),1)
