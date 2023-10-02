import matplotlib.pyplot as plt
import numpy as np

#pyplot to graph the projectile motion
def projectileMotionGraph():
    #Defining the constants
    g = 9.8 #m/s^2
    v0 = 15 #m/s
    theta = 72 #degrees
    theta = theta * (np.pi/180) #radians
    x0 = 0 #m
    y0 = 0 #m
    t = np.linspace(0, 2, 100) #s
    #Defining the equations
    x = x0 + v0 * np.cos(theta) * t
    y = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
    #Plotting the graph
    plt.plot(x, y)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Projectile Motion')
    plt.show()

projectileMotionGraph()