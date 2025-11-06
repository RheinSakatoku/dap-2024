import numpy as np

z = np.arange(25).reshape(5,5)
print(z)

z[[0, 1]] = z[[1, 0]]
print(z)