from numpy import sin, cos, pi


def sineWave(A=1, L=50, theta=0, phi=0):
    value = lambda x, y: int(A * sin(2*pi/L*(x*sin(theta)+y*cos(theta))+phi) * 255/2 + 255/2)
    result = lambda a, b: (value(a,b), value(a,b), value(a,b), 255)
    return result

def squareWave(A=1, L=50, theta=0, phi=0):
    pass
