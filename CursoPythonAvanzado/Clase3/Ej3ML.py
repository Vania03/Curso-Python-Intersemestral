import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0.0,5.0,0.2)

plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')#Line azul, linea roja, recytangulos azules, triangulos verdes

plt.show()