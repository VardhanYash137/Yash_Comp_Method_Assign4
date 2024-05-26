#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Chat-gpt code

import matplotlib.pyplot as plt
import numpy as np

def lcrng(a, c, m, seed, n):
    """
    Linear Congruential Random Number Generator
    Parameters:
        a (int): multiplier
        c (int): increment
        m (int): modulus
        seed (int): initial seed
        n (int): number of random numbers to generate
    Returns:
        list: generated random numbers
    """
    random_numbers = []
    for _ in range(n):
        seed = (a * seed + c) % m
        random_numbers.append(seed / m)
    return random_numbers

# Parameters for LCRNG
a = 1664525
c = 1013904223
m = 2**32
seed = 123456789
n = 10000

# Generate random numbers
random_numbers = lcrng(a, c, m, seed, n)

# Plotting the histogram
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g')

# Plotting the uniform PDF
x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), color='r')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Random Numbers')
plt.legend(['Uniform PDF', 'Generated Data'])
plt.grid()
plt.savefig("q1_plot")
plt.show()


# In[ ]:




