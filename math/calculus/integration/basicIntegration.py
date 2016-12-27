'''
Created on 2016. 12. 22.

@author: shmoc
'''
from sympy import *
init_printing()

#init_printing(use_unicode=False, wrap_line=False, no_global=True)
x = Symbol('x')
f=Function("f")

#적분 표현
Integral(f(x))

#적분 하라
integrate(f(x))
#a=integrate(x**2 + x + 1, x)

'''
example
'''
#1
a=integrate(2*x, x)

print(a)