'''
Created on 2017. 1. 5.

@author: lsh
'''
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    num=0
    for word in keyword:
        num+=(ord(word))
    return num%buckets
        





print (hash_string('a',12))
#>>> 1

#print (hash_string('b',12))
#>>> 2

print (hash_string('a',13))
#>>> 6

print (hash_string('au',12))
#>>> 10

print (hash_string('udacity',30267))
#>>> 11
