'''
Created on 2017. 1. 2.

@author: lsh
'''


from sympy import *
init_printing()

x = Symbol('x')


y=12*x**(1/3.)

Integral(y,(x,-1,8))

#sal's answer is 135 but this has strange number
print(integrate(y, (x,-1,8)))
print((-2)**2)

##############################
#ok
y=9*sin(x)
Integral(y,(x,6*pi,(11*pi)/2))
print(integrate(y,(x,6*pi,(11*pi)/2)))


##############################
#https://www.khanacademy.org/math/integral-calculus/definite-integral-evaluation-ic/definite-integral-evaluation-tut-ic/v/definite-integral-involving-natural-log
y=(6+(x**2))/(x**3)
expr=Integral(y,(x,2,4))
#integrate(y,(x,2,4))
expr.doit()