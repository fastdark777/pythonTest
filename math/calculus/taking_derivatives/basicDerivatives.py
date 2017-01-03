'''
Created on 2016. 12. 18.

@author: shmoc
'''
from sympy import *
import numpy as np
x = Symbol('x')
y = x**2
yprime = y.diff(x)  
print(yprime)


f = lambdify(x, yprime, 'numpy')
arr=np.arange(0,5,1)
#print(arr)
print(f(arr))

y = x**2
deriv = Derivative(y,x)
