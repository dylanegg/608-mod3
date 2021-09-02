#bonus.py
"""Calculate the variance and standard deviation for a set of data"""

import statistics as stats

#create list of numbers
numbers = [524, 475, 1169, 102, 136, 1138, 20, 145, 990, 533, 363, 112, 1022, 70, 87, 228, 638, 18, 1097, 1006, 156, 801, 521, 1070, 783, 817, 266, 880, 258, 472, 621, 162, 624, 1183, 705, 369, 287, 1, 795, 565, 338, 1037, 1165, 541, 1069, 603, 1180, 1116, 83, 236, 743, 522, 1167, 1027, 1066, 720, 733, 406, 467, 640, 122, 956, 815, 587, 588, 1003, 318, 579, 1196, 912, 1111, 1086, 907, 846, 625, 193, 1179, 537, 598, 1020, 1194, 1107, 909, 968, 798, 654, 1057, 398, 214, 742, 576, 779, 925, 680, 420, 423, 476, 979, 796, 572]

#Calculate population variance
print('Population Variance:', stats.pvariance(numbers))

#Calculate population standard deviation
print('Population Standard Deviation:', stats.pstdev(numbers))

#Calculate sample variance
print('Sample Variance:', stats.variance(numbers))

#Calculate sample standard deviation
print('Sample Standard Deviation:', stats.stdev(numbers))