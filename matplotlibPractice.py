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

def function3(x, y):
    #Defining another SM223 function
    return (np.arctan(y/x))

def function4(x, y):
    #Defining another SM223 function
    return (np.sin(x) + np.sin(y))

def function5(x, y):
    #Defining another SM223 function
    return (np.sin(np.sqrt(x**2 + y**2)))

def function6(x, y):
    #Defining another SM223 function
    return (x*np.exp(x*y))

#14.7 HW
def function7(x, y):
    #From Question 3
    #Set zlim to (-30, 30)
    return (4 + np.power(x, 3) + np.power(y, 3) - (3*x*y))

def function8(x, y):
    #From Question 5
    return (np.power(x, 2) + (x*y) + np.power(y, 2) + y)

def function9(x, y):
    #From Question 11
    return (np.power(x, 3) - (3*x) + (3*x*np.power(y, 2)))

def function10(x, y):
    #From Question 6
    return ((x*y) - (2*x) - (2*y) - (np.power(x, 2)) - (np.power(y, 2)))

def function11(x, y):
    #From Question 41
    return (1 - x - y)

def line(x, y):
    return (x + y)

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = meshgrid(x, y) #Makes grid of points
Z = function11(X, Y) #Creates the height Z from the meshmap and multivariable function
#Z2 = line(X, Y)

im = imshow(Z,cmap=cm.coolwarm) #Draws the function
#Adds the Contour lines with labels
cset = contour(Z,np.arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) #Adds the colorbar on the right
#Latex rendered title
title('Contour Map of Function')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0.01, antialiased=False)
#surf2 = ax.plot_surface(X, Y, Z2, cmap=cm.viridis, linewidth=0, antialiased=False)

ax.set_zlim(-30, 30)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title('3D Plot of Function')
plt.show()
show()