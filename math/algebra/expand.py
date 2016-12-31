'''
Created on 2016. 12. 10.

@author: shmoc

Use this to expand an algebraic expression. It will try to denest powers and multiplications:
'''

from sympy import Symbol, factor, expand, simplify
x = Symbol('x')
y = Symbol('y')

print(expand((x + y) ** 4))