import numpy as np
from stl import mesh
from scipy import interpolate

def create_mesh(x, y):

    # Interpolate the curve
    f_interp = interpolate.interp1d(x, y, kind='cubic', fill_value="extrapolate")

    # Define the thickness of the mesh
    thickness = 0.1

    # Define the number of points for generating the mesh
    num_points = 100

    # Generate the mesh points
    mesh_points = []
    for i in range(num_points):
        x_val = x[0] + i * (x[-1] - x[0]) / (num_points - 1)
        y_val = f_interp(x_val)
        mesh_points.append([x_val, y_val, 0])
        mesh_points.append([x_val, y_val, thickness])

    # Convert the list of points to a numpy array
    mesh_points = np.array(mesh_points)

    # Generate the mesh faces
    faces = []
    for i in range(num_points - 1):
        # Define vertices for each face
        v0 = 2 * i
        v1 = 2 * i + 1
        v2 = 2 * (i + 1) + 1
        v3 = 2 * (i + 1)
        # Create two triangular faces
        faces.append([v0, v1, v2])
        faces.append([v0, v2, v3])

    # Convert the list of faces to a numpy array
    faces = np.array(faces)

    # Create the mesh object
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = mesh_points[f[j], :]

    return mesh_data

def save_stl(mesh_data, filename):
    mesh_data.save(filename)
