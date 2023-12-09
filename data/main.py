import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10, 10, 100)
x = np.arcsinh(t)
y = - np.sqrt(1 + t**2)

plt.plot(x, y)

plt.show()
