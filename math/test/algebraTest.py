'''
Created on 2016. 12. 11.

@author: shmoc
'''
import math


from sympy import Symbol, sqrt
from util.stringUtil import toFraction


x = Symbol('x')
y = sqrt(x)
print(y)


a=96**(1/5)

print(a)

print('============= log =============')
print('what power do I need to raise 6 to, to get 216')
l=math.log(216,6)
print(toFraction(l))

result=math.log(2,8)
print(toFraction(result))

print(math.log(1/8,2))
# print(getFraction(math.log(2,8)))


exp=(1+1/10)**10
print(exp)
print(1.1**10)
print(math.e)

print(math.log(67, math.e))

print(math.e**4.20  )