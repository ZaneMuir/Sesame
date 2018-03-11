"""using pyglet to visualize sitmuli, in 60hz."""

import pyglet
from pyglet.window import key
from pyglet import app

import controller
import time
import os
import json
import logging
logger = logging.getLogger(__name__)

this_image = None
timer = 0
start_time = 0
film = []
colormap_copy = []
this_trial = {'color_sequence': []}
trial_count = 0
filmString = ""
actualFilm = []


def makeFilm(paradigm):
    """Reformat stim sequence for pyglet usage."""
    film = []
    rawFilm = controller.generatePlaylist(paradigm)
    # TODO: store raw film information into database
    for each_session in rawFilm:
        for each_trial in each_session['trial_sequence']:
            for each_color in each_trial['color_sequence']:
                film.append(each_color)
    logger.debug("Film made: " + film.__str__())
    return film


def makeFilm_reverse(paradigm):
    """Reformat stim sequence for pyglet usage, in reverse order."""
    global filmString
    rawFilm = controller.generatePlaylist(paradigm)

    # store raw film information into database
    filmString = json.dumps(rawFilm)

    for each_session in rawFilm:
        for each_trial in each_session['trial_sequence']:
            each_trial['color_sequence'].reverse()
        each_session['trial_sequence'].reverse()
    rawFilm.reverse()

    logger.debug("Film made: " + rawFilm.__str__())
    return rawFilm


def flick(dt):
    """Flicker for makeFilm()."""
    global timer, start_time, film, this_image, colormap_copy

    if time.time() - start_time > timer:
        colorname, step = film.pop()
        logger.debug(colorname+', step: '+str(step))
        this_image = colormap_copy[colorname]
        timer += step


def flick_reverse(dt):
    """Flicker for makeFilm_reverse()."""
    global timer, start_time, film, this_image, colormap_copy, this_trial
    global trial_count, actualFilm

    # FIXME: too complex.
    if time.time() - start_time > timer:
        try:
            colorname, step = this_trial['color_sequence'].pop()
        except IndexError:
            try:
                this_trial = film[-1]['trial_sequence'].pop()
            except IndexError:
                try:
                    film.pop()
                    if len(film) == 0:
                        timer += 9999
                        logger.warn("all session done. Press 'Q' to exit.")
                        return
                except IndexError:
                    timer += 9999
                    logger.warn("all session done. Press 'Q' to exit.")
                    return
                trial_count = len(film[-1]['trial_sequence']) - 2
                this_trial = film[-1]['trial_sequence'].pop()

            colorname, step = this_trial['color_sequence'].pop()
            logger.info('{left}/{total}'.format(
                left=trial_count-len(film[-1]['trial_sequence']) + 1,
                total=trial_count)+':'+this_trial['name'])

        actualFilm.append((colorname, step))
        this_image = colormap_copy[colorname]
        timer += step


def storeDataIntoFile(dataToStore, dir_path="./recording", prefix=False):
    """Store data before quiting."""
    global start_time

    if not prefix:
        prefix = time.strftime("%y%m%d_%H%M_{count}.data")
    prefix = os.path.join(dir_path, prefix)
    counter = 0
    while os.path.isfile(prefix.format(count=counter)):
        counter += 1

    with open(prefix.format(count=counter), 'w') as output:
        output.write(dataToStore)
        output.write("\n")
        output.write(start_time.__str__())


def start(colormap, paradigm):
    """Pyglet.app in loop."""
    global this_image, start_time, film, colormap_copy, trial_count

    # TODO: window setups, esp. for fullscreen.
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()

    '''for screen in display.get_screens():
    print screen
    window = pyglet.window.Window()
    window.on_draw = on_draw

    window.set_fullscreen(screen=screen)'''

    colormap_copy = colormap
    fps_display = pyglet.clock.ClockDisplay()

    film = makeFilm_reverse(paradigm)
    # film = makeFilm(paradigm).reverse()
    trial_count = len(film[-1]['trial_sequence']) - 2
    controller = pyglet.window.Window()
    windows = [pyglet.window.Window() for _ in range(5)]

    @controller.event
    def on_key_press(symbol, modifier):
        if symbol == key.ESCAPE or symbol == key.Q:
            # TODO: quitting in the middle way.
            storeDataIntoFile(filmString)
            storeDataIntoFile(
                actualFilm.__str__(),
                prefix=time.strftime("actual_%y%m%d_%H%M_{count}.data"))

            exit(0)

    @controller.event
    def on_draw():
        global this_image
        controller.clear()
        this_image.blit(0, 0)  # QUESTION: do we need a larger image?
        fps_display.draw()

    def drawer(this):
        def temp():
            global this_image
            this.clear()
            this_image.blit(0, 0)
        return temp

    for item in windows:
        item.on_draw = drawer(item)

    start_time = time.time()
    pyglet.clock.schedule(flick_reverse)
    try:
        for index in range(5):
            windows[index].set_fullscreen(screen=screens[index+1])
    except IndexError:
        pass
    # pyglet.clock.schedule(flick)
    app.run()
