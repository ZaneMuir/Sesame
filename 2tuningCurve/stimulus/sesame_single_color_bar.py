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


def flick(dt):
    """Flicker for makeFilm()."""
    global timer, current_color_name, playlist, color_cursor, start_time
    global trialName, subjectName

    if elapsed() > timer:
        if color_cursor % 2 == 0:
            current_color_name = playlist[color_cursor//2 % len(playlist)]
            color_cursor += 1
            storeDataIntoFile(
                "{start},{color}".format(start=elapsed(),
                                         color=current_color_name),
                prefix=subjectName,
                name=trialName)
            timer += 1
            logger.info("{round}:{trial}/{total}:{color}".format(
                round=color_cursor // 2 // len(playlist),
                trial=color_cursor // 2 % len(playlist),
                total=len(playlist),
                color=current_color_name
            ))
        else:
            current_color_name = 'black'
            color_cursor += 1
            timer += 4
            logger.debug(current_color_name+', until: '+str(timer))


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
            output.write("startstamp,colorname\n")
            output.write(dataToStore)
            output.write("\n")


def start(subject, trial, windowN):
    """Pyglet.app in loop."""
    global start_time, trialName, subjectName
    trialName = trial
    subjectName = subject
    # TODO: window setups, esp. for fullscreen.
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
        global current_color_name, colormap
        controller.clear()
        if current_color_name is "black":
            colormap['black'].blit(0, 0)
        else:
            colormap['white'].blit(0, 0)
        fps_display.draw()

    def drawer(this):
        def temp():
            global current_color_name, colormap
            this.clear()
            colormap[current_color_name].blit(0, 0)
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
    muskmap = cf.generateGradientMusk()  # TODO
    colormap = cf.getPygeltColorMaps(32)
    playlist = [name for name in colormap.keys()
                if name != "black" and name != "white" and
                name[0] in arguments['--mode']]
    random.shuffle(playlist)
    color_cursor = 0
    start_time = 0
    trialName = "demo"
    subjectName = "ts0"

    start(
        arguments['SUBJECT'],
        arguments['--mode'],
        int(arguments['--window']))
