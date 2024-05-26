#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(2/np.pi)*np.exp((-x**2)/2)

def g(x):
    if x<10 and x>0:
        return 1

x_arr=np.linspace(0,10,100)
fx_arr=f(x_arr)
g=np.vectorize(g)
gx_arr=g(x_arr)

no_points=10000
x_shot=10*np.random.rand(no_points)
y_shot=1*np.random.rand(no_points)


x_inside=[]
y_inside=[]
for i in range(len(x_shot)):
    if y_shot[i]<f(x_shot[i]):
        x_inside.append(x_shot[i])
        y_inside.append(y_shot[i])
        
    
plt.plot(x_arr,gx_arr,label="g(x)")
plt.plot(x_arr,fx_arr,label="f(x)")
plt.scatter(x_shot,y_shot,label="random pts(rejected)",marker=".")
plt.scatter(x_inside,y_inside,label="random pts(in function)",marker=".")
plt.title("Shooting Pts on graph")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title("Rejection Method")
plt.savefig("q6_plot1")
plt.show()

# Plotting the histogram
plt.hist(x_inside, bins=20, color='blue', density=True)

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Random values of Erf(x)')
plt.plot(x_arr,fx_arr,c="red",label="function curve")
plt.grid()
plt.legend()
plt.savefig("q6_plot2")
# Displaying the histogram
plt.show()


# In[ ]:




