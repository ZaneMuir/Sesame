"""trival operations."""

from pyglet.image import SolidColorImagePattern, ImageData
import numpy as np
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


def generatePygletGrating(grating, height=1080, width=1440,
                          L=50, theta=0, title=""):
    """Generate image with a given function."""
    actual_width = int(width+4*L*np.cos(theta)) + 1
    actual_height = int(height+4*L*np.sin(theta)) + 1

    map_dir = os.path.join("map", "{prefix}_{p1}_{p2}_{p3}_{p4}".format(
        prefix=title, p1=height, p2=width, p3=int(L), p4=int(theta/np.pi*180)))
    if os.path.isfile(map_dir):
        logger.debug("reading map")
        with open(map_dir, 'rb') as mapfile:
            data = mapfile.read()
        unit_map = ImageData(width=actual_width, height=actual_height,
                             data=data, format='RGBA',
                             pitch=actual_width*4)
    else:
        logger.debug("generating map")
        datamap = np.zeros((actual_height, actual_width, 4), dtype=np.int8)
        for x in range(actual_height):
            for y in range(actual_width):
                datamap[x, y] = grating(x, y)

        with open(map_dir, "wb") as mapfile:
            mapfile.write(datamap.tobytes())

        unit_map = ImageData(width=actual_width, height=actual_height,
                             data=datamap.tobytes(), format='RGBA',
                             pitch=actual_width*4)

    logger.debug("image generated: "+unit_map.__str__())
    colormap = {}
    source = [("white", (255, 255, 255)), ("black", (0, 0, 0))]
    for name, array in source:
        r, g, b = [i if i < 256 else 255 for i in array]
        a = 255
        colormap[name] = (SolidColorImagePattern((r, g, b, a)).create_image(
            width=actual_width, height=actual_height), 0)

    return unit_map, colormap


def generateGradientMusk(height=1080, width=1440, musk_seq=[(0, 0xff, 0x00)],
                         title=""):
    musks = {}
    for (theta, head, tail) in musk_seq:
        musk_name = "{prefix}_{width}_{height}_{setting}_{ori}".format(
            prefix=title, width=width, height=height,
            setting=hex(head)[2:]+hex(tail)[2:], ori=str(int(theta/np.pi*180)))
        if os.path.isfile(os.path.join("map", musk_name)):
            logger.debug("reading musk map: "+musk_name)
            with open(os.path.join("map", musk_name), 'rb') as mapfile:
                data = mapfile.read()
            unit_map = ImageData(width=width, height=height,
                                 data=data, format='RGBA',
                                 pitch=width*4)
        else:
            logger.debug("generating map: "+musk_name)
            datamap = np.zeros((height, width, 4), dtype=np.int8)
            for x in range(height):
                for y in range(width):
                    datamap[x, y] = (0, 0, 0, int(head-(np.cos(theta)*x+np.sin(theta)*y)/
                                     (np.cos(theta)*width+np.sin(theta)*height)*
                                     (head-tail)))
            with open(os.path.join("map", musk_name), "wb") as mapfile:
                mapfile.write(datamap.tobytes())

            unit_map = ImageData(width=width, height=height,
                                 data=datamap.tobytes(), format='RGBA',
                                 pitch=width*4)

            logger.debug("image generated: "+unit_map.__str__())
        musks[str(int(theta/np.pi*180))] = unit_map
    return musks


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(generateGradientMusk(musk_seq=[
        (0, 0xff, 0x00), (np.pi/2, 0xff, 0x00),
        (np.pi, 0xff, 0x00), (3*np.pi/2, 0xff, 0x00)],
        title="single_color_bar"))
