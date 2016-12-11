from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')

# eq = 2 * x ** 2 -1
# eq=(x+3)**2-4
eq = (x - 2) ** 2 - 9
t = solve(eq, x, 'rational')
print(t)


