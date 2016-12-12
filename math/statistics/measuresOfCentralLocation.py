'''
Created on 2016. 12. 8.

@author: lsh
'''

import statistics as sta

data=[1,2,3,4,5,6]

print(sta.mean(data))
print(sta.median(data))
print(sta.median_low(data))
print(sta.median_high(data))

print(sta.pvariance(data))
print(sta.pstdev(data))


print(sta.variance(data))
print(sta.stdev(data))