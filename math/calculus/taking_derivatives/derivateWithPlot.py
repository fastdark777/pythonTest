'''
Created on 2016. 12. 24.

@author: shmoc
'''
 
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing() 

x = Symbol('x')

# f = (sin(x)**2)
f=x**2
fPrime=diff(f,x)
# diff(f,x)
# diff(f,sin(x))


# print(diff(f,x))

arr=np.arange(-5,6,0.1)
ff = lambdify(x, f, 'numpy')
ffPrime = lambdify(x, fPrime)


print(ff(2))
plt.plot(arr,ff(arr))

plt.plot(arr,ffPrime(arr))


plt.grid(True)
plt.show()



