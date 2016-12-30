
import matplotlib.pyplot as plt
from numpy import *
from math import e


def f(x):
    return (math.e**x)/2+x**3
    

# t = arange(0.1, 2 * pi, 0.1)
x=arange(-5,5,0.1)

# plt.plot(x, f(x), '-o')

fig, ax = plt.subplots()
ax.plot(x, f(x), '-o')



# ax.plot(x,x*0, '--g')
# ax.plot(x*0,f(x), '--g')

# plt.xticks(arange(min(x), max(x)+1, 1.0))
plt.grid(True)


#annote the point with number
# for i,j in zip(x,f(x)):
#      plt.annotate(str(j),xy=(i,j))
#     plt.text(i+0.1, j, str(j))


plt.show()
