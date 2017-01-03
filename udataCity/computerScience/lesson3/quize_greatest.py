'''
Created on 2017. 1. 2.

@author: lsh
'''
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    topNum=0
    for num in list_of_numbers:
        if topNum<num:
            topNum=num
    return topNum



print (greatest([4,23,1]))
#>>> 23
#print (greatest([]))
#>>> 0

    
