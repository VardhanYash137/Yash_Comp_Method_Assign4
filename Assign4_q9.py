#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def f(x):
    if x>3 and x<7:
        return 0.25
    else:
        return 0.0001

n_steps=5000
theta=1
theta_list=[]
index_accept=[]
reject_list=[]
index_reject=[]
for i in range(n_steps):
    theta_prime=np.random.standard_normal()+theta #symmetric in theta and theta_prime
    r=np.random.rand()
    if f(theta_prime)/f(theta) > r:
        theta=theta_prime
        theta_list.append(theta)
        index_accept.append(i)
    else:
        reject_list.append(theta)
        index_reject.append(i)
            

print(len(theta_list))
plt.plot(index_accept,theta_list,label="Markov Chains")
plt.scatter(index_reject,reject_list,c="red",label="Rejected",marker=".")
plt.legend()
plt.grid()
plt.xlabel("step count")
plt.ylabel("Value")
plt.savefig("q9_plot1")
plt.show()

plt.hist(theta_list,bins=20,density=True)
plt.grid()
theta_arr=np.arange(0,9,0.01)
f=np.vectorize(f)
plt.plot(theta_arr,f(theta_arr),label="Uniform pdf")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Histogram of sampled random numbers")
plt.xlim([0,9])
plt.savefig("q9_plot2")
plt.show()


# In[ ]:




