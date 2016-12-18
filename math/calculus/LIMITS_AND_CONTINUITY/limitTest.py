'''
Created on 2016. 12. 17.

@author: shmoc
'''

import sympy as sy
from mpmath import *
#import numpy as np
x = sy.symbols('x')
#k, m, n = symbols('k m n', integer=True)
#f, g, h = symbols('f g h', cls=Function)

#print(solve([x*y - 1, x - 2], x, y))


eq = (x**2-7)/(2*x**2+5*x)
s=sy.solve(eq, x)
limL=sy.limit(eq, x, -1, '-')
limR=sy.limit(eq, x, -1, '+')

print(s)
print(limL)
print(limR)


print("==================")
#=================


eq1 = x/sy.log(x)
s1=sy.solve(eq1,x)

limL1=sy.limit(eq1, x, 1, '-')
limR1=sy.limit(eq1, x, 1, '+')

print(limL1)
print(limR1)


print("==================")



#=================


eq2 = (x**2+6-6)/(x-2)
s2=sy.solve(eq2,x)

lim2=sy.limit(eq2, x, 2)

print(lim2)
