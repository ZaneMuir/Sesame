"""using pyglet to visualize sitmuli, in 60hz."""

import configure as cf

import pyglet
from pyglet.window import key
from pyglet import app

import time
import os
import logging
import random
import sys
logger = logging.getLogger(__name__)

if sys.platform == "win32":
    def elapsed():
        return time.clock()
else:
    def elapsed():
        global start_time
        return time.time() - start_time

a_function = lambda x:x

timer = 0
stim_cursor = 0

def flick(dt):
    """Flicker for makeFilm()."""
    global current_color_name, playlist, stim_cursor, backgrounds, current_musk
    global trialName, subjectName, delay
    global timer, wake_time, sleep_time

    # update_luminance_musk()

    if elapsed() > timer:
        stim_cursor += 1
        delay = elapsed()
        if stim_cursor % 2 == 0:
            timer += wake_time
            _color = playlist[stim_cursor//2 % len(playlist) - 1][0]
            logger.info("{round}:{trial}/{total}:{color}".format(
                round=stim_cursor // 2 // len(playlist),
                trial=stim_cursor // 2 % len(playlist),
                total=len(playlist),
                color=playlist[stim_cursor//2 % len(playlist) - 1][2]
            ))
            if _color != backgrounds:
                storeDataIntoFile(
                    "{start},{color}".format(start=elapsed(),
                                            color=playlist[stim_cursor//2 % len(playlist) - 1][2]),
                    prefix=subjectName,
                    name=trialName)
        else:
            timer += sleep_time
            
    if stim_cursor % 2 == 0:
        # timer += wake_time
        current_color_name, _luminance, _ = playlist[stim_cursor//2 % len(
            playlist)-1]
        # current_musk = cf.createLuminanceMap(_luminance) 
        current_musk = int(_luminance(elapsed() - delay))
        # print(current_musk)
        # stim_cursor += 1
        # storeDataIntoFile(
        #     "{start},{color}".format(start=elapsed(),
        #                              color=current_color_name),
        #     prefix=subjectName,
        #     name=trialName)
    else:
        current_color_name = backgrounds
        # stim_cursor += 1
        # timer += sleep_time
        # logger.debug(current_color_name+', until: '+str(timer))


def storeDataIntoFile(dataToStore,
                      dir_path="./recording",
                      prefix="",
                      name=""):
    """Store data before quiting."""
    global timer

    filename = time.strftime("{prefix}_%y%m%d_{name}.csv")
    filename = filename.format(name=name, prefix=prefix)
    filename = os.path.join(dir_path, filename)

    if os.path.isfile(filename):
        with open(filename, "a") as output:
            output.write(dataToStore)
            output.write("\n")
    else:
        with open(filename, 'w') as output:
            output.write("time,marker\n")
            output.write(dataToStore)
            output.write("\n")


def start(subject, trial, windowN):
    """Pyglet.app in loop."""
    global start_time, trialName, subjectName
    trialName = trial
    subjectName = subject
    # window setups, esp. for fullscreen.
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    fps_display = pyglet.clock.ClockDisplay()

    # film = makeFilm(paradigm).reverse()
    controller = pyglet.window.Window()
    windows = [pyglet.window.Window() for _ in range(windowN)]

    @controller.event
    def on_key_press(symbol, modifier):
        if symbol == key.ESCAPE or symbol == key.Q:
            # quitting in the middle way.
            # storeDataIntoFile(filmString)
            storeDataIntoFile(
                "{startstamp},{colorname}".format(startstamp=time.time(),
                                                  colorname="QUIT"),
                prefix=subjectName,
                name=trialName)

            exit(0)

    @controller.event
    def on_draw():
        global current_color_name, colormap, backgrounds
        controller.clear()
        if current_color_name == backgrounds:
            colormap['black'].blit(0, 0)
        else:
            colormap['white'].blit(0, 0)
        fps_display.draw()

    def drawer(this):
        def temp():
            global colormap, current_musk, colordictmap, backgrounds
            this.clear()
            if current_color_name != backgrounds:
                # print(current_musk)
                cf.createColorMap(colordictmap[current_color_name], current_musk).blit(0,0)
            else:
                colormap[backgrounds].blit(0,0)
        return temp

    for item in windows:
        item.on_draw = drawer(item)

    start_time = time.time()
    storeDataIntoFile("{startstamp},{colorname}".format(startstamp=start_time,
                                                        colorname="START"),
                      prefix=subjectName,
                      name=trialName)

    pyglet.clock.schedule(flick)
    try:
        for index in range(windowN):
            windows[index].set_fullscreen(screen=screens[index+1])
    except IndexError:
        logger.warn("secondary screens not found.")
        pass
    # pyglet.clock.schedule(flick)
    app.run()


# grating_dict,  # Dict{name: (grating, theta, L, moving_speed)}
#                 subject = "", suffix = "", window_num = 1,
#                 high_duration = 5, low_duration = 5,
#                 initial_wait = 5, inital_color = default_color_name,
#                 stim_seq = None, shuffle = False

def main(colordict, stim_seq, window_num=1, mode="discrete",
         subject="test",  suffix="", high_duration = 2, low_duration=2,
         initial_wait = 60, initial_color="gray", background_color="gray",
         shuffle=False):
        
    global current_color_name, current_musk, colormap, colordictmap
    global timer, stim_cursor, sleep_time, wake_time, delay
    global backgrounds, playlist
    global on, off

    current_color_name = initial_color
    backgrounds = background_color
    timer = initial_wait
    colordictmap = colordict

    on = cf.createColorMap([255,255,255])
    off = cf.createColorMap([0, 0, 0])

    playlist = stim_seq or [("gray", 255)]  # (colorname, luminance)

    colormap = cf.getPygletColorMap(colordict)

    if shuffle:
        random.shuffle(playlist)

    stim_cursor = 1
    sleep_time = low_duration
    wake_time = high_duration
    current_musk = 255
    delay = initial_wait

    start(subject, suffix, window_num)


    


if __name__ == '__main__':
    __version__ = "v1.0-dev"
    __doc__ = """
    Sesame {version}

    Usage: sesame_tuning_curve.py [options] SUBJECT

    Options:
        --debug
        --window=WINDOWN    # number of secondary screeens [default: 1]
        --session=TEST      # test name [default: demo]
        --mode=MODE         # stimulus mode [default: GB]
    """.format(version=__version__)
    from docopt import docopt
    arguments = docopt(__doc__, version=__version__)

    if arguments['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    current_color_name = "black"
    timer = 10
    colormap = cf.getPygeltColorMaps(32)
    playlist = [name for name in colormap.keys()
                if name != "black" and name != "white" and
                name[0] in arguments['--mode']]
    random.shuffle(playlist)
    stim_cursor = 0
    start_time = 0
    trialName = "demo"
    subjectName = "ts0"

    start(
        arguments['SUBJECT'],
        arguments['--mode'],
        int(arguments['--window']))
