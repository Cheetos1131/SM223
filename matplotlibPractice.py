#Setting up the imports for the program
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import meshgrid,imshow,contour,clabel,colorbar,axis,title,show
from matplotlib.ticker import LinearLocator
import numpy as np

def function(x, y):
    #Defining a SM223 function
    return ((np.sin(x)*np.sin(y))/(x*y))

def function2(x, y):
    #Defining another SM223 function
    return (-1*(x*y*np.exp((-1*x**2)-(y**2))))

x = np.arange(-3.0, 3.0, 0.1)
y = np.arange(-3.0, 3.0, 0.1)
X, Y = meshgrid(x, y) # grid of point
Z = function(X, Y) # evaluation of the function on the grid

im = imshow(Z,cmap=cm.RdBu) # drawing the function
# adding the Contour lines with labels
cset = contour(Z,np.arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # adding the colobar on the right
# latex fashion title
title('$-xye^{-x^2-y^2}$')
show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_zlim(-1, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()