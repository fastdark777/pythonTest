'''
Created on 2016. 12. 24.

@author: shmoc
'''
 
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing() 

x = Symbol('x')

# y = (sin(x)**2)
y = (cos(x)**3)

dydx=diff(y,x)
dydsinx=diff(y,cos(x))


# print(diff(f,x))

arr=np.arange(-5,6,1)
lamdydx = lambdify(x, dydx, 'numpy')
#ffPrime = lambdify(x, fPrime)


print(lamdydx(arr))


# print(ff(2))
# plt.plot(arr,ff(arr))
# 
# plt.plot(arr,ffPrime(arr))
# 
# 
# plt.grid(True)
# plt.show()



