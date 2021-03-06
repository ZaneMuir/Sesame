"""using pyglet to visualize sitmuli, in 60hz."""

import configure as cf

import pyglet
from pyglet.window import key
from pyglet import app
try:
    from numpy import cos, sin
except ModuleNotFoundError:
    from math import cos, sin
import time
import os
import logging
import random
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if sys.platform == "win32":
    def elapsed():
        """In windows, clock is better."""
        return time.clock()
else:
    def elapsed():
        """In other systems, time is used."""
        global start_time
        return time.time() - start_time

default_color_name = 'gray'


def update_pos(ori, dt=0, reset=False, T=50):
    """Update position in each tick."""
    global x_pos, y_pos, speed, screen_width, screen_height, setoff_x, setoff_y
    if reset:
        x_pos = -setoff_x
        y_pos = -setoff_y
        logging.debug("reset pos to: "+str(x_pos)+", "+str(y_pos))
    elif x_pos > 0 or y_pos > 0:
        x_pos = -setoff_x + speed * cos(ori) * dt
        y_pos = -setoff_y + speed * sin(ori) * dt
        logging.debug("reset pos to: "+str(x_pos)+", "+str(y_pos))
    else:
        x_pos += speed * cos(ori) * dt
        y_pos += speed * sin(ori) * dt
        logging.debug("new pos: "+str(x_pos)+", "+str(y_pos))


def flick(dt):
    """Flicker for makeFilm()."""
    global timer, current_color_name, playlist, stim_cursor, start_time
    global trialName, subjectName, screen_width, screen_height, x_pos, y_pos
    global sleep_time, speed, ori, colormap, setoff_x, setoff_y

    update_pos(ori, dt)

    if elapsed() > timer:
        current_color_name, ori, L, speed, stim_duration = \
                playlist[stim_cursor//2 % len(playlist)]
        stim_cursor += 1
        setoff_x = L*cos(ori)
        setoff_y = L*sin(ori)
        x_pos = -setoff_x
        y_pos = -setoff_y
        if stim_cursor % 2 == 0:
            storeDataIntoFile(
                "{start},{color}".format(start=elapsed(),
                                         color=current_color_name),
                prefix=subjectName,
                name=trialName)
            timer += stim_duration
            update_pos(ori, reset=True)
            logger.info("{round}:{trial}/{total}:{color}".format(
                round=stim_cursor // 2 // len(playlist),
                trial=stim_cursor // 2 % len(playlist),
                total=len(playlist),
                color=current_color_name
            ))
        else:
            ori = 0
            speed = 0
            current_color_name = default_color_name
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
            output.write("time,marker\n")
            output.write(dataToStore)
            output.write("\n")


def start(subject, trial, windowN):
    """Pyglet.app in loop."""
    global start_time, trialName, subjectName, screen_width, screen_height

    trialName = trial
    subjectName = subject
    # TODO: window setups, esp. for fullscreen.
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    fps_display = pyglet.clock.ClockDisplay()

    screen_width = screens[-1].width
    screen_height = screens[-1].height

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
        global current_color_name
        controller.clear()
        if current_color_name == default_color_name:
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


def movingGrate(grating_dict,  # Dict{name: (grating, theta, L, moving_speed)}
                subject="", suffix="", window_num=1,
                high_duration=5, low_duration=5,
                initial_wait=5, inital_color=default_color_name,
                stim_seq=None, shuffle=False):
    """Portal function."""
    global current_color_name, timer, colormap
    global playlist, stim_cursor
    global x_pos, y_pos, speed, ori
    global sleep_time, setoff_x, setoff_y

    current_color_name = inital_color
    timer = initial_wait

    pre_playlist = stim_seq or ['white']

    default_map = cf.generatePygletBWMap()
    colormap = {}

    for (key, (grating, theta, L, moving_speed)) in grating_dict.items():
        themap = cf.generatePygletGrating(grating, L=L, theta=theta, title=key)
        colormap[key] = themap
    colormap.update(default_map)

    playlist = []
    for name in pre_playlist:
        try:
            theta, L, moving_speed = grating_dict[name][1:]
        except KeyError:
            theta, L, moving_speed = 0, 0, 0
        playlist.append((name, theta, L, moving_speed, high_duration))

    if shuffle:
        random.shuffle(playlist)

    stim_cursor = 0
    first_stim = playlist[0]
    setoff_x = first_stim[2]*cos(first_stim[1])
    setoff_y = first_stim[2]*sin(first_stim[1])
    x_pos = -setoff_x
    y_pos = -setoff_y
    ori = first_stim[1]
    sleep_time = low_duration
    speed = 0

    start(subject, suffix, window_num)


if __name__ == '__main__':
    pass
    # TODO: add layers.
