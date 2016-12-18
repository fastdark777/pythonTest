'''
Created on 2016. 12. 17.

@author: shmoc
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import *


def f(x):
    equation=(2**-x)-5
    return equation

def g(x):
    return 2**x
    

x=arange(-5,5.5,0.5)


fig, ax = plt.subplots()
ax.plot(x, f(x), '-o')
ax.plot(x,g(x))


ax.plot(x,x*0, '--g')
ax.plot(x*0,f(x), '--g')

plt.xticks(arange(min(x), max(x)+1, 1.0))
plt.grid(True)


#annote the point with number
for i,j in zip(x,f(x)):
     plt.annotate(str(j),xy=(i,j))


for i,j in zip(x,g(x)):
     plt.annotate(str(j),xy=(i,j))

plt.show()
