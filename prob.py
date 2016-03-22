import matplotlib.pyplot as py
import scipy.stats as stats
import numpy as np
import collections as cl

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
# frequency
c=cl.Counter(x)
print(c)
cnt=sum(c.values())
for key, val in c.items():
    print("the frequency of number {} is: " .format(key), float(val)/cnt)

# boxplot
py.boxplot(x)
py.show()
py.savefig("boxplot")

# histogram
py.hist(x, histtype="bar")
py.show()
py.savefig("histogram")

#qq Plot
norm_data=np.random.normal(size=1000)
graph1=stats.probplot(norm_data, plot=py, dist="norm")
py.show()
py.savefig("qqplot")