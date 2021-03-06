"""Demo."""

from sesame_grating import movingGrate
try:
    from numpy import sin, cos, pi
except ModuleNotFoundError:
    import logging
    logger = logging.getLogger(__name__)
    logger.warn("numpy not found, using math module")
    from math import sin, cos, pi


def sineWave(A, L, theta, phi):
    """Sine wave funciton."""
    def value(x, y, alpha):
        v = A*sin(2*pi/L*(x*sin(theta)+y*cos(theta))+phi)*255/2+255/2
        return (v, v, v, alpha)

    return lambda a, b: value(a, b, 255)

moving_speed = 150
grating_list = {
    # (grating, theta, L, moving_speed)
    "A": (sineWave(1, 50, 0, 0), pi/2, 50, moving_speed),
    "B": (sineWave(1, 50, pi/2, 0), 0, 50, moving_speed)
}

movingGrate(grating_list,
            subject="test", suffix="ABABA", window_num=1,
            high_duration=1.5, low_duration=1.5,
            initial_wait=5, inital_color="gray",
            stim_seq=[
                # (name[, high_duration])
                "A", "B", "A", "B", "A", "gray", "gray", "gray"])
