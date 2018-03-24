"""trival operations."""

import json
from pyglet.image import SolidColorImagePattern
import logging
logger = logging.getLogger(__name__)


def generateColorMapName(step):
    cmap = [("white", (255, 255, 255)),
            ("black", (0, 0, 0))]

    n = int(256/step)
    cmap.extend([("G"+str(i+1), (0, (i+1)*step, 0)) for i in range(n)])
    cmap.extend([("B"+str(i+1), (0, 0, (i+1)*step)) for i in range(n)])
    cmap.extend([("L"+str(i+1)+","+str(j+1), (0, (i+1)*step, (j+1)*step))
                 for i in range(n) for j in range(n)])

    return cmap


def getPygeltColorMaps(step, screensize=(1920, 1080, 3)):
    """Return colormap in pyglet.image."""

    colormap = {}
    for name, array in generateColorMapName(step):
        r, g, b = [i if i < 256 else 255 for i in array]
        a = 255
        colormap[name] = SolidColorImagePattern((r, g, b, a)).create_image(
            width=screensize[0], height=screensize[1])

    logger.debug("generate colors: " + colormap.keys().__str__())
    return colormap


if __name__ == '__main__':
    print(getPygeltColorMaps(32))
