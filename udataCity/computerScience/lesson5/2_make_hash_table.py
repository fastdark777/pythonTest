'''
Created on 2017. 1. 6.

@author: lsh
'''
# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


#===============================================================================
# me
#===============================================================================
def make_hashtable_my(nbuckets):
    hash_table=[]
    i=0
    while i<nbuckets:
        hash_table.append([])
        i+=1
    
    return hash_table

#===============================================================================
# instructor
#===============================================================================
def make_hashtable(nbuckets):
    hash_table=[]
    
    for unused in range(0,nbuckets):
        hash_table.append([])
        
    return hash_table
    
    

print(make_hashtable(10))


