'''
Created on 2017. 1. 12.

@author: lsh
'''

#import scipy.misc.comb
#import scipy as sc
#import scipy.misc.comb as co


def usingScipy():    
    from scipy.special import comb
    from scipy.special import perm

    n=3
    k=2
    
    print(comb(n,k))
    print(perm(n,k))



def usingIterTools():
    import itertools  
    
    print (list(itertools.combinations([1,2,3], 2)))  
    print (list(itertools.permutations([1,2,3], 2)))
    
    

usingScipy()
print("################")
usingIterTools()  