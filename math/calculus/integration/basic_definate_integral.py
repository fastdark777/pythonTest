'''
Created on 2016. 12. 31.

@author: shmoc
'''
from sympy import *
init_printing()

x = Symbol('x')


y=x**2

Integral(y,(x,1,4))

print(integrate(y, (x,1,4)))