"""trival operations."""

from pyglet.image import SolidColorImagePattern, ImageData
import numpy as np
import logging
import os
logger = logging.getLogger(__name__)


def generatePygletGrating(grating, height=1080, width=1440,
                          L=50, theta=0, title=""):
    canvas_size = (width+2*L, height+2*L)  # width, height
    map_dir = os.path.join("map", "{prefix}_{p1}_{p2}_{p3}_{p4}".format(
        prefix=title, p1=height, p2=width, p3=int(L), p4=int(theta/np.pi*180)))

    if os.path.isfile(map_dir):
        logger.debug("reading map: "+title)
        with open(map_dir, 'rb') as mapfile:
            data = mapfile.read()
        unit_map = ImageData(width=canvas_size[0], height=canvas_size[1],
                             data=data, format='RGBA',
                             pitch=canvas_size[0]*4)
        return unit_map
    else:
        logger.debug("generating map: "+title)
        datamap = np.zeros((canvas_size[1], canvas_size[0], 4), dtype=np.int8)
        for x in range(canvas_size[0]):
            for y in range(canvas_size[1]):
                datamap[y, x] = grating(x, y)

        with open(map_dir, "wb") as mapfile:
            mapfile.write(datamap.tobytes())

        logger.debug("generating map: "+title)

        return ImageData(width=canvas_size[0], height=canvas_size[1],
                             data=datamap.tobytes(), format='RGBA',
                             pitch=canvas_size[0]*4)


def generatePygletBWMap(height=1080, width=1440, L=50):
    """Generate image with a given function."""
    colormap = {}
    source = [("white", (255, 255, 255, 255)), ("gray", (0, 0, 0, 255)),("black", (128, 128, 128, 255))]
    for name, array in source:
        r, g, b, a = array
        colormap[name] = SolidColorImagePattern((r, g, b, a)).create_image(
            width=width+2*L, height=height+2*L)

    return colormap  # {name: (image, speed)}


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(generateGradientMusk(musk_seq=[
        (0, 0xff, 0x00), (np.pi/2, 0xff, 0x00),
        (np.pi, 0xff, 0x00), (3*np.pi/2, 0xff, 0x00)],
        title="single_color_bar"))
