'''
Created on 2017. 1. 5.

@author: lsh
'''
import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,100)
print(v)
# Plot a normalized histogram with 50 bins
#plt.hist(v, bins=50, normed=1)       # matplotlib version (plot)
#plt.show()