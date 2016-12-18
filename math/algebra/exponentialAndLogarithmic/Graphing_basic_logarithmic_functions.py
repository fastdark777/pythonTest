'''
Created on 2016. 12. 17.

@author: shmoc
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from numpy import insert
import numpy as np
import math


#using built-in math function
def f(x, base):
    return math.log(x,base)

#using numpy
def g(x, base):
    return np.log(x)/np.log(base)


x1=np.arange(1,1000,10)
x2=np.arange(0,1)
x=np.setdiff1d(x1, x2)

print(x)

fig, ax = plt.subplots()


#plot first function

ax.plot(x, g(x,10), '-o')
# annote the point with number
for i,j in zip(x,g(x,10)):
      plt.annotate(str(j),xy=(i,j))

#line 0,0 axis
#ax.plot(x,x*0, '--g')
#ax.plot(x*0,f(x), '--g')


#tick the x axis
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.grid(True)
plt.show()




