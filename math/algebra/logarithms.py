'''
Created on 2016. 12. 11.

@author: shmoc
'''
import math
from util.stringUtil import toFraction
import matplotlib.pyplot as plt
from numpy import *
from numpy import log, sin


result=math.log(2,8)
print(toFraction(result))
print(math.log(1/8,2))





def f(x):
    return 3**x

def g(x):
     return  log(x)
#     return sin(x)

# g = lambda number : math.log(number,3)

# t = arange(0.1, 2 * pi, 0.1)
x=arange(1,5,1)
aa=range(1,5)
# plt.plot(x, f(x), '-o')

fig, ax = plt.subplots()
ax.plot(x, f(x), '-o')
ax.plot(x, log(x), '-o')

print(g(x))
# ax.plot(x,g(x))


ax.yaxis.grid(True, which='minor')
# tick_spacing = 1
# ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
# ax.plot(x,x*0, '--g')
# ax.plot(x*0,f(x), '--g')

plt.xticks(arange(min(x), max(x)+1, 1.0))

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('plot test function')
plt.grid(True)
# plt.savefig("test.png")


#annote the point with number
for i,j in zip(x,g(x)):
     plt.annotate(str(j),xy=(i,j))
#     plt.text(i+0.1, j, str(j))

plt.show()