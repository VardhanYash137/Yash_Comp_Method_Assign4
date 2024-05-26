#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import numpy as np

start_time = time.time()

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

end_time = time.time()
execution_time = end_time - start_time
print("Time taken:", execution_time, "seconds")


# In[2]:


import time

start_time = time.time()

# Generate 10,000 uniformly distributed random numbers between 0 and 1
random_numbers = np.random.rand(10000)

end_time = time.time()
execution_time = end_time - start_time
print("Time taken:", execution_time, "seconds")


# In[ ]:




