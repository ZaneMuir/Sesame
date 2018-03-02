"""using pyglet to visualize sitmuli, in 60hz."""

import pyglet
from pyglet.window import key
from pyglet import app

import controller
import time
import logging
logger = logging.getLogger(__name__)

this_image = None
timer = 0
start_time = 0
film = []
colormap_copy = []
this_trial = {'color_sequence': []}
trial_count = 0


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
    # film = []
    rawFilm = controller.generatePlaylist(paradigm)

    # TODO: store raw film information into database

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
    global trial_count

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

        this_image = colormap_copy[colorname]
        timer += step


def start(colormap, paradigm):
    """Pyglet.app in loop."""
    global this_image, start_time, film, colormap_copy, trial_count

    # TODO: widow setups, esp. for fullscreen.
    window = pyglet.window.Window(width=640, height=480)

    colormap_copy = colormap
    fps_display = pyglet.clock.ClockDisplay()

    film = makeFilm_reverse(paradigm)
    # film = makeFilm(paradigm).reverse()
    trial_count = len(film[-1]['trial_sequence']) - 2

    @window.event
    def on_key_press(symbol, modifier):
        if symbol == key.ESCAPE or symbol == key.Q:
            # TODO: quitting in the middle way.
            exit(0)

    @window.event
    def on_draw():
        global this_image
        window.clear()
        this_image.blit(0, 0)
        fps_display.draw()

    start_time = time.time()
    pyglet.clock.schedule(flick_reverse)

    # pyglet.clock.schedule(flick)
    app.run()
