#population-dispersion.py
"""Calculate measures of dispersion for a population"""

import statistics as stats

#define die rolls
die_rolls = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

#Calculate population variance
print('Population Variance:', stats.pvariance(die_rolls))

#Calculate population standard deviation
print('Population Standard Deviation:', stats.pstdev(die_rolls))

#Calculate sample variance
print('Sample Variance:', stats.variance(die_rolls))

#Calculate sample standard deviation
print('Sample Standard Deviation:', stats.stdev(die_rolls))