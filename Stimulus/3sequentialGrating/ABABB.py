"""Demo."""

from sesame_grating import movingGrate
from numpy import sin, cos, pi, sign


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
            subject="test", suffix="sine_grating", window_num=1,
            high_duration=1, low_duration=1,
            initial_wait=5, inital_color="black",
            stim_seq=[
                # (name[, high_duration])
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "B", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black",
                "A", "B", "A", "B", "A", "black", "black", "black"])
