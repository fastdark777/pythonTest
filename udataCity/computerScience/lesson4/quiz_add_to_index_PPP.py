'''
Created on 2017. 1. 3.

@author: lsh
'''
# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

#===============================================================================
# very hard problem to me tt
# 1 add_to_index
#===============================================================================
def add_to_index(index,keyword,url):
    for entry in index:
        if(entry[0]==keyword):
            entry[1].append(url)
            return
        
    index.append([keyword,[url]])    
    

#===============================================================================
# 2 lookup
#===============================================================================
def lookup(index,keyword):
    for entry in index:
        if keyword in entry:
            return entry[1]
    
    return []
    

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
#print (index)
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


print (lookup(index,'udacity'))
#>>> ['http://udacity.com','http://npr.org']

