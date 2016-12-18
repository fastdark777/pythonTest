'''
Created on 2016. 12. 17.

@author: shmoc
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from numpy import insert
import numpy as np
import math


from sympy import *

x, y, z, t = symbols('x y z t')
#k, m, n = symbols('k m n', integer=True)
#f, g, h = symbols('f g h', cls=Function)

#print(solve([x*y - 1, x - 2], x, y))


eq = 6*(x**2)+5*x-1
s=solve(eq, x)
limL=limit(eq, x, 0, '-')
limR=limit(eq, x, 0, '+')

print(s)
print(limL)
print(limR)


# x, y, z = symbols('x y z')
# from sympy import sin, limit


#using built-in math function

def f(x):
    exp=6*(x**2)+5*x-1
    return exp


x=np.arange(-5,5,1)

fig, ax = plt.subplots()

ax.plot(x, f(x), '-o')



# annote the point with number
for i,j in zip(x,f(x)):
      plt.annotate(str(j),xy=(i,j))

#tick the x axis
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.grid(True)
plt.show()








