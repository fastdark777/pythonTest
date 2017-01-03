'''
Created on 2017. 1. 3.

@author: lsh
'''

from sympy import *
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
init_printing() 

x = Symbol('x')

def basicTest():        
    y = x**2

    dydx=Derivative(y,x)
    display(dydx)
    display(dydx.doit())
    #diff(y,x)

def chainRule():
    y = (cos(x)**3)
    dydx=Derivative(y,x)
    dydsinx=Derivative(y,cos(x))
    display(dydx)    
    display(dydsinx)
    
    display(dydx.doit())
    display(dydsinx.doit())

def basicTestWithPlot():        
    y = x**5

    dydx=Derivative(y,x)
#     display(dydx)
#     display(dydx.doit())

    arr=np.arange(-5,6,1)
    
    #plot f(x)
    f=lambdify(x,y,'numpy')
    plt.subplot(211)
    plt.plot(arr,f(arr))
    
    #plot f'(x)
    fPrime = lambdify(x, dydx.doit(), 'numpy')
    plt.subplot(212)
    plt.plot(arr,fPrime(arr))

    plt.grid(True)  
    plt.show()



basicTestWithPlot()
