'''
Created on 2016. 12. 23.

@author: shmoc
'''

from sympy import *

#from IPython.display import display

init_printing()

x = Symbol('x')
y = Symbol('y')

f=Function("f")
g=Function("g")
h=Function("h")


#2 function
diff(f(x)*g(x))
print(diff(f(x)*g(x)))



#apply 1
diff(x**2*sin(x))

#2
diff(exp(x)*cos(x))




#3 function
diff(f(x)*g(x)*h(x))