#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

mu=0.5

def exp_fn(x):
    return (1/mu)*np.exp(-x/mu)

def read_data_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Convert values to float if necessary
            data.append(float(line))
    return data

exp_rand_arr = read_data_file("q4_data.txt")
#print(exp_rand_arr)

# Plot the histogram of the generated random samples
plt.hist(exp_rand_arr, bins=50, density=True, alpha=0.6)

# Plot the PDF of the exponential distribution for comparison
x = np.linspace(0, np.max(exp_rand_arr),1000)
plt.plot(x,exp_fn(x), 'r-', lw=2)

plt.xlabel('x')
plt.ylabel('Density')
plt.title('Histogram of generated random samples and PDF of Exponential distribution')
plt.grid()
plt.savefig("q4_plot")
plt.show()


# In[ ]:




