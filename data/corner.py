from math import sqrt, sin, cos, pi


def f_prim(theta):
    return sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

def i_1(theta):
    return 3/4 * (sin(theta) + cos(theta))/sqrt(2)

def y(theta):
    return -(3*sqrt(2))/4 * cos(theta + pi/4) - sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

start = -0.927
stop = -0.644

h = 0.001

cur_theta = start
cur_f = 0

x = []
y_list = []
theta = []

while cur_theta < stop:
    cur_f_prim = f_prim(cur_theta)
    cur_i1 = i_1(cur_theta)
    cur_y = y(cur_theta)
    
    cur_f += h * cur_f_prim

    x.append(cur_i1 + cur_f)
    y_list.append(cur_y)
    theta.append(cur_theta)

    cur_theta += h

# plot x and y
import matplotlib.pyplot as plt

plt.plot(x, y_list)
plt.show()
