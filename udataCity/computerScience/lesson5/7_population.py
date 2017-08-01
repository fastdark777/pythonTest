'''
Created on 2017. 1. 17.

@author: lsh
'''
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5


city = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai": 12.5}
city["seoul"] = 10
print(city)
print(city["Shanghai"])