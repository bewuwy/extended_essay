from numpy import arctan, sqrt, sin, cos, pi

def x_2_prim(theta): # derivative of 2nd part of x function
    return sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

def x_1(theta): # 1st part of x function
    return 3/4 * (sin(theta) + cos(theta))

def y(theta): # y function
    return -(3*sqrt(2))/4 * cos(theta + pi/4) - sqrt( 1/16 - 9/8 * (sin(pi/4 + theta) )**2 )

theta_start = - arctan(4/3)
theta_stop = arctan(4/3) - pi/2 

h = 0.001
x_0 = 0.693 * 1.22

y_shift = - 0.041

cur_theta = theta_start
cur_x2 = x_0

x_list = []
y_list = []

while cur_theta < theta_stop:
    cur_x_2_prim = x_2_prim(cur_theta)    
    cur_x2 += h * cur_x_2_prim
    
    cur_x = x_1(cur_theta) + cur_x2
    
    x_list.append(cur_x)
    y_list.append(y(cur_theta) + y_shift)

    cur_theta += h

# plot x and y
import matplotlib.pyplot as plt

plt.plot(x_list, y_list, color="tab:cyan", linewidth=4)

# set 1:1 aspect ratio
plt.gca().set_aspect('equal')

if __name__ == "__main__":
    plt.show()
