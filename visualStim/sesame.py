#!/usr/bin/env python3

"""Sesame visual stimulation generator."""

import logging
import json
from configure import getPygeltColorMaps
import visual

__version__ = "v0.0.1-dev"
__doc__ = """
Sesame {version}

Usage: sesame.py [options] PARADIGM

Options:
    --debug
    -q              # quiet mode
    -H HEIGHT       # screen height [default: 1920]
    -W WIDTH        # screen width [default: 1080]
    -c COLORMAPS    # color map file [default: config/stimColorNames.json]
""".format(version=__version__)

from docopt import docopt
arguments = docopt(__doc__, version=__version__)

if arguments['--debug']:
    logging.basicConfig(level=logging.DEBUG)
elif arguments['-q']:
    logging.basicConfig(level=logging.WARN)
else:
    logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug(arguments.__str__())

colormap = getPygeltColorMaps(arguments['-c'],
                              (int(arguments['-H']), int(arguments['-W']), 3))

# reading paradigm parameters
with open(arguments["PARADIGM"], 'r') as p_file:
    paradigm = json.loads(p_file.read())
    logger.debug("read paradigm file: " + arguments["PARADIGM"])

# start
visual.start(colormap, paradigm)  # TODO: window configurations.
