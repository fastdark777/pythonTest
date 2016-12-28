'''
Created on 2016. 12. 27.

@author: shmoc
'''
from sympy import *
import numpy as np
x = Symbol('x')
a = Symbol('a')
y = a**x


###############################
diff(y,x)
print(diff(y,x))


###############################
diff(exp(1)**x)
