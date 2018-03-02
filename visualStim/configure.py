"""trival operations."""

import json
import numpy as np
from pyglet.image import SolidColorImagePattern
import logging
logger = logging.getLogger(__name__)


def getColorMaps(colornamefile, screensize=(1920, 1080, 3)):
    """Return colormap in numpy.array."""
    with open(colornamefile, 'r') as f:
        content = f.read()

    colormap = {}
    for name, array in json.loads(content).items():
        colormap[name] = np.ones(screensize, dtype='uint8') * \
                         np.array(array, dtype='uint8')
    return colormap


def getPygeltColorMaps(colornamefile, screensize=(1920, 1080, 3)):
    """Return colormap in pyglet.image."""
    with open(colornamefile, 'r') as f:
        content = f.read()
    logger.debug("read colormap file: " + colornamefile)

    colormap = {}
    for name, array in json.loads(content).items():
        r, g, b = array
        a = 255
        colormap[name] = SolidColorImagePattern((r, g, b, a)).create_image(
            width=screensize[0], height=screensize[1])

    logger.debug("generate colors: " + colormap.keys().__str__())
    return colormap
