'''
Created on 2016. 12. 18.

@author: shmoc
'''
from sympy import *
import numpy as np
x = Symbol('x')
y = 3*x**2
yprime = y.diff(x)
print(yprime)


f = lambdify(x, yprime, 'numpy')
# print(f(np.ones(5)))
arr=np.arange(0,5,1)
print(arr)
print(f(arr))