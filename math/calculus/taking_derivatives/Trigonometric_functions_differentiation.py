'''
Created on 2016. 12. 27.

@author: shmoc
'''
from sympy import *
import numpy as np
x = Symbol('x')
y = tan(x)



simplify(diff(tan(x)))
print(simplify(diff(tan(x))))


limit((tan(x+y)-tan(x))/y, y, 0)

# yprime = y.diff(x)  
# print(yprime)


#f = lambdify(x, yprime, 'numpy')
# print(f(np.ones(5)))
# arr=np.arange(0,5,1)
# print(arr)
# print(f(arr))