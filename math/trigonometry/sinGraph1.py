'''
Created on 2016. 12. 10.

@author: shmoc
'''
from matplotlib.pyplot import figure, show
from numpy import arange, sin, cos, pi


def f(x):
    """
    Returns temperature in Celsius.
    """
    return (-1/2) * cos(3*x)


t = arange(0.0, 2*pi, 0.1)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, f(t))
ax1.grid(True)
#ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')



show()