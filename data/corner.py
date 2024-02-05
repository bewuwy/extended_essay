from numpy import arctan, sqrt, sin, cos, pi

def f_prim(theta):
    return sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

def i_1(theta):
    return 3/4 * (sin(theta) + cos(theta))/sqrt(2)

def y(theta):
    return -(3*sqrt(2))/4 * cos(theta + pi/4) - sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

theta_start = - arctan(4/3)
theta_stop = arctan(4/3) - pi/2 

h = 0.001
x_0 = 0.06606459412 * 1.5 + 0.693

x_min = 9999
x_max = -9999

cur_theta = theta_start
cur_f = x_0

x = []
y_list = []
theta = []

while cur_theta < theta_stop:
    cur_f_prim = f_prim(cur_theta)
    cur_i1 = i_1(cur_theta)
    cur_y = y(cur_theta)
    
    cur_f += h * cur_f_prim

    cur_x = cur_i1 + cur_f
    x.append(cur_x)
    y_list.append(cur_y)
    theta.append(cur_theta)
    
    x_min = min(x_min, cur_x)
    x_max = max(x_max, cur_x)

    cur_theta += h
    
print("x_min", x_min)
print("x_max", x_max)

# plot x and y
import matplotlib.pyplot as plt

plt.plot(x, y_list, color="tab:red", linewidth=4)

# set 1:1 aspect ratio
plt.gca().set_aspect('equal')

plt.show()
