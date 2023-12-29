import matplotlib.pyplot as plt
import numpy as np

# t = np.linspace(-10, 10, 100)
# x = np.arcsinh(t)
# y = - np.sqrt(1 + t**2)

x = np.linspace(-3, 3)

x1 = np.linspace(-np.arcsinh(1), np.arcsinh(1))
y1 = - np.cosh(x)
plt.plot(x, y1)
x2 = np.linspace(-3*np.arcsinh(1), -np.arcsinh(1))
y2 = - np.cosh(x - 2*np.arcsinh(1))
plt.plot(x, y2)
y3 = - np.cosh(x + 2*np.arcsinh(1))
plt.plot(x, y3)

# y1, y2, y3 = [np.clip(i, -1.414, -1) for i in [y1, y2, y3]]

# x_square = np.linspace(-1, 1)
# y_square = np.repeat(-1, 50)
# plt.plot(x_square, y_square)

def square(x_start):    
    m = - np.sinh(x_start)
    c = - np.cosh(x_start) + x_start * np.sinh(x_start)
    
    x_length = 2 / np.sqrt(m**2 +1)
    
    x_range = np.linspace(x_start - x_length/2, x_start + x_length/2)
    y = m * x_range + c
    return x_range, y

# x_square3, y_square3 = square(.6)
# plt.plot(x_square3, y_square3)

# x_square2, y_square2 = square(.8)
# plt.plot(x_square2, y_square2)

# x4, y4 = square(1.2)
# plt.plot(x4, y4)

plt.ylim(-1.414, .5)
plt.xlim(-3, 3)

plt.gca().set_aspect('equal')

plt.show()
