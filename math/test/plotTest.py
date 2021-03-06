'''
Created on 2016. 12. 11.

@author: shmoc
'''
'''
Created on 2016. 12. 10.

@author: shmoc
'''
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import *
from math import e



def f(x):

    equation=2**-x
    return equation


# t = arange(0.1, 2 * pi, 0.1)
x=arange(-5,5,0.5)

# plt.plot(x, f(x), '-o')

fig, ax = plt.subplots()
ax.plot(x, f(x), '-o')
# tick_spacing = 1
# ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))


ax.plot(x,x*0, '--g')
ax.plot(x*0,f(x), '--g')

plt.xticks(arange(min(x), max(x)+1, 1.0))

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('plot test function')
plt.grid(True)
# plt.savefig("test.png")


#annote the point with number
for i,j in zip(x,f(x)):
     plt.annotate(str(j),xy=(i,j))
#     plt.text(i+0.1, j, str(j))



plt.show()
# print(t)
