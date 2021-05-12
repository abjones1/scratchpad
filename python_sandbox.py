import numpy as np
from scipy.stats import ttest_1samp
from matplotlib import pyplot as plt

a = ([1, 2, 3, 4, 5])

mean = np.mean(a)
print(a)
print(mean)

ages = np.genfromtxt("ages.csv", delimiter=",")
#ages = ([32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22])
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tstat, pval = ttest_1samp(ages, 30)
print(pval)

#test for work laptop push

b_data = np.random.normal(6.7, 0.7, 1000)
f_data = np.random.normal(7.7, 0.3, 1000)
plt.hist(b_data, bins=30, range=(5,8.5), histtype='step', label='Brachiosaurus')
plt.hist(f_data, bins=30, range=(5,8.5), histtype='step', label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()
