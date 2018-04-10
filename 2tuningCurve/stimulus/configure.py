"""trival operations."""

from pyglet.image import SolidColorImagePattern, ImageData
import logging
import os
logger = logging.getLogger(__name__)


def generateColorMapName(step):
    cmap = []

    n = int(256/step)
    cmap.extend([("G"+str(i+1), (0, (i+1)*step, 0)) for i in range(n)])
    cmap.extend([("B"+str(i+1), (0, 0, (i+1)*step)) for i in range(n)])
    cmap.extend([("L"+str(i+1)+"#"+str(j+1), (0, (i+1)*step, (j+1)*step))
                 for i in range(n) for j in range(n)])
    return cmap


def getPygeltColorMaps(step, height=1080, width=1440, suffix=""):
    """Return colormap in pyglet.image."""

    colormap = {}
    source = generateColorMapName(step)
    for name, array in source:
        r, g, b = [i if i < 256 else 255 for i in array]
        a = 255
        thename = name+suffix
        colormap[thename] = SolidColorImagePattern((r, g, b, a)).create_image(
            width=width, height=height)

    source = [("white", (255, 255, 255)), ("black", (0, 0, 0))]
    for name, array in source:
        r, g, b = [i if i < 256 else 255 for i in array]
        a = 255
        colormap[name] = SolidColorImagePattern((r, g, b, a)).create_image(
            width=1280, height=1080)

    logger.debug("generate colors: " + colormap.keys().__str__())
    return colormap


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    pass
