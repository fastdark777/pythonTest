# First, the required modules are imported. The array-manipulation module
# **numpy** and the matplotlib submodule **pyplot**, to plot 2d graphics. The
# corresponding aliases `np` and `plt` for these two modules are widely used
# conventions.

import numpy as np
import matplotlib.pyplot as plt

# In the next block of code `clf()` clears the current figure to prevent
# multiple labels. The second part creates a dictionary of pairs
# `attribute:value` to configure the fonts to label the axes and print the
# title. 

plt.clf() #Clear the current figure (prevents multiple labels)

labelfont = {
        'family' : 'sans-serif',  # (cursive, fantasy, monospace, serif)
        'color'  : 'black',       # html hex or colour name
        'weight' : 'normal',      # (normal, bold, bolder, lighter)
        'size'   : 14,            # default value:12
        }

titlefont = {
        'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 16,
        }

# The code below computes the sine and cosine for x in the interval [-2pi,
# 2pi]. The mathematical constant `pi` and the functions `sin()` and `cos()`
# are provided by the numpy module. `x` is a numpy array with 100 points
# between the bounds of the interval, the more points we use the better
# quality we get, but it requires more computing-power.

pi = np.pi 
x = np.linspace(-2*pi, 2*pi, 50) #return evenly spaceed number over a specified interval
f1 = np.sin(0.25*x)
f2 = np.cos(x) 

# The next block of code creates the plot, most of the options are
# self-descriptive. Notice that you can use LaTeX code for the labels and the
# legends.  The available line styles are: `--`, `-`, `-.`, `:` and `steps`
# and for the colours it is possible to use html hexadecimal notation or
# colour names.

plt.plot(x, f1,                             
         'darkgreen',                       # colour
         linestyle='--',                    # line style
         linewidth=3,                       # line width
         label='$0.25 \cdot \sin(x)$')      # plot label

plt.plot(x, f2, 
         'darkmagenta', 
         linestyle='-', 
         linewidth=3, 
         label='$\cos(x)$') 

axes = plt.gca()
axes.set_xlim([-2*pi, 2*pi])            # x-axis bounds
axes.set_ylim([-1.5, 1.5])              # y-axis bounds

legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

plt.title('Trigonometric functions', fontdict=titlefont) 
plt.xlabel('Angle (in radians)', fontdict=labelfont)
plt.ylabel('Function', fontdict=labelfont)

plt.subplots_adjust(left=0.15)        # prevents overlapping of the y label

plt.show()
