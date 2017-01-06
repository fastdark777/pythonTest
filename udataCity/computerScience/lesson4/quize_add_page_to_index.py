

'''
Created on 2017. 1. 3.

@author: lsh
'''
# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

# coding: utf8
index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    
    keyWord=content.split()
    
    for entry in keyWord:
        add_to_index(index, entry, url)



def get_page(url):
    try:
        import urllib.request
        
        cont = urllib.request.urlopen(url).read()
        print(cont)       
    except:
        return ""
     


print(get_page("http://www.koreatimes.co.kr/www/index.asp"))

#add_page_to_index(index,'fake.text',"This is a test")
#print (index)
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


