import numpy as np

m, n = 3, 4
arr = np.random.choice([0, 1], size=(m, n), p=[0.3, 0.7])
print(arr)


# create an array from 1 to 10000
arr = np.arange(1, 10001)