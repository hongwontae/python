import numpy as np

a = np.array([
 [1,2,3],
 [4,5,6],
])

b = np.array([
 [170,60,20],
 [180,80,25],
 [175,70,23]
])

print(np.sum(a, axis=0))