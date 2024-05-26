#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Function to generate Gaussian distributed random numbers using the Box-Muller transform
def box_muller_transform(num_samples):
    u1 = np.random.uniform(0, 1, num_samples)
    u2 = np.random.uniform(0, 1, num_samples)
    
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    z1 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)
    
    return z0, z1

# Generate 10,000 random numbers using Box-Muller transform
num_samples = 10000
z0, z1 = box_muller_transform(num_samples // 2)

# Combine the two sets of numbers to get the total required samples
samples = np.concatenate((z0, z1))

# Plot the histogram of the generated samples
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='Histogram of samples')

# Plot the theoretical Gaussian PDF for comparison
x = np.linspace(-4, 4, 1000)
pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, pdf, 'r-', lw=2, label='Gaussian PDF')

# Add labels and legend
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Gaussian Samples and Gaussian PDF')
plt.legend()
plt.grid()
plt.savefig("q5_plot")
# Show the plot
plt.show()


# In[ ]:




