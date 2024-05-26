#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy.stats import chi2

# Determine randomness
def evaluate_randomness(chi_squared_statistic):
    if chi_squared_statistic > critical_value:
        return "not sufficiently random"
    elif chi_squared_statistic > critical_value * 0.75:
        return "almost suspect"
    elif chi_squared_statistic > critical_value * 0.5:
        return "suspect"
    else:
        return "sufficiently random"

# Observed counts for two runs
observed_counts_1 = [4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]
observed_counts_2 = [3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]

# Total observations for each run
total_observations_1 = sum(observed_counts_1)
total_observations_2 = sum(observed_counts_2)


# Probabilities for each score (from 2 to 12)
probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Expected counts for each run
expected_counts_1 = [p * total_observations_1 for p in probabilities]
expected_counts_2 = [p * total_observations_2 for p in probabilities]

# Calculate chi-squared statistic for each run
chi_squared_statistic_1 = sum((o - e) ** 2 / e for o, e in zip(observed_counts_1, expected_counts_1))
chi_squared_statistic_2 = sum((o - e) ** 2 / e for o, e in zip(observed_counts_2, expected_counts_2))

# Degrees of freedom (number of categories - 1)
degrees_of_freedom = len(probabilities) - 1

# Critical value for chi-squared distribution at significance level 0.05
critical_value = chi2.ppf(0.95, degrees_of_freedom)

# Print results
print(f"Chi-squared statistic for observed counts 1: {chi_squared_statistic_1:.2f} ({evaluate_randomness(chi_squared_statistic_1)})")
print(f"Chi-squared statistic for observed counts 2: {chi_squared_statistic_2:.2f} ({evaluate_randomness(chi_squared_statistic_2)})")


# In[ ]:




