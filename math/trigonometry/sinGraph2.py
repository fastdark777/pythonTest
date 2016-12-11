'''
Created on 2016. 12. 10.

@author: shmoc
'''
import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi


def f(x):
    """
    Returns temperature in Celsius.
    """
#     return (-1/2) * cos(3*x)
    return sin(5 * x - 5) / x - 1


t = arange(0.1, 2 * pi, 0.1)

plt.plot(t, f(t), '-o')

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
# plt.savefig("test.png")
plt.show()
# print(t)
