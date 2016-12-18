'''
Created on 2016. 12. 17.

@author: shmoc
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from numpy import insert
import numpy as np

def f(x):
    equation=(2**x)
    return equation

def g(x, base):
    return np.log(x)/np.log(base)


def h(y):
    return np.power(2,y)
    
x=np.arange(-5,4,1.0)
fig, ax = plt.subplots()


#plot first function
xx=[]
ax.plot(x, f(x), '-o')
# annote the point with number
for i,j in zip(x,f(x)):
      plt.annotate(str(j),xy=(i,j))
      xx.append(j)
     # xy=np.insert(i)

    
#plot second function with is the log function    
ax.plot(xx,g(xx,2))
for i,j in zip(xx,g(xx,2)):
    plt.annotate(str(j),xy=(i,j))


#line 0,0 axis
ax.plot(x,x*0, '--g')
ax.plot(x*0,f(x), '--g')


#tick the x axis
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.grid(True)
plt.show()




