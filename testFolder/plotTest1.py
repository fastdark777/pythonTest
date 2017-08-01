'''
Created on 2017. 2. 23.

@author: lsh
'''

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(-1., 1., 0.1)

# red dashes, blue squares and green triangles
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

print(t)
print(t**2)
plt.plot(t, t, 'r--', t,t**2)
plt.show()