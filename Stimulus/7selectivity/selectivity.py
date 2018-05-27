from selectivity_player import start
from docopt import docopt

__usage__ = '''
selectivity

Usage: 
    selectivity.py [options] SESSION

Options:
    --mode=MODE         # modes [default: 8]
    --initial=WAIT      # initial wait [default: 15]
    --hightime=HIGH     # high time [default: 4]
    --lowtime=LOW       # low time [default: 4]
    --sf=SF             # grating spatial frequency [default: 0.004]
    --speed=SPEED       # grating moving speed [default: 0.02]
    --tex=TEX           # grating texture [default: sqr]
    --windowN=WIN       # window N 
'''

arguments = docopt(__usage__)
print(arguments)

grating_config = {'sf': float(arguments['--sf']), 
                  'tex': arguments['--tex'], 
                  'speed': float(arguments['--speed'])}


start(windowN=[4, 5], grating_config=grating_config, 
      mode=arguments['--mode'],
      sessionName=arguments['SESSION'],
      start_time=int(arguments['--initial']), 
      high_time=int(arguments['--hightime']), 
      low_time=int(arguments['--lowtime']))