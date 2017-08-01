'''
Created on 2017. 1. 17.

@author: lsh
'''
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

num=1

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)





print (factorial(0))
#>>> 1

print (factorial(5))
#>>> 120

#print factorial(10)
#>>> 3628800