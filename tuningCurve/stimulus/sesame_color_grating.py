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

screen_width = 1
screen_height = 1
x_pos = 0
y_pos = 0
x_speed = 0
y_speed = 0
ori = ''


def update_pos(ori, dt=0, reset=False):
    global x_pos, y_pos, x_speed, y_speed, screen_width, screen_height
    if ori == 'h':
        x_pos = 0 if reset else x_pos + x_speed*dt
    elif ori == 'H':
        x_pos = screen_width if reset else x_pos - x_speed*dt
    elif ori == 'v':
        y_pos = 0 if reset else y_pos + y_speed*dt
    elif ori == 'V':
        y_pos = screen_height if reset else y_pos - y_speed*dt
    else:
        pass


def flick(dt):
    """Flicker for makeFilm()."""
    global timer, current_color_name, playlist, color_cursor, start_time
    global trialName, subjectName, screen_width, screen_height, x_pos, y_pos
    global moving_speed, sleep_time, x_speed, y_speed, ori

    update_pos(ori, dt)

    if elapsed() > timer:
        if color_cursor % 2 == 0:
            current_color_name, ori = playlist[color_cursor//2 % len(playlist)]
            color_cursor += 1
            storeDataIntoFile(
                "{start},{color}".format(start=elapsed(),
                                         color=current_color_name),
                prefix=subjectName,
                name=trialName)
            timer += moving_speed
            update_pos(ori, reset=True)
            logger.info("{round}:{trial}/{total}:{color}".format(
                round=color_cursor // 2 // len(playlist),
                trial=color_cursor // 2 % len(playlist),
                total=len(playlist),
                color=current_color_name
            ))
        else:
            ori = ''
            current_color_name = 'black'
            color_cursor += 1
            timer += sleep_time
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
    global start_time, trialName, subjectName, screen_width, screen_height
    global x_speed, y_speed, moving_speed
    trialName = trial
    subjectName = subject
    # TODO: window setups, esp. for fullscreen.
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    fps_display = pyglet.clock.ClockDisplay()

    screen_width = screens[-1].width
    screen_height = screens[-1].height
    x_speed = screen_width / moving_speed
    y_speed = screen_height / moving_speed

    # film = makeFilm(paradigm).reverse()
    controller = pyglet.window.Window()
    windows = [pyglet.window.Window(1440, 900) for _ in range(windowN)]

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
            global current_color_name, colormap, x_pos, y_pos
            this.clear()
            colormap[current_color_name].blit(x_pos, y_pos)
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
        --window=WINDOWN        # number of secondary screeens [default: 1]
        --session=TEST          # test name [default: demo]
        --mode=MODE             # stimulus mode [default: GB]
        --direction=DIRECT      # grate direction [default: vh]
        --gratingwidth=WIDTH    # width of grate [default: 50]
        --speed=SPEED           # grating moving speed [default: 2]
        --sleep=SLEEP           # gap time [default: 3]
    """.format(version=__version__)
    from docopt import docopt
    arguments = docopt(__doc__, version=__version__)

    if arguments['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    current_color_name = "black"
    timer = 2

    colormap = {}
    if 'v' in arguments['--direction']:
        colormap.update(cf.getPygeltColorMaps(32,
                        height=int(arguments['--gratingwidth']),
                        suffix='v'))
    if 'h' in arguments['--direction']:
        colormap.update(cf.getPygeltColorMaps(32,
                        width=int(arguments['--gratingwidth']),
                        suffix='h'))
    if 'V' in arguments['--direction']:
        colormap.update(cf.getPygeltColorMaps(32,
                        height=int(arguments['--gratingwidth']),
                        suffix='V'))
    if 'H' in arguments['--direction']:
        colormap.update(cf.getPygeltColorMaps(32,
                        width=int(arguments['--gratingwidth']),
                        suffix='H'))

    playlist = [(name, name[-1]) for name in colormap.keys()
                if name != "black" and name != "white" and
                name[0] in arguments['--mode']]
    random.shuffle(playlist)
    color_cursor = 0
    start_time = 0
    trialName = "demo"
    subjectName = "ts0"
    moving_speed = float(arguments['--speed'])
    sleep_time = float(arguments['--sleep'])

    start(
        arguments['SUBJECT'],
        arguments['--mode'],
        int(arguments['--window']))
