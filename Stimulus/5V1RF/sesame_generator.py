import pyglet
import logging
logger = logging.getLogger(__name__)

def getIndicatorMap(width, height):
    colormap = {}
    indicators = {
            "black":(0,0,0,255),
            "white":(255,255,255,255),
            "gray":(127,127,127,255)}
    for (name, pattern) in indicators.items():
        _temp = pyglet.image.SolidColorImagePattern(pattern)
        colormap[name] = _temp.create_image(width=width, height=height)
    return colormap

def getSingleBar(bar_width, bar_height, bar_color):
    _temp = pyglet.image.SolidColorImagePattern(bar_color)
    _image = _temp.create_image(width=bar_width, height=bar_height)

    bar = pyglet.sprite.Sprite(_image)
    return bar
