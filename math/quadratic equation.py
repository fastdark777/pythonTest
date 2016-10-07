import math

a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

d = b**2-4*a*c # discriminant


if d < 0:
    print ('No solutions')
elif d == 0:
    x1 = -b / (2*a)
    print ('The sole solution is',x1)
else: # if d > 0
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print ('Solutions are',x1,'and',x2)
