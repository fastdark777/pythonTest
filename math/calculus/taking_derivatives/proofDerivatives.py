'''
Created on 2016. 12. 28.

@author: lsh
'''
from sympy import *
from sympy.abc import delta


x,y=symbols('x,y')
#f=Function('f')


#1. basic derivate proof
f = lambdify(x, 3*x**2)
#l=limit((f(x + delta) - f(x))/delta, delta, 0)
# print(f(3))

#2. trigonometric proof
l=limit((sin(x + delta) - sin(x))/delta, delta, 0)

#3. natural log proof
limit((log(x + delta) - log(x))/delta, delta, 0)

#4. log base b proof
b=symbols('b')
#limit((log(x + delta, 10) - log(x,10))/delta, delta, 0)
limit((log(x + delta, b) - log(x,b))/delta, delta, 0)


#5. e^x proof
limit((exp(x + delta) - exp(x))/delta, delta, 0)
 
# l=Limit(f(x+delta)-f(x)/delta,delta,0)


print(l)