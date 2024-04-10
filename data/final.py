import matplotlib.pyplot as plt
import numpy as np

square_color = 'tab:blue'

# define the thickness of the lines
thickness = 4

# plot line from (-0.75, 1) to (0.75, 1)
plt.plot([-0.75, 0.75], [1, 1], color=square_color, linewidth=thickness)
# plot line from (-0.75, -1) to (0.75, -1)
plt.plot([-0.75, 0.75], [-1, -1], color=square_color, linewidth=thickness)
# plot line from (1, 0.75) to (1, -0.75)
plt.plot([1, 1], [0.75, -0.75], color=square_color, linewidth=thickness)
# plot line from (-1, 0.75) to (-1, -0.75)
plt.plot([-1, -1], [0.75, -0.75], color=square_color, linewidth=thickness)

# plot 4 circles at the corners of the square with radius 0.25
circle1 = plt.Circle((0.75, 0.75), 0.25, edgecolor=square_color, facecolor='none', linewidth=thickness)
circle2 = plt.Circle((-0.75, 0.75), 0.25, edgecolor=square_color, facecolor='none', linewidth=thickness)
circle3 = plt.Circle((0.75, -0.75), 0.25, edgecolor=square_color, facecolor='none', linewidth=thickness)
circle4 = plt.Circle((-0.75, -0.75), 0.25, edgecolor=square_color, facecolor='none', linewidth=thickness)

# add the circles to the plot
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.gca().add_patch(circle4)

plt.axis('equal')

import main
import corner

plt.ylim(-1.414, 1.614)
plt.xlim(-1.1, 4 * np.arcsinh(1) + 1.1)

# add second corner plot
corner_x = corner.x_list
corner_y = corner.y_list

def get_closest_corner_y(x):
    closest_x = min(corner_x, key=lambda a:abs(a-x))
    
    # if closes is further than 0.05 from x, return -999
    if abs(closest_x - x) > 0.05:
        return -999
    
    return corner_y[corner_x.index(closest_x)]

# shift the corner plot to the right
corner_x_shifted = [x + 1.765 for x in corner_x]

plt.plot(corner_x_shifted, corner_y, color="tab:cyan", linewidth=thickness)

plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.gca().xaxis.set_label_coords(1, -0.025)
plt.gca().yaxis.set_label_coords(-0.025, 0.98)

# plt.show()

# get the final values of x and y for the final road
final_y = {}

for x in np.arange(-1, 4 * np.arcsinh(1) + 1.1, 0.05):
    if x < 0:
        final_y[x] = -1
        continue
        
    if x > 4 * np.arcsinh(1):
        final_y[x] = -1
        continue
    
    final_y[x] = max(- np.cosh(x), -np.cosh(x - 2*np.arcsinh(1)), -np.cosh(x - 4*np.arcsinh(1)), get_closest_corner_y(x), get_closest_corner_y(x-1.765))

x = np.array(list(final_y.keys()))
y = np.array(list(final_y.values()))

plt.cla()
plt.plot(x, y, color="tab:red", linewidth=thickness)

plt.ylim(-1.414, 1.614)
plt.xlim(-1.1, 4 * np.arcsinh(1) + 1.1)
# plt.show()

# # save x and y values to a csv file
# with open('final.csv', 'w') as f:
#     f.write('x,y\n')
#     for x, y in zip(final_y.keys(), final_y.values()):
#         f.write(f'{x},{y}\n')

import create_mesh

mesh = create_mesh.create_mesh(x, y)
create_mesh.save_stl(mesh, 'final.stl')
