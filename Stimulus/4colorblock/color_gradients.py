if __name__ == '__main__':
    __version__ = "v1.0-dev"
    __doc__ = """
    Sesame Color Gradients{version}

    Usage: color_gradients.py [options] SUBJECT

    Options:
        --debug
        --window=WINDOWN    # number of secondary screeens [default: 1]
        --mode==MODE        # gradients mode, either be "discrete" or "continuous" [default: discrete]
        --initialwait=WAIT  # the initial waiting time [default: 60]
        --hightime=HIGH     # high time duration [default: 3]
        --lowtime=LOW       # low time duration [default: 3]
    """.format(version=__version__)

    from docopt import docopt
    import logging
    arguments = docopt(__doc__, version=__version__)

    if arguments['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if arguments['--mode'] == 'discrete':
        from discrete import start_experiment
    elif arguments['--mode'] == 'continuous':
        from continuous import start_experiment
    else:
        raise ValueError("no such mode yet: "+arguments['--mode'])

    start_experiment(arguments['SUBJECT'], arguments['--mode'], int(arguments['--window']),
                     int(arguments['--initialwait']), int(arguments['--hightime']), 
                     int(arguments['--lowtime']),)
