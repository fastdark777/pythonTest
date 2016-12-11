'''
Created on 2016. 12. 10.

@author: shmoc

Use simplify if you would like to transform an expression into a simpler form:
In [19]: simplify((x+x*y)/x)
Out[19]: 1 + y
Simplification is a somewhat vague term, and more precises alternatives to simplify exists: 
powsimp (simplification of exponents), trigsimp (for trigonometric expressions) , logcombine, rad

'''
from sympy import Symbol, simplify

x = Symbol('x')
y = Symbol('y')

print(simplify((x + x * y) / x))