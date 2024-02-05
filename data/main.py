import matplotlib.pyplot as plt
import numpy as np

# t = np.linspace(-10, 10, 100)
# x = np.arcsinh(t)
# y = - np.sqrt(1 + t**2)

thickness = 4

x = np.linspace(-3, 6, 3500)
y_shift = 0 #0.033

y1 = - np.cosh(x) + y_shift
plt.plot(x, y1, color="tab:cyan", linewidth=thickness)
y2 = - np.cosh(x - 2*np.arcsinh(1)) + y_shift
plt.plot(x, y2, color="tab:cyan", linewidth=thickness)
y3 = - np.cosh(x - 4*np.arcsinh(1))
plt.plot(x, y3, color="tab:cyan", linewidth=thickness)

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

plt.ylim(-1.414, 0)
plt.xlim(-1, 2.7)

plt.gca().set_aspect('equal')

import corner

if __name__ == "__main__":
    plt.show()
