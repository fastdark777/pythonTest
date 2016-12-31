'''
Created on 2016. 12. 15.

@author: lsh
'''
def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link<0:
        return None, 0
    
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
                 

#print (get_next_target('<a href="/user/main.do"><strong>M-teletech</strong></a>'))
print (get_next_target('good'))

