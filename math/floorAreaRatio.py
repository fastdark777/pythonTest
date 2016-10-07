import numpy as np
import matplotlib.pyplot as plt


def getFloorAreaRatio(a, b):
    return (a/b)*100
    
plt.clf() #Clear the current figure (prevents multiple labels)


grossArea = np.linspace(1000, 5000, 5)
landSize=1000

y=getFloorAreaRatio(grossArea, landSize)

#print(y)
#plt.plot(grossArea,y, 'r')


plt.plot(grossArea,y,
        'darkmagenta',
        linestyle='--', 
        linewidth=1, 
        label='$\cos(x)$')
plt.plot(grossArea,y, 'bo', label='$\int_a^b f(x)\mathrm{d}x$') #same function with cyan dots



plt.axis([1000, 7000, 0, 600])
'''
axes = plt.gca()
axes.set_xlim([1000, 7000])            # x-axis bounds
axes.set_ylim([0, 600])              # y-axis bounds
'''



#legend(optional)
plt.legend(loc='upper right', shadow=True, fontsize='small')


#writing numerical values on the plot
for a,b in zip(grossArea, y): 
    plt.text(a, b, str(b))



#printing label on x,y axis and title(optional)
labelfont = {
        'family' : 'sans-serif',  # (cursive, fantasy, monospace, serif)
        'color'  : 'black',       # html hex or colour name
        'weight' : 'normal',      # (normal, bold, bolder, lighter)
        'size'   : 14,            # default value:12
        }

titlefont = {
        'family' : 'serif',
        'color'  : 'red',
        'weight' : 'bold',
        'size'   : 16,
        }

plt.title('floorAreaRatio functions', fontdict=titlefont) 
plt.xlabel('grossArea', fontdict=labelfont)
plt.ylabel('floorAreaRatio', fontdict=labelfont)

plt.subplots_adjust(left=0.15) #prevents overlapping of the y label
plt.show()
