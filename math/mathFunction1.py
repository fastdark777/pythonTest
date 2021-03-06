import matplotlib.pyplot as plt
import numpy as np

def f(z,t):
    return np.exp(-z)*np.sin(t-z)

z = np.linspace(0,5,3001)
t = np.arange(0,40000,4000)

for tval in t:
    plt.plot(z, f(z, tval))
plt.show()
