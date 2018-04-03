"""Demo."""

from sesame_grating import movingGrate
from numpy import sin, cos, pi

A = 1
L = 50
theta = pi/2  # orientation in radium
phi = 0
moving_speed = 100  # pixels per second


def sineWave():
    """Sine wave funciton."""
    def value(x, y):
        return A*sin(2*pi/L*(x*sin(theta)+y*cos(theta))+phi)*255/2+255/2

    return lambda a, b: (value(a, b), value(a, b), value(a, b), 255)


movingGrate(sineWave(), theta, L, moving_speed,
            subject="test", suffix="sine_grating", window_num=1,
            high_duration=5, low_duration=5,
            initial_wait=5, inital_color="black",
            stim_seq=None)
