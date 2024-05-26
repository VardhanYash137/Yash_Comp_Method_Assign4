#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# Generate 10,000 uniformly distributed random numbers between 0 and 1
random_numbers = np.random.rand(10000)

# Plotting the histogram
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g')

# Plotting the uniform PDF
x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), color='r')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Random Numbers')
plt.legend(['Uniform PDF', 'Generated Data'])
plt.grid(True)
plt.savefig("plot_q2")
plt.show()


# In[ ]:




