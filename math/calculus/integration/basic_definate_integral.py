'''
Created on 2016. 12. 31.

@author: shmoc
'''
from sympy import *
init_printing()

x = Symbol('x')


##ex 1
y=x**2
Integral(y,(x,1,4))
print(integrate(y))
print(integrate(y, (x,1,4)))


## ex2
integrate(y,(x,pi/2,3*pi/2))

## ex3
integrate(y,(x,0,3*pi/2))