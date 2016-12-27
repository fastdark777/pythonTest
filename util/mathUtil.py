'''
Created on 2016. 12. 14.

@author: shmoc
'''
def toFraction(number):
    from fractions import Fraction
    
    return Fraction(number).limit_denominator()

