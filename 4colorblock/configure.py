"""trival operations."""

import pyglet
import logging
logger = logging.getLogger(__name__)
import os
try:
    import numpy2 as np
except ModuleNotFoundError:
    import math as np

    

def getPygletColorMap(colordict, height=1080, width=1440, suffix=""):
    """Return colormap in pyglet.image.
    the colordict should be {colorname:(r,g,b,a)}
    """
    colormap = {}
    for (name, pattern) in colordict.items():
        r,g,b=pattern
        _temp = pyglet.image.SolidColorImagePattern((r,g,b,255))
        colormap[name] = _temp.create_image(width=width, height=height)
    
    return colormap


def createColorMap(pattern, alpha=255, height=1080, width=1440, suffix=""):
    r,g,b=pattern
    # print(r, g, b)
    _temp = pyglet.image.SolidColorImagePattern(
        (r*alpha//255, g*alpha//255, b*alpha//255, 255)).create_image(width=width, height=height)
    return _temp

def createLuminanceMap(L, height=1080, width=1440):
    _data = np.ones(height*width, dtype='uint8') * int(L)
    _buffer = pyglet.image.ImageData(width=width, height=height, 
                                     data=_data.tobytes(), format='A',
                                     pitch=width)
    return _buffer

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    pass
