'''
Created on 2016. 12. 10.

@author: shmoc
'''

from sympy.solvers import solve
from sympy import Symbol, factor, expand, simplify
x = Symbol('x')
y = Symbol('y')


print(factor(x ** 3 + 3 * x ** 2 * y + 3 * x * y ** 2 + y ** 3))



