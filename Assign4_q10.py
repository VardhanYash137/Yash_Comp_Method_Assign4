#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt

def model(params, x):
    a, b, c = params
    return a * x**2 + b * x + c

def log_likelihood(params, x, y, yerr):
    model_y = model(params, x)
    sigma2 = yerr**2
    return -0.5 * np.sum((y - model_y)**2 / sigma2 + np.log(sigma2))

def log_prior(params):
    a, b, c = params
    # Uniform priors for simplicity, modify as needed
    if -1e3 < a < 1e3 and -1e3 < b < 1e3 and -1e3 < c < 1e3:
        return 0.0
    return -np.inf

def log_posterior(params, x, y, yerr):
    lp = log_prior(params)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(params, x, y, yerr)


# Load the data from the file
data = np.loadtxt('q10_data.txt')

# Split the data into columns
index_arr = data[:, 0]
x = data[:, 1]
y = data[:,2]
yerr=data[:,3]

# Initial guess
initial = np.array([0.0, 0.0, 0.0])
ndim = len(initial)
nwalkers = 50
nsteps = 4000

# Perturb the initial guess to get starting positions for the walkers
pos = initial + 1e-4 * np.random.randn(nwalkers, ndim)

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x, y, yerr))
sampler.run_mcmc(pos, nsteps, progress=True)
samples=sampler.get_chain(discard=1000,flat=True)





# In[2]:


fig = corner.corner(samples, labels=["a", "b", "c"], truths=[0, 0, 0])
plt.savefig("q10_plot1")
plt.show()
plt.close()


# In[3]:


medians=np.median(samples,axis=0)
sigma=np.std(samples,axis=0)
 
print(f"Median values: a = {medians[0]}, b = {medians[1]}, c = {medians[2]}")
print(f"One-sigma uncertainties: a = {sigma[0]}, b = {sigma[1]}, c = {sigma[2]}")


# In[4]:


import matplotlib.pyplot as plt

fig,axs=plt.subplots(ndim,figsize=(10,7))
for i in range(ndim):
    ax=axs[i]
    ax.plot(sampler.get_chain()[:,:,i],"k")
    ax.set_ylabel(["a","b","c"][i])
axs[-1].set_xlabel("Step")
plt.savefig("q10_plot2")
plt.show()


# In[5]:


xvals=np.linspace(min(x),max(x))
best_fit = model(medians, xvals)

for a, b, c in samples[np.random.randint(len(samples), size=200)]:
    plt.plot(xvals, model([a, b, c], xvals), color='gray', alpha=0.01)

plt.errorbar(x, y,yerr,fmt=".k", label='Data')
plt.plot(xvals, best_fit,"k",label='Best-fit model')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig('q10_plot3')
plt.show()


# In[ ]:




