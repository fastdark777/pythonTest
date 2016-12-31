'''
Created on 2016. 12. 15.

@author: lsh
if and while have same structure
'''

def biggest(a, b):
    if (a > b):
        return a
    else:
        return b


def whileTest():
    i=0
    while (i!=10):
        i=i+1
        print(i)
    
# print(biggest(biggest(3,5),9))
#print(whileTest())


# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.


def print_numbers(a):
    i=1
    while i<=a:
        print(i)
        i=i+1

#print_numbers(5)


# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    num=1
    while 1<n:
        num=num*n
        n=n-1
    return num

print (factorial(6))



    