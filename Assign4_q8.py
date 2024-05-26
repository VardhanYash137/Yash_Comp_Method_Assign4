#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Number of random points
num_points = 100000


# Generate random points uniformly within the unit square
points = np.random.uniform(-1, 1, size=(num_points, 2))

plt.scatter(points[:,0],points[:,1],marker=".")

selected_x_arr=[]
selected_y_arr=[]
for pt in points:
    if np.linalg.norm(pt)<=1:
        selected_x_arr.append(pt[0])
        selected_y_arr.append(pt[1])
plt.scatter(selected_x_arr,selected_y_arr,c="red",marker=".")

# Count the number of points inside the unit circle
inside_circle = np.sum(np.linalg.norm(points, axis=1) <= 1)

# Estimate the area of the circle
area_circle = inside_circle / num_points * 4  # Multiply by 4 because the unit square has area 4
plt.title("Monte Carlo Integration")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("q8_plot")
plt.show()
print("Estimated area of the unit circle:", area_circle)


# In[4]:


# Number of random points
num_points = 1000000

# Generate random points uniformly within the unit hypercube
points = np.random.uniform(-1, 1, size=(num_points, 10))

# Count the number of points inside the unit sphere
inside_sphere = np.sum(np.linalg.norm(points, axis=1) <= 1)

# Estimate the volume of the unit sphere
volume_sphere = inside_sphere / num_points * (2 ** 10)  # Multiply by 2^10 because the unit hypercube has volume 2^10

print("Estimated volume of the ten-dimensional unit sphere:", volume_sphere)


# In[ ]:




