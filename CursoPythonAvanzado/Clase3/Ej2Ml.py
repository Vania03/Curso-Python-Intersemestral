import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-15,15,100)
y=np.sin(x)/x

plt.plot(x,y)
plt.plot(x,y,'co')#Puntos cyan
plt.plot(x,2*y,x,3*y)#puntos cyan

plt.show()
